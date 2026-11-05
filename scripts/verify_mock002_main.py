"""Independent stem-driven checks for Mock002 GA/mathematics; no eval."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations,combinations
import json
R=Path(__file__).resolve().parents[1];out={}
def put(n,a,e):out[str(n)]={'answer':a,'evidence':e}
put(1,['B'],'Context contrasts endorsement with required pilot: conditional/reserved support, not credentials or withdrawal.')
put(2,20,'8=2^3 in12h gives4h doubling time;32=2^5 takes20h.')
obs=[(1,1,1,0),(1,1,0,1),(1,0,1,1),(0,1,1,0),(0,1,0,0)]
truth=[all(fn(r,c,f)==v for r,c,f,v in obs) for fn in [lambda r,c,f:r and(c or f),lambda r,c,f:r and(c!=f),lambda r,c,f:c!=f,lambda r,c,f:r or c]]
put(3,['B'],f'Candidate consistency A-D: {truth}')
# Fix A on +z, B on -y, C on +x, then enumerate remaining labels; orientations satisfy top cross front=right.
vec=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
base={'A':vec[4],'B':vec[3],'C':vec[0]};assignments=[]
for rem in permutations([vec[1],vec[2],vec[5]]):
 d=base|dict(zip('DEF',rem))
 if all(cross(d[t],d[f])==d[r] for t,f,r in [('A','B','C'),('A','D','E'),('F','B','E')]):assignments.append(d)
put(4,['C'],f'With first orientation fixed, unique labelling {assignments}; opposite B is D.')
a=[0,2,5]
for n in range(3,6):a.append(2*a[-1]-a[-2]+n)
put(5,a[5]-a[4],f'Sequence a1..a5={a[1:]}')
put(6,['B'],'(16-2w)(10-2w)=72 implies w2-13w+22=0; roots2,11; w<=5 selects2m.')
put(7,['B'],'Past unreal conditional requires would have caught; explicit Mira subject repairs dangling participial modifier.')
milk=F(72)*F(90,120);water=F(48)*F(90,120)+30
milk=milk*F(100,120)+20;water=water*F(100,120)
put(8,['B'],f'Final milk={milk},water={water}; ratio={milk/water}')
sched=[]
for p in permutations('ABCDE'):
 ix=lambda a:p.index(a)+1
 if ix('C')==5 and ix('A')<ix('C') and abs(ix('B')-ix('D'))==2 and ix('E') not in(1,5):sched.append(p)
opts=[any(p.index('A')==3 for p in sched),all(p.index('A')<p.index('E') for p in sched),any(p.index('E')==2 for p in sched),all(p.index('B')%2==0 and p.index('D')%2==0 for p in sched)]
put(9,['A','C'],f'Schedules {sched}; A-D truths {opts}')
heights=[]
for h in product(range(3),range(4),range(2),range(3),range(3),range(2)):
 if [max(h[j],h[j+3]) for j in range(3)]==[2,3,1] and max(h[:3])==3 and max(h[3:])==2:heights.append(h)
put(10,['B'],f'Feasible stack configurations {len(heights)}; total min={min(map(sum,heights))},max={max(map(sum,heights))}')
put(22,['A','C'],'After column1 elimination lower-right block is [[t-4,1],[1,0]]. Det=-1; t4 prevents unpivoted unit-L factorization, but row swap yields nonzero pivots1,1. t5 final pivot=-1.')
put(24,0.667,f'Integral = [x-x²]0..1/3 + [x²/2]1/3..1 = {F(1,3)-F(1,9)+(1-F(1,9))/2}')
mean=F(3*2+2*7,5);var=F(3*(2+4)+2*(1+49),5)-mean**2
put(29,float(var),f'Combined mean={mean}; variance from second moments={var}')
f=lambda x:2*x%5;g=lambda x:(x+1)%5;fi=lambda x:3*x%5;gi=lambda x:(x-1)%5
h=[f(g(fi(gi(x)))) for x in range(5)];power=list(range(5));k=0
while True:
 k+=1;power=[h[x] for x in power]
 if power==list(range(5)):break
put(33,['D'],f'h={h}; order={k}')
# Connected pair of triangles with one inter-triangle bridge: required degrees, nonbipartite, no Hamiltonian cycle.
edges={(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)}
deg=[sum(v in e for e in edges) for v in range(6)]
put(35,['A','B'],f'Counterexample edges={sorted(edges)},degrees={deg}; bridge excludes Hamiltonian cycle and triangle excludes bipartiteness. Handshake7edges and exactly2 odd vertices prove A,B.')
words={p for p in product('RBG',repeat=6) if all(p.count(c)==2 for c in'RBG') and all(p[i]!=p[(i+1)%6] for i in range(6))}
canon=lambda p:min(p[i:]+p[:i] for i in range(6))
orbits={canon(p) for p in words}
put(39,len(orbits),f'Labelled legal words={len(words)}; rotation representatives={["".join(x) for x in sorted(orbits)]}; reflections not identified.')
e=[]
for n in range(13):e.append(sum(sum(w)%2==0 and all(not(w[i] and w[i+1]) for i in range(n-1)) for w in product([0,1],repeat=n)))
def coefficients(num,den,n):
 a=[]
 for k in range(n):a.append((num[k] if k<len(num) else 0)-sum(den[j]*a[k-j] for j in range(1,min(k+1,len(den)))))
 return a
series=[coefficients(*p,len(e)) for p in [([1,1],[1,-1,-1]),([1,-1,0,1],[1,-2,1,0,-1]),([1],[1,-1,-1]),([1,-1],[1,-2,1,0,-1])]]
put(40,['B'],f'Enumerated e0..12={e}; matches A-D={[a==e for a in series]}. General proof even filter half[(1+x)/(1-x-x²)+(1-x)/(1-x+x²)] gives optionB.')
witness={}
for n in range(1,4):
 for bits in product([0,1],repeat=n*n):
  rel=lambda x,y:bool(bits[x*n+y]);E=all(any(rel(x,y) for y in range(n))for x in range(n));T=all(not(rel(x,y) and rel(y,z)) or rel(x,z) for x,y,z in product(range(n),repeat=3));I=all(not rel(x,x)for x in range(n));S=all(rel(x,y)==rel(y,x)for x,y in product(range(n),repeat=2));Fun=all(sum(rel(x,y)for y in range(n))<=1 for x in range(n))
  for label,ok in zip('ABCD',[E and T and I,E and S and I and Fun,E and T and I and Fun,E and T and S]):
   if ok and label not in witness:witness[label]={'n':n,'edges':[list(divmod(i,n))for i,b in enumerate(bits)if b]}
put(44,['B','D'],f'Finite small witnesses={witness}. For all finite sizes, E yields infinite successor walk, repetition forms cycle; T then produces loop contradicting I, excluding A,C.')
# Symmetric circulant commuting with A: first row(a,b,c,b); eigenvalues a+2b+c, a-2b+c, a-c (last twice).
projectors=[]
for alt,plane in product([0,1],repeat=2):
 b=-F(alt,4);a=(F(alt,2)+plane)/2;c=(F(alt,2)-plane)/2
 rows=[[a,b,c,b],[b,a,b,c],[c,b,a,b],[b,c,b,a]]
 assert all(sum(rows[i][k]*rows[k][j]for k in range(4))==rows[i][j]for i in range(4)for j in range(4))
 assert all(sum(row)==0 for row in rows)
 projectors.append([[str(x)for x in row]for row in rows])
put(54,len(projectors),f'All four matrices={projectors}. Completeness: AX=XA implies circulant, symmetry reduces it to(a,b,c,b); row sum0 and idempotence leave independent eigenvalues alt,plane in0/1.')
(R/'drafts/review_mock002_main_evidence.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
