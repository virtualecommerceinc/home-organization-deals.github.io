#!/usr/bin/env python3
import re, sys
from pathlib import Path
TAG = "tag=virtualecomme-20"
PAT = re.compile(r'href="(https?://[^"]+)"', re.I)
AMZ = re.compile(r'https?://([^/]*amazon\.[^/]+|amzn\.to)/', re.I)
bad=[]
for f in Path('.').glob('*.html'):
    txt=f.read_text(encoding='utf-8', errors='ignore')
    for u in PAT.findall(txt):
        if AMZ.search(u) and TAG not in u:
            bad.append((str(f),u))
if bad:
    print('Found Amazon links without required tag:')
    for f,u in bad: print(f'- {f}: {u}')
    sys.exit(1)
print('Amazon link tag validation passed.')
