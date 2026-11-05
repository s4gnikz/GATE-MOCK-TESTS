## Q1

**Correct answer:** B

**Concept:** General Aptitude — Vocabulary in context

1. The reviewer supports the objective, so the endorsement is not withdrawn.
2. The requirement of a smaller pilot places a condition on that support. Here “qualified” means limited by reservations, rather than describing professional credentials.

- **A:** This contradicts the explicit condition.
- **B:** This captures support with a limitation.
- **C:** The context gives no information about credentials.
- **D:** Support remains; it has not been withdrawn.

**Common misconception:** A familiar word can have a contextual meaning unrelated to its usual professional use.

## Q2

**Correct answer:** 20 (accepted exactly as entered at the stated precision)

**Concept:** General Aptitude — Powers and logarithms

1. Eight is 2^3, so three doublings take 12 hours and one doubling takes 4 hours.
2. Thirty-two is 2^5, requiring five doublings. The time is 5*4=20 hours.

**Common misconception:** Exponential growth relates elapsed time to the logarithm of the multiplication factor.

## Q3

**Correct answer:** B

**Concept:** General Aptitude — Inductive reasoning and analogies

1. The rejected red, circular, filled card excludes rules that accept both properties together: A and D.
2. The rejected blue, circular, hollow card excludes a colour-independent exclusive-or rule C.
3. B accepts precisely the two listed red cards with one of the two properties and rejects all three other rows. This selects among the stated candidates; it does not claim uniqueness among all imaginable rules.

- **A:** It would accept the first row.
- **B:** It matches all five rows.
- **C:** It would accept the final blue card.
- **D:** It would accept the first, fourth and fifth rows.

**Common misconception:** Observed examples select a rule only relative to a specified candidate set.

## Q4

**Correct answer:** C

**Concept:** General Aptitude — Two- and three-dimensional patterns

1. With A on top, the clockwise side-face order consistent with front B and right C begins B,C. The other view with the same top places D immediately before E in that order.
2. The four side labels are distinct, so their cyclic order is B,C,D,E. Opposite side pairs are B-D and C-E.
3. The third view is consistent with F opposite A and confirms the orientation without changing B's opposite.

- **A:** A is adjacent to B in the first view.
- **B:** C is adjacent to B in the first view.
- **C:** D lies two positions from B around the four side faces.
- **D:** E is adjacent to B in the third view.

**Common misconception:** Face adjacency and cyclic orientation together determine opposite faces.

## Q5

**Correct answer:** 15 (accepted exactly as entered at the stated precision)

**Concept:** General Aptitude — Numerical series

1. Let d_n=a_n-a_(n-1). Subtracting a_(n-1) from the recurrence gives d_n=d_(n-1)+n.
2. Starting from d2=3, obtain d3=6, d4=10 and d5=15.
3. Therefore a5-a4=15. Direct terms 2,5,11,21,36 give the same result.

**Common misconception:** A second-order sequence can become a simpler first-difference pattern.

## Q6

**Correct answer:** B

**Concept:** General Aptitude — Geometry and mensuration

1. If the width is x, the planted dimensions are 16-2x and 10-2x. The planted area is 160-88=72.
2. Expanding (16-2x)(10-2x)=72 gives x^2-13x+22=0, with roots 2 and 11.
3. Geometry requires 0<x<5, so only x=2 is admissible.

- **A:** Width 1 leaves 14*8=112 square metres planted, so the path area is 48.
- **B:** Width 2 leaves 12*6=72, giving path area 88.
- **C:** Width 3 leaves 10*4=40, giving path area 120.
- **D:** Width 4 leaves 8*2=16, giving path area 144.

**Common misconception:** A border removes its width from both ends of each dimension, and algebraic roots must meet geometric bounds.

## Q7

**Correct answer:** B

**Concept:** General Aptitude — Verbal grammar

1. An unreal past condition uses “had left” with the result “would have caught”.
2. A participial clause cannot attach Mira's late arrival to the grammatical subject “the meeting”. Naming Mira in a when-clause resolves that dangling modifier.
3. Only B satisfies both requirements and retains the original time relationship.

- **A:** It changes the past counterfactual and still assigns the late arrival to the meeting.
- **B:** The past counterfactual and arrival subject are both correct.
- **C:** The result should be would have caught; the dangling modifier also remains.
- **D:** The conditional form is wrong and the subjects no longer express the intended facts.

**Common misconception:** Fixing one tense error does not repair a separate dangling modifier.

## Q8

**Correct answer:** B

**Concept:** General Aptitude — Ratios and percentages

1. Initially milk=72 and water=48 litres. The first withdrawal removes one-quarter of each, leaving 54 milk and 36 water; the refill makes water 66.
2. The next withdrawal removes one-sixth of each: the remaining amounts are milk=45 and water=55.
3. Adding 20 litres of milk gives 65:55=13:11.

- **A:** This reverses the final milk and water quantities.
- **B:** The final quantities are 65 and 55 litres.
- **C:** The two different replacement fluids do not preserve the starting ratio.
- **D:** This would require 70 litres milk rather than 65.

**Common misconception:** Each withdrawal uses the composition after the preceding mixing step.

## Q9

**Correct answer:** A, C

**Concept:** General Aptitude — Deductive logic

1. Since C is fifth, the positions of B and D must be {1,3} or {2,4}.
2. With B,D in {1,3}, A,E occupy {2,4} in either order; hence A can be fourth and need not precede E.
3. With B,D in {2,4}, E must be third and A first. Thus C is possible and D's claim of odd positions is false.

- **A:** For example B,E,D,A,C is valid.
- **B:** The same schedule places E before A.
- **C:** For example A,B,E,D,C is valid.
- **D:** The latter schedule has both B and D in even positions.

**Common misconception:** A claim of possibility needs one witness; a claim of necessity must survive every valid schedule.

## Q10

**Correct answer:** B

**Concept:** General Aptitude — Two- and three-dimensional patterns

1. Each stack at row i, column j is at most min(row maximum i, column maximum j). The componentwise largest arrangement is rows [2,3,1] and [2,2,1], with 11 cubes; it meets every projection.
2. Each column must attain its maximum, so at least 2+3+1=6 cubes are needed.
3. Rows [0,3,1] and [2,0,0] attain all required row and column maxima with exactly 6 cubes. Thus both bounds are achievable.

- **A:** The displayed 6-cube construction disproves a minimum of 7.
- **B:** It gives the two attainable bounds.
- **C:** The per-stack upper bounds sum to only 11.
- **D:** Both numbers exceed attainable tight bounds.

**Common misconception:** Projection heights are maxima, not sums; each visible peak can serve both a row and a column constraint.

## Q11

**Correct answer:** 4 (accepted exactly as entered at the stated precision)

**Concept:** Computer Organization and Architecture — Cache mapping

All references map to set 0. References 0 and2 miss and fill both lines. The next0 hits and makes2 least recently used. Reading 4 misses and evicts 2. The final2 therefore misses, evicting0. There are four misses; set 1 is unused.

**Common misconception:** Total cache capacity does not prevent conflicts when blocks map to one set.

## Q12

**Correct answer:** C

**Concept:** Programming and Data Structures — Trees

A is the root. Its first subtree must contain B,C because B closes at the second postorder position; its other subtree contains D,E. Thus A has two children, B and D. B has only child C and D has only child E. Either only child may independently be placed left or right, giving 2*2=4 trees.

- **A:** False: traversals do not specify which side holds an only child.
- **B:** False: there are two independent only-child choices, not one.
- **C:** True: two independent left/right choices give four.
- **D:** False: A must have two children; it does not contribute a third binary choice.

**Common misconception:** Preorder and postorder can fix subtree membership without fixing the side of an only child.

## Q13

**Correct answer:** 6 (exact)

**Concept:** Algorithms — Divide and conquer

1. Merging seven distinct keys takes at most six comparisons.
2. If the four-key left run were exhausted within five comparisons, at most one right key would have been emitted. At most four cross inversions would then be possible.
3. If the three-key right run were exhausted within five comparisons, at least two left keys would remain. Each exceeds all three right keys, forcing at least six cross inversions.
4. Both possibilities contradict exactly five inversions, so six comparisons are necessary. Left [1,3,5,6] and right [2,4,7] attain five inversions and six comparisons.

**Common misconception:** The inversion constraint limits when a run can be exhausted; the inversion count itself is not the comparison count.

## Q14

**Correct answer:** B

**Concept:** Computer Organization and Architecture — Interrupts and DMA

DMA reads main memory rather than the processor's dirty cache copies. Writing back the buffer lines and waiting makes main memory contain the updates before DMA reads them. Discarding dirty lines loses modifications. Interrupt control changes notification, not visibility of cached data, and a completion event cannot precede starting the transfer.

- **A:** False: discarding dirty lines without write-back loses the updated data.
- **B:** True: completed write-back makes the DMA source in main memory current.
- **C:** False: interrupt masking does not update memory.
- **D:** False: this ordering cannot start the required transfer and does not flush the cache.

**Common misconception:** DMA bypassing the CPU does not automatically observe its dirty cache contents.

## Q15

**Correct answer:** B

**Concept:** Algorithms — Graph traversals

Nested intervals show that u is a proper ancestor of v in the DFS forest. The tree path from u to v consists of directed edges. Adding v→u closes a directed cycle; v→u is a back edge. Thus only B follows.

- **A:** False: a tree edge runs from an ancestor to a newly discovered descendant, not back to an ancestor.
- **B:** True: the tree path u to v together with v→u is a directed cycle.
- **C:** False: the nested intervals identify an ancestor relationship, not separate branches.
- **D:** False: this return edge closes a cycle.

**Common misconception:** Nested DFS intervals alone do not imply acyclicity; edge direction matters.

## Q16

**Correct answer:** A, C, D

**Concept:** Programming and Data Structures — Binary search trees

With a nonempty right subtree, the successor is its minimum-key node, found by following left-child links from x's right child. It therefore lies in that subtree and has no left child. It can have a right child: for root 10 with children5,15 and node15 having right child 20, the successor of 10 is 15. Hence A,C,D hold and B fails.

- **A:** True: successor is the minimum of the nonempty right subtree.
- **B:** False: the minimum node can have a right child.
- **C:** True: a left child would have a smaller key in that same subtree.
- **D:** True: a right child does not violate minimality in the right subtree.

**Common misconception:** The successor's lack of a left child does not make it necessarily a leaf.

## Q17

**Correct answer:** 3 (accepted exactly as entered at the stated precision)

**Concept:** Theory of Computation — Regular expressions and finite automata

Initially the closure is{0}. After the first a it is{0,1,2}; after the second a, only 0 has an a transition, again giving closure{0,1,2}. On b only 2 moves, producing{3}. Its epsilon closure adds1 and then2, so the final set is{1,2,3}, size 3.

**Common misconception:** Epsilon closure must be recomputed after the last input symbol, including chains of epsilon edges.

## Q18

**Correct answer:** A

**Concept:** Compiler Design — Local optimization

Write initial values b0,c0. The first statement sets a=b0+c0. The second sets b=(b0+c0)-c0=b0. The third reads this restored b and sets c=(b0+c0)-b0=c0. Thus b and c end unchanged, and only a=b+c is required.

- **A:** True: a becomes the sum and b,c retain their original values.
- **B:** False: it changes b whenever b0 differs from c0.
- **C:** False: it changes c to b0+c0 rather than preserving c0.
- **D:** False: it generally changes both b and c.

**Common misconception:** Algebraic simplification must track which version of each variable an expression uses.

## Q19

**Correct answer:** D

**Concept:** Theory of Computation — Context-free grammars

The base production generates ab. To generate aabb one must add one leading a and one trailing b; choosing aS at the root and then Sb, or Sb at the root and then aS, gives distinct trees with the same yield. The other strings require zero or only one extra production and therefore have unique trees.

- **A:** False: only the base production generates this length-two string.
- **B:** False: the sole extra a must come from one aS production.
- **C:** False: the sole extra b must come from one Sb production.
- **D:** True: the leading-a and trailing-b productions can nest in either order.

**Common misconception:** Ambiguity concerns distinct parse trees, not merely multiple derivation orders for one tree.

## Q20

**Correct answer:** 4 (accepted exactly as entered at the stated precision)

**Concept:** Computer Networks — Distance-vector and link-state routing

Initially dA=2 and dB=1. In round 1 B loses its direct link and uses A's previous 2, giving 3. A still uses B's previous 1 and remains 2. In round 2 A uses B's3 and obtains min(10,1+3)=4. B uses A's previous 2 and remains 3. The requested advertised metric is 4, not the true surviving shortest-path distance 10.

**Common misconception:** Synchronous distance vectors use previous-round advertisements, which can retain routes through the failed link.

## Q21

**Correct answer:** A, C

**Concept:** Digital Logic — Floating-point representation

Near 1 the spacing is 1/4, so1.125 is halfway between 1.00(binary) and1.01(binary); the even last significand bit selects1.0. In[2,4), spacing doubles to1/2. The sum 1.75+0.25=2 is exactly representable. At[8,16), spacing is 2, so9 is not representable. A,C hold.

- **A:** True: it is a midpoint and ties-to-even chooses significand1.00.
- **B:** False: the spacing in this exponent binade is 0.5.
- **C:** True: both inputs and the exact sum are representable.
- **D:** False:9 lies between consecutive representable values8 and10.

**Common misconception:** Floating-point spacing depends on the exponent, and midpoint rounding depends on the retained low bit.

## Q22

**Correct answer:** A, C

**Concept:** Engineering Mathematics — LU decomposition

1. Eliminate column 1 to obtain rows [1,2,1], [0,t-4,1], [0,1,0]. Expanding along column 1 gives determinant -1 for every t.
2. At t=4 the second pivot is zero while the entry below it is 1. In any unit-lower LU decomposition the forced leading U block would have U22=0, making the required A32 residual impossible. Row exchange fixes this, giving trailing block diag(1,1).
3. At t=5, the second pivot is 1 and eliminating the last row gives U33=-1, not 1.

- **A:** The trailing 2-by-2 determinant is (t-4)*0-1=-1.
- **B:** Nonsingularity does not ensure all unpivoted pivots exist; t=4 is a counterexample.
- **C:** The swapped trailing rows are [1,0] and [0,1].
- **D:** The last elimination subtracts the second trailing row and produces -1.

**Common misconception:** An invertible matrix may still require pivoting for a particular elimination order.

## Q23

**Correct answer:** A, D

**Concept:** Compiler Design — Constant propagation

Both concrete paths give x+y=5, proving A. At the join, x has values2 or3 and y has3 or2; each independently becomes not constant. This abstraction loses the relation x+y=5 and cannot evaluate the sum as a constant there. Evaluating within each branch first produces the same constant 5 for z on both incoming paths, which survives the join. Thus D holds, B,C do not.

- **A:** True: the two concrete branch sums both equal5.
- **B:** False: x differs between the incoming paths.
- **C:** False: independent unknown values do not retain their correlation.
- **D:** True: equal incoming constants for z survive the join.

**Common misconception:** A property true on every path may be lost by an abstraction that forgets correlations.

## Q24

**Correct answer:** 0.667 (accepted exactly as entered at the stated precision)

**Concept:** Engineering Mathematics — Integration

1. The two expressions cross at x=1/3. The maximum is 1-2x to its left and x to its right.
2. The two integrals are [x-x^2] from 0 to 1/3 = 2/9 and [x^2/2] from 1/3 to 1 = 4/9.
3. Their sum is 2/3, which rounds to 0.667.

**Common misconception:** Integrate the upper expression separately on each side of its crossover.

## Q25

**Correct answer:** A

**Concept:** Compiler Design — Liveness analysis

1. At P, z is immediately read to assign y. After the back edge to L, flag is read by the branch before any assignment to flag.
2. The old y is overwritten at P. The old x is overwritten at L before either a return or another loop iteration could read x.
3. Hence the live set is exactly {z, flag}.

- **A:** Correct: both variables have a future use before redefinition.
- **B:** Incorrect: the old x is killed at L.
- **C:** Incorrect: the old y is killed at P.
- **D:** Incorrect: neither old x nor old y survives to a use.

**Common misconception:** A variable used elsewhere in a loop need not be live at every point; track the current value across the back edge.

## Q26

**Correct answer:** C

**Concept:** Digital Logic — Boolean algebra

The two occurrences of x cancel under XOR. If z=0, both AND terms are0 and D=0. If z=1, their values are y and NOT y, whose XOR is 1. Thus D=z independently of x and y.

- **A:** False: when x=0,z=1 the result is 1.
- **B:** False: when y=0,z=1 the result is 1.
- **C:** True: flipping y affects F exactly when z=1.
- **D:** False: z=0 yields D=0, not 1.

**Common misconception:** A Boolean input's influence may be gated by another variable even when the output also contains XOR.

## Q27

**Correct answer:** 2 (accepted exactly as entered at the stated precision)

**Concept:** Operating Systems — CPU scheduling

A runs0–2, leaving5. B arrives with 4 and runs2–4, leaving2. C runs4–5 and completes; B resumes5–7 and completes; A runs7–12. Waiting times are A:12-0-7=5, B:7-2-4=1, C:5-4-1=0. Average=(5+1+0)/3=2.

**Common misconception:** Preemption compares remaining time, and waiting time includes intervals after preemption.

## Q28

**Correct answer:** C

**Concept:** Databases — Functional dependencies and normal forms

Neither A nor B determines C, so candidate keys are AC and BC. Every attribute is prime because each occurs in a candidate key. Each nontrivial dependency has a prime right-side attribute, satisfying 3NF. A→B violates BCNF since A is not a superkey, and similarly for B→A. Thus 3NF but not BCNF.

- **A:** False: every attribute is prime, so there is no nonprime partial dependency violating 2NF.
- **B:** False: prime right-side attributes satisfy 3NF.
- **C:** True:3NF holds while A and B are non-superkey determinants.
- **D:** False: A→B is nontrivial and A does not determine C.

**Common misconception:** Third normal form allows a prime dependent attribute even when the determinant is not a superkey.

## Q29

**Correct answer:** 7.6 (accepted exactly as entered at the stated precision)

**Concept:** Engineering Mathematics — Descriptive statistics

1. The combined mean is (3*2+2*7)/5=4.
2. The mean square in A is 2+2^2=6, and that in B is 1+7^2=50. The combined mean square is (3*6+2*50)/5=118/5.
3. Subtract the square of the combined mean: 118/5-16=38/5=7.6.

**Common misconception:** Pooling variances requires accounting for different group means as well as group sizes.

## Q30

**Correct answer:** 175 (accepted exactly as entered at the stated precision)

**Concept:** Computer Networks — IPv4 fragmentation

The incoming payload is 1000 bytes. Each new fragment can hold620-20=600 payload bytes, and600 is divisible by 8. The first retains offset 100. The second begins600 bytes later, so its offset is 100+600/8=175. Offsets remain relative to the original datagram, not relative to the incoming fragment.

**Common misconception:** Refragmentation adds to the existing fragment offset rather than restarting at zero.

## Q31

**Correct answer:** 205 (exact)

**Concept:** Operating Systems — I/O scheduling

1. The head reaches 70 at time 20 and 90 at time 40, then reverses toward the pending request at 10.
2. At time 45 it is at 85, moving downward. The new request at 95 is behind its direction of travel, so it does not interrupt this sweep.
3. The head reaches 10 at time 120 and then travels 85 cylinders to 95. Total movement is 20 + 20 + 80 + 85 = 205.

**Common misconception:** A request arriving near the head is not necessarily served next; LOOK preserves the sweep direction while a request remains ahead.

## Q32

**Correct answer:** C

**Concept:** Computer Organization and Architecture — Pipelining and hazards

If the first ADD is fetched in cycle1, it writes R1 in cycle5. The second ADD's ID must be no earlier than5, so its IF must be4: two NOPs are needed between them. The second then writes R2 in cycle8, so the third's ID must be8 and IF7: two more NOPs. Four total suffice and fewer cannot meet both dependencies.

- **A:** False: two NOPs repair only one of the two immediate dependencies.
- **B:** False: at least two separations of two NOPs each are required.
- **C:** True: both consumer ID stages coincide with the corresponding producer WB stages.
- **D:** False: same-cycle write-before-read permits two, not three, NOPs per dependency.

**Common misconception:** A producer's EX completion does not make its result available without forwarding.

## Q33

**Correct answer:** D

**Concept:** Engineering Mathematics — Monoids and groups

1. The inverses are f-inverse(x)=3x mod 5 and g-inverse(x)=x-1 mod 5.
2. Apply the maps right to left: x becomes x-1, then 3x-3, then 3x-2, then 6x-4, which is x+1 modulo 5.
3. Thus h is a translation by 1; its k-fold application is x+k, equal to x for every residue exactly when k is a multiple of 5.

- **A:** h is not identity; it maps 0 to 1.
- **B:** Two applications map 0 to 2.
- **C:** The order of f alone is 4, but h is a different permutation.
- **D:** Five is the least positive translation count returning every residue.

**Common misconception:** Composition order matters when the permutations do not commute.

## Q34

**Correct answer:** C

**Concept:** Databases — File organization

If the first record is at slot 0, the 16 records occupy two pages. If it starts at any slot 1 through7, the 16 consecutive records cross into a third data page. Thus at most three data pages are needed, and this is attainable. Add two index reads for a largest total of 5.

- **A:** False: this counts only the worst-case data pages and omits the index reads.
- **B:** False: it assumes the range begins exactly at a page boundary.
- **C:** True: three data pages plus two index pages attain the maximum.
- **D:** False: sixteen consecutive records cannot span four eight-record pages.

**Common misconception:** A contiguous record range can span one extra page because its first record need not be page-aligned.

## Q35

**Correct answer:** A, B

**Concept:** Engineering Mathematics — Graph connectivity matching and colouring

1. The degree sum is 14, so the handshake lemma gives 7 edges.
2. G is connected and has exactly two odd-degree vertices. It therefore has an open Euler trail.
3. For a counterexample to both remaining assertions, take two disjoint triangles and connect one vertex of each by one bridge. The bridge endpoints have degree 3 and all others degree 2. The triangles exclude bipartiteness; the bridge excludes a Hamiltonian cycle.

- **A:** Each undirected edge contributes twice to the degree sum.
- **B:** Connectedness and exactly two odd vertices are sufficient.
- **C:** The two-triangle bridge construction has an odd cycle.
- **D:** A Hamiltonian cycle cannot cross a bridge and return without reusing it.

**Common misconception:** A degree sequence can force an Euler trail without forcing bipartiteness or a Hamiltonian cycle.




