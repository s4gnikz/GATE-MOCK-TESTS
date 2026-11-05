"""Shared fail-closed validation and deterministic Markdown rendering."""
from __future__ import annotations
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GA = "General Aptitude"
EM = "Engineering Mathematics"
LETTERS = "ABCD"
REQUIRED = {"id", "paper", "number", "subject", "subtopic", "type", "marks", "difficulty", "stem", "options", "answer", "nat", "solution", "option_explanations", "misconception", "family", "reasoning_pattern", "structure_signature", "reasoning_steps", "references", "verification", "validation_status", "assets"}

def read_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.exists() else default

def load_bank(root=ROOT):
    path = root / "data/questions.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)

def normalized(text, numbers=False):
    text = re.sub(r"\s+", " ", re.sub(r"[^\w\s.+-]", " ", text.casefold())).strip()
    return re.sub(r"\b\d+(?:\.\d+)?\b", "#", text) if numbers else text

def fingerprint(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def reviewed_content_hash(q):
    fields=('id','stem','options','answer','nat','solution','option_explanations')
    payload={k:q.get(k) for k in fields}
    return fingerprint(json.dumps(payload,sort_keys=True,ensure_ascii=False,separators=(',',':')))

def shingles(text, n=4):
    words = normalized(text, True).split()
    return {tuple(words[i:i+n]) for i in range(max(0, len(words)-n+1))}

def duplicate_warnings(questions):
    """Deterministic candidate detection; collisions block release pending redesign.

    Thresholds are heuristic, not a proof of originality. No embedding model is used.
    Inverted n-gram postings avoid exhaustive comparisons across the full bank.
    """
    warnings, registry, seen, postings, gramsets, wordsets = [], {}, {}, {}, {}, {}
    for q in sorted(questions, key=lambda q: (q.get("paper",0),q.get("number",0))):
        qid = q.get("id", "MISSING")
        text = q.get("stem", "")
        keys = [("exact", normalized(text)), ("numeric_normalized", normalized(text,True)),
                ("family_reasoning", normalized(q.get("family", "") + "|" + q.get("reasoning_pattern", ""))),
                ("structure", normalized(q.get("structure_signature", "")))]
        found = set()
        for kind, value in keys:
            key = kind + ":" + fingerprint(value)
            if key in seen:
                other = seen[key]
                warnings.append({"a":other,"b":qid,"reason":kind})
                found.add(other)
            else:
                seen[key] = qid
        grams = shingles(text)
        candidates = Counter(other for gram in grams for other in postings.get(gram, []))
        for other, common in candidates.items():
            union = len(grams) + len(gramsets[other]) - common
            score = common / union if union else 0
            if score >= .62 and other not in found:
                warnings.append({"a":other,"b":qid,"reason":"ngram_near_duplicate","score":round(score,4)})
                found.add(other)
            words=set(normalized(text,True).split())
            lexical=len(words & wordsets[other])/len(words | wordsets[other]) if words | wordsets[other] else 0
            if lexical>=.90 and score>=.20 and other not in found:
                warnings.append({"a":other,"b":qid,"reason":"lexical_near_duplicate","score":round(lexical,4)})
        for gram in grams:
            postings.setdefault(gram, []).append(qid)
        gramsets[qid] = grams
        wordsets[qid] = set(normalized(text,True).split())
        registry[qid] = {"paper":q.get("paper"),"number":q.get("number"),"text_hash":fingerprint(normalized(text)),"numeric_hash":fingerprint(normalized(text,True)),"family":q.get("family"),"reasoning_pattern":q.get("reasoning_pattern"),"structure_signature":q.get("structure_signature")}
    return warnings, registry

def numeric(x):
    return isinstance(x, (int,float)) and not isinstance(x,bool) and math.isfinite(x)

def validate_records(questions, syllabus, paper, root=ROOT):
    errors = []
    def require(condition, message):
        if not condition: errors.append(message)
    require(len(questions)==65, "Exactly 65 questions required")
    nums = [q.get("number") for q in questions]
    require(sorted(nums, key=lambda x: x if isinstance(x,int) else -1)==list(range(1,66)), "Numbering must be Q1–Q65 without gaps or repeats")
    require(len({q.get("id") for q in questions})==len(questions), "Duplicate IDs")
    marks = Counter()
    counts = Counter()
    difficulties = Counter()
    multi = 0
    for q in questions:
        label = f"Q{q.get('number','?')}"
        missing = REQUIRED-set(q)
        require(not missing, f"{label}: missing fields {sorted(missing)}")
        n, subject, mark, typ = q.get("number"),q.get("subject"),q.get("marks"),q.get("type")
        require(q.get("paper")==paper, f"{label}: wrong paper")
        require(isinstance(q.get("id"),str) and bool(q["id"].strip()),f"{label}: invalid ID")
        if isinstance(n,int):
            require(q.get('id')==f'CS27-M{paper:03}-Q{n:03}',f'{label}: ID must use deterministic paper/question encoding')
        require(subject in syllabus and q.get("subtopic") in syllabus.get(subject,[]), f"{label}: invalid syllabus topic")
        require(typ in {"MCQ","MSQ","NAT"}, f"{label}: unsupported type")
        if isinstance(n,int) and 1<=n<=65:
            expected = 1 if n<=5 or 11<=n<=35 else 2
            require(mark==expected, f"{label}: wrong positional mark allocation")
            require((subject==GA)==(n<=10),f"{label}: wrong GA section")
        require(mark in (1,2), f"{label}: invalid marks")
        if mark in (1,2):
            marks[subject]+=mark
            counts[mark]+=1
            counts[(subject,mark)]+=1
        difficulties[q.get("difficulty")]+=1
        if subject!=GA and isinstance(q.get("reasoning_steps"),int) and q["reasoning_steps"]>=2: multi+=1
        for field in ("stem","solution","misconception","family","reasoning_pattern","structure_signature"):
            require(isinstance(q.get(field),str) and bool(q[field].strip()),f"{label}: empty {field}")
        require(q.get("validation_status")=="ACCEPTED",f"{label}: not accepted")
        verification=q.get("verification",{})
        require(isinstance(verification,dict) and verification.get("status")=="VERIFIED",f"{label}: not independently verified")
        for field in ("method","independent_solution","evidence"):
            require(bool(verification.get(field)) if isinstance(verification,dict) else False,f"{label}: verification lacks {field}")
        require(isinstance(verification,dict) and verification.get('reviewed_content_hash')==reviewed_content_hash(q),f'{label}: missing or stale content-bound independent review')
        options,answer=q.get("options",[]),q.get("answer")
        if typ in ("MCQ","MSQ"):
            require(isinstance(options,list) and len(options)==4 and all(isinstance(o,str) and o.strip() for o in options) and len({normalized(o) for o in options})==4,f"{label}: four distinct options required")
            valid=isinstance(answer,list) and all(isinstance(a,str) and len(a)==1 and a in LETTERS for a in answer) and len(set(answer))==len(answer)
            require(valid and (len(answer)==1 if typ=="MCQ" else 2<=len(answer)<=4),f"{label}: invalid answer set")
            explanations=q.get("option_explanations",[])
            require(isinstance(explanations,list) and len(explanations)==4 and all(isinstance(x,str) and x.strip() for x in explanations),f"{label}: all four option explanations required")
            require(q.get("nat") is None,f"{label}: selection question has NAT metadata")
        elif typ=="NAT":
            require(options==[],f"{label}: NAT must not have options")
            nat=q.get("nat") or {}
            valid=numeric(answer) and numeric(nat.get("min")) and numeric(nat.get("max"))
            require(valid and nat["min"]<=answer<=nat["max"],f"{label}: invalid NAT answer/range")
            require(isinstance(nat.get("precision"),int) and not isinstance(nat.get("precision"),bool) and nat["precision"]>=0,f"{label}: invalid precision")
        for asset in q.get("assets",[]):
            target=(root/"papers"/f"Mock_{paper:03}"/asset).resolve()
            folder=(root/"papers"/f"Mock_{paper:03}").resolve()
            require(target.is_relative_to(folder) and target.is_file(),f"{label}: missing or unsafe asset {asset}")
    require(counts[1]==30 and counts[2]==35,"Expected 30 one-mark and 35 two-mark questions")
    require(sum(marks.values())==100,"Total marks must equal 100")
    require(marks[GA]==15 and counts[(GA,1)]+counts[(GA,2)]==10,"GA allocation must be 10 questions / 15 marks")
    require(marks[EM]==13 and counts[(EM,1)]==5 and counts[(EM,2)]==4,"Engineering Mathematics must be 5 one-mark + 4 two-mark questions")
    require(sum(v for s,v in marks.items() if s not in (GA,EM))==72,"Core CS must total 72 marks")
    for subject in syllabus:
        if subject not in (GA,EM): require(marks[subject]>0,f"Core subject absent: {subject}")
    config=read_json(root/'blueprints/config.json',{})
    minimum_multi=config.get('minimum_multistep_technical',28)
    require(multi>=minimum_multi,f"At least {minimum_multi} technical questions must require two meaningful reasoning steps")
    for difficulty,target in (("Medium",26),("Medium-Hard",29),("Hard",10)):
        low,high=config.get('difficulty_bounds',{}).get(difficulty,[target-2,target+2])
        require(low<=difficulties[difficulty]<=high,f"Difficulty {difficulty} outside configured bounds {low}–{high}")
    require(set(difficulties)<={"Medium","Medium-Hard","Hard"},"Unknown difficulty label")
    return errors

def answer_text(q):
    if q["type"]!="NAT": return ", ".join(q["answer"])
    nat=q["nat"]
    value=f"{q['answer']:.{nat['precision']}f}"
    return value + (f" (accepted: {nat['min']} to {nat['max']})" if nat["min"]!=nat["max"] else " (exact)")

def render_paper(questions,paper):
    lines=[f"# GATE CS 2027 — Full-Length Mock Test {paper:03}","","**Paper Code:** CS  ","**Duration:** 180 Minutes  ","**Maximum Marks:** 100  ","**Total Questions:** 65  ","**Difficulty:** Medium to Hard","","## General Instructions","","- Attempt all 65 questions within 180 minutes.","- MCQ: select exactly one of four options. Incorrect 1-mark MCQ: −1/3; incorrect 2-mark MCQ: −2/3.","- MSQ: select every correct option. There is no partial credit and no negative marking.","- NAT: enter a numerical answer, using the stated precision. There is no negative marking.","- Unattempted questions receive zero marks.","","---","","## Section A — General Aptitude",""]
    solutions=[f"# Worked Solutions — Mock Test {paper:03}","","Review provenance is recorded in the structured bank; no human review is claimed.",""]
    for q in sorted(questions,key=lambda q:q["number"]):
        n=q["number"]
        if n==11: lines += ["---","","## Section B — Computer Science and Engineering Mathematics",""]
        lines += [f"### Q{n}. [{q['marks']} {'Mark' if q['marks']==1 else 'Marks'}] [{q['type']}]","",q["stem"],""]
        if q["type"]=="NAT": lines += [f"**Answer format:** Numeric value; {'integer' if q['nat']['precision']==0 else str(q['nat']['precision'])+' decimal places'}.",""]
        else: lines += [f"{letter}. {option}  " for letter,option in zip(LETTERS,q["options"])]+[""]
        solutions += [f"## Q{n}","",f"**Correct answer:** {answer_text(q)}","",f"**Concept:** {q['subject']} — {q['subtopic']}","",q["solution"],""]
        if q["type"]!="NAT": solutions += [f"- **{letter}:** {why}" for letter,why in zip(LETTERS,q["option_explanations"])]+[""]
        solutions += [f"**Common misconception:** {q['misconception']}",""]
    lines += ["---","",f"## ANSWER KEY — MOCK TEST {paper:03}","","| Question | Type | Marks | Correct Answer |","|---|---|---|---|"]
    lines += [f"| {q['number']} | {q['type']} | {q['marks']} | {answer_text(q)} |" for q in sorted(questions,key=lambda q:q["number"])]
    return "\n".join(lines)+"\n","\n".join(solutions)+"\n"

def validate_rendered(questions,paper,root=ROOT):
    errors=[]
    folder=root/"papers"/f"Mock_{paper:03}"
    for name,expected in zip(("README.md","SOLUTIONS.md"),render_paper(questions,paper)):
        path=folder/name
        if not path.exists(): errors.append(f"Missing {path.relative_to(root)}"); continue
        actual=path.read_text(encoding="utf-8")
        if actual!=expected: errors.append(f"{name} differs from canonical records or template")
        if actual.count("```")%2: errors.append(f"{name}: unbalanced fenced code")
        for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)",actual):
            if "://" in link: errors.append(f"{name}: external resource not independently portable: {link}")
            elif not (folder/link).is_file(): errors.append(f"{name}: missing linked asset: {link}")
    return errors
