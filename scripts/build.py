"""Publish authored, independently reviewed records; never synthesize questions."""
import argparse
from pathlib import Path
from common import ROOT, load_bank, render_paper, validate_rendered
from validate import audit

def build(papers,root=ROOT):
    review=audit(root,papers,rendered=False)
    if review["status"]!="PASS":
        raise ValueError("Publication blocked: see reports/validation.json")
    bank=load_bank(root)
    for paper in papers:
        qs=[q for q in bank if q.get("paper")==paper]
        folder=root/"papers"/f"Mock_{paper:03}"
        outputs=list(zip(("README.md","SOLUTIONS.md"),render_paper(qs,paper)))
        # Inspect both files before any write, preserving previously released content.
        for name,content in outputs:
            path=folder/name
            if path.exists() and path.read_text(encoding="utf-8")!=content:
                raise ValueError(f"Refusing to overwrite differing completed content: {path}")
        folder.mkdir(parents=True,exist_ok=True)
        (folder/"assets").mkdir(exist_ok=True)
        for name,content in outputs:
            path=folder/name
            if not path.exists():
                temp=path.with_suffix(".tmp")
                temp.write_text(content,encoding="utf-8")
                temp.replace(path)
        errors=validate_rendered(qs,paper,root)
        if errors: raise ValueError("; ".join(errors))
        review=audit(root,[paper],rendered=True)
        if review["status"]!="PASS": raise ValueError("Post-publication validation failed")
    return audit(root,papers,rendered=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--paper",type=int)
    p.add_argument("--start",type=int,default=1)
    p.add_argument("--end",type=int,default=100)
    p.add_argument("--resume",action="store_true",help="Idempotent by default; identical published files are preserved")
    a=p.parse_args()
    papers=[a.paper] if a.paper else list(range(a.start,a.end+1))
    if not papers or min(papers)<1 or max(papers)>100: p.error("Paper range must be 1–100")
    try:
        result=build(papers)
    except ValueError as error:
        print(error)
        raise SystemExit(1)
    print(f"{result['status']}: {len(papers)} complete paper(s) published")

if __name__=="__main__": main()
