"""Archive the two authoritative syllabus PDFs without changing topic labels."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen
ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'research/official_2027'
folder.mkdir(exist_ok=True)
manifest=[]
for code in ('CS','GA'):
    url=f'https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/{code}_GATE2027_Syllabus.pdf'
    target=folder/f'{code}_GATE2027_Syllabus.pdf'
    entry={'url':url,'checked_date':'2026-10-12','timezone':'Asia/Calcutta'}
    try:
        data=target.read_bytes() if target.exists() else urlopen(url,timeout=25).read()
        if not data.startswith(b'%PDF'): raise ValueError('Response is not a PDF')
        target.write_bytes(data)
        entry.update(status='SAVED',file=str(target.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        entry.update(status='FETCH_FAILED',error=str(exc))
    manifest.append(entry)
(folder/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
