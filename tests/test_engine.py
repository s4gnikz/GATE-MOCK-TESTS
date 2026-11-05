"""Adversarial utility tests use clearly artificial in-memory fixtures, never papers."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from common import duplicate_warnings, validate_records, render_paper, validate_rendered, write_json, reviewed_content_hash
from build import build
from validate import audit

SYLLABUS={"General Aptitude":["test"],"Engineering Mathematics":["test"],"Algorithms":["test"]}

def fixture():
    rows=[]
    for n in range(1,66):
        subject="General Aptitude" if n<=10 else "Engineering Mathematics" if n in (11,12,13,14,15,36,37,38,39) else "Algorithms"
        rows.append({"id":f"TEST-{n}","paper":1,"number":n,"subject":subject,"subtopic":"test","type":"MCQ","marks":1 if n<=5 or 11<=n<=35 else 2,"difficulty":"Medium" if n<=26 else "Medium-Hard" if n<=55 else "Hard","stem":f"Fixture sentinel {chr(0x400+n)}: deliberate non-examination text.","options":["alpha","beta","gamma","delta"],"answer":["A"],"nat":None,"solution":"Fixture proof.","option_explanations":["fixture evidence"]*4,"misconception":"Fixture only.","family":f"fixture{chr(0x400+n)}","reasoning_pattern":f"pattern{chr(0x400+n)}","structure_signature":f"shape{chr(0x400+n)}","reasoning_steps":2,"references":[],"verification":{"status":"VERIFIED","method":"fixture","independent_solution":"fixture","evidence":"fixture"},"validation_status":"ACCEPTED","assets":[]})
    for row in rows:
        row['id']=f"CS27-M001-Q{row['number']:03}"
        row['verification']['reviewed_content_hash']=reviewed_content_hash(row)
    return rows

class ValidationTests(unittest.TestCase):
    def test_changed_question_invalidates_review(self):
        rows=fixture()
        rows[0]['stem']+=' A material new assumption.'
        self.assertTrue(any('stale content-bound' in e for e in validate_records(rows,SYLLABUS,1)))

    def test_valid_fixture_record_structure(self):
        self.assertEqual(validate_records(fixture(),SYLLABUS,1),[])

    def test_missing_number_and_wrong_marks_fail(self):
        rows=fixture()
        rows[0]["number"]=2
        rows[35]["marks"]=1
        errors=validate_records(rows,SYLLABUS,1)
        self.assertTrue(any("Numbering" in e for e in errors))
        self.assertTrue(any("positional" in e for e in errors))
        self.assertTrue(any("100" in e for e in errors))

    def test_unsupported_syllabus_and_unverified_fail(self):
        rows=fixture()
        rows[3]["subtopic"]="Unrelated web framework"
        rows[4]["verification"]["status"]="REVIEW_REQUIRED"
        rows[5]["verification"]["evidence"]=""
        errors=validate_records(rows,SYLLABUS,1)
        self.assertTrue(any("syllabus" in e for e in errors))
        self.assertTrue(any("not independently verified" in e for e in errors))
        self.assertTrue(any("lacks evidence" in e for e in errors))

    def test_options_and_nat_precision_fail(self):
        rows=fixture()
        rows[0]["options"][1]="alpha"
        rows[1]["type"]="MSQ"
        rows[2].update(type="NAT",options=[],answer=3,nat={"min":4,"max":5,"precision":-1})
        errors=validate_records(rows,SYLLABUS,1)
        for message in ("distinct options","invalid answer set","invalid NAT answer","invalid precision"):
            self.assertTrue(any(message in e for e in errors),message)

    def test_numeric_reparameterization_is_flagged(self):
        a=fixture()[0]
        b=copy.deepcopy(a)
        a["stem"]="A cache has 16 blocks and 4 sets. Determine its associativity."
        b.update(id="OTHER",number=2,stem="A cache has 32 blocks and 8 sets. Determine its associativity.",family="different",reasoning_pattern="different",structure_signature="different")
        warnings,_=duplicate_warnings([a,b])
        self.assertTrue(any(w["reason"]=="numeric_normalized" for w in warnings))

    def test_structural_duplicate_even_with_different_wording(self):
        a,b=fixture()[:2]
        b["structure_signature"]=a["structure_signature"]
        warnings,_=duplicate_warnings([a,b])
        self.assertTrue(any(w["reason"]=="structure" for w in warnings))

    def test_answer_key_only_after_all_questions(self):
        paper,_=render_paper(fixture(),1)
        self.assertGreater(paper.index("## ANSWER KEY"),paper.index("### Q65."))
        self.assertEqual(len([line for line in paper.splitlines() if line.startswith("| ")]),66)

    def test_tampered_published_key_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            folder=root/"papers/Mock_001"
            folder.mkdir(parents=True)
            paper,solutions=render_paper(fixture(),1)
            (folder/"README.md").write_text(paper.replace("| 1 | MCQ | 1 | A |","| 1 | MCQ | 1 | B |"),encoding="utf-8")
            (folder/"SOLUTIONS.md").write_text(solutions,encoding="utf-8")
            self.assertTrue(any("canonical" in e for e in validate_rendered(fixture(),1,root)))

    def test_missing_asset_and_reasoning_depth_fail(self):
        rows=fixture()
        rows[0]["assets"]=["assets/nonexistent.png"]
        for row in rows: row["reasoning_steps"]=1
        errors=validate_records(rows,SYLLABUS,1)
        self.assertTrue(any("missing or unsafe" in e for e in errors))
        self.assertTrue(any("28 technical" in e for e in errors))

    def test_empty_bank_fails_final(self):
        with tempfile.TemporaryDirectory() as temp:
            result=audit(Path(temp),[],final=True)
            self.assertEqual(result["status"],"FAIL")
            self.assertTrue(any("6500" in x for x in result["global_issues"]))

    def test_final_cannot_skip_papers_or_rendered_checks(self):
        with tempfile.TemporaryDirectory() as temp:
            # Isolate orchestration: even a caller passing [] and rendered=False
            # must run actual document validation on all 100 paper numbers.
            with patch('validate.validate_records',side_effect=lambda *args: []), patch('validate.validate_rendered',return_value=['sentinel render failure']) as rendered:
                result=audit(Path(temp),[],final=True,rendered=False)
                self.assertEqual(rendered.call_count,100)
                self.assertEqual(len(result['papers']),100)
                self.assertEqual(result['status'],'FAIL')

    def test_build_rejects_unverified_before_publishing(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            rows=fixture()
            rows[0]["validation_status"]="REVIEW_REQUIRED"
            write_json(root/"blueprints/syllabus.json",SYLLABUS)
            (root/"data").mkdir()
            (root/"data/questions.jsonl").write_text("\n".join(json.dumps(r) for r in rows),encoding="utf-8")
            with self.assertRaises(ValueError): build([1],root)
            self.assertFalse((root/"papers/Mock_001/README.md").exists())

if __name__=="__main__": unittest.main()
