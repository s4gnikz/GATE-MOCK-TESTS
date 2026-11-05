import urllib.request, re, pathlib, concurrent.futures
from pypdf import PdfReader
root=pathlib.Path('GATE-CS-2027-MOCK-SERIES/research/historical')
base='https://gate2026.iitg.ac.in/'
urls=[]
for page in ['download.html','QPs-answer-keys.html']:
 s=urllib.request.urlopen(base+page, timeout=30).read().decode()
 for href in re.findall(r'href=["\']([^"\']+)', s):
  if '.pdf' in href.lower() and re.search(r'/cs[^/]*\.pdf',href,re.I): urls.append(base+href.lstrip('/') if not href.startswith('http') else href)
def get(u):
 try:
  p=root/(u.replace(base+'doc/download/','').replace('/','_'))
  if not p.exists(): p.write_bytes(urllib.request.urlopen(u,timeout=60).read())
  r=PdfReader(p); text='\n'.join(f'PAGE {i+1}\n'+(pg.extract_text() or '') for i,pg in enumerate(r.pages));p.with_suffix('.txt').write_text(text,encoding='utf-8')
  return (u,len(r.pages),len(text))
 except Exception as e: return (u,str(e))
for x in concurrent.futures.ThreadPoolExecutor(max_workers=6).map(get,urls): print(x)
