#!/usr/bin/env python3
"""Verify PUBLIC-SAFE canonical/reference files; never needs the restricted archive.

The original 316-member ZIP is kept offline, while the 74 safe members are imported
into reference/ and evaluation/. Any other member is deliberately excluded from Git.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'SOURCE_ARTIFACT_MANIFEST.json').read_text(encoding='utf-8'))
all_entries = manifest['source_members']
assert len(all_entries) == 316, f'Expected exact source inventory 316, got {len(all_entries)}'
public = [e for e in all_entries if e['classification'].startswith('PUBLIC_')]
errors=[]
for entry in public:
    file=root / entry['target_destination']
    if not file.is_file():
        errors.append(f'missing: {file.relative_to(root)}')
        continue
    digest=hashlib.sha256(file.read_bytes()).hexdigest()
    if digest != entry['sha256']:
        errors.append(f'checksum mismatch: {file.relative_to(root)}')
for entry in all_entries:
    if entry['classification'].startswith('PUBLIC_'):
        continue
    if (root / entry['relative_path']).exists():
        errors.append(f'restricted source path accidentally exists: {entry["relative_path"]}')
print(f'Inventory: {len(all_entries)} original files, public: {len(public)}, restricted/review: {len(all_entries)-len(public)}')
if errors:
    for err in errors: print('FAIL:',err)
    raise SystemExit(1)
print('PASS: all public imported files match ORIGINAL SHA256; restricted source files absent from expected repo paths')
