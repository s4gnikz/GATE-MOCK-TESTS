import urllib.request,re,pathlib,concurrent.futures
from pypdf import PdfReader
base='https://gate.iitk.ac.in/GATE2023/'
s=urllib.request.urlopen(base+'download_info.html').read().decode()
urls=[base+h for h in re.findall(r'href=["\']([^"\']+)',s) if re.search(r'/201[5-8]/cs',h,re.I)]
root=pathlib.Path('GATE-CS-2027-MOCK-SERIES/research/historical')
def get(u):
 try:
  p=root/('IITK_'+u.split('/')[-1]);p.write_bytes(urllib.request.urlopen(u,timeout=45).read()); r=PdfReader(p);p.with_suffix('.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+(x.extract_text() or '') for i,x in enumerate(r.pages)),encoding='utf-8');return u,len(r.pages)
 except Exception as e:return u,str(e)
for x in concurrent.futures.ThreadPoolExecutor(max_workers=4).map(get,urls):print(x)
