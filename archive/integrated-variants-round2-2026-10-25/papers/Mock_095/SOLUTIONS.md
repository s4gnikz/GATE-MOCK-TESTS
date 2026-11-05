# Worked Solutions — Mock Test 095

## Q1

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: induction versus proof. The observation establishes correctness only on the tested executions, which is B. A extrapolates to all programs, C invents universal failure outside the suite, and D denies the possibility of a revealing new test. Finite testing alone is not a universal correctness proof.

## Q2

**Correct answer:** 22

The original surface area is24. Each removed corner cube had three exterior faces, so six exterior units disappear. Each also had three neighbours, one being the other removed cube, leaving two retained neighbours per removed cube whose shared faces become exposed. Add four, giving24−6+4=22. The face between the two removed cubes does not become a remaining-solid surface.

## Q3

**Correct answer:** 2

The recurrence gives a(n)=n². The inequality is2n+1>n², which for positive integers holds only at n=1,2. At n=3 it fails, and n²−2n−1 increases thereafter. The ten-term range therefore contains two solutions.

## Q4

**Correct answer:** 1
**Concept:** Symmetries preserving labels or colours.

Any valid rotation must fix the unique red point (1,0). Among angles in [0,360), only the zero-degree rotation does this. The uncoloured set would have four rotational symmetries, but three do not preserve colour.

**Common misconception:** Geometric symmetry can be destroyed by a distinguishing mark.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

“Had the survey included” is inversion of a past counterfactual condition. Its unreal past consequence is “would have been,” B. A uses an incompatible future perfect; C describes an awkward progressive state rather than the completed past consequence; D does not supply the required conditional consequence.

## Q6

**Correct answer:** 42

Initially there are3 litres of salt-solution component. Removing one fifth leaves2.4 litres, with volume restored to10. Removing half of that mixture leaves1.2 litres of the component. The replacement contributes5×0.6=3 litres, giving4.2 litres in10, or42%. Each removal uses the concentration at that stage, not the original30% throughout.

## Q7

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If A is absent, the three statements are true,false,true. If B is absent, they are false,false,false. If C is absent, they are true,true,false. The counts of true statements are2,0,2, never1. Thus none of A,B,C can be the absent person under all conditions and D is correct. The task requires checking consistency, not assuming the conditions have a solution.

## Q8

**Correct answer:** 5

Track orientations in the order(top,bottom,north,south,east,west). Initially they are(1,6,2,5,3,4). After north:(5,2,1,6,3,4); east:(4,3,1,6,5,2); south:(1,6,3,4,5,2); west:(5,2,3,4,6,1). The final top is5. A closed path of rolls need not restore orientation.

## Q9

**Correct answer:** C

The passage explicitly combines an unchanged mean with individual changes, which is C. A,D contradict the stated increases and decreases. B incorrectly equates one summary statistic with the entire distribution. Offsetting changes can preserve a mean while altering many other properties.

## Q10

**Correct answer:** 32

There are5!=120 circular arrangements. For each specified pair forced adjacent, contract it to a block with2 internal orders:2·4!=48. For two designated adjacent pairs there are2²·3!=24 arrangements; for all three,2³·2!=16. Inclusion–exclusion gives120−3·48+3·24−16=32. Reflections remain distinct, so no additional division by2 is allowed.

## Q11

**Correct answer:** 64

**Concept:** Bit patterns versus maximum value.

Six unsigned bits encode 2⁶=64 values, from zero to 63 inclusive. The question asks the count, not the greatest value.

**Common misconception:** Answering 63 by confusing maximum value with number of values.

## Q12

**Correct answer:** A, C

If p is null, the first comparison is false and short-circuit evaluation bypasses the dereference, proving A,C. Eager evaluation in B could introduce an invalid null dereference. D reverses the required order. Correct intermediate code must preserve which expressions are evaluated, not just a truth-table identity on safe operands.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Prefix block boundaries.

A /26 leaves six host bits, so this block covers final octets 128–191. Only 160 lies inside. A is below, C begins the next block, and D changes the preceding octet.

**Common misconception:** Including the first address of the next subnet in the current block.

## Q14

**Correct answer:** 1

Reachable nonterminals are S,A,B. A is productive through a. B has no terminating production: every derivation retains B, so neither B nor S is productive. C is productive but unreachable. Only A satisfies both conditions, giving1. Reachability and productivity are independent checks.

## Q15

**Correct answer:** 36 (exact)
**Concept:** Surjections after identifying domain elements.

Treat {1,2} as one effective element, giving four labelled units mapping onto three labels. Inclusion-exclusion yields 3⁴−3×2⁴+3×1⁴=81−48+3=36.

**Common misconception:** The equality constraint reduces the number of independently assigned domain units; it does not reduce the codomain.

## Q16

**Correct answer:** A, B, D

**Concept:** Unbounded stack height with a small alphabet.

Repeated X symbols can encode an unbounded unary count (A), which later pops can match (B). Stack height has no fixed bound, proving D. With exactly one X per prefix symbol and no alternative encoding, only the length is stored in the stack; finite control cannot distinguish every arbitrary binary prefix, so C is false.

**Common misconception:** Confusing finite stack alphabet with bounded stack capacity.

## Q17

**Correct answer:** 512

**Concept:** Instruction-field bit allocation.

Each register field needs log₂32=5 bits. Three such fields and the immediate use 15+8=23 bits. The remaining nine opcode bits encode 2⁹=512 patterns.

**Common misconception:** Subtracting the number of registers instead of the field width.

## Q18

**Correct answer:** 4

**Concept:** Projection duplicate elimination and Cartesian product.

π_A(R)={1,2} and π_B(R)={2,3}, each of size two. Their product contains four ordered pairs. Projected duplicates are eliminated under set semantics.

**Common misconception:** Retaining all three original occurrences in each projected relation.

## Q19

**Correct answer:** 3
**Concept:** Cycle detection trace.

After iterations 1,2,3, the (slow,fast) node pairs are (1,2),(2,4),(3,3). The first equality is therefore at node 3. The initial equality at node 0 is explicitly not tested before movement.

**Common misconception:** The test location in the loop affects whether an initial equality is mistakenly counted.

## Q20

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A downward scan reads dp[c−w] before that lower entry is updated for the current item, preventing its reuse; A is true. Upward scanning can read already updated values, so B is true and C false. For the example, dp[2]=3 before dp[4] is updated from dp[2]+3=6, proving D. Space compression must preserve the original DP dependency layer.

## Q21

**Correct answer:** B, C

A pushdown automaton can maintain unmatched symbols: push when the incoming symbol agrees with the stack top and pop when it differs, accepting when no unmatched symbols remain. Thus B is true. Restricting to 0*1* gives exactly0^n1^n, so C is true. If L were regular, its intersection with the regular language0*1* would be regular, contradicting the standard pumping argument for0^n1^n; A is false. The string10 is a counterexample to D. Equal counts do not impose symbol order.

## Q22

**Correct answer:** 11

Rearranging gives a(n)−a(n−1)=a(n−1)−a(n−2), so every first difference is 2. Therefore a(n)=1+2n and a5=11. By the definition of the ordinary generating function, the requested coefficient is precisely a5. The recurrence's repeated root leads to linear, not exponential, growth.

## Q23

**Correct answer:** 0.3466 (range 0.34655–0.34665)
**Concept:** Integration by substitution.

Set u=1+x², so du=2x dx. The integral becomes (1/2)∫₁² du/u=(ln 2)/2≈0.3465735903, which rounds to 0.3466.

**Common misconception:** The substitution introduces a factor of one-half and changes both limits.

## Q24

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For every nonzero signed integer x, x/x=1, proving A. A dominating nonzero fact remains useful if x is unchanged, proving C. If x can be zero, replacement suppresses the invalid division, so B and D are false under the requirement to preserve the stated behavior. Algebraic identities have preconditions.

## Q25

**Correct answer:** A, B

The IPv4 header checksum covers the source address, so A is true. TCP includes its ports and a pseudo-header containing IP addresses, making B true. C and D incorrectly omit checksum-covered fields. Rewriting at one protocol layer can affect integrity checks at another.

## Q26

**Correct answer:** A

**Concept:** Universal quantification with a domain restriction.

A requires Works(e,d) for each d that is a department, while not constraining other domain objects. B requires merely one department. C demands that every domain object be a department and assigned, which is too strong. D expresses no assignments. If Department is empty, A correctly holds vacuously for every employee.

**Common misconception:** Using conjunction instead of implication to restrict a universal quantifier.

## Q27

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Pipe endpoint lifetime.

End-of-file requires the pipe buffer to be empty and every write-end reference to be closed. Child II still owns one, so the read blocks. A ignores that inherited reference. C is not stream-read behavior. D concerns writing to a pipe with no reader, not this read operation.

**Common misconception:** The process that supplied the data is not necessarily the only process keeping the pipe open.

## Q28

**Correct answer:** 5

The first three pushes store(5,5),(2,2),(2,2). Popping one duplicate minimum leaves the other minimum2. Pushing and popping4 does not remove that2. The final pop removes the remaining 2, leaving(5,5), so the minimum is 5. Per-entry minimum metadata restores the previous minimum correctly even with duplicates.

## Q29

**Correct answer:** 500

**Concept:** Cumulative acknowledgment boundaries.

ACK2500 acknowledges every byte below2500, covering the first three listed segments. Only[2500,3000), of length500, remains unacknowledged among the listed bytes. The acknowledgment number names the next expected byte, not the last received byte.

**Misconception:** Counting byte2500 as acknowledged or assuming the ACK covers only one segment.

## Q30

**Correct answer:** 3

Simultaneous updates give 00→01→11→00. There are three distinct states. In particular, B' uses the old A, not A' computed at the same edge.

## Q31

**Correct answer:** C

After fewer than n−1 inspections all returning1, at least two uninspected positions remain possible locations of0, each consistent with the rotation promise. Thus n−1 inspections can be necessary, and a linear scan suffices. C is correct; A,B are too small and D exceeds the tight bound. Duplicates can remove the information needed for logarithmic rotated-array search.

## Q32

**Correct answer:** -1.5

**Concept:** Signed fixed-point scaling.

The unsigned pattern is 232; in eight-bit two's complement it means 232−256=−24. Four fractional bits scale this by 2⁻⁴, giving −24/16=−1.5.

**Common misconception:** Interpreting the raw bit pattern as unsigned before applying fractional scaling.

## Q33

**Correct answer:** 2 (exact)

**Concept:** Engineering Mathematics — Matrices determinants and linear systems

1. Subtract row 1 from rows 2 and 3. The determinant becomes (t-1)^2-1=t(t-2).
2. A real homogeneous square system has infinitely many solutions precisely when it is singular.
3. The distinct singular values are t=0 and t=2, whose sum is 2.

**Common misconception:** A homogeneous singular system is always consistent and has a nontrivial null space.

## Q34

**Correct answer:** 37

**Concept:** Logical shift and unsigned interpretation.

10010110₂ shifted right twice with zero fill becomes 00100101₂, equal to 32+4+1=37.

**Common misconception:** Sign-extending as if an arithmetic shift had been requested.

## Q35

**Correct answer:** C

For x>0 the expression is 0; for x<0 it is−2. The one-sided limits disagree, so no value assigned at 0 can give continuity(C). A,B select only one side's value, and differentiability in B would also require continuity. D ignores the unequal limits.

## Q36

**Correct answer:** A, C

Concept: edge identities in multigraph DFS. Traversing one edge u→v and returning on the other forms the allowed length-two cycle, A. At v, only the entering edge should be ignored; the other edge to the already visited parent reveals the cycle, C. B incorrectly ignores both edges; D discards a structurally distinct edge. Parent-vertex exclusion assumes a simple graph.

## Q37

**Correct answer:** 4

Concept: tree diameter endpoints. The leaves are D,E,G,H. A longest path in an unweighted tree has leaf endpoints. D–E and G–H each have distance two; any pair with one endpoint in {D,E} and the other in {G,H} has distance five, through B,A,C,F. Thus the diameter is five and exactly 2·2=4 unordered endpoint pairs attain it. Reversing endpoints does not create another pair.

## Q38

**Correct answer:** -5

**Concept:** Depth changes under rotation.

After the left rotation, x moves down one level and y up one, cancelling their contributions. Every node in A moves down one (+4 total), every node in C moves up one (−9), and B's nodes remain at the same depth. Nodes outside the rotated subtree are unchanged. Net comparison-count change is 4−9=−5.

**Common misconception:** Moving B's nodes with y even though the rotation reattaches B beneath x at their original depth.

## Q39

**Correct answer:** 0.1944 (accepted range 0.19435–0.19445)

E[W]=P(X=Y=1)=1/6. E[Z]=1/2+1/3=5/6. ZW is2 when both succeed and0 otherwise, so E[ZW]=1/3. Covariance is1/3−(5/6)(1/6)=7/36≈0.194444. Independence of X,Y does not make their derived variables Z,W independent.

## Q40

**Correct answer:** 896

Encoded widths are3 for eight choices,3 for five choices and4 for arbitrary enable subsets, total10. Horizontal width is8+5+4=17. Saving7 bits per word across128 words gives896 bits. Independent enables cannot be reduced to the logarithm of four because all16 subsets must be representable.

## Q41

**Correct answer:** 2

Bytes0,3 specify a three-byte payload65,66,67. The first read ends after66 and is incomplete. The second supplies67, then length0,2 and payload68,69, completing two messages. Reads and protocol boundaries differ; a buffer must retain partial header/payload data across reads.

## Q42

**Correct answer:** 3

The lookup at0 remains valid at4 and9 but expires at10. The refreshed answer at10 is valid at19 but expires at20. Therefore misses occur at0,10,20: three upstream lookups. Cache hits do not extend the fixed expiry time under the stated rule.

## Q43

**Correct answer:** 24
**Concept:** Strong components of a tournament.

There are 64 orientations in total. A non-strong tournament on four vertices is either transitive, giving 4!=24 orders, or consists of a directed three-cycle and a fourth vertex that beats all three or loses to all three. The latter gives 4 choices of singleton, 2 cycle orientations, and 2 directions, totaling 16. These cases are disjoint and exhaustive because a nontrivial strongly connected tournament needs at least three vertices. Therefore strongly connected tournaments number 64−24−16=24.

**Common misconception:** A tournament with a directed cycle need not be strongly connected as a whole.

## Q44

**Correct answer:** 7
**Concept:** Resource-constrained instruction scheduling.

Run P on the multiplier during 0–3 and Q during 3–6. Compute R on the adder during 3–4, overlapping Q. Then S runs during 6–7. The multiplier's two operations require six cycles total, and S must follow the completion of both products through its dependencies, so finishing before seven is impossible. Seven is attained.

**Common misconception:** Parallel functional units permit overlap, but a final dependent operation still supplies a lower bound after the bottleneck resource finishes.

## Q45

**Correct answer:** A, B, D

Forwarding normally creates a new link-layer header for the outgoing link, while IP destination remains end-to-end, proving A,D and disproving C. TTL is within the IPv4 header and affects its checksum, proving B. Different layers can legitimately change different fields at the same hop.

## Q46

**Correct answer:** 2.5

**Concept:** Nested conditional cache-miss probabilities.

All accesses cost one ns. An L1 miss adds an average 5+0.20×50=15 ns. Weighting by the L1 miss probability gives 1+0.10×15=2.5 ns. The main-memory access probability is 0.10×0.20=0.02, not 0.20.

**Common misconception:** Applying a local L2 miss rate to all CPU memory accesses.

## Q47

**Correct answer:** 7

Below4, spacing is1/4, so the predecessor is3.75; above4, spacing is1/2, so the successor is4.5. The rounding interval for4 therefore extends from midpoint3.875 to midpoint4.25. Both ties round to4 because its significand1000 has even low bit, whereas neighbouring significands1111 and1001 have odd low bits. Multiplying endpoints by16 gives k=62 through68 inclusive, seven integers. The rounding interval is asymmetric at a binade boundary.

## Q48

**Correct answer:** 70

The head travels50→70 first, a distance20. The new request60 arrives behind the upward-moving head at65 and waits for reversal. It then travels70→60→20, a distance50. Total70. LOOK reverses at70 rather than travelling to the physical endpoint99, and the late request does not cause early reversal.

## Q49

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Timestamp ordering in wait-die.

T1 is older than the holder T2, so it waits for x. T2 is older than holder T3, so it waits for y. T3 is younger than holder T1, so it aborts when requesting z. Only C matches. A,B reverse the requester/holder age test; D ignores the final younger-on-older request.

**Common misconception:** Under wait-die, the younger requester aborts; this differs from policies in which an older requester aborts a younger holder.

## Q50

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Boolean absorption and redundancy.

Expanding gives x+xy+xz+yz=x+yz, proving A. Whenever F=1, either x=1 or y=z=1, so x+y+z=1; multiplying by that redundant factor preserves F, proving C. At x=0,y=z=1, F=1 while B and D are zero, refuting both.

**Common misconception:** Distributing without applying absorption, or forgetting the yz term.

## Q51

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Bu=Au+u(v^T u)=2u-2u=0, so zero is an eigenvalue.
2. Choose a basis (u,w1,w4) in which Aw1=w1 and Aw4=4w4. Distinct eigenvalues ensure this is a basis. In this basis A is diag(2,1,4), and u v^T has nonzero entries only in its first row, whose first entry is -2.
3. Therefore B is upper triangular with diagonal (0,1,4). These distinct real eigenvalues make B diagonalizable, and exactly two are nonzero, so rank(B)=2.
4. Commutation need not hold. In this basis choose v^T=(-2,1,0). Then B has first row (0,1,0); AB has entry (1,2)=2, whereas BA has that entry 1. A and B do not commute.
- Original option A: u is a nonzero vector in the null space of B.
- Original option B: The three eigenvalues are 0,1,4, all distinct and real.
- Original option C: The explicit choice A=diag(2,1,4), u=(1,0,0)^T, v=(-2,1,0)^T is a counterexample.
- Original option D: Similarity to a diagonal matrix with exactly two nonzero entries gives rank two.

## Q52

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first p symbols are all a, and y is nonempty within them, so A is true. Removing y decreases only the a count, establishing C for every permitted decomposition. A regular-language pumping guarantee is existential over a suitable decomposition; disproving one convenient decomposition is insufficient, so B is false. The pumping length must work for every sufficiently long language word and cannot be reset to suit later choices, refuting D. Correct quantifier order is essential.

## Q53

**Correct answer:** 4

Replacing index4 by the last value4 leaves[1,10,2,4,12,3]. Its parent10 exceeds4, so sift upward: exchange indices4 and2 to obtain[1,4,2,10,12,3]. No further exchange is needed. Index2 contains4. Arbitrary-index deletion may require upward repair, unlike the familiar root deletion's usual downward repair.

## Q54

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Loop joins and fixed-point facts.

The initial edge carries zero while iterations can carry one,two,…, so C holds and no single constant generally describes all header visits, A. B ignores the back edge. Constant propagation does not generally determine arbitrary input-dependent loop counts, so D is false.

**Common misconception:** Propagating an initialization through a modifying loop as an invariant.

## Q55

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: recognizable reachability and reduction. Simulation accepts upon entering PRINT, establishing A. Simulating an arbitrary machine/input and entering PRINT iff it halts reduces halting to this property, establishing C. No universal fixed simulation bound exists, so B is false. If the complement also had a recognizer, dovetailing both would decide the property, contradicting C; D is false. A finite machine description does not bound its halting time.

## Q56

**Correct answer:** B

The first update temporarily gives both rows code B, violating immediate uniqueness. The completed swap has distinct codes B and A, so commit-only validation can accept it. B is correct. A overlooks the intermediate violation; C contradicts the specified check timing; D confuses the code column with the unchanged primary keys. Constraint timing can affect executability without changing final-state validity.

## Q57

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordering resource and mutex waits in a bounded buffer.

The consumer can lock M and block on F=0. The producer can obtain E but then blocks on M, so it cannot insert and signal F; A,D describe this cycle. Waiting for F before acquiring M means an empty-buffer consumer holds no mutex, allowing the producer to fill and signal; B holds for this specific deadlock. Extra capacity changes E but not the blocked consumer's need for F or the producer's need for M, refuting C.

**Common misconception:** More buffer space cannot fix an ordering cycle involving a mutex and an empty-item semaphore.

## Q58

**Correct answer:** 1

x is needed either for B2's update or B3's return, so it is live at B1 entry. The incoming value of p is overwritten by read() before any use; it is not live at entry, though the new p is live after that assignment until the branch. Thus exactly one of the two variables is live. Loops require a fixed-point computation, but a definite kill before every use still removes the old value.

## Q59

**Correct answer:** 1

Concept: spanning trees of a cycle. Every spanning tree deletes exactly one cycle edge. Total edge weight=22. Unconstrained minimum deletes 7, yielding 15; with 7 required, delete the largest other edge, 6, yielding 16. Additional cost=1. Strictly, the constrained object is a minimum-weight spanning tree subject to the requirement; no unconstrained MST here contains 7.

## Q60

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Starvation under strict priority.

Persistent higher-priority work can always be selected first, establishing A. An aging policy that eventually raises a waiting job sufficiently can address that risk, B. Readiness alone gives no time bound under strict priority, refuting C; preemption does not create fairness, refuting D.

**Common misconception:** Equating eligibility to run with a guarantee of timely scheduling.

## Q61

**Correct answer:** 8

**Concept:** Set mapping and independent LRU histories.

The block sequence is 0,2,0,4,2,1,3,5,1. In set 0, references 0,2,0,4,2 produce miss,miss,hit,miss,miss: accessing 0 refreshes it, so 4 evicts 2, which later must be fetched again. In set 1, references 1,3,5,1 are all misses: 5 evicts 1. Thus four misses per set give eight fetches.

**Common misconception:** Maintaining one global LRU order instead of a replacement order within each set.

## Q62

**Correct answer:** 7

Concept: product states and distinguishability. Track a-count zero or one, together with length modulo three: six states. A second a enters one permanent sink. All seven are reachable. Different residues with the same count can be separated by a suitable suffix: only b symbols for count one, or one a plus enough bs for count zero. A zero-count state and a one-count state are separated by a suffix containing exactly one a that completes a multiple-of-three length for the zero-count state; it sends the other to the sink. Every nonsink state has an accepting continuation. Thus no states merge and seven is minimal.

## Q63

**Correct answer:** 3 (exact)

**Concept:** Compiler Design — Common subexpression elimination

The initial *p and *q must each be read: in the allowed case where the pointers differ, their original values are independent and both are returned. After *p=7, the old value b cannot always replace c: if p=q, the store changes *q to 7; otherwise *q retains its old value. Without the prohibited runtime pointer test, a third load is needed for c. No subsequent store occurs, so e=c. The store itself establishes d=7, even if p and q alias. Three loads therefore suffice and are necessary under the allowed transformations.

An equivalent sequence retains the loads for a,b,c and replaces d by 7 and e by c.

**Common misconception:** Syntactically identical loads are not common subexpressions across a potentially aliasing store; a load from the exact stored address can, however, use the stored value.

## Q64

**Correct answer:** A, B, C

With b=c=0 the expression is a AND NOT a, always 0, proving A. During a transition, the direct and inverted paths can temporarily make both OR outputs 1, proving B. By the consensus theorem, (a+b)(NOT a+c) already implies (b+c), so adding that factor preserves the truth table. When b=c=0 the added factor remains 0 and blocks the glitch, proving C and refuting D. A redundant Boolean factor can be physically useful for hazard suppression.

## Q65

**Correct answer:** 32

**Concept:** Constrained univariate maximization.

Substitute y=6−x to get h(x)=6x²−x³ on [0,6]. Its derivative is 3x(4−x), so the interior maximum is at x=4,y=2 and equals 32. Both endpoints give zero.

**Common misconception:** Assuming symmetry forces x=y even when the objective weights them differently.

