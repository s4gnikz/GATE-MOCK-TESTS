"""Optional offline HTML export for reading and browser Print / Save as PDF.

Install markdown-it-py==3.0.0 (or use the isolated .runtime directory).
Markdown remains the canonical source. This script does not generate new content.
"""
import argparse
import html
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.runtime'))
STYLE='''
body { color:#17191c; background:white; font:16px/1.6 system-ui,Segoe UI,sans-serif;
       max-width:780px; margin:40px auto; padding:0 28px; }
h1 {font-size:28px; line-height:1.25;} h2 {font-size:22px; margin-top:36px;}
h3 {font-size:18px; margin-top:32px; break-after:avoid;}
pre,code {font-family:Consolas,monospace; font-size:14px;}
pre {padding:14px; background:#f5f5f5; white-space:pre-wrap; overflow-wrap:anywhere; break-inside:avoid;}
table {border-collapse:collapse; width:100%; font-size:14px; break-inside:avoid;}
td,th {padding:6px 9px; border:1px solid #cbd0d5; text-align:left;}
th {background:#f5f5f5;} img {max-width:100%;} p {orphans:3; widows:3;}
a {color:#174fa1;} hr {border:0; border-top:1px solid #cbd0d5; margin:32px 0;}
@page {size:A4; margin:16mm;}
@media print {body {font-size:10.5pt; margin:0; padding:0; max-width:none;}
h1{font-size:20pt} h2{font-size:16pt} h3{font-size:12pt} pre,code,table{font-size:9pt}}
'''
def export(paper,root=ROOT):
    try:
        from markdown_it import MarkdownIt
    except ImportError as e:
        raise SystemExit('Optional export dependency missing: python -m pip install markdown-it-py==3.0.0') from e
    from validate import audit
    result=audit(root,[paper])
    if result['status']!='PASS': raise SystemExit('Export blocked: paper validation failed')
    md=MarkdownIt('commonmark',{'html':False}).enable('table')
    folder=root/'reports/rendered'/f'Mock_{paper:03}'
    folder.mkdir(parents=True,exist_ok=True)
    for filename in ('README.md','SOLUTIONS.md'):
        source=root/'papers'/f'Mock_{paper:03}'/filename
        # Current pilot has no image assets. Future papers must keep resources portable.
        import shutil
        assets=source.parent/'assets'
        if assets.exists(): shutil.copytree(assets,folder/'assets',dirs_exist_ok=True)
        body=md.render(source.read_text(encoding='utf-8'))
        document=f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Mock {paper:03} — {html.escape(filename)}</title><style>{STYLE}</style><body>{body}</body></html>'
        target=folder/source.with_suffix('.html').name
        target.write_text(document,encoding='utf-8')
        print(target)
    return folder
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--paper',type=int,required=True)
    export(p.parse_args().paper)
