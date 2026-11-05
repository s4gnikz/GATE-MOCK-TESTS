"""Hand-authored pilot content. This is not a parameterized question generator."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
slots=json.loads((ROOT/'blueprints/papers.json').read_text())[0]['slots']
questions=[]
def add(n,typ,stem,options,answer,solution,why,misconception,family,steps=2,precision=0):
    q=dict(slots[n-1]); q.update(id=f'CS27-M001-Q{n:03}',paper=1,type=typ,stem=stem,
        options=options,answer=answer,solution=solution,option_explanations=why,
        misconception=misconception,family=family,reasoning_pattern=family,
        structure_signature=family,reasoning_steps=steps,
        references=['research/SYLLABUS_2027.md','research/GATE_PATTERN_ANALYSIS.md'],
        verification={'status':'REVIEW_REQUIRED','method':'author derivation',
                      'independent_solution':'','evidence':''},
        validation_status='REVIEW_REQUIRED',assets=[],
        nat=({'min':answer,'max':answer,'precision':precision} if typ=='NAT' else None))
    questions.append(q)

add(1,'MCQ',
'''Choose the pair that completes the sentence grammatically.

Each of the instruments that ___ damaged during transport ___ now been recalibrated.''',
['were; has','was; have','were; have','was; has'],['A'],
'''1. The relative clause “that were damaged” modifies the plural noun instruments.
2. The main clause has the singular subject Each, so its verb is has.
The complete sentence therefore uses were; has.''',
['Both agreements are correct.','Both verbs have the wrong number.','The main verb must agree with Each, not instruments.','The relative-clause verb must agree with instruments.'],
'A noun near a verb need not be that verb\'s grammatical subject.','ga_relative_clause_vs_main_agreement')

add(2,'NAT',
'''A service receives orders of two kinds, X and Y. Initially, 40% of the orders are X. Exactly 25% of X orders and 10% of Y orders are cancelled; all remaining orders are completed. What percentage of completed orders are X? Round to two decimal places.''',
[],35.71,
'''1. Normalize the initial number of orders to 100. There are 40 X and 60 Y orders.
2. Completed X orders = 40(0.75) = 30; completed Y orders = 60(0.90) = 54.
3. The required percentage is 100(30/84) = 250/7 = 35.714285..., which rounds to 35.71.''',[],
'The denominator is completed orders, not original orders.','ga_conditional_percentage_after_asymmetric_cancellation',3,2)

add(3,'NAT',
'''Exactly two of A, B, C and D must be on duty. If A is on duty, B must be on duty. In addition, C is on duty if and only if D is not on duty. How many different pairs can be on duty?''',
[],2,
'''1. The biconditional requires exactly one of C and D to be selected.
2. The other selected person must be A or B. Selecting A would also require B, producing three people, which is forbidden.
3. Hence the possible pairs are {B,C} and {B,D}: two pairs.''',[],
'An implication does not require its antecedent to be true.','ga_exact_cardinality_implication_biconditional',3)

add(4,'MCQ',
'''A triangular tile has labelled vertices P=(1,1), Q=(3,1), R=(1,2) in a Cartesian plane. First reflect the tile in the x-axis. Then rotate the result clockwise by 90 degrees about the origin. Which ordered triple gives the final positions of P, Q and R?''',
['((-1,-1),(-1,-3),(-2,-1))','((1,1),(1,3),(2,1))','((1,-1),(1,-3),(2,-1))','((-1,1),(-1,3),(-2,1))'],['A'],
'''1. Reflection maps (x,y) to (x,-y).
2. Clockwise quarter-turn maps (u,v) to (v,-u). The combined map is (x,y) to (-y,-x).
3. Applying it separately to the labelled vertices gives (-1,-1), (-1,-3), (-2,-1).''',
['All three vertices obey (-y,-x).','This is the combined map for a counterclockwise rotation after reflection.','This applies clockwise rotation without the preceding reflection.','This applies counterclockwise rotation without reflection.'],
'Reflection and rotation must be composed in the stated order.','ga_labelled_triangle_reflection_rotation',3)

add(5,'MCQ',
'''Read the passage.

“A library extended its evening opening hours in June. Evening visits increased, while total daily visits remained unchanged. The library did not record whether evening visitors had previously visited at other times.”

Which conclusion is best supported by the passage?''',
['The extended hours attracted no new visitors.','Some visits may have shifted from earlier hours to the evening.','Every evening visitor formerly visited in the morning.','The extension reduced the total number of visits.'],['B'],
'''1. The data establish increased evening visits and unchanged daily totals.
2. A shift in visit timing is compatible with those observations, but individual histories were not recorded.
3. Therefore the cautious possibility in B is supported; definitive claims about individual visitors are not.''',
['New visitors could have been offset by losses elsewhere.','A timing shift is possible and fits both reported totals.','No individual histories establish this universal claim.','The passage explicitly says daily totals were unchanged.'],
'Aggregate counts do not identify the behaviour of each individual.','ga_aggregate_observation_vs_individual_inference')

add(6,'MCQ',
'''Seven distinct people, including A, B, C and D, sit around a circular table. A and B must sit next to each other, whereas C and D must not sit next to each other. Rotations of an arrangement are identical; reflections are different. How many arrangements are possible?''',
['96','120','144','240'],['C'],
'''1. Treat A and B as a block with two internal orders. There are six units around the circle, giving 2(5!) = 240 arrangements.
2. Of these, arrangements with C and D also adjacent have five circular units and four internal block orders: 4(4!) = 96.
3. Subtract the forbidden arrangements: 240 - 96 = 144.''',
['This counts the forbidden cases with both pairs adjacent.','This loses the two possible orders inside the A-B block.','The subtraction gives 144.','This ignores the restriction on C and D.'],
'Circular blocks reduce the number of rotationally distinct units before factorial counting.','ga_circular_two_blocks_exclusion',3)

add(7,'MCQ',
'''Two teams produce identical items. The table lists working hours and completed items in two months. Overall productivity means total completed items divided by total working hours.

| Team | Month 1 hours | Month 1 items | Month 2 hours | Month 2 items |
|---|---:|---:|---:|---:|
| A | 40 | 400 | 60 | 660 |
| B | 60 | 900 | 40 | 640 |

What is the percentage change in overall productivity from Month 1 to Month 2?''',
['0%','8% increase','10% increase','12% increase'],['A'],
'''1. Month 1 productivity is (400+900)/(40+60) = 13 items/hour.
2. Month 2 productivity is (660+640)/(60+40) = 13 items/hour.
3. The percentage change is zero, even though each team's own rate improved. More hours were allocated to the slower team.''',
['Both aggregate rates are 13.','A simple or weighted average of team percentage gains cannot replace aggregation with the new hour mix.','This is only A\'s rate improvement.','Neither the total output nor the total hours implies this increase.'],
'A changed mixture can offset improvements in every component rate.','ga_productivity_mix_shift',3)

add(8,'NAT',
'''A square sheet occupies 0 <= x <= 8 and 0 <= y <= 8. Fold its left half onto its right half along x=4. Next fold its bottom half onto its top half along y=4. Punch small point-like holes through all layers at (5,6) and (6,5) in the folded sheet. After fully unfolding, how many distinct holes lie on the line y=x+1? Ignore hole diameter and sheet thickness.''',
[],2,
'''1. Unfolding a point (x,y) produces (x,y), (8-x,y), (x,8-y), (8-x,8-y).
2. The first punch produces (5,6),(3,6),(5,2),(3,2). Only (5,6) lies on y=x+1.
3. The second produces (6,5),(2,5),(6,3),(2,3). Only (2,3) lies on that line. The sets are disjoint, so the answer is 2.''',[],
'Both folds must be reversed; points from different punches need not lie on the same symmetry line.','ga_double_fold_two_punch_line_incidence',3)

add(9,'MCQ',
'''Arrange the following sentences into a coherent chronological account. Treat the explicitly stated causal and time relations as binding.

P. Based on the successful repeat trial, the final report recommended a full rollout.
Q. Both gauges were calibrated before the first trial began.
R. During that first trial, the two readings diverged as temperature rose.
S. Replacing one gauge eliminated this divergence in a repeat trial.
T. After receiving the final report, the committee accepted its recommendation.

Which sequence is correct?''',
['Q-R-P-S-T','R-Q-S-P-T','Q-R-S-P-T','Q-S-R-T-P'],['C'],
'''1. Calibration precedes the first trial: Q precedes R.
2. “This divergence” in S refers to R, and the successful repeat trial is the basis of P: R precedes S precedes P.
3. T follows receipt of the final report: P precedes T. Combining the constraints gives Q-R-S-P-T.''',
['P cannot precede the repeat trial on which it is based.','Q explicitly precedes the first trial described in R.','This satisfies all four precedence links.','S cannot precede the divergence, and T cannot precede the report.'],
'A grammatically plausible adjacent pair can still violate the account\'s causal order.','ga_causal_narrative_constraint_chain',3)

add(10,'MCQ',
'''A fair coin selects one of two bags. Bag I contains 4 red and 2 blue balls; Bag II contains 2 red and 3 blue balls. Two balls are then drawn uniformly without replacement from the selected bag. Given that the two balls have the same colour, what is the probability that both are red?''',
['1/2','15/26','7/13','3/5'],['B'],
'''1. In Bag I, P(RR)=6/15 and P(same)=7/15. In Bag II, P(RR)=1/10 and P(same)=4/10.
2. Before conditioning, P(RR)=(1/2)(6/15+1/10)=1/4, and P(same)=(1/2)(7/15+4/10)=13/30.
3. Since RR is a subset of same, P(RR | same)=(1/4)/(13/30)=15/26.''',
['Conditioning on same does not leave red and blue equally likely.','The ratio of the mixture probabilities is 15/26.','This is not the ratio P(RR)/P(same).','Conditioning cannot be replaced by the initial proportion in a bag.'],
'Conditional probabilities from different bags cannot be averaged without updating their weights.','ga_mixture_without_replacement_colour_condition',3)

add(11,'MCQ',
'''For Boolean variables x, y and z, let F=(x OR y) AND ((NOT x) OR z). Which expression is equivalent to F for every input?''',
['(x AND z) OR ((NOT x) AND y)','(x AND y) OR ((NOT x) AND z)','y OR z','x XOR y XOR z'],['A'],
'''1. If x=0, the original expression reduces to y. If x=1, it reduces to z.
2. A selects exactly these two cofactors. Equivalently, expansion gives xz + x\'y + yz, and the consensus term yz is redundant.''',
['Its x=0 and x=1 cofactors are y and z.','This swaps the selected cofactors; x=0,y=1,z=0 is a counterexample.','For x=1,y=1,z=0 it gives 1, whereas F=0.','For x=y=z=0 it agrees, but x=1,y=z=0 gives 1 while F=0.'],
'The consensus term need not appear in a minimal equivalent expression.','dl_mux_cofactor_consensus')

add(12,'NAT',
'''A process opens a regular file for reading, obtaining descriptor p with file offset 0, and then executes q=dup(p). It performs the following successful operations in order: read 2 bytes through p; read 3 bytes through q; seek through p to absolute byte offset 1; read 1 byte through q. The file is long enough for every read. What is the resulting shared file offset? Offsets are zero-based.''',
[],2,
'''1. dup creates a second descriptor referring to the same open-file description, so the offset is shared.
2. The two reads move the offset to 2 and then 5.
3. The absolute seek resets it to 1. The final one-byte read moves it to 2.''',[],
'Duplicated descriptors share an offset; reopening the path would create an independent offset.','os_dup_seek_shared_open_description',3)

add(13,'MCQ',
'''A four-variable Boolean function F(A,B,C,D), with A as the most significant bit of the minterm index, is 1 at minterms 1,3,9,11. Minterms 0,2,8,10 are don't-cares, and all remaining minterms are 0. Which is a minimum-literal sum-of-products implementation?''',
['NOT B','NOT D','A OR C','(NOT B) AND D'],['A'],
'''1. The required ones and don't-cares together are exactly the eight inputs with B=0.
2. Assign those don't-cares to 1 and group all eight cells. This yields NOT B with one literal.
3. A zero-literal constant is impossible because both required zeros and required ones exist.''',
['It covers all required ones and no required zero with one literal.','It misses every required one, each of which has D=1.','For A=B=1,C=0,D=0 it produces a forbidden 1.','It is valid but has two literals, so it is not minimum-literal.'],
"A valid implementation may still be nonminimal when don't-cares are available.",'dl_dontcare_eightcell_literal_lower_bound',3)

add(14,'MCQ',
'''Let R be a binary relation on a nonempty domain. Which formula is the logical negation of

`forall x exists y [R(x,y) AND forall z (R(x,z) -> z=y)]`?

All variables in the options are bound as displayed.''',
['exists x forall y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]',
 'exists x exists y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]',
 'forall x forall y [NOT R(x,y) AND exists z (R(x,z) AND z!=y)]',
 'exists x forall y [NOT R(x,y) OR forall z (R(x,z) AND z!=y)]'],['A'],
'''1. Negating the outer quantifiers changes forall x exists y into exists x forall y.
2. Negating the conjunction gives NOT R(x,y) OR NOT forall z (R(x,z) -> z=y).
3. The inner negation is exists z [R(x,z) AND z!=y]. Substitution gives A. The original formula says each x has exactly one R-successor; its negation allows an x with none or more than one.''',
['It follows all three quantifier and connective changes.','For a two-element identity relation the original is true, but this option is also true by choosing x!=y.','For a singleton empty relation the original is false, but this conjunction is false.','For a universal relation on two elements the original is false; this option is false because z=y defeats its universal conjunct.'],
'Negating unique existence requires accounting for both zero and multiple witnesses.','em_nested_unique_successor_negation',3)

add(15,'NAT',
'''A byte-addressed machine executes a 4-byte load instruction beginning at address 100. Its indirect PC-relative mode first sign-extends an 8-bit displacement, multiplies that signed displacement by 4, and adds it to the address immediately after the instruction. The 32-bit word at this intermediate address is the effective address of the operand. The displacement bits are 11111010. Memory words M[80]=120 and M[120]=7 are given. What is the effective address of the operand? All addresses are decimal; the machine uses two's-complement displacements.''',
[],120,
'''1. The displacement is -6, not 250. The post-instruction PC is 104.
2. The intermediate address is 104+4(-6)=80.
3. Indirection reads M[80]=120, so the operand address is 120. M[120]=7 is the value loaded, not the address asked for.''',[],
'PC base, scale, indirection and loaded value are distinct stages.','coa_signed_scaled_pc_relative_indirection',3)

add(16,'MCQ',
'''A 4-bit adder-subtractor computes A+(B XOR ssss)+s and keeps the low four result bits. Its carry-out is C and its two's-complement signed overflow flag is V. For A=0111, B=1010 and s=1, which triple (result,C,V) is correct?''',
['(1101,1,0)','(1101,0,0)','(0011,1,1)','(1101,0,1)'],['D'],
'''1. With s=1, invert B to 0101 and add 1: 0111+0101+1=1101, with no fifth bit. Thus C=0.
2. Signed interpretation gives 7-(-6)=13, outside [-8,7], so V=1 even though the unsigned carry-out is zero.''',
['Carry-out is zero and signed overflow is present.','It gets result and carry right but misses signed overflow.','The stated bit addition does not yield 0011.','Both the bit arithmetic and signed range test agree.'],
'Carry-out and signed overflow are different conditions.','coa_subtractor_carry_vs_signed_overflow')

add(17,'NAT',
'''In an ER model, Department is a strong entity with key dept_id. Project is weak and identified by its owning Department and partial key project_code. Task is weak and identified by its owning Project and partial key task_no. Project codes may repeat across departments; task numbers may repeat across projects. No surrogate keys or additional uniqueness constraints are introduced. How many attributes are needed in the minimal primary key of the mapped Task relation?''',
[],3,
'''1. Project is identified by (dept_id, project_code), because project_code alone may repeat.
2. Task adds its own partial key, giving (dept_id, project_code, task_no).
3. Dropping any attribute can merge allowed distinct tasks, so all three are necessary.''',[],
'A weak owner can itself have a composite identifying key.','db_nested_weak_entity_key_inheritance',3)

add(18,'MCQ',
'''A lexer recognizes identifiers by `[a-z][a-z0-9]*`, the keyword `if`, and operators `==`, `=`, `++`, `+`. It uses maximal munch; an identifier lexeme exactly equal to `if` is classified as a keyword. Whitespace is ignored. What token-lexeme sequence is produced for `ifx==if+++x`?''',
['if, x, ==, if, ++, +, x','ifx, ==, if, ++, +, x','ifx, =, =, if, +, ++, x','ifx, ==, if, +++, x'],['B'],
'''1. The longest identifier prefix is ifx; a keyword prefix does not split it.
2. Maximal munch chooses == rather than two = operators.
3. The next identifier is exactly if, followed by ++ and +, because +++ is not a token. The final token is x.''',
['A keyword prefix cannot split the longer valid identifier ifx.','Every boundary follows maximal munch.','It splits == and fails to take ++ at the first plus.','+++ is not among the recognized operators.'],
'Token priority breaks equal-length ties; it does not override longest match.','compiler_maximal_munch_keyword_prefix',3)

add(19,'MSQ',
'''An IPv4 packet carrying a TCP segment crosses one router between two Ethernet LANs. The router performs ordinary forwarding, with no NAT, fragmentation or tunnelling. Its incoming TTL is greater than 1. Which statements are correct about the outgoing packet/frame?''',
['The destination IPv4 address is unchanged.','The destination Ethernet address must be unchanged.','The IPv4 TTL is one less than on arrival.','The TCP destination port is replaced by the router\'s port number.'],['A','C'],
'''1. Ordinary routing keeps the end-to-end IPv4 destination and TCP port unchanged.
2. Forwarding decrements TTL and constructs an Ethernet frame for the outgoing LAN's next hop.
3. Therefore A and C hold; the incoming and outgoing link-layer destinations need not match.''',
['No address translation occurs.','The outgoing frame addresses the next hop on a different LAN, not necessarily the incoming destination MAC.','The stated assumptions ensure ordinary forwarding with a one-hop decrement.','TCP ports identify endpoints; a transit router does not replace them.'],
'Link-layer next-hop addressing must be distinguished from end-to-end addressing.','cn_router_layer_specific_field_changes',3)

add(20,'NAT',
'''Insertion sort is run on keys `[3a, 1, 3b, 2, 3c]`, where 3a, 3b and 3c have equal numeric key 3 and the suffixes only identify records. The usual inner loop shifts a preceding record while its key is strictly greater than the key being inserted. A modified version shifts while it is greater than or equal. Count only shifts of preceding records one position to the right, not final placements of the inserted record. How many additional shifts does the modified version perform?''',
[],3,
'''1. Strictly unequal inversions cause the same shifts in both versions: 3a past 1 and 2, and 3b past 2.
2. Only the modified version also shifts equal preceding records: one when inserting 3b and two when inserting 3c.
3. The additional count is 1+2=3; totals are 3 and 6 respectively.''',[],
'Equality in the comparison changes stability and adds one shift per equal-key pair.','alg_insertion_stability_equal_pair_shift_delta',3)

add(21,'MSQ',
'''Use set semantics. R(A,B)={(1,x),(1,y),(2,x)} and S(B)={(x),(y)}. Define

`E = projection_A(R) - projection_A((projection_A(R) x S) - R)`

where x is Cartesian product and - is set difference. Which statements are correct? Each proposed change is applied independently to the original relations.''',
['For the original relations, E={(1)}.','If S is empty, E={(1),(2)}.','If (2,y) is added to R, E remains {(1)}.','If (z) is added to S, E is empty.'],['A','B','D'],
'''1. The product creates every candidate A paired with every required B. Subtracting R identifies a missing required pair; its A is excluded.
2. Originally only A=2 misses y, leaving 1. With empty S there are no missing pairs, so all candidate A values remain.
3. Adding (2,y) makes both candidates qualify. Adding z to S makes both fail because neither has a z pair.''',
['Only 1 is paired with every B in S.','Universal coverage of an empty required set is vacuously true.','The result becomes {(1),(2)}, not {(1)}.','Both candidates lack z.'],
'Division-like expressions include vacuous truth and candidate-domain restrictions.','db_division_expression_empty_divisor_counterfactuals',3)

add(22,'MCQ',
'''For the grammar S -> AB, A -> aA | epsilon, B -> bB | epsilon, with start symbol S and end marker $, what is FOLLOW(A)?''',
['{a,b}','{b,$}','{$}','{a,b,$}'],['B'],
'''1. Since A is followed by B, FIRST(B) excluding epsilon contributes b.
2. B is nullable, so FOLLOW(S)={$} also contributes to FOLLOW(A).
3. The recursive occurrence at the end of A -> aA adds only FOLLOW(A) itself. Thus the fixed point is {b,$}.''',
['a starts A but does not follow it here; $ is missing.','It includes both contributions and no extra terminal.','It misses b from FIRST(B).','It incorrectly adds a.'],
'FIRST and FOLLOW are different, and nullable suffixes propagate FOLLOW.','compiler_nullable_suffix_follow_fixed_point',3)

add(23,'NAT',
'''For real t, consider the homogeneous system M(t)v=0, where

```text
M(t) = [1  1  1]
       [1  t  2]
       [1  2  t]
```

What is the sum of all distinct real values of t for which the system has infinitely many solutions?''',
[],2,
'''1. Subtract row 1 from rows 2 and 3. The determinant becomes (t-1)^2-1=t(t-2).
2. A real homogeneous square system has infinitely many solutions precisely when it is singular.
3. The distinct singular values are t=0 and t=2, whose sum is 2.''',[],
'A homogeneous singular system is always consistent and has a nontrivial null space.','em_parameter_singular_homogeneous_system',3)

add(24,'MCQ',
'''Define f(0)=0 and f(x)=x^2 sin(1/x) for real x!=0. Which statement is correct?''',
['f is discontinuous at 0.','f is differentiable at 0, but its derivative is not continuous at 0.','f is continuous at 0 but not differentiable there.','f has a continuous derivative at 0.'],['B'],
'''1. |f(x)|<=x^2 proves continuity at 0.
2. The difference quotient f(h)/h=h sin(1/h) tends to zero, so f\'(0)=0.
3. For x!=0, f\'(x)=2x sin(1/x)-cos(1/x). Along x=1/(2k*pi) it tends to -1; along x=1/((2k+1)*pi) it tends to 1. It has no limit at 0.''',
['The bound x^2 forces continuity.','The difference quotient exists but derivative limits disagree.','The difference quotient tends to zero.','Oscillation in the cosine term prevents derivative continuity.'],
'Differentiability at a point does not guarantee a continuous derivative there.','em_oscillatory_function_vs_derivative_limit',3)

add(25,'NAT',
'''X has a Poisson distribution with parameter lambda>0. It is known that P(X=0)=P(X=1). What is E[X^2]?''',
[],2,
'''1. P(X=0)=exp(-lambda) and P(X=1)=lambda exp(-lambda), so lambda=1.
2. A Poisson variable has variance lambda and mean lambda. Thus E[X^2]=Var(X)+(E[X])^2=lambda+lambda^2=2.''',[],
'The second moment is not the variance alone.','em_poisson_probability_identity_second_moment')

add(26,'NAT',
'''A three-variable Boolean function F(A,B,C), with A as the most significant index bit, is 1 exactly at minterms 0,1,2,5,6,7 and has no don't-cares. How many distinct minimum-product-term sum-of-products covers can be formed using only prime implicants? Ignore the order of terms.''',
[],2,
'''1. No four-cell cube avoids both zero minterms 3 and 4. The prime implicants therefore cover the six adjacent pairs (0,1),(0,2),(1,5),(2,6),(5,7),(6,7).
2. Each covers two minterms, so at least three are necessary. These pairs form a cycle on six vertices: 0-1-5-7-6-2-0.
3. A three-edge cover of six vertices must be a perfect matching. The cycle has exactly two alternating perfect matchings, giving two minimum covers.''',[],
'Finding the minimum number of terms is different from counting all minimum covers.','dl_prime_implicant_cycle_minimum_cover_count',3)

add(27,'MCQ',
'''What does this C program print? Assume a conforming C implementation.

```c
#include <stdio.h>
int main(void) {
    int a[2][3] = {{2,4,6},{1,3,5}};
    int (*p)[3] = a;
    int *q = p[1];
    p[0][2] += q[1];
    int *r = p[0] + 1;
    *r++ = q[0];
    q[2] = *r;
    printf("%d\\n", a[0][1] + a[1][2]);
    return 0;
}
```''',
['7','10','13','The program has undefined behaviour.'],['B'],
'''1. p points to the first row, and q points to the start of row 1. The addition changes a[0][2] from 6 to 9.
2. r initially points to a[0][1]. Because postfix ++ binds before unary *, *r++ stores q[0]=1 at that element, then advances r to a[0][2].
3. q[2]=*r sets a[1][2]=9. The printed sum is 1+9=10. All pointer arithmetic stays inside its row array, and side effects are sequenced across statements.''',
['This misses the earlier update of a[0][2].','The final values are 1 and 9.','This retains the old value 4 in a[0][1].','No access is out of bounds and no scalar has unsequenced conflicting accesses.'],
'Post-increment advances the pointer, not the pointed-to value.','pds_pointer_to_row_postincrement_alias_trace',3)

add(28,'MSQ',
'''An open-addressed hash table has seven slots and uses h1(k)=k mod 7 and h2(k)=1+(k mod 5), probing (h1(k)+j*h2(k)) mod 7 for j=0,1,... . Keys 10,17,24 are inserted in that order into an empty table. Key 10 is then deleted and its slot marked with a tombstone. Which statements are correct?''',
['Searching for 24 must continue past the tombstone.','Replacing that tombstone with a never-used marker preserves all successful searches.','A subsequent insertion of absent key 31 may reuse the tombstone slot.','The deletion permanently reduces the maximum number of keys the table can hold to six.'],['A','C'],
'''1. Key 10 occupies slot 3. Key 17 probes 3 then 6; key 24 probes 3 then 1. Deleting 10 leaves a tombstone at 3.
2. Search for 24 visits 3 and then 1; stopping at 3 would miss it.
3. Tombstones are reusable on insertion. Key 31 starts at 3, so that slot is a possible insertion location after confirming absence. Capacity is not permanently lost.''',
['Its probe sequence reaches slot 1 only after slot 3.','A never-used marker would incorrectly terminate search for 24.','Tombstones retain search chains while remaining available for reuse.','The tombstone may hold a later key, restoring all seven slots as potential capacity.'],
'A tombstone is neither an occupied record nor an ordinary empty stopping point.','alg_doublehash_delete_search_reuse',3)

add(29,'MCQ',
'''A process executes the following pseudocode. Every fork succeeds, fork returns 0 only in the child, and all processes eventually execute print once. There is no buffered output before a fork.

```text
i = 0
while i < 3:
    if fork() == 0:
        break
    i = i + 1
print(i)
```

Ignoring output order, which multiset of values is printed?''',
['{0,1,2,3}','{0,1,1,2,2,2,3,3}','{3,3,3,3}','{0,0,0,3}'],['A'],
'''1. At i=0, the first child breaks and prints 0; only the parent increments and continues.
2. The continuing parent similarly creates children that print 1 and 2.
3. The original parent increments to 3 and exits the loop. Thus exactly four values, 0,1,2,3, are printed.''',
['One child stops in each iteration and the original parent finishes.','Children break; they do not take part in later forks.','A child preserves its copied value of i when it breaks.','Later children inherit i=1 and i=2, not the initial value.'],
'A fork inside a loop is not automatically exponential when children stop iterating.','os_fork_child_break_parent_continuation',3)

add(30,'NAT',
'''Over the alphabet {a,b}, let L contain exactly the strings that end in a and contain an even number of b symbols. The empty string is not in L. What is the number of states in a smallest complete DFA for L?''',
[],3,
'''1. Track E0: even b count but not currently accepting; E1: even b count and last symbol a; O: odd b count. In O the last symbol does not affect future acceptance, so one state suffices.
2. Transitions are E0 --a--> E1, E1 --a--> E1, both E states --b--> O; O --a--> O and O --b--> E0. E0 is initial and E1 alone accepts.
3. E1 is distinguished from the others by the empty suffix; E0 and O are distinguished by suffix a. All three are reachable, proving minimality.''',[],
'The naive product construction can contain equivalent states.','toc_parity_lastsymbol_product_quotient',3)

add(31,'NAT',
'''Two packets of 1000 bits each are ready at time 0 and travel through three store-and-forward links in order. Their rates are 2 Mbit/s, 1 Mbit/s and 2 Mbit/s, respectively; 1 Mbit=10^6 bits. Each link transmits only one packet at a time, buffers are sufficient, and propagation and processing delays are zero. Packets retain their order. At what time, in milliseconds, does the last bit of the second packet reach the destination?''',
[],3,
'''1. Transmission times per link are 0.5, 1 and 0.5 ms. Packet 1 finishes the links at 0.5,1.5,2 ms.
2. Packet 2 finishes link 1 at 1 ms but waits until 1.5 ms for link 2. It finishes link 2 at 2.5 ms.
3. Link 3 is free by then, so its final transmission ends at 3 ms.''',[],
'Pipeline overlap does not remove serialization at the slowest link.','cn_heterogeneous_storeforward_two_packet_schedule',3)

add(32,'MCQ',
'''Consider the grammar S -> SS | aSb | epsilon. Count finite ordered parse trees, distinguishing different tree shapes even when they yield the same string. How many parse trees yield the string ab?''',
['Exactly one','Exactly two','A finite number greater than two','Infinitely many'],['D'],
'''1. A base tree uses S -> aSb with the inner S -> epsilon.
2. Replace the root with S -> SS, placing the previous tree on one child and S -> epsilon on the other. The yield remains ab.
3. Repeating this operation creates arbitrarily large finite trees with the same yield, so their count is infinite.''',
['The base tree is not unique; an empty sibling adds a second shape.','The construction can be repeated after two trees have been obtained.','There is no finite size bound on added empty siblings.','The unbounded family consists of distinct finite trees.'],
'A fixed finite string can have infinitely many parse trees in an epsilon-generating recursive grammar.','toc_nullable_binary_recursion_infinite_parse_ambiguity',3)

add(33,'MCQ',
'''Consider this recursive function on a positive integer n. Arithmetic is exact.

```text
f(n):
    if n == 1: return 1
    r = f(floor(n/2))
    if n is even: return 2*r
    else: return 2*r + 1
```

Which pair gives f(45) and the number of simultaneous active calls at maximum recursion depth, including the initial and base calls?''',
['(45,6)','(45,5)','(32,6)','(63,6)'],['A'],
'''1. Induction gives f(n)=n: the even case restores 2(n/2), and the odd case restores 2 floor(n/2)+1.
2. The call chain is 45,22,11,5,2,1, which contains six active calls at its deepest point.''',
['Both the induction and explicit chain give this pair.','It counts five recursive edges instead of six calls.','The odd branches preserve the discarded low-order bits.','The branches do not append 1 at even n.'],
'Recursion depth counts frames, which is one greater than the number of recursive edges.','pds_binary_reconstruction_induction_depth')

add(34,'MSQ',
'''Let L={w#reverse(w) : w is a string over {0,1}}, where # is a separator not in {0,1}. A pushdown recognizer reads input left to right and may reject immediately on a mismatch. Which statements are correct?''',
['A deterministic pushdown recognizer can push before # and compare/pop after #.','The recognizer can accept after input exhaustion even if unmatched symbols remain on its stack.','The same push-then-pop equality test recognizes {w#w : w over {0,1}}.','The one-symbol input # belongs to L.'],['A','D'],
'''1. The separator deterministically identifies the midpoint. Push each pre-separator bit, then match each later bit to the stack top and pop; accept only after the input ends with the data stack empty.
2. LIFO order compares against reverse(w), not w in its original order.
3. Choosing w=epsilon gives #, which is accepted with an empty data stack.''',
['The separator removes the need to guess when to switch phases.','Remaining symbols mean the second half was too short.','For w=01, input 01#01 fails this test, while 01#10 passes it.','The definition allows the empty string for w.'],
'A stack reverses order; the separator solves midpoint detection, not copying in forward order.','toc_marked_reverse_deterministic_stack_invariant',3)

add(35,'NAT',
'''How many functions f:{1,2,3}->{1,2,3} satisfy f(f(x))=f(x) for every x and have exactly two fixed points? A fixed point is an x for which f(x)=x.''',
[],6,
'''1. Idempotence implies every value in the image is fixed: if y=f(x), then f(y)=y.
2. Choose the two fixed elements in 3 ways. The remaining element must map to one of them, in 2 ways.
3. Each of these 3*2=6 functions satisfies idempotence and has exactly two fixed points.''',[],
'The nonfixed element cannot map to itself or to another nonfixed image under idempotence.','em_idempotent_map_exact_fixedpoint_count',3)

add(39,'MCQ',
'''P is a real 4x4 matrix satisfying P^2=P and rank(P)=2. Let A=3I-2P. Which pair is (det(A), trace(A))?''',
['(9,8)','(1,4)','(81,12)','(9,6)'],['A'],
'''1. The minimal polynomial of P divides x(x-1), whose roots are distinct; hence P is diagonalizable with eigenvalues 0 and 1.
2. Rank 2 implies two eigenvalues of each kind. A therefore has eigenvalues 1,1,3,3.
3. Their product is 9 and their sum is 8.''',
['The transformed eigenvalues give product 9 and sum 8.','This incorrectly treats all four eigenvalues of P as 1.','This incorrectly treats all four as 0.','The product is right but the four eigenvalues sum to 8.'],
'A matrix polynomial transforms each eigenvalue; rank alone is useful here because idempotence constrains the spectrum.','em_idempotent_spectrum_affine_transform',3)

add(40,'NAT',
'''For real a, define f_a(x)=x^4-2a*x^2+4x on the whole real line. What is the smallest integer a for which f_a has two distinct strict local minima?''',
[],2,
'''1. f_a\'(x)=4g(x), where g(x)=x^3-a*x+1. Two strict minima of this quartic require three distinct real roots of g, with alternating derivative signs -,+,-,+.
2. For a<=0, g is increasing and has only one root. For a>0 its turning points are at +/-sqrt(a/3). Its local maximum is 1+2(a/3)^(3/2)>0, and its local minimum is 1-2(a/3)^(3/2).
3. Three distinct roots exist exactly when 1-2(a/3)^(3/2)<0, equivalently a^3>27/4. The threshold is approximately 1.88988, so the smallest integer is 2. At equality a repeated stationary point does not give a second strict minimum.''',[],
'Stationary points must be classified; a repeated derivative root need not be an extremum.','em_quartic_parameter_two_strict_minima_threshold',3)

add(55,'MSQ',
'''A component is faulty with probability 1/4. A test is positive with probability 4/5 for a faulty component and 1/10 for a sound component. Two repetitions of the test are conditionally independent given whether the component is faulty. Let P1 and P2 denote positive results on the first and second repetitions. Which statements are correct?''',
['P(P1)=11/40.','P1 and P2 are independent without conditioning on component status.','P(faulty | P1 and P2)=64/67.','P(P2 | P1)=67/110.'],['A','C','D'],
'''1. Total probability gives P(P1)=(1/4)(4/5)+(3/4)(1/10)=11/40.
2. Conditional independence gives P(P1 and P2)=(1/4)(16/25)+(3/4)(1/100)=67/400. This differs from (11/40)^2, so unconditional independence fails.
3. Bayes gives (16/100)/(67/400)=64/67 for faulty given two positives. The conditional probability of a second positive is (67/400)/(11/40)=67/110.''',
['It follows from the two possible component statuses.','The shared latent status induces dependence; 67/400 is not 121/1600.','The faulty-and-two-positive probability is 64/400.','Divide the joint probability by 11/40.'],
'Conditional independence does not generally imply marginal independence.','em_latent_status_repeated_test_bayes_dependence',3)

add(64,'MSQ',
'''Let L={empty set, {a}, {b}, {a,b}, {a,b,c}} be ordered by inclusion. A complement of x means an element y with meet(x,y)=empty set and join(x,y)={a,b,c}. Which statements are correct?''',
['L is a distributive lattice.','Exactly two elements of L have a complement.','The greatest element is join-irreducible: it cannot be expressed as the join of two strictly smaller elements.','L is a Boolean lattice.'],['A','B','C'],
'''1. L is closed under ordinary union and intersection, which give its joins and meets. Set union and intersection obey distributivity, so L is distributive.
2. Empty set and {a,b,c} complement each other. For any other x, the only possible y whose union with x contains c is the top element; its intersection with nonempty x is not empty. Thus exactly two elements are complemented.
3. Every strictly smaller element is a subset of {a,b}, so the union of two of them is still below the top. The top is join-irreducible. The lack of complements for the other elements means the lattice is not Boolean.''',
['Its set operations stay in L and distribute.','Only bottom and top have complements.','No join of proper elements can contain c.','A Boolean lattice must complement every element.'],
'Distributivity alone does not make a bounded lattice Boolean.','em_union_closed_lattice_complement_top_join_irreducibility',3)

(ROOT/'drafts/pilot_main.json').write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Saved {len(questions)} authored questions; independent review pending.')
