# Worked Solutions — Additional Practice Set 005

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Month 1 productivity is (400+900)/(40+60) = 13 items/hour.
2. Month 2 productivity is (660+640)/(60+40) = 13 items/hour.
3. The percentage change is zero, even though each team's own rate improved. More hours were allocated to the slower team.
- Original option A: Both aggregate rates are 13.
- Original option B: A simple or weighted average of team percentage gains cannot replace aggregation with the new hour mix.
- Original option C: This is only A's rate improvement.
- Original option D: Neither the total output nor the total hours implies this increase.

## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

C is declared directly inside A, so every C activation reaches the same active A through its static link. Its references to x therefore name A's x, initially 4, even when a B activation containing its own x is C's caller. B(2) first calls B(1), which first calls B(0). B(0) calls C: A.x becomes 5 and 5 is returned. B(1) next calls C, obtaining 6, and returns 5+6=11. B(2) next calls C, obtaining 7, and returns 11+7=18. Main prints 18. The recursive B locals would matter under dynamic lookup, but not under the specified lexical lookup.
- Original option A: True: the calls to C update the single enclosing A.x to 5,6,7 and their returned values sum to 18.
- Original option B: False: 101+102+103=306 uses each calling B activation as the variable environment, which would be dynamic rather than static scoping.
- Original option C: False: 15 assumes all three C calls start from a fresh copy of A.x=4; the enclosing activation persists and is modified.
- Original option D: False: 21+22+23=66 uses Main.x, but the nearer enclosing declaration in A shadows it.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Verbal grammar

1. An unreal past condition uses “had left” with the result “would have caught”.
2. A participial clause cannot attach Mira's late arrival to the grammatical subject “the meeting”. Naming Mira in a when-clause resolves that dangling modifier.
3. Only B satisfies both requirements and retains the original time relationship.

- **A:** It changes the past counterfactual and still assigns the late arrival to the meeting.
- **B:** The past counterfactual and arrival subject are both correct.
- **C:** The result should be would have caught; the dangling modifier also remains.
- **D:** The conditional form is wrong and the subjects no longer express the intended facts.

**Common misconception:** Fixing one tense error does not repair a separate dangling modifier.

## Q4

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Engineering Mathematics — Recurrences and generating functions

1. Mark each 1 by y. If F(x,y) counts all strings with no consecutive 1s, the last-bit recurrence for n>=2 is F_n(y)=F_(n-1)(y)+y*F_(n-2)(y), with F_0=1 and F_1=1+y. Thus F(x,y)=(1+xy)/(1-x-x^2*y).
2. Keeping only even powers of y gives E(x)=(F(x,1)+F(x,-1))/2.
3. Combining the fractions gives numerator 1-x+x^3 and denominator (1-x)^2-x^4=1-2x+x^2-x^4. This is B; it begins 1+x+x^2+2x^3+4x^4+... .

- **A:** This counts all allowed strings without the parity restriction; its coefficient of x is 2 instead of 1.
- **B:** It is the even-parity projection of the bivariate generating function.
- **C:** Its coefficient of x^2 is 2, but the only even-parity valid length-2 string is 00.
- **D:** It misses the x^3 numerator contribution and gives coefficient 1 at x^3 instead of 2.

**Common misconception:** Parity restrictions require tracking a marked statistic, not merely forbidding local patterns.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reading comprehension and inference.

Weekly visits may be redistributed across times without increasing their total. In addition, one visitor can make several visits, so distinct visitors cannot be inferred from visit totals. B identifies both gaps. A wrongly excludes redistribution; C asserts an unsupported decrease; D replaces a possibility with an assertion about every visitor.

**Common misconception:** Treating counts of events as counts of distinct people, or a before/after association as proof of recruitment.

## Q6

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Conditional cache hit rates.

L1 misses with probability 0.2. Half hit L2 and half reach memory, each with probability 0.1. Expected time is 1+0.2×9+0.1×90=11.8 ns. A,B,C hold. D confuses a conditional 50% with an unconditional 10%.

**Common misconception:** Additional miss penalties must be weighted by the probability of reaching their level.

## Q7

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Quantified deduction.

The witness that is both A and B is C and therefore not D, proving B. Every B is C and no C is D, proving D. A generalizes the one known A witness to every A. C asserts an overlap with D that is neither required nor supplied.

**Common misconception:** An existential premise cannot generally be promoted to a universal conclusion.

## Q8

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recovery conditions versus serializability.

T2 reads from T1 and commits after T1; T3 reads from T2 and commits after T2, so the schedule is recoverable. Both reads occur before the producing transaction commits, so it is neither cascadeless nor strict. Conflict edges are T1→T2→T3 with no cycle. Thus A,C hold and B,D fail.

**Common misconception:** Recoverability permits dirty reads if commit dependencies are respected; cascadelessness does not.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Recovering subgroup totals.

The original total is 20×30=600. The retained total is 15×34=510. The removed five therefore average (600−510)/5=18. The new total is 510+5×28=650, giving mean 32.5. The required difference is 32.5−18=14.5, option B. A,C,D disagree with these totals.

**Common misconception:** The incoming workers' mean is not the new group's mean.

## Q10

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Context-free union and intersection limitations.

L is the union of {aⁿbⁿcᵏ} and {aⁱbⁿcⁿ}; both are context-free, so L is context-free. It contains every aⁿbⁿcⁿ, making its intersection with that language exactly the non-context-free language {aⁿbⁿcⁿ}. C is correct. A incorrectly infers complexity from containing a subset. B is false: intersecting L with the regular language a*b* (no c) gives {aⁿbⁿ}∪a*, which is nonregular; alternatively a standard regular pumping argument on aᵖbᵖ disproves regularity of L itself. D is false because cᵏ is in L for every k.

**Common misconception:** Context-free languages are closed under union, but not arbitrary intersection.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Arithmetic versus logical shifts.

11111011 represents −5. Arithmetic right shift gives 11111101, which is −3; logical right shift gives 01111101, which is 125. B matches. A assumes truncation toward zero for the arithmetic shift; C,D fail to insert zero at the high bit for the logical shift.

**Common misconception:** Arithmetic right shift of a negative odd integer rounds toward negative infinity, unlike truncating integer division in some languages.

## Q12

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Weighted means with positive weights.

The combined mean is a convex combination of 40,60,80 with all weights positive, so it lies strictly between 40 and 80 (A). Equal sizes give 60 (C). Sizes 2,1,1 give mean 55, refuting B and D.

**Common misconception:** An unweighted mean of group means is valid only with suitable group weights.

## Q13

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Pointer updates and reachability.

t first saves node 3. Then node 2 points to node 5, and node 4 points to node 3. Node 3 still points to node 4, so those two form a separate cycle, but it is unreachable from node 1. The traversal from the specified head is 1,2,5,NULL. A is correct; B,C assume a different splice, and D confuses an unreachable cycle with the head's traversal.

**Common misconception:** A cycle elsewhere in the allocated nodes need not be reachable from the list head.

## Q14

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Output-sensitive lower bounds.

There are C(n,2)=n(n−1)/2 distinct pairs to emit. Constant work per output gives Ω(n²), so D is the tight bound from output size. A,B,C are asymptotically weaker and do not express the tight output-size requirement.

**Common misconception:** An efficient internal algorithm cannot avoid the time needed to materialize its required output.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Confounding in observational comparisons.

A supplies a pre-existing difference that can explain part of the final gap, undermining attribution of the entire gap to tutoring. B describes a venue, C gives a common assessment, and D describes reporting completeness; none supplies a competing explanation for the score difference.

**Common misconception:** Interpreting a voluntary-treatment comparison as randomized causal evidence.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Linked-list reversal invariants.

After saving next, point cur back to prev, move prev to the newly reversed head cur, then advance cur to saved next. This is B. A advances too soon and rewires the wrong node; C also rewires the successor and can dereference null; D retains the forward link and moves both pointers to the successor, performing no reversal.

**Common misconception:** Updating traversal pointers before preserving and reversing the current node's link.

## Q17

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Closures and environment lifetime.

F and G need separate cells associated with their separate outer activations, and those cells must remain alive while captured. B provides both identity and lifetime. A wrongly merges cells, C leaves dangling references, and D implements caller-dependent lookup rather than lexical capture.

**Common misconception:** Assuming every local variable's lifetime must end when its defining call returns.

## Q18

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Right inverses throughout a monoid.

For a, choose b with ab=e. Choose c with bc=e. Associativity gives a=a(bc)=(ab)c=c, hence ba=bc=e. Thus every a has a two-sided inverse, establishing A and the group property B. Groups need not commute (C false), and inverses must satisfy the equations rather than being arbitrary (D false, as any nontrivial group illustrates).

**Common misconception:** Assuming one-sided inverses remain one-sided when the inverse-existence condition applies to every element.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** LOOK direction and reversal point.

Starting upward, the head serves 55 then 70, reverses at the final pending request, and serves 30 then 10. A matches. B reverses too soon; C changes direction before serving all upward requests; D skips nearer upward request 55 on its outward pass.

**Common misconception:** Confusing LOOK with shortest-seek-first or with movement to the disk's physical endpoint.

## Q20

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Process-image replacement versus process identity.

The specified semantics preserve the PID and unmarked descriptors while replacing the address space, directly giving A and B. Old heap pointers have no guarantee of their old objects after replacement, refuting C. D contradicts the descriptor-preservation rule.

**Common misconception:** Treating successful exec as creation of a new process or preservation of the old memory image.

## Q21

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Subtraction flags and signed range.

The full unsigned sum is A+(2ⁿ−1−B)+1=2ⁿ+A−B. A carry exists exactly when A≥B, meaning no unsigned borrow, proving A. Retained bits give the modulo result, proving B. Opposite signed operands can produce a sign inconsistent with A when their difference exceeds range, establishing D. Borrow and signed overflow are different: for four bits, 0−1 borrows but has valid signed result −1, refuting C.

**Common misconception:** Using one flag interpretation for both signed and unsigned arithmetic.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Definitions along branch paths.

Each feasible branch defines the value consumed at the join, establishing A. B would make x=b even when p is true, while C and D disregard the source condition and selected values.

**Common misconception:** Treating a branch join as permission to execute both mutually exclusive assignments.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Scope of measured evidence.

Only average processing time was measured as improving, while error counts were not measured. A respects that boundary. B,D invent accuracy findings, and C also turns an average improvement into a statement about every decision.

**Common misconception:** Extending evidence on speed to evidence on accuracy.

## Q24

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Vacuous pumping conditions for a finite language.

With p=8, no word in L has length at least p, so the condition holds vacuously. For any positive p≤7, word a⁷ is long enough; every valid pumped segment is nonempty, and pumping it twice produces a word longer than seven, outside L. Thus no smaller p works. A is correct, B,C fail this test, and D denies regularity of finite languages.

**Common misconception:** Assuming a pumping lemma must actually pump some word even when all words are shorter than its bound.

## Q25

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: dead stores. No operation reads the first stored value before the second assignment overwrites it; removing that store preserves behavior (A). B invents an invalidity rule; C contradicts print's use of x; D would remove the value that print requires. The side-effect assumption is essential.

## Q26

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: postfix translation. Multiplication forms subtree b*c, emitting bc*. Addition emits a, then that subtree, then +, producing abc*+. C is correct. A represents (a+b)*c; B is prefix order; D represents a*(b+c). Tree traversal follows precedence before emitting operators.

## Q27

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: nondeterministic midpoint matching. To consume abba and empty its pushed portion, push and matching lengths must both be two, proving A. The matched suffix ba is the reversal of prefix ab. A guess after one symbol cannot ignore a mismatch or extra input, so B is false. For abab the only possible balanced lengths are two and two, but suffix ab is not the reversal ba, so C is true. Nondeterministic acceptance needs one successful branch; incorrect guesses do not invalidate another accepting branch, so D fails.

## Q28

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: complete address decoding. First interval has high bits A15A14=00, so A is correct. Second interval has A15A14A13=010, giving D. B would also enable the chip over 0x6000–0x7FFF, creating unwanted aliases. Mapped capacity is 16+8=24 KiB of 64 KiB, leaving 40 KiB, so C is false. Chip offset bits and chip-selection bits serve different roles.

## Q29

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: instance-level functional dependencies. Each AB pair occurs once, so AB→C holds (B). Repeated C=p always has B=x; q and r each have B=y, so C→B holds (D). A=1 has C=p and q, disproving A. C=p occurs with A=1 and 2, disproving C. A dependency is checked by equal determinant values, not by counting columns or rows alone.

## Q30

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Distinct meanings of unsigned carry and signed overflow.

The unsigned addition is128+254+1=383=256+127. Thus the low bits are01111111 and carry-out is1. Signed interpretation computes−128−1=−129, outside the signed8-bit range, so overflow is1. B states all three correctly. A misses carry and overflow. C has the wrong result and overflow. D gives the right result and overflow but the wrong carry-out.

**Misconception:** Assuming that carry-out and signed overflow are mutually exclusive or equivalent indicators.

## Q31

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After buffered data are exhausted, pipe EOF requires every write-end reference to be closed. The child still has one, so B is true and A false. Closing its read end does not remove that writer, making C false. Closing its write end with no other writers permits EOF, making D true. An idle writer is different from a closed writer.

## Q32

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Reusing the same tag can match an old virtual-page entry and produce an obsolete frame, making A true. Invalidating the tag's entries removes those stale hits, so C is true. ASIDs distinguish concurrently assigned address spaces only when reuse is managed; B is false. The lookup key in the question omits the page-table base, so changing that base alone does not guarantee a miss, making D false.

## Q33

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

R−S={(1,y),(2,x)}, so its A-projection is{1,2}, proving A. Separately the projections are{1,2} and{1}, whose difference is{2}, proving B. The surviving(1,y) gives D and directly disproves C's proposed distributivity. Projection can collapse tuples that difference distinguishes.

## Q34

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Alternation gives each simulation unbounded progress, so an acceptance by either is eventually observed: A,C are true. Both may run forever without acceptance, disproving B. The acceptance rule is either, not both, so it neither implements intersection nor guarantees a decision; D is false.

## Q35

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Stability preserves the input order of equal-key records, proving A and C. It does not impose a complexity bound, so B is false. Sorting must generally reorder unequal keys, disproving D. Stability is a tie-order property.

## Q36

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Only reachable incoming values describe possible executions. Ignoring the unreachable7 leaves constant5, proving A,B. Including it would join5 with7 and lose constancy, proving C. D contradicts this example. Semantic reachability can sharpen a syntactic data-flow join.

## Q37

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

p−1=a+3 points to the last actual element and may be dereferenced. p itself is one-past, so A,D dereference outside the array. p+1 goes beyond even the permitted one-past pointer, making C invalid. Forming a boundary pointer does not authorize reading at it.

## Q38

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Once queued bytes have been read, an orderly end of the peer's sending stream can be reported by a zero receive result, proving A. Zero is a count, not an extra byte: B is false. TCP maintains two directions; closing one sending direction does not itself close the other, so C is true and D false. An orderly half-close differs from a connection error or forced process exit.

## Q39

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

REAL accepts digits followed by a dot and zero further digits, so it consumes the two-character lexeme consisting of1 followed by a dot. This beats the one-character INTEGER, proving A. One dot remains before2; neither RANGE nor any other rule matches there, proving C. Priority resolves equal lengths at the same starting position; RANGE cannot start at the initial digit, so B is false. Requiring a digit after REAL's dot prevents that initial real match, allowing INTEGER1, RANGE.., INTEGER2, proving D. Longest match can consume punctuation needed by a later token.

## Q40

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both calls pass the same starting buffer address. The first places A,B at positions0,1; the second places C,D,E at0,1,2, overwriting earlier bytes. A is true and B false. Using buf+n retains the first n bytes and writes subsequent bytes after them, proving C. D is false because network order does not prevent an application from choosing an incorrect destination address. Successful total byte counts alone do not prove correct assembly.

## Q41

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each link supplies its own framing, so A,C are true. Its checksum must correspond to its own frame rather than blindly copying the incoming one, refuting B. Changing encapsulation does not require changing the application message, refuting D.

## Q42

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The divisibility order has chain1<2<4<12 and the extra branch1<3<12. Every pair has a join and meet, so A. In particular join(2,3)=12 and meet(4,3)=1, proving C,D. Distributivity fails: 4 meet(2 join3)=4, whereas(4 meet2) join(4 meet3)=2 join1=2. Thus B is false. Removing a divisor can change a join from the ordinary numerical least common multiple.

## Q43

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The passage explicitly combines an unchanged mean with individual changes, which is C. A,D contradict the stated increases and decreases. B incorrectly equates one summary statistic with the entire distribution. Offsetting changes can preserve a mean while altering many other properties.

## Q44

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

At a shared suffix, linking the same node again can make its next pointer refer to itself or to an earlier shared node, proving A and refuting D. When current pointers are equal, their entire remaining suffix is the same physical list and can be attached once, proving B. Distinct nodes may contain equal values, refuting C. An in-place merge relies on aliasing assumptions as well as sort order.

## Q45

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At the join, x merges 2 with 7 and y merges 7 with 2. Each becomes nonconstant in the stated abstraction. Their correlation is discarded, so the analysis cannot infer z=9. Actual execution gives 9 in both branches. A,B incorrectly retain branch-specific constants; D combines values from incompatible branches.

## Q46

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Negating the universal yields an existential counterexample x. The implication fails when P(x) holds and its consequent ∃yR(x,y) fails; the latter negates to ∀y¬R(x,y). This is C. A retains a universal x; B negates the antecedent incorrectly; D requires only one failed witness instead of absence of every witness.

## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At most one observation of the first dataset is strictly below2, and at most one of the second is below2 because its median is9. Thus the combined third observation is at least2. Similarly, at most two combined observations exceed9, so the fourth is at most9. Their average lies in[2,9], proving B. For datasets(0,2,3) and(8,9,10), the median is5.5 and need not be an observed value, disproving D. Datasets(0,2,2) and(2,9,9) give combined median2, disproving A. Extreme tail observations make the mean arbitrarily large or small, disproving C.

## Q48

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For a list of length n, final position i holds the negative of original entry n+1−i under either order, proving B for all entries and lengths. Reversal and negation each undo themselves, and they commute; applying the composition twice restores the input(C). One example does not prove a universal statement(A), and commutation does not mean either operation is the identity(D). The argument applies equally to repeated values and an empty list.

## Q49

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The circumference difference is 2π(r+1)−2πr=2π metres. Advancing the outer start by that distance leaves equal distances to the common finish. Equal speeds then give equal finish times. A uses only half the difference; C and D depend on the unspecified radius and do not equal the difference in general.

## Q50

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The probes are 0,1,4,2,2,4,1. Four distinct slots are reachable, so the first four insertions succeed and the fifth fails despite three unused slots. This proves A and refutes B. Slot 3 is never probed, proving C. Linear probing visits all seven slots and permits seven insertions, so D is false. Table occupancy alone does not ensure a restricted probe sequence finds an empty slot.

