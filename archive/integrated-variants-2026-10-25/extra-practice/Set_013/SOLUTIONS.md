# Worked Solutions — Additional Practice Set 013

## Q1

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

1. Ordinary routing keeps the end-to-end IPv4 destination and TCP port unchanged.
2. Forwarding decrements TTL and constructs an Ethernet frame for the outgoing LAN's next hop.
3. Therefore A and C hold; the incoming and outgoing link-layer destinations need not match.
- Original option A: No address translation occurs.
- Original option B: The outgoing frame addresses the next hop on a different LAN, not necessarily the incoming destination MAC.
- Original option C: The stated assumptions ensure ordinary forwarding with a one-hop decrement.
- Original option D: TCP ports identify endpoints; a transit router does not replace them.

## Q2

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. P(N>=2)=P(first positive)=11/40. Reaching test 3 requires the first two positives, whose probability is (1/4)(4/5)^2+(3/4)(1/10)^2=67/400. Thus E[N]=1+11/40+67/400=577/400.
2. N=3 does not disclose the third result. P(faulty | N=3)=[(1/4)(4/5)^2]/(67/400)=64/67. The value 512/515 would instead condition on three positives.
3. Exactly two positives before a negative is the path ++-. Faulty and sound weights are (1/4)(4/5)^2(1/5)=128/4000 and (3/4)(1/10)^2(9/10)=27/4000, giving posterior 128/155.
4. Positive first and negative stopping includes paths +- and ++-. With conditional positive probability p, their total probability is p(1-p)+p^2(1-p)=p-p^3. Faulty and sound weighted probabilities are 288/4000 and 297/4000. Their posterior ratio is 288/585=32/65.
- Original option A: The tail-sum formula uses the probabilities of reaching the second and third tests.
- Original option B: Reaching three tests means only that the first two were positive; the third may be negative.
- Original option C: This conditions on the specific path ++-, with weights 128 and 27.
- Original option D: The two possible terminating paths give weights 288 and 297, whose normalized faulty weight is 32/65.

## Q3

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Compiler Design — Local optimization

Write initial values b0,c0. The first statement sets a=b0+c0. The second sets b=(b0+c0)-c0=b0. The third reads this restored b and sets c=(b0+c0)-b0=c0. Thus b and c end unchanged, and only a=b+c is required.

- **A:** True: a becomes the sum and b,c retain their original values.
- **B:** False: it changes b whenever b0 differs from c0.
- **C:** False: it changes c to b0+c0 rather than preserving c0.
- **D:** False: it generally changes both b and c.

**Common misconception:** Algebraic simplification must track which version of each variable an expression uses.

## Q4

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Theory of Computation — Closure properties and regular restrictions

1. L is context-free: it is the union of the context-free languages with i=j and with j=k. R is regular, expressed as a*(epsilon|b|bb)c*.
2. For each fixed j in {0,1,2}, membership of L intersect R requires i=j or k=j. Its portion for that j is a^j b^j c* union a* b^j c^j. These are regular, and their finite union is regular.
3. L minus R equals L intersect the complement of R. A context-free language intersected with a regular language remains context-free.
4. L minus R is not regular. Intersect it with the regular language a*b* (no c symbols). Since j>2, the alternative j=k=0 is impossible, leaving {a^n b^n:n≥3}, which is nonregular. A regular L minus R could not have this nonregular regular-language intersection.
5. In L intersect S we have i=k, together with i=j or j=k. Either alternative forces all three counts equal. Thus the intersection is {a^n b^n c^n:n≥0}, which is not context-free. For the standard pumping argument, choose a^p b^p c^p: a pumping window of length at most p cannot cover all three blocks, so pumping changes at least one count while leaving another unchanged, or violates block order.

- **A:** Correct: the middle block is bounded, giving a finite union of regular languages.
- **B:** Incorrect: the c-free regular slice proves nonregularity.
- **C:** Correct: difference by a regular language preserves context-freeness.
- **D:** Incorrect: the equal-outer-count restriction forces three equal block counts.

**Common misconception:** Intersection with a regular language preserves context-freeness, but intersection with another context-free language need not; bounded and unbounded restrictions behave differently.

## Q5

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Chip selection and local addressing.

Each chip covers 0x1000 bytes. Chip bases are 0x8000,0x9000,0xA000,0xB000. Address 0x9ABC lies in chip 1 at offset 0xABC. A fails both the range and local-offset requirement; B chooses the next chip; C exceeds the maximum local offset 0xFFF.

**Common misconception:** Local chip addresses exclude the bits used to select the chip.

## Q6

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Common subexpressions with changing variable versions.

Share x*y with y*x, and share their identical sums with z. After x=x+1, x has a new value, so the later multiplication and sum cannot be shared with the earlier ones. Required operations: two multiplications, one initial sum with z, one increment, one final sum with z. Thus (2,3). A incorrectly shares across the definition of x; B omits the increment; D fails to merge the initial commutative products.

**Common misconception:** Equal variable names do not guarantee equal expression values across assignments.

## Q7

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lossless decomposition and dependency preservation.

The intersection is B, which determines R2's attributes, so the decomposition is lossless. A→B is checkable in R1 and B→C in R2, preserving both. Each component's determinant is its key, so both are BCNF. In R, B does not determine A, and B→C violates BCNF. Thus A,B,D are true and C false.

**Common misconception:** A decomposition may improve normal form while also being lossless and dependency-preserving.

## Q8

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Directory links versus open-file references.

An open descriptor keeps the unlinked file available until the reference is released, proving A and refuting B. Removed pathnames no longer resolve to it, proving C. Open descriptors are not directory hard links; the hard-link count is zero, refuting D.

**Common misconception:** Removing a name is not necessarily the same as immediately destroying the referenced data.

## Q9

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Closures and minimal keys.

AB determines C and hence all attributes; neither A nor B alone does, so AB is a candidate key. BC determines A through C→A, and neither B nor C alone determines all attributes, so BC is also a candidate key. AC lacks B, and C's closure is only AC. Thus A,C are correct and B,D are not.

**Common misconception:** A determinant of one dependency need not be a key for the entire relation.

## Q10

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Conflict versus view serializability with blind writes.

On x, the first two writes create T1→T2, while the second and third create T2→T1. This cycle rules out conflict serializability. For view equivalence, x's final writer T1 forces T2 before T1. The read of y by T3 reads T2's write, forcing T2 before T3. No constraint orders T1 versus T3. Thus the two serial orders are T2,T1,T3 and T2,T3,T1. A is correct. B,D incorrectly ignore the conflict cycle; C incorrectly treats it as proof against view serializability.

**Common misconception:** Blind writes allow some view-serializable schedules to fail conflict serializability.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Register coloring and an odd cycle.

A five-cycle has edges but no triangle, so its largest clique has size two. Alternating two colors around the cycle forces equal colors at the closing edge, making two registers insufficient. Three suffice, for example a=1,b=2,c=1,d=2,e=3. B is correct. A misses the odd-cycle obstruction; C,D invent a triangle, and D also overallocates registers.

**Common misconception:** The maximum clique gives a lower bound on required colors, not always an exact answer.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Priority aging.

Waiting gradually improves a job's urgency, counteracting indefinite postponement by newly arriving high-priority jobs. This is B. It does not change mutex acquisition order (A), page allocation (C), or cache/DMA coherence (D).

**Common misconception:** Scheduling starvation and resource deadlock require different remedies.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Mean versus dispersion.

Reduced variability means reduced dispersion under the reported measure, so B follows. It need not eliminate all variation (A), make the unchanged mean zero (C), or establish bias relative to a true value (D).

**Common misconception:** Precision and accuracy are distinct properties.

## Q14

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Combinational dependency depth.

The final carry can depend sequentially on all n propagation stages, taking n units (A). Extra lookahead/group logic can shorten that dependency chain (C). Physical simultaneous presence of gates does not remove signal dependencies, refuting B. The ripple bound grows with n, refuting D.

**Common misconception:** Gate parallelism and critical-path depth are different measures.

## Q15

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Finite configuration-space reachability.

Determinism makes a repeated nonhalting configuration repeat its entire future, proving A. Record configurations and stop on acceptance, rejecting halt, or repetition; finiteness ensures one occurs, proving C. Plain simulation can loop forever, refuting B and D.

**Common misconception:** Confusing finitely many possible states with finitely many execution steps.

## Q16

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Vocabulary in context.

The following clause explicitly attaches a condition to the endorsement, establishing C. A is a different meaning of “qualified” and is not supported here. B removes the condition, while D denies the support that the sentence explicitly reports.

**Common misconception:** Choosing a familiar dictionary meaning without checking its context.

## Q17

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Recursion-tree harmonic sums.

Write n=2^k. At depth j with subproblem size at least four, the aggregate merge cost is Θ(n/(k−j)). Summing j=0,…,k−2 gives Θ(n Σ_(r=2)^k 1/r)=Θ(n log k). The leaves cost Θ(n), so the result is Θ(n log log n), B. A omits the growing harmonic factor, C treats every level as Θ(n), and D overcounts beyond the recursion-tree work.

**Common misconception:** Applying only the basic polynomial-gap Master Theorem cases to a logarithmic boundary case.

## Q18

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Mutual exclusion versus progress.

Both can set their flag before either checks the other's flag, leaving both spinning forever. Progress therefore fails. Mutual exclusion still holds: a thread entering has its own flag true, preventing the other from passing its test until that flag is cleared after the critical section. B captures both facts. A overlooks the preceding writes, C overlooks the deadlocking interleaving, and D invents a turn variable.

**Common misconception:** Treating absence of simultaneous entry as a complete synchronization proof.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Microprogrammed versus hardwired control.

Stored control-word sequences characterize microprogramming, and altering them can alter sequencing, establishing A. Such a design still needs sequencing logic, refuting B. C incorrectly assigns microinstruction fetching to the hardwired design. The ISA need not expose internal control formats, refuting D.

**Common misconception:** Treating an instruction-set specification as a specification of internal control implementation.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Direct-mapped conflict tracing.

B gives misses on 0 and 1, a hit on the second 0, and a miss on 4, which replaces 0 at index zero. A alternates conflicting blocks and has no hits; C visits four new blocks and has no hits; D has three hits after its first miss.

**Common misconception:** Treating blocks with the same index as the same cached block.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** TCP byte-stream reception.

A positive short read can return available data without indicating EOF. The application must use its own framing and accumulate as needed, B. A and C misinterpret a permitted short return; D invents message boundaries absent from TCP's stream interface.

**Common misconception:** Equating one send with one receive.

## Q22

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

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Acceptance requires an exhausted input as well as the stack criterion.

A stack can empty before the unread suffix has been processed. That configuration is not accepting under the stated convention, so A holds. B is false by the convention itself; C and D impose nonexistent restrictions.

**Common misconception:** Ignoring unread input when checking an acceptance configuration.

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: vocabulary in context. Restoring the previous configuration undoes the change, which is B. A is the opposite meaning; C asserts repetition, which reversibility does not require; D contradicts restoration of the previous state. Use the sentence's definition rather than an association with the prefix alone.

## Q25

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: fair search of nondeterministic computations. With finite branching each finite depth has finitely many nodes, so BFS eventually reaches any finite accepting branch (A). DFS can stay forever on an epsilon loop (C), disproving B. For a rejected input an infinite nonaccepting computation tree can keep naive BFS running forever, disproving D. CFL membership is decidable by other constructions; this does not make every naive simulation a decider.

## Q26

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: resource-allocation cycles. Deadlock requires a directed cycle, making A true and its contrapositive B true. With multiple instances a cycle need not be sufficient: another holder may release an instance and enable progress, so C fails. Acyclic waiting may include unfinished processes, disproving D. Distinguish a necessary condition from a sufficient one.

## Q27

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: preorder subtree ranges. A first lists root 40, then its valid left subtree 20,10,30, then its valid right subtree 60,50,70. B enters the right subtree at 50 and later returns to 10<40. C similarly puts 20<40 after entering the right subtree. D visits 30 in 20's right subtree then incorrectly places 10 there. Bounds from all ancestors matter.

## Q28

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: scope of survey evidence. The volunteers reported a result, but self-selection can affect representativeness; C preserves that distinction. A generalizes to every resident, B assumes away selection bias, and D asserts dishonesty without evidence. A limitation on generalization does not invalidate the observations themselves.

## Q29

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: finite-state value invariants. Starting at zero, x alternates between zero and one. B holds, while A fails for an odd number of iterations. Both values make x(x−1)=0, proving C and disproving D. The expression can be constant even when a constituent variable is not.

## Q30

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

U used an uncommitted value that disappears when T aborts. Cascading recovery therefore rolls back U's dependent execution, even if U wrote nothing. A is correct. B invents a conflict: read–read pairs are not conflicts. C and D assert unjustified universal abort rules. Read-only does not mean immune to dirty data.

## Q31

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If both read0 before either writes, both write1, giving A. If one increment completes before the other's read, the result is2, giving B. Shared memory supplies visibility/storage, not atomic compound operations, so C is false. Each computed write is based on0 or1, and only two increments occur, so3 cannot arise; D is false. Lost updates are possible without mutual exclusion or atomic increment.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Overall rates are weighted departmental averages. For example, rates90%,50% with shares90%,10% give86%; later rates91%,51% with shares10%,90% give55%. Both rates rise but the overall rate falls, proving B possible and A false. C and D introduce changes not needed by the example. Comparing weighted averages requires checking the weights.

## Q33

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The byte offset of B[i,j] is4(5j+i). Its i-stride is4 and j-stride20, proving A and B. A row-major traversal of B advances j first, so consecutive elements generally lie20 bytes apart; C is false. The defined index mapping gives B[2,1]=A[1,2] as aliases, proving D. A transpose view changes strides and index interpretation without rearranging the underlying storage.

## Q34

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A valid BST satisfies the local comparisons, so A is true. The stated tree passes those checks but puts12 in10's left subtree, violating the ancestor constraint; C is true and B false. Carrying the upper bound10 into the whole left subtree detects12, proving D. Parent-only checks omit inherited constraints.

## Q35

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A selects at least one true input but excludes both true, while B explicitly selects the two unequal-input cases. Both are XOR. C also accepts11; D complements XOR and accepts equal inputs. A truth table verifies all four cases.

## Q36

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Every equal-block string belongs to a*b*, but L is the standard nonregular equal-count language while R is regular. Thus A,C are true. This example disproves B; L is infinite, disproving D. Regular supersets may contain nonregular subsets.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If p were true, the implication would force q true, contradicting exactly one true proposition. Thus A holds. The sole true proposition must be q or r, giving B and D. Either can be the true one, so C is not forced.

## Q38

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Substitution gives3,7,13, establishing A; at4 the rule gives16+4+1=21, proving D. The extra product vanishes at1,2,3 but not at4, so C is true and B false. Finite observations can support a pattern without uniquely determining its continuation.

## Q39

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For outer value i=n/2^r, r=0..k, the inner loop executes r+1 times. The total is1+2+...+(k+1)=(k+1)(k+2)/2, or Θ(k²)=Θ((log n)²). Thus C is correct. A misses the growing inner count, while B,D overestimate it by treating geometric index values as linearly many iterations.

## Q40

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The duplicated and inherited descriptors refer to the same open file description under the stated semantics. Its offset is shared, so A,C are true and B false. Closing one descriptor drops one reference; other open references remain valid, refuting D. Descriptor-table entries and open file descriptions are distinct levels of state.

## Q41

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

One word says nothing about a uniform bound and all sufficiently long words, proving B and refuting A. The pumping condition is necessary but not sufficient for regularity, proving C. To refute regularity with the lemma one must defeat every allowed decomposition of an appropriately chosen word, not merely one, refuting D.

## Q42

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The identifier is the pair, permitting the same room number under different owners, proving A and refuting B. BuildingID contributes to identification, proving C. Replacing it with another owner's identifier can duplicate an existing pair, proving D. A partial key is not a global key.

## Q43

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Each append grows capacity n→2n and copies n elements. Removing the appended element leaves size n, exactly half the capacity, so it shrinks back and copies n retained elements. The same starting state recurs, costing2n copies per pair and Θ(kn) overall, C. A,B assume amortized growth without accounting for repeated shrink/grow oscillation; D ignores both data size and repetition count.

## Q44

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Base strings a,b are odd palindromes, and recursive productions add the same symbol at both ends, preserving that property, proving A. No production removes the central base symbol, refuting B. A palindrome equals its reversal, proving C. Both a and b are generated but their concatenation ab is not, refuting D. Recursive symmetry does not imply closure under concatenation.

## Q45

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

F selects y when x=1 and z when x=0. Therefore the two cofactors agree exactly when y=z, proving A. Expanding B's product gives xy+(NOT x)z+yz; the consensus term yz is redundant, so B holds. C fails with x=0,y=1, where F=z. When y=NOT z, F equals z for x=0 and NOT z for x=1, hence F XOR z=x: D. Treating the selector as an ordinary OR input obscures these dependencies.

## Q46

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A usable cached or otherwise known address can avoid a fresh lookup, A. The redirected hostname may need its own DNS resolution, C. Distinct hostnames need not resolve to the same address, so B is false. A response cannot change a request already transmitted; following a redirect involves another request, so D is false.

## Q47

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Conditional next-address logic can select using a status flag(A), while a microinstruction can drive multiple nonconflicting controls in one cycle(C). Control stores can be read-only, so B is false. Different instructions or conditional paths may traverse different numbers of microinstructions, so D is false. Microprogramming specifies control sequencing; it does not impose equal instruction latency or writable storage.

## Q48

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After buffered data is drained, orderly end-of-stream is reported by a zero return on a positive-length receive(A). TCP supports independent directional shutdown, so continued sending can remain valid(C). Zero here is a count, not a delivered data byte(B), and TCP supplies a byte stream without a separate application shutdown record(D).

## Q49

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Division requires every B value in S for a selected A. Initially only 1 has both x and y, while P={1,2}, proving A and refuting B. Adding (2,y) makes both A values qualify, proving C. If S becomes {x}, both already have x, so D is false. Division expresses a universal matching condition.

## Q50

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At endpoint 0 choose [0,6], which extends farther than [0,4]. At endpoint 6, [6,9] extends farther than [3,8]. At endpoint 9 choose [8,10], reaching the target; B is the stated sequence. A starts with a nongreedy choice even though it also covers the target. C leaves (6,7) uncovered, and D leaves (4,7) uncovered. A later interval cannot repair an earlier uncovered gap under this covering rule.

