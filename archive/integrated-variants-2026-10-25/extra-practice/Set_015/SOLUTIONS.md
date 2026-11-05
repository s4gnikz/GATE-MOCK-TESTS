# Worked Solutions — Additional Practice Set 015

## Q1

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. p points to the first row, and q points to the start of row 1. The addition changes a[0][2] from 6 to 9.
2. r initially points to a[0][1]. Because postfix ++ binds before unary *, *r++ stores q[0]=1 at that element, then advances r to a[0][2].
3. q[2]=*r sets a[1][2]=9. The printed sum is 1+9=10. All pointer arithmetic stays inside its row array, and side effects are sequenced across statements.
- Original option A: This misses the earlier update of a[0][2].
- Original option B: The final values are 1 and 9.
- Original option C: This retains the old value 4 in a[0][1].
- Original option D: No access is out of bounds and no scalar has unsequenced conflicting accesses.

## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For k=1, COUNT(*)=3, COUNT(v)=2 and SUM(v)=20, so both predicates are true. For k=2, counts are 2 and 0, but SUM(v) is NULL; NULL>=10 evaluates UNKNOWN and HAVING does not retain the group. For k=3, both counts are 1 and SUM(v)=5, so the group fails. SQL aggregates retain duplicate non-null values unless DISTINCT is requested. The single output row is (1,3,2).
- Original option A: True: only group 1 satisfies both HAVING conditions.
- Original option B: False: group 2 has an unknown second predicate and is discarded.
- Original option C: False: COUNT does not deduplicate rows or values without DISTINCT.
- Original option D: False: group 1 has counts 3 and 2 and sum 20, and therefore passes.

## Q3

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Digital Logic — Floating-point representation

Near 1 the spacing is 1/4, so1.125 is halfway between 1.00(binary) and1.01(binary); the even last significand bit selects1.0. In[2,4), spacing doubles to1/2. The sum 1.75+0.25=2 is exactly representable. At[8,16), spacing is 2, so9 is not representable. A,C hold.

- **A:** True: it is a midpoint and ties-to-even chooses significand1.00.
- **B:** False: the spacing in this exponent binade is 0.5.
- **C:** True: both inputs and the exact sum are representable.
- **D:** False:9 lies between consecutive representable values8 and10.

**Common misconception:** Floating-point spacing depends on the exponent, and midpoint rounding depends on the retained low bit.

## Q4

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Programming and Data Structures — Directed multigraph representation and edge-distinct walks

1. Every closed walk without a repeated edge decomposes into directed cycles using disjoint edges. Here a four-edge walk can be either two two-edge cycles or one three-edge cycle plus the self-loop at vertex 3. There is no four-vertex simple cycle and only one loop.
2. The first case combines 1→2→1 with 2→3→2. The 1→2 edge has two choices. For either choice, the resulting four-edge circuit has four distinct cyclic starting positions, including two distinct edge orders starting at vertex 2. Contribution: 2×4=8.
3. The only directed three-vertex cycle is 1→3→2→1. Insert the loop 3→3 at vertex 3. This circuit has four distinct cyclic starting positions. Contribution: 4.
4. Repeating the 1↔2 cycle would reuse the sole 2→1 edge; repeating the 2↔3 cycle would also reuse edges. Neither is allowed. The total is 8+4=12.

- **A:** Incorrect: 7 is the ordinary closed-walk count for length two, not this task.
- **B:** Correct: the two permissible cycle decompositions give 12.
- **C:** Incorrect: it does not follow from the permitted disjoint-edge decompositions.
- **D:** Incorrect: reversing a directed circuit is not automatically permitted; doubling 12 counts nonexistent reversals.

**Common misconception:** Powers of an adjacency matrix count unrestricted walks, including edge reuse. An edge-distinct restriction requires additional state or a structural counting argument.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Recursive execution order.

visit(1) prints 1. visit(2) calls visit(1), prints 2, then calls visit(0), yielding 1,2. visit(4) therefore prints 1,2 from its first call, then 4, then 1 from visit(1). B is correct. A moves the right subtree before the root; C is preorder; D assumes every value from 1 through 4 is visited.

**Common misconception:** The recursive arguments determine the visited values; they are not necessarily all integers below the initial argument.

## Q6

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Composite foreign keys and three-valued CHECK evaluation.

A skips the foreign-key check because one component is NULL, and qty=5 satisfies CHECK. B skips the foreign-key check but fails qty>0. C has both key components non-NULL, so the missing parent (9,9) rejects it despite the UNKNOWN check. D finds parent (1,2), and NULL qty produces UNKNOWN rather than FALSE, so it succeeds.

**Common misconception:** A nullable CHECK is not equivalent to requiring its expression to be TRUE; NOT NULL is a separate constraint.

## Q7

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Transient forwarding loops during routing updates.

Initially B reaches D through A at cost two, below direct cost four. After the change, A's new best route is through B at cost five, below direct cost ten. During the mixed-table interval A sends to B and B sends back to A. B is correct. A and C ignore the actual chosen next hops; D incorrectly assumes independently correct snapshots imply a consistent network-wide snapshot.

**Common misconception:** Correct shortest-path computation does not eliminate transient loops when updates are asynchronous.

## Q8

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Counter recovery and output waveforms.

States 6 and 7 enter 0 after one edge, proving A and refuting B. On states 0–5, q2=1 only for 4 and 5, two out of six intervals, proving C. The low bit has sequence 0,1,0,1,0,1 before returning to 0, proving D.

**Common misconception:** The physical number of state bits does not force a cycle containing all eight bit patterns.

## Q9

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Structural invariants of recursive productions.

Each step adds complementary symbols to opposite ends. The base is empty. Induction therefore gives strings w followed by complement(reverse(w)), and any such string can be reduced by repeatedly stripping its complementary end pair. C is exact. A is too broad: abba has equal counts but equal end symbols and cannot be generated. B is wrong because nonempty generated strings have unequal end symbols. D omits ba, which is generated.

**Common misconception:** Equal symbol counts are necessary here but do not characterize the ordering constraint.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordering constraints.

A must precede B, and B must precede C, so B can be neither first nor last. A can be first in A,B,D,C. C can be last in that same order. D can be first in D,A,B,C. Thus A,C,D do not meet the stated condition, and B does.

**Common misconception:** Not every position must be uniquely determined to exclude both extreme positions for a runner.

## Q11

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** MST structure and the next distinct weight.

AB is uniquely lightest across the cut {B}, so every MST includes it (A). Connecting C to the AB component costs at least 2, and D costs at least 3. Weight 6 is achieved by choosing AC or BC, and independently BD or CD: four trees (B). A tree using AB,AC,AD has weight 7, and integer weights permit no value strictly between 6 and 7, so C is false. AD occurs in no weight-6 tree, and increasing its weight cannot improve another tree or damage these four, proving D.

**Common misconception:** Distinct trees of minimum weight are not the same as trees of the next strictly greater weight.

## Q12

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Heap-order ancestry.

The smallest key occupies the root. If the second-smallest were deeper than a root child, its parent would have to be smaller as well, introducing a second smaller key in addition to the root. Thus only indices 2 or 3 are possible, and either is achievable. C,D have an intervening parent and are impossible.

**Common misconception:** Heap order constrains ancestors, not the full left-to-right order of the array.

## Q13

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Contraposition and existential information.

Passed calibration implies installed, so not installed implies did not pass calibration (A). The second premise explicitly supplies C. B reverses the first implication; D adds an unsupported connection between testing and calibration.

**Common misconception:** “Did not pass” need not mean a test was taken and failed; it is the negation of passing.

## Q14

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Pumping-lemma quantifiers.

The first p symbols are all a, and y is a nonempty part of that prefix, proving A. Pumping down removes positive a count while leaving p b symbols, so the result is outside L (C). Pumping twice also unbalances counts, refuting B. D violates the lemma's required decomposition constraints.

**Common misconception:** A contradiction must work for every allowed decomposition of the selected witness.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Blocking and CPU dispatch.

Completion removes the reason for blocking, making the process eligible for the CPU, hence ready. It does not terminate the process (B) or guarantee immediate dispatch (C). D describes the opposite direction and the wrong starting state.

**Common misconception:** Assuming an I/O completion necessarily preempts the current process.

## Q16

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reference and causal sequencing.

R introduces the result and competing explanations. P's “these explanations” refers back to them and introduces the repeat. Q describes that repeat's outcome; S states the ensuing conclusion. Thus R–P–Q–S is required. A uses an unresolved reference, B reports the repeat before introducing it, and D places the conclusion before its grounds.

**Common misconception:** Ordering sentences by vocabulary alone instead of their logical dependencies.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reconciling aggregate and subgroup changes.

If some existing visits move later, evening attendance rises while the daily total stays constant, so A is consistent. B directly contradicts the unchanged daily total. C contradicts the unchanged total when evening attendance rises. D asserts an error without evidence.

**Common misconception:** Interpreting growth in one time segment as growth in the whole day.

## Q18

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Completion, complementation, and state distinguishability.

The original language is a^k for k≥2. Add a dead state for every missing b transition, with self-loops on both symbols. Complementing accepting states gives a complete four-state DFA. The four original-language states corresponding to prefixes ε,a,aa,b are distinguishable: a separates ε from a; ε separates aa from ε or a; and an appropriate a-suffix separates b from each nondead prefix. Complementation preserves distinguishability. Thus four is minimal; B is too small and C,D exceed the exhibited minimum.

**Common misconception:** Complementing the accepting set of a partial DFA without first representing rejecting undefined transitions.

## Q19

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

## Q20

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Preserving expression availability across unrelated assignments.

Neither a nor b changes between t and u, so t is the correct replacement, A. c=d+e need not equal a+b, refuting B and C. D leaves a use of an undefined replacement value.

**Common misconception:** Assuming every intervening assignment invalidates every available expression.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Per-activation storage.

Each active recursive call needs its own x, and stack activation records provide these separate slots with return-time reclamation, B. A overwrites older calls' values, C falsely forbids locals, and D ignores assignments to a variable.

**Common misconception:** Allocating one slot per function rather than one per active call.

## Q22

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Liveness kill and use sets.

Assignment defines a new x and does not use old x; its right-hand side uses y and z. Thus the transfer removes x from live-out and adds y,z, B. A conflates old and new values; C reverses uses and definitions; D treats liveness as preventing assignment.

**Common misconception:** Keeping a variable's old value live merely because its newly assigned value is needed later.

## Q23

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

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: CPU execution time. Time depends on instruction count, CPI and clock period. A higher hit rate can lower memory stalls while a longer period raises time per cycle; their net effect needs magnitudes. B is correct. A asserts an unproved net benefit; C has no basis; D contradicts the permitted tradeoff. A single performance metric cannot determine elapsed time.

## Q25

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: balanced delimiters and finite memory. Distinct unmatched-OPEN counts require distinct future numbers of CLOSE tokens. An unbounded family cannot be represented by finitely many states (A). B falsely says finite inputs require infinitely many steps; C falsely calls a two-token alphabet infinite; D falsely generalizes to ordinary nonnested comments, which can be recognized by finite-state methods. It is unbounded nesting, not comments as such, that causes the limitation.

## Q26

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: Boolean sensitivity. F(0,y,z)=yz; F(1,y,z)=y+z. Their XOR is one exactly when y and z differ, giving y XOR z (B). The substituted expression has no x (C). A fails at y=z=1 because the difference is zero but OR is one; D fails at y=1,z=0 because the difference is one but AND is zero. Boolean difference uses XOR, not ordinary subtraction.

## Q27

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: backward liveness. After `x=d`, only y is needed by return. Immediately before that assignment, d is needed as its source and y remains needed, so B and D are live after statement two. The old x is overwritten before any further use, making A false; c has already had its last use, making C false. Syntactic liveness precedes any deletion of the dead assignment.

## Q28

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: precedence constraints. Both A and B must precede C, and D must follow C. Only the order of A and B is free, yielding ABCD and BACD. B is exact; A omits BACD; C puts certification before a prerequisite; D ignores the constraints. A partial order can allow several chronological sequences.

## Q29

**Correct answer:** A

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: SSTF starvation under arrivals. The head alternates between tracks 0 and 1, each new nearby request being closer than track 100. Thus the far request can wait forever, A, disproving B. A finite request set decreases by one per completed service and cannot sustain this infinite pattern, so C is false and D true. Low immediate seek cost is not a waiting-time guarantee.

## Q30

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

TCP provides an ordered byte stream. A read can return some available bytes, including bytes spanning application writes. Thus C is true. Timing can prevent the first call from gathering either particular length, so A and B are not guaranteed. TCP does not preserve write boundaries, making D false. Applications needing records must provide framing.

## Q31

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A downward scan reads dp[c−w] before that lower entry is updated for the current item, preventing its reuse; A is true. Upward scanning can read already updated values, so B is true and C false. For the example, dp[2]=3 before dp[4] is updated from dp[2]+3=6, proving D. Space compression must preserve the original DP dependency layer.

## Q32

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

In a bipartition, each vertex needs three opposite-side neighbours, forcing each side to have at least three vertices. Six vertices therefore split3+3, and every vertex connects to all three opposite vertices. This is connected K3,3, proving A,B,C. A bipartite graph has no odd cycle, so D is false. The degree constraint forces the complete bipartite structure here.

## Q33

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The pumping lemma is a necessary condition for regularity, not a characterization. Its conclusion alone therefore does not establish regularity, so C is correct. A incorrectly reverses the implication; B and D assert additional classifications not supplied by the condition. A failed attempt to contradict pumping is not a regularity proof.

## Q34

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An intervening write to the pointed-to object can change the repeated expression's value, proving C and disproving A. A valid no-modification proof restores availability and allows reuse, so B is true. Calls can have memory effects, making D false. Source-level repetition is insufficient without effect analysis.

## Q35

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An exclusive lock blocks conflicting reads until the writer ends, preventing those dirty reads and their cascading aborts, so A,B are true. Transactions can still wait cyclically for locks, disproving C. D directly violates retention until commit or abort. Strictness and deadlock freedom are different guarantees.

## Q36

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The language makes each read an observable action, so eliminating one changes behavior even when values match: B,C. This disproves A. Observability imposes no requirement that consecutive values differ, making D false. Value equivalence alone does not establish effect equivalence.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Lexicographic row-count minimization favours2 over3 regardless of the secondary cost, so A holds. Cost-first favours6 over8, proving B. These different outcomes disprove C and demonstrate D's ambiguity. State the optimization objective before comparing covers.

## Q38

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Incoming x is overwritten before use, so A is false. Incoming y is used to compute the new x and again in z, proving B. Both new x and y are needed by the second assignment, proving C. After z is assigned, only z is needed for the return, so D is false. Liveness concerns the current value's future use before redefinition, not whether the variable name occurs anywhere later.

## Q39

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The observed group difference establishes association in this sample, proving A. Optional enrolment and absent baseline information leave alternative explanations, so B is true. C claims individual causal improvements unsupported by the data. D invents equality of prior achievement. A group mean comparison alone cannot remove selection effects.

## Q40

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

With a full buffer and no consumer progress, a further blocking write can wait indefinitely, proving A. An open read endpoint is merely a reference, not an action consuming data, so B is false. Closing all readers changes the endpoint condition, rather than leaving an ordinary full pipe with a potential reader, proving C. A finite buffer cannot absorb unlimited data without draining, so D is false. Capacity can postpone blocking but cannot replace consumer progress.

## Q41

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For k²≤i<(k+1)², the step is k and the band's width is2k+1. Thus a constant number of iterations suffices to leave each band, giving O(sqrt(n)) over the bands. Each step before termination is at most sqrt(n), while total increase must be at least n−1, giving Ω(sqrt(n)). Together this proves D. A is too small; B,C overestimate growth by treating the increment as constant. Perfect-square boundaries change step size gradually, not multiplicatively.

## Q42

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The order of x divides both4 and6, hence divides2, proving x²=e and C. It also divides the odd group order, so it cannot be2; its order is1, giving x=e and A. B,D contradict that order. The two exponent equations alone would allow order2; the odd-order hypothesis eliminates it.

## Q43

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Following alpha reaches beta, which immediately leads back to alpha. No address record is supplied, so B. A,C,D invent an address unsupported by this configuration. Cycle detection can stop the futile traversal but cannot derive missing address data.

## Q44

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The stated order is archive, recalibrate, repeat, compare. Among those events, repeating directly precedes comparison, so B. A,C are earlier, and D never occurs in the account. The question concerns the narrated event ordering, not whether unmentioned activities occurred between them.

## Q45

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A deterministic PDA is a restricted nondeterministic PDA, so its language is context-free (A). Final-state and empty-stack acceptance have equivalent expressive power for nondeterministic PDAs; the standard simulation gives C. Deterministic PDAs recognize only a proper subset of context-free languages, so B is false. D can introduce acceptance in previously nonfinal states after input consumption. An equivalence theorem about machine classes is not permission to alter acceptance states arbitrarily.

## Q46

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each router decapsulates the incoming link frame and constructs an outgoing frame for the next link, so link addresses can change (A). Forwarding decrements TTL (C). In the stipulated absence of NAT/tunneling, end-to-end IP addresses remain H and J, making B false. A first-hop Ethernet destination can be the router's local interface, not the remote host, so D is false. Link-layer delivery and end-to-end addressing have different scopes.

## Q47

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Pumping twice adds k=|v|, with1≤k≤p. Since(p+1)²−p²=2p+1>p, the new length lies strictly between consecutive squares, proving A. Primality is irrelevant and not guaranteed(B); the next square is too far away(C); pumping twice increases rather than decreases length(D). The interval argument covers every legal block length, not one selected decomposition.

## Q48

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The returned function must retain the captured variable for later use(A), and an environment with a sufficiently long lifetime can do so(C). A pointer into reclaimed storage does not preserve a valid variable(B). Lexical capture refers to outer's binding, not an unrelated caller's variable(D). The lifetime of an escaping environment can exceed the dynamic lifetime of its original call.

## Q49

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The initial in matches the keyword and identifier patterns at equal length, so priority makes it a keyword. The dot is its own token. The entire inner is a five-letter identifier, longer than the keyword prefix in; longest match therefore selects the identifier. A is correct. B and D ignore keyword priority for the first token. C incorrectly lets keyword priority override a longer identifier match. Priority resolves ties only after maximal length is determined.

## Q50

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

EOF requires no write descriptors remain open and all buffered bytes are consumed. The child itself retains an open write end, so it can block after reading the message, proving A and refuting B. Closing that unused end removes the obstacle; after the parent's close and buffer drain, EOF can occur, proving C. Waiting does not close another process's descriptors, refuting D. The parent's wait can therefore participate in a hang caused by inherited descriptor ownership.

