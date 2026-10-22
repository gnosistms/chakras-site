#!/usr/bin/env python3
"""Refresh the existing public site from Spaces; no credentials are required."""
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://gnosiswebtools.sgp1.cdn.digitaloceanspaces.com/'
objects = json.loads((ROOT / 'objects.json').read_text())
paths = [item['key'] for item in objects] + ['3d', 'where', 'donde', 'dau']

def download(key):
    target = ROOT / 'public' / (key if key.startswith('chakras/') else key + '/index.html')
    target.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(ORIGIN + key, timeout=60) as response:
        data = response.read()
        assert response.status == 200
        if key in ('3d', 'where', 'donde', 'dau'):
            assert 'text/html' in response.headers['Content-Type']
    target.write_bytes(data)
    return {'path': str(target.relative_to(ROOT / 'public')), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

with ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(download, paths))
(ROOT / 'public/index.html').write_bytes((ROOT / 'public/3d/index.html').read_bytes())
(ROOT / 'snapshot.json').write_text(json.dumps(records, indent=2) + '\n')
print(f'Downloaded {len(records)} public files ({sum(r["bytes"] for r in records):,} bytes)')
