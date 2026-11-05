from pathlib import Path
import re,json,hashlib
r=Path('GATE-CS-2027-MOCK-SERIES/research/historical')
out=[]
for p in r.glob('*.txt'):
 if 'Key' in p.name or 'keys' in p.name or 'ANS' in p.name:
  t=p.read_text(encoding='utf-8'); rows=re.findall(r'^\s*(\d+)\s+\d+\s+(MCQ|MSQ|NAT)\s+(.+?)\s+([12])\s*$',t,re.M)
  if len(rows)==65:out.append({'file':p.name,'rows':65,'counts':{x:sum(q[1]==x for q in rows) for x in ['MCQ','MSQ','NAT']},'marks':sum(int(q[3]) for q in rows)})
(r/'type_counts.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
(r/'sha256.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in r.glob('*.pdf')},indent=2))
