"""Import actual authored questions only after a content-bound separate review.

This validates provenance consistency; it cannot replace the review itself.
"""
import argparse
import json
from datetime import datetime, timezone
from common import ROOT, read_json, write_json, load_bank, reviewed_content_hash, validate_records, duplicate_warnings

def accept(question_files,review_files,root=ROOT):
    incoming=[]
    reviews={}
    for file in question_files:
        incoming.extend(read_json(root/file,[]))
    for file in review_files:
        content=read_json(root/file,{})
        overlap=set(content)&set(reviews)
        if overlap: raise ValueError(f'Duplicate review IDs: {sorted(overlap)}')
        reviews.update(content)
    if not incoming: raise ValueError('No authored questions provided')
    if len({q['id'] for q in incoming})!=len(incoming): raise ValueError('Repeated incoming ID')
    existing=load_bank(root)
    current={q['id']:q for q in existing}
    for q in incoming:
        review=reviews.get(q['id'],{})
        if review.get('verdict') not in ('PASS','VERIFIED') or review.get('issues'):
            raise ValueError(f"{q['id']}: unresolved independent review")
        if review.get('answer')!=q['answer']:
            raise ValueError(f"{q['id']}: independent answer does not match")
        if review.get('reviewed_content_hash')!=reviewed_content_hash(q):
            raise ValueError(f"{q['id']}: review does not match current content")
        q['verification']={k:review[k] for k in ('method','independent_solution','evidence','reviewed_content_hash')}
        q['verification'].update(status='VERIFIED',review_provenance=review.get('review_provenance','Separate model review; no human review claimed.'))
        q['validation_status']='ACCEPTED'
        if q['id'] in current and current[q['id']]!=q:
            raise ValueError(f"{q['id']}: refusing to replace an accepted record; use a separately reviewed revision workflow")
        current[q['id']]=q
    combined=sorted(current.values(),key=lambda q:(q['paper'],q['number']))
    syllabus=read_json(root/'blueprints/syllabus.json',{})
    for p in sorted({q['paper'] for q in incoming}):
        errors=validate_records([q for q in combined if q['paper']==p],syllabus,p,root)
        if errors: raise ValueError('\n'.join(errors))
    duplicates,_=duplicate_warnings(combined)
    if duplicates: raise ValueError(f'Unresolved duplication candidates: {duplicates}')
    target=root/'data/questions.jsonl'
    target.parent.mkdir(exist_ok=True)
    text=''.join(json.dumps(q,ensure_ascii=False,sort_keys=True)+'\n' for q in combined)
    if target.exists() and target.read_text(encoding='utf-8')==text:
        print('Identical accepted bank preserved; no new acceptance event.')
        return
    tmp=target.with_suffix('.jsonl.tmp')
    tmp.write_text(text,encoding='utf-8')
    tmp.replace(target)
    with (root/'data/acceptance_log.jsonl').open('a',encoding='utf-8') as log:
        log.write(json.dumps({'time_utc':datetime.now(timezone.utc).isoformat(),'question_files':[str(p) for p in question_files],
            'review_files':[str(p) for p in review_files],'accepted_ids':[q['id'] for q in incoming],
            'content_hashes':{q['id']:reviewed_content_hash(q) for q in incoming}})+'\n')
    print(f'Accepted bank contains {len(combined)} actual reviewed questions.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--questions',nargs='+',required=True)
    p.add_argument('--reviews',nargs='+',required=True)
    a=p.parse_args()
    try: accept(a.questions,a.reviews)
    except (ValueError,KeyError) as e:
        print(f'Acceptance blocked: {e}')
        raise SystemExit(1)
