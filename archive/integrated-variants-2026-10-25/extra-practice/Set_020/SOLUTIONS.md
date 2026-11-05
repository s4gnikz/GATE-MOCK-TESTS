# Worked Solutions — Additional Practice Set 020

## Q1

**Correct answer:** C

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

1. The separator deterministically identifies the midpoint. Push each pre-separator bit, then match each later bit to the stack top and pop; accept only after the input ends with the data stack empty.
2. LIFO order compares against reverse(w), not w in its original order.
3. Choosing w=epsilon gives #, which is accepted with an empty data stack.
- Original option A: The separator removes the need to guess when to switch phases.
- Original option B: Remaining symbols mean the second half was too short.
- Original option C: For w=01, input 01#01 fails this test, while 01#10 passes it.
- Original option D: The definition allows the empty string for w.

## Q2

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

ON DELETE SET NULL changes each referencing pid to NULL, which is permitted because pid is nullable; so A holds. Updating 2 to the unused key 3 preserves the parent primary key and cascades the new value to Child, so B holds. A single-column foreign key with NULL does not require a matching referenced row, so the insertion in C succeeds. The update in D would duplicate existing parent primary key 2 and violates the primary-key constraint. Cascading describes changes to referencing rows; it does not waive uniqueness of referenced keys.
- Original option A: True: nullable pid permits the specified SET NULL action.
- Original option B: True: the new parent key is unused and the child reference follows the update.
- Original option C: False: NULL in this nullable single-column foreign key does not require a parent match.
- Original option D: True: primary-key uniqueness independently forbids changing 1 to the existing key 2.

## Q3

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Organization and Architecture — Pipelining and hazards

If the first ADD is fetched in cycle1, it writes R1 in cycle5. The second ADD's ID must be no earlier than5, so its IF must be4: two NOPs are needed between them. The second then writes R2 in cycle8, so the third's ID must be8 and IF7: two more NOPs. Four total suffice and fewer cannot meet both dependencies.

- **A:** False: two NOPs repair only one of the two immediate dependencies.
- **B:** False: at least two separations of two NOPs each are required.
- **C:** True: both consumer ID stages coincide with the corresponding producer WB stages.
- **D:** False: same-cycle write-before-read permits two, not three, NOPs per dependency.

**Common misconception:** A producer's EX completion does not make its result available without forwarding.

## Q4

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Compiler Design — Parsing

FIRST(aSbS)={a} and FOLLOW(S)={b,$}. Therefore the epsilon alternative occupies lookaheads b and $, while the other alternative occupies a. There is no LL(1) conflict, proving A and also establishing unambiguity, so B is false.

The LR(0) initial state contains S->.aSbS and S->. (the completed epsilon item). LR(0) would reduce by epsilon on every lookahead while also shifting a, causing a shift/reduce conflict; D is false. In the SLR construction, epsilon reductions occur only on FOLLOW(S)={b,$}. States where an S is expected have the same a-shift versus epsilon-reduce distinction; their reductions do not conflict. The state with S->aS.bS only shifts b, and the completed nonempty production occupies a separate state. Thus the SLR table is conflict-free and C is true.

- **A:** True: FIRST and FOLLOW sets have disjoint lookahead sets, so the grammar is LL(1).
- **B:** False: every LL(1) grammar is unambiguous.
- **C:** True: in the SLR parser, reductions are restricted to FOLLOW(S), eliminating the shift/reduce conflict on terminal a.
- **D:** False: LR(0) produces a shift/reduce conflict in the initial state between shifting on a and reducing S -> epsilon.

**Common misconception:** An LR(0) conflict caused by an epsilon reduction may disappear when reductions are restricted by FOLLOW sets.

## Q5

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Syntax-directed postfix translation.

The grammar groups the input as (8−3)−2. The first subtraction emits 8 3 −; the outer one appends 2 −. C is correct. A encodes 8−(3−2), B is prefix, and D is infix.

**Common misconception:** Postfix output follows the parse tree's grouping rather than the textual placement of operator symbols.

## Q6

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Absolute-value integration and parameter inequalities.

Split at x=t: I(t)=t²/2+(1−t)²/2=(t−1/2)²+1/4. The minimum and its unique location prove A. Symmetry gives I(1−t)=I(t), so their sum is at least 1/2, proving B. Integration gives ∫(t²−t+1/2)dt=1/3, not 1/2, refuting C. The last inequality becomes (t−1/2)²≤1/16, hence t∈[1/4,3/4], proving D.

**Common misconception:** Integrating an absolute value requires determining where the inner expression changes sign.

## Q7

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Segmentation bounds within allocated pages.

5000=4096+904 and is below 6000, so A holds. Offset 5999 is the last byte, proving C. Offsets at least 6000 violate the segment bound, even when their containing page exists; B and D are false.

**Common misconception:** Page allocation granularity does not erase an independent segment-length protection boundary.

## Q8

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Marked reversal languages and closure.

A deterministic PDA pushes the symbols before #, then compares and pops them after #; a final state indicates exactly matched input, proving A. Intersecting L with 0*#0* gives {0^n#0^n}, which is nonregular by the pumping lemma, so L cannot be regular and B is false. CFLs are closed under homomorphisms, including erasing #, proving C. In 0*#1*, the left word contains only zeros while its reversal must contain only ones, forcing both empty; D follows.

**Common misconception:** A visible midpoint enables deterministic stack switching, but does not make unbounded matching a finite-state task.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** DISTINCT aggregates and NULL exclusion.

Department A has two distinct non-NULL salaries {10,20} and sum 40; both predicates hold. Department B has one distinct non-NULL salary {20} and sum 20; neither predicate holds. Therefore only A is returned, option B. A omits a qualifying group, C selects the failing group, and D includes both.

**Common misconception:** COUNT(DISTINCT salary) ignores NULL, and SUM still counts repeated non-NULL rows.

## Q10

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reachability and residual-language equivalence.

The strings ε,a,b,ab reach p,q,r,s, respectively, proving A. From either p or q, acceptance occurs exactly when a future suffix contains b; they are equivalent, so B is false. r and s accept every suffix and are equivalent (C). Before the first b the machine alternates between p and q; after a b it stays in an accepting sink, proving D.

**Common misconception:** Distinct reachable states need not remain distinct after minimization.

## Q11

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Circular-array indices and occupancy.

Initially occupancy is (2−6) mod 8=4. The operations change head/tail as follows: dequeue (7,2), enqueue (7,3), enqueue (7,4), dequeue (0,4), enqueue (0,5). Occupancy is 4−1+1+1−1+1=5, agreeing with (5−0) mod 8. A is correct; B has the right indices but inconsistent occupancy, and C,D miscount index advances.

**Common misconception:** Index wraparound does not reset queue occupancy to zero.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Descriptor inheritance and exec flags.

The child inherits the descriptor and its close-on-exec flag. Its successful exec closes that descriptor in the child. The parent has a separate descriptor table and neither execs nor closes it, so its descriptor remains open. B is correct; A incorrectly propagates the close, C invents a fork restriction, and D ignores the flag.

**Common misconception:** Sharing an open file description does not make descriptor-table close operations global to all processes.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Allocated storage and sizeof.

Allocated storage persists until freed even if its pointer variable leaves scope (B), though losing every pointer can make it unreachable. malloc does not initialize it to zero (A). sizeof *p determines the int type's size without reading its value here (C). Allocation is three times sizeof(int), not necessarily three bytes (D).

**Common misconception:** Pointer-variable lifetime and allocated-object lifetime differ.

## Q14

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recoverability versus dirty reads.

T2 commits after the transaction whose value it read, so the displayed schedule is recoverable (A). Its read nevertheless occurs before T1 commits, making it a dirty read and refuting cascadelessness (B). If T1 instead aborted after that read, T2 could need rollback (C). The displayed commit order directly refutes D.

**Common misconception:** Recoverable schedules can still permit cascading aborts.

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** DFA upper and lower state bounds.

Store the last four bits, padding shorter prefixes on the left with zeros. This gives a complete 16-state DFA, accepting exactly when the stored first bit is 1. For a lower bound, take any two distinct four-bit words and a differing position i, numbered from the left. Appending i−1 zeros makes that differing position fourth from the right. The resulting strings differ in acceptance, so all 16 words reach distinguishable states. Exactly 16 states are necessary and sufficient. A is below the lower bound; C and D exceed the exhibited minimum.

**Common misconception:** Counting positions in an NFA as if they were sufficient deterministic memory.

## Q16

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recognizability of complementary languages.

Interleave one step of each recognizer. Exactly one language contains the input, so one simulation eventually accepts; that determines membership and yields a decider. Thus A and C hold. A decidable language need not be regular, refuting B. A recognizer can still loop on nonmembers even when another decider exists, refuting D.

**Common misconception:** Confusing existence of a decider with termination of every recognizer.

## Q17

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Undirected DFS edge structure.

Undirected DFS has tree and ancestor–descendant non-tree edges; cross edges between completed unrelated subtrees would have discovered the second subtree while exploring the first. This establishes A and refutes B. The undirected parent edge appears again in adjacency traversal and is not a separate cycle, proving C. DFS need not visit by distance layers, so D is false.

**Common misconception:** Applying directed DFS cross-edge categories unchanged to undirected graphs.

## Q18

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Listening versus connected sockets.

Accept returns connected sockets with their own lifetimes. Closing the listening socket stops accepting new connections through it but does not itself close c1,c2, proving B and refuting A. No descriptor is automatically promoted to a listener (C), and the established connections retain separate byte streams (D).

**Common misconception:** Treating all accepted connections as the same socket as the listener.

## Q19

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Unequal constant-fraction recursion splits.

At each nonterminal level, total subproblem sizes sum to at most n, giving O(n) work per level. Every root-to-leaf path has O(log n) depth because the largest child shrinks by a fixed factor, so O(n log n) follows. For the first Θ(log n) levels before even the smallest descendants reach base size, aggregate work is Θ(n) per level, giving the matching lower bound. Thus C holds; A and B omit required level work and D overestimates it.

**Common misconception:** Assuming only exactly equal halves give an n log n recurrence.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lexical recognition versus semantic binding.

A lexer can identify a spelling as an identifier without resolving its declaration, which may require scope information. B is correct. A asserts an unnecessary implementation rule; C leaps from lexical validity to type correctness; D misclassifies whitespace.

**Common misconception:** Treating tokenization, name resolution and type checking as the same analysis.

## Q21

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Diagnosis before intervention and verification.

Record the symptom, isolate its cause, replace that component, then test the result: S,Q,R,P. B verifies before replacement, C replaces before diagnosis, and D verifies before the original fault is even recorded. A is the coherent order.

**Common misconception:** Treating replacement itself as proof that the original fault was corrected.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Direction of heap-order repair.

Decreasing a key cannot make it exceed a child that was previously at least its old value. It can become smaller than its parent, requiring upward repair, A. B reverses the direction; C exaggerates the local violation; D ignores the parent relation.

**Common misconception:** Applying the same repair direction to both increasing and decreasing keys.

## Q23

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Preserving short-circuit effects and exceptions.

A and C both avoid division when x=0, preserving the original behaviour. B introduces a division-by-zero exception on that input. D changes the false result for x=0 and for many other values. Thus only A,C are sound.

**Common misconception:** Reordering apparently pure arithmetic while ignoring observable traps.

## Q24

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: dirty-page eviction. A modified page may need write-back to preserve its latest contents (A). A clean page with an identical backing copy can be discarded (B). A fault may evict either clean or dirty pages, or use a free frame, so C is false. Policies may use recency or other criteria; dirty status is not a universal selection rule, so D is false. Victim selection and preservation of its contents are separate decisions.

## Q25

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: orthogonal projections of stacked cubes. The horizontal projection contains four unit squares. In one vertical view, projected heights are the column maxima 2 and 3, giving area five. In the other, row maxima are 3 and 2, also giving five. Sum=4+5+5=14, so D. A is the volume, not the projection sum; B and C undercount the projections. Occluded cubes do not add duplicate projected squares.

## Q26

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: lexical versus dynamic scope. S is declared inside P, so its x is P's x, regardless of the R→S call chain. The two calls return 11 and 12, summing to 23 (B). A omits one increment's effect; C would increment Q's x instead, giving 21+22; D simply uses Q's unchanged value twice. Static links follow declarations, not the immediate caller.

## Q27

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: MST uniqueness conditions. Pairwise distinct weights guarantee a unique MST, B. A graph already a tree offers only its own spanning tree, C, even if all weights are equal; this disproves A. A bridge must be included in every spanning tree regardless of weight, disproving D. Distinct weights are sufficient, not necessary, for uniqueness.

## Q28

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: PDA acceptance-mode conversion. After consuming all input in an original final state, drain mode can empty the protected stack and accept, A. If input remains, drain mode has no consuming transitions and cannot meet the all-input-consumed requirement, D; B is therefore false. The fresh marker protects against premature empty-stack acceptance and must be distinguished from original symbols, so C is false. Acceptance requires both the stack/final-state condition and complete input consumption.

## Q29

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Combining implication with a cardinality constraint.

If P were ON, Q would be ON, forcing R and S OFF because exactly two switches are ON. But R OFF would require S ON, a contradiction. Hence A is true. The implication R OFF implies S ON forbids R and S both OFF, so B is true. Q need not be ON: R,S ON with P,Q OFF is valid, making C false. If Q is OFF, P must also be OFF, and the two ON switches must be R and S; D is true. The complete valid ON pairs are QR, QS and RS.

**Misconception:** Applying implications separately while ignoring the exact-count constraint.

## Q30

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For fixed i, the loop executes floor(n/i) times. Summing gives sum from1 to n of floor(n/i). This lies between nHn−n and nHn, where Hn=Θ(log n), so the total isΘ(n log n). B is correct. A ignores the harmonic factor; C and D exceed the tight growth rate. Varying strides prevent multiplication of two uniform loop bounds.

## Q31

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The shortest-path equality gives dist(v,d)=dist(u,d)−cost(u,v)<dist(u,d), so B is true. A directed cycle would require a strict descent back to the original distance, impossible; A is false. In a finite graph, an indefinitely continuing route would repeat a vertex, so with a next hop at every non-destination it must reach d; C is true. Zero-cost edges allow equality and can create cycles among tied next hops, so D is false. Exact distances and strictly positive costs are essential assumptions.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A tombstone makes lookup continue through5 to6, so B is correct. A would stop lookup prematurely. C destroys another live key. D cannot repair the probe chain for the remaining key and is not a coherent deletion operation. Deleted and never-used slots have different search meanings.

## Q33

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If A is absent, the three statements are true,false,true. If B is absent, they are false,false,false. If C is absent, they are true,true,false. The counts of true statements are2,0,2, never1. Thus none of A,B,C can be the absent person under all conditions and D is correct. The task requires checking consistency, not assuming the conditions have a solution.

## Q34

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A distinguishing future sequence disproves equivalence, so B is true. Equivalent Moore states must have equal current outputs and equivalent successors for each input, proving C. Equal output now alone leaves future behavior unconstrained, making A false. Encodings are internal labels, not external observations, so D is false.

## Q35

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Write A=2I+N with N²=0 and N≠0. Then A⁵=32I+5×16N=32I+80N. This proves B,C and disproves D. The eigenspace solves Nv=0 and has dimension1, not2, so A is false. Repeated eigenvalues do not ensure diagonalizability.

## Q36

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

N behaves identically on every input. It accepts every string if the embedded simulation accepts, and no strings otherwise, proving A,B. An emptiness decider could therefore distinguish arbitrary acceptance by negating its result, proving C. Producing N requires only embedding the simulation instructions, not resolving their outcome, so D is false.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A finite union of singleton strings has a regular expression and hence a DFA, proving A,D. Regular languages are context-free, proving B. A finite language need not contain ε, so C is false. Finiteness guarantees recognizability classes, not particular members.

## Q38

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Atomic operations serialize their counter updates. The first sees0 and sets1; the second sees1 and sets2. A,C follow, while B contradicts atomicity. A thread can start earlier but execute its atomic instruction later, refuting D. Thread start order is not the atomic operation's execution order.

## Q39

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The specified acceptance rule asks for at least one accepting branch, so D is true. A rejecting or infinite alternative does not erase a finite accepting branch, proving B and refuting A. C ignores the explicit full-input-consumption requirement. Nondeterministic acceptance is not a requirement that every branch terminate successfully.

## Q40

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A missing transition previously rejected the word, so its complement must accept it, proving C. Complete the original machine with a rejecting sink and then complement every state, including that sink: B. A leaves such words rejected; D wrongly leaves the new sink rejecting. Complementation requires total transition behaviour.

## Q41

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Remaining places are necessary for considering a late application, so with none available it cannot be considered: D. A turns a necessary condition into sufficient acceptance and confuses consideration with acceptance. B,C add claims about timely applications not covered by the notice.

## Q42

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A is a subset of finite R and C is the union of two finite sets, so both are finite. B excludes only finite R from an infinite domain, leaving infinitely many values. D excludes finite R∪S and is likewise infinite. Negation alone does not restrict free variables to stored values.

## Q43

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An aligned two-byte word uses both banks at one word address, proving A. An odd-start two-byte load crosses an aligned-word boundary, refuting B. Independent bank enables permit a one-byte store without changing its neighbour, proving C. Endianness concerns byte significance, not whether an address number is even, refuting D.

## Q44

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Invalidation removes the stale clean copy, and the next read fetches the device-updated memory. A leaves the cached value valid; C does not affect cache contents; D can keep reading the stale line indefinitely. Completion ordering alone is insufficient without cache coherence or explicit maintenance.

## Q45

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

“Had the survey included” is inversion of a past counterfactual condition. Its unreal past consequence is “would have been,” B. A uses an incompatible future perfect; C describes an awkward progressive state rather than the completed past consequence; D does not supply the required conditional consequence.

## Q46

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The reply permits both agreement and refusal as interpretations, so C captures its ambiguity. A describes length without addressing meaning; B describes evidential support; D contradicts the possibility of refusal. The explanatory clause establishes the relevant sense without requiring a claim about the witness's intent.

## Q47

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

p is a valid one-past pointer. Subtracting a within the same array yields3(A), stepping back and dereferencing yields6(B), and comparing with the same one-past pointer is defined(D). Dereferencing p itself accesses no array element and is undefined(C). Formation and comparison of one-past pointers are permitted; dereference is not.

## Q48

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Short-circuit semantics already skip f() in A,C, so replacing those expressions removes no executed side effect and preserves the constant result. In B,D, f() is evaluated first even though the final value is predetermined; replacing the whole expression would suppress its effects. Boolean algebra alone is insufficient for effectful expressions.

## Q49

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The direct path costs 2, while s→b→a costs 5−4=1, proving A. Settling a at 2 before exploring b can prevent correction, proving C. The graph is acyclic, refuting B. Its shortest path to a has two edges despite an available one-edge path, refuting D. Negative edges, even without a negative cycle, invalidate the usual Dijkstra settling guarantee.

## Q50

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The bounds on row 2 and column 2 force h(1,1)=3. The other three heights are each 1 or 2, with at least one 2 in row 2 and at least one 2 in column 2. Heights arranged as [3,1;1,2], [3,2;1,2], and [3,2;2,2] satisfy all views and give totals 7,8,9, proving A,B,C. The componentwise upper bounds sum to 9, excluding D. Projection maxima constrain columns but do not uniquely determine volume.

