# Worked Solutions — Additional Practice Set 014

## Q1

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. The product creates every candidate A paired with every required B. Subtracting R identifies a missing required pair; its A is excluded.
2. Originally only A=2 misses y, leaving 1. With empty S there are no missing pairs, so all candidate A values remain.
3. Adding (2,y) makes both candidates qualify. Adding z to S makes both fail because neither has a z pair.
- Original option A: Only 1 is paired with every B in S.
- Original option B: Universal coverage of an empty required set is vacuously true.
- Original option C: The result becomes {(1),(2)}, not {(1)}.
- Original option D: Both candidates lack z.

## Q2

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The region is 0x8000–0xBFFF, so its upper two address bits are 10. A13:A12 enumerate the four 4 KiB subregions, and A11:A0 choose one of 4096 bytes in each chip. Hence A and B hold. Ignoring A14 enables both 0x8000–0xBFFF and 0xC000–0xFFFF; the chip and offset bits are unchanged when A14 flips, so each byte has two aliases, establishing C. In D, A0 is unused, so adjacent byte addresses have the same chip and local address. A12 also redundantly enters the chip's address and decoder, leaving parts inaccessible; one-to-one addressing fails.
- Original option A: True: the upper bits 10 identify the 16 KiB window and the next two choose its four chips.
- Original option B: True: B123−8000=3123 hexadecimal, giving bank 3 and offset 123.
- Original option C: True: toggling the ignored A14 yields another enabled address for the same storage cell.
- Original option D: False: ignoring A0 aliases every adjacent address pair.

## Q3

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Theory of Computation — Context-free grammars

The base production generates ab. To generate aabb one must add one leading a and one trailing b; choosing aS at the root and then Sb, or Sb at the root and then aS, gives distinct trees with the same yield. The other strings require zero or only one extra production and therefore have unique trees.

- **A:** False: only the base production generates this length-two string.
- **B:** False: the sole extra a must come from one aS production.
- **C:** False: the sole extra b must come from one Sb production.
- **D:** True: the leading-a and trailing-b productions can nest in either order.

**Common misconception:** Ambiguity concerns distinct parse trees, not merely multiple derivation orders for one tree.

## Q4

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Programming and Data Structures — Binary heaps

The root must be 7. Choose the three keys for the left subtree in C(6,3)=20 ways; the others form the right subtree. Each three-node subtree must place its largest key at its root, while its other two keys may occupy its two child positions in 2 ways. Thus the total is 20*2*2=80.

A misses the two arrangements in one subtree. B does not account for selecting subtree key sets. C is correct. D overcounts arrangements that violate a subtree's root constraint.

- **A:** False: misses the ordering factor in one of the subtrees.
- **B:** False: does not account for the combinations of selecting subtree key sets.
- **C:** True: C(6,3) * 2 * 2 = 80 distinct valid max-heap configurations.
- **D:** False: overcounts arrangements that violate max-heap subtree root properties.

**Common misconception:** A heap fixes ancestor-descendant inequalities but does not sort the entire array.

## Q5

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Continuity and matching one-sided derivatives.

Near zero, eˣ=1+x+x²/2+O(x³), so the left branch is 1+x/2+O(x²). Continuity requires a=1, and matching derivatives requires b=1/2. B and D fail continuity; C preserves continuity but has right derivative 1 instead of 1/2.

**Common misconception:** Matching function limits ensures continuity, not differentiability.

## Q6

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordered parse trees and language versus grammar ambiguity.

Let c_n count trees with n a-leaves. c_1=1 and c_n=Σ(c_i c_(n−i)), giving c_2=1,c_3=2,c_4=5,c_5=14. Every tree has exactly one leftmost derivation, so A,B hold. A tree also has a rightmost derivation, but that is not a new tree; C is false. The generated language is a+, a regular language, so D is true.

**Common misconception:** An ambiguous context-free grammar can generate a regular language.

## Q7

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Liveness over alternative paths.

c is read by the test. A true branch uses the current a; a false branch uses the current b. The old x is overwritten on either branch before return reads x. Therefore a,b,c are live, while old x is not. This proves A,B,D and refutes C.

**Common misconception:** Liveness uses existence of a future use on some path, not a requirement that every path uses the value.

## Q8

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Rapidly growing loop indices and dominant work.

The i values are 2,4,16,…,2^(2^(k−1))=√n; the next value equals n and is excluded. Work equals the sum of these indices. The last term gives a √n lower bound, and preceding terms decrease at least geometrically, giving an O(√n) upper bound. A counts only outer iterations; C includes the excluded n-sized iteration; D multiplies two inappropriate bounds.

**Common misconception:** The number of outer iterations is not the total cost when their bodies have sharply different sizes.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Array parameters and local pointer reassignment.

The parameter a is a pointer to x[0]; p saves that pointer. Advancing local a makes it point to x[1], without changing the caller's array or p. With n=3, a[n−2]=a[1] refers to x[2], which becomes p[0]+a[0]=4+7=11. x[0] stays 4. Only B matches; A treats pointer advancement as shifting array contents, and C,D miss the actual target.

**Common misconception:** Reassigning a pointer parameter and modifying its pointed-to object are different operations.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Necessary conditions.

“Only registered participants may enter” means permitted entry implies registration, which is B. It does not promise a seat, so A is false. A registered person might be denied a seat, making C unsupported. D contradicts the entry restriction.

**Common misconception:** A necessary eligibility condition is not a guarantee of availability.

## Q11

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Boolean substitution with dependent inputs.

Substitute s=a: F=(NOT a)a+ab=ab, proving A. With a=0, F is always zero, refuting B. NAND(a,b) followed by inversion computes ab, proving C. OR differs at (a,b)=(0,1), refuting D.

**Common misconception:** A selector tied to a data input is not an independent Boolean variable.

## Q12

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Homomorphic images.

aⁿbⁿ has 2n symbols, each mapped to 0, so its image is 0²ⁿ (A). The expression (00)* recognizes the image, proving B. The original equal-count language remains nonregular, refuting C. Neither symbol is erased; each has a one-symbol image, refuting D.

**Common misconception:** A homomorphism can merge distinctions that made the original language nonregular.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Context-dependent vocabulary.

“Qualified support” is support with reservations or conditions. B is therefore correct. A expresses its opposite; C concerns a person's credentials rather than the character of the support; D introduces a legal restriction absent from the sentence.

**Common misconception:** A word's sense depends on the phrase in which it occurs.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Bottom-up heap construction.

Processing index 3 swaps 3 with 7, producing [1,2,7,4,5,6,3]. Index 2 swaps 2 with 5, giving [1,5,7,4,2,6,3]. At index 1, swap 1 with 7 and then with 6, yielding [7,5,6,4,2,1,3]. The counts are 1+1+2=4, so B is correct. A counts only root repair, C misses one downward swap, and D overcounts the four actual exchanges.

**Common misconception:** Bottom-up construction first repairs child subtrees; the root must be traced using those updated values.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Left factoring with an empty suffix.

Extract the shared initial a, leaving suffixes b,c,ε. A produces exactly ab,ac,a. B puts the common a at the end; C permits arbitrarily long suffixes; D leaves X unreachable and produces only a.

**Common misconception:** Dropping ε when one production equals the common prefix.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Induction versus universal deduction.

The observations support a tentative pattern restricted to the observed circumstances, as B says. A generalizes across every route and bus; C makes an unsupported dry-weather claim; D treats association as proof of a unique cause. None of those stronger claims follows.

**Common misconception:** Turning repeated observations into a logically necessary universal statement.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** CFL closure with a regular constraint.

A PDA for L can be combined with a DFA for R by storing their finite control states together and retaining the PDA stack, proving A. CFLs are not closed under complement or arbitrary CFL intersection, so B and C are not guaranteed. D would include the complement of L by taking R to be the full language, so it too is not guaranteed.

**Common misconception:** Extending intersection closure with regular languages to arbitrary context-free languages.

## Q18

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Graph representation costs.

The full matrix has n² entries regardless of m, proving A. Without extra indexing, finding a row's neighbours scans n entries, so B is false for small degrees. A list traversal costs its entries plus constant access overhead, proving C. Lists contain n headers and 2m edge entries, proving D.

**Common misconception:** Assuming an adjacency matrix can skip zero entries without an additional structure.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reusing a common scalar subexpression.

Compute the shared sum once and square it: one addition and one multiplication. A does this. B gives 2ab, C also gives 2ab, and D gives a+2b; none equals (a+b)² for all operands.

**Common misconception:** Confusing algebraic expansion with a computation that preserves all terms.

## Q20

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Scope and cost of interrupt masking.

A is the specified masking effect. An interrupt arriving during a longer masked interval may wait longer, proving C. Masking on one CPU does not stop other CPUs, refuting B, and it does not change ordinary memory operations into atomic multi-CPU operations, refuting D.

**Common misconception:** Treating local interrupt exclusion as a complete multiprocessor lock.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Aggregate resizing cost.

The n appends themselves cost n. Resizing copies 1,2,4,…,n/2 elements, summing to n−1. Total cost is 2n−1, B. A counts resize events rather than copied elements; C incorrectly charges logarithmic copying for each append; D exceeds the exact count.

**Common misconception:** Multiplying the largest single append cost by the number of appends.

## Q22

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Finite execution traces versus unbounded halting.

Simulating at most k steps decides acceptance and halting within that bound, establishing A,B. Recording the finite sequence of complete configurations permits exact repetition testing, establishing D. Unbounded halting for arbitrary M,x is undecidable, so C is false.

**Common misconception:** Treating bounded and unbounded execution questions as equally undecidable.

## Q23

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

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: constant propagation. All feasible incoming paths establish x=4, so 3x−2=12−2=10. B is correct. A omits the subtraction; C is not the expression's value; D denies the justified substitution. A value known on only one incoming path would not suffice.

## Q25

**Correct answer:** C

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: closure and its limits. If Lᴿ were context-free, reversing again would make L context-free, a contradiction; A holds. Erasing every symbol maps nonempty L to {ε}, which is regular; non-context-free L is necessarily nonempty. Thus D holds and B fails. Intersecting with the empty regular language gives the empty context-free language, disproving C. Closure theorems must be applied in the correct direction.

## Q26

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: dovetailing recognizers. Exactly one of L and its complement contains w, so its recognizer eventually accepts. Interleaving steps ensures that acceptance is reached even if the other machine loops; C gives the appropriate answer. A can wait forever on M for a nonmember. B mislabels complement acceptance; D imposes an unjustified time bound. A recognizer need not halt when its answer would be negative.

## Q27

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: recoverable schedules. T2 depends on T1's uncommitted value but commits first; when T1 aborts, T2 can no longer be rolled back as an uncommitted dependent transaction. This violates recoverability, C. A reverses the required commit order; B and D deny the read dependency. Committing early does not make a dirty read safe.

## Q28

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: cumulative frequencies. The median is the thirteenth ordered observation. The first two bins contain 4+6=10 observations, and the third extends the cumulative count to 20. Hence observation 13 lies in [20,30), C. A and B finish too early; D starts after observation 20. The bin containing the mean need not be identifiable from these data.

## Q29

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: edge identities in multigraph DFS. Traversing one edge u→v and returning on the other forms the allowed length-two cycle, A. At v, only the entering edge should be ignored; the other edge to the already visited parent reveals the cycle, C. B incorrectly ignores both edges; D discards a structurally distinct edge. Parent-vertex exclusion assumes a simple graph.

## Q30

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A pushdown automaton can maintain unmatched symbols: push when the incoming symbol agrees with the stack top and pop when it differs, accepting when no unmatched symbols remain. Thus B is true. Restricting to 0*1* gives exactly0^n1^n, so C is true. If L were regular, its intersection with the regular language0*1* would be regular, contradicting the standard pumping argument for0^n1^n; A is false. The string10 is a counterexample to D. Equal counts do not impose symbol order.

## Q31

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

To pop3 first,1 and2 must already be below it. After removing3,2 blocks1, so3,1,2,4 is impossible. A is obtained by pushing1,2, popping both, then pushing3,4 and popping both. B is obtained by pushing1,2,3, popping all, then pushing/popping4. D pushes all and pops all. LIFO constrains relative accessibility, not just membership of outputs.

## Q32

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The statement explicitly allows withdrawal before inspection and forbids it afterward, exactly C. A ignores the post-inspection restriction. B invents an exception. D confuses ending a withdrawal right with cancellation. The timing qualifies the agreement's provisional nature.

## Q33

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Context-free languages are closed under intersection with a regular language, proving A. Since the complement of R is regular, C−R=C∩complement(R) is context-free, proving B. Union closure, with regular languages also context-free, proves D. C is false: taking R=Σ* would assert closure of all context-free languages under complement, which does not hold. For a concrete counterexample, the complement of{a^n b^n c^n} is context-free (union of malformed block order and unequal adjacent block-count cases), while its complement is not. Difference is asymmetric here.

## Q34

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first phase stores a prefix; the second must match its reverse, consuming one stack symbol per input symbol. A successful branch therefore divides an even-length palindrome equally. B is true. NPDA acceptance requires some successful branch, not every guess, disproving A. One stack is sufficient, disproving C. End-of-input remains mandatory, disproving D.

## Q35

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A reader must not commit before the transaction whose value it read if recoverability is required. Otherwise a later writer abort would invalidate an already committed reader. A is correct; B,C,D concern unrelated properties and do not address the commit dependency.

## Q36

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

After fewer than n−1 inspections all returning1, at least two uninspected positions remain possible locations of0, each consistent with the rotation promise. Thus n−1 inspections can be necessary, and a linear scan suffices. C is correct; A,B are too small and D exceeds the tight bound. Duplicates can remove the information needed for logarithmic rotated-array search.

## Q37

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both one-sided function limits are0, matching f(0), proving A. Difference quotients are−1 from the left and1 from the right, proving B and disproving C. This same example disproves D. An extremum need not have zero derivative when differentiability fails.

## Q38

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For non-NULL a values, UNIQUE excludes repetitions, proving A. NOT NULL on b proves C but imposes no uniqueness, so B is false. Neither constraint requires every value to occur, so D is false. Constraints restrict stored rows; they do not populate absent rows.

## Q39

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

With neither/nor joining unlike-number subjects, agreement follows the nearer subject, here the plural authors, so “are willing” is appropriate. A and D are singular. C is singular and also cannot combine as “has willing.” Read the complete predicate as well as the subject number.

## Q40

**Correct answer:** B

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first header visit has x=0; a later visit can have1,2,and higher values. A single constant0 cannot soundly describe them all, so A is false and B true. Zero or multiple iterations refute C. All reachable values are nonnegative in mathematical integer arithmetic, so a range analysis could retain x≥0, proving D. Losing a precise constant does not imply that all useful invariants are lost.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Later by-reference accesses need live storage, proving A. Lifetime-preserving allocation or another valid mechanism can supply it, proving C. A dangling pointer to reused stack storage does not suffice, refuting B. Lexical visibility is not a storage-lifetime guarantee, refuting D.

## Q42

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Let the original operands be a0,b0, so t=a0+b0. Path P makes the sum a0+1+b0=t+1, proving A. Path Q leaves it t, making the path-dependent selection in D valid. Global reuse of t in B misses the increment. Assigning a does not mutate the already computed scalar t, refuting C. Dependency of a value at computation time is not an ongoing reference link.

## Q43

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A's inherited information cannot depend on a right sibling C under the left-to-right restriction, so A violates it. B,C use information from a left sibling; D uses the parent's inherited information. Those are permitted dependency directions, subject to the rest of the definition being consistent.

## Q44

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A punch away from both folds unfolds to all four sign combinations of its nonzero coordinates. A is exactly such a reflection orbit. B violates reflection symmetry, while C,D contain only two of the four distinct images. Being away from folds prevents coincident mirrored centres.

## Q45

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The parent retains its three threads. Only the calling thread is replicated into the child, which therefore starts with one thread. B is correct; A,C,D have incorrect thread counts. A copied address space can contain synchronization objects representing the old multithreaded state, but this does not recreate the other threads.

## Q46

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A determines B, so it supplies AB and hence C; B on the left of AB→C is extraneous (A). C then determines D, making the direct A→D redundant (B). A determines all attributes and is minimal, proving D. Without C→D, the closure of C contains only C, so that dependency is not redundant and C is false. Removing an entire dependency differs from removing an extraneous attribute within another one.

## Q47

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each component is context-free: a PDA matches the first two blocks for L1 or the last two for L2. Union closure proves A. Membership in both forces all three counts equal, proving C. That intersection is the standard non-context-free three-equal-block language and therefore is not regular, disproving B. If the union were regular, intersecting it with the regular language a+ b+ (no c) would be regular. That intersection is {a^n b^n:n≥1}, which is nonregular, so D is false. The regular restriction excludes L2's c-free strings with positive b-count.

## Q48

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Greedy chooses6,1,1, using three coins. The optimal choice4,4 uses two; a one-coin solution is unavailable. Greedy exceeds optimum by one(B). A assumes greedy is always optimal, C overstates the difference, and D reports greedy's count rather than the excess. Arbitrary denomination systems need not support greedy optimality.

## Q49

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A spanning tree must connect v, and e is its sole possible connection. Thus every spanning tree, including every minimum one, contains e. C is false because a mandatory bridge can have any weight. Removing e isolates v, refuting D. The bridge argument does not depend on distinct or positive weights.

## Q50

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The two expressions cross at x=±1. For |x|≤1 the minimum is x²; outside it is 2−x². Thus maximum 1 occurs at ±1, and minimum −2 at endpoints ±2, proving A,B. Near 0 the function is the polynomial x² and differentiable, proving C. At 1 the left derivative is 2 and right derivative −2, refuting D. Continuity at a branch crossing does not imply differentiability.

