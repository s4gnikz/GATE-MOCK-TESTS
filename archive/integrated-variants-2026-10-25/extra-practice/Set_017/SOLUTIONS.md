# Worked Solutions — Additional Practice Set 017

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. At i=0, the first child breaks and prints 0; only the parent increments and continues.
2. The continuing parent similarly creates children that print 1 and 2.
3. The original parent increments to 3 and exits the loop. Thus exactly four values, 0,1,2,3, are printed.
- Original option A: One child stops in each iteration and the original parent finishes.
- Original option B: Children break; they do not take part in later forks.
- Original option C: A child preserves its copied value of i when it breaks.
- Original option D: Later children inherit i=1 and i=2, not the initial value.

## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The expected additional cost of an L1 miss is 6+0.20×60=18 ns. The initial mean is 1+0.10×18=2.8 ns. The redesigned mean is t+0.05×18=t+0.9 ns. Strict improvement requires t+0.9<2.8, or t<1.9 ns. The L2 miss probability is local, so only the fraction 0.10×0.20 (or 0.05×0.20) of all accesses reaches memory.
- Original option A: True: the redesign saves 0.9 ns of expected miss cost, so L1 can rise by less than that.
- Original option B: False: it ignores the redesigned system's remaining 0.9 ns expected miss cost.
- Original option C: False: this is sufficient but not necessary; for example t=1.8 ns also improves performance.
- Original option D: False: values such as t=3 ns satisfy it but are slower than the original.

## Q3

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Compiler Design — Liveness analysis

1. At P, z is immediately read to assign y. After the back edge to L, flag is read by the branch before any assignment to flag.
2. The old y is overwritten at P. The old x is overwritten at L before either a return or another loop iteration could read x.
3. Hence the live set is exactly {z, flag}.

- **A:** Correct: both variables have a future use before redefinition.
- **B:** Incorrect: the old x is killed at L.
- **C:** Incorrect: the old y is killed at P.
- **D:** Incorrect: neither old x nor old y survives to a use.

**Common misconception:** A variable used elsewhere in a loop need not be live at every point; track the current value across the back edge.

## Q4

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Programming and Data Structures — C programming and pointers

In the first call, t points to a[0], and assigning *p=q changes the caller's p to a+1. The next statement makes a[0]=2+5=7, and the last makes a[1]=6. In the second call, t points to a[1], while the caller's p changes back to a. Therefore a[1]=6+7=13 and then a[0]=8. The final offset p-a is 0.

A omits the last increment of a[0]. B matches the trace. C fails to follow the second call's target changes. D is false: each side effect occurs in a separate full expression, all pointers stay within the valid array, and no incompatible-type access occurs.

- **A:** False: omits the final increment of a[0].
- **B:** True: the program prints 8 13 0.
- **C:** False: fails to track pointer target reassignment across function calls.
- **D:** False: all pointer arithmetic and side effects are within valid bounds and fully sequenced without undefined behavior.

**Common misconception:** Saving the pointer value in t preserves its old target even when a pointer-to-pointer argument changes the caller's p.

## Q5

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Interleaving and lost updates.

For 2, both threads read 0 before either first write, then both read 1 before either second write. For 4, run the threads serially. For 3, let the first pair of increments lose one update, reaching 1, then execute the two remaining increments serially.

Value 1 cannot be final: the final write is a thread's second write. Its preceding read occurs after its first write, which wrote at least 1; no operation writes 0, so that final read is at least 1 and the final write at least 2. Thus A is false and B,C,D are true.

**Common misconception:** Atomic individual accesses do not make a read-modify-write increment atomic.

## Q6

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Counting versus binary semaphore event accumulation.

Counting V calls create two permits, and fair scheduling lets both P calls complete: A true, D false. With the binary version, if both V calls occur before a P, their effect collapses to value 1; the consumer prints once then blocks, proving B. Interleaving V,P,V,P preserves both wakeups and prints twice, proving C.

**Common misconception:** A binary semaphore cannot necessarily count multiple notifications that arrive before they are consumed.

## Q7

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reductions and recognizability of complements.

If L were decidable, compose its decider with the given reduction to decide halting, impossible; A holds. B contradicts the premise. If both L and its complement were recognizable, dovetail their recognizers to decide L, contradicting A; hence C holds. D mistakes a reduction into L for an algorithm deciding membership in L.

**Common misconception:** A recognizable target can still encode an undecidable problem.

## Q8

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** SLR FOLLOW-based reductions.

FOLLOW(A)={a,c}. The state reached after initial d contains S→d·c and A→d·, producing a shift/reduce conflict on c. The state reached after b d contains S→bd·a and A→d·, producing one on a. A has no other completed-production state; completed S productions reduce only on end marker, with no conflicting shift. Thus exactly two states conflict. A overlooks both; C merges distinct prefix states; D introduces an extra conflict unsupported by an item set.

**Common misconception:** SLR applies the entire FOLLOW set at a completed item, even where a more context-specific LR lookahead would be narrower.

## Q9

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recognizability and decidability.

If both U and its complement were recognizable, dovetailing their recognizers would decide U, a contradiction; A holds. Every finite language is decidable by a finite lookup, so U is infinite (B). An infinite countable U has uncountably many subsets but only countably many machines, refuting C. D is also not forced: for a recognizable undecidable K, the language {0w:w arbitrary}∪{1w:w∈K} is recognizable and undecidable while containing the decidable infinite subset of strings starting with 0.

**Common misconception:** Closure properties of recognizable languages do not extend to arbitrary subsets.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Inclusion–exclusion with a restricted denominator.

One hundred people read at least one paper. Intersection size is 70+60−100=30. Exactly-one readership is 100−30=70. The requested fraction among the 100 readers is 70/100=7/10. B is correct; A counts both-paper readers, while C,D use incorrect counts or denominators.

**Common misconception:** “Among those who read at least one” changes the denominator from the full survey size.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Expected distinct blocks via indicators.

For each of ten blocks, a random record request misses that block with probability 9/10. All ten requests miss it with probability (9/10)¹⁰, so its probability of being read at least once is 1−(9/10)¹⁰. Sum ten such indicators to obtain B. A ignores repeated blocks. C counts distinct records rather than blocks. D is only the probability that one specified block is never requested.

**Common misconception:** Linearity of expectation does not require the block-hit indicators to be independent.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Language of a left-recursive grammar.

Each recursive step appends either a or b to the right of the remaining A, and the terminating production replaces A by c. The result is c followed by any string over {a,b}, namely B. A,C place c at the wrong end; D unnecessarily forces alternating pairs.

**Common misconception:** Left recursion describes a derivation mechanism, not the position of the terminal base symbol in the final word.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Precedence-constrained parallel tasks.

Run A and B from time zero on the two workers. They finish at 4 and 3; C then runs from 4 to 6. The chain A→C requires at least 4+2=6 hours, so this schedule is optimal. B is correct; A violates that lower bound, while C,D fail to use available concurrency optimally.

**Common misconception:** Worker capacity cannot remove a precedence constraint.

## Q14

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Counting-semaphore permits.

Each signal contributes one permit, and Q needs two, so eventual scheduling lets it print (A). If Q arrives before the first signal it blocks, proving C. Counting permits do not collapse (B false), and Q cannot complete both waits before the second permit is produced (D false).

**Common misconception:** Counting semaphores preserve multiple permits, unlike a single Boolean notification flag.

## Q15

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

## Q16

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Strict asymptotic domination.

f/g=(log₂n)/√n tends to zero. This proves f=o(g), hence also f=O(g), establishing C and A. The reciprocal ratio is unbounded, refuting B and Θ-equivalence in D.

**Common misconception:** Assuming a logarithmic factor exceeds every fractional power.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Cause, intermediate effect, observation, interpretation.

Q disconnects power; S describes the lost signal; P is the alarm response; R interprets the test. B places the response first, C begins with a consequence before its cause, and D states the conclusion before the observed result. A gives the causal order.

**Common misconception:** Ignoring the events referred to by “then” and “this”.

## Q18

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Foreign keys versus uniqueness and participation.

The primary key is cid, so multiple distinct child rows can share a parent, proving A. A non-NULL foreign key must find a referenced parent, proving B. No constraint forces parents to have children, so C is false. A foreign key need not be unique, refuting D.

**Common misconception:** Importing the referenced key's uniqueness into the referencing column.

## Q19

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Direction of many-one reductions.

To decide A using a decider for B, compute f(x) and run that decider; total computability guarantees termination, proving A. The same composition with a recognizer shows that recognizable B would imply recognizable A; its contrapositive proves C. B and D fail, for example, when A is empty and B is a nonrecognizable language with a known fixed nonmember used as the constant output of f. An easy source language does not force an easy target.

**Common misconception:** Reversing the direction in which a reduction transfers an upper bound.

## Q20

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Unbounded stack height with a small alphabet.

Repeated X symbols can encode an unbounded unary count (A), which later pops can match (B). Stack height has no fixed bound, proving D. With exactly one X per prefix symbol and no alternative encoding, only the length is stored in the stack; finite control cannot distinguish every arbitrary binary prefix, so C is false.

**Common misconception:** Confusing finite stack alphabet with bounded stack capacity.

## Q21

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** MST exchange arguments independent of weight signs.

Kruskal's cut-based choices remain correct with negative weights, proving A and C. A spanning tree cannot contain a cycle even if every edge on it is negative, refuting B. Adding c to each edge adds exactly (n−1)c to every spanning tree, preserving all comparisons and ties, so D is false.

**Common misconception:** Transferring shortest-path restrictions on negative weights to minimum spanning trees.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Forked private state.

Each process starts with its own logical copy of counter=5 and increments it to six. Copy-on-write implementation details do not turn the ordinary global into shared writable state. Thus A holds; B assumes sharing, while C,D contradict the executed increment and inherited value.

**Common misconception:** Confusing initially identical contents with a shared variable.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** S-attributed definitions.

S-attributed definitions use synthesized attributes, computed from child information, so A is correct. B describes a different restriction; C removes the attributes; D excludes the very child dependency synthesis uses.

**Common misconception:** Confusing synthesized and inherited directions of information flow.

## Q24

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: HTTP representation selection. The request-header value can select different representations even for an unchanged URL; lookup must respect that variation (A). B confuses selection with freshness; C contradicts the request-header premise; D incorrectly assigns an application-layer selection rule to TCP sequence arithmetic. Resource identity and representation selection are distinct.

## Q25

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: switch learning followed by forwarding. First learn A→3 and forward to known B→2. Then B's frame to A goes to 3. C's frame to unknown D floods to 1,2,4, excluding ingress 3. Finally learn D→4 and forward to known C→3. A lists these sets. B retains A's stale entry; C floods back onto ingress; D assumes an unknown D location and then ignores known C. Learning uses the source, lookup uses the destination.

## Q26

**Correct answer:** C, D

The underlying question is correctly answered by A, B. This variant asks for its invalid answers, so select the complementary set: C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: grammar invariants and ambiguity. Each nonempty production adds one a and one b, proving A. For abab, the root production aSbS can pair its initial a with the second symbol b (empty first S, second S→ab), or with the final b (first S→ba, second S→ε). These are different parse trees, proving B. The word ba is generated, disproving C. In fact the language is all equal-count words: split any nonempty such word at the first return of its count balance to zero and induct on the two balanced parts. Intersecting with regular a*b* gives {aⁿbⁿ}, which is nonregular; therefore D is false. Equal total counts do not impose a prefix-balance condition.

## Q27

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: conflict graph. w1(X) precedes r2(X), producing T1→T2. w2(Y) precedes r1(Y), producing T2→T1. The cycle precludes conflict serializability, D. A and B each ignore one edge; C is false because read/write pairs on the same item conflict. Commit order cannot remove an existing precedence cycle.

## Q28

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: bounded blocking queues. Each first send fills its queue. Neither process reaches a receive until after its second send, but those second sends block on full queues. Once both have run that far, neither can make progress, C. A ignores capacity after the first send; B incorrectly distinguishes the symmetric processes; D invents overwrite semantics. Eventual scheduling cannot overcome this circular wait.

## Q29

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: NAT mapping capacity. Policy I needs six distinct external ports, requiring ceil(6/4)=2 public addresses. Policy II needs only three port values for each remote endpoint and may reuse them across X and Y, fitting one address. B=(2,1). A ignores policy I's six mappings; C misses remote-endpoint reuse; D overstates both requirements. Mapping identity determines which flows compete for a port namespace.

## Q30

**Correct answer:** B

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first two writes give an edge T1→T2; the last two give T2→T1. The graph has a cycle, so A and C are false. There are no read-from relationships to preserve, and T1 is the final writer. Serial order T2,T1 has the same final writer, so B and D are true. Blind writes permit view equivalence even when conflict serializability fails.

## Q31

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

An odd number of bit flips toggles parity and is detected, proving A and D. An even number leaves total parity unchanged, disproving B. Flipping one data bit and the parity bit is an example of two undetected flips, proving C. Include the parity bit itself when counting errors.

## Q32

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The forced old value permits restoration if the uncommitted update reaches disk; A and C are true. Reversing the order creates a crash interval with changed data but no durable undo information, making B false. The rule orders logging before a particular write; it does not force all committed values to disk, so D is false. Recovery information and commit durability require distinct arguments.

## Q33

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The consumer takes mutex then blocks on full=0, proving A. A producer can take an empty slot token but cannot take mutex, so it cannot insert and signal full, proving B. Any initially empty finite buffer still starts full=0, so merely increasing capacity does not fix the ordering, disproving C. Waiting for an item before taking mutex avoids holding that mutex while waiting on full, proving D.

## Q34

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The /25 covers addresses128–255 and is more specific, so200 uses Y and100 uses X: A,B are true. Lookup is based on prefix length, not installation order, making C false. Removing the /25 leaves the matching /24 for200, proving D.

## Q35

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The stream abc could split as a|bc or ab|c, so B is true. A length field can disambiguate such splits, proving C. TCP preserves bytes and order, not application record boundaries, so A,D are false. Network read sizes cannot replace a framing protocol.

## Q36

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Each of A,B,C has a NULL component and is exempt from matching under the stated rule. D has two non-null components and cannot match an empty referenced table. Apply the supplied composite-key rule rather than treating each component as an independent foreign key.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The writes are to x and y separately, so A holds. Together they leave0,0 and violate the invariant, proving B,D. In a serial order, the second transaction sees the first variable become0 and does not perform its conditional write, preserving the invariant; C is false. This is a write-skew pattern rather than a direct write collision.

## Q38

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Updating b changes the expression's operand value and kills the old a+b result's availability; C is true and A false. No operand changes between q and r, so r may reuse q, proving B. D ignores operand redefinitions. Common-subexpression elimination requires matching values, not merely matching text.

## Q39

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both mappings translate to the same frame and offset, so writes alias shared storage, proving A,C. Different virtual page numbers can map to one frame, refuting B. Without copy-on-write there is no stated fresh-frame allocation, refuting D. Virtual address distinction does not imply physical storage distinction.

## Q40

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Contingent on means dependent on fulfilment of the condition, so B preserves the meaning. A removes the dependency, C substitutes a temporal statement, and D says the outcome holds regardless of the condition. A condition is not the same as a chronological relation.

## Q41

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The error is explicitly a multiple of g, so its remainder is zero, proving A. Adding it to a valid codeword leaves a divisible polynomial, proving B. C contradicts this construction. The polynomial has three nonzero terms at shifted degrees, not one, refuting D. CRC detection depends on divisibility, not merely on nonzero errors.

## Q42

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The HEX token stops after1 because G is outside[0-9A-F]; ID then matches G. This proves A and refutes B,D. The resulting token sequence may still violate the parser grammar, proving C. Lexical validity and grammatical validity are separate questions.

## Q43

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Both tuples share B=2 but differ in A, directly violating B→A, so C. A→B holds in this instance because A values are distinct. B,D are trivial dependencies from the combined attribute set. An instance satisfying a dependency does not establish it as a constraint on all future instances.

## Q44

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

This is write skew under the stated snapshot rule. The write sets are {A} and {B}, so both pass the conflict test and both flags become zero: A,C,D are true. In either serial order, the second transaction sees the first flag cleared and does not clear its own flag, making B false. Disjoint writes do not imply preservation of an invariant involving both items.

## Q45

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Changing the IPv4 source address affects the IPv4 header checksum. The TCP checksum covers both its header, including the source port, and a pseudo-header containing IP addresses, so it also changes. D is correct. A omits TCP's pseudo-header/header changes; B omits the IP header change; C wrongly treats checksums as covering only payload. Incremental checksum updates are possible, but both fields require adjustment.

## Q46

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Near1.5, adjacent representable values are1.375,1.5,1.625, with spacing0.125. The midpoint boundaries are1.4375 and1.5625. The significand of1.5 is1.100, whose last retained bit is even; both ties therefore round to1.5. A,C are included, B is strictly inside the interval, and D is already exactly represented at1.625. Ties on both sides can select the same even significand.

## Q47

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A displaced key's probe chain can cross a deleted slot, so turning it into EMPTY would terminate search prematurely(A). Remembering a tombstone while checking the remaining chain avoids duplicate insertion and allows reuse(B). Searches must continue past tombstones, disproving C and explaining the added unsuccessful-search work in D. Deleted and never-used slots have different historical meanings.

## Q48

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The usable DNS cache can supply the address without a new query(A). An entity-tag conditional request can receive a not-modified response and reuse the body(B). DNS freshness concerns name-to-address information, not resource freshness(C). HTTP receipt does not reset DNS TTL(D). The two caches have independent validity rules.

## Q49

**Correct answer:** A

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Every bit flip toggles overall parity. An odd number of flips gives odd received parity, detecting A and D. An even number preserves even parity, so B and C are undetected by this check. The parity bit itself is not exempt from the same toggling argument.

## Q50

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Q introduces the missing entries and the comparison. P supplies that comparison's result, S uses the result to restore the entries, and R verifies the completed restoration. Thus Q,P,S,R is coherent. B mentions the result before introducing the comparison, C restores using evidence not yet supplied, and D verifies restoration before it occurs. The explicit restrictions exclude an unstated earlier operation that might otherwise rescue a different order.

