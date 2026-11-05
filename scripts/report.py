"""Create honest full-series status, coverage matrix and navigable local index."""
import csv
from collections import Counter
from common import ROOT, load_bank, read_json
from validate import audit

def report(root=ROOT):
    result=audit(root,list(range(1,101)),final=True)
    bank=load_bank(root)
    syllabus=read_json(root/"blueprints/syllabus.json",{})
    reports=root/"reports"
    released=[]
    for number,row in result["papers"].items():
        if row["status"]=="PASS" and not result["duplicate_warnings"]: released.append(int(number))
    index=["# GATE CS 2027 — Full-Length Mock Series","",f"**Validated complete papers: {len(released)}/100. Canonical questions: {len(bank)}/6,500. Final release: {result['status']}.**","","Research and review limitations are recorded in [Sources](research/SOURCES.md) and the [validation report](reports/FINAL_VALIDATION_REPORT.md).","","| Mock | Difficulty | Questions | Marks | Validation | Paper | Solutions |","|---|---|---|---|---|---|---|"]
    for n in range(1,101):
        row=result["papers"][str(n)]
        folder=root/"papers"/f"Mock_{n:03}"
        links=[f"[{label}](papers/Mock_{n:03}/{file})" if (folder/file).is_file() else "—" for label,file in (("Questions","README.md"),("Solutions","SOLUTIONS.md"))]
        state="VALIDATED" if n in released else "DRAFT / FAILED" if row["questions"] else "PLANNED"
        index.append(f"| {n:03} | Medium to Hard (target) | {row['questions']} | {sum(row['subject_marks'].values())} | {state} | {' | '.join(links)} |")
    index += ["","[Subject and subtopic coverage](reports/COVERAGE.md) · [Machine-readable coverage matrix](reports/coverage.csv)","","[Pilot quality report](reports/PILOT_001_REVIEW.md) · [Resume checkpoint](CHECKPOINT.md)","","## Local workflow","","Python 3.10+; no API keys or model calls are required by the publishing engine. Questions must first be authored and independently verified in `data/questions.jsonl`.","","```text","python scripts/build.py --paper 1 --resume","python scripts/build.py --start 2 --end 10 --resume","python scripts/validate.py --paper 1","python scripts/validate.py --final","python scripts/report.py","python -m unittest discover -s tests -v","```","","Optional printable HTML: `python scripts/export.py --paper 1` (requires `markdown-it-py==3.0.0`). Open the exported HTML in a browser and use Print / Save as PDF. Markdown remains primary; no web server is required.","","Build and validation fail on incomplete or unverified content. Resume preserves identical publications and refuses to overwrite differing files. A failed final audit remains failed until all 100 complete papers and 6,500 accepted records satisfy its checks.",""]
    (root/"INDEX.md").write_text("\n".join(index),encoding="utf-8")
    coverage=["# Subject and Subtopic Coverage","","Actual authored records are counted below; zero means not yet covered.","","| Subject | Subtopic | Questions | Marks | Papers |","|---|---|---|---|---|"]
    with (reports/"coverage.csv").open("w",newline="",encoding="utf-8") as handle:
        writer=csv.writer(handle)
        writer.writerow(["subject","subtopic"]+[f"Mock_{i:03}" for i in range(1,101)])
        for subject,topics in syllabus.items():
            for topic in topics:
                qs=[q for q in bank if q.get("subject")==subject and q.get("subtopic")==topic]
                counts=Counter(q["paper"] for q in qs)
                writer.writerow([subject,topic]+[counts[i] for i in range(1,101)])
                coverage.append(f"| {subject} | {topic} | {len(qs)} | {sum(q['marks'] for q in qs)} | {len(counts)} |")
    (reports/"COVERAGE.md").write_text("\n".join(coverage)+"\n",encoding="utf-8")
    lines=["# Final Validation Report","",f"**Final release: {result['status']}. Complete validated papers: {len(released)}/100.**","",f"Canonical records: {len(bank)} / 6,500. Unique IDs: {result['unique_ids']}. Unresolved duplicate warnings: {len(result['duplicate_warnings'])}.","","## Global findings",""]
    lines += [f"- {issue}" for issue in result["global_issues"]] or ["- No global structural findings."]
    lines += ["","## Verification limitations",""]+[f"- {s}" for s in result["review_limitations"]]
    lines += ["- Official-source availability and syllabus authority must be checked against research/SOURCES.md before final release.","","## Paper audit","","| Paper | Questions | Status | Medium / Medium-Hard / Hard | Errors |","|---|---|---|---|---|"]
    for n,row in result["papers"].items():
        d=row["difficulty"]
        lines.append(f"| {int(n):03} | {row['questions']} | {row['status']} | {d.get('Medium',0)} / {d.get('Medium-Hard',0)} / {d.get('Hard',0)} | {len(row['errors'])} |")
    lines += ["","Full error details: [validation.json](validation.json). Topic detail: [COVERAGE.md](COVERAGE.md).","","A structural PASS certifies the implemented mechanical checks only. It does not certify human review or mathematical correctness independently of supplied verification evidence.",""]
    (reports/"FINAL_VALIDATION_REPORT.md").write_text("\n".join(lines),encoding="utf-8")
    return result

if __name__=="__main__":
    result=report()
    print(f"Reports written; final release {result['status']}")
