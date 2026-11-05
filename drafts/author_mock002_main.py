"""Individually authored GA/mathematics for Mock 002; never reparameterizes the pilot."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
slots=json.loads((ROOT/'blueprints/papers.json').read_text())[1]['slots']
out=[]
def add(n,typ,stem,options,answer,solution,why,misconception,family,steps=3,precision=0,difficulty=None):
 q=dict(slots[n-1]);q.update(id=f'CS27-M002-Q{n:03}',paper=2,type=typ,stem=stem,options=options,answer=answer,
 solution=solution,option_explanations=why,misconception=misconception,family=family,reasoning_pattern=family,
 structure_signature=family,reasoning_steps=steps,references=['research/SYLLABUS_2027.md','research/GATE_PATTERN_ANALYSIS.md'],
 verification={'status':'REVIEW_REQUIRED','method':'author derivation','independent_solution':'','evidence':''},
 validation_status='REVIEW_REQUIRED',assets=[],nat={'min':answer,'max':answer,'precision':precision} if typ=='NAT' else None)
 if difficulty:q['difficulty']=difficulty
 out.append(q)

add(1,'MCQ',
'''The reviewer gave the proposal a “qualified endorsement”: she supported its objective but required a smaller pilot before implementation. In this context, “qualified” most nearly means:''',
['supported without any reservations','conditional on stated reservations','written by a certified professional','withdrawn after reconsideration'],['B'],
'''1. The reviewer supports the objective, so the endorsement is not withdrawn.
2. The requirement of a smaller pilot places a condition on that support. Here “qualified” means limited by reservations, rather than describing professional credentials.''',
['This contradicts the explicit condition.','This captures support with a limitation.','The context gives no information about credentials.','Support remains; it has not been withdrawn.'],
'A familiar word can have a contextual meaning unrelated to its usual professional use.','ga_contextual_qualified_endorsement',2)

add(2,'NAT',
'''A culture grows exponentially at a constant rate. Its population becomes eight times its initial value in 12 hours. Starting from the same initial population, after how many hours will it become 32 times its initial value?''',
[],20,
'''1. Eight is 2^3, so three doublings take 12 hours and one doubling takes 4 hours.
2. Thirty-two is 2^5, requiring five doublings. The time is 5*4=20 hours.''',[],
'Exponential growth relates elapsed time to the logarithm of the multiplication factor.','ga_exponential_growth_compare_doubling_counts',2)

add(3,'MCQ',
'''An inspector accepts or rejects cards using one of the four candidate rules below. Each card has one colour, one shape, and is either filled or hollow. Observations are:

| Colour | Shape | Appearance | Decision |
|---|---|---|---|
| Red | Circle | Filled | Reject |
| Red | Circle | Hollow | Accept |
| Red | Square | Filled | Accept |
| Blue | Circle | Filled | Reject |
| Blue | Circle | Hollow | Reject |

Which candidate rule agrees with every observation?''',
['Accept if the card is red and is either circular or filled, including when both hold.',
 'Accept if the card is red and exactly one of “circular” and “filled” holds.',
 'Accept if exactly one of “circular” and “filled” holds, regardless of colour.',
 'Accept if the card is red or circular, including when both hold.'],['B'],
'''1. The rejected red, circular, filled card excludes rules that accept both properties together: A and D.
2. The rejected blue, circular, hollow card excludes a colour-independent exclusive-or rule C.
3. B accepts precisely the two listed red cards with one of the two properties and rejects all three other rows. This selects among the stated candidates; it does not claim uniqueness among all imaginable rules.''',
['It would accept the first row.','It matches all five rows.','It would accept the final blue card.','It would accept the first, fourth and fifth rows.'],
'Observed examples select a rule only relative to a specified candidate set.','ga_candidate_rule_elimination_three_attributes')

add(4,'MCQ',
'''A cube has six distinct face labels A,B,C,D,E,F. Three valid orientations are listed as (top, front, right): (A,B,C), (A,D,E), and (F,B,E). Which face is opposite B? Rotating the cube does not change its labels.''',
['A','C','D','E'],['C'],
'''1. With A on top, the clockwise side-face order consistent with front B and right C begins B,C. The other view with the same top places D immediately before E in that order.
2. The four side labels are distinct, so their cyclic order is B,C,D,E. Opposite side pairs are B-D and C-E.
3. The third view is consistent with F opposite A and confirms the orientation without changing B's opposite.''',
['A is adjacent to B in the first view.','C is adjacent to B in the first view.','D lies two positions from B around the four side faces.','E is adjacent to B in the third view.'],
'Face adjacency and cyclic orientation together determine opposite faces.','ga_cube_three_views_opposite_face')

add(5,'NAT',
'''A numerical sequence begins a1=2 and a2=5. For every integer n>=3, its rule is a_n=2*a_(n-1)-a_(n-2)+n. What is a5-a4?''',
[],15,
'''1. Let d_n=a_n-a_(n-1). Subtracting a_(n-1) from the recurrence gives d_n=d_(n-1)+n.
2. Starting from d2=3, obtain d3=6, d4=10 and d5=15.
3. Therefore a5-a4=15. Direct terms 2,5,11,21,36 give the same result.''',[],
'A second-order sequence can become a simpler first-difference pattern.','ga_explicit_second_difference_increment_series')

add(6,'MCQ',
'''A rectangular garden is 16 m long and 10 m wide. A path of uniform width is laid inside all four edges, leaving a smaller rectangular planted region. The path occupies 88 square metres. What is the width of the path?''',
['1 m','2 m','3 m','4 m'],['B'],
'''1. If the width is x, the planted dimensions are 16-2x and 10-2x. The planted area is 160-88=72.
2. Expanding (16-2x)(10-2x)=72 gives x^2-13x+22=0, with roots 2 and 11.
3. Geometry requires 0<x<5, so only x=2 is admissible.''',
['Width 1 leaves 14*8=112 square metres planted, so the path area is 48.','Width 2 leaves 12*6=72, giving path area 88.','Width 3 leaves 10*4=40, giving path area 120.','Width 4 leaves 8*2=16, giving path area 144.'],
'A border removes its width from both ends of each dimension, and algebraic roots must meet geometric bounds.','ga_inner_border_area_root_admissibility')

add(7,'MCQ',
'''Choose the revision that is grammatically correct and preserves both intended meanings: Mira did not leave earlier, so she missed the train; Mira, not the meeting, reached the office late.

Original: “If Mira had left earlier, she will catch the train. Having reached the office late, the meeting had already begun.”''',
['If Mira left earlier, she will catch the train. Having reached the office late, the meeting began.',
 'If Mira had left earlier, she would have caught the train. When Mira reached the office late, the meeting had already begun.',
 'If Mira had left earlier, she would catch the train. Having reached the office late, the meeting had begun.',
 'If Mira would have left earlier, she caught the train. When the meeting reached the office late, Mira had begun.'],['B'],
'''1. An unreal past condition uses “had left” with the result “would have caught”.
2. A participial clause cannot attach Mira's late arrival to the grammatical subject “the meeting”. Naming Mira in a when-clause resolves that dangling modifier.
3. Only B satisfies both requirements and retains the original time relationship.''',
['It changes the past counterfactual and still assigns the late arrival to the meeting.','The past counterfactual and arrival subject are both correct.','The result should be would have caught; the dangling modifier also remains.','The conditional form is wrong and the subjects no longer express the intended facts.'],
'Fixing one tense error does not repair a separate dangling modifier.','ga_past_counterfactual_and_dangling_modifier_repair')

add(8,'MCQ',
'''A tank contains 120 litres of a well-mixed milk-water mixture in the ratio 3:2. First, 30 litres are removed and replaced with water. After thorough mixing, 20 litres are removed and replaced with pure milk. What is the final ratio of milk to water? Volumes are additive.''',
['11:13','13:11','3:2','7:5'],['B'],
'''1. Initially milk=72 and water=48 litres. The first withdrawal removes one-quarter of each, leaving 54 milk and 36 water; the refill makes water 66.
2. The next withdrawal removes one-sixth of each: the remaining amounts are milk=45 and water=55.
3. Adding 20 litres of milk gives 65:55=13:11.''',
['This reverses the final milk and water quantities.','The final quantities are 65 and 55 litres.','The two different replacement fluids do not preserve the starting ratio.','This would require 70 litres milk rather than 65.'],
'Each withdrawal uses the composition after the preceding mixing step.','ga_sequential_replacement_different_refill_fluids')

add(9,'MSQ',
'''Five distinct talks A,B,C,D,E are scheduled in positions 1 through 5. C is last. A occurs before C. Exactly one talk lies between B and D. E is neither first nor last. Which statements are true over schedules satisfying all these conditions?''',
['A can be fourth.','A must occur before E.','E can be third.','B and D must both occupy odd-numbered positions.'],['A','C'],
'''1. Since C is fifth, the positions of B and D must be {1,3} or {2,4}.
2. With B,D in {1,3}, A,E occupy {2,4} in either order; hence A can be fourth and need not precede E.
3. With B,D in {2,4}, E must be third and A first. Thus C is possible and D's claim of odd positions is false.''',
['For example B,E,D,A,C is valid.','The same schedule places E before A.','For example A,B,E,D,C is valid.','The latter schedule has both B and D in even positions.'],
'A claim of possibility needs one witness; a claim of necessity must survive every valid schedule.','ga_position_constraints_possible_vs_necessary')

add(10,'MCQ',
'''Solid stacks of unit cubes stand in a 2-by-3 grid. Each stack has a nonnegative integer height and has no gaps. Looking along the two-row direction, the maximum heights in the three columns are 2,3,1 respectively. Looking along the three-column direction, the maximum heights in the two rows are 3,2 respectively. What pair gives the minimum and maximum possible total number of cubes?''',
['(7,11)','(6,11)','(6,12)','(8,12)'],['B'],
'''1. Each stack at row i, column j is at most min(row maximum i, column maximum j). The componentwise largest arrangement is rows [2,3,1] and [2,2,1], with 11 cubes; it meets every projection.
2. Each column must attain its maximum, so at least 2+3+1=6 cubes are needed.
3. Rows [0,3,1] and [2,0,0] attain all required row and column maxima with exactly 6 cubes. Thus both bounds are achievable.''',
['The displayed 6-cube construction disproves a minimum of 7.','It gives the two attainable bounds.','The per-stack upper bounds sum to only 11.','Both numbers exceed attainable tight bounds.'],
'Projection heights are maxima, not sums; each visible peak can serve both a row and a column constraint.','ga_voxel_projections_tight_volume_bounds')
out[-1]['subtopic']='Two- and three-dimensional patterns'

add(22,'MSQ',
'''For real t let

```text
A(t) = [1  2  1]
       [2  t  3]
       [1  3  1].
```

Use Doolittle elimination, with unit diagonal in L and no row exchanges unless an option explicitly permits one. Which statements are correct?''',
['det(A(t))=-1 for every real t.','An unpivoted factorization A=LU with unit lower-triangular L exists for every real t.','At t=4, exchanging rows 2 and 3 after eliminating column 1 allows elimination to finish without a zero pivot.','At t=5, the final diagonal entry U33 is 1.'],['A','C'],
'''1. Eliminate column 1 to obtain rows [1,2,1], [0,t-4,1], [0,1,0]. Expanding along column 1 gives determinant -1 for every t.
2. At t=4 the second pivot is zero while the entry below it is 1. In any unit-lower LU decomposition the forced leading U block would have U22=0, making the required A32 residual impossible. Row exchange fixes this, giving trailing block diag(1,1).
3. At t=5, the second pivot is 1 and eliminating the last row gives U33=-1, not 1.''',
['The trailing 2-by-2 determinant is (t-4)*0-1=-1.','Nonsingularity does not ensure all unpivoted pivots exist; t=4 is a counterexample.','The swapped trailing rows are [1,0] and [0,1].','The last elimination subtracts the second trailing row and produces -1.'],
'An invertible matrix may still require pivoting for a particular elimination order.','em_nonsingular_parameter_matrix_lu_pivot_failure')

add(24,'NAT',
'''Evaluate the integral from 0 to 1 of max(x,1-2x) with respect to x. Round the result to three decimal places.''',
[],0.667,
'''1. The two expressions cross at x=1/3. The maximum is 1-2x to its left and x to its right.
2. The two integrals are [x-x^2] from 0 to 1/3 = 2/9 and [x^2/2] from 1/3 to 1 = 4/9.
3. Their sum is 2/3, which rounds to 0.667.''',[],
'Integrate the upper expression separately on each side of its crossover.','em_integral_upper_envelope_linear_crossover',3,3)

add(29,'NAT',
'''Dataset A contains 3 observations with mean 2 and population variance 2. Dataset B contains 2 observations with mean 7 and population variance 1. What is the population variance of their combined five observations? Use division by the population size, not by one less than that size.''',
[],7.6,
'''1. The combined mean is (3*2+2*7)/5=4.
2. The mean square in A is 2+2^2=6, and that in B is 1+7^2=50. The combined mean square is (3*6+2*50)/5=118/5.
3. Subtract the square of the combined mean: 118/5-16=38/5=7.6.''',[],
'Pooling variances requires accounting for different group means as well as group sizes.','em_pooled_variance_with_between_group_shift',3,1)

add(33,'MCQ',
'''On the set of residues {0,1,2,3,4} modulo 5, define permutations f(x)=2x mod 5 and g(x)=(x+1) mod 5. Let h=f composed with g composed with f-inverse composed with g-inverse; the rightmost map acts first. What is the smallest positive integer k for which h applied k times is the identity?''',
['1','2','4','5'],['D'],
'''1. The inverses are f-inverse(x)=3x mod 5 and g-inverse(x)=x-1 mod 5.
2. Apply the maps right to left: x becomes x-1, then 3x-3, then 3x-2, then 6x-4, which is x+1 modulo 5.
3. Thus h is a translation by 1; its k-fold application is x+k, equal to x for every residue exactly when k is a multiple of 5.''',
['h is not identity; it maps 0 to 1.','Two applications map 0 to 2.','The order of f alone is 4, but h is a different permutation.','Five is the least positive translation count returning every residue.'],
'Composition order matters when the permutations do not commute.','em_affine_permutation_commutator_order')

add(35,'MSQ',
'''G is a connected simple undirected graph with degree multiset {3,3,2,2,2,2}. Which statements must hold?''',
['G has exactly 7 edges.','G has an Euler trail that uses every edge exactly once.','G is bipartite.','G has a Hamiltonian cycle.'],['A','B'],
'''1. The degree sum is 14, so the handshake lemma gives 7 edges.
2. G is connected and has exactly two odd-degree vertices. It therefore has an open Euler trail.
3. For a counterexample to both remaining assertions, take two disjoint triangles and connect one vertex of each by one bridge. The bridge endpoints have degree 3 and all others degree 2. The triangles exclude bipartiteness; the bridge excludes a Hamiltonian cycle.''',
['Each undirected edge contributes twice to the degree sum.','Connectedness and exactly two odd vertices are sufficient.','The two-triangle bridge construction has an odd cycle.','A Hamiltonian cycle cannot cross a bridge and return without reusing it.'],
'A degree sequence can force an Euler trail without forcing bipartiteness or a Hamiltonian cycle.','em_degree_multiset_euler_guarantee_shared_counterexample')

add(39,'NAT',
'''Six positions around a circle are filled with two red, two blue and two green beads. Beads of the same colour are indistinguishable. Adjacent positions, including the last and first, must have different colours. Arrangements related by rotation are identified; reflections are counted separately unless a rotation already identifies them. How many arrangements are there?''',
[],5,
'''1. First label the six positions. Without adjacency restrictions there are 6!/(2!2!2!)=90 colourings. For a given colour to occupy adjacent positions, choose its edge in 6 ways and place the other two pairs in 6 ways: 36 colourings.
2. For two specified colours both to be adjacent, choose the first edge in 6 ways and a disjoint edge in 3 ways: 18. For all three pairs to be adjacent, choose one of the two perfect matchings of the 6-cycle, then assign the colours in 3!=6 ways: 12. Inclusion-exclusion gives 90-3*36+3*18-12=24 valid labelled colourings.
3. Six of these have the form XYZXYZ, where X,Y,Z are different. They have rotation orbits of size 3, giving two arrangements. Every other valid colouring has six distinct rotations: periods 1 and 2 are incompatible with two of each colour. The other 18 colourings give three arrangements.
4. Total arrangements = 2+3=5.''',[],
'Dividing by six blindly fails when some colourings have rotational symmetry.','em_balanced_cycle_colouring_inclusion_exclusion_variable_orbits',4,difficulty='Hard')

add(40,'MCQ',
'''Let e_n be the number of binary strings of length n that have no consecutive 1s and contain an even number of 1s. The empty string is counted, so e_0=1. Which formal ordinary generating function E(x)=sum over n>=0 of e_n*x^n is correct?''',
['(1+x)/(1-x-x^2)','(1-x+x^3)/(1-2x+x^2-x^4)','1/(1-x-x^2)','(1-x)/(1-2x+x^2-x^4)'],['B'],
'''1. Mark each 1 by y. If F(x,y) counts all strings with no consecutive 1s, the last-bit recurrence for n>=2 is F_n(y)=F_(n-1)(y)+y*F_(n-2)(y), with F_0=1 and F_1=1+y. Thus F(x,y)=(1+xy)/(1-x-x^2*y).
2. Keeping only even powers of y gives E(x)=(F(x,1)+F(x,-1))/2.
3. Combining the fractions gives numerator 1-x+x^3 and denominator (1-x)^2-x^4=1-2x+x^2-x^4. This is B; it begins 1+x+x^2+2x^3+4x^4+... .''',
['This counts all allowed strings without the parity restriction; its coefficient of x is 2 instead of 1.','It is the even-parity projection of the bivariate generating function.','Its coefficient of x^2 is 2, but the only even-parity valid length-2 string is 00.','It misses the x^3 numerator contribution and gives coefficient 1 at x^3 instead of 2.'],
'Parity restrictions require tracking a marked statistic, not merely forbidding local patterns.','em_binary_no_adjacent_ones_even_parity_generating_function',3)

add(44,'MSQ',
'''R is a binary relation on a finite nonempty domain. Use the following properties:

- E: for every x there exists y such that R(x,y).
- T: R is transitive.
- I: R is irreflexive.
- S: R is symmetric.
- F: for each x, at most one y satisfies R(x,y).

Which listed combinations admit a model on some finite nonempty domain? Properties not listed in an option impose no condition.''',
['E, T, I','E, S, I, F','E, T, I, F','E, T, S'],['B','D'],
'''1. E lets us follow an R-edge indefinitely from any vertex. Finiteness forces a repeated vertex, hence a directed cycle. Under T, a directed cycle yields a self-loop, contradicting I. Thus A and C have no finite nonempty model, irrespective of F.
2. B has a two-element model {u,v} with only R(u,v) and R(v,u). Every element has one successor; the relation is symmetric and irreflexive.
3. D has a singleton model {u} with R(u,u). It satisfies E, T and S; irreflexivity was not required.''',
['A finite successor chain repeats, and transitivity then violates irreflexivity.','The two-element swap relation is a witness.','Adding functionality cannot repair the E,T,I contradiction.','The singleton reflexive relation is a witness.'],
'Finiteness changes satisfiability: an irreflexive transitive relation can have successors everywhere on an infinite ordered domain.','em_finite_relation_model_existence_cycle_transitivity',3)

add(54,'NAT',
'''Let A be the real 4x4 matrix

```text
A = [0 1 0 0]
    [0 0 1 0]
    [0 0 0 1]
    [1 0 0 0].
```

How many real matrices X simultaneously satisfy X=X^T, AX=XA, X^2=X, and X*(1,1,1,1)^T=0?''',
[],4,
'''1. AX=XA means the entries repeat under a simultaneous cyclic shift of row and column indices. Symmetry therefore forces X to have rows [a,b,c,b], [b,a,b,c], [c,b,a,b], [b,c,b,a].
2. The zero-row-sum requirement gives a+c+2b=0. The vector (1,-1,1,-1) has eigenvalue mu=a+c-2b=-4b. Every vector (p,q,-p,-q) has eigenvalue nu=a-c; this is a two-dimensional eigenspace. Together with the all-ones vector, these spaces span R^4.
3. X^2=X holds exactly when mu and nu each belong to {0,1}, since the remaining eigenvalue is already zero.
4. Every ordered pair (mu,nu) determines one matrix: b=-mu/4, a=mu/4+nu/2, c=mu/4-nu/2. There are 2*2=4 pairs and hence four matrices.''',[],
'The commuting and symmetry constraints couple entries before idempotence is imposed; an arbitrary projection is not allowed.','em_symmetric_cyclic_commuting_zero_sum_projection_count',4,difficulty='Hard')

(ROOT/'drafts/mock002_main.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Saved {len(out)} original authored records; review pending.')
