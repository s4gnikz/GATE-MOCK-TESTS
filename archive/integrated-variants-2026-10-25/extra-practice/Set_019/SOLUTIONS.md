# Worked Solutions — Additional Practice Set 019

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Induction gives f(n)=n: the even case restores 2(n/2), and the odd case restores 2 floor(n/2)+1.
2. The call chain is 45,22,11,5,2,1, which contains six active calls at its deepest point.
- Original option A: Both the induction and explicit chain give this pair.
- Original option B: It counts five recursive edges instead of six calls.
- Original option C: The odd branches preserve the discarded low-order bits.
- Original option D: The branches do not append 1 at even n.

## Q2

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

In a downward scan, j−wi<j has not yet been updated for the current item. Thus the right-hand side combines the previous-item optimum with at most one copy of the new item, preserving the 0/1 recurrence. This proves A and D. In an upward scan, the lower entry may already contain this item: for the single item (2,3), update D[2]=3 and then D[4]=D[2]+3=6, although the true 0/1 optimum is 3. Hence C is true and B is false. The descending order is a dependency discipline that allows two DP rows to share storage.
- Original option A: True: descending capacity order preserves the previous-row dependency for every item.
- Original option B: False: upward order can reuse the current item repeatedly.
- Original option C: True: the update at capacity 4 reads the newly changed D[2]=3.
- Original option D: True: positive weight makes j−wi smaller than j, so the downward scan has not visited it yet.

## Q3

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Databases — Functional dependencies and normal forms

Neither A nor B determines C, so candidate keys are AC and BC. Every attribute is prime because each occurs in a candidate key. Each nontrivial dependency has a prime right-side attribute, satisfying 3NF. A→B violates BCNF since A is not a superkey, and similarly for B→A. Thus 3NF but not BCNF.

- **A:** False: every attribute is prime, so there is no nonprime partial dependency violating 2NF.
- **B:** False: prime right-side attributes satisfy 3NF.
- **C:** True:3NF holds while A and B are non-superkey determinants.
- **D:** False: A→B is nontrivial and A does not determine C.

**Common misconception:** Third normal form allows a prime dependent attribute even when the determinant is not a superkey.

## Q4

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Algorithms — Shortest paths

The three s-to-t paths are s-a-t of weight 4, s-b-t of weight 15, and s-b-a-t of weight 3. Thus A is true. Dijkstra first settles s, then a at distance 2, then t at distance 4, before b at distance 5 can improve a. Hence B is true for the stated algorithm.

C is false. Adding 4 per edge changes the three path weights to 12,23,15 respectively. The shortest path becomes s-a-t instead of s-b-a-t. D is false: the graph is acyclic, so it contains no directed cycle at all.

- **A:** True: path s-b-a-t has weight 3, which is strictly less than s-a-t (weight 4) and s-b-t (weight 15).
- **B:** True: Dijkstra settles vertices in order s, a, t, b, selecting path s-a-t of weight 4 before b is considered.
- **C:** False: adding 4 to each edge changes the path lengths to 12, 23, and 15, making s-a-t the shortest path.
- **D:** False: the directed graph is acyclic and contains no directed cycles.

**Common misconception:** Adding a constant to every edge preserves ordering only among paths with the same number of edges.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Multiplexer truth-table construction.

For AB=00 output C is true only at minterm 1. For AB=01 output NOT C is true at 2. AB=10 gives 4 and 5. AB=11 gives none. Therefore the on-set is {1,2,4,5}. A reverses the first two data inputs, C exchanges select groups 10 and 11, and D does not match the prescribed data inputs.

**Common misconception:** A select bit is not another data input; first identify the selected function, then evaluate C.

## Q6

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Safety test after tentative allocation.

Initially only P2's need fits (1,1). Its completion releases (1,1), giving (2,2), after which P0 and P1 can finish in either order: exactly two sequences, proving A.

Granting P0 (1,0) leaves available (0,1) and needs (0,2),(2,0),(1,1). None fits, so B is true. Granting P1 (1,0) leaves available (0,1) and needs (1,2),(1,0),(1,1); none fits, so C is false. Granting P2 (1,0) leaves its need (0,1), which fits. It then releases its enlarged allocation (2,1), yielding (2,2), and both other processes can finish. D is true.

**Common misconception:** A request fitting currently available resources need not preserve a safe completion order.

## Q7

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Static hazards and the consensus term.

Before and after A changes, F is 1. Unequal direct and complemented path delays can temporarily make both original products 0. BC remains 1 throughout, bridging the transition. It is redundant: when BC=1, either AB or (NOT A)C already makes the steady-state output 1. AC and A(NOT C) still depend on A; the latter is also 0 here and changes the function elsewhere. (NOT B)C is 0 during this transition and changes the function, for example at A=1,B=0,C=1. Thus A,B,D fail.

**Common misconception:** Boolean equivalence alone does not ensure glitch-free behaviour under unequal delays.

## Q8

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** NAT mapping keys.

Endpoint-dependent keys distinguish H1→S1, H1→S2 and H2→S1: three. Endpoint-independent keys distinguish only H1:5000 and H2:5000: two. A is correct. B reverses the policies, C unnecessarily splits the independent mapping, and D merges H1's two dependent destinations.

**Common misconception:** Equal private port numbers do not merge different private hosts, while destination dependence may split one host-port pair.

## Q9

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Safe loop-invariant code motion.

n never changes, so 100/n is invariant on iterations where it is evaluated (A). But when n=0 the original loop executes no iterations and does not divide; unconditional hoisting introduces a trap, refuting B. Guarding the hoisted evaluation with n>0 evaluates it exactly when the loop has at least one iteration, where n is nonzero and the same quotient is used throughout (C). This demonstrates D: invariance does not ensure safety on newly executed paths.

**Common misconception:** Removing repeated computation may introduce an exception even when the expression's inputs are unchanged.

## Q10

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Three-way partitioning on repeated keys.

The initial partition scans n keys in Θ(n). Every key falls into the equal part, leaving both recursive parts empty. No further nontrivial partition is performed. C is correct. A,B ignore the initial scan, and D assumes repeated recursive handling of equal keys, which this variant explicitly avoids.

**Common misconception:** Quicksort's behaviour on equal keys depends on the specified partition scheme.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Longest-prefix matching before metric comparison.

The destination lies in all three explicit blocks, including /25's range 172.16.5.128–255. The /25 is the longest match and therefore wins before metrics are compared. B is correct. A applies the tie-breaker across unequal prefix lengths; C prefers the broadest rather than narrowest match; D ignores the deterministic selection rule.

**Common misconception:** A better metric on a shorter prefix does not override longest-prefix matching under the stated policy.

## Q12

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

## Q13

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Signed encodings.

Sign-magnitude 10000000 is negative zero, numerically zero (A). Two's complement gives −128 (B). With a leading zero, both read the lower seven bits as a nonnegative value (D). With leading one they generally disagree, and the first pattern already refutes C.

**Common misconception:** A bit string has no signed numeric meaning independently of its representation convention.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Decidability from two recognizers.

Every input belongs to exactly one of L and its complement, so exactly the corresponding recognizer is guaranteed eventually to accept. Dovetailing reaches that event in finite time and yields a decision (B). A has no valid universal timeout, C discards the complementary recognizer's guarantee, and D is not a construction for complementation of arbitrary machines.

**Common misconception:** The two recognizers need not halt on their nonmembers for the combined decider to halt.

## Q15

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

## Q16

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** JK flip-flop transition rules.

(1,0) sets the output to 1; (1,1) toggles it to 0; (0,0) retains 0; (0,1) resets it to 0. Thus A is correct. B fails to toggle, C fails to set initially, and D changes state on the hold input.

**Common misconception:** Treating the toggle input as another set input.

## Q17

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Comparison groups and causal uncertainty.

A shared external factor is compatible with both decreases, so C states the justified limitation. A attributes the whole effect without isolating causes; B claims exact absence of an effect without adequate evidence; D extrapolates a universal relationship from one period.

**Common misconception:** Replacing an unsupported positive causal claim with an equally unsupported zero-effect claim.

## Q18

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Quantifier order and nonempty domains.

A common witness y works for every x and therefore supplies a witness for each x, proving A. C follows by choosing any y in the nonempty domain. B fails for equality on {0,1}: each x has its own equal y, but no y equals both. D fails for a relation containing only (0,0) on that domain, because x=1 lacks a witness.

**Common misconception:** Moving an existential quantifier across a universal one without changing its permitted dependence.

## Q19

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Modular identities and unsigned division.

A is repeated addition modulo 2^w. B follows cancellation in the modular additive group. For unsigned values, logical right shift by one equals truncating division by two, giving C. D fails already at x=1, where division gives zero and multiplication gives two since w≥2.

**Common misconception:** Importing signed-overflow or sign-extension concerns into explicitly unsigned modular arithmetic.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Shared storage versus synchronization.

Shared memory provides access to common data but does not automatically order protocol steps or exclude conflicting operations, proving B. A and C are false restrictions; D incorrectly supplies automatic serialization.

**Common misconception:** Assuming communication visibility is sufficient for a race-free protocol.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Different statistics describe different features.

The average improved while the largest delay increased, precisely B. A need not hold because a worse maximum exists. Such changes can coexist, refuting C, and they do not determine the median, refuting D.

**Common misconception:** Assuming a smaller mean forces every observation or every other statistic to decrease.

## Q22

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Path-sensitive expression availability.

On the false branch no operand changes, so t can replace the final expression, B. On the true branch a is reset to zero and the old t may differ, so unconditional replacement is unsound, A, and C is false. This is why availability must track definitions along paths, D.

**Common misconception:** Reusing an expression because it is available on one predecessor rather than all relevant predecessors.

## Q23

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Cumulative acknowledgment across holes.

The third segment leaves byte 1000 missing, so ACK=1000. The first fills 1000–1099 but leaves 1100 missing, so ACK=1100. The fourth still leaves that hole, so ACK stays 1100. The second finally fills the hole and joins all buffered data through 1399, so ACK=1400. B is correct; A follows arrival ends, while C,D advance past missing bytes too early.

**Common misconception:** Treating cumulative ACKs as acknowledgments of the most recently arriving segment alone.

## Q24

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: contiguous allocation. Free space is split into separate holes, neither large enough, which is external fragmentation (A). B concerns waste inside allocated blocks and no such block was allocated; C is unnecessary; D has no connection to the allocation failure. Total free capacity is not the maximum contiguous capacity.

## Q25

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: finite ordering constraints. The orders with exactly two true comparisons are ABC, BCA and CAB. In CAB, B finishes last, so exclude it. ABC permits A first; BCA permits B first. A and B are correct, C is impossible and D is false because feasible orders exist. Three cyclic before-relations cannot all hold.

## Q26

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: keys and lossless decomposition. C cannot be derived, so every key includes C. Either A or B then supplies the other; C supplies D. Exactly AC and BC are minimal keys (A). Determinants A,B,C are not superkeys of R, so B is false. Split off AB using A→B, leaving ACD; split that using C→D into CD and AC. Both binary splits are lossless, and AB preserves A→B and B→A while CD preserves C→D, so C is true. AB and CD alone lose the association between A and C: two original rows with distinct A and C values can recombine into four rows, so D is false. Dependency preservation alone does not prove losslessness.

## Q27

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: CFL closure and exact intersection. Each language is context-free; union and concatenation preserve this property, giving A and D. A word in both has the same a-count n but b-count simultaneously n and 2n, forcing n=0; B holds. C is the false general intersection-closure claim: for example {aⁿbⁿcᵐ} and {aᵐbⁿcⁿ} are CFLs whose intersection {aⁿbⁿcⁿ} is not. A particular regular intersection does not establish a general theorem.

## Q28

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: amortized geometric copying. Copies occur at sizes 1,2,4,... below n. Their sum is less than 2n, so A holds and B fails. An append at a full capacity proportional to n copies Θ(n) elements, making C true and D false. Amortized constant time does not mean worst-case constant time per operation.

## Q29

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Necessary versus sufficient conditions in English.

“May enter only if accompanied” asserts entry implies accompaniment, without asserting its converse. C is correct. A asserts the converse, making accompaniment sufficient. B asserts both directions. D uses “unless” to authorize entry in the absence of accompaniment and does not express the required condition.

**Misconception:** Interchanging “if” and “only if”.

## Q30

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The pumping lemma guarantees the existence of a suitable decomposition for each sufficiently long string. To refute regularity one must defeat every permitted decomposition, so A is true. The bound |xy|≤p forces nonempty y wholly into the first block of a's, so B is true. The lemma requires |y|>0, making C false. It allows every string of length at least p, including2p, making D false. Quantifier order is essential to pumping arguments.

## Q31

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first assignment makes x=0, so y=b. The later x=7 does not change the previously stored y. C is correct. A incorrectly uses the later x, B ignores multiplication by zero, and D loses the contribution of b. Track definitions at their points of use.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The stated token classes give identifier x, two separate minus operators and unsigned integer12. B is correct. A invents a signed integer token, C violates identifier boundaries, and D introduces an explicitly excluded operator. Unary-versus-binary classification is deferred to parsing.

## Q33

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

B permits a different reviewer for each report, expressing for every report there exists a reviewer. A requires one reviewer for all; C requires every reviewer for all; D denies reading. The order of quantifiers changes the claim.

## Q34

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Regular and context-free languages are closed under homomorphism, including erasing homomorphisms, so A,B are true. Erasing all symbols turns every string into ε; a nonempty input language therefore maps to{ε}, proving D and providing a counterexample to C. Homomorphisms can discard the structure responsible for nonregularity.

## Q35

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The original successor's value occupies p's position and its node is bypassed, giving the value sequence in A. A successor is needed to perform that operation, proving C. The actual removed node is the successor, not p; external references can distinguish this, so D is true and B false. Value-sequence equivalence is weaker than identity preservation.

## Q36

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The DFS tree path from an ancestor to the current vertex plus a back edge forms a directed cycle, proving A and C. An edge to a finished vertex can be a forward or cross edge without a cycle, so B is false. One local cycle does not imply all vertices mutually reach each other, disproving D.

## Q37

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Epsilon specifies no consumed input, not no state or stack action, so A,C are true. B overrestricts stack behavior, and D misinterprets epsilon as an actual character. Several internal moves may occur without advancing the input head.

## Q38

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Forwarding onto a new Ethernet link requires a new frame with the router's outgoing source MAC address and the appropriate next-hop destination MAC address. C is correct. A describes end-to-end IPv4 addresses, B transport ports, and D application data, none of which this stated forwarding operation necessarily replaces. IPv4 TTL changes, but it is not one of the offered pairs.

## Q39

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A finite format has only finitely many representable numbers, whereas a real interval contains infinitely many inputs; rounding maps many distinct inputs to the same value, proving B and refuting A. Finite precision and binary fractional representation matter even within exponent range, proving C and refuting D. Being in range avoids one problem, not every rounding error.

## Q40

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The store's MEM stage follows the load's MEM stage by one cycle, allowing the stated bypass, proving A. Without it the store may have to wait for a register-file update, proving C. B contradicts the independent address assumption; D ignores the forwarding opportunity. A consumer's required stage determines the hazard.

## Q41

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An exempt design cannot use M. Since D does, it is not exempt, proving C. Approval requires tested or exempt, so it must be tested, proving A and refuting B. D reverses an implication: nothing states that tested designs all use M. Apply the restriction to D, not indiscriminately to all designs.

## Q42

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After signal(full), the consumer can pass its wait and read while the producer is paused before writing, proving A. Atomic operations do not reorder the intervening ordinary write, refuting B,D. Publishing full only after writing ensures that this signal cannot authorize an early read, proving C under the stated one-producer, one-consumer ordering. Synchronization operations must surround the data access in the correct order.

## Q43

**Correct answer:** C, D

The underlying question is correctly answered by A, B. This variant asks for its invalid answers, so select the complementary set: C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

OR and XOR both yield0 at00 and1 at01,10, proving A,B. Their disagreement at11 is permitted because that state is unreachable. AND is0 on the two required one-input cases, refuting C. NAND is1 at00, refuting D. Don't-care freedom applies only to the explicitly unreachable assignment.

## Q44

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

When a is processed before b, both c and d are enqueued before b can enqueue e. C puts e between c and d and is impossible. A,D are possible with a's neighbors ordered c,d or d,c. B results when b is processed first, discovering e before a discovers c,d. Equal BFS distance does not make every within-level ordering attainable.

## Q45

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both original S alternatives have FIRST set {a}, causing an LL(1) table conflict: A. Factoring leaves alternatives b and c with disjoint FIRST sets, giving the equivalent LL(1) grammar in C; this disproves B. Each generated string, ab or ac, has a unique parse tree, so D is false. Failure of a particular grammar to be LL(1) does not imply ambiguity or impossibility of an LL(1) grammar for its language.

## Q46

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

There are finitely many strings in each bounded-length set. Run M on every candidate; the promise guarantees every run finishes, allowing A,B to be decided. The promise does not bound the number of inputs. For undecidability, construct a total machine that simulates a chosen machine on a fixed input for |w| steps. Accepting iff it has halted makes emptiness equivalent to nonhalting; accepting iff it has not halted makes universality equivalent to nonhalting. Thus C,D remain undecidable even on promised total machines. A per-input termination guarantee is not a bound on all inputs collectively.

## Q47

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Dovetail over all strings and allocate increasing finite steps to both recognizers on each. If a common accepted string exists, both accepting runs eventually finish, proving A,C. B can become stuck forever on an early nonmember before reaching that witness. No finite failure to find a witness proves that none exists, so D is false. A semidecision procedure need only terminate for positive instances.

## Q48

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Commit can be durable while data remains only buffered, so redo may be needed(A). Forcing a position in a sequential log can make all earlier records durable(C). WAL requires the update's log record to be durable before its data page is flushed, contradicting B. Missing flushed data for a committed transaction calls for redo, not automatic undo(D).

## Q49

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The source address establishes A's location on incoming port 1. B's destination location is unknown, so the frame floods out the other two ports. B is correct. A learns the destination from the wrong evidence; C assigns the wrong source port; D assumes the destination's physical location can be learned merely from its address in this frame.

## Q50

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The tested integer 37 is directly covered, proving A. No observation concerns 37.5, so both success and failure there remain compatible; C is correct and B is not justified. Temperatures above 100 lie outside the tested set, so D is also unsupported. A finite set of successful tests does not establish behaviour at all untested inputs without further assumptions.

