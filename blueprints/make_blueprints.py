"""Reproducible planning only: never creates examination content."""
import collections
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
topics = json.loads((ROOT/'blueprints/syllabus.json').read_text())
config = json.loads((ROOT/'blueprints/config.json').read_text())
subjects = list(topics)[2:]
cursors = collections.Counter()
topic_order = {
 'General Aptitude': [0,4,11,13,2,6,10,14,3,9,1,5,12,15,7,8],
 'Engineering Mathematics': [0,7,10,13,1,8,11,14,2,9,12,15,3,4,5,6]
}
papers = []
for p in range(1, 101):
    rng = random.Random(config['seed'] + p)
    one = [s for s in subjects for _ in range(2)]
    one += [subjects[(p-1+i*4) % 9] for i in range(2)]
    two = [s for s in subjects for _ in range(2)]
    two += [subjects[(p-1+i) % 9] for i in range(8)]
    one += ['Engineering Mathematics'] * 5
    two += ['Engineering Mathematics'] * 4
    rng.shuffle(one)
    rng.shuffle(two)
    assignment = ['General Aptitude']*10 + one + two
    # GA stays realistic: two medium-hard two-mark items; no arbitrary hard labels.
    levels = ['Medium']*8 + ['Medium-Hard']*2
    low = ['Medium']*12 + ['Medium-Hard']*10 + ['Hard']*3
    high = ['Medium']*6 + ['Medium-Hard']*17 + ['Hard']*7
    rng.shuffle(low)
    rng.shuffle(high)
    tech_levels = low + high
    levels += tech_levels
    slots=[]
    for n,s in enumerate(assignment, 1):
        order=topic_order.get(s,list(range(len(topics[s]))))
        t=topics[s][order[cursors[s] % len(order)]]
        cursors[s]+=1
        slots.append(dict(number=n,subject=s,subtopic=t,
            marks=1 if n<=5 or 11<=n<=35 else 2,
            difficulty=levels[n-1],type=('MCQ' if s=='General Aptitude' and t in ['Verbal grammar','Vocabulary in context','Reading comprehension','Narrative sequencing','Spatial transformations','Paper folding and cutting'] else rng.choices(['MCQ','MSQ','NAT'],[5,2,3])[0])))
    papers.append(dict(paper=p,seed=config['seed']+p,slots=slots))
(ROOT/'blueprints/papers.json').write_text(json.dumps(papers,indent=2)+'\n')
rows=['# Planned topic coverage','', 'Planning only; this is not delivered question coverage.','',
      '| Subject | Subtopic | Planned questions |','|---|---|---|']
coverage=collections.Counter((q['subject'],q['subtopic']) for p in papers for q in p['slots'])
for (s,t),n in sorted(coverage.items()): rows.append(f'| {s} | {t} | {n} |')
(ROOT/'blueprints/PLANNED_COVERAGE.md').write_text('\n'.join(rows)+'\n')
