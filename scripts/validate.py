"""Validate canonical content and releases. Exit nonzero on any mandatory failure."""
import argparse
from collections import Counter
from common import ROOT, load_bank, read_json, write_json, duplicate_warnings, validate_records, validate_rendered

def audit(root=ROOT, papers=None, final=False, rendered=True):
    # Final release always checks every rendered paper, even for library callers
    # that request a narrower selection or records-only validation.
    if final:
        rendered=True
        papers=list(range(1,101))
    bank=load_bank(root)
    syllabus=read_json(root/"blueprints/syllabus.json",{})
    issues=[]
    if not syllabus: issues.append("Missing official syllabus taxonomy")
    ids=[q.get("id") for q in bank]
    if len(ids)!=len(set(ids)): issues.append("Global IDs are not unique")
    duplicates, registry=duplicate_warnings(bank)
    write_json(root/"data/uniqueness_registry.json",{"algorithm_version":1,"semantic_embeddings":"UNAVAILABLE; n-gram and signature heuristics do not prove originality","records":registry,"unresolved_warnings":duplicates})
    for warning in duplicates: issues.append(f"Unresolved duplicate warning: {warning}")
    selected=sorted(set(papers if papers is not None else [q.get("paper") for q in bank]))
    results={}
    for paper in selected:
        qs=[q for q in bank if q.get("paper")==paper]
        errors=validate_records(qs,syllabus,paper,root)
        if rendered and not errors: errors += validate_rendered(qs,paper,root)
        results[str(paper)]={"questions":len(qs),"status":"FAIL" if errors else "PASS","errors":errors,"difficulty":dict(Counter(q.get("difficulty") for q in qs)),"subject_marks":dict(Counter({s:sum(q.get("marks",0) for q in qs if q.get("subject")==s) for s in {q.get("subject") for q in qs}}))}
    if not selected: issues.append("No question records exist")
    if final:
        readiness=read_json(root/'research/release_readiness.json',{})
        for field in ('official_2027_pattern_confirmed','official_2027_cs_syllabus_confirmed','official_2027_ga_syllabus_confirmed'):
            if readiness.get(field) is not True: issues.append(f'Research authority not confirmed: {field}')
        if not readiness or readiness.get('unresolved_required_research'):
            issues.append('Required historical research remains incomplete; see research/release_readiness.json')
        if len(bank)!=6500: issues.append(f"Final release requires 6500 records; found {len(bank)}")
        if set(q.get("paper") for q in bank)!=set(range(1,101)): issues.append("Final release requires every paper 1–100")
        readmes=list((root/"papers").glob("Mock_*/README.md"))
        if len(readmes)!=100: issues.append(f"Final release requires 100 student-facing README files; found {len(readmes)}")
        accepted=sum(q.get("validation_status")=="ACCEPTED" and q.get("verification",{}).get("status")=="VERIFIED" for q in bank)
        if accepted!=6500: issues.append(f"Final release requires 6500 accepted verified records; found {accepted}")
    passed=not issues and all(v["status"]=="PASS" for v in results.values())
    result={"status":"PASS" if passed else "FAIL","mode":"FINAL" if final else "INCREMENTAL","total_records":len(bank),"unique_ids":len(set(ids)),"global_issues":issues,"papers":results,"duplicate_warnings":duplicates,"review_limitations":["Programmatic checks inspect supplied evidence and structure; they cannot establish mathematical truth from status flags.","Independent model review must be recorded explicitly; no human review is claimed.","Semantic embedding comparison unavailable; originality still requires independent reasoning-pattern review.","Markdown canonical consistency is checked. Visual export/render inspection is separately required."]}
    write_json(root/"reports/validation.json",result)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--paper",type=int)
    p.add_argument("--start",type=int)
    p.add_argument("--end",type=int)
    p.add_argument("--final",action="store_true")
    p.add_argument("--records-only",action="store_true")
    a=p.parse_args()
    if a.final and a.records_only: p.error("--final requires rendered-document validation; --records-only is incompatible")
    selected=[a.paper] if a.paper else list(range(a.start or 1,(a.end or 100)+1)) if a.start or a.end else None
    if a.final: selected=list(range(1,101))
    result=audit(papers=selected,final=a.final,rendered=not a.records_only)
    print(f"{result['status']}: {result['total_records']} records, {len(result['papers'])} papers checked")
    for issue in result["global_issues"]: print(issue)
    for paper,row in result["papers"].items():
        for issue in row["errors"]: print(f"Mock {int(paper):03}: {issue}")
    raise SystemExit(0 if result["status"]=="PASS" else 1)

if __name__=="__main__": main()
