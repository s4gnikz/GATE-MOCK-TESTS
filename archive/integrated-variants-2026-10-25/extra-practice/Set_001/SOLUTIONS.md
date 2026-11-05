# Worked Solutions — Additional Practice Set 001

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. The relative clause “that were damaged” modifies the plural noun instruments.
2. The main clause has the singular subject Each, so its verb is has.
The complete sentence therefore uses were; has.
- Original option A: Both agreements are correct.
- Original option B: Both verbs have the wrong number.
- Original option C: The main verb must agree with Each, not instruments.
- Original option D: The relative-clause verb must agree with instruments.

## Q2

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A deterministic pushdown automaton can push a stack symbol on a and pop one on b, rejecting underflow. Its finite control also remembers the preceding symbol and whether its current run has length one or two; it rejects a third repetition. It accepts at end of input exactly when the stack is empty. Thus L is deterministic context-free.

To show nonregularity, consider the prefixes u_n=(aab)^n for n≥0. For distinct m,n, append v_n=(abb)^n. The string u_n v_n has no triple repetition, never underflows, and has net stack change n−n=0, so it lies in L. But u_m v_n has net stack change m−n≠0, so it cannot lie in L. Hence infinitely many prefixes are pairwise distinguishable by suffixes, and no finite automaton recognizes L. In particular, banning long runs does not bound stack depth: repeated aab blocks keep increasing it.
- Original option A: False: (aab)^n raises the stack height without creating aaa or bbb; suffixes distinguish infinitely many such prefixes.
- Original option B: True: finite control checks the run restriction while the deterministic stack checks balanced legal operations; the suffix argument proves nonregularity.
- Original option C: False: the explicit deterministic push/pop construction handles both restrictions without guessing.
- Original option D: False: a pushdown stack together with finite control can impose both restrictions simultaneously.

## Q3

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Intersections remain in L, so they are meets. All unions are in L except {a} union {b}; for that pair the least available upper bound is {a,b,c}. Hence L is a lattice, but joins need not equal unions.
2. Distributivity fails: {c} meet ({a} join {b})={c}, whereas ({c} meet {a}) join ({c} meet {b})=empty set.
3. Bottom and top complement one another. {a} has complements {b} and {b,c}; {b} has complements {a} and {a,c}; {a,c} and {b,c} are consequently complemented too. The remaining element {c} has no complement: the only nonempty elements disjoint from it are {a} and {b}, and their individual joins with {c} are below top. Thus six elements have complements.
4. Among the three atoms, {c} uniquely has two immediate upper covers; {a} and {b} each have one. Any automorphism must fix {c} and may only fix or swap {a},{b}. The two choices determine all other images, and both are valid. Thus there are exactly two automorphisms.
- Original option A: The explicit distributive-law calculation yields {c} on one side and empty set on the other.
- Original option B: Only {c} lacks any complement.
- Original option C: An automorphism fixes {c}; its only freedom is the swap of a and b.
- Original option D: Because {a,b} is absent, the only common upper bound for the two atoms is top.

## Q4

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Engineering Mathematics — Monoids and groups

1. The inverses are f-inverse(x)=3x mod 5 and g-inverse(x)=x-1 mod 5.
2. Apply the maps right to left: x becomes x-1, then 3x-3, then 3x-2, then 6x-4, which is x+1 modulo 5.
3. Thus h is a translation by 1; its k-fold application is x+k, equal to x for every residue exactly when k is a multiple of 5.

- **A:** h is not identity; it maps 0 to 1.
- **B:** Two applications map 0 to 2.
- **C:** The order of f alone is 4, but h is a different permutation.
- **D:** Five is the least positive translation count returning every residue.

**Common misconception:** Composition order matters when the permutations do not commute.

## Q5

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Operating Systems — File systems

Each indirect block holds 1024/4=256 pointers. The direct range is 0-3 and the single-indirect range is 4-259. The remaining logical blocks 260-262 require a double-indirect root and one lower-level indirect block. Together with the single-indirect block, this gives three allocated indirect blocks.

A is true by the count above. B is true: read the double-indirect root, its selected lower-level block, and the data block. C is false: 259 is the last single-indirect data block. D is true because 263*1024=269312 bytes.

- **A:** True: 1 single-indirect block + 1 double-indirect root + 1 double-indirect second-level block = 3 metadata blocks.
- **B:** True: reading block 260 uncached requires reading double-indirect root, double-indirect child, and data block (3 disk reads).
- **C:** False: block index 259 is single-indirect, not double-indirect.
- **D:** True: file size is 263 * 1024 = 269,312 bytes.

**Common misconception:** Metadata-block allocation depends on the populated part of the pointer tree, not its maximum possible capacity.

## Q6

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** TCP byte-stream delivery.

TCP preserves byte order, but not send-call boundaries. Buffering and arrival timing permit a single five-byte return or a one-byte return followed by four, proving A and B. With a blocking socket and no closure, lack of data causes waiting, not a zero return; C is false. Ordered delivery excludes D.

**Common misconception:** TCP provides a byte stream, not an application-message boundary for every send call.

## Q7

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Right quotient of a language.

Appending k zeros changes counts from (n0,n1) to (n0+k,n1). Equality requires k=n1−n0, which exists as a nonnegative integer exactly when n0≤n1. B is correct. A excludes strings fixable by appending zeros; C reverses the inequality; D wrongly includes w=0, which cannot be balanced by more zeros.

**Common misconception:** The suffix alphabet restricts which count imbalances can be repaired.

## Q8

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reachability of negative cycles.

The only path to b is s→a→b, of length five. Neither c nor d is reachable, so their negative cycle cannot affect paths from s. A,C hold; B,D incorrectly apply an unreachable cycle to reachable distances.

**Common misconception:** A negative cycle matters to a source-to-target distance only when it can participate in a source-to-target walk.

## Q9

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Modifier attachment and grammatical parallelism.

The person examining the records must be the subject immediately following the introductory phrase. In C that subject is Mira, and the three coordinated verbs are corrected, recalculated, and reorganized. A and B attach the introductory phrase to errors and totals, respectively, and mix incompatible list forms. D has no coherent parallel structure and also makes totals the subject of examining. Only C meets both conditions.

**Common misconception:** A sentence can contain individually grammatical phrases while linking them incorrectly.

## Q10

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** A nilpotent chain and a finite matrix inverse series.

Choose v with A²v≠0. The vectors v,Av,A²v are linearly independent: applying A² to a supposed relation first makes the v coefficient zero; applying A then makes the Av coefficient zero; the last coefficient follows. They form a basis. A maps that basis to Av,A²v,0, so rank(A)=2 and rank(A²)=1 (A,B). Every eigenvalue λ obeys λ³=0, hence C is false. Multiplication gives (I−A)(I+A+A²)=I−A³=I, proving D.

**Common misconception:** A zero eigenvalue for every eigenvector does not mean the matrix itself is zero.

## Q11

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Redundant dependencies in a minimal cover.

A→C follows transitively from A→B and B→C, so it can be removed. Neither remaining dependency follows from the other, and their single-attribute left sides have no extraneous attributes. A is a minimal cover. B cannot derive A→B; C cannot derive B→C; D lacks a singleton right-hand side and cannot derive B→C either.

**Common misconception:** Preserving A's closure alone does not preserve dependencies with other determinants.

## Q12

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Object lifetime after function return.

A's automatic scalar and D's automatic array cease to exist when their functions return; their pointers do not permit later access to live objects. B's static object persists throughout program execution. C's allocated object persists until freed, which the question excludes before the first access. Thus B,C are valid and A,D are not.

**Common misconception:** Returning an address does not extend the lifetime of the object at that address.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** A recurrence with dominant nonrecursive work.

Let f(n)=n²/log₂n. Relative to f(n), the next recursion level contributes 3f(n/2)/f(n)=(3/4)log₂n/(log₂n−1), which is bounded below one for all sufficiently large n. The levels therefore sum geometrically to Θ(f(n)); the finite last levels and leaf cost n^(log₂3) are lower order. B follows. A drops the denominator; C treats the leaves as dominant; D applies a boundary-case logarithmic accumulation that does not occur.

**Common misconception:** A logarithmic divisor does not automatically put a recurrence into the critical Master-theorem case.

## Q14

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Regular-language closure.

Reverse a finite automaton's edges and exchange start/final roles using nondeterminism for reversal (A). Complement a complete DFA's accepting set for B. Concatenation can be implemented by an ε-NFA connecting copies, proving D. C fails with L=Σ* and a nonregular CFL: their intersection is that nonregular CFL.

**Common misconception:** Intersection with a language from a larger class need not remain regular.

## Q15

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** State encoding and unused-state behaviour.

Two bits encode at most four states, so at least three are needed (A). Three bits provide eight patterns, leaving three outside the five-state cycle (C). Five one-hot bits are one possible encoding, not a necessity (B false). Recovery from unused states depends on the chosen transition logic and is not automatic (D false).

**Common misconception:** Designing the intended cycle does not by itself specify safe behaviour from every other encoding.

## Q16

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Backward liveness across branching control flow.

On the B2 path, y is read before any redefinition, so A holds. On B3, a,b,c are read; thus D holds and B is false. The old x is read on neither path: B2 never uses it, and B3 overwrites it before use. Hence C holds. Including the pending branch test, the full live set is {a,b,c,y,p}.

**Common misconception:** Treating a value used earlier in the block as necessarily live after its last use.

## Q17

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** FIRST and FOLLOW in LL(1) parsing.

At S the alternatives begin with distinct a and b. At A and B, c selects the nonempty production and the end marker in FOLLOW selects ε. No table cell has two entries, proving B. A ignores separate nonterminals and lookaheads; C ignores the leading symbols; D claims nonexistent left recursion.

**Common misconception:** Declaring a conflict merely because terminal symbols occur in different productions.

## Q18

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

## Q19

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Equivalent NPDA acceptance conventions through conversion.

Final-state acceptance can be converted using a new protected bottom symbol and an epsilon cleanup phase after an old final state. Empty-stack acceptance can be converted using a bottom marker and a new final state reached on detecting the emptied original stack. With full input consumption required, these constructions preserve languages, establishing A,C,D. An unchanged machine can have a final state with nonempty stack, or empty its stack in a nonfinal state, so B is false.

**Common misconception:** Confusing equivalence of language families with equivalence of conventions on an unchanged machine.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Precision limits of an abstract domain.

At the merge, x can be 2 or 3 and is not a known constant, so A is false. A constant-only evaluator may treat both operands as unknown and fail to retain their equality, whereas algebra proves x−x=0. B captures that distinction. Each execution uses the same x twice, so C is impossible; unknown p does not invalidate the identity, refuting D.

**Common misconception:** Treating separate occurrences of the same variable as independently chosen values.

## Q21

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Closure under finite changes.

Finite F is regular. Union and difference of regular languages are regular, establishing A and B. F−L is finite, establishing C directly. D fails by taking L empty and a nonregular superset, such as {aⁿbⁿ}.

**Common misconception:** Assuming an arbitrary superset inherits a subset's language class.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Distinguishing brevity from superficiality.

The sentence explicitly says that required issues remain covered despite removal of repetition, supporting A. B and D contradict this distinction. C claims a necessary length relation not stated or implied.

**Common misconception:** Treating concise and cursory as synonyms in this context.

## Q23

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Regular-expression identities and counterexamples.

A holds because concatenating arbitrary strings of a symbols gives another string of a symbols, and every such string is already in a*. C is the identity property of ε for concatenation. B fails on ba, which is in the left language but not a*b*. D fails on a, which belongs to a*b* but not (ab)*.

**Common misconception:** Moving a star through union or concatenation as though it were an ordinary arithmetic operation.

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Dead results versus observable evaluation.

The unused store can be removed, but the device effect of the call must remain, B. A,C remove it; D duplicates it. Dead-variable reasoning does not license eliminating side effects.

**Common misconception:** Treating a dead destination as proof that the whole right-hand expression is dispensable.

## Q25

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: transport demultiplexing. Ports identify application endpoints on a host, in combination with transport/address context (A). B concerns link framing; C hardware pins; D processor addressing. These are not transport-port roles. A port number by itself is not a globally unique connection identifier.

## Q26

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: inconsistent cyclic evidence and an independent constraint. If each cyclic log entry in turn is the sole false one, the possible chronological orders are R,S,P,Q; S,P,Q,R; P,Q,R,S; Q,R,S,P. The reliable R-before-P record retains only R,S,P,Q and Q,R,S,P. Both place S before P, making C necessary. A and B hold only in the second retained order, not the first. D contradicts the reliable record. One cannot discard an arbitrary log entry without checking the other three together.

## Q27

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: external connection identity and checksum coverage. With identical public IP and remote endpoint, two simultaneous translated TCP connections need distinct external source ports (A). Distinct remote endpoints can disambiguate a reused external port if the NAT's mapping and lookup support that policy (C). TCP's checksum includes a pseudo-header containing IP addresses, so B is false. Two internal hosts may share a local source port, so D is false. A port is only one component of a connection identifier.

## Q28

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: TLB address-space separation. Without tags, a matching virtual page can retrieve the previous process's frame. Flushing the relevant entries prevents this, B. A ignores different page tables; C destroys data unnecessarily; D denies the point of a cached translation, since a hit does not necessarily walk the page table. A virtual page number is meaningful within an address space.

## Q29

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: attribute dependency ordering. X is the left child, but its inherited value depends on right sibling Y's synthesized attribute, violating the usual L-attributed restriction, A. Y is independent of X, so there is no forced cycle; compute Y.v first, then X.i, making C true and B false. Attribute dependencies do not establish syntactic ambiguity, so D is false. A valid evaluation order need not be the standard left-to-right attributed order.

## Q30

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Composition of a rotation and an offset reflection.

R sends(x,y) to(-y,x). Reflection about x=1 sends(u,v) to(2-u,v), so one pair T sends(x,y) to(2+y,x). Applying the pair twice gives T²(x,y)=(x+2,y+2), and four times gives T⁴(x,y)=(x+4,y+4). The final point is(6,5), option B. A incorrectly assumes the composition has order four. C is the result of a half-turn about the origin, which is not the specified composite. D is not obtained by the specified sequence; the intermediate points are(3,2),(4,3),(5,4),(6,5).

**Misconception:** Treating a rotation followed by an offset reflection as a rotation about the origin.

## Q31

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Since |f(x)|≤x², continuity at0 follows, making A true. The difference quotient f(x)/x=x sin(1/x) tends to0, proving B and D. For nonzero x, f'(x)=2x sin(1/x)−cos(1/x), whose cosine term oscillates without a limit at0; C is false. Differentiability does not force continuity of the derivative.

## Q32

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Write L=[[1,0],[l,1]] and U=[[u,v],[0,w]]. Matching A forces u=0 and lu=1, impossible. Nonzero determinant−1 still proves invertibility, making C true and A false. Swapping rows gives[[1,1],[0,1]], already upper triangular, so L=I works and B is true. Invertibility guarantees a unique solution for every b, disproving D. Failure of unpivoted elimination is not singularity.

## Q33

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The wait-for edges T1→T2 and T2→T1 form a cycle, so A is true. Aborting either and releasing its locks breaks the cycle, proving B. Two-phase locking ensures a serializability property, not deadlock freedom, so C is false. Simultaneous commit is neither possible while blocked nor necessary for recovery, making D false.

## Q34

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A reflection reverses orientation and a rotation preserves it, proving A. Two reversals restore orientation and both maps preserve distances, proving C. Two different parallel-line reflections can give a nonzero translation, disproving B. Translation preserves area, disproving D. Orientation preservation does not mean every point is fixed.

## Q35

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The |xy|≤p condition puts nonempty y entirely in the first p zeros, proving A. Removing it preserves all p ones but reduces zeros, proving B. This works for every possible allowed length of y, so C is false. The contradiction establishes nonregularity, proving D. The string is chosen before the decomposition but handles all legal decompositions.

## Q36

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An earliest-finishing interval ends no later than the first chosen interval in an optimum, leaving at least as much remaining scheduling time, proving A. Half-open endpoints allow back-to-back compatibility, proving C. Weighted objectives can prefer a later-finishing higher-value interval, so B is false. A long interval can block many short intervals, disproving D. The exchange proof relies on the equal-value cardinality objective.

## Q37

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If a spanning tree contained e, deleting e splits it into two components; the cycle contains another crossing edge with smaller weight, enabling a cheaper replacement. Hence no MST contains e, proving B and disproving A. The rest of the cycle provides a path around e, so C is true. When weights tie, replacing e need not reduce cost and e may belong to some MST, disproving D.

## Q38

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The only child thread is T1, while the copied mutex records a lock whose owner has no surviving child thread. With no repair or possible releaser, a wait can persist indefinitely: A,C are true. B contradicts the specified fork model. D confuses a private copied mutex with shared synchronization storage; changing the parent's copy does not unlock the child's. The conclusion depends on the explicit model, not on assuming arbitrary library calls are safe after fork.

## Q39

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each aSb adds one of each symbol, SS concatenates strings with equal counts, and ε has equal counts; hence A. Taking each S in SS to ab generates abab, proving C and refuting B. Every generated prefix has at least as many a's as b's, preserved by both constructions, so ba is impossible and D false. Equal total counts alone do not describe the language completely.

## Q40

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The mean value theorem gives c1 in(0,1) with f'(c1)=2 and c2 in(1,2) with f'(c2)=−2. Apply it to f' on[c1,c2]: some point has f''=(−2−2)/(c2−c1)<0, proving B. A is stronger than this existence claim. To refute C,D, add t·x(x−1)(x−2) to the parabola−2x²+4x: it preserves all three function values but changes f'(1) when t≠0. To vary f''(1), add t·x(x−1)²(x−2), again preserving the values. Such perturbations can also make f'' positive elsewhere, refuting A. Pointwise values do not determine all derivatives.

## Q41

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The store may change an operand, invalidating the earlier result, so A is true and C false. Excluding both aliases preserves the operands, proving B. Recomputing after the store uses their updated values, proving D. Availability depends on intervening effects.

## Q42

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Corroboration supplies supporting evidence, while the second clause withholds proof of the explanation. A preserves both. B reverses support, C exaggerates it to universal proof, and D mistakes evidentiary support for repetition of wording. Support for an observation and support for its proposed cause are distinct.

## Q43

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first test reads a[0]=1 and increments i to1; the body adds a[1]=2. The next test reads a[1]=2 and increments i to2; the body adds a[2]=0. The next test reads a[2]=0 and increments i to3, but the body is skipped. It prints3 2, option B. A,D incorrectly sum tested elements rather than the body accesses; C misses the increment in the failed test. No out-of-bounds body access occurs for this particular array.

## Q44

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The unnormalized joint weights at(1,0),(1,1),(2,0),(2,1) are1,2,2,3, summing to8, so A. Summing the Y=1 column gives5/8, proving C. Given Y=0, X=1,2 have probabilities1/3,2/3, so the conditional mean is5/3, proving D. Independence fails since P(1,0)=1/8 differs from P(X=1)P(Y=0)=(3/8)(3/8)=9/64, refuting B.

## Q45

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each spanning tree has n−1 edges, so its new weight is three times its old weight plus 7(n−1). Strict comparisons and uniqueness are preserved: A,C. Paths can have different edge counts, so B need not hold. D ignores both scaling and the number of edges. The shortcut is to identify equal cardinality of all candidate trees.

## Q46

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

K being coordinator implies L available. Since L is unavailable, K cannot coordinate (A). Exactly one of L,M must therefore coordinate (C). Either may do so; being unavailable was not stated to prohibit coordinating, so B is not forced. If L coordinates, M need not, and N's availability is unconstrained, so D is not forced. Do not add an unstated availability requirement.

## Q47

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

(3k+1)²=3(3k²+2k)+1, proving A. A finite list alone does not prove the rule for all integers, so B is false. For n=2, n²=4 has remainder1, proving C and giving a counterexample to the converse in D. A true implication need not have a true converse.

## Q48

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The free instance of R satisfies Q's pending request. Q can then finish and release S, allowing P to finish, establishing B. A incorrectly treats a resource-type cycle as sufficient with multiple instances. C ignores the free resource and D invents an exclusivity rule across different instances. The execution has a completion sequence despite its cycle in the type-level graph.

## Q49

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After reading u, its DFA state can reach an original accepting state iff some suffix v completes uv into L. Marking precisely these reachable-to-accept states therefore recognizes Pref(L), proving B and regularity(A). For L={ab}, prefix a is not in L, disproving C. If L is empty, no suffix completes even epsilon, disproving D.

## Q50

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Before failure, routes through U and V cost 2+7=9 and 5+3=8. After V is unavailable, the only remaining candidate is 9 through U. C follows. A omits the local link; B retains the failed route; D overlooks U's valid advertisement.

