# Worked Solutions — Additional Practice Set 010

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Negating the outer quantifiers changes forall x exists y into exists x forall y.
2. Negating the conjunction gives NOT R(x,y) OR NOT forall z (R(x,z) -> z=y).
3. The inner negation is exists z [R(x,z) AND z!=y]. Substitution gives A. The original formula says each x has exactly one R-successor; its negation allows an x with none or more than one.
- Original option A: It follows all three quantifier and connective changes.
- Original option B: For a two-element identity relation the original is true, but this option is also true by choosing x!=y.
- Original option C: For a singleton empty relation the original is false, but this conjunction is false.
- Original option D: For a universal relation on two elements the original is false; this option is false because z=y defeats its universal conjunct.

## Q2

**Correct answer:** C, D

The underlying question is correctly answered by A, B. This variant asks for its invalid answers, so select the complementary set: C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A substring containing an a and a c must include all p b's between them, plus at least one a and one c, requiring length at least p+2. This contradicts |vxy|≤p, proving A. Consequently deletion of v and y changes the counts of at most two symbol types. At least one symbol is deleted since |vy|>0, while at least one type retains count p. Thus all three counts cannot remain equal; deletions preserve block order, and i=0 is outside L for every legal decomposition. This proves B. To contradict the pumping lemma, every permitted decomposition must fail for some pumping index; choosing only a convenient one, or assuming where its pieces lie, is invalid.
- Original option A: True: spanning an a and a c needs at least p+2 symbols.
- Original option B: True: at least one count decreases and at least one remains p.
- Original option C: False: the lemma asserts existence of a successful decomposition, so every legal choice must be ruled out.
- Original option D: False: v and y may lie in other blocks or cross a boundary; the proof must cover those choices.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Organization and Architecture — Interrupts and DMA

DMA reads main memory rather than the processor's dirty cache copies. Writing back the buffer lines and waiting makes main memory contain the updates before DMA reads them. Discarding dirty lines loses modifications. Interrupt control changes notification, not visibility of cached data, and a completion event cannot precede starting the transfer.

- **A:** False: discarding dirty lines without write-back loses the updated data.
- **B:** True: completed write-back makes the DMA source in main memory current.
- **C:** False: interrupt masking does not update memory.
- **D:** False: this ordering cannot start the required transfer and does not flush the cache.

**Common misconception:** DMA bypassing the CPU does not automatically observe its dirty cache contents.

## Q4

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Organization and Architecture — Signed overflow and unsigned comparison

1. N=0 with V=1 means the mathematical signed subtraction was less than −128, wrapping into a nonnegative result. Positive overflow would instead produce N=1.
2. Therefore A represents a negative signed number and B a nonnegative signed number. Write the unsigned value of A as 128+r, where 0≤r≤127, and the value of B as b, where 0≤b≤127. Their signed difference is r−128−b.
3. Overflow requires r−128−b<−128, hence b>r. Every such pair automatically has unsigned A>B, so C=1.
4. For r=0 there are 127 choices of b, for r=1 there are 126, and so on down to zero. The count is 127+126+⋯+1=127×128/2=8128.

- **A:** Incorrect: 8192 treats the boundary as exactly half of all opposite-sign pairs without excluding the equality diagonal.
- **B:** Correct: the strict triangular inequality gives 8128.
- **C:** Incorrect: 8256 includes b=r, whose signed result is exactly −128 and does not overflow.
- **D:** Incorrect: 16384 counts all opposite-sign pairs, including those with no overflow.

**Common misconception:** Unsigned carry and signed overflow describe different properties; endpoint pairs must be checked against the signed representable range.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Necessary conditions and separate permissions.

No renewal implies stopping Monday. Because the policy is obeyed and the pilot continues Tuesday, renewal occurred before Monday. Expansion has the additional review requirement, whose satisfaction is not stated. B follows. A and C infer expansion permission without evidence; D treats review as a substitute despite the word “also.”

**Common misconception:** Satisfying a necessary condition for one action does not satisfy all conditions for a different action.

## Q6

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Bayesian updating of a hidden Bernoulli source.

The likelihoods of exactly two successes are 3(1/4)²(3/4)=9/64 and 3(1/2)³=24/64. Multiplying by priors gives relative weights 9 and 48, so posterior probabilities are 3/19 and 16/19. The predictive success probability is (3/19)(1/4)+(16/19)(1/2)=35/76. A ignores the posterior mixture; C is the posterior probability of source I rather than a trial success; D is not the posterior-weighted value.

**Common misconception:** Trials are independent conditional on the hidden source, not necessarily unconditionally.

## Q7

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Pumping-lemma quantifiers and a forced pumping region.

The bound |xy|≤p confines nonempty y to the first zero block, proving A. Pumping up adds zeros only before the single 1, so the two sides no longer match: B is false. Pumping down removes at least one zero from only that side, proving C. A nonregularity proof must defeat every permitted decomposition for its chosen witness; D is false.

**Common misconception:** The adversary chooses the decomposition; a proof must control all of its permitted choices.

## Q8

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Saturation versus modular overflow.

S saturates 7+3 to 7, then adds −5 to obtain 2. W represents 10 as signed −6, then wraps −6−5=−11 to signed 5. Thus (2,5). A delays saturation until the end; C fails to wrap the second W addition; D reports intermediate values.

**Common misconception:** Applying overflow rules after each operation differs from applying them only to the final exact result.

## Q9

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** NULL in anti-membership queries.

For x=1, NOT IN compares against both 2 and NULL, yielding UNKNOWN; x=2 yields FALSE; x=NULL yields UNKNOWN. WHERE retains none, proving A. NOT EXISTS instead asks whether an equality is TRUE for some inner row. It finds a match only for x=2, returning 1 and NULL (B). Removing the inner NULL permits x=1 through NOT IN but leaves outer x=NULL UNKNOWN, refuting C. IN returns only 2, not three rows, refuting D.

**Common misconception:** NOT IN and correlated NOT EXISTS need not agree in the presence of NULL.

## Q10

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Rounding-induced nonassociativity.

In [16,32), the spacing is 2. The exact 16+1=17 is midway between 16 and 18, and ties-to-even selects 16, so (a+b)+c=0 (A). For the other grouping, 1−16=−15 is exactly representable with four significant bits (1111₂), and 16−15=1 is exact (B). Real arithmetic gives 1 (D). The unequal computed results refute C without any overflow.

**Common misconception:** Finite-precision rounding alone breaks associativity, even with unbounded exponents.

## Q11

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Domain independence in relational calculus.

E1 is exactly the fixed tuples of R, so enlarging an external domain adds nothing to it (A). E2 contains all domain values not in R; any new domain value enters it, proving C and refuting B. E1 need not include domain values absent from R, refuting D.

**Common misconception:** Unrestricted negation can make a query depend on values not stored in the database.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** DFA state requirements.

Use two accepting states for having read even or odd length, plus a rejecting sink for a forbidden b in an even position. The parity states are distinguishable by suffix b: allowed after even length, forbidden after odd length. The sink is distinguished by ε. All three are reachable, so three are necessary and sufficient. A is too small; C,D are not minimal.

**Common misconception:** A condition on positions requires parity tracking even when both parity states can accept at input exhaustion.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Runs versus accepted strings.

An accepting run must eventually take q→r on the sole symbol a. Before doing so it may traverse the ε-cycle any finite number of times. Thus only a is accepted, but it has infinitely many finite accepting runs (B). A confuses runs with words; C never reaches final r without reading a; D incorrectly treats nondeterminism as forcing an infinite cycle.

**Common misconception:** Nondeterministic acceptance needs one finite accepting run; nonaccepting infinite alternatives do not prevent it.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Comparison decision trees.

Correct sorting must distinguish the n! strict input orders, so the tree needs at least n! leaves. A binary tree of height h has at most 2ʰ leaves, giving h≥ceil(log₂(n!)). B is correct. A undercounts orders; C asserts an incorrect universal quadratic cost; D assumes a comparison settles a full key position.

**Common misconception:** A comparison supplies one binary outcome, not a key's complete rank.

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** B-tree occupancy bounds.

There are four levels. At minimum occupancy, each internal node has two children and each node has one key: 1+2+4+8=15 keys. At maximum occupancy, each internal node has four children and every node has three keys: 3(1+4+16+64)=255. A uses one fewer level; C confuses leaves with all keys; D counts maximum nodes, not maximum keys.

**Common misconception:** Mixing height measured in edges with height measured in levels.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Longest-path dynamic programming in a DAG.

Initialize the source distance to zero and unreachable distances to negative infinity; process reachable edges in topological order. Every predecessor distance is final before a vertex is processed, so maximizing over incoming paths is correct regardless of negative weights. This proves B and refutes A. Path lengths in edges may differ (C false), and converting to an undirected graph destroys the acyclic dependency structure (D false).

**Common misconception:** Transferring restrictions of greedy shortest-path algorithms to topological dynamic programming.

## Q17

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Earliest-finish activity selection.

Choose B, then C, then D to obtain three activities. Choosing A first allows E afterwards but no third activity, proving B. A's claimed count is false. C is false because earliest-finish already achieves three. The compatible sets {A,E} and {B,C,D} are both maximal but have different sizes, refuting D.

**Common misconception:** Equating maximality with maximum cardinality.

## Q18

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Unique-light-edge cut property.

If an MST omitted e, adding e creates a cycle containing another crossing edge. That crossing edge is heavier because e is uniquely minimum; replacing it gives a lighter spanning tree, contradiction. Thus A and C hold. An MST may cross the cut through several edges, refuting B. A triangle with distinct edge weights supplies a cut-minimum edge that is not a bridge, refuting D.

**Common misconception:** Assuming an MST must cross every cut exactly once.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Gray-code adjacency in Karnaugh maps.

The order makes each adjacent pair differ in one variable, including 10 next to 00 at wraparound. Such pairs can combine while eliminating one literal. A holds. B wrongly universalizes a display convention; C confuses reordering with changing function values; D states the opposite adjacency condition.

**Common misconception:** Ignoring edge wraparound when reasoning about adjacent map cells.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Contextual vocabulary.

A conclusion open to revision is tentative, B. Irrevocable means it cannot be reversed; unrelated concerns relevance; unanimous concerns agreement among people. None of A,C,D expresses the stated revisability.

**Common misconception:** Selecting a word associated with authority rather than with uncertainty.

## Q21

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Bounded simulation.

The allowed simulation horizon is computable and finite for every input. Test acceptance initially and after each permitted step, stopping no later than |x| steps; this decides membership, proving A and C. It requires no unbounded halting decision, so B is false. Behaviour on another input cannot invalidate acceptance within this input's finite bound, refuting D.

**Common misconception:** Treating every question about a Turing machine's behaviour as an undecidable halting question.

## Q22

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Algebraic identities under explicit exact semantics.

Zero is the additive identity, one the multiplicative identity, and subtracting a value from itself yields zero. These establish A,B,D. C fails for any nonzero x because x×0 equals zero, not x.

**Common misconception:** Confusing a multiplicative annihilator with an identity.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Longest valid token prefix.

The longest valid initial token is >=, leaving >, so A follows. B invents an undeclared => token, C invents an undeclared full token, and D discards a valid trailing token.

**Common misconception:** Treating longest match as permission to create tokens absent from the lexical specification.

## Q24

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Finite binary expansions.

A reduced rational has a finite binary expansion exactly when its denominator is a power of two. 3/8=0.011₂ and 7/4=1.11₂ fit the stated precision, giving A,C. The reduced denominators of 1/10 and 1/3 contain odd factors, so B,D require infinitely repeating expansions.

**Common misconception:** Assuming every short decimal fraction is exact in finite binary precision.

## Q25

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: zero-weight cycles and walks. Every s-to-t walk must pay 1 entering a and 2 leaving b for t. Repeating a→b→a adds zero; hence infinitely many walks attain weight 3 (C). A would require an exploitable negative cycle; B ignores zero-cost repetitions; D overlooks s→a→b→t. Paths and walks have different counting behavior.

## Q26

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: negating the pumping condition. The regular-language statement has order ∃p ∀w ∃split ∀i with membership preserved. Negation gives ∀p ∃w ∀split ∃i with membership failing, exactly D. A only exhibits one bad split; B chooses the split and even requires failure at i=1, which reproduces w; C uses the wrong initial quantifier and still allows a bad chosen split. The adversary chooses the decomposition.

## Q27

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: periodic transformations. The orbit is (1,0)→(1,1)→(0,1)→(0,0)→(1,0). Since 2027 leaves remainder three on division by four, the answer is (0,0), C. A, B and D correspond to remainders one, two and zero. The translation term is part of each application.

## Q28

**Correct answer:** B

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: determinant and augmented consistency. Expansion gives det A=1+a³, B, nonzero for real a≠−1, disproving A. At −1 the rows sum to zero but the first two are independent, so rank is two, D. The right-hand sides sum to three, contradicting that row dependency; the displayed system is inconsistent, not infinitely soluble, so C is false. A singular matrix alone does not determine the number of solutions.

## Q29

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: aggregation with longest-prefix exceptions. The two /25s exactly partition the /24 and share H. Keeping the more-specific /26 retains J for its destinations, so A. No address outside the /24 gains a matching nondefault route, so C. Longest-prefix matching selects by prefix length, not insertion time, disproving B. Removing the /26 would send its destinations to H instead of J, disproving D.

## Q30

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The right leaf becomes[30], which satisfies the stated minimum occupancy. Its minimum changes to30, so the separator must change to30. B is correct. A assumes an unstated occupancy bound; C violates the explicit separator convention; D discards valid keys. Separator repair and underflow repair are distinct operations.

## Q31

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

p initially points to B. The second assignment connects A to C. The third connects B to A, and the final assignment moves head to B. The reachable list is B→A→C. Thus B is correct; A and C place the links in different orders, while D ignores the rewiring. Trace node identities separately from pointer-variable names.

## Q32

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Every string has finitely many predecessors in length-lexicographic order, and D halts on each. Therefore every member is eventually reached and printed, proving A. The enumerator continues testing strings even when L is empty or finite, so B is false and C true. Individual termination suffices for progress; no known uniform runtime bound is needed, disproving D. Enumeration need not announce when the final member has been printed.

## Q33

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

On abab, the stack empties twice without underflow, so the machine accepts despite the forbidden alternation: A is true and C false. A separate post-b phase can reject any subsequent a, proving B. aabb pushes twice then pops twice and is accepted, disproving D. Stack balance alone does not enforce block order.

## Q34

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A thread holding Y must already have acquired X, so two threads cannot split the locks in opposite acquisition orders. The common order excludes circular wait, proving B and disproving A. It gives neither equal waits nor absence of waiting, so C,D are false. Deadlock prevention is weaker than immediate access or fairness.

## Q35

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The two zeros compare equal but have distinct signs; reciprocal division can yield positive versus negative infinity, proving A,B and disproving C. Infinity is outside the finite representable values, so D is false. Numeric equality need not imply bitwise equality.

## Q36

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The sole common lower bound maximal under the order is0, and the least common upper bound is1, so A is true. Every pair has a meet and join, making C true. Incomparability of a,b disproves B, and1 disproves D. A lattice need not be a total order.

## Q37

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The given explanation establishes a shared measurement basis, making A correct. It explicitly rejects B. It says nothing about deception, so C is unsupported, and explicitly uses currency/time units, disproving D. Comparability does not require equality.

## Q38

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A positive TTL permits reuse of a cached answer until its expiry under this model, so A is true. TTL is a lifetime field, not a push channel; B is false. Changing the authoritative TTL does not edit already stored expiry times, proving C. The authoritative value can change during a cached record's lifetime, so D is false. Caching freshness is bounded by reuse policy, not guaranteed by preventing updates.

## Q39

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A establishes descending score order first; the later stable department sort groups departments while retaining that score order and original tie order within each. C directly uses the desired composite key and stability, so both work. B makes score the primary final key and can intermix departments. D reverses the original order of equal-key records, which later stable sorts retain rather than restore. Stable multi-pass sorting processes the least significant key first.

## Q40

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If an A value occurs in R but not in S, any corresponding R tuple survives R−S, proving B. A fails for R={(1,x)}, S={(1,y)} with x≠y: the left side is{1}, the right empty. Every tuple in R∩S supplies an A value present in both projections, proving C. The same counterexample has empty intersection but common projected value1, refuting D. Projection can erase the distinctions on which intersection and difference depend.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Rank is2 with three variables, so nullity is1: A true, D false. A consistent system's solutions are one particular solution plus that one-dimensional nullspace, an affine line, proving C and refuting B. Consistency does not imply uniqueness.

## Q42

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A full link-state database supports independent shortest-path computation from each router, proving A. The source differs, so the resulting trees and next hops can differ, proving C and refuting D. B describes distance-vector-style information rather than the stated topology database. Shared input topology is not a shared source vertex.

## Q43

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The reversed result is(2,C),(1,B),(1,A). Its key order is descending, but the tied records A,B have reversed relative order, so A. B,D mistakenly assume stability survives whole-array reversal. C describes the correct descending key order, not the defect.

## Q44

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At depth d there are2^d calls, each initializing2^d cells, so total initializations sum4^d from d=0 to k, which is Θ(4^k)=Θ(n²). Sequential depth-first processing keeps only one root-to-leaf chain of buffers live at once; its sizes sum1+2+...+2^k=2n−1, giving Θ(n). A follows. B,D undercount total work, and C counts allocations from nonoverlapping sibling calls as simultaneously live.

## Q45

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A does not modify either operand. B,D store the operand's existing value, so the sum is unchanged despite aliasing. C is insufficient: with a=0,b=5,p=&b, the old sum is 5 and the new sum is 0. Aliasing alone neither establishes nor rules out redundancy; the stored value also matters.

## Q46

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The nullable declaration permits A. A non-NULL foreign-key value must match its referenced key when checked, giving D. Neither self-reference nor cyclic reference violates these key constraints, so B,C are false. A foreign key enforces existence, not a tree structure.

## Q47

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If a tree contains e, deleting it partitions the tree into two components. The alternative u-v path must cross this cut on some edge f whose weight is at most7. Inserting f restores a spanning tree and reduces weight by at least1, proving C and excluding e from any MST(A). The alternative path preserves connectivity between e's endpoints, so e is not a bridge and B is false. Its path edges may themselves have alternatives, so D need not hold. The exchange uses a crossing path edge, not an arbitrary edge chosen without checking the cut.

## Q48

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The device continues asserting the interrupt level while its status remains1, permitting redelivery(A). Acknowledging the controller does not inherently acknowledge or clear the device's own condition, so B is false. Neither transfer rollback(C) nor a change in electrical trigger semantics(D) follows. The handler must address the source condition as required by the device interface.

## Q49

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The old sum is 5×12=60; the new mean is (60+100)/6=80/3. The old median fixes the third ordered observation but not the fourth, and appending 100 does not fix a unique new median. For example [0,0,10,20,30] and [5,5,10,15,25] meet the premises but give different new medians, ranges and variances. Therefore A,C,D are not determined; B is.

## Q50

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

With b=c=0 the expression is a AND NOT a, always 0, proving A. During a transition, the direct and inverted paths can temporarily make both OR outputs 1, proving B. By the consensus theorem, (a+b)(NOT a+c) already implies (b+c), so adding that factor preserves the truth table. When b=c=0 the added factor remains 0 and blocks the glitch, proving C and refuting D. A redundant Boolean factor can be physically useful for hazard suppression.

