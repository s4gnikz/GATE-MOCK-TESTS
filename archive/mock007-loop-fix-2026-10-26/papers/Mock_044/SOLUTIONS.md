# Worked Solutions — Mock Test 044

## Q1

**Correct answer:** A, B, D

The required numerical answer is **32**, so exclude **C** and select the other three options.

**Concept:** Second-order recurrence evaluation.

The successive terms are 1,2,4,8,16,32. Each calculation uses the preceding two terms; induction also verifies a_n=2^(n−1).

**Common misconception:** Ignoring the coefficient two on the second preceding term.

**Option check**
- **A: Select.** Its value differs from the required answer by 32 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -16 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q2

**Correct answer:** D

The required numerical answer is **1**, so select **D**.

**Concept:** Symmetries preserving labels or colours.

Any valid rotation must fix the unique red point (1,0). Among angles in [0,360), only the zero-degree rotation does this. The uncoloured set would have four rotational symmetries, but three do not preserve colour.

**Common misconception:** Geometric symmetry can be destroyed by a distinguishing mark.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q3

**Correct answer:** D

**Correct audit:** D.
 valid original candidates are B, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

B permits a different reviewer for each report, expressing for every report there exists a reviewer. A requires one reviewer for all; C requires every reviewer for all; D denies reading. The order of quantifiers changes the claim.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Incorrect; it misclassifies candidate(s) III.
- C: Incorrect; it misclassifies candidate(s) I, II, III, IV.
- D: Correct; all four candidate classifications agree with the derivation.


## Q4

**Correct answer:** A, B, D

The required numerical answer is **20**, so exclude **C** and select the other three options.

The multiplier is (1+p/100)(1−p/100)=1−p²/10000=0.96. Hence p²=400 and the stipulated positive p is 20. Equal percentage changes in opposite directions do not cancel because the second uses the changed base.

**Option check**
- **A: Select.** Its value differs from the required answer by 20 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -10 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q5

**Correct answer:** B

The required numerical answer is **2**, so select **B**.

1. The biconditional requires exactly one of C and D to be selected.
2. The other selected person must be A or B. Selecting A would also require B, producing three people, which is forbidden.
3. Hence the possible pairs are {B,C} and {B,D}: two pairs.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q6

**Correct answer:** C

**Correct audit:** C.
 valid original candidates are B, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

**Concept:** General Aptitude — Two- and three-dimensional patterns

1. Each stack at row i, column j is at most min(row maximum i, column maximum j). The componentwise largest arrangement is rows [2,3,1] and [2,2,1], with 11 cubes; it meets every projection.
2. Each column must attain its maximum, so at least 2+3+1=6 cubes are needed.
3. Rows [0,3,1] and [2,0,0] attain all required row and column maxima with exactly 6 cubes. Thus both bounds are achievable.

- **A:** The displayed 6-cube construction disproves a minimum of 7.
- **B:** It gives the two attainable bounds.
- **C:** The per-stack upper bounds sum to only 11.
- **D:** Both numbers exceed attainable tight bounds.

**Common misconception:** Projection heights are maxima, not sums; each visible peak can serve both a row and a column constraint.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Incorrect; it misclassifies candidate(s) III.
- C: Correct; all four candidate classifications agree with the derivation.
- D: Incorrect; it misclassifies candidate(s) I, II, III, IV.


## Q7

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The passage explicitly combines an unchanged mean with individual changes, which is C. A,D contradict the stated increases and decreases. B incorrectly equates one summary statistic with the entire distribution. Offsetting changes can preserve a mean while altering many other properties.

## Q8

**Correct answer:** D

The required numerical answer is **24**, so select **D**.

The mathematics books have one allowed relative order and create four gaps around/between them. Place the three literature books in three distinct gaps to prevent adjacency: choose(4,3)=4 choices of gaps, with3!=6 assignments of distinct literature books. Total24. The fixed order of mathematics books removes a factor3! that would otherwise occur.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 24 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -12 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q9

**Correct answer:** C

The required numerical answer is **25**, so select **C**.

**Concept:** Membership counting and attainability.

There are 80+75+70=225 subject memberships. If t students take all three, the other students contribute at most two memberships each, so 225≤3t+2(100−t), giving t≥25. Equality is attained with 25 in all three, 30 in A and B only, 25 in A and C only, and 20 in B and C only. These groups total 100 and reproduce all three subject totals.

**Common misconception:** Reporting a counting bound without showing it can be achieved.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 25 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -12 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q10

**Correct answer:** A

The required numerical answer is **5**, so select **A**.

Undo the second fold: the cut x=5 reflects to x=7 in the first packet. Undo the first fold: x=5 and7 reflect across x=4 to x=3 and1. The full-height cuts are therefore at1,3,5,7, dividing the rectangle into five strips. The fold lines themselves are not cuts.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 5 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q11

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Truth-table synthesis.

The possible values are 0,1,2,3. Exactly 2 and 3 are prime, and both have a=1, so A realizes the required function. B includes 1 and excludes 2; C includes 1 and excludes 3; D excludes prime 2.

**Common misconception:** Treating 1 as prime.

## Q12

**Correct answer:** 12

Each of12 employees participates exactly once, so there are12 pairs. A department may participate in many of these pairs or none. Multiplying employee and department counts would ignore the exactly-one ownership condition.

## Q13

**Correct answer:** A, B, D

The required numerical answer is **1**, so exclude **C** and select the other three options.

Concept: weighted interval scheduling. Earliest finish first chooses [0,2), then [2,4), total weight eight. Choosing only [0,4) yields nine, which is optimal among the listed choices. Shortfall=1. The unweighted greedy rule does not generally maximize weights.

**Option check**
- **A: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.


## Q14

**Correct answer:** A

The required numerical answer is **7**, so select **A**.

The pumped block consists only of a's and its length k is1,2,or3. Pumping with exponent i changes the a-count to3+(i−1)k. Equating this to9 gives i=1+6/k, respectively7,4,3. The largest required exponent is7. The exponent may depend on the decomposition; one need not use the same exponent for every legal block. This finite instance illustrates the pumping contradiction mechanism rather than constituting a full proof for every pumping length.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 7 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Thread-private execution state and shared memory.

Separate stacks do not isolate shared heap storage, so unsynchronized accesses can race: B. A incorrectly infers isolation; C conflates sharing memory with sharing register state; D describes a private-copy mechanism that ordinary threads do not provide.

**Common misconception:** Treating all data accessed by a thread as private because its stack is private.

## Q16

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Cut property of minimum spanning trees.

If a spanning tree omitted a uniquely lightest cut edge e, adding e creates a cycle containing another cut-crossing edge of strictly greater weight. Exchanging them lowers total weight, contradicting minimality. Thus C holds. Tied weights do not necessarily create alternative MSTs (A); a maximum-weight bridge must be included (B); Kruskal can break ties arbitrarily and remains correct (D).

**Common misconception:** Global distinctness of all weights is stronger than the local uniqueness needed by this cut argument.

## Q17

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Enumeration without an end-of-output signal.

A correct enumerator must eventually print every member and no nonmember; it need not announce exhaustion. It can keep testing strings forever after its last output, so B holds. A adds an unjustified termination test; C confuses enumeration duration with membership decidability; D is refuted by an enumerator that never prints.

**Common misconception:** Requiring finite languages to have enumerators that halt after their last member.

## Q18

**Correct answer:** A

The required numerical answer is **4**, so select **A**.

**Concept:** Projection duplicate elimination and Cartesian product.

π_A(R)={1,2} and π_B(R)={2,3}, each of size two. Their product contains four ordered pairs. Projected duplicates are eliminated under set semantics.

**Common misconception:** Retaining all three original occurrences in each projected relation.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q19

**Correct answer:** A, B, D

The required numerical answer is **0.21**, so exclude **C** and select the other three options.

**Concept:** Bernoulli variance and affine transformation.

X+2Y=2−X. If p=P(X=1), its expectation is 2−p=1.7, so p=0.3. Translation and a sign change preserve variance: Var(2−X)=p(1−p)=0.3×0.7=0.21.

**Common misconception:** X and Y are dependent; adding their variances as if independent is invalid.

**Option check**
- **A: Select.** Its value differs from the required answer by 0.58 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -0.10 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 0.40 and is outside the source answer's accepted range.


## Q20

**Correct answer:** A, B, C

The required numerical answer is **4**, so exclude **D** and select the other three options.

Label nodes by first-visit indices0,1,2,3,4,5,6, with6 linking back to3. After iterations1,2,3,4 the slow pointer is at1,2,3,4 while the fast pointer is at2,4,6,4. The first equality after advancement is iteration4. Starting equality at the head is explicitly excluded, and cycle length alone does not in general determine the first meeting without considering the prefix.

**Option check**
- **A: Select.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Do not select.** It matches the derived answer at the required precision.


## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Integer promotion and unsigned conversion.

The addition is performed after integer promotion and is representable; assignment converts the result back modulo 256. Starting at an even value and adding two modulo 256 always leaves i even. It never becomes 255, and every even eight-bit value is less than 255. The loop is infinite (B). A,C wrongly claim termination; D mistakes conversion wraparound for signed overflow.

**Common misconception:** Promotion does not prevent wraparound when a representable sum is assigned back to a narrower unsigned type.

## Q22

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The query selects every domain value absent from a finite relation; over the infinite domain this is infinite and includes values outside the active domain. B is correct and A false. Negation can be safe when variables are appropriately range-restricted, so C is false. Complementation does not reproduce R, making D false. Finiteness of stored input does not ensure safety of an unrestricted query.

## Q23

**Correct answer:** B, C, D

The required numerical answer is **3**, so exclude **A** and select the other three options.

The successive depths are 1 after a,2 after b,1 after +,2 after c,3 after d,2 after −,and1 after *. The maximum is 3. An operator reduces the depth by one because it consumes two values and produces one, not because it simply pops both without replacement.

**Option check**
- **A: Do not select.** It matches the derived answer at the required precision.
- **B: Select.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q24

**Correct answer:** A

The required numerical answer is **9**, so select **A**.

Concept: symmetric transitive relations. If an element x is related to any y, symmetry gives yRx and transitivity gives xRx. Therefore any element missing its self-pair has no incident pairs at all. Nonreflexivity forces at least one such isolated element; at most three active elements remain, allowing at most 3²=9 pairs. The complete relation on three elements, with the fourth isolated, attains nine. Nonreflexive does not mean every self-pair is absent.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 9 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q25

**Correct answer:** C

**Correct audit:** C.
 valid original candidates are A, B, D, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

**Concept:** Algebraic identities under explicit exact semantics.

Zero is the additive identity, one the multiplicative identity, and subtracting a value from itself yields zero. These establish A,B,D. C fails for any nonzero x because x×0 equals zero, not x.

**Common misconception:** Confusing a multiplicative annihilator with an identity.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Incorrect; it misclassifies candidate(s) III.
- C: Correct; all four candidate classifications agree with the derivation.
- D: Incorrect; it misclassifies candidate(s) I, II, III, IV.


## Q26

**Correct answer:** C

**Correct audit:** C.
 valid original candidates are A, B, D, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

**Concept:** Traversal reconstruction.

Preorder gives root A. A is first in inorder, so it has no left subtree. Repeating the argument gives a right-only chain A→B→C→D (A,B). Postorder visits that chain backward, D,C,B,A (D). C describes the opposite chain and contradicts inorder.

**Common misconception:** Equal preorder and inorder sequences do not indicate a balanced tree.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Incorrect; it misclassifies candidate(s) III.
- C: Correct; all four candidate classifications agree with the derivation.
- D: Incorrect; it misclassifies candidate(s) I, II, III, IV.


## Q27

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Characteristic polynomial and diagonalization.

The characteristic polynomial is (λ−2)(λ+1)=λ²−λ−2. Cayley–Hamilton gives A²−A−2I=0, proving A. Distinct real eigenvalues give two independent real eigenvectors, proving C. The determinant is −2, so B is false. For example, the upper triangular matrix with rows (2,1),(0,−1) has these eigenvalues but is not symmetric, refuting D.

**Common misconception:** Confusing real diagonalizability with orthogonal diagonalizability of symmetric matrices.

## Q28

**Correct answer:** B

**Correct audit:** B.
 valid original candidates are A, B, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

**Concept:** Explicit communication interfaces.

Message passing uses message send/receive operations and can cross separate process address spaces, giving A,B. Application protocols can still race or deadlock, refuting C. Blocking implementations need not busy-wait, refuting D.

**Common misconception:** Treating the communication mechanism as a blanket correctness guarantee.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Correct; all four candidate classifications agree with the derivation.
- C: Incorrect; it misclassifies candidate(s) III.
- D: Incorrect; it misclassifies candidate(s) I, II, III, IV.


## Q29

**Correct answer:** A

The required numerical answer is **19**, so select **A**.

A full binary tree with L leaves has 2L−1 vertices, initially 21. The operation removes precisely the chosen leaf and its parent, retaining every vertex of the sibling subtree. Hence 19 remain. A sibling that is internal does not cause its descendants to be deleted.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 19 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -9 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q30

**Correct answer:** A, C

A usable cached or otherwise known address can avoid a fresh lookup, A. The redirected hostname may need its own DNS resolution, C. Distinct hostnames need not resolve to the same address, so B is false. A response cannot change a request already transmitted; following a redirect involves another request, so D is false.

## Q31

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Rolle's theorem and compact-interval extrema.

Rolle's theorem gives A, while continuity on the closed bounded interval gives C. Nonconstant examples such as 1+x(2−x) refute B. To refute D, use 1+x(x−2)(x+1): its endpoint values are one but its derivative at one is nonzero.

**Common misconception:** Assuming Rolle's point must be the midpoint.

## Q32

**Correct answer:** B

The required numerical answer is **2**, so select **B**.

References0 and1 miss into lines0 and1. Block4 replaces0. The next1 hits,0 misses and replaces4, and the final1 hits. There are2 hits. Conflicts in line0 do not evict block1 from its distinct line.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q33

**Correct answer:** D

The required numerical answer is **0.9**, so select **D**.

Concept: Bayesian prediction. Likelihoods of HH are 1/4 for the fair coin and 1 for the double-headed coin. Equal priors yield posterior probabilities 1/5 and 4/5. Predictive probability=(1/5)(1/2)+(4/5)(1)=9/10. The third toss is not independent of the observed evidence after marginalizing over the unknown coin.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by -0.8 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -0.4 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 0.1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q34

**Correct answer:** B

The required numerical answer is **1058**, so select **B**.

Concept: encapsulation accounting. Total=1000 application+20 TCP+20 IP+14 Ethernet header+4 FCS=1058 bytes. The expressly excluded preamble and inter-frame gap are not added. Headers of successive layers accumulate.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1058 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -529 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q35

**Correct answer:** 1

The first edge sends7 to0. Thereafter the cycle is0,1,2,3,4,5. Thirteen further edges advance by13 modulo6=1, giving1. The initial invalid state contributes a transient step.

## Q36

**Correct answer:** A

**Correct audit:** A.
 valid original candidates are A, C, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

After signal(full), the consumer can pass its wait and read while the producer is paused before writing, proving A. Atomic operations do not reorder the intervening ordinary write, refuting B,D. Publishing full only after writing ensures that this signal cannot authorize an early read, proving C under the stated one-producer, one-consumer ordering. Synchronization operations must surround the data access in the correct order.


**Audit-option checks**
- A: Correct; all four candidate classifications agree with the derivation.
- B: Incorrect; it misclassifies candidate(s) I.
- C: Incorrect; it misclassifies candidate(s) III.
- D: Incorrect; it misclassifies candidate(s) I, II, III, IV.


## Q37

**Correct answer:** 1

For A, COUNT(*)=2,COUNT(v)=1,SUM(v)=2, so both conditions hold. For B, counts2 and0 satisfy the first condition, but SUM(v)=NULL and NULL>1 is UNKNOWN, which HAVING rejects. For C, the counts are equal, failing the first condition. Only group A returns, giving one row. SUM of entirely NULL inputs is NULL, not zero.

## Q38

**Correct answer:** A, B, D

The required numerical answer is **22**, so exclude **C** and select the other three options.

The predecessor of root8 is7, the largest key in its left subtree. Copying7 to the root and deleting its old leaf leaves the search path for5 as7→4→6→5. The sum is7+4+6+5=22. The predecessor comes from the left subtree, not the smallest right-subtree key10.

**Option check**
- **A: Select.** Its value differs from the required answer by 22 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -11 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q39

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: finite-state value invariants. Starting at zero, x alternates between zero and one. B holds, while A fails for an odd number of iterations. Both values make x(x−1)=0, proving C and disproving D. The expression can be constant even when a constituent variable is not.

## Q40

**Correct answer:** A

The required numerical answer is **8**, so select **A**.

**Concept:** Remembering a fixed suffix and distinguishability.

Store the last three bits, padding the initial history with zeros, giving eight states; accept when its oldest bit is 1. This rejects lengths below three. Every three-bit history is reachable. Two different histories differ at some position; append zero, one or two zeros so that the differing position becomes third from the right. Exactly one resulting word is accepted. All eight states are distinct residuals.

**Common misconception:** An NFA can guess the relevant 1, but a DFA must retain all relevant suffix possibilities simultaneously.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 8 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q41

**Correct answer:** B

The required numerical answer is **0.5**, so select **B**.

First round11/16=0.6875 to the nearest quarter:0.75. Rounding0.75 to halves is a tie between0.5 (raw coefficient1, odd) and1 (coefficient2, even), so it becomes1. Direct rounding of0.6875 to halves gives0.5. Difference1−0.5=0.5. Intermediate rounding can move a value onto a tie.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by -0.2 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by 0.3 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by -0.4 and is outside the source answer's accepted range.


## Q42

**Correct answer:** D

**Correct audit:** D.
 valid original candidates are A, B, D, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

**Concept:** Ordering resource and mutex waits in a bounded buffer.

The consumer can lock M and block on F=0. The producer can obtain E but then blocks on M, so it cannot insert and signal F; A,D describe this cycle. Waiting for F before acquiring M means an empty-buffer consumer holds no mutex, allowing the producer to fill and signal; B holds for this specific deadlock. Extra capacity changes E but not the blocked consumer's need for F or the producer's need for M, refuting C.

**Common misconception:** More buffer space cannot fix an ordering cycle involving a mutex and an empty-item semaphore.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Incorrect; it misclassifies candidate(s) III.
- C: Incorrect; it misclassifies candidate(s) I, II, III, IV.
- D: Correct; all four candidate classifications agree with the derivation.


## Q43

**Correct answer:** A, B, D

The required numerical answer is **24**, so exclude **C** and select the other three options.

There are three merge levels for eight elements. Every level writes all eight elements once across its buffers, so total writes are3·8=24. Equivalently W(n)=2W(n/2)+n with W(1)=0. This is cumulative work, not simultaneous buffer space.

**Option check**
- **A: Select.** Its value differs from the required answer by 24 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -12 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q44

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** State-cycle analysis and input counting.

Input 1 cycles 01→10→11→01, while input 0 resets to 01. Acceptance therefore requires the trailing run of ones to have length divisible by three. At length five, a string containing a zero is accepted with trailing run length 0 or 3: respectively 16 strings ending in 0 and two ending in 0111 (one free prefix bit). The all-one string has five trailing ones and is rejected. Total 18, option C. A omits the trailing-three case; B includes only one of its two prefixes; D exceeds the exhaustive count.

**Common misconception:** Counting all ones rather than only those after the last reset.

## Q45

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Liveness at a loop fixed point.

At L, p is read by the test, so C is live. The exit branch reads x, and B's assignment also reads old x, so A is live. The path into B reads old y before assigning y=0, making B live. These paths establish all three at the least fixed point; no use of z can propagate liveness, so D is false.

**Common misconception:** Treating a later assignment to y as killing its earlier use within the same iteration.

## Q46

**Correct answer:** D

The required numerical answer is **4**, so select **D**.

**Concept:** BFS queue constraints on discovery order.

If s enqueues a before b, a discovers c,d in either order before b discovers e. Orders are s,a,b,c,d,e and s,a,b,d,c,e. If b comes first, b discovers d,e in either order before a discovers c, giving s,b,a,d,e,c and s,b,a,e,d,c. Marking on enqueue prevents rediscovering d. Thus four distinct orders exist.

**Common misconception:** Permuting each distance layer freely despite restrictions imposed by the parent queue order.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first update temporarily gives both rows code B, violating immediate uniqueness. The completed swap has distinct codes B and A, so commit-only validation can accept it. B is correct. A overlooks the intermediate violation; C contradicts the specified check timing; D confuses the code column with the unchanged primary keys. Constraint timing can affect executability without changing final-state validity.

## Q48

**Correct answer:** C, D

The underlying question is correctly answered by A, B. This variant asks for its invalid answers, so select the complementary set: C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: grammar invariants and ambiguity. Each nonempty production adds one a and one b, proving A. For abab, the root production aSbS can pair its initial a with the second symbol b (empty first S, second S→ab), or with the final b (first S→ba, second S→ε). These are different parse trees, proving B. The word ba is generated, disproving C. In fact the language is all equal-count words: split any nonempty such word at the first return of its count balance to zero and induct on the two balanced parts. Intersecting with regular a*b* gives {aⁿbⁿ}, which is nonregular; therefore D is false. Equal total counts do not impose a prefix-balance condition.

## Q49

**Correct answer:** A, B, C

The required numerical answer is **4**, so exclude **D** and select the other three options.

A determines B and C. No dependency derives A from a set lacking it, so precisely the subsets containing A are superkeys: A,AB,AC,ABC. There are four. Only A is minimal and hence a candidate key.

**Option check**
- **A: Select.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Do not select.** It matches the derived answer at the required precision.


## Q50

**Correct answer:** A

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Matching consumes one input symbol per stored symbol, so a successful branch's guess splits the length equally, proving A. Immediate guessing accepts ε, proving D. Acceptance is existential, refuting B. Immediate guessing leaves no symbols to match a nonempty input, refuting C.

## Q51

**Correct answer:** A, B, C

The required numerical answer is **1**, so exclude **D** and select the other three options.

Concept: subnormal spacing and rounding to zero. Minimum normal is 2⁻²=1/4; with two stored fraction bits, subnormal spacing is 2⁻⁴=1/16. The first product 1/16 is exactly representable. Multiplying by 1/2 gives 1/32, midway between zero and 1/16. Ties-to-even chooses zero. Relative error=|0−1/32|/(1/32)=1. Normal-range relative-error bounds need not hold at underflow.

**Option check**
- **A: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **D: Do not select.** It matches the derived answer at the required precision.


## Q52

**Correct answer:** A, B, D

The required numerical answer is **2**, so exclude **C** and select the other three options.

**Concept:** Boolean constraint propagation.

For the AND to be one, each adjacent pair must differ. Once a is chosen, b=¬a, c=a, d=¬a are forced. The satisfying assignments are 0101 and 1010, giving two.

**Common misconception:** Counting the three XOR constraints as independent choices despite shared variables.

**Option check**
- **A: Select.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q53

**Correct answer:** B

The required numerical answer is **6**, so select **B**.

Since30=2×3×5 with distinct prime factors, a maximal divisor chain introduces exactly one previously absent prime at each step. The orders of these three introductions yield3!=6 chains. Skipping a multiplication would leave an intermediate divisor that could be inserted, making that chain nonmaximal.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 6 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q54

**Correct answer:** C

The required numerical answer is **254**, so select **C**.

Concept: one's-complement checksum. FE+02=100 hexadecimal. End-around carry adds the overflow one to the low byte 00, yielding 01. Its eight-bit complement is FE=254. Dropping carry would wrongly produce FF; two's-complement negation is also a different operation.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 254 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -127 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q55

**Correct answer:** A, B, C

The required numerical answer is **300**, so exclude **D** and select the other three options.

Base computation costs1000×2=2000 cycles. DMA adds100 stall cycles, total2100. Programmed I/O adds400 cycles, total2400. DMA saves300 cycles. The baseline CPI must be combined with the respective transfer overhead, not multiplied by it.

**Option check**
- **A: Select.** Its value differs from the required answer by 300 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -150 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Do not select.** It matches the derived answer at the required precision.


## Q56

**Correct answer:** B

**Correct audit:** B.
 valid original candidates are A, B, D, corresponding to the roman-numbered candidates above. In the original derivation below, A, B, C and D refer to candidates I, II, III and IV, respectively; they are not the audit options.

**Derivation of candidate validity**

A does not modify either operand. B,D store the operand's existing value, so the sum is unchanged despite aliasing. C is insufficient: with a=0,b=5,p=&b, the old sum is 5 and the new sum is 0. Aliasing alone neither establishes nor rules out redundancy; the stored value also matters.


**Audit-option checks**
- A: Incorrect; it misclassifies candidate(s) I.
- B: Correct; all four candidate classifications agree with the derivation.
- C: Incorrect; it misclassifies candidate(s) III.
- D: Incorrect; it misclassifies candidate(s) I, II, III, IV.


## Q57

**Correct answer:** A, B, D

The required numerical answer is **6**, so exclude **C** and select the other three options.

Issue M1 at0 and M2 at1; their results arrive at3 and4. A can issue at4 and finish at5. B issues at5 and finishes at6. Independent multiply overlap does not remove the need to wait for the later operand.

**Option check**
- **A: Select.** Its value differs from the required answer by 6 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q58

**Correct answer:** A, B, D

The required numerical answer is **-2**, so exclude **C** and select the other three options.

**Concept:** LU elimination and back substitution.

Eliminate using multipliers 2 and 4 in column one, then multiplier 3 in column two. U has rows (2,1,1),(0,1,1),(0,0,2). The transformed right side is (4,2,8). Back substitution gives x3=4, x2=2−4=−2, and x1=(4−x2−x3)/2=1. Direct substitution gives (4,10,30), checking the result.

**Common misconception:** Row operations must be applied to the right-hand side as well as the coefficient matrix.

**Option check**
- **A: Select.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.


## Q59

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Cycle property of minimum spanning trees.

The unique heaviest edge on a cycle cannot be in an MST: removing it from a proposed tree gives a cut crossed by a lighter edge of the cycle, reducing weight. This proves A. The remainder of the cycle also provides an alternate route after removing that edge, proving C. For a graph consisting only of this cycle, both weight-2 edges occur in the MST, refuting B. Additional graph structure can contain equal-cost alternatives, so uniqueness does not follow; D is false.

**Common misconception:** Excluding every edge whose weight is not the minimum on a cycle.

## Q60

**Correct answer:** B, C, D

The required numerical answer is **1536**, so exclude **A** and select the other three options.

**Concept:** Computer Organization and Architecture — Instruction sets and addressing modes

There are 256 eight-bit prefixes. The 200 two-register opcodes consume 200 complete prefix subtrees, leaving 56. Each unused eight-bit prefix supplies 16 possible twelve-bit opcodes, so there are initially 56*16=896 available twelve-bit prefixes. Allocating 800 one-register opcodes leaves 96 such prefixes. Each can supply 16 sixteen-bit zero-register opcodes, giving 96*16=1536. Equivalently, subtract complete instruction encodings: 65536-200*256-800*16=1536.

**Common misconception:** Instructions with different operand counts cannot reuse an opcode prefix that already decodes as a shorter opcode.

**Option check**
- **A: Do not select.** It matches the derived answer at the required precision.
- **B: Select.** Its value differs from the required answer by 1536 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by -768 and is outside the source answer's accepted range.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q61

**Correct answer:** B, C, D

The required numerical answer is **2**, so exclude **A** and select the other three options.

Entry(1,1) of A³ counts directed walks of length3 from1 back to1. They are1→2→4→1 and1→3→4→1, giving2. Matrix powers count walks of an exact length, not arbitrary reachability or only simple paths in general.

**Option check**
- **A: Do not select.** It matches the derived answer at the required precision.
- **B: Select.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q62

**Correct answer:** 0.6817 (range 0.68165–0.68175)

Concept: integrating an upper envelope. The crossing r in [0,1] solves r²=1−r, so r=(sqrt(5)−1)/2. The maximum is 1−x on [0,r] and x² on [r,1]. Integral=r−r²/2+(1−r³)/3. Using r²=1−r and r³=2r−1 reduces it to (5sqrt(5)−3)/12=0.6816949906…. Round to 0.6817; range 0.68165–0.68175. Integrating one branch over the entire interval would miss where the larger function changes.

## Q63

**Correct answer:** A, C, D

The required numerical answer is **1**, so exclude **B** and select the other three options.

For x<4, the unique MST uses AD,BC,AB, with total x+3. These three edges form a tree and each alternative connection costs more; ties x=1 or2 do not create a same-weight cycle exchange. At x=4, either AB or CD can connect the components formed by AD and BC, giving two MSTs of weight7. For x>4, AD,BC,CD form the unique MST; AC=5 and AB≥5 cannot replace a cheaper cut edge at no cost. Exactly one integer choice, x=4, produces multiplicity. Equal weights matter only when they offer interchangeable connections.

**Option check**
- **A: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Do not select.** It matches the derived answer at the required precision.
- **C: Select.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Select.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.


## Q64

**Correct answer:** A, B, D

The required numerical answer is **1.25**, so exclude **C** and select the other three options.

**Concept:** Updating sufficient statistics.

After removal the sum is 14 and sum of squares 54. Mean is 14/4=3.5; population variance is 54/4−3.5²=13.5−12.25=1.25.

**Common misconception:** Removing six from the sum of squares instead of removing 6².

**Option check**
- **A: Select.** Its value differs from the required answer by 1.25 and is outside the source answer's accepted range.
- **B: Select.** Its value differs from the required answer by -0.62 and is outside the source answer's accepted range.
- **C: Do not select.** It matches the derived answer at the required precision.
- **D: Select.** Its value differs from the required answer by 1.00 and is outside the source answer's accepted range.


## Q65

**Correct answer:** A, C, D

The required numerical answer is **325**, so exclude **B** and select the other three options.

One-way propagation is 2400/(2×10^8)=12 microseconds. A far-end station can begin just before the first bit arrives, so the collision disturbance takes almost another 12 microseconds to return. The stated inclusive bound is 24 microseconds, and detector delay adds 2, giving 26 microseconds. At 100×10^6 bits/s the sender must transmit at least 2600 bits. Dividing by eight gives 325 bytes exactly. These are parameters of the idealized link, not a claim about a standard Ethernet minimum frame size.

**Option check**
- **A: Select.** Its value differs from the required answer by 325 and is outside the source answer's accepted range.
- **B: Do not select.** It matches the derived answer at the required precision.
- **C: Select.** Its value differs from the required answer by -162 and is outside the source answer's accepted range.
- **D: Select.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


