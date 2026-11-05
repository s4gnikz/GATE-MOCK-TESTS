# Worked Solutions — Additional Practice Set 012

## Q1

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. The longest identifier prefix is ifx; a keyword prefix does not split it.
2. Maximal munch chooses == rather than two = operators.
3. The next identifier is exactly if, followed by ++ and +, because +++ is not a token. The final token is x.
- Original option A: A keyword prefix cannot split the longer valid identifier ifx.
- Original option B: Every boundary follows maximal munch.
- Original option C: It splits == and fails to take ++ at the first plus.
- Original option D: +++ is not among the recognized operators.

## Q2

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Five destinations have 2^5−1=31 nonempty subsets. There are 8×31=248 non-idle bus commands and one idle command, giving 249 commands. Since 128<249≤256, the joint bus field needs 8 bits. Independently, six ALU choices need 3 bits, 128 addresses need 7 bits, and four sequencing conditions need 2 bits. The total is 8+3+7+2=20 bits. A separate source field plus five literal destination-enable bits would consume more bits, but the question explicitly permits a joint binary command encoding.
- Original option A: False: the other fields need 12 bits, leaving only seven bus-command bits, which cannot encode 249 commands.
- Original option B: True: 8 bits for the 249 bus commands plus 3+7+2 bits for the other fields gives 20.
- Original option C: False: 21 bits suffice but are not minimal; joint encoding uses eight bus bits instead of separately encoding source and destination enables.
- Original option D: False: the command choices can be binary encoded; 20 bits already suffice.

## Q3

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Programming and Data Structures — Binary search trees

With a nonempty right subtree, the successor is its minimum-key node, found by following left-child links from x's right child. It therefore lies in that subtree and has no left child. It can have a right child: for root 10 with children5,15 and node15 having right child 20, the successor of 10 is 15. Hence A,C,D hold and B fails.

- **A:** True: successor is the minimum of the nonempty right subtree.
- **B:** False: the minimum node can have a right child.
- **C:** True: a left child would have a smaller key in that same subtree.
- **D:** True: a right child does not violate minimality in the right subtree.

**Common misconception:** The successor's lack of a left child does not make it necessarily a leaf.

## Q4

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Theory of Computation — Pushdown automata

The finite language L is regular, so a DFA recognizes it. A final-state DPDA can simulate that DFA without using its stack. A nondeterministic empty-stack PDA can choose whether to finish after a or to wait for b and then finish.

A deterministic empty-stack PDA accepting a has a unique computation on that prefix. On input ab it must follow the same computation until the prefix a has been consumed. If it then empties its stack through epsilon transitions, determinism prevents choosing a b-consuming alternative, and no transition can consume b after the stack is empty. Hence it cannot also accept ab. This is the prefix-free obstruction under the stated conventions.

A, B and C can recognize L by the constructions above. D cannot.

- **A:** False: a DFA recognizes the regular language {a, ab}, so a final-state PDA can also recognize it.
- **B:** False: an NPDA can nondeterministically guess whether to accept after a or after ab.
- **C:** False: a DPDA accepting by final state easily recognizes {a, ab}.
- **D:** True: a DPDA accepting by empty stack cannot recognize {a, ab} because it is not prefix-free and no end marker is provided.

**Common misconception:** Final-state and empty-stack acceptance have equivalent power for nondeterministic PDAs, but not automatically for deterministic PDAs without an end marker.

## Q5

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Bounded simulation and decidability.

A is decidable by simulating at most 100 transitions. C is decidable by checking whether any rejecting state is reachable from the DFA's start state. B is the general halting problem. D is undecidable: given machine M and input w, construct a machine that ignores its own input and simulates M on w; it halts on all inputs exactly when M halts on w.

**Common misconception:** A finite description does not imply a computable bound on an arbitrary computation's duration.

## Q6

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Limits of the unweighted interval greedy rule.

Earliest finish chooses A then C, then E rather than F because E starts earlier in the finish-time tie. Its weight is 12. For the optimum, the best compatible predecessor totals at A,B,C,D,E,F are 4,5,8,10,12,13. In particular B,D,F attain 13. Thus C gives (12,13). A misses the better weighted solution; B attributes it to the greedy rule; D miscounts the greedy choices.

**Common misconception:** Maximizing the number of compatible intervals does not maximize their total weight.

## Q7

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Heap deletion and sift-down.

Move 3 to the root and remove the last slot: [3,8,7,6,5,4]. Swap with larger child 8, then larger child 6, giving [8,6,7,3,5,4]. A unnecessarily sorts the keys; C violates root heap order; D swaps the wrong lower-level elements.

**Common misconception:** A heap is partially ordered; deleting its root does not sort the remaining array.

## Q8

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Longest-prefix fallback after withdrawal.

160 lies in the withdrawn /17 but outside the surviving /18, so it falls back to the /16 via B. 200 remains inside the /18, so uses D. A skips valid more-specific routes; B retains the withdrawn route; C ignores the surviving /18.

**Common misconception:** Withdrawing a prefix does not withdraw its more-specific routes.

## Q9

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Asymmetric signed range.

The eight-bit signed range is −128 to 127. Negating 10000000 wraps back to 10000000, although mathematical +128 is outside that range. Zero (A) also negates to itself but its negation is representable. 127 and −1 (B,C) have representable, different negatives. Only D satisfies both conditions.

**Common misconception:** Two's-complement ranges have one more negative value than positive values.

## Q10

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Conditional HTTP validation.

A matching entity tag permits the server to report that the cached representation may be reused without transferring the full representation body. The client still sends the request and receives the validation response, so a network round trip remains (C). A confuses validation with a fresh local-cache hit. B incorrectly assigns a representation body to 304. D makes an unsupported claim about unrelated caches.

**Common misconception:** Saving transferred bytes and eliminating network latency are different benefits.

## Q11

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lossless BCNF decomposition versus dependency preservation.

The intersection is A, which determines R1=AB, proving losslessness (A). R1 has key A; R2 has no nontrivial projected dependency with a non-superkey determinant, so both are BCNF (B). To refute preservation of BC→A, take R1={(1,b),(2,b)} and R2={(1,c),(2,c)}. Both obey their projected dependencies, but their join contains (1,b,c),(2,b,c), violating BC→A (C). A alone cannot determine C in the original schema, so it is not a key (D is false).

**Common misconception:** Losslessness and dependency preservation are different properties.

## Q12

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Error-detection parity.

Each flipped bit toggles total parity. Any odd number of flips changes even to odd and is detected, proving A,C. Two flips restore the original parity, refuting B; the same counterexample refutes D.

**Common misconception:** A parity bit detects every odd-weight error, not every nonzero error.

## Q13

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** A decreasing distance as a loop-prevention invariant.

With w(v,u)>0, d(u)=d(v)−w(v,u)<d(v), proving D; strict decrease around a directed cycle is impossible, proving A. With a zero-cost A–B link and unit-cost links from both A and B to t, both distances are 1. Each may choose the other as an equal-cost next hop, producing a cycle despite exact distances (B). This example refutes C.

**Common misconception:** Nonnegative costs suffice for shortest-distance algorithms, but strict decrease of chosen forwarding distances needs positive costs or an additional tie rule.

## Q14

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Dependency-preserving chained decomposition.

AB,BC,CD directly enforce each stated FD. Joining AB with BC is lossless because B determines BC; joining that result with CD is lossless because C determines CD. Thus A has both properties. B loses B→C across its disjoint components; C and D similarly cannot enforce the original chain using only their projected dependencies and lose essential associations.

**Common misconception:** Keeping all attributes across components does not by itself preserve their dependencies or tuple associations.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Precise exceptions and retirement.

On an older fault, architectural state must exclude younger instructions' effects. Deferring visible stores preserves that boundary, making A correct. It neither fixes load latency (B), removes dependencies (C), nor guarantees predictions (D).

**Common misconception:** Treating speculative execution and architectural commitment as the same event.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Independently expiring DNS records.

The CNAME expires at time 120, so at time 80 it has 40 seconds remaining. The A record expires at 20+50=70 and is already stale. Reuse the live alias mapping but resolve its target afresh: B. A wrongly assigns the CNAME's lifetime to the A record; C reverses which record expired; D disregards TTL expiry altogether.

**Common misconception:** Treating a cached alias chain as one record with one shared expiration time.

## Q17

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Value relations across redefinitions.

Let initial a be a0. Then t=a0+b, final a=a0+1, u=t+1 and v=t. Therefore final a+b−1 equals t (A), and u may be replaced by t+1 (C). B lowers u by one. D removes a definition whose value is still required, so it cannot preserve all final values.

**Common misconception:** Reusing an expression after one operand changes without adjusting its value relation.

## Q18

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Universal quantification with a domain restriction.

A requires Works(e,d) for each d that is a department, while not constraining other domain objects. B requires merely one department. C demands that every domain object be a department and assigned, which is too strong. D expresses no assignments. If Department is empty, A correctly holds vacuously for every employee.

**Common misconception:** Using conjunction instead of implication to restrict a universal quantifier.

## Q19

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** A counterexample to greedy coin selection.

Greedy chooses 4, then 1, then 1, using three coins. The feasible choice 3+3 uses two, and one coin cannot make six. Thus B is correct. A gives the wrong greedy count; C ignores denomination one; D ignores 3+3.

**Common misconception:** Assuming the familiar greedy rule works for every denomination system.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** A necessary prerequisite.

B forbids restarting before closure, exactly expressing the prerequisite. A reverses the time order, C removes the prerequisite, and D converts a necessary condition into a sufficient automatic trigger.

**Common misconception:** Equating “only after” with “whenever”.

## Q21

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Precedence and associativity encoded in grammar levels.

Multiplication is built inside T before addition combines T terms, establishing A. Left-recursive addition groups chains on the left, establishing B. Immediate left recursion causes naive recursive descent to recurse without consuming input, refuting C. The separated precedence levels give the unique parse id+(id*id), refuting D.

**Common misconception:** Assuming left recursion implies ambiguity rather than an implementation issue for naive top-down parsing.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Gaps between successive squares.

Pumping once extra gives length p²+d. It exceeds p² because d≥1, but d≤p<2p+1, so it is below (p+1)². Thus it is not a square and leaves the language, A. B reverses the inequality; C is false; D invents an alphabet restriction.

**Common misconception:** Failing to bound the pumped length between consecutive allowed lengths.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** One-bit addition.

Unequal inputs yield sum one, giving XOR. Both inputs one produce carry one, giving AND. A combines these correctly. B mishandles 11 in its sum, C swaps incompatible functions, and D does not implement addition even at 00.

**Common misconception:** Using OR as the sum bit without checking the two-one case.

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: logical sequencing. Comparing the result with the requirement (S) reveals a mismatch; identify its source (Q), revise that step (R), and test the revision (P). B follows these dependencies. A tests before revision and identification; C revises before identification; D tests before the stated revision and places the initial comparison last. Distinguish discovery from verification.

## Q25

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: Shannon decomposition of parity. Sum=a XOR b XOR c. For ab=00,01,10,11 it is c,c′,c′,c, hence B. A is the carry-out input pattern, not sum. C complements every required output. D gives only a, independent of b and c. Separate sum and carry functions.

## Q26

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: NULL and anti-joins. For x=1 or 3, NOT IN encounters UNKNOWN from comparison with NULL; for x=2 it is false. WHERE retains none, so A holds. NOT EXISTS checks for a true equality match; only x=2 has one, giving 1,3 and making B true. COUNT(y) ignores NULL and returns one, so C is false. NULL=NULL is UNKNOWN, not TRUE, so D is false. NOT IN and NOT EXISTS are not interchangeable with nullable subqueries.

## Q27

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: true versus name dependences. Renaming separates an earlier reader from a later writer using the same architectural name (WAR), and separates different writers (WAW), so B and D. A's consumer still needs its producer's actual value, and C depends on the branch outcome, so neither is removed merely by register names. Renaming is not value prediction.

## Q28

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: open-file descriptions versus descriptors. p and q share an offset: read(p,2) gets AB and moves it to two; read(q,1) gets C and moves it to three. r has its own offset; seek to one and read two gives BC without changing p/q. The final p read gets D. Thus D. A treats dup as a separate open; B wrongly advances the shared offset on r's read; C misplaces r's explicit seek. Sharing the underlying file does not always mean sharing an offset.

## Q29

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: ordered auto-increment addressing. Source read uses 100 and gives three, then R becomes 104. Destination read uses 104 and gives five, then R becomes 108. The sum eight is written to captured destination 104. C=(108,8). A and D omit an increment; B reads the wrong destination value. The explicitly stated evaluation order resolves reuse of the same address register.

## Q30

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A store through q may modify the object read through p. If p=q and its old value is4, x=5 while y=10, proving C and disproving A. Proven distinct objects prevent this store from changing *p, so B is true. D ignores aliasing and is false. Availability of an expression depends on memory effects, not just matching source text.

## Q31

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The query selects every domain value absent from a finite relation; over the infinite domain this is infinite and includes values outside the active domain. B is correct and A false. Negation can be safe when variables are appropriately range-restricted, so C is false. Complementation does not reproduce R, making D false. Finiteness of stored input does not ensure safety of an unrestricted query.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Selection rewards either of two attributes, so among selected applicants one attribute can compensate for the other. This can induce the reported association, supporting B as a possibility. A asserts causation and population generality without evidence. C contradicts the stated selection rule. D rules out a combination that the rule permits. A selected subgroup need not preserve population associations.

## Q33

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

F can only output values satisfying R, so A and D are true. G includes the infinite complement of finite S, making B true. Range-restricted negation is not inherently unsafe; F illustrates this, disproving C. Safety depends on how variables are bounded, not merely on the presence of negation.

## Q34

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A→D→C already implies AB→C, so deleting AB→C preserves the closure and A is true. Starting from C without C→B reaches no other attribute, so that dependency is not redundant and B is false. A determines D,C,B and is minimal as a singleton, making C true. D reaches C,B but not A, so D is false. Testing redundancy requires closure under the set with the tested dependency removed.

## Q35

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Acceptance by a recognizer certifies membership, so A is true. A sufficiently long computation may still accept later, invalidating B's arbitrary cutoff. Deciders halt on every input, proving C; recognizers need not, disproving D.

## Q36

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Correct mutex acquisition serializes the two regions, so no update is lost: A,B. Either thread may acquire first, disproving C. An unmatched unlock does not replace mutual exclusion and may itself be invalid, disproving D.

## Q37

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The rule says nonanonymous implies includes-name. Only C has a true antecedent and false consequent. A and D are anonymous and therefore exempt under this rule, while B satisfies the requirement. No converse prohibition on names in anonymous submissions is stated.

## Q38

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Suggestive evidence provides support without establishing certainty; a provisional recommendation can be revised. B preserves both meanings. A upgrades both to certainty and finality, C reverses the evidentiary direction, and D substitutes irrelevance and unanimity, neither stated. The qualifying words control the strength of the claim.

## Q39

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Given a decider for L, compute the reduction f(M,w) and run that decider to decide HALT, proving C. Since HALT is undecidable, A follows. The reduction provides hardness, not an upper bound on L's recognizability, so B need not hold. Likewise it does not supply the reverse reduction in D. A one-way reduction must not be silently reversed.

## Q40

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Every nonroot node has a smaller ancestor, so the second-smallest can only be a root child, proving A. The distinct-key min-heap property makes every parent strictly smaller, proving C. The sorted array[1,2,3,4,5,6,7] is a heap with third-smallest at index3, refuting B. The valid heap[1,3,2,7,6,5,4] is not globally sorted, refuting D. Heap order constrains ancestors, not arbitrary array positions.

## Q41

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Doubling w gives even length, proving A. abba is an even palindrome but its halves ab and ba differ, refuting B. abab=(ab)(ab) is not a palindrome, proving C. Reversing ww gives reverse(w)reverse(w), proving D. Repetition and reflection are different symmetries.

## Q42

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For s=0, T=a and F=T=a. For s=1, T=b and F=NOT T=NOT b. This proves A. When a=b, these two outputs are complements, proving B. When a≠b, a=NOT b and they agree, proving C. With s=a=b=0, F=0, but with s=0,a=b=1, F=1 whereas s XOR a XOR b=0, refuting D. Evaluate the two selection levels in their stated order.

## Q43

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The shift yields floor(−3.5)=−4, while division truncates to−3. Difference−4−(−3)=−1, option D. A treats both rounding directions as identical; B reverses subtraction; C is unrelated to the two resulting integers.

## Q44

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Pinning prevents eviction/reuse until the physical-address transfer finishes, proving A. If the frame is reused, the device still targets that same physical address and may corrupt the new allocation, proving C. A stable virtual name does not prevent physical reuse, refuting B, and D contradicts the stated DMA addressing model. Page-table remapping and device address state require coordination.

## Q45

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Unsigned addition gives 0x80+0xFE+1=0x17F, so the low byte is 0x7F and carry C=1. Therefore A is true and B is false. Signed subtraction is −128−1=−129, outside [−128,127], so V=1 and D is false. Carry and signed overflow answer different questions.

## Q46

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

accept returns a separate connected socket, while the listening socket can keep accepting, D. A incorrectly replaces the listening endpoint; B confuses accepting with application data transmission; C wrongly couples the descriptors' lifetimes. Closing a connected endpoint does not inherently close the listener.

## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The entire five-character input matches ID, so maximal munch selects one identifier(B). The shorter initial match IF loses despite keyword priority, which applies only on equal-length matches. A,C split before the longest match ends; D contradicts the permitted digits after the first letter. Token priority and longest-match selection serve different roles.

## Q48

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

j doubles monotonically across the entire program and is not reset per i, so the while body runs only floor(log2 n)+1 times in total. The outer loop still performs n iterations and tests, giving Theta(n). A omits those iterations, B incorrectly multiplies the total doubling count by n, and D assumes a linear inner loop each time.

## Q49

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The owner key distinguishes loans; the partial key distinguishes installments of a given loan. Their pair identifies each installment, so C. A collides across owners; B collides among installments of one owner. Amount need not be unique at either level, so D fails. A weak entity's partial key is interpreted within its owner.

## Q50

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For each i the inner loop visits i,2i,…,floor(n/i)i, proving A. The total is bounded above by nH_n and below by nH_n−n, hence Θ(n log n), proving B and refuting D. Only loop counters and constant-size state are needed; no array of iterations must be stored, so C is false. Counting the inner loop as n iterations independently of its stride overestimates the work.

