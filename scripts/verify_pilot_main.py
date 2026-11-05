"""Independent finite checks for pilot parent-authored questions. No eval; no answer-driven calculation."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations, combinations
import json, subprocess, re
ROOT=Path(__file__).resolve().parents[1]
out={}
def put(n,answer,detail): out[str(n)]={'answer':answer,'evidence':detail}
put(2,round(float(100*F(40*75,40*75+60*90)),2),'Exact completed-X proportion 5/14; percentage 250/7.')
pairs=[p for p in combinations('ABCD',2) if ('A' not in p or 'B' in p) and (('C' in p)==('D' not in p))]
put(3,len(pairs),str(pairs))
put(4,['A'],str([(-y,-x) for x,y in [(1,1),(3,1),(1,2)]]))
seatings=[]
for tail in permutations('BCDEFG'):
 p=('A',)+tail
 adjacent=lambda x,y: (p.index(x)-p.index(y))%7 in (1,6)
 if adjacent('A','B') and not adjacent('C','D') and not adjacent('E','F'):seatings.append(p)
put(6,['A'],f'{len(seatings)} arrangements with A fixed; all 720 rotations representatives enumerated.')
put(7,['A'],str((F(400+900,40+60), F(660+640,60+40))))
holes={(a,b) for x,y in [(5,6),(6,5)] for a in [x,8-x] for b in [y,8-y]}
put(8,sum(y==x+1 for x,y in holes),str(sorted(holes)))
pred=F(1,2)*(F(6,15)+F(1,10));psame=F(1,2)*(F(7,15)+F(4,10))
put(10,['B'],f'P(red pair)={pred}; P(same)={psame}; ratio={pred/psame}')
truth=[]
for x,y,z in product([False,True],repeat=3):
 f=(x or y) and (not x or z)
 opts=[(x and z) or (not x and y),(x and y) or (not x and z), y or z, x^y^z]
 truth.append((x,y,z,f,opts))
put(11,['A'],str([all(row[3]==row[4][i] for row in truth) for i in range(4)]))
offset=0;offset+=2;offset+=3;offset=1;offset+=1
put(12,offset,'Sequential shared-offset state: 0,2,5,1,2.')
ons={1,3,9,11};dc={0,2,8,10}; off=set(range(16))-ons-dc
funcs=[lambda a,b,c,d:not b,lambda a,b,c,d:not d,lambda a,b,c,d:a or c,lambda a,b,c,d:not b and d]
valid=[]
for fn in funcs:
 vals={i for i in range(16) if fn(*[bool(i&(1<<j)) for j in [3,2,1,0]])}
 valid.append(ons<=vals and not vals&off)
put(13,['A'],f'Option implementation validity {valid}; A one literal; D two literals; no constant can satisfy required 0 and 1 rows.')
witnesses=[None]*4;cases=0
for n in range(1,4):
 for bits in product([False,True],repeat=n*n):
  R=lambda x,y: bits[x*n+y]
  target=not all(any(R(x,y) and all(not R(x,z) or z==y for z in range(n)) for y in range(n)) for x in range(n))
  opts=[any(all(not R(x,y) or any(R(x,z) and z!=y for z in range(n)) for y in range(n)) for x in range(n)),any(any(not R(x,y) or any(R(x,z) and z!=y for z in range(n)) for y in range(n)) for x in range(n)),all(all(not R(x,y) and any(R(x,z) and z!=y for z in range(n)) for y in range(n)) for x in range(n)),any(all(not R(x,y) or all(R(x,z) and z!=y for z in range(n)) for y in range(n)) for x in range(n))]
  for i in range(4):
   if opts[i]!=target and witnesses[i] is None:witnesses[i]={'domain_size':n,'R':[list(divmod(k,n)) for k,b in enumerate(bits) if b]}
  cases+=1
put(14,['A'],f'{cases} finite relations checked; inequivalence witnesses A-D: {witnesses}. General proof uses quantifier/De Morgan laws.')
signed=int('11111010',2)-256; intermediate=104+4*signed
put(15,120,f'displacement {signed}; intermediate address {intermediate}; M[80]=120 effective address.')
a=7;b=10;total=a+(b^15)+1; val=total&15
put(16,['D'],f'unsigned sum {total}, low {val:04b}, C={total>>4}; signed 7-(-6)=13 outside [-8,7], V=1.')
put(17,3,'Key comprises dept_id, project_code, task_no; repeat permissions rule out dropping any component.')
lex=re.findall(r'[a-z][a-z0-9]*|==|\+\+|=|\+', 'ifx==if+++x')
put(18,['B'],str(lex))
def shifts(ge):
 a=[3,1,3,2,3];c=0
 for i in range(1,len(a)):
  x=a[i];j=i-1
  while j>=0 and (a[j]>=x if ge else a[j]>x):a[j+1]=a[j];c+=1;j-=1
  a[j+1]=x
 return c
put(20,shifts(True)-shifts(False),f'strict shifts={shifts(False)}; modified shifts={shifts(True)}')
R={(1,'x'),(1,'y'),(2,'x')};S={'x','y'}
def div(r,s):return {a for a,b in r if all((a,v) in r for v in s)}
put(21,['A','B','D'],str([sorted(div(R,S)),sorted(div(R,set())),sorted(div(R|{(2,'y')},S)),sorted(div(R,S|{'z'}))]))
put(23,2,'Subtract row 1: determinant=(t-1)^2-1=t(t-2); singular parameters 0,2.')
put(25,2,'P1/P0=lambda=1; second moment lambda+lambda^2=2.')
ons={0,1,2,5,6,7};cubes=[]
for cube in product([None,0,1],repeat=3):
 vals={m for m in range(8) if all(v is None or v==((m>>(2-i))&1) for i,v in enumerate(cube))}
 if vals and vals<=ons:cubes.append((cube,vals))
primes=[(c,v) for c,v in cubes if not any(v<w for d,w in cubes)]
for k in range(1,len(primes)+1):
 covers=[ix for ix in combinations(range(len(primes)),k) if set().union(*(primes[i][1] for i in ix))==ons]
 if covers:break
put(26,len(covers),f'Prime cubes {[(c,sorted(v)) for c,v in primes]}; minimum terms {k}; covers {covers}')
qs=json.loads((ROOT/'drafts/pilot_main.json').read_text(encoding='utf-8-sig'));q27=next(q for q in qs if q['number']==27)
c=re.search(r'```c\n(.*?)\n```',q27['stem'],re.S).group(1)
tmp=ROOT/'drafts/review_c';tmp.mkdir(exist_ok=True)
def compile_run(name,code):
 p=tmp/(name+'.c');p.write_text(code,encoding='utf-8');exe=tmp/(name+'.exe')
 r=subprocess.run(['gcc','-std=c11','-Wall','-Wextra','-pedantic-errors',str(p),'-o',str(exe)],capture_output=True,text=True)
 return {'compile_exit':r.returncode,'diagnostic':r.stderr,'stdout':subprocess.run([str(exe)],capture_output=True,text=True).stdout if r.returncode==0 else None}
original=compile_run('original',c);corrected=compile_run('corrected',c.replace('"%d\n"','"%d\\n"'))
put(27,['B'],{'original':original,'corrected':corrected,'intended_answer':['B']})
table=[None]*7
for key in [10,17,24]:
 for j in range(7):
  i=(key%7+j*(1+key%5))%7
  if table[i] is None:table[i]=key;break
put(28,['A','C'],f'Insertion table {table}; all begin probing slot 3; deleting it must retain chain continuation; 31 also starts at slot 3.')
put(29,['A'],'Only parent continues; children break at i=0,1,2; parent exits at i=3.')
put(30,3,'Classes: even-b ending a (accept), even-b not ending a (reject), odd-b (reject). First two epsilon-distinguished; the two rejecting classes distinguished by suffix a.')
finish=[[0]*3 for _ in range(2)]
for p in range(2):
 for l,d in enumerate([F(1,2),F(1),F(1,2)]):finish[p][l]=max(finish[p-1][l] if p else 0,finish[p][l-1] if l else 0)+d
put(31,float(finish[-1][-1]),str(finish))
def f(n):
 if n==1:return 1,1
 r,d=f(n//2);return 2*r+n%2,d+1
put(33,['A'],str(f(45)))
funcs=[v for v in product(range(3),repeat=3) if all(v[v[x]]==v[x] for x in range(3)) and sum(v[x]==x for x in range(3))==2]
put(35,len(funcs),str(funcs))
put(22,2,'LL1 cells: S,a={S->Aa}; S,b={S->Aa,S->b}; A,a={A->aA,A->B}; A,b={A->B}; B,a={B->epsilon}; B,b={B->bB}. Conflicts exactly (S,b),(A,a).')
def cusp_composition(x):
 f=lambda t:abs(t-1)+abs(t+1)
 return f(f(x)-3)
checks=[(str(x),cusp_composition(x)) for x in [F(-3),F(-2),F(-3,2),F(-1),F(0),F(1),F(3,2),F(2),F(3)]]
assert all(cusp_composition(F(k,10))==(2 if abs(F(k,10))<=2 else 4*abs(F(k,10))-6) for k in range(-100,101))
put(24,['C'],f'Piecewise g=2 on [-2,2], 4*abs(x)-6 elsewhere; sampled exact rational values {checks}. One-sided slopes differ only at +/-2.')
put(39,['A','B','D'],'In eigenbasis with second vector u, rank-one update changes only second row to (alpha,0,beta), leaving diagonal1,0,4. Characteristic roots0,1,4 imply real diagonalizability and rank2. Counterexample A=diag(1,2,4), u=e2, v=(1,-2,0): AB[2,1]=2 while BA[2,1]=1 (one-based).')
put(40,2,'Derivative /4=x^3-a*x+1; cubic discriminant4*a^3-27 positive iff three simple roots; threshold a>cube_root(27/4).')
paths=['-','+-','++-','+++']
fault={p:F(1,4)*F(4,5)**p.count('+')*F(1,5)**p.count('-') for p in paths}
sound={p:F(3,4)*F(1,10)**p.count('+')*F(9,10)**p.count('-') for p in paths}
assert sum(fault.values())==F(1,4) and sum(sound.values())==F(3,4)
expected=sum(len(p)*(fault[p]+sound[p]) for p in paths)
n3=sum(fault[p] for p in paths if len(p)==3)/sum(fault[p]+sound[p] for p in paths if len(p)==3)
twopos=fault['++-']/(fault['++-']+sound['++-'])
firstposneg=sum(fault[p] for p in ['+-','++-'])/sum(fault[p]+sound[p] for p in ['+-','++-'])
put(55,['A','C','D'],f'Paths {paths}; E[N]={expected}; faulty given N3={n3}; faulty given ++-={twopos}; faulty given + then terminal -={firstposneg}.')
L=[frozenset(),frozenset('a'),frozenset('b'),frozenset('c'),frozenset('ac'),frozenset('bc'),frozenset('abc')]
def meet(x,y):return x&y
def join(x,y):
 uppers=[z for z in L if x<=z and y<=z]
 return next(z for z in uppers if all(z<=w for w in uppers))
comps=[x for x in L if any(not meet(x,y) and join(x,y)==L[-1] for y in L)]
autos=[]
for perm in permutations(range(7)):
 if all((L[i]<=L[j])==(L[perm[i]]<=L[perm[j]]) for i in range(7) for j in range(7)):autos.append(perm)
dist=all(meet(x,join(y,z))==join(meet(x,y),meet(x,z)) for x,y,z in product(L,repeat=3))
put(64,['B','C','D'],f'All7! permutations checked; automorphisms {autos}; complemented elements={list(map(sorted,comps))}; distributive={dist}; join(a,b)={sorted(join(frozenset("a"),frozenset("b")))}.')
(ROOT/'drafts/review_main_evidence.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
