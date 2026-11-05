# Worked Solutions — Additional Practice Set 004

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. With A and B adjacent, treat them as a block with two orders. There are 2(5!)=240 circular arrangements.
2. If C and D are also adjacent, there are 4(4!)=96 arrangements. The same count applies when E and F are adjacent.
3. When both forbidden adjacencies occur, three two-person blocks and G form four circular units. There are 2^3(3!)=48 arrangements.
4. Inclusion-exclusion gives 240-96-96+48=96.
- Original option A: This subtracts both forbidden events and restores their intersection.
- Original option B: This is 5!: it fixes the A-B order and ignores both forbidden adjacencies.
- Original option C: This enforces only one of the two forbidden adjacencies: 240-96.
- Original option D: This ignores both forbidden adjacencies.

## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Fixing bc=00 leaves at most two ones, so I0=0. Fixing bc=01 or 10 supplies one one, so both a and d must be one: I1=I2=ad. Fixing bc=11 supplies two ones, so either a or d suffices: I3=a+d. This is Shannon decomposition with respect to the select variables.
- Original option A: True: the four cofactors are 0, ad, ad, a+d.
- Original option B: False: for bc=01, a=1,d=0 it outputs 1 with only two ones; for bc=11,a=1,d=0 it also misses a required 1.
- Original option C: False: for bc=00,a=d=1 it outputs 1 despite only two ones; bc=11,a=d=0 is another false positive.
- Original option D: False: bc=01,a=d=1 has three ones and must yield 1.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Geometry and mensuration

1. If the width is x, the planted dimensions are 16-2x and 10-2x. The planted area is 160-88=72.
2. Expanding (16-2x)(10-2x)=72 gives x^2-13x+22=0, with roots 2 and 11.
3. Geometry requires 0<x<5, so only x=2 is admissible.

- **A:** Width 1 leaves 14*8=112 square metres planted, so the path area is 48.
- **B:** Width 2 leaves 12*6=72, giving path area 88.
- **C:** Width 3 leaves 10*4=40, giving path area 120.
- **D:** Width 4 leaves 8*2=16, giving path area 144.

**Common misconception:** A border removes its width from both ends of each dimension, and algebraic roots must meet geometric bounds.

## Q4

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Algorithms — Minimum spanning trees and constrained counting

1. A spanning tree needs five edges and must connect the two triangles. Four unit edges and one weight-2 connector give weight 6. A lighter tree cannot connect all six vertices, since every connector weighs at least 2.
2. For weight 6, choose a spanning tree in each triangle in 3 ways each, then one of AD, BE, CF in 3 ways. This gives 3×3×3=27.
3. A weight-7 tree has either four unit edges and AE, or three unit edges and two weight-2 connectors. The first case gives 3×3=9.
4. In the second case choose the two connectors in 3 ways. The three unit edges must split as two in one triangle and one in the other: taking all three from a triangle would create a cycle. There are 2 choices of which triangle gets two edges, 3 choices of its spanning tree, and 2 choices of the other triangle's single edge. That edge must attach its otherwise unconnected third vertex to a connector endpoint. Thus this case contributes 3×2×3×2=36.
5. Total weight-7 trees: 9+36=45.

- **A:** Correct: the lower bound 6 is attained.
- **B:** Correct: the three independent choices give 27 distinct edge sets.
- **C:** Correct: the two disjoint weight compositions give 45 trees.
- **D:** Incorrect: a spanning tree in each triangle together with AE has weight 7 and uses no weight-2 edge.

**Common misconception:** Equal-weight edges create multiple optima, and counting the next weight requires checking connectivity and cycles, not just the number of chosen edges.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Organization and Architecture — Hardwired and microprogrammed control

The START pulse must be outside the wait loop. The loop must avoid repeating the register increment, and DATA must be sampled only after READY establishes completion. Routine B issues START once, waits in a control-only state, and executes the data transfer and increment exactly once afterward.

A repeats START and the increment during waiting. B satisfies all requirements. C starts only once but increments on each wait-loop visit. D does not wait and can sample invalid data if memory takes longer than the start cycle.

- **A:** False: repeats START and the pointer increment on each wait-loop cycle.
- **B:** True: routine B asserts START once, waits for READY, and transfers data and increments exactly once.
- **C:** False: asserts START once but repeatedly increments the pointer while polling.
- **D:** False: fails to poll READY and may sample invalid data if memory access is slow.

**Common misconception:** A control-state self-loop reexecutes that state's data-path operations every cycle.

## Q6

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Circular-list pointer updates.

The first update bypasses node 1, making node 2 the head. Inserting 5 after old tail 4 sets 4.next=5 and 5.next=2. Updating tail to 5 leaves head=2. Thus traversal is 2,3,4,5. A retains the deleted node; B starts at the tail; D inserts 5 before rather than after node 4.

**Common misconception:** In a tail-only circular-list representation the head is defined indirectly as tail.next.

## Q7

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Agreement in nested clauses.

“Reports that are missing” takes a plural verb in the relative clause. The main subject is singular “the number,” so its verb is “is.” C gives both. A gets both wrong; B misses the main subject; D misses the relative-clause subject.

**Common misconception:** The noun closest to a verb is not always that verb's subject.

## Q8

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lexer states and longest match.

The tokens are string literal "if", keyword if, and identifier if2. The comment is discarded. The string's content is not tokenized as source code, and longest match keeps if2 as one identifier. Thus one keyword and three total tokens. A counts comment/string text as keywords; B counts if2 as a keyword; C retains an extra token from discarded or split text.

**Common misconception:** Keyword recognition depends on lexical context and full token boundaries.

## Q9

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Necessary versus sufficient conditions.

Approval implies timely receipt, so timely receipt is necessary. The explicitly mentioned timely rejections show it is insufficient. A reverses the implication; B contradicts those timely rejections. C is not implied: the report is compatible with some approvals or none. D precisely states the implication and its failed converse.

**Common misconception:** “Every approved application was timely” does not mean every timely application was approved.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Prediction penalties and clock-period tradeoffs.

Old CPI is 1+0.20×0.60×3=1.36, giving 1.36 ns per instruction. New CPI is 1+0.20×0.10×3=1.06, with time 1.06×1.1=1.166 ns. Speedup is 1.36/1.166≈1.166. B is closest. A reverses the comparison; C ignores the longer clock; D treats the new execution time as 1 ns per instruction.

**Common misconception:** Improving CPI can be partly offset by a longer clock period.

## Q11

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Regular restriction of a nonregular language.

The intersection in C contains only a³b³, a finite regular language. A is the standard nonregular equal-count language. B equals L itself because all members already have a*b* form. If D were regular, complementing it would make L regular, a contradiction. Only C is regular.

**Common misconception:** Intersecting a nonregular language with a regular one can yield a regular result.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Modifier attachment.

In B, “exhausted” directly modifies researchers. A attaches the introductory modifier to experiment, C explicitly describes the samples as exhausted, and D again modifies experiment. Only B conveys the required meaning.

**Common misconception:** A nearby adjective need not describe the intended actor unless the sentence attaches it clearly.

## Q13

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Timestamp ordering in wait-die.

T1 is older than the holder T2, so it waits for x. T2 is older than holder T3, so it waits for y. T3 is younger than holder T1, so it aborts when requesting z. Only C matches. A,B reverse the requester/holder age test; D ignores the final younger-on-older request.

**Common misconception:** Under wait-die, the younger requester aborts; this differs from policies in which an older requester aborts a younger holder.

## Q14

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Full-adder outputs.

With x=y=1, the total is 2+c. Its low bit is c and its carry is always one, yielding A. B incorrectly complements the sum; C,D incorrectly make carry depend on c.

**Common misconception:** Carry indicates a total of at least two, which is already guaranteed by x=y=1.

## Q15

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Necessary conditions with an exception.

For a nonexempt consignment, release implies inspection. C asserts release and denies inspection, violating this implication. A is allowed by the exemption; B is allowed because inspection does not guarantee release; D satisfies the condition regardless of exemption.

**Common misconception:** Reading “only if” as “if and only if”.

## Q16

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Commuting idempotents and joint eigenspaces.

An idempotent is diagonalizable with eigenvalues 0 and 1. Commuting idempotents preserve one another's eigenspaces and can be diagonalized together. Let k be the dimension where both eigenvalues are 1. The dimensions for joint eigenvalues (1,1),(1,0),(0,1),(0,0) are k,3−k,2−k,k−1. Nonnegativity forces k=1 or 2. Thus rank(E−F)=5−2k is 3 or 1 (A), trace(E+F)=3+2=5 (B), and rank(EF)=k need not be 2 (C false). If k=1, E+F has eigenvalues 2,1,1,1 and determinant 2; if k=2 it has a zero eigenvalue and determinant 0 (D).

**Common misconception:** Identifying the product's rank with the smaller rank without considering the intersection.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ties-to-even binary rounding.

The value 1.101₂ lies halfway between 1.10₂ and 1.11₂. The retained least significant bit in 1.10 is zero, so ties-to-even selects A. B chooses the odd last bit; C and D are not the adjacent nearest values.

**Common misconception:** Always rounding an exact halfway case upward.

## Q18

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Blocking message-queue operations.

A receive frees capacity and may enable a sender, giving A. A blocked process need not spin, giving C. Applications can deadlock through cyclic waits even with bounded queues, so B is false. Finite capacity directly refutes D.

**Common misconception:** Mistaking a useful synchronization mechanism for a guarantee of application-wide progress.

## Q19

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Self-selection and causal direction.

People already inclined to exercise might choose locations near parks. This is the alternative causal direction described by B. Different measurement units (A) do not invalidate association; C reverses the reported association without justification; D denies the very selection mechanism identified.

**Common misconception:** Assuming location was assigned independently of residents' preferences.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Directory-link count versus open references.

Removing the two links removes names but the open descriptor still keeps the file available. Closing the last descriptor then leaves no links or open references, permitting reclamation, B. A leaves both a link and an open reference; C and D do not remove the remaining reference.

**Common misconception:** Equating removal of a filename with immediate destruction of an open file's storage.

## Q21

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Inessential variables through equal cofactors.

The given equality makes both z-cofactors identical, proving A. Set z=0 to obtain a function of x,y that equals F everywhere, proving B. F=x is a nonconstant counterexample to C and can be written without z, refuting D.

**Common misconception:** Interpreting independence of one variable as independence of every variable.

## Q22

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reliability above a datagram service.

Transport can track missing bytes, retransmit and reorder received bytes, giving A and B. It cannot prevent every physical error (C), and simultaneous application endpoints still need identification (D).

**Common misconception:** Equating recovery from lower-layer errors with prevention of those errors.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Chained necessary conditions.

A has a symbol but only seven characters, violating the second rule. B triggers neither antecedent. C satisfies the symbol-length requirement without needing a digit. D satisfies both implications. Thus only A necessarily violates a rule.

**Common misconception:** Treating a sufficient antecedent as a required feature of every valid password.

## Q24

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lossless dependency-preserving BCNF decomposition.

The intersection is B, and B→BC determines all of R2, giving losslessness, A. A→B is enforced in R1 and B→C in R2, proving B. In R, B is not a superkey but determines C, so C is false. A is a key of R1 and B a key of R2; their nontrivial projected dependencies have key determinants, proving D.

**Common misconception:** Inferring BCNF for the original relation from BCNF of its components.

## Q25

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: asynchronous I/O notification. Completion can raise an interrupt for the CPU (A). B destroys processor state; C corrupts addressing; D prevents useful transfer activity. None is a completion-notification mechanism. DMA transfers data independently but can still notify software when done.

## Q26

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: poisoned reverse. A advertises infinity back to the neighbour it uses as next hop for D, discouraging B from routing D through A. C is correct. A advertises the selected cost without poisoning; B advertises an unselected direct alternative rather than the specified poisoned route; D is not a distance-to-D advertisement. Poisoning is neighbour-specific.

## Q27

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: mean value theorem and continuity of f′. On [0,1/2] the secant slope is 2/(1/2)=4, proving A. On [1/2,1] it is (1−2)/(1/2)=−2, proving C and disproving B. The derivative is continuous and takes both signs, so it equals zero between those two interior points, proving D. The whole-interval secant slope alone would hide both the rise and the fall.

## Q28

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: recognizable reachability and reduction. Simulation accepts upon entering PRINT, establishing A. Simulating an arbitrary machine/input and entering PRINT iff it halts reduces halting to this property, establishing C. No universal fixed simulation bound exists, so B is false. If the complement also had a recognizer, dovetailing both would decide the property, contradicting C; D is false. A finite machine description does not bound its halting time.

## Q29

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: SQL NULL constraint semantics. For (NULL,−5), the CHECK evaluates UNKNOWN rather than FALSE, and MATCH SIMPLE skips the foreign-key lookup. UNIQUE permits NULL-containing duplicates under the stated rule. Thus A and C hold. B wrongly treats UNKNOWN as a rejection; D fails because non-null (1,1) requires a referenced row and none exists. All three constraint semantics were explicitly specified to avoid database-specific ambiguity.

## Q30

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Opposite faces and vertex incidence after folding a cube net.

The four squares A,B,C,D wrap around the cube as a belt. Positions two apart in this belt are opposite: A opposite C, and B opposite D. The two remaining squares E,F close the top and bottom and are opposite. A,B,E take one face from each opposite pair and meet at a vertex. Thus A is correct. B incorrectly makes adjacent B,C opposite and its proposed triple includes opposite A,C. C has the correct opposite pair E,F, but its proposed triple includes opposite A,C. D gives a wrong opposite pair A,D and a triple containing opposite E,F.

**Misconception:** Using distance on the flat net instead of adjacency on the folded cube.

## Q31

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

No required item can be a counterexample when Required is empty, so both candidates qualify: B is true and A false. C expresses precisely the absence of a missing requirement. Completed's x-projection is empty, which would remove both candidates from consideration; D is false. Universal conditions require a separately specified candidate domain, especially when the requirement set is empty.

## Q32

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A PDA can match the a and b blocks of L1 and then ignore the c count; similarly L2 matches b and c, proving A. Simultaneously satisfying both equalities forces all three counts equal, proving B. This intersection is the standard non-context-free three-equal-block language, disproving C. Context-free languages are closed under union, so D is true. Closure under union must not be confused with closure under intersection.

## Q33

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For fixed i, the inner work is1+2+4+...+2^floor(log2 i), which lies between i and2i. Summing over i=1..n givesΘ(n²), so B is correct. A counts doubling iterations but ignores their growing work; C multiplies by a spurious log factor; D ignores the outer linear range. Geometric inner workloads must be summed, not bounded by their maximum at every iteration.

## Q34

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

y receives4 before x is replaced by9, so z=4+9=13. A and C are true. Ordinary value assignment does not alias variables, making B and D false. Propagation must respect which definition reaches each use.

## Q35

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At n=40 the expression is1600+40+41=1681=41², composite. Thus C supplies a counterexample. A and B are positive examples and cannot prove universality; D only establishes oddness in one case, which is not primality. One verified counterexample refutes a universal conjecture.

## Q36

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Forwarding normally creates a new link-layer header for the outgoing link, while IP destination remains end-to-end, proving A,D and disproving C. TTL is within the IPv4 header and affects its checksum, proving B. Different layers can legitimately change different fields at the same hop.

## Q37

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After locating the lower bound, linked leaves permit ordered scanning, proving A and disproving B. Separator values can also appear among leaf keys, so C is true. The links still require a starting leaf to be located, disproving D. Search navigation and sequential continuation are complementary.

## Q38

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both first operations are sends and require a receive that neither process has reached; A is true and B false. If Q receives first, it matches P's send, after which Q's send can match P's receive; C is true. A mutex can keep a needed partner from entering its communication sequence and does not create a receive, so D is false. Textual presence of matching operations is insufficient when blocking order prevents reaching them.

## Q39

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A matching without cd cannot perfectly match either odd triangle. Thus any perfect matching must use cd, after which edges ab and ef complete one; A,B are true. Each triangle is an odd cycle, so C is false. Covering all edges inside each triangle requires at least two of its vertices, hence at least4 overall; choosing b,c,d,e achieves4, refuting D. Matching and vertex-cover sizes need not agree in a nonbipartite graph.

## Q40

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If the complement were regular, complementing it again would make L regular, a contradiction; A is true. The union in B equalsΣ*, which is regular. C is false: for L={a^n b^n}, intersection with the infinite regular language a* is just{ε}. For D, if deleting a finite set made L regular, adding back the finitely many removed words would make L regular by closure under finite union; this is impossible. Nonregularity is not preserved under every intersection.

## Q41

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

304 validates reuse of the stored representation rather than supplying a replacement body; C follows. A confuses status metadata with content, B confuses validation with deletion, and D assumes a body that the validation response does not supply.

## Q42

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Let q=P(A∩B). The feasible interval is max(0,0.8+0.7−1)≤q≤min(0.8,0.7), or0.5≤q≤0.7. B chooses0.6 and D implies q=0.5, both feasible. A is below the lower bound. C would give q=0.5·0.7=0.35, also impossible. A conditional probability must be compatible with the other supplied probabilities.

## Q43

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Let a,b,c,d denote the truth statuses. The statements impose a=NOT b, b=NOT c, c=NOT d, d=a AND b. Since a and b are opposites, a AND b=0, so d=0, c=1, b=0, a=1. Exactly A,C tell the truth, option B. Options A,C,D list pairs inconsistent with these statuses. A liar's statement must be false, not merely unproved.

## Q44

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The minimum is2 root children, each with2 leaf children, each leaf with2 keys:2·2·2=8. The maximum is4·4·4=64. B gives the pair. A omits a branching level; C understates maximum fan-out; D overstates the minimum. Count data keys at leaves, not separator copies.

## Q45

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first p symbols are all a, so every permitted nonempty v consists solely of a's. Pumping down reduces only their count and leaves all p b's, proving A. B contradicts this location; C reverses the universal quantification required to refute the lemma; D violates |v|≥1. One convenient split is insufficient: the argument must cover all legal splits.

## Q46

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Each column is covered by two rows, so no implicant is essential (A). One row covers only two columns, requiring at least two rows. Both {P,R} and {Q,S} cover all four, proving C,D and disproving B. A row in one minimum cover is not necessarily present in every minimum cover.

## Q47

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The determinant is−1 independently of t, proving A. Multiplying L=[[1,0],[l,1]] by U=[[u,v],[0,w]] forces u=t,v=1,lt=1,and l+w=0. If t=0, lt=1 is impossible, so B is false. If t≠0, choose l=1/t,w=−1/t, proving C,D. Invertibility does not guarantee an LU factorization without pivoting.

## Q48

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The assessor must attend carefully to evidence while lacking a financial stake, so the intended quality is impartiality(B). A contradicts careful examination; C concerns competence, which is not specified; D introduces a predetermined negative conclusion, contrary to impartiality. “Disinterested” in this context does not mean “uninterested.”

## Q49

**Correct answer:** C

Candidates III, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I, II and omits valid candidate(s) III, IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

All legal pumped blocks have the form a^k with 1≤k≤p. After pumping, the counts are m=p+(i−1)k and n=p. For C, m=p+k>p, so positive m cannot divide p. For D, m=p+(p+1)k>p, with the same consequence. B leaves the original string, whose two counts are equal, inside L. A is not guaranteed to leave L: choose k=p−1, giving m=1 and n=p, and 1 divides p. This legal decomposition exists for every p≥2. A decomposition that fails for some exponent is not enough; here the successful choices force failure for every legal decomposition.

## Q50

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A blocking operation can suspend the caller, making the core available to another runnable process; B and C hold. The caller need not busy-wait, so A is false. An empty pipe with a writer still open may later receive data; emptiness alone does not establish EOF, refuting D.

