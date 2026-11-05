"""Specific editorial revisions after independent pilot review; no acceptance here."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'drafts/pilot_main.json'
qs=json.loads(path.read_text(encoding='utf-8'))
by={q['number']:q for q in qs}
for n in (9,11,23,29,34): by[n]['difficulty']='Medium'
for n in (14,15,27,6,22): by[n]['difficulty']='Medium-Hard'
for n in (39,55,64): by[n]['difficulty']='Hard'
q=by[6]
q['stem']='''Seven distinct people A, B, C, D, E, F and G sit around a circular table. A and B must sit next to each other. Neither C and D nor E and F may sit next to each other. Rotations of an arrangement are identical; reflections are different. How many arrangements are possible?'''
q['answer']=['A']
q['solution']='''1. With A and B adjacent, treat them as a block with two orders. There are 2(5!)=240 circular arrangements.
2. If C and D are also adjacent, there are 4(4!)=96 arrangements. The same count applies when E and F are adjacent.
3. When both forbidden adjacencies occur, three two-person blocks and G form four circular units. There are 2^3(3!)=48 arrangements.
4. Inclusion-exclusion gives 240-96-96+48=96.'''
q['option_explanations']=['This subtracts both forbidden events and restores their intersection.','This is 5!: it fixes the A-B order and ignores both forbidden adjacencies.','This enforces only one of the two forbidden adjacencies: 240-96.','This ignores both forbidden adjacencies.']
q['family']=q['reasoning_pattern']=q['structure_signature']='ga_circular_required_block_two_forbidden_blocks_inclusion_exclusion'
q['reasoning_steps']=4
q=by[22]
q.update(type='NAT',options=[],answer=2,nat={'min':2,'max':2,'precision':0},option_explanations=[],reasoning_steps=3)
q['stem']='''For the grammar below, construct the standard LL(1) predictive parsing table using FIRST and FOLLOW sets. A conflicting entry means a single table cell containing two or more distinct productions. Count conflicting cells, not pairs of productions. The start symbol is S and the end marker is $.

```text
S -> A a | b
A -> a A | B
B -> b B | epsilon
```

How many table cells conflict?'''
q['solution']='''1. FIRST(B)={b,epsilon} and FIRST(A)={a,b,epsilon}. FOLLOW(A)={a}, propagated to FOLLOW(B)={a}. FOLLOW(S)={$}.
2. S -> A a enters columns a and b, while S -> b enters b. Thus M[S,b] conflicts. A -> a A enters a; A -> B enters b and, because B is nullable, FOLLOW(A)'s a. Thus M[A,a] conflicts.
3. B -> b B enters b; B -> epsilon enters a. These do not conflict. Exactly two table cells conflict.'''
q['misconception']='Nullable productions can create conflicts through FOLLOW, separately from overlapping FIRST sets.'
q['family']=q['reasoning_pattern']=q['structure_signature']='compiler_predictive_table_two_distinct_sources_of_conflict'
q=by[24]
q['stem']='''For every real x, define f(x)=|x-1|+|x+1| and g(x)=f(f(x)-3). At exactly which points is g not differentiable?'''
q['options']=['x=-1 and x=1 only','x=-2,-1,1,2','x=-2 and x=2 only','At no real point']
q['answer']=['C']
q['solution']='''1. Set r=|x|. Then f(x)=2 for r<=1 and f(x)=2r for r>1; equivalently f(x)=2 max(1,r).
2. When r<=1, the outer argument is -1 and g=2. When 1<r<=2, the outer argument 2r-3 lies in (-1,1], so g remains 2. When r>2, that argument exceeds 1 and g=4r-6.
3. Thus g is constant on [-2,2], linear with slope -4 on x<-2 and slope 4 on x>2. Only -2 and 2 have unequal one-sided derivatives. The original corners at +/-1 disappear under the composition.'''
q['option_explanations']=['The outer function is constant across the relevant images around +/-1, so g has no corners there.','This retains the original f corners incorrectly; g is constant around +/-1.','At each of +/-2, the slope changes between zero and a nonzero value.','The slopes on the two sides of +/-2 differ.']
q['misconception']='A composition can remove a corner of the inner function; the chain rule cannot simply be applied at nondifferentiable points.'
q['family']=q['reasoning_pattern']=q['structure_signature']='em_absolute_value_composition_hides_inner_corners'
q=by[31]
q['stem']=q['stem'].replace('Packets retain their order.', 'Packets retain their order. Each link begins transmitting as soon as both the packet and that link are available.')
q=by[39]
q.update(type='MSQ',answer=['A','B','D'],reasoning_steps=4)
q['stem']='''A is a real 3x3 matrix with distinct eigenvalues 1, 2 and 4. Let u be a nonzero column vector satisfying Au=2u, and let v be a real column vector satisfying v^T u=-2. Define B=A+u v^T. Which statements hold for every such A,u,v?'''
q['options']=['Zero is an eigenvalue of B.','B is diagonalizable over the real numbers.','A and B necessarily commute.','rank(B)=2.']
q['solution']='''1. Bu=Au+u(v^T u)=2u-2u=0, so zero is an eigenvalue.
2. Choose a basis (u,w1,w4) in which Aw1=w1 and Aw4=4w4. Distinct eigenvalues ensure this is a basis. In this basis A is diag(2,1,4), and u v^T has nonzero entries only in its first row, whose first entry is -2.
3. Therefore B is upper triangular with diagonal (0,1,4). These distinct real eigenvalues make B diagonalizable, and exactly two are nonzero, so rank(B)=2.
4. Commutation need not hold. In this basis choose v^T=(-2,1,0). Then B has first row (0,1,0); AB has entry (1,2)=2, whereas BA has that entry 1. A and B do not commute.'''
q['option_explanations']=['u is a nonzero vector in the null space of B.','The three eigenvalues are 0,1,4, all distinct and real.','The explicit choice A=diag(2,1,4), u=(1,0,0)^T, v=(-2,1,0)^T is a counterexample.','Similarity to a diagonal matrix with exactly two nonzero entries gives rank two.']
q['misconception']='A rank-one change need not commute with the original matrix, even when its image is an eigenspace.'
q['family']=q['reasoning_pattern']=q['structure_signature']='em_rank_one_update_eigenspace_triangularization_commutation'
q=by[55]
q['stem']='''A component is faulty with probability 1/4. Each test is positive with probability 4/5 for a faulty component and 1/10 for a sound component. Repeated results are conditionally independent given the component's status. Testing stops at the first negative result or after three tests, whichever occurs first. N is the number of tests performed. Which statements are correct?'''
q['options']=['E[N]=577/400.','P(faulty | N=3)=512/515.','Given that exactly two positive results were observed before a negative result, the probability of a faulty component is 128/155.','Given that the first result was positive and the stopping result was negative, the probability of a faulty component is 32/65.']
q['answer']=['A','C','D']
q['solution']='''1. P(N>=2)=P(first positive)=11/40. Reaching test 3 requires the first two positives, whose probability is (1/4)(4/5)^2+(3/4)(1/10)^2=67/400. Thus E[N]=1+11/40+67/400=577/400.
2. N=3 does not disclose the third result. P(faulty | N=3)=[(1/4)(4/5)^2]/(67/400)=64/67. The value 512/515 would instead condition on three positives.
3. Exactly two positives before a negative is the path ++-. Faulty and sound weights are (1/4)(4/5)^2(1/5)=128/4000 and (3/4)(1/10)^2(9/10)=27/4000, giving posterior 128/155.
4. Positive first and negative stopping includes paths +- and ++-. With conditional positive probability p, their total probability is p(1-p)+p^2(1-p)=p-p^3. Faulty and sound weighted probabilities are 288/4000 and 297/4000. Their posterior ratio is 288/585=32/65.'''
q['option_explanations']=['The tail-sum formula uses the probabilities of reaching the second and third tests.','Reaching three tests means only that the first two were positive; the third may be negative.','This conditions on the specific path ++-, with weights 128 and 27.','The two possible terminating paths give weights 288 and 297, whose normalized faulty weight is 32/65.']
q['misconception']='The number of tests performed and the number of positives are different observations under a stopping rule.'
q['family']=q['reasoning_pattern']=q['structure_signature']='em_latent_status_stopped_test_paths_expectation_posteriors'
q['reasoning_steps']=4
q=by[64]
q['stem']='''Let L={empty set, {a}, {b}, {c}, {a,c}, {b,c}, {a,b,c}}, ordered by inclusion. Notice that {a,b} is absent. Meets and joins are taken within L. A complement of x is a y with meet(x,y)=empty set and join(x,y)={a,b,c}. An order automorphism is a bijection L->L preserving the order in both directions. Which statements are correct?'''
q['options']=['L is a distributive lattice.','Exactly six elements of L have at least one complement.','L has exactly two order automorphisms.','The join of {a} and {b} is {a,b,c}.']
q['answer']=['B','C','D']
q['solution']='''1. Intersections remain in L, so they are meets. All unions are in L except {a} union {b}; for that pair the least available upper bound is {a,b,c}. Hence L is a lattice, but joins need not equal unions.
2. Distributivity fails: {c} meet ({a} join {b})={c}, whereas ({c} meet {a}) join ({c} meet {b})=empty set.
3. Bottom and top complement one another. {a} has complements {b} and {b,c}; {b} has complements {a} and {a,c}; {a,c} and {b,c} are consequently complemented too. The remaining element {c} has no complement: the only nonempty elements disjoint from it are {a} and {b}, and their individual joins with {c} are below top. Thus six elements have complements.
4. Among the three atoms, {c} uniquely has two immediate upper covers; {a} and {b} each have one. Any automorphism must fix {c} and may only fix or swap {a},{b}. The two choices determine all other images, and both are valid. Thus there are exactly two automorphisms.'''
q['option_explanations']=['The explicit distributive-law calculation yields {c} on one side and empty set on the other.','Only {c} lacks any complement.','An automorphism fixes {c}; its only freedom is the swap of a and b.','Because {a,b} is absent, the only common upper bound for the two atoms is top.']
q['misconception']='An inclusion-ordered family can have joins different from set union, so it need not inherit Boolean distributivity.'
q['family']=q['reasoning_pattern']=q['structure_signature']='em_missing_union_lattice_complements_order_automorphisms'
q['reasoning_steps']=4
path.write_text(json.dumps(qs,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Specific pilot revisions saved; all records still require acceptance review.')
