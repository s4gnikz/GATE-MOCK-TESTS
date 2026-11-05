"""Independent reviewer computations for pilot high-mark core questions.

Not human review, and not blind review: the first source inspection exposed
author answers. Expected answers below were re-derived; computations do not
read proposed answers. This script writes a separate review, never the bank.
"""
import itertools as it
import json
import math
from pathlib import Path
import sqlite3
import hashlib
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]
checks={}

width=1; touches=0
while width<128:
    for base in range(0,128,2*width): touches+=len(range(width))
    width*=2
assert touches==448
checks[36]=f"Direct pseudocode loop simulation: {touches} touch operations."
depth=0; trace=[]
for token in 'a b + c d e * + *'.split():
    depth += -1 if token in '+*' else 1
    trace.append(depth)
assert max(trace)==4
checks[38]=f"Postfix stack simulation depths: {trace}."
a=list(range(25))
for _ in range(2027):
    for r in range(5):
        for c in range(r+1,5): a[5*r+c],a[5*c+r]=a[5*c+r],a[5*r+c]
    for r in range(5):
        for c in range(2): a[5*r+c],a[5*r+4-c]=a[5*r+4-c],a[5*r+c]
assert (a[7],a[17])==(13,11)
checks[41]=f"Full 2027-iteration array simulation: queried values {a[7]}, {a[17]}."
valid=[]
for option in range(4):
    match=True
    for a,b,c,d in it.product((0,1),repeat=4):
        terms=[(0,a&d,a&d,a|d),(0,a|d,a|d,a&d),(a&d,a&d,a&d,1),(0,0,0,a|d)]
        match &= terms[option][2*b+c]==int(a+b+c+d>=3)
    if match: valid.append('ABCD'[option])
assert valid==['A']
checks[42]=f"Exhausted all 16 inputs for each of four option circuits; matches: {valid}."
s=(0,0)
for _ in range(2027): s=(s[0]^s[1],1-s[0])
assert s==(1,1)
checks[44]=f"Simulated 2027 simultaneous state updates: {s}."
outcomes=set(); count=0
for seq in it.permutations(range(6)):
    if any(seq.index(2*t)>seq.index(2*t+1) for t in range(3)): continue
    count+=1; x=0; reg={}
    for op in seq:
        t=op//2
        if op%2==0: reg[t]=x
        else: x=2*reg[t]+1 if t==0 else reg[t]+(3 if t==1 else 5)
    outcomes.add(x)
assert len(outcomes)==12 and count==90
checks[46]=f"All {count} read-before-write schedules enumerated; final values {sorted(outcomes)}."
def remainder(e):
    while e.bit_length()>=4: e ^= 0b1011<<(e.bit_length()-4)
    return e
assert all(remainder(1<<k)!=0 for k in range(32))
assert remainder((1<<7)|1)==0 and remainder(0b1011)==0
assert all(remainder((1<<(length-1))|1|middle)!=0 for length in (2,3) for middle in range(1<<(length-1)))
checks[47]="GF(2) polynomial division: remainder(x^7+1)=0; remainder(g)=0, and g has odd Hamming weight 3. All bursts up to degree 2 are nonzero remainders. Single-bit correctness additionally follows from gcd(g,x)=1."
emps={'u':'A','v':'A','w':'B','z':'C'}
required={'A':{'p','q'},'B':{'q'},'C':set()}
done={'u':{'p','q','r'},'v':{'p','q'},'w':{'q'},'z':{'r'}}
eligible={e for e,d in emps.items() if done[e]==required[d]}
assert eligible=={'v','w'}
checks[48]=f"Set-equality computation: {sorted(eligible)}."
assert 5//2==2 and 5>2*2
checks[49]="Counterexample to B: x=2,y=5,z=0. Original increments z and is false; replacement skips increment and is true. C fails at x=0 (division undefined)."
next_node={i:i+1 for i in range(1,6)};next_node[6]=None
p=1;q=None
while p is not None and next_node[p] is not None:
    r=next_node[p];next_node[p]=next_node[r];next_node[r]=q;q=r;p=next_node[p]
def traverse(head):
    result=[]
    while head is not None: result.append(head);head=next_node[head]
    return result
assert traverse(1)==[1,3,5] and traverse(q)==[6,4,2]
checks[51]=f"Node-identity pointer simulation: head={traverse(1)}, q={traverse(q)}."
from fractions import Fraction
raw_product=Fraction((-25)*57,16)
rounded=round(raw_product)
assert raw_product==Fraction(-1425,16) and rounded==-89 and rounded%256==167
checks[52]=f"Exact Fraction arithmetic: desired signed raw value {raw_product}; ties-to-even rounds to {rounded}, byte {rounded%256}."
outputs=set()
def stacks(next_input,stack,output):
    if len(output)<=2 and output!=[3,2][:len(output)]: return
    if len(output)==6: outputs.add(tuple(output));return
    if next_input<=6 and len(stack)<3: stacks(next_input+1,stack+[next_input],output)
    if stack: stacks(next_input,stack[:-1],output+[stack[-1]])
stacks(1,[],[])
checks[53]=f"Exhaustive legal push/pop recursion with capacity 3 and required prefix: {len(outputs)} sequences, {sorted(outputs)}."
assert 1+8*(2**5-1)==249
assert sum([math.ceil(math.log2(249)),math.ceil(math.log2(6)),7,2])==20
checks[54]="Enumerative command count:1+8*(32-1)=249, needing8 bits. Other independent fields3+7+2 yield20 bits."
aliases={}
for address in range(0x8000,0x10000):
    physical=((address>>12)&3,address&0xfff)
    aliases[physical]=aliases.get(physical,0)+1
assert set(aliases.values())=={2}
assert ((0xB123>>12)&3,0xB123&0xfff)==(3,0x123)
checks[57]="Exhaustive address mapping with only A15 decoded: 16384 physical locations, each with exactly two aliases. B123 maps to bank3/offset123. Under D, 8000 and 8001 share chip and local address."
db=sqlite3.connect(':memory:')
db.execute('CREATE TABLE T(k,v)')
db.executemany('INSERT INTO T VALUES (?,?)',[(1,10),(1,None),(1,10),(2,None),(2,None),(3,5)])
result=db.execute('SELECT k,COUNT(*),COUNT(v) FROM T GROUP BY k HAVING COUNT(v)<COUNT(*) AND SUM(v)>=10').fetchall()
assert result==[(1,3,2)]
checks[58]=f"SQLite executed query with supplied rows: {result}; relevant aggregate NULL semantics agree with stated SQL rules."
allocation=[(1,0),(0,1),(1,1)];maximum=[(2,2),(1,2),(3,1)]
def safe_orders(alloc,available):
    result=[]
    for order in it.permutations(range(3)):
        work=list(available)
        for process in order:
            if any(maximum[process][r]-alloc[process][r]>work[r] for r in range(2)): break
            work=[work[r]+alloc[process][r] for r in range(2)]
        else: result.append(order)
    return result
old=safe_orders(allocation,(1,1));new=safe_orders([(1,1),allocation[1],allocation[2]],(1,0))
assert old==[(1,0,2)] and new==[]
checks[59]=f"Exhausted 6 process orders: before request {old}; after grant {new}."
old=Fraction(1)+Fraction(1,10)*(6+Fraction(1,5)*60)
penalty=Fraction(1,20)*(6+Fraction(1,5)*60)
assert old-penalty==Fraction(19,10)
checks[60]=f"Exact arithmetic: initial AMAT {old}, new residual miss cost {penalty}, strict t threshold {old-penalty}."
intervals={'A':(0,3),'B':(1,2),'C':(2,4),'D':(3,5),'E':(4,6),'F':(5,7),'G':(6,8),'H':(7,9)}
feasible=[]
for bits in it.product((0,1),repeat=8):
    chosen=[name for name,bit in zip(intervals,bits) if bit]
    ordered=sorted(chosen,key=lambda name:intervals[name][0])
    if all(intervals[x][1]<=intervals[y][0] for x,y in zip(ordered,ordered[1:])): feasible.append(chosen)
best=max(map(len,feasible));opts=[x for x in feasible if len(x)==best]
assert best==4 and len(opts)==5
checks[61]=f"All 256 subsets checked: maximum {best}, five optimum subsets {opts}."
def knapsack(items,W,down):
    D=[0]*(W+1)
    for w,v in items:
        for j in (range(W,w-1,-1) if down else range(w,W+1)): D[j]=max(D[j],D[j-w]+v)
    return D[W]
assert knapsack([(2,3)],4,False)==6 and knapsack([(2,3)],4,True)==3
checks[62]="Executed upward/downward single-item counterexample: 6 vs 3; general correctness proved using j-w<j and descending update invariant."
actions=['DELETE FROM Parent WHERE id=1','UPDATE Parent SET id=3 WHERE id=2','INSERT INTO Child VALUES (13,NULL)','UPDATE Parent SET id=2 WHERE id=1']
sql_results=[]
for action in actions:
    c=sqlite3.connect(':memory:');c.execute('PRAGMA foreign_keys=ON')
    c.executescript('CREATE TABLE Parent(id INTEGER PRIMARY KEY); CREATE TABLE Child(id INTEGER PRIMARY KEY,pid INTEGER REFERENCES Parent(id) ON DELETE SET NULL ON UPDATE CASCADE); INSERT INTO Parent VALUES (1),(2); INSERT INTO Child VALUES (10,1),(11,2),(12,NULL);')
    try:
        c.execute(action);sql_results.append({'success':True,'children':c.execute('SELECT * FROM Child ORDER BY id').fetchall()})
    except sqlite3.IntegrityError: sql_results.append({'success':False})
assert [r['success'] for r in sql_results]==[True,True,True,False]
checks[63]=f"Separate SQLite databases with FK enforcement for each operation: {sql_results}."
bits=Fraction(100_000_000)*(2*Fraction(2400,200_000_000)+Fraction(2,1_000_000))
assert math.ceil(bits/8)==325
checks[65]=f"Exact delay-rate calculation: {bits} bits, {math.ceil(bits/8)} bytes."

reviews={
36:(448,"At width w=1,2,...,64, n/(2w) blocks each contribute w operations. Each of the seven levels costs 64; 7*64=448. Bounds are exact since n is a power of two.",[]),
37:(["B"],"Each operand language is CFL. Their union is CFL by closure. Their intersection is a^n b^n c^n, not CFL. The union is nonregular: its intersection with a+b+ is a^n b^n for n>=1. A wrongly asserts CFL intersection; C wrongly asserts regular union; D wrongly denies CFL union. B alone holds.",["Quality: classic textbook closure example; originality cannot be established merely from new wording. Medium is a more plausible difficulty than Medium-Hard."]),
38:(4,"Postfix emission yields ab+cde*+*. Occupancies 1,2,1,2,3,4,3,2,1 establish peak four. Left-before-right order is explicit and removes evaluation-order ambiguity.",[]),
41:(["B"],"p[-1]=a[0] is inside the array. Updating positions one, two and three successively yields 8,16,26. The assignments do not write elements read by their own right-hand side. A uses stale previous neighbors; C gets the initial indices wrong; D fails to propagate the second update. B alone holds.",["Difficulty: three straightforward iterations suggest Medium, not Medium-Hard."]),
42:(["A"],"Zero selected ones leave at most two total ones, so I0=0. One selected one requires a=d=1, so I1=I2=ad. Two selected ones require a OR d, so I3=a+d. B fails for bc=01,a=1,d=0; C fails for bc=00,a=d=1; D fails for bc=01,a=d=1. A is correct.",[]),
43:(["B"],"C is lexically nested in A, so its static link reaches A. Its immediate caller is the second B activation, so its dynamic link reaches that activation. A confuses lexical parent with caller; C skips one lexical level and has the wrong caller; D chooses the caller's caller. B alone holds.",["Difficulty: mostly direct definitions; Medium is more appropriate. The local x declarations are extraneous."]),
44:(["C"],"Simultaneous old-state transitions are 00->01->11->00, while 10 is fixed. The initial state remains in the three-cycle. 2027 mod3=2 selects 11. A applies at mod0, B at mod1, D is unreachable; C is correct.",[]),
45:(["C"],"Original dependencies form Q waiting for R to close X, R waiting for P, P waiting for Q to close Y. Moving R's close before its wait removes the retained writer and permits Q, then P, then R to complete. A changes no dependency. B creates direct mutual process waits. D retains the original cycle and adds a Y-close dependency on P. C alone resolves the cycle.",[]),
46:(12,"Every legal execution is an order of six operations with each read preceding its paired write. Enumerating all 90 orders, updating each private read register separately, yields twelve distinct final integers: 1,3,4,5,6,7,8,9,11,12,14,17. This is an interleaving problem, not undefined C data-race semantics, because the model explicitly defines atomicity and sequential consistency.",[]),
47:(["A","B","C"],"A is true because a polynomial with nonzero constant term and degree>0 cannot divide a monomial. B is true because a burst of span<=3, after removing an x power, has degree<3. C is true since x^7+1 is divisible by g. D is false: the polynomial g itself has three flipped positions and is undetected. Thus ABC.",[]),
48:(["B"],"The biconditional means equality of done and required sets. u has extra r and fails; v has exactly p,q and passes; w has exactly q and passes; z has r despite an empty requirement and fails. A includes u; C includes z; D includes both. B alone equals {v,w}.",[]),
49:(["A","D"],"The right OR operand is evaluated iff the left conjunction fails: x=0 or x!=0 with the quotient<=2. Thus A and D hold. B fails at x=2,y=5: truncation gives quotient2 but y>2*x is true; side effects can differ. C introduces division by zero at x=0. Distinct locations and unbounded integers remove alias/overflow complications.",[]),
50:(["A","B"],"A substring spanning an a and a c must contain all p b's plus at least two endpoint symbols, contradicting length<=p; hence A. Deleting v,y removes at least one symbol from at most two blocks and leaves one block at p, so equal counts cannot remain: B. The adversarial decomposition requires all cases, not one, so C is false. No legal justification restricts both pumped pieces to a's, so D is false.",[]),
51:(["B"],"Each iteration bypasses the next even-position node and prepends it to q. The successive extracted nodes are 2,4,6, hence head retains 1,3,5 and q is 6,4,2. A neglects prepend reversal. C spuriously moves odd nodes. D describes a different partition. B is correct.",[]),
52:(167,"E7 represents raw -25 and 39 raw57. Their physical product is -1425/256; the target fixed-point raw value is -1425/16=-89.0625. Nearest integer is -89, with no tie. The eight-bit two's-complement code is 256-89=167. Answer is the unsigned raw byte, not the represented negative value.",[]),
53:(len(outputs),"The prefix 3,2 forces initial pushes1,2,3 then pops3,2, leaving stack[1] and unread4,5,6. Recursively exploring every legal subsequent push/pop under capacity3, collecting output sequences rather than action sequences, gives "+str(len(outputs))+" distinct completions. Evidence lists every sequence.",[]),
54:(["C"],"Nine source choices need4 bits; six ALU choices need3; arbitrary destination subsets need5 independent bits; 128 addresses need7; four conditions need2. Independent fields sum to21. A and B undercount required codes/enables, D exceeds the minimum; C holds.",["Difficulty/quality: direct sum of field widths; suitable as a routine one-mark item more than a substantial two-mark task."]),
56:(2,"Set1 is recognizable by direct simulation on01. Set4 is recognizable by dovetailing all binary inputs until any run reaches q. Set2 is not recognizable: construct a machine accepting string00 iff an arbitrary M(w) halts; its language is contained in{01} iff M(w) never halts, reducing nonhalting to set2. Set3 is not recognizable: on input x simulate M(w) for |x| steps; halt iff it has not halted, otherwise loop. The constructed machine is total iff M(w) never halts. Thus exactly sets1 and4 are recognizable.",[]),
57:(["A","B","C"],"Four 4KiB banks occupy 8000-BFFF; upper pattern10 enables, A13:A12 choose bank, lower12 bits offset. B123 therefore has bank3, offset123. Ignoring A14 duplicates each location at address xor4000. Rewiring local address to A12:A1 ignores A0, so adjacent addresses alias; D fails. ABC hold.",[]),
58:(["A"],"Group1 has counts3,2 and sum20 and passes. Group2 has counts2,0 but NULL sum, so its comparison is UNKNOWN and HAVING drops it. Group3 has counts1,1 and fails the first condition. A is the only result; B includes a dropped group, C invents deduplication, D omits a passing group.",[]),
59:(["C"],"Original needs are (1,2),(1,1),(2,0). Available(1,1) permits P1, after whose release P0 then P2 can complete. Tentative grant leaves available(1,0), needs(1,1),(1,1),(2,0), so no process can complete. A cannot start P0; B cannot start P2; D wrongly declares the original state unsafe. C holds.",[]),
60:(["A"],"Conditional miss cost=6+.2*60=18. Original average=1+.1*18=2.8; redesigned=t+.05*18=t+.9. Strict improvement iff t<1.9. B and D allow slower cases; C is only sufficient, not necessary (t=1.8 improves). A is necessary and sufficient.",[]),
61:(["B"],"B is feasible because its intervals meet only at endpoints, and contains four jobs. Exhaustion of all64 subsets confirms unique maximum size4. A is feasible but size2; C overlaps A,C; D overlaps D,F. B is correct.",["REVISE FOR QUALITY: the only feasible large option is obvious by inspection. Does not credibly require two meaningful technical reasoning steps for a two-mark item; add an optimization inference or replace."]),
62:(["A","C","D"],"Positive wi implies j-wi<j. Descending scan has not yet updated that lower entry for this item, maintaining previous-item recurrence: A,D true. Ascending scan can read a just-updated entry; item(2,3) yields D2=3 and D4=6 at W4: C true, B false. Zero initialization represents at-most capacity, as stated.",[]),
63:(["A","B","D"],"A follows nullable SET NULL. B updates to unused key3 and propagates. C is false since a nullable single-column FK accepts NULL without matching a parent. D is true because parent primary-key uniqueness forbids merging1 into existing2; cascade does not waive it. Independent initial states are explicitly provided.",[]),
65:(325,"One-way propagation=12us. Worst-case return disturbance bound=24us; specified detection adds2us. At100 million bits/s,26us spans2600 bits=325 bytes. Inclusive boundary explicitly allows equality; standard Ethernet minimum sizes are irrelevant to this idealized model.",[]),
}

# Independently re-solved revised stems before inspecting their answer fields.
reviews.update({
37:(["B"],"Use a DPDA stack to enforce balance/nonunderflow and finite control to reject runs of length3. To prove nonregularity, choose prefixes u_n=(aab)^n and suffixes v_n=(abb)^n. Each u_n v_n is valid without triple runs, but u_m v_n has nonzero net balance when m!=n. Infinitely many distinguishable prefixes exclude a DFA. A is false because bounded runs do not bound stack depth; C contradicts the explicit deterministic construction; D contradicts its CFL recognition. B holds.",[]),
41:(["A"],"The first swap nest transposes and the second reverses rows, a clockwise quarter turn. Period4 gives three clockwise turns for2027, equivalent to counterclockwise. New[r,c]=old[c,4-r]; indices7=(1,2) and17=(3,2) therefore retrieve original13 and11. B is the one-clockwise-turn result; C is the unchanged array; D is the half-turn result. All pointer indices stay within0..24 and swaps are sequenced. A holds.",[]),
43:(["A"],"Lexical lookup in C resolves x to A's single active local, irrespective of the caller B's shadowing declaration. B0 calls C and returns5. B1 then obtains6, returning11. B2 next obtains7, returning18. B's306 follows dynamic lookup incorrectly; C's15 ignores persistent mutation of A.x; D's66 skips A's nearer shadowing declaration and uses Main.x. A holds.",[]),
54:(["B"],"There are31 nonempty destination subsets, each compatible with8 sources, and one idle command:249 distinct codes. Thus bus encoding needs8 bits. Separate ALU6 choices needs3, address128 needs7, condition4 needs2. Total20. A19 leaves7 bus bits and cannot represent249; C21 and D25 suffice but exceed minimum. B holds.",[]),
61:(["C"],"Earliest-finish greedy produces B,C,E,G of size4; its exchange invariant proves optimal cardinality. Counting maximum subsets gives A,D,F,H; B,C,E,G; B,C,E,H; B,C,F,H; B,D,F,H. Exhaustion independently confirms all five. A understates cardinality, B undercounts maximum subsets, D overstates cardinality. C=(4,5) holds. This revision adds a substantive counting task beyond feasibility inspection.",[]),
})

def main():
    source=json.loads((ROOT/'drafts/pilot_core_high.json').read_text(encoding='utf-8-sig'))
    # Re-running a verifier cannot silently bless modified content. A reviewer
    # must explicitly re-derive and replace the review after any such change.
    prior_path=ROOT/'drafts/review_core_high.json'
    prior=json.loads(prior_path.read_text(encoding='utf-8')) if prior_path.exists() else {}
    for q in source:
        content={k:q[k] for k in ['id','stem','options','answer','nat','solution','option_explanations']}
        digest=hashlib.sha256(json.dumps(content,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
        if q['id'] in prior and prior[q['id']].get('reviewed_content_hash')!=digest:
            raise ValueError('Content changed since independent review: '+q['id']+'. Re-review required; automatic re-certification refused.')
    c_question=next(q for q in source if q['number']==41)
    c_source=c_question['stem'].split('```c\n')[1].split('```')[0]
    compiler=Path('C:/MinGW/bin/gcc.exe')
    if compiler.is_file():
        with tempfile.TemporaryDirectory() as temp:
            cpath=Path(temp)/'q41.c';exe=Path(temp)/'q41.exe'
            cpath.write_text(c_source,encoding='utf-8')
            subprocess.run([str(compiler),'-std=c11','-Wall','-Wextra',str(cpath),'-o',str(exe)],check=True,capture_output=True,text=True)
            output=subprocess.run([str(exe)],check=True,capture_output=True,text=True).stdout
            assert output=='13 11'
            checks[41]+=' Native GCC C11 compile/run independently returned: '+output+'.'
    result={}
    for q in source:
        n=q['number'];answer,solution,issues=reviews[n]
        issues=list(issues)
        if q['answer']!=answer: issues.append(f"ANSWER MISMATCH: proposed {q['answer']}, reviewer {answer}")
        content={k:q[k] for k in ['id','stem','options','answer','nat','solution','option_explanations']}
        digest=hashlib.sha256(json.dumps(content,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
        result[q['id']]={'answer':answer,'independent_solution':solution,'method':'Independent model reviewer re-derivation'+(' plus reproducible Python computation' if n in checks else ' with proof/option counterexamples'),'evidence':checks.get(n,solution),'verdict':'REVIEW_REQUIRED' if q['answer']!=answer else 'VERIFIED','issues':issues,'reviewed_content_hash':digest,'review_provenance':'Separate model reviewer; no human review. Initial source inspection exposed many author answers; not a blind review. Revisions37/41/43/54/61 were separately solved from stems/options before viewing revised answers.'}
    assert len(result)==26
    (ROOT/'drafts/review_core_high.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f"Reviewed {len(result)} questions. Programmatic checks: {len(checks)}. Q53={len(outputs)}. Five quality revisions independently rechecked.")
    for qid,r in result.items():
        for issue in r['issues']: print(qid,issue)

if __name__=='__main__': main()
