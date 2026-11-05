# Worked Solutions — Mock Test 097

## Q1

**Correct answer:** C

**Concept:** Necessary versus sufficient conditions in English.

“May enter only if accompanied” asserts entry implies accompaniment, without asserting its converse. C is correct. A asserts the converse, making accompaniment sufficient. B asserts both directions. D uses “unless” to authorize entry in the absence of accompaniment and does not express the required condition.

**Misconception:** Interchanging “if” and “only if”.

## Q2

**Correct answer:** D

The required numerical answer is **10**, so select **D**.

If the mass is M, initial value is50M. Removal subtracts5·50=250 and replacement adds5·40=200. Thus45M=50M−50, giving M=10. The removed uniform mixture has its existing average cost, not the cost of just one constituent.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 10 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -5 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q3

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Quantified deduction.

The witness that is both A and B is C and therefore not D, proving B. Every B is C and no C is D, proving D. A generalizes the one known A witness to every A. C asserts an overlap with D that is neither required nor supplied.

**Common misconception:** An existential premise cannot generally be promoted to a universal conclusion.

## Q4

**Correct answer:** 20

The first half-turn maps(3,4) to(−1,−4), and the second maps that to(1,8). The displacement is(−2,4), with squared length4+16=20. Half-turns about different centres do not cancel: their composition is a translation.

## Q5

**Correct answer:** B

**Concept:** Different statistics describe different features.

The average improved while the largest delay increased, precisely B. A need not hold because a worse maximum exists. Such changes can coexist, refuting C, and they do not determine the median, refuting D.

**Common misconception:** Assuming a smaller mean forces every observation or every other statistic to decrease.

## Q6

**Correct answer:** 84

**Concept:** Integer optimization with a capacity constraint.

Let x items use A and 20−x use B. Time is 2x+20−x=20+x≤28, so x≤8. Cost is 3x+5(20−x)=100−2x, decreasing in x. Choose x=8, giving cost 84 and exactly 28 hours.

**Common misconception:** Choosing the cheaper method for every item without checking time feasibility.

## Q7

**Correct answer:** 10

**Concept:** A target weighted rate.

After two days, 30 of 40 jobs are complete. With x Wednesday jobs, all completed, require (30+x)/(40+x)≥0.8. This simplifies to 0.2x≥2, or x≥10. Ten is feasible and achieves exactly 80%.

**Common misconception:** Averaging daily percentages without weighting the daily job counts.

## Q8

**Correct answer:** 12

The cut reaches x=4, so undoing that fold joins the two mirrored half-cuts into one rectangle of width2 and height1. Undoing the y=3 fold produces a second disjoint rectangle, at y from4 to5. Each hole has perimeter2(2+1)=6, for total12. The shared crease is not an internal hole boundary after unfolding; summing four separate unit-square perimeters would count it twice.

## Q9

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Calibration precedes the first trial: Q precedes R.
2. “This divergence” in S refers to R, and the successful repeat trial is the basis of P: R precedes S precedes P.
3. T follows receipt of the final report: P precedes T. Combining the constraints gives Q-R-S-P-T.
- Original option A: P cannot precede the repeat trial on which it is based.
- Original option B: Q explicitly precedes the first trial described in R.
- Original option C: This satisfies all four precedence links.
- Original option D: S cannot precede the divergence, and T cannot precede the report.

## Q10

**Correct answer:** 18
**Concept:** Boundary tracing of overlapping shapes.

The outer polygon can be traced through (0,0),(4,0),(4,1),(6,1),(6,3),(2,3),(2,2),(0,2). Its successive side lengths are 4,1,2,2,4,1,2,2, summing to 18. The portions hidden inside the overlap are not part of the outer boundary.

**Common misconception:** Adding the separate rectangle perimeters counts internal boundary segments.

## Q11

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Acceptance by a recognizer certifies membership, so A is true. A sufficiently long computation may still accept later, invalidating B's arbitrary cutoff. Deciders halt on every input, proving C; recognizers need not, disproving D.

## Q12

**Correct answer:** 3 (exact)

**Concept:** Theory of Computation — Regular expressions and finite automata

Initially the closure is{0}. After the first a it is{0,1,2}; after the second a, only 0 has an a transition, again giving closure{0,1,2}. On b only 2 moves, producing{3}. Its epsilon closure adds1 and then2, so the final set is{1,2,3}, size 3.

**Common misconception:** Epsilon closure must be recomputed after the last input symbol, including chains of epsilon edges.

## Q13

**Correct answer:** A, C

A uniform truth of either predicate guarantees their pointwise disjunction, proving A. One common witness proves both existential claims, proving C. On domain{1,2}, let P hold only at1 and Q only at2: this refutes both B and D. Separate witnesses need not coincide.

## Q14

**Correct answer:** 4

Concept: counting ordered compositions. Without a 3, only 1,1,1,1,1 works. With one 3, the remaining two 1s give 3,1,1; 1,3,1; 1,1,3. Two 3s exceed 5. Total four sequences. Counting unordered multisets would yield only two.

## Q15

**Correct answer:** A, C, D

This is write skew under the stated snapshot rule. The write sets are {A} and {B}, so both pass the conflict test and both flags become zero: A,C,D are true. In either serial order, the second transaction sees the first flag cleared and does not clear its own flag, making B false. Disjoint writes do not imply preservation of an invariant involving both items.

## Q16

**Correct answer:** 3

Insert index0, value4. Value2 removes4 from the back; value3 removes nothing. Before processing value1, index0 has already gone, so expiration removes nothing. Value1 removes3 and then2 from the back. Total back removals are1+0+2=3. Expiration removals and dominance removals are different operations.

## Q17

**Correct answer:** D

The required numerical answer is **3**, so select **D**.

**Concept:** Binary-search trace.

The compared keys are 8, then 12, then 14. The third comparison finds equality. Midpoint rounding and the stated inclusive halves determine this sequence.

**Common misconception:** The worst-case search depth is not necessarily the depth of a particular target.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q18

**Correct answer:** 3

Among R's children, A points to B and B to C: two sibling pointers. Among A's children, D points to E: one. C's sole child and last siblings have null right-sibling pointers. Total3. These pointers connect siblings, not parent-child pairs.

## Q19

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Correct mutex acquisition serializes the two regions, so no update is lost: A,B. Either thread may acquire first, disproving C. An unmatched unlock does not replace mutual exclusion and may itself be invalid, disproving D.

## Q20

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: essential prime implicants. Every column is covered by two rows, so no row uniquely covers a required minterm; B is true and A false. Any two rows cover all three columns, proving C. D is false: a cover need not contain an essential row. Covering many columns alone does not establish essentiality.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Shannon expansion and multiplexers.

At x=0, F=yz; at x=1, F=y+z. Thus B supplies the two cofactors. A reverses them; C fails when y=z=1 and x=0; D fails, for example, at x=y=z=0.

**Common misconception:** Interchanging the inputs selected by zero and one.

## Q22

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Aliasing and load reuse.

If p and q address different objects, the intervening store cannot alter *p, so u=t is valid (A). If they alias and the original value is 3, the first load gives t=3, the store writes 7, and the second load gives u=7 (C). That case refutes B and D.

**Common misconception:** Different pointer variable names do not prove distinct target objects.

## Q23

**Correct answer:** 96

The /25 route covers128 addresses, from.128 through.255. The more-specific /27 route removes32 addresses,.160 through.191, from B's traffic. Thus128−32=96 addresses go to B. These routing counts include network/broadcast-looking addresses because the question counts address matches, not assignable hosts.

## Q24

**Correct answer:** B, C

Incoming x is overwritten before use, so A is false. Incoming y is used to compute the new x and again in z, proving B. Both new x and y are needed by the second assignment, proving C. After z is assigned, only z is needed for the return, so D is false. Liveness concerns the current value's future use before redefinition, not whether the variable name occurs anywhere later.

## Q25

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Explicit communication interfaces.

Message passing uses message send/receive operations and can cross separate process address spaces, giving A,B. Application protocols can still race or deadlock, refuting C. Blocking implementations need not busy-wait, refuting D.

**Common misconception:** Treating the communication mechanism as a blanket correctness guarantee.

## Q26

**Correct answer:** 5

Left2 exceeds right1, contributing1; left5 exceeds only1, contributing1; left7 exceeds1,5,6, contributing3. Total5. Equal5 values are not inversions because the comparison is strict.

## Q27

**Correct answer:** 2

Concept: rank and consistency. Row three is row one plus row two; the first two rows are independent. Consistency requires 3=1+t, so t=2. Then rank is two in three unknowns, leaving one free parameter and infinitely many solutions. A dependent coefficient row does not guarantee consistency for arbitrary right-hand sides.

## Q28

**Correct answer:** C

The required numerical answer is **9**, so select **C**.

Concept: finite ticket-number wraparound. Eight outstanding contenders can hold the eight distinct ticket values, including the owner. The ninth issued ticket repeats the owner's value while it is still served, allowing a second contender to satisfy the entry test. Thus nine is the first unsafe outstanding count. Atomic issuance does not prevent modulo-counter aliasing.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 9 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q29

**Correct answer:** A

The required numerical answer is **2**, so select **A**.

The physical byte is selected by A0…A12, and the enabled region fixes A15,A14. Only A13 is free, giving two addresses per chip byte, separated by 8192. Partial decoding creates aliases rather than extra physical storage.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q30

**Correct answer:** 5

**Concept:** Hit lookup plus conditional miss penalty.

Every access costs two ns; a fraction 0.05 additionally costs 60 ns. The mean is 2+0.05×60=5 ns.

**Common misconception:** Charging the miss penalty on every access or excluding the cache lookup on a miss.

## Q31

**Correct answer:** C

**Concept:** Engineering Mathematics — Limits continuity and differentiability

1. Set r=|x|. Then f(x)=2 for r<=1 and f(x)=2r for r>1; equivalently f(x)=2 max(1,r).
2. When r<=1, the outer argument is -1 and g=2. When 1<r<=2, the outer argument 2r-3 lies in (-1,1], so g remains 2. When r>2, that argument exceeds 1 and g=4r-6.
3. Thus g is constant on [-2,2], linear with slope -4 on x<-2 and slope 4 on x>2. Only -2 and 2 have unequal one-sided derivatives. The original corners at +/-1 disappear under the composition.

- **A:** The outer function is constant across the relevant images around +/-1, so g has no corners there.
- **B:** This retains the original f corners incorrectly; g is constant around +/-1.
- **C:** At each of +/-2, the slope changes between zero and a nonzero value.
- **D:** The slopes on the two sides of +/-2 differ.

**Common misconception:** A composition can remove a corner of the inner function; the chain rule cannot simply be applied at nondifferentiable points.

## Q32

**Correct answer:** 16

There are eight inclusive ports per address and two addresses, giving16 distinct endpoint pairs. Distinguish the inclusive port count from4007−4000=7.

## Q33

**Correct answer:** C

The required numerical answer is **0.21**, so select **C**.

**Concept:** Bernoulli variance and affine transformation.

X+2Y=2−X. If p=P(X=1), its expectation is 2−p=1.7, so p=0.3. Translation and a sign change preserve variance: Var(2−X)=p(1−p)=0.3×0.7=0.21.

**Common misconception:** X and Y are dependent; adding their variances as if independent is invalid.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 0.58 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -0.10 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 0.40 and is outside the source answer's accepted range.


## Q34

**Correct answer:** 1

Concept: expressing exactly two related values. The existential part supplies two distinct B values and the universal part excludes any others. A=1 has exactly {a,b}; A=2 has only {a}; A=3 has {a,b,c}. Only A=1 qualifies, giving one. Existential witnesses alone would express at least two rather than exactly two.

## Q35

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If f mapped two distinct A elements together, their compositions would coincide, contradicting injectivity; A follows. Distinct points of f(A) also cannot be identified by g, proving C. g may identify points outside that image without affecting the composition, so B is not necessary. For example, embedding a smaller set in B need not be onto, disproving D.

## Q36

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reachability of and from negative cycles.

The reachable a→b→a cycle has weight −1; it can be repeated arbitrarily before continuing from b to c, so s-to-c walk weights are unbounded below (A). No edge from that component reaches t; the only s-to-t route has weight 5 (B). Thus C is false. c has no outgoing edges and cannot reach the cycle, refuting D.

**Common misconception:** A negative cycle affects destinations reachable from it, not every reachable vertex indiscriminately.

## Q37

**Correct answer:** 5000 (exact)

**Concept:** Computer Networks — Sliding receive and congestion windows

1. Initially the receive-window right edge is 1001+6000=7001, and the congestion-window right edge is 1001+8000=9001. The next new byte is 5001, so the sender may transmit 2000 new bytes, advancing next to 7001.
2. After ACK=3001, the receive-window right edge becomes 3001+3500=6501, behind the next new byte. Existing data remains outstanding; no additional new data is permitted at this step.
3. After ACK=5501, the receive edge is 10501 and the congestion edge is 5501+4500=10001. The binding edge is 10001. With next still 7001, the sender can transmit 3000 new bytes.
4. Total new data is 2000+0+3000=5000 bytes. The intervals are half-open, so no extra byte is added at an edge.

**Common misconception:** A receive window is anchored at the accompanying acknowledgement, and shrinking it does not retract previously transmitted data or reset the next sequence number.

## Q38

**Correct answer:** B, C

Write A=2I+N with N²=0 and N≠0. Then A⁵=32I+5×16N=32I+80N. This proves B,C and disproves D. The eigenspace solves Nv=0 and has dimension1, not2, so A is false. Repeated eigenvalues do not ensure diagonalizability.

## Q39

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If a spanning tree contained e, deleting e splits it into two components; the cycle contains another crossing edge with smaller weight, enabling a cheaper replacement. Hence no MST contains e, proving B and disproving A. The rest of the cycle provides a path around e, so C is true. When weights tie, replacing e need not reduce cost and e may belong to some MST, disproving D.

## Q40

**Correct answer:** B, C

Concept: path-sensitive available values. On the true path t is recomputed after a changes; on the false path a is unchanged and t=p=a+b. Thus t equals the current expression on both paths, making B and C true. A fails on the true path; D fails on the false path. A value can be available via a join even when an earlier temporary has been invalidated on one branch.

## Q41

**Correct answer:** A, B, D
**Concept:** Safety test after tentative allocation.

Initially only P2's need fits (1,1). Its completion releases (1,1), giving (2,2), after which P0 and P1 can finish in either order: exactly two sequences, proving A.

Granting P0 (1,0) leaves available (0,1) and needs (0,2),(2,0),(1,1). None fits, so B is true. Granting P1 (1,0) leaves available (0,1) and needs (1,2),(1,0),(1,1); none fits, so C is false. Granting P2 (1,0) leaves its need (0,1), which fits. It then releases its enlarged allocation (2,1), yielding (2,2), and both other processes can finish. D is true.

**Common misconception:** A request fitting currently available resources need not preserve a safe completion order.

## Q42

**Correct answer:** B

The required numerical answer is **5**, so select **B**.

**Concept:** Parse trees and Catalan recurrence.

Let C(n) count trees with n leaves. C(1)=1, and splitting the root's ordered children gives C(n)=Σ C(i)C(n−i). Thus C(2)=1, C(3)=2 and C(4)=1×2+1×1+2×1=5.

**Common misconception:** Counting derivation schedules instead of distinct tree structures.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 5 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q43

**Correct answer:** A

The required numerical answer is **22**, so select **A**.

The predecessor of root8 is7, the largest key in its left subtree. Copying7 to the root and deleting its old leaf leaves the search path for5 as7→4→6→5. The sum is7+4+6+5=22. The predecessor comes from the left subtree, not the smallest right-subtree key10.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 22 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -11 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q44

**Correct answer:** A, C
**Concept:** Dovetailing and enumeration of recognizable languages.

Dovetailing eventually performs every finite number of steps of every started simulation, so each accepting computation is eventually found (A). If L is finite, other simulations may loop forever and there is no general way to detect that no further member will be found; B is false. With L empty no simulation accepts, so an infinite silent run is possible (C). Waiting for a nonmember to print never terminates, refuting D.

**Common misconception:** An enumeration is evidence of membership when an item appears, not evidence of nonmembership when it has not yet appeared.

## Q45

**Correct answer:** D

The required numerical answer is **4**, so select **D**.

For f(x)=x³−3x, stationary points are±1. Checking those and endpoints±2 gives absolute value2 in all four cases; monotonicity between stationary points shows no larger value occurs. Alternatively f(x)=2 factors as(x−2)(x+1)²=0 and f(x)=−2 as(x+2)(x−1)²=0. The distinct maximizers are−2,−1,1,2, giving4. Count distinct locations rather than root multiplicities.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q46

**Correct answer:** 0

Two-edge paths yield(a,c),(b,c),(c,c). The two paths from a to c collapse into one tuple under set projection. Each resulting pair already belongs to E, so subtracting E leaves zero tuples. Self-loops create length-two paths but do not necessarily create new reachability pairs.

## Q47

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: negative edges and premature finalization. True best route s→b→a→t costs 5−4+3=4, so B is true and A false. Other routes cost 5 and 6. The graph is acyclic, so C is false. Dijkstra first finalizes a at two, sets t to five, and then chooses t before b at the specified tie, returning five, so D is true. The negative edge permits later improvement of an already-finalized distance.

## Q48

**Correct answer:** A

The required numerical answer is **0.3333**, so select **A**.

The joint probability of blue then red is(1/2)(1/3)=1/6. Red then red has probability(1/2)(2/3)=1/3. Thus P(second red)=1/2 and the requested posterior is(1/6)/(1/2)=1/3. Replacement plus reinforcement makes the two draws dependent.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 0.3334 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -0.1666 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by -0.0833 and is outside the source answer's accepted range.


## Q49

**Correct answer:** A

The required numerical answer is **3**, so select **A**.

**Concept:** Fan-in bounds and balanced XOR trees.

An output depending on eight distinct inputs requires at least seven two-input gates: merging eight independent input contributions into one output takes at least seven merges. A balanced tree uses four XORs in layer one, two in layer two, and one in layer three, achieving seven gates and delay three. A depth-d two-input circuit can depend on at most 2ᵈ inputs, so depth less than three cannot cover all eight. The minimum delay among minimum-gate circuits is therefore three.

**Common misconception:** A serial seven-gate chain has minimum gate count but not minimum delay.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q50

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The stream abc could split as a|bc or ab|c, so B is true. A length field can disambiguate such splits, proving C. TCP preserves bytes and order, not application record boundaries, so A,D are false. Network read sizes cannot replace a framing protocol.

## Q51

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** SQL CHECK and three-valued logic.

For B=3, the predicate is TRUE and passes. For NULL it is UNKNOWN, which is not FALSE and therefore passes under the specified semantics. Zero and −2 make the predicate FALSE and are rejected. The fresh primary keys remove key collisions from consideration.

**Common misconception:** Assuming CHECK(B>0) also imposes NOT NULL.

## Q52

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The HEX token stops after1 because G is outside[0-9A-F]; ID then matches G. This proves A and refutes B,D. The resulting token sequence may still violate the parser grammar, proving C. Lexical validity and grammatical validity are separate questions.

## Q53

**Correct answer:** 3

Concept: indexing conflicts and associativity. Mapping I puts all three even block numbers in set zero. Cycling through three blocks in a two-way LRU set yields six misses. Mapping II puts 0 and 4 in set zero, 2 in set one. Each fits after its first load, giving three misses. Difference=6−3=3. Total cache capacity alone does not prevent conflict misses.

## Q54

**Correct answer:** C

The required numerical answer is **958200**, so select **C**.

**Concept:** CPU overhead under different I/O mechanisms.

Interrupt-driven cost is 12000×80=960000 cycles. DMA uses twelve blocks, costing 12(120+30)=1800 cycles. Savings are 960000−1800=958200 cycles.

**Common misconception:** Omitting per-block setup or counting DMA completion interrupts per byte.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 958200 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -479100 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q55

**Correct answer:** D

The required numerical answer is **5.3333**, so select **D**.

**Concept:** Nonpreemptive scheduling with later arrivals.

J1 starts at zero and runs to five. Both others are then ready, so J3 runs 5–6 and J2 runs 6–8. Turnaround times are 5,7,4 respectively, averaging 16/3=5.333333…. Accepted range: 5.33325–5.33335.

**Common misconception:** Preempting J1 when a shorter job arrives despite the nonpreemptive policy.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 5.3333 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -2.6666 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1.0000 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q56

**Correct answer:** A, C

Appending b's can complete exactly strings a^i b^j with i≥j≥0, so K is that language. aaab has3≥1, proving A; abb has1<2 and cannot be repaired by more b's, refuting B. A grammar S→aSb | A, A→aA | ε generates K, proving C. For any i<j, the suffix b^j distinguishes prefixes a^i and a^j: only the latter completes a word in K. Infinitely many distinguishable prefixes imply nonregularity, refuting D. Right quotient by a regular language preserves context-freeness, but does not force regularity.

## Q57

**Correct answer:** C

The required numerical answer is **35**, so select **C**.

SSTF chooses55, whose seek5 plus rotational wait50 gives55. The other service times are20+0=20 for30 and30+0=30 for80. Minimum20, so excess55−20=35. Minimum seek distance does not necessarily minimize seek-plus-rotation time.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 35 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -17 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q58

**Correct answer:** 0

**Concept:** Interval enumeration in a subset lattice.

The meet is {b} and the join {a,b,c}. The interval contains exactly {b},{a,b},{b,c},{a,b,c}. The first and last are comparable with both X,Y; X is comparable with itself, as is Y. None is incomparable with both, so the count is zero.

**Common misconception:** Considering {a,c}, which is incomparable with both but does not contain the required meet {b}.

## Q59

**Correct answer:** A

The required numerical answer is **4**, so select **A**.

A determines B and C. No dependency derives A from a set lacking it, so precisely the subsets containing A are superkeys: A,AB,AC,ABC. There are four. Only A is minimal and hence a candidate key.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q60

**Correct answer:** 5000

The full response sends5200 bytes; the revalidation response sends200. Saving=5000 bytes. The cached body is reused locally and is not retransmitted as part of the specified304 response.

## Q61

**Correct answer:** C

The required numerical answer is **8**, so select **C**.

Three instructions through five stages need3+5−1=7 cycles without stalls. The immediate load consumer requires one bubble because the value is available only after MEM. The second add's dependency is satisfied by EX forwarding with no extra bubble. Total8 cycles. Full forwarding does not remove this load-use timing gap.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 8 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q62

**Correct answer:** 5

Compare each input with the preceding input, taking the initial preceding value as q=0. Inputs110101 yield outputs1,0,1,1,1,1, so five outputs are1. Each output uses the old state; updating q before producing y would incorrectly make every output zero.

## Q63

**Correct answer:** A, C

**Concept:** Cycle property of minimum spanning trees.

The unique heaviest edge on a cycle cannot be in an MST: removing it from a proposed tree gives a cut crossed by a lighter edge of the cycle, reducing weight. This proves A. The remainder of the cycle also provides an alternate route after removing that edge, proving C. For a graph consisting only of this cycle, both weight-2 edges occur in the MST, refuting B. Additional graph structure can contain equal-cost alternatives, so uniqueness does not follow; D is false.

**Common misconception:** Excluding every edge whose weight is not the minimum on a cycle.

## Q64

**Correct answer:** -1.5

**Concept:** Signed ties-to-even fixed-point rounding.

Scaling by four gives exact encoded value −5.5, midway between −6 and −5. The even integer is −6, so the stored real value is −6/4=−1.5.

**Common misconception:** Assuming ties-to-even always rounds toward zero for negative inputs.

## Q65

**Correct answer:** B

The required numerical answer is **64**, so select **B**.

Concept: representation storage thresholds. Matrix storage=4096 bits. Lists require 65·32+2m·16=2080+32m. Strict inequality 4096<2080+32m means m>63. Therefore the smallest integer is 64, feasible for a 64-vertex simple graph. At m=63 the sizes tie, which does not satisfy the question.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 64 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -32 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


