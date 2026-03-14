#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs
cfg = json.loads(Path('affiliate-config.json').read_text(encoding='utf-8'))
SITE_TAG = cfg.get('amazon_tracking_id','').strip()
if not SITE_TAG:
    print('Missing amazon_tracking_id in affiliate-config.json')
    sys.exit(1)
PAT = re.compile(r'href="(https?://[^"]+)"', re.I)
AMZ = re.compile(r'https?://([^/]*amazon\.com)/', re.I)  # US-only policy
bad=[]
for f in Path('.').glob('*.html'):
    txt=f.read_text(encoding='utf-8', errors='ignore')
    for u in PAT.findall(txt):
        if not AMZ.search(u):
            continue
        q=parse_qs(urlparse(u).query)
        tag=(q.get('tag') or [''])[0]
        if tag != SITE_TAG:
            bad.append((str(f),u,tag))
if bad:
    print(f'Found amazon.com links with wrong/missing tag (required: {SITE_TAG}):')
    for f,u,t in bad:
        print(f'- {f}: tag={t or "<missing>"} :: {u}')
    sys.exit(1)
print(f'Amazon link tag validation passed for {SITE_TAG}.')
