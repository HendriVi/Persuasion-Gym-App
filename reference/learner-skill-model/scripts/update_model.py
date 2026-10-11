#!/usr/bin/env python3
"""Deterministically append one AttemptEvidence object and recompute per-skill summaries.
This is a reference implementation, not a psychometric claim.
"""
import json, sys, statistics
from pathlib import Path
from datetime import datetime, timezone

CRITICAL={
 'PERSON_ACTIVATION_OVERREACH','INTENT_OVERREACH','CAUSAL_OVERREACH',
 'MEDIATION_MECHANISM_OVERREACH','FALSEHOOD_MANIPULATION_COLLAPSE',
 'MANIPULATION_FALSEHOOD_COLLAPSE','UNCERTAINTY_ERASURE','SYSTEM_LOOP_FORCED'
}

def eligible_dim(a,d):
    return a['mastery_eligible'] and d['scoreable'] and d['skill_id'] in a['skill_ids']

def dim_correct(d):
    if d['correct_binary'] is not None: return 1 if d['correct_binary'] else 0
    return 1 if d['score'] >= .8 else 0

def recompute(model, skill_id, now):
    rows=[]
    for a in model['attempts']:
        for d in a['dimensions']:
            if d['skill_id']==skill_id and d['scoreable']:
                rows.append((a,d))
    eligible=[(a,d) for a,d in rows if eligible_dim(a,d)]
    rolling=eligible[-8:]
    acc=(sum(dim_correct(d) for _,d in rolling)/len(rolling)) if rolling else None
    hce=sum(1 for a,d in eligible if d['correct_binary'] is False and d['confidence'] is not None and d['confidence']>=80)
    cal=[]
    for a,d in eligible:
        if d['correct_binary'] is not None and d['confidence'] is not None and a['confidence_captured_before_feedback']:
            p=d['confidence']/100; y=1 if d['correct_binary'] else 0
            cal.append((p-y)**2); 
    signed=[]; absolute=[]
    for a,d in eligible:
        if d['correct_binary'] is not None and d['confidence'] is not None and a['confidence_captured_before_feedback']:
            e=d['confidence']/100-(1 if d['correct_binary'] else 0); signed.append(e); absolute.append(abs(e))
    if len(cal)<8: clabel='INSUFFICIENT_DATA'
    else:
        ms=sum(signed)/len(signed); ma=sum(absolute)/len(absolute)
        if ma<=.20 and abs(ms)<=.10: clabel='WELL_CALIBRATED'
        elif ms>.10: clabel='OVERCONFIDENT_PATTERN'
        elif ms<-.10: clabel='UNDERCONFIDENT_PATTERN'
        else: clabel='MIXED'
    transfers=[(a,d) for a,d in eligible if a['transfer_level']!='NONE']
    tacc=(sum(dim_correct(d) for _,d in transfers)/len(transfers)) if transfers else None
    tcontexts={(a['domain'],a['modality']) for a,_ in transfers}
    last2=transfers[-2:]
    no_crit=None if len(last2)<2 else all(not (set(d['error_tags']) & CRITICAL) for _,d in last2)
    delays=[(a,d) for a,d in eligible if a['delayed_retrieval']]
    dates={a['timestamp'][:10] for a,_ in delays}
    latest_delay=None if not delays else bool(dim_correct(delays[-1][1]))
    contexts={}
    for a,d in eligible:
        k=f"domain:{a['domain']}"
        contexts.setdefault(k,[]).append(dim_correct(d))
    cs=[{'context_key':k,'attempts':len(v),'accuracy':sum(v)/len(v)} for k,v in sorted(contexts.items()) if len(v)>=3]
    # recurring critical error detection over latest 5 eligible opportunities
    recent5=eligible[-5:]
    open_critical=False
    for tag in CRITICAL:
        if len(recent5)>=5 and sum(tag in d['error_tags'] for _,d in recent5)>=3:
            open_critical=True
    # discrimination attempts
    discr=[(a,d) for a,d in eligible if a['training_mode']=='DISCRIMINATE']
    discr_acc=sum(dim_correct(d) for _,d in discr)/len(discr) if discr else 0
    # determine state by gates
    state='UNSEEN'
    if rows: state='INTRODUCED'
    if len(eligible)>=3 and sum(dim_correct(d) for _,d in eligible)>=2: state='RETRIEVING'
    if state in {'RETRIEVING','DISCRIMINATING','PROVISIONAL_MASTERY','TRANSFER_VERIFIED','DELAYED_VERIFIED'} and len(discr)>=2 and discr_acc>=.75:
        state='DISCRIMINATING'
    if len(eligible)>=8 and len({a['domain'] for a,_ in eligible})>=2 and acc is not None and acc>=.80 and not open_critical:
        state='PROVISIONAL_MASTERY'
    if state=='PROVISIONAL_MASTERY' and len(transfers)>=3 and len(tcontexts)>=2 and tacc is not None and tacc>=.67 and no_crit is True:
        state='TRANSFER_VERIFIED'
    if state in {'TRANSFER_VERIFIED','DELAYED_VERIFIED'} and len(delays)>=2 and len(dates)>=2 and latest_delay is True:
        state='DELAYED_VERIFIED'
    if open_critical: state='NEEDS_REPAIR'
    return {
      'skill_id':skill_id,'state':state,'state_evidence_refs':[a['attempt_id'] for a,_ in eligible[-8:]],
      'summary':{'eligible_attempts':len(eligible),'unaided_attempts':sum(a['assistance_level']=='UNAIDED' for a,_ in rows),'rolling_attempts':len(rolling),'rolling_accuracy':acc,'high_confidence_errors':hce},
      'calibration':{'n':len(cal),'label':clabel,'mean_brier':None if not cal else sum(cal)/len(cal),'mean_signed_error':None if not signed else sum(signed)/len(signed),'mean_absolute_error':None if not absolute else sum(absolute)/len(absolute)},
      'transfer':{'eligible_transfer_attempts':len(transfers),'distinct_transfer_contexts':len(tcontexts),'transfer_accuracy':tacc,'latest_two_no_critical_overclaim':no_crit},
      'delayed_retrieval':{'eligible_delayed_attempts':len(delays),'distinct_dates':len(dates),'latest_delayed_correct':latest_delay},
      'context_slices':cs,'last_updated':now
    }

def main():
    if len(sys.argv)<4:
        print('usage: update_model.py MODEL.json ATTEMPT.json OUTPUT.json',file=sys.stderr); sys.exit(2)
    mp,ap,op=map(Path,sys.argv[1:4])
    model=json.loads(mp.read_text()); attempt=json.loads(ap.read_text())
    model['attempts'].append(attempt)
    now=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    ids=set(attempt['skill_ids']) | {s['skill_id'] for s in model.get('skills',[])}
    model['skills']=[recompute(model,s,now) for s in sorted(ids)]
    model['updated_at']=now
    op.write_text(json.dumps(model,indent=2)+"\n")
if __name__=='__main__': main()
