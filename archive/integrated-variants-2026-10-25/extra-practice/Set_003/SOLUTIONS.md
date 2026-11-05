# Worked Solutions — Additional Practice Set 003

## Q1

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. The data establish increased evening visits and unchanged daily totals.
2. A shift in visit timing is compatible with those observations, but individual histories were not recorded.
3. Therefore the cautious possibility in B is supported; definitive claims about individual visitors are not.
- Original option A: New visitors could have been offset by losses elsewhere.
- Original option B: A timing shift is possible and fits both reported totals.
- Original option C: No individual histories establish this universal claim.
- Original option D: The passage explicitly says daily totals were unchanged.

## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first nested loop swaps each pair of entries on opposite sides of the main diagonal exactly once, so it transposes the matrix. The second nested loop reverses each row. The composition is a clockwise 90-degree rotation. Four iterations restore the original array, and 2027 has remainder 3 modulo 4, so the net transformation is a counterclockwise 90-degree rotation. Under that net transformation, new[r,c]=old[c,4−r]. Index 7 is (r,c)=(1,2), so its value is old[2,3]=5×2+3=13. Index 17 is (3,2), so its value is old[2,1]=11. Hence the program prints `13 11`. Every pointer is inside the single a array and every swap uses distinct entries.
- Original option A: True: three clockwise quarter-turns map the queried positions to original positions (2,3) and (2,1).
- Original option B: False: these are the values after one clockwise quarter-turn, not after 2027 iterations.
- Original option C: False: these are the unchanged initial values; 2027 is not divisible by four.
- Original option D: False: these are the values after two quarter-turns, not three.

## Q3

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Two- and three-dimensional patterns

1. With A on top, the clockwise side-face order consistent with front B and right C begins B,C. The other view with the same top places D immediately before E in that order.
2. The four side labels are distinct, so their cyclic order is B,C,D,E. Opposite side pairs are B-D and C-E.
3. The third view is consistent with F opposite A and confirms the orientation without changing B's opposite.

- **A:** A is adjacent to B in the first view.
- **B:** C is adjacent to B in the first view.
- **C:** D lies two positions from B around the four side faces.
- **D:** E is adjacent to B in the third view.

**Common misconception:** Face adjacency and cyclic orientation together determine opposite faces.

## Q4

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Engineering Mathematics — Graph connectivity matching and colouring

1. The degree sum is 14, so the handshake lemma gives 7 edges.
2. G is connected and has exactly two odd-degree vertices. It therefore has an open Euler trail.
3. For a counterexample to both remaining assertions, take two disjoint triangles and connect one vertex of each by one bridge. The bridge endpoints have degree 3 and all others degree 2. The triangles exclude bipartiteness; the bridge excludes a Hamiltonian cycle.

- **A:** Each undirected edge contributes twice to the degree sum.
- **B:** Connectedness and exactly two odd vertices are sufficient.
- **C:** The two-triangle bridge construction has an odd cycle.
- **D:** A Hamiltonian cycle cannot cross a bridge and return without reusing it.

**Common misconception:** A degree sequence can force an Euler trail without forcing bipartiteness or a Hamiltonian cycle.

## Q5

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Digital Logic — Tabular minimization

Every pair of rows misses one column: P1P2 misses m6; P1P3 misses m5; P1P4 misses m4; P2P3 misses m3; P2P4 misses m2; P3P4 misses m1. Therefore at least three product terms are necessary. Every triple covers all columns. Their literal totals are 8 for P1P2P3, 9 for P1P2P4, 9 for P1P3P4 and 10 for P2P3P4. The unique preferred set is P1P2P3.

A is not a cover. B is a cover with nine literals. C is the minimum-literal three-term cover. D is a cover with ten literals.

- **A:** False: pair P1P4 misses minterm m4 and does not cover all required minterms.
- **B:** False: P1P2P4 covers all minterms but has total literal cost 9.
- **C:** True: P1P2P3 covers all minterms with the minimum total literal cost of 8.
- **D:** False: P2P3P4 covers all minterms but has total literal cost 10.

**Common misconception:** A chart with no essential prime implicant can still have a unique optimum once literal costs are considered.

## Q6

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Static and dynamic activation links.

R's lexical parent is P, so one static link reaches P. Its caller is Q, whose caller is P, so two dynamic links are required. A reverses the link roles, B assumes caller and lexical parent coincide, and C incorrectly follows a sibling in the static chain.

**Common misconception:** Lexical nesting and call nesting are different structures.

## Q7

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Loop fixed points and zero-iteration paths.

At the header, the entry edge carries x=1 and the back edge x=2; the analysis joins them as not constant, so A is false. The assignment establishes x=2 immediately after itself, proving B. The loop may execute zero times, leaving final y=1, so C is false. A do-while executes the assignment at least once and never changes x afterwards, eliminating y=1 and proving D.

**Common misconception:** A fact established by a loop body need not hold after a loop that can execute zero times.

## Q8

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** C sequencing and side effects.

A reads the old i to calculate i+1 and then assigns it, which is defined. In C, B reads i for the left index without sequencing that read relative to the increment on the right, so behaviour is undefined. The left operand of && is sequenced before the right, so C is defined. D has two unsequenced modifications of i in function arguments, so is undefined.

**Common misconception:** Function arguments are not evaluated in a guaranteed left-to-right order in C; short-circuit operators have different sequencing rules.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Composition of spatial transformations.

Track the direction vector (1,0). Reflection in y=x sends it to (0,1); a clockwise quarter-turn sends that to (1,0); reflection in the y-axis gives (−1,0). Thus B is correct. A omits the last reflection; C stops after the first operation; D is not the final vector.

**Common misconception:** Reflections and rotations must be applied in the stated order.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Outstanding bytes and the updated send window.

After the ACK, outstanding data are bytes 23000 through 24999, totaling 2000. The effective window is min(10000,4000)=4000 bytes. Thus 4000−2000=2000 additional bytes can be sent. B is correct. A uses an obsolete window edge, C ignores outstanding data, and D exceeds the receive window.

**Common misconception:** A window advertises total allowed unacknowledged data, not an allowance entirely additional to data already in flight.

## Q11

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Expression kills and a must-analysis join.

Changing c does not change either operand, so the first predecessor preserves availability (A). Assigning a invalidates the previously computed value of a+b on the second path, refuting B. The must join intersects predecessor facts and therefore omits the expression (C). Union could falsely reuse a value on the second path, so D is unsound.

**Common misconception:** Having evaluated an expression somewhere earlier is insufficient if an operand was subsequently assigned.

## Q12

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Short-circuit control flow with side effects.

The original evaluates p exactly once; when false it skips q and assigns 2. When true it evaluates q exactly once and uses its result to choose 1 or 2. C reproduces that sequence. A changes evaluation order, B evaluates q on a previously skipped path, and D duplicates p's evaluation. Side effects make all three changes observably different on some execution.

**Common misconception:** Boolean equivalence alone does not preserve evaluation behaviour of expressions with side effects.

## Q13

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Euler degree conditions and bipartite alternation.

The graph is connected, with two degree-3 vertices and three degree-2 vertices. Exactly two odd vertices yield an Euler trail (A), but no Euler circuit (B false). A path can alternate between sides of sizes three and two, beginning and ending in the larger side, so C holds. A cycle would need equal numbers from both parts, impossible when it visits all five vertices, proving D.

**Common misconception:** Euler conditions concern edge use and degrees; Hamiltonian conditions concern visiting vertices.

## Q14

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** SQL aggregate treatment of NULL and duplicates.

COUNT(*) counts four rows. COUNT(x) excludes the one NULL but retains both rows with value 2, giving three. A is correct. B excludes NULL from COUNT(*); C,D mistakenly apply DISTINCT.

**Common misconception:** COUNT(column) is not COUNT(DISTINCT column).

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Negating a universal statement.

“Not every” means that at least one submitted report lacks a diagram. Thus B is equivalent. A and C both say none has a diagram, which is stronger; D concerns a report outside the submitted set and need not hold.

**Common misconception:** Negating “all” produces “none” rather than “at least one not”.

## Q16

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Signed overflow in two's-complement addition.

For equal-sign operands, a result with the opposite sign is outside the signed range, giving A and B. The equivalent bit-level test is XOR of carry into and out of the sign bit, giving D. Opposite-sign addition stays within the signed range, so C is false.

**Common misconception:** Using the carry-out bit alone as the signed overflow flag.

## Q17

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

## Q18

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Necessary versus sufficient conditions.

The pumping property is necessary for regularity, so its failure implies nonregularity, proving A. Its converse is not supplied by the lemma, refuting B. Infinite regular languages such as a* refute C. Every sufficiently large bound also works once a pumping length works, refuting D.

**Common misconception:** Reversing a one-way implication.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordered three-dimensional transformations.

The first transformation gives (−2,1,3). Applying the second to these updated coordinates gives (−2,−3,1), A. B interchanges axes differently, C loses the required signs, and D reverses the second rotation's signs.

**Common misconception:** Applying both transformations to the original coordinates rather than composing them.

## Q20

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Product automata with Boolean acceptance predicates.

Both components accepting implements intersection (A). Exactly one implements symmetric difference (B). First accepting and second rejecting implements set difference (D). At least one implements union, not concatenation, so C is false. Concatenation needs tracking a split point rather than merely simultaneous acceptance of the entire same input.

**Common misconception:** Confusing Boolean combination of whole-word acceptance with sequential language composition.

## Q21

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Negating implication under universal quantification.

P→Q is ¬P∨Q, giving C by direct substitution. Negating the universal and then the disjunction gives ∃x(P∧¬Q), A. B requires all objects to be counterexamples rather than one; D describes the opposite truth pattern.

**Common misconception:** Negating the consequent without also handling the implication and quantifier.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** DNS record types.

AAAA records associate names with IPv6 addresses, A. Ethernet addresses, TCP sequence information and HTTP bodies belong to different mechanisms, eliminating B,C,D.

**Common misconception:** Confusing address resolution at different network layers.

## Q23

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Agreement with the head of a subject phrase.

“Neither” is singular here and correctly takes “is”, C. A needs “has”, B's singular “list” needs “is”, and D's plural “results” needs “indicate”.

**Common misconception:** Matching the verb to the nearest noun rather than the subject's grammatical head.

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Backward-shift deletion respecting probe paths.

The key in slot 3 has home 2, so moving it into the hole at 2 preserves its search path. The key at 4 has home 4 and can remain there; an empty slot 3 does not interrupt a search starting at 4. Thus B is valid. A strands the home-2 key behind an empty slot. C moves a home-4 key before its starting point and makes it unreachable by the specified search. D loses keys.

**Common misconception:** Shifting every later key blindly rather than checking whether its probe path crosses the hole.

## Q25

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: absorption. x+xy=x(1+y)=x, and x(x+y)=xx+xy=x+xy=x, so A and B hold. C fails at x=0,y=1. D is always zero and fails at x=1. Boolean addition is OR, not arithmetic addition.

## Q26

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: sequential consistency and ordering cycles. Running A entirely before B yields (0,1), so A is possible; reversing their order yields (1,0), so C is possible. Performing both writes before both reads yields (1,1), so D is possible. To obtain (0,0), A's read must precede B's write and B's read must precede A's write. Together with the two program-order edges this would form a strict ordering cycle, impossible in a sequentially consistent total order. Thus B is false. Weak-memory outcomes must not be assumed under the stated stronger model.

## Q27

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: induction-variable strength reduction. At iteration i=s+r, B's running address is base+4s+4r=base+4i; retaining i preserves its other uses. The now-unused address multiplication can be removed, so C also holds. A starts at the wrong element unless s=0. D corrupts statements that still depend on i. A derived induction variable need not replace the original variable everywhere.

## Q28

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: signed comparison after overflow. A represents −128 and B represents one. Exact difference −129 wraps to 127=0x7F, giving N=0 and V=1. Signed less-than is N XOR V=1. Thus D. A wrongly uses the unrepresentable exact difference's sign as the stored sign; B misses overflow; C gives the wrong stored sign and comparison. A subtraction's sign alone is insufficient when it overflows.

## Q29

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: mean value theorem bounds. The increase f(3)−f(0) lies between 2·3 and 5·3, so 7≤f(3)≤16. B's value ten is achieved by f(x)=1+3x. A is below seven, C and D exceed sixteen. Bounding derivatives constrains endpoint differences, not just local slopes.

## Q30

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Inclusion–exclusion for overlapping adjacency constraints.

Treat AB or BA as one block. There are2×4!=48 arrangements in X, so A is true; Y also has48. For both adjacency conditions, B must be between A and C, giving the blocks ABC or CBA. Alongside D and E, this yields2×3!=12 arrangements, not24, so B is false. The union has48+48−12=84, so C's72 is false. There are5!=120 total arrangements, leaving120−84=36 in neither set, making D true.

**Misconception:** Counting overlapping adjacency blocks as if B could be used twice independently.

## Q31

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

After A,B,C all three slots are full. The second A is a hit. FIFO retains insertion order A,B,C and evicts A for D, so B is true; its final A misses, giving five misses. LRU updates A's recency and evicts B for D, so C is true; its final A hits, giving four misses. D is true and A is false. A cache hit affects LRU recency but not FIFO insertion order.

## Q32

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both incoming definitions assign the same constant2, so their join retains x=2. The second condition is therefore true and z=7, proving A and C. The program does not assign y, so B is false. A join of equal constants preserves that constant, not the nonconstant value, making D false. Multiple reaching definitions are not by themselves evidence of varying values.

## Q33

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The owner key together with the partial key distinguishes every room, proving A. Equal room numbers in different buildings disprove B and explain D. A required, non-null foreign key checks existence of the owner; combined with the composite Room key it implements this mapping, so C is true. A partial key is unique only relative to its owner.

## Q34

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For every nonzero signed integer x, x/x=1, proving A. A dominating nonzero fact remains useful if x is unchanged, proving C. If x can be zero, replacement suppresses the invalid division, so B and D are false under the requirement to preserve the stated behavior. Algebraic identities have preconditions.

## Q35

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Discrete means distinct or separate; discreet means tactful or careful about confidential matters. B assigns both meanings correctly. A reverses them; C misuses the second word; D misuses the first.

## Q36

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Rename the inner bound variable to y to obtain R(x) AND exists y S(y), proving A. The existential part is independent of the free output x: it is true for nonempty S and false for empty S, proving C,D. It does not test S(x), so B's intersection interpretation is false. Equal variable spellings do not override quantifier scope.

## Q37

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Different acceptance at the current state is distinguished by the empty suffix, proving A. If successors were distinguishable by suffix z, the original states would be distinguished by the leading symbol followed by z, proving C. One common transition is insufficient, so B is false. Unreachability from the designated start says nothing about the two states' future languages, making D false.

## Q38

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The outer R(x,y) requires membership. The negated existential rules out another y value for that same x, so A,C are true. Other x values are irrelevant to this test, making B false. The membership conjunct excludes pairs outside R, making D false. Uniqueness is per x, not a requirement that the whole relation contain one tuple.

## Q39

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Since each element is its own inverse, (ab)^(−1)=b^(−1)a^(−1)=ba, proving A. If they commute, (ab)²=a²b²=e; ab≠e because a≠b, so its order is2, proving C. Conversely order2 gives ab=(ab)^(−1)=ba, proving D. Noncommuting transpositions in a permutation group satisfy the individual square conditions, refuting B. Individual involutions need not commute.

## Q40

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

With a common public address and common external endpoint, distinct public source ports distinguish the two active mappings, proving A. The stored mapping sends replies to the appropriate private endpoint, proving C. B incorrectly requires the private addresses to coincide. D confuses translation state with changing application payloads. Demultiplexing follows transport/address metadata under the stated model.

## Q41

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Wakeup does not certify the predicate, and another thread can act before mutex reacquisition, so A,C hold. B omits the needed recheck. D contradicts the specified reacquisition. Waiting should normally occur inside a predicate-checking loop.

## Q42

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Distributivity holds in arithmetic modulo2^n, so A is valid even across wrapping. Multiplication by0 is always defined and zero, proving C. B changes an undefined zero-divided-by-zero expression into a defined constant, so it does not preserve definedness. For n=2,x=1,y=0, the two orders in D give1 and3, refuting D.

## Q43

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The relative clause “that were discussed” modifies plural proposals, while the main clause's subject is singular “One,” requiring has. D supplies both. A is wrong in both positions; B gets the relative clause right but not the main clause; C gets the main clause right but not the relative clause.

## Q44

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The intended loads are2 and1, giving a[0]=3. The faulty first store sets a[0]=2; because k=0, the second statement then reads that changed2 for both terms, yielding4. Difference4−3=1, option D. A reverses the difference, B ignores aliasing, and C is not the difference between the two outcomes.

## Q45

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Successful exec replaces the executing program within the same process. A is false because it is not fork. B is false because descriptors without close-on-exec can survive. C is false because only a failed exec returns to the old program. D states the preserved process identity correctly.

## Q46

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The stated rise in evening visits and fall in morning visits establish a timing redistribution, C. Aggregate counts do not identify visitors, so A,B are not supported. Unchanged total visits do not rule out convenience or other benefits, so D is not supported. Visits and distinct users are different quantities.

## Q47

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An open descriptor refers to the opened file object rather than repeatedly resolving its pathname. Thus R retains F(A), while the replaced directory entry sends a later open to G(B). C confuses the directory entry with the existing open-file reference. D is false because the open reference can keep F alive after its last name is removed. Atomic replacement affects pathname visibility, not the identity of already-open files.

## Q48

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

F must precede each of I,A, and both must precede P, so F is first and P last(A,C). The middle events can be ordered I,A or A,I, giving exactly two possibilities(D). B holds only in the first order, not necessarily. A partial order specifies constraints rather than one uniquely determined narrative.

## Q49

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

T3 is younger than holder T2, so wait-die aborts T3. T1 is older than T2 and is permitted to wait. This is B; A,D apply one rule indiscriminately, while C reverses the age comparison. The scenario specifies wait-die, not wound-wait.

## Q50

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Normalize the original time to 1. The new time is 1/2+(1/2)/2=3/4, so speedup is 1/(3/4)=4/3. A incorrectly halves all time; B confuses a time reduction with a speedup factor; D ignores the improved component. The unaffected fraction bounds the benefit.

