#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
cfg = json.loads(Path('affiliate-config.json').read_text(encoding='utf-8'))
SITE_TAG = cfg.get('amazon_tracking_id','').strip()
if not SITE_TAG:
    print('Missing amazon_tracking_id in affiliate-config.json')
    sys.exit(1)
REQ = f"tag={SITE_TAG}"
PAT = re.compile(r'href="(https?://[^"]+)"', re.I)
AMZ = re.compile(r'https?://([^/]*amazon\.com)/', re.I)  # US-only policy
bad=[]
for f in Path('.').glob('*.html'):
    txt=f.read_text(encoding='utf-8', errors='ignore')
    for u in PAT.findall(txt):
        if AMZ.search(u) and REQ not in u:
            bad.append((str(f),u))
if bad:
    print(f'Found Amazon links missing required tag {SITE_TAG}:')
    for f,u in bad: print(f'- {f}: {u}')
    sys.exit(1)
print(f'Amazon link tag validation passed for {SITE_TAG}.')
