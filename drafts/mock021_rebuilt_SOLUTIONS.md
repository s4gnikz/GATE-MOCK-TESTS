# Worked Solutions — GATE CS 2027 Mock Test 021

## Q1

**Correct answer:** A

Q establishes the discrepant readings; S explains the diagnosis; P describes the repair; R gives the subsequent test. Thus Q,S,P,R is required. B uses “this discrepancy” before its referent and puts the second trial before repair. C diagnoses the defect after the repair and trial. D introduces repair before the problem. Follow explicit references and causal dependencies, not just grammatical possibility.

## Q2

**Correct answer:** 0.2000 (accepted range 0.19995–0.20005)

There are six equally likely unordered pairs. One is two red, one two blue and four mixed. The report excludes the blue pair, leaving five pairs; one is all red. The probability is1/5. The observer did not reveal that a particular designated draw was red, which would define a different condition.

## Q3

**Correct answer:** B

The clause beginning “only if” imposes a condition on the endorsement. Thus B is the contextual meaning. A is the occupational sense of qualified, C wrongly asserts withdrawal, and D contradicts the stated reservation. Interpret vocabulary through its surrounding claim.

## Q4

**Correct answer:** 32

Let X=log2(x), Y=log2(y). Then X+Y=7 and X−Y=3, so X=5 and x=32. Solving for a logarithm is not the same as returning the original variable.

## Q5

**Correct answer:** A

For digit string ab, both RS and SR produce(9−b)(9−a): digitwise replacement commutes with reversal. A is true. R² and S² each restore the original string, so B and C are false in general. D fails, for example, on12, which becomes78. A transformation being its own inverse does not make the composite the identity.

## Q6

**Correct answer:** 72

The original exterior area is54. Removing the six face-centre cubes removes six outward faces, leaving48. Each of those removed cubes exposes four faces on retained adjacent cubes, adding24. Its inward neighbour is the removed central cube, so there is no additional retained face in that direction. The central cube's six neighbours are all removed. Total48+24=72. Count retained-to-empty interfaces, not the surfaces of removed cubes.

## Q7

**Correct answer:** 46

The given terms imply3u+2v=8 and8u+3v=19. Eliminating v gives u=2, then v=1. The fifth term is2×19+8=46. The declared recurrence, rather than an arbitrary extrapolation, fixes the answer.

## Q8

**Correct answer:** 2

Each square has area16. An area28 union implies overlap32−28=4. The overlap is a square of side4−t, so(4−t)²=4. Because0≤t≤4, 4−t=2 and t=2. The other algebraic root lies outside the allowed displacement range.

## Q9

**Correct answer:** B

B attaches both participial actions to the engineer, who also recommends closure. A makes “cracks” the grammatical subject of having inspected. C incorrectly attributes the recommendation to cracks and misattaches inspection. D explicitly reverses the inspector and inspected object. The introductory modifier must attach to the intended actor.

## Q10

**Correct answer:** 100

Original expenditure is60×50+40×75=6000. New unit prices are60 and90. If a units come from A, the cost is60a+90(100−a)=6000, yielding a=100. A20% price rise cannot be offset by merely reducing one supplier's share by20%; use the weighted cost equation.

## Q11

**Correct answer:** 124

There are100 issue slots for actual instructions and12×2=24 lost slots for taken branches. Total124. Untaken branches cause no penalty under the stated model; pipeline filling and draining are explicitly excluded.

## Q12

**Correct answer:** B

p initially points to B. The second assignment connects A to C. The third connects B to A, and the final assignment moves head to B. The reachable list is B→A→C. Thus B is correct; A and C place the links in different orders, while D ignores the rewiring. Trace node identities separately from pointer-variable names.

## Q13

**Correct answer:** 4

A can produce0,1,2 or3 copies of a, with B producing the remainder. Each split has a unique parse within A and B, giving four trees. Although each component grammar is unambiguous, their concatenation has an ambiguous boundary.

## Q14

**Correct answer:** B, C

R∩S contains only the three diagonal pairs, proving B. R∪S includes(1,2) and(2,3) but not(1,3), so A and D are false. Transitive equivalence closure connects all three elements, making C true. A union of equivalence relations need not itself be an equivalence relation.

## Q15

**Correct answer:** B

The query selects every domain value absent from a finite relation; over the infinite domain this is infinite and includes values outside the active domain. B is correct and A false. Negation can be safe when variables are appropriately range-restricted, so C is false. Complementation does not reproduce R, making D false. Finiteness of stored input does not ensure safety of an unrestricted query.

## Q16

**Correct answer:** 92

The next instruction begins at104. The signed scaled displacement is2×(−6)=−12. Target104−12=92. Distinguish the current PC from the architecture's specified next-instruction base.

## Q17

**Correct answer:** B

Greedy chooses6,1,1: three coins. Two4 coins suffice, and one coin cannot equal8, so the optimum is two. B is correct. A wrongly describes the greedy output; C gives both counts incorrectly; D ignores valid representations. Greedy optimality depends on the denomination system.

## Q18

**Correct answer:** 5

The first SELECT emits four rows. In the second, only2 satisfies x<>1; NULL yields UNKNOWN and is excluded. UNION ALL retains duplicates, giving4+1=5 rows. Neither deduplication nor treating NULL as an ordinary unequal value is valid here.

## Q19

**Correct answer:** 3

An idempotent has eigenvalues0 or1 and is diagonalizable because its annihilating polynomial t(t−1) has distinct roots. Trace3 gives a three-dimensional1-eigenspace. That eigenspace is exactly ker(I−P), whose dimension is3. Do not confuse it with ker(P), of dimension1.

## Q20

**Correct answer:** A, B

If both read0 before either writes, both write1, giving A. If one increment completes before the other's read, the result is2, giving B. Shared memory supplies visibility/storage, not atomic compound operations, so C is false. Each computed write is based on0 or1, and only two increments occur, so3 cannot arise; D is false. Lost updates are possible without mutual exclusion or atomic increment.

## Q21

**Correct answer:** 3

Rolle's theorem gives at least four distinct roots of f' between consecutive roots of f, and then at least three roots of f''. A degree-five polynomial with five distinct real roots has a cubic second derivative, showing three is attainable. Repeated application supplies a lower bound, while degree supplies attainability.

## Q22

**Correct answer:** 4

Apply both next-state equations to the old state simultaneously:00→01→11→10→00. The first return takes four edges. Sequentially updating one bit and feeding that new value into the other would model a different circuit.

## Q23

**Correct answer:** 0.75

P(B and defective)=0.5×0.3=0.15. Total defective probability is0.5×0.1+0.5×0.3=0.20. The posterior is0.15/0.20=0.75. Equal factory-selection probabilities do not imply equal probabilities after defect information.

## Q24

**Correct answer:** C

To pop3 first,1 and2 must already be below it. After removing3,2 blocks1, so3,1,2,4 is impossible. A is obtained by pushing1,2, popping both, then pushing3,4 and popping both. B is obtained by pushing1,2,3, popping all, then pushing/popping4. D pushes all and pops all. LIFO constrains relative accessibility, not just membership of outputs.

## Q25

**Correct answer:** A, B, D

A downward scan reads dp[c−w] before that lower entry is updated for the current item, preventing its reuse; A is true. Upward scanning can read already updated values, so B is true and C false. For the example, dp[2]=3 before dp[4] is updated from dp[2]+3=6, proving D. Space compression must preserve the original DP dependency layer.

## Q26

**Correct answer:** 4

Compute t1=a+b, t2=c−d, t3=t1*t2, and result=t3+t1: four binary operations. There are four distinct required operation nodes in the expression DAG under the restriction against reassociation. Counting the repeated a+b twice would miss reuse.

## Q27

**Correct answer:** B

B rechecks the predicate while holding the mutex after every wakeup. A fails on a spurious wakeup or when another thread consumes the condition first. C races with changes to ready. D can prevent another process from acquiring the mutex to make ready true. A wakeup is a reason to recheck, not proof of the predicate.

## Q28

**Correct answer:** 2

One resource remains free. It can satisfy either process's outstanding request; that process then finishes and releases its two resources. Both processes are possible first finishers, so the answer is2. Holding one resource each does not imply deadlock while a suitable resource is still free.

## Q29

**Correct answer:** 2

A has subtrees rooted at B and C. B has leaves D and E in the uniquely determined left/right order. C has the sole child F. Preorder and postorder cannot distinguish whether that sole child is left or right, giving exactly two trees. No other unary node exists. Distinct labels make inorder plus preorder unique, but preorder plus postorder can retain unary-child ambiguity.
## Q30

**Correct answer:** A, C, D

An odd number of bit flips toggles parity and is detected, proving A and D. An even number leaves total parity unchanged, disproving B. Flipping one data bit and the parity bit is an example of two undetected flips, proving C. Include the parity bit itself when counting errors.

## Q31

**Correct answer:** 6

The elements in the given set divisible by both2 and3 are6 and12. Under divisibility,6 precedes12, so6 is their least upper bound. The numerically largest common multiple is not the join.

## Q32

**Correct answer:** 60

The operands are24/16=1.5 and40/16=2.5. Their product is3.75, encoded with four fractional bits as3.75×16=60. Equivalently multiply the raw encodings and shift right by four:960/16=60. Raw multiplication initially doubles the fractional-bit count.

## Q33

**Correct answer:** A, C

The empty string begins and ends with an empty stack, so A is true. Every accepted prefix avoids a pop from empty, establishing C. Equal totals are insufficient: '())(' has equal totals but its third character tries to pop an empty stack. Thus B and D are false. Global balance and prefix balance are separate requirements.

## Q34

**Correct answer:** C

The first assignment makes x=0, so y=b. The later x=7 does not change the previously stored y. C is correct. A incorrectly uses the later x, B ignores multiplication by zero, and D loses the contribution of b. Track definitions at their points of use.

## Q35

**Correct answer:** 0.25

Conditional on any allowed choice2,3 or4 by A, independent B matches that choice with probability1/4. Averaging the same probability over those three choices leaves1/4. Restricting A's choices does not restrict B's independent choices.

## Q36

**Correct answer:** B, C

The shortest-path equality gives dist(v,d)=dist(u,d)−cost(u,v)<dist(u,d), so B is true. A directed cycle would require a strict descent back to the original distance, impossible; A is false. In a finite graph, an indefinitely continuing route would repeat a vertex, so with a next hop at every non-destination it must reach d; C is true. Zero-cost edges allow equality and can create cycles among tied next hops, so D is false. Exact distances and strictly positive costs are essential assumptions.

## Q37

**Correct answer:** B, C

Write L=[[1,0],[l,1]] and U=[[u,v],[0,w]]. Matching A forces u=0 and lu=1, impossible. Nonzero determinant−1 still proves invertibility, making C true and A false. Swapping rows gives[[1,1],[0,1]], already upper triangular, so L=I works and B is true. Invertibility guarantees a unique solution for every b, disproving D. Failure of unpivoted elimination is not singularity.

## Q38

**Correct answer:** B

The first update temporarily gives both rows code B, violating immediate uniqueness. The completed swap has distinct codes B and A, so commit-only validation can accept it. B is correct. A overlooks the intermediate violation; C contradicts the specified check timing; D confuses the code column with the unchanged primary keys. Constraint timing can affect executability without changing final-state validity.

## Q39

**Correct answer:** 6

The schedule is P:[0,1), Q:[1,3), R:[3,4), Q:[4,6), P:[6,12). Waiting time equals completion minus arrival minus CPU requirement: P=12−0−7=5, Q=6−1−4=1, R=4−3−1=0. Total6. A process's remaining time, rather than its original demand, determines preemption.

## Q40

**Correct answer:** A, C

Both incoming definitions assign the same constant2, so their join retains x=2. The second condition is therefore true and z=7, proving A and C. The program does not assign y, so B is false. A join of equal constants preserves that constant, not the nonconstant value, making D false. Multiple reaching definitions are not by themselves evidence of varying values.
## Q41

**Correct answer:** 63

The recursion has64 singleton leaves and each non-leaf has two children, so it has63 internal nodes. Each internal node performs exactly one boundary test; no comparisons occur in skipped merges. Total63. The ordinary mergesort n log n bound is not the exact cost of this adaptive sorted-input execution.

## Q42

**Correct answer:** A, B, D

A PDA can match the a and b blocks of L1 and then ignore the c count; similarly L2 matches b and c, proving A. Simultaneously satisfying both equalities forces all three counts equal, proving B. This intersection is the standard non-context-free three-equal-block language, disproving C. Context-free languages are closed under union, so D is true. Closure under union must not be confused with closure under intersection.

## Q43

**Correct answer:** 22

The predecessor of root8 is7, the largest key in its left subtree. Copying7 to the root and deleting its old leaf leaves the search path for5 as7→4→6→5. The sum is7+4+6+5=22. The predecessor comes from the left subtree, not the smallest right-subtree key10.

## Q44

**Correct answer:** 5

Integration by parts gives integral(x f')=[x f] from0 to2−integral(f)=2f(2)−0f(0)−3=8−3=5. f(0) need not be known because its boundary coefficient is zero. The endpoint and integral information together determine the answer without reconstructing f.

## Q45

**Correct answer:** 258

LOOK travels50→70→20, distance20+50=70. SCAN travels50→199→20, distance149+179=328. The excess is328−70=258, twice the unnecessary outward distance199−70. Both stop at20 because no requests remain; do not add a final sweep to cylinder0.

## Q46

**Correct answer:** A, C

Reusing the same tag can match an old virtual-page entry and produce an obsolete frame, making A true. Invalidating the tag's entries removes those stale hits, so C is true. ASIDs distinguish concurrently assigned address spaces only when reuse is managed; B is false. The lookup key in the question omits the page-table base, so changing that base alone does not guarantee a miss, making D false.

## Q47

**Correct answer:** 2

First100+60=160 exceeds127, wraps to−96 and overflows. Then−96−60=−156 is below−128, wraps to100 and also overflows. Both operations signal overflow, although the final wrapped result equals the original x. Algebraic cancellation of the final result does not eliminate intermediate overflow flags.

## Q48

**Correct answer:** A, C

The shared attribute is Z, and Z→ZY, so the intersection determines R2, establishing a lossless binary decomposition; A is true. R2 has Z as a key and R1 has no nontrivial projected dependency, so both are BCNF and C is true. The projected dependencies provide Z→Y but cannot derive XY→Z, so B is false. Z does not determine X and is not necessarily a key of R, disproving D. Losslessness and dependency preservation are separate properties.

## Q49

**Correct answer:** 8

With four significant binary bits, representable values near8 are8=1.000×2³ and9=1.001×2³, spacing1. The exact sum8.5 is halfway; ties-to-even picks8 because its trailing significand bit is0. The second addition again rounds8.5 to8. Thus the result is8, although performing the exact sum first would give9. Rounding after each operation is consequential.

## Q50

**Correct answer:** 2

At c=0, XOR differs from OR only when a=b=1. At c=1, the comparison expression is always1, whereas f=a OR b is0 only when a=b=0. These are two distinct input assignments. Condition on c before comparing the Boolean functions.

## Q51

**Correct answer:** A, C

After line2 there exists a path through line3 that uses x before redefining it, so may-liveness includes x and A is true. On the path beginning at line5, x is never used, making B false. Line6 uses y, so C is true. The existence of a path using line1's definition prevents deleting it as dead; D is false. May-liveness takes a union over possible successors, not an intersection.

## Q52

**Correct answer:** 2

Deleting1 gives provisional[7,4,2,8,5,3]. Swapping down through2 and then3 gives[2,4,3,8,5,7]. Insert0 at index7 and swap with its parent at3, then with the root. Final array[0,4,2,8,5,7,3] has2 at index3. Reheapification uses actual parent/child positions, not global sorting.

## Q53

**Correct answer:** 896

Encoded widths are3 for eight choices,3 for five choices and4 for arbitrary enable subsets, total10. Horizontal width is8+5+4=17. Saving7 bits per word across128 words gives896 bits. Independent enables cannot be reduced to the logarithm of four because all16 subsets must be representable.

## Q54

**Correct answer:** 275

The first MTU permits1000 payload bytes, already divisible by8, giving payload lengths1000,1000,400 and offsets0,125,250. The final400-byte payload is split into200 and200 bytes for MTU220. Their offsets remain relative to the original payload:250 and250+200/8=275. Refragmentation does not reset offsets to zero.

## Q55

**Correct answer:** 2

The free addresses are.64 through.191, totaling128. This interval is not aligned to a /25 boundary; a single /25 starts at.0 or.128 and would include reserved addresses. Two /26 prefixes,.64/26 and.128/26, cover the interval exactly. Address count alone does not establish CIDR alignment.

## Q56

**Correct answer:** 14

The combined mean is5. The within-group variance average is(1+9)/2=5. Each group's mean is3 from the combined mean, so the between-group contribution is9. Total population variance is5+9=14. Averaging variances alone omits the spread of group means.

## Q57

**Correct answer:** A, C

The two unequal(a,b) assignments give the two products in A, independent of c,d. Each leaves two variables free and covers four inputs, proving C. Their eight inputs do not form one cube: spanning01 and10 while omitting a,b would also cover00 and11 zeros. Thus B and D are false. Power-of-two cardinality is necessary but not sufficient for a valid Karnaugh group.

## Q58

**Correct answer:** 1

The graph is connected with five vertices and five edges. Its real signed incidence matrix has rank n−1=4, so rank-nullity gives kernel dimension5−4=1. The triangle supplies the single independent cycle; the edges to4 and5 do not add cycles. Arbitrary edge orientation changes signs, not rank.

## Q59

**Correct answer:** 3

Each block stores floor((4096−96)/100)=40 records. Ranks39 and40 are in block1, ranks41–80 in block2 and ranks81–83 in block3. Thus three data blocks must be read. The in-memory directory costs no disk read and does not remove the need to read each block containing selected records.

## Q60

**Correct answer:** A, B

For1≤k≤p, p²<p²+k≤p²+p<(p+1)² because the gap to the next square is2p+1. Pumping y twice therefore produces a nonsquare length for every legal decomposition. A and B are true. No particular k needs to be chosen, so C is false. The contradiction disproves regularity, making D false. The uniform inequality is what handles the pumping lemma's existential decomposition.

## Q61

**Correct answer:** 1

DFS follows s→a→c→d, then returns to s and visits b. On b→c, c is already marked. All other edges first discover their targets, so exactly one examined edge has an already marked destination. Marking on entry prevents repeated exploration of the shared descendant.

## Q62

**Correct answer:** 4

By the Chinese remainder correspondence, modulo3 and modulo5 the equation x²=1 permits x=±1 independently. This gives2×2=4 residues modulo15:1,4,11,14. All are units. The group is not being assumed cyclic; a quadratic congruence over a composite modulus can have more than two roots.

## Q63

**Correct answer:** 3

The edge AD of weight2 is uniquely cheapest across the cut isolating D, so every MST includes it. Connecting A,B,C then requires two of the three unit triangle edges, with three choices. All have total weight4; using BD of weight3 would increase the weight. Thus there are3 MSTs. Equal edge weights allow distinct optimal trees without changing their common cost.

## Q64

**Correct answer:** A, C

Both branch paths evaluate the same unchanged expression, so A is true. However the then and else values are held in different names: t is not defined on the else path and u is not defined on the then path, disproving B and D. Hoisting the side-effect-free expression into a common temporary is legal under the given assumptions, proving C. Expression availability is different from availability of a particular temporary variable.

## Q65

**Correct answer:** A, C

Every string has finitely many predecessors in length-lexicographic order, and D halts on each. Therefore every member is eventually reached and printed, proving A. The enumerator continues testing strings even when L is empty or finite, so B is false and C true. Individual termination suffices for progress; no known uniform runtime bound is needed, disproving D. Enumeration need not announce when the final member has been printed.


