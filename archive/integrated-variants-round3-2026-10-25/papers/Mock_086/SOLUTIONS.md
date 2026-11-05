# Worked Solutions — Mock Test 086

## Q1

**Correct answer:** A

The required numerical answer is **2**, so select **A**.

For x=1 the statements have truth pattern true,false,false. For2 it is true,true,false. For3 it is false,false,true, and for4 false,true,false. Exactly two are true only at2. Evaluating the conjunction of all three would answer a different condition.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordered reflections.

The first reflection sends (x,y) to (x,−y); the second swaps the coordinates, producing (−y,x), A. B gives the reverse-order composition, C is a half-turn, and D gives only the first reflection.

**Common misconception:** Assuming transformations commute.

## Q3

**Correct answer:** B

Selection rewards either of two attributes, so among selected applicants one attribute can compensate for the other. This can induce the reported association, supporting B as a possibility. A asserts causation and population generality without evidence. C contradicts the stated selection rule. D rules out a combination that the rule permits. A selected subgroup need not preserve population associations.

## Q4

**Correct answer:** B

The required numerical answer is **8**, so select **B**.

Fix A at seat 0 to quotient out rotations; B must occupy seat 3. Among remaining seats 1,2,4,5, the only adjacent pairs are{1,2} and{4,5}. Choose one of those pairs for C,D in two ways, orient C,D in two ways, and place E,F in the two remaining seats in two ways. Total 2×2×2=8. Reflection is not identified, so the reversed orientations remain distinct.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 8 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q5

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: cumulative frequencies. The median is the thirteenth ordered observation. The first two bins contain 4+6=10 observations, and the third extends the cumulative count to 20. Hence observation 13 lies in [20,30), C. A and B finish too early; D starts after observation 20. The bin containing the mean need not be identifiable from these data.

## Q6

**Correct answer:** 2 (exact)

**Concept:** General Aptitude — Paper folding and cutting

1. Unfolding a point (x,y) produces (x,y), (8-x,y), (x,8-y), (8-x,8-y).
2. The first punch produces (5,6),(3,6),(5,2),(3,2). Only (5,6) lies on y=x+1.
3. The second produces (6,5),(2,5),(6,3),(2,3). Only (2,3) lies on that line. The sets are disjoint, so the answer is 2.

**Common misconception:** Both folds must be reversed; points from different punches need not lie on the same symmetry line.

## Q7

**Correct answer:** B
**Concept:** Inclusion–exclusion with a restricted denominator.

One hundred people read at least one paper. Intersection size is 70+60−100=30. Exactly-one readership is 100−30=70. The requested fraction among the 100 readers is 70/100=7/10. B is correct; A counts both-paper readers, while C,D use incorrect counts or denominators.

**Common misconception:** “Among those who read at least one” changes the denominator from the full survey size.

## Q8

**Correct answer:** 0.4286 (accepted range 0.42855–0.42865)

There are4²−3²=7 ordered outcomes with maximum4. An even sum requires both entries even; among even values{2,4}, the pairs with at least one4 are(2,4),(4,2),(4,4), three outcomes. Conditional probability3/7≈0.4286. Do not count only unordered pairs because doubles and unequal pairs have different multiplicities.

## Q9

**Correct answer:** B
**Concept:** Necessary conditions and separate permissions.

No renewal implies stopping Monday. Because the policy is obeyed and the pilot continues Tuesday, renewal occurred before Monday. Expansion has the additional review requirement, whose satisfaction is not stated. B follows. A and C infer expansion permission without evidence; D treats review as a substitute despite the word “also.”

**Common misconception:** Satisfying a necessary condition for one action does not satisfy all conditions for a different action.

## Q10

**Correct answer:** 1

Put t=log2(x), so log4(x)=t/2. Then t²/2=8, giving t=4 or−4. Hence x=16 or1/16, whose product is1. Positive x does not imply a positive logarithm, so the negative t solution must not be discarded.

## Q11

**Correct answer:** C

**Concept:** Regular versus unbounded matching requirements.

C has regular expression (aa)*b*. A requires matching two unbounded counts and is nonregular. For B, pumping a sufficiently long prime-length unary word by q extra copies of a nonempty pumped block, where q is the chosen prime length, gives composite length q(1+|y|), violating the prime condition. D is nonregular: distinct prefixes 0^n1 are distinguished by suffixes 0^n1, since equality of the two zero-block lengths is required for the resulting two-one word to be a square.

**Common misconception:** Treating all numerical length restrictions as nonregular; fixed modular restrictions are regular.

## Q12

**Correct answer:** C
**Concept:** Stable multi-key sorting.

The first pass gives (a,2),(a,1),(b,1),(b,2). The second pass moves both number-1 records ahead of both number-2 records while preserving letter order within each equal-number group. The result is (a,1),(b,1),(a,2),(b,2). C matches. A instead gives letter priority; B,D violate preserved ordering within a numeric group.

**Common misconception:** With successive stable sorts, the final sort key has highest priority.

## Q13

**Correct answer:** A, C

Conditional next-address logic can select using a status flag(A), while a microinstruction can drive multiple nonconflicting controls in one cycle(C). Control stores can be read-only, so B is false. Different instructions or conditional paths may traverse different numbers of microinstructions, so D is false. Microprogramming specifies control sequencing; it does not impose equal instruction latency or writable storage.

## Q14

**Correct answer:** 2

Each triangle is an odd cycle and requires one of its own edges removed. The triangles have disjoint edge sets, so at least two removals are necessary. Removing one edge from each leaves two paths joined by a bridge, a tree, which is bipartite. Thus the lower bound is achievable. Removing the connecting bridge alone leaves both obstructions.

## Q15

**Correct answer:** 4

Start with{1,2,3}, sum6. Replacing any chosen i by i+3 adds3 and flips parity. The sum is even when the number of replacements is even: choose0 or2 of the three pairs, giving1+3=4 subsets. Selecting exactly one from each pair is a constraint separate from selecting three arbitrary elements.

## Q16

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A determines B, so it supplies AB and hence C; B on the left of AB→C is extraneous (A). C then determines D, making the direct A→D redundant (B). A determines all attributes and is minimal, proving D. Without C→D, the closure of C contains only C, so that dependency is not redundant and C is false. Removing an entire dependency differs from removing an extraneous attribute within another one.

## Q17

**Correct answer:** A

**Concept:** Quantifiers in the pumping lemma.

Regularity promises at least one pumpable valid decomposition. Showing that one chosen decomposition fails does not exclude another. For the selected word, every allowed y lies in the initial zeros and has positive length; pumping it down breaks equal counts. That universal step repairs the proof, as A says. B is not required, C incorrectly bans a permitted pumping exponent, and D reverses the length condition.

**Common misconception:** Choosing the adversary's decomposition in a nonregularity proof.

## Q18

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

## Q19

**Correct answer:** B

By-value parameter assignment changes the callee's own scalar copy, proving B and disproving A,D. The parameter can normally be assigned like another local scalar, so C is false. Passing a pointer value would be a different situation expressly excluded here.

## Q20

**Correct answer:** 4

Compute t1=a+b, t2=c−d, t3=t1*t2, and result=t3+t1: four binary operations. There are four distinct required operation nodes in the expression DAG under the restriction against reassociation. Counting the repeated a+b twice would miss reuse.

## Q21

**Correct answer:** 4

**Concept:** Product of generating functions.

Expanding gives Σ_(i≥0)x^i times Σ_(j≥0)x^(2j). The coefficient counts nonnegative solutions to i+2j=7, with j=0,1,2,3. There are four.

**Common misconception:** Using ordered partitions into arbitrary positive parts instead of the two generating factors' choices.

## Q22

**Correct answer:** 4 (exact)

**Concept:** Computer Networks — Distance-vector and link-state routing

Initially dA=2 and dB=1. In round 1 B loses its direct link and uses A's previous 2, giving 3. A still uses B's previous 1 and remains 2. In round 2 A uses B's3 and obtains min(10,1+3)=4. B uses A's previous 2 and remains 3. The requested advertised metric is 4, not the true surviving shortest-path distance 10.

**Common misconception:** Synchronous distance vectors use previous-round advertisements, which can retain routes through the failed link.

## Q23

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: IPv4 fragment payload units. Subtract the 20-byte header: payloads are 512,520,532,536. Dividing by eight gives integers for A, B and D; 532 leaves remainder four, so C fails. MF=1 means more fragments follow, so this is not the final-payload exception. Alignment applies to payload length, not total length.

## Q24

**Correct answer:** C

The required numerical answer is **16**, so select **C**.

The first copy produces[1,1,2,3,4]. The second saves its source[2,3,4] before overwriting positions0–2, yielding[2,3,4,3,4]. The sum is16. Temporary-copy semantics prevent an overlapping write from changing a later source read within the same copy.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 16 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -8 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q25

**Correct answer:** D

The required numerical answer is **0**, so select **D**.

If b OR c is false, b=c=0. The two remaining conjuncts require a and NOT a simultaneously, impossible. No assignment qualifies. This is also the resolution implication from(a OR b) and(NOT a OR c) to(b OR c).

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q26

**Correct answer:** A, C

Negating NOT p OR q gives p AND NOT q, so A is true. Under p=true, p XOR q equals NOT q; under p=false, conjunction with p is false, proving C equivalent. B is the original implication and D represents the opposite asymmetric case.

## Q27

**Correct answer:** B

The required numerical answer is **6**, so select **B**.

**Concept:** Determinant effects of elementary operations.

Swapping two rows changes −2 to 2. Scaling a column by three then changes the determinant to 6.

**Common misconception:** Applying a row-swap sign change twice or scaling by the matrix dimension.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 6 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q28

**Correct answer:** B

The required numerical answer is **20**, so select **B**.

**Concept:** Prefix-range membership before longest matching.

The /20 beginning at third octet 32 covers third octets 32 through 47, so 41 matches it. The /24 route covers only third octet 40 and does not match. The /16 and default match but are less specific. Selected length: 20.

**Common misconception:** Choosing the most specific table entry without first checking that it matches.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 20 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -10 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q29

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Doubly linked neighbour repair.

Bypassing X requires P's forward pointer to reach N and N's backward pointer to reach P, A. B changes the wrong directions; C retains X; D creates self-links rather than preserving the remaining chain.

**Common misconception:** Updating only the forward chain or reversing the pointer directions.

## Q30

**Correct answer:** B
**Concept:** Overlapping pattern occurrences.

The windows ending at positions 3 and 5 are both 101. The detector emits two pulses, so B holds. A disallows the overlap, C counts the three possible windows without testing them, and D counts bits rather than matches.

**Common misconception:** An overlapping detector may reuse the last bit of an earlier match.

## Q31

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

## Q32

**Correct answer:** A, C

Wakeup does not certify the predicate, and another thread can act before mutex reacquisition, so A,C hold. B omits the needed recheck. D contradicts the specified reacquisition. Waiting should normally occur inside a predicate-checking loop.

## Q33

**Correct answer:** 205 (exact)

**Concept:** Operating Systems — I/O scheduling

1. The head reaches 70 at time 20 and 90 at time 40, then reverses toward the pending request at 10.
2. At time 45 it is at 85, moving downward. The new request at 95 is behind its direction of travel, so it does not interrupt this sweep.
3. The head reaches 10 at time 120 and then travels 85 cylinders to 95. Total movement is 20 + 20 + 80 + 85 = 205.

**Common misconception:** A request arriving near the head is not necessarily served next; LOOK preserves the sweep direction while a request remains ahead.

## Q34

**Correct answer:** D

The required numerical answer is **2**, so select **D**.

**Concept:** Memory bank selection.

Four chips are needed: 64/16=4. Each chip uses fourteen internal address bits for its 16 KiB locations. The full memory needs sixteen address bits, leaving two to select one of four chips.

**Common misconception:** Confusing data width with address depth.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q35

**Correct answer:** 5
**Concept:** Counting linear extensions of a DAG.

The valid orders are ABCD,ABDC,BACD,BADC,BDAC. To derive the list, if A is first then B must be second and C,D can follow in either order. If B is first, either A is next followed by C,D in either order, or D precedes A and then C. Total 2+3=5.

**Common misconception:** Vertices that have no edge between them can still be indirectly constrained by other vertices.

## Q36

**Correct answer:** 8

Concept: bounded-stack permutations. Each valid push/pop history determines a unique permutation because inputs are pushed in a fixed order. Conversely the desired next output determines which unpushed inputs must be pushed before its pop, making the history unique. A nonempty push/pop path of maximum height two decomposes into excursions of the form push, k repetitions of push-pop at height one, pop. Such an excursion uses any positive number of pushes and has one shape for each number. Histories with four pushes therefore correspond to ordered compositions of four, counted by 2³=8. Counting all Catalan paths would allow stacks of height three or four.

## Q37

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Tree reconstruction from traversals.

Preorder makes A the root. Inorder splits left D,B,E from right C,F. The left subtree root is B with children D,E; the right subtree root is C with right child F. Postorder is D,E,B,F,C,A, option A. B places B before E, C reverses children and right-subtree order, and D interleaves nodes from different subtrees.

**Common misconception:** Preserving preorder's root-first order while attempting a postorder traversal.

## Q38

**Correct answer:** A, C, D

**Concept:** Computer Networks — Network address translation

The NAT distinguishes the simultaneous connections using its assigned public ports. Its reverse mapping for 41002 restores destination address 10.0.0.2 and destination port 5000.

- **A:** is true by the stated mapping.
- **B:** is false: the server sees public source address 198.51.100.6 for both connections, with distinct source ports.
- **C:** is true: the source address is part of the IPv4 header covered by its header checksum.
- **D:** is true: the TCP checksum covers the TCP header, including the source port, and an IPv4 pseudoheader that includes the source and destination addresses.

**Common misconception:** A transport checksum can depend on network-layer addresses even though those addresses are not in the TCP header itself.

## Q39

**Correct answer:** 8

Concept: overflow in an otherwise valid cancellation. For x=−4,...,3, doubling stays in −8,...,7 and exact halving recovers x: eight values. For x=4,...,7, the wrapped product is 2x−16 and halving gives x−8. For x=−8,...,−5, it is 2x+16 and halving gives x+8. None of these recover x. Algebraic cancellation can fail when the intermediate representation overflows.

## Q40

**Correct answer:** 6

Concept: DFA memory and minimization. Use one start state, two states with no equal pair yet and last bit 0/1, two accepting states with exactly one equal pair and last bit 0/1, and one sink after a second equality. All six are reachable. Accepting states differ on suffix 0; zero-equality states also differ on suffix 0. Start differs from each zero-equality state by repeating that state's last bit once. Accepting versus nonaccepting states differ on ε. The sink differs from every other nonaccepting state because each has an accepting continuation. Therefore no states merge. An equality count alone loses the previous-bit information.

## Q41

**Correct answer:** A, C

Tabular combination requires identical dash positions and exactly one differing fixed bit. A combines {0,1} and {2,3}; its cube covers precisely four ON minterms. C combines {0,2} with {8,10}; allowing the don't-care 10 gives the valid cube {0,2,8,10}. B's inputs have different dash positions and different sizes. Its proposed cube also includes OFF minterm 11. D likewise combines unequal dash patterns, and its proposed cube includes 11. Thus A and C are valid; B and D are invalid. Don't-care minterms may assist grouping, but OFF minterms never may.

## Q42

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Loop fixed points and zero-iteration paths.

At the header, the entry edge carries x=1 and the back edge x=2; the analysis joins them as not constant, so A is false. The assignment establishes x=2 immediately after itself, proving B. The loop may execute zero times, leaving final y=1, so C is false. A do-while executes the assignment at least once and never changes x afterwards, eliminating y=1 and proving D.

**Common misconception:** A fact established by a loop body need not hold after a loop that can execute zero times.

## Q43

**Correct answer:** A

At depth d there are2^d calls, each initializing2^d cells, so total initializations sum4^d from d=0 to k, which is Θ(4^k)=Θ(n²). Sequential depth-first processing keeps only one root-to-leaf chain of buffers live at once; its sizes sum1+2+...+2^k=2n−1, giving Θ(n). A follows. B,D undercount total work, and C counts allocations from nonoverlapping sibling calls as simultaneously live.

## Q44

**Correct answer:** D

The required numerical answer is **5**, so select **D**.

**Concept:** Round-robin scheduling with I/O.

The CPU schedule is P:[0,2), Q:[2,4), Q:[4,6), P:[6,8), Q:[8,9). P performs I/O on [2,5), then waits [5,6), giving waiting time 1. Q waits [0,2) and [6,8), giving 4. Their sum is 5. Q is not preempted at time 5 because the I/O completion only enqueues P.

**Common misconception:** Including blocked I/O time in ready-queue waiting time.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 5 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q45

**Correct answer:** B

**Concept:** Virtual reservation and demand allocation.

An address range can be validly reserved before private physical frames are allocated; first writes trigger backing allocation. This proves B and refutes A. Address translation allows distinct virtual and physical addresses, refuting C, and first-write faults on valid mappings refute D.

**Common misconception:** Treating a valid virtual mapping as proof that its private physical storage is already present.

## Q46

**Correct answer:** A, B, C

The two expressions cross at x=±1. For |x|≤1 the minimum is x²; outside it is 2−x². Thus maximum 1 occurs at ±1, and minimum −2 at endpoints ±2, proving A,B. Near 0 the function is the polynomial x² and differentiable, proving C. At 1 the left derivative is 2 and right derivative −2, refuting D. Continuity at a branch crossing does not imply differentiability.

## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: Shannon decomposition of parity. Sum=a XOR b XOR c. For ab=00,01,10,11 it is c,c′,c′,c, hence B. A is the carry-out input pattern, not sum. C complements every required output. D gives only a, independent of b and c. Separate sum and carry functions.

## Q48

**Correct answer:** D

The required numerical answer is **0.375**, so select **D**.

**Concept:** Conditional density over a planar region.

P(Y>X²)=∫₀¹(1−x²)dx=2/3. The weighted first moment over that event is ∫₀¹x(1−x²)dx=1/4. Dividing gives (1/4)/(2/3)=3/8=0.375.

**Common misconception:** Conditioning by substituting Y=X² instead of integrating the region above the curve.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 0.250 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -0.187 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 0.313 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q49

**Correct answer:** A, C, D
**Concept:** Counter recovery and output waveforms.

States 6 and 7 enter 0 after one edge, proving A and refuting B. On states 0–5, q2=1 only for 4 and 5, two out of six intervals, proving C. The low bit has sequence 0,1,0,1,0,1 before returning to 0, proving D.

**Common misconception:** The physical number of state bits does not force a cycle containing all eight bit patterns.

## Q50

**Correct answer:** A

The required numerical answer is **405**, so select **A**.

**Concept:** Matrix-chain dynamic programming.

For adjacent pairs, costs are m12=150,m23=360,m34=180. For triples, m13=min(360+600,150+180)=330 and m24=min(180+150,360+600)=330. Splitting the four-matrix chain after positions 1,2,3 gives costs 330+250=580, 150+180+75=405, and 330+300=630. The minimum is 405, achieved by (A1A2)(A3A4).

**Common misconception:** Multiplication is associative algebraically, but the intermediate dimensions determine computational cost.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 405 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -202 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q51

**Correct answer:** B

The required numerical answer is **0**, so select **B**.

The requested end offset is98+4=102, exceeding the limit100. The entire access fails the atomic bounds check before any byte is read, so zero bytes are accessed. Two requested byte addresses lie within the segment, but that does not authorize a partial read under these semantics.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.


## Q52

**Correct answer:** D

The required numerical answer is **2**, so select **D**.

Inserting35 changes the right leaf to[30,35,40,50], which splits into[30,35] and[40,50]; separator40 is added, leaving root keys[30,40]. Inserting45 yields[40,45,50] without overflow. Inserting15 yields[10,15,20] without overflow. The root thus retains2 separators and3 children. The copied key remains in its leaf; B+ leaf splitting does not remove it as a data key.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q53

**Correct answer:** A
**Concept:** Pointer updates and reachability.

t first saves node 3. Then node 2 points to node 5, and node 4 points to node 3. Node 3 still points to node 4, so those two form a separate cycle, but it is unreachable from node 1. The traversal from the specified head is 1,2,5,NULL. A is correct; B,C assume a different splice, and D confuses an unreachable cycle with the head's traversal.

**Common misconception:** A cycle elsewhere in the allocated nodes need not be reachable from the list head.

## Q54

**Correct answer:** B

The required numerical answer is **72**, so select **B**.

The equation g∘f=id_A forces f injective. Choose distinct images for A's three labelled elements in4×3×2=24 ways. g is then forced on those three images, while its value on the unused B element is any of three A elements. Total24×3=72. A left inverse need not be uniquely determined outside the image.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 72 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -36 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q55

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recoverability and cascading aborts.

r2(X) reads the uncommitted w1(X), proving A. Recoverability would require T1 to commit before T2 commits; instead T1 aborts after c2, so B is false. T2's dependence requires aborting it when T1 aborts, but T2 has already committed, establishing C's problem. Strict schedules prohibit this read of an uncommitted write, so D is false.

**Common misconception:** Treating a completed commit as evidence that a schedule satisfies recovery constraints.

## Q56

**Correct answer:** 22

**Concept:** Congestion-window timing within rounds.

The first four rounds transmit windows 4,5,6,7 MSS, increasing only after each round. Total 4+5+6+7=22 MSS.

**Common misconception:** Applying the first increase before transmitting the first window.

## Q57

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Mutual exclusion versus progress.

Both threads can set their flags before either tests the other, after which both wait forever with flags true (A). For simultaneous entry, both would need to read the other's flag false after setting their own true. Sequential consistency cannot order those four events that way: whichever thread sets its flag first prevents the other from passing once that other sets its own. Thus mutual exclusion holds (C), and B is false. Volatile alone does not change the allowed flag-setting interleaving or add a tie-breaker, refuting D.

**Common misconception:** Mutual exclusion does not imply deadlock freedom or progress.

## Q58

**Correct answer:** B

The required numerical answer is **3**, so select **B**.

At the point queried, p is needed for the branch. If execution goes to Again, b supplies the next a; if it goes to Exit, the current a is returned. Thus a,b,p are live under may-liveness, giving3. The analysis unions possible successor uses; it does not require all three to be used on the same execution path.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q59

**Correct answer:** B

The required numerical answer is **64**, so select **B**.

The first write to each of the two blocks causes one16-byte write-allocate fetch, totaling32 bytes. The other two writes hit those lines. Flushing writes the two dirty blocks once each, adding32 bytes. Total traffic is64 bytes. One-byte stores do not imply one-byte memory transfers under the given full-block policy.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 64 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -32 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q60

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

## Q61

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Read timestamps in timestamp ordering.

After the read, RTS(x)=10 while WTS(x)=0. T5's write has timestamp 5<RTS(x), meaning a later transaction already read a value that would have preceded this write in timestamp order. T5 must abort. A ignores that read; B misuses the obsolete-write exception; D destroys the recorded ordering information.

**Common misconception:** Thomas's rule does not authorize ignoring a violation of the read-timestamp check.

## Q62

**Correct answer:** A

The required numerical answer is **1**, so select **A**.

The polynomial p(t)=t²−5t+7 maps both eigenvalues2 and3 to1. Eigenvalues of p(A) are consequently1,1, and its determinant is their product1. Equivalently Cayley–Hamilton gives A²−5A+6I=0, so the target matrix is I. Matrix entries need not be reconstructed.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.


## Q63

**Correct answer:** A, C

Concept: fair search of nondeterministic computations. With finite branching each finite depth has finitely many nodes, so BFS eventually reaches any finite accepting branch (A). DFS can stay forever on an epsilon loop (C), disproving B. For a rejected input an infinite nonaccepting computation tree can keep naive BFS running forever, disproving D. CFL membership is decidable by other constructions; this does not make every naive simulation a decider.

## Q64

**Correct answer:** 2048

Offset6144 is in logical block6, using zero-based block numbering. The four direct pointers cover blocks0–3; block6 needs the single-indirect structure. Allocate one1024-byte indirect block and one1024-byte data block. Sparse holes require no intervening data blocks, giving2048 bytes. Logical file length is not allocated storage size.

## Q65

**Correct answer:** A, C
**Concept:** Unequal-count context-free language.

Split L into i<j and i>j; a PDA can match counts with its stack and accept an unmatched excess on either side, so their union is context-free (A). Its complement within a*b* is exactly the equal-count language (C). If L were regular, subtracting it from regular a*b* would make that equal-count language regular, a contradiction, so B is false. ε has equal zero counts and is excluded (D false).

**Common misconception:** Context-free unequal-count languages need not be regular.

