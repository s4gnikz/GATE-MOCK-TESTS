# Worked Solutions — Mock Test 096

## Q1

**Correct answer:** 3.2

Concept: weighted percentages. The two batches contain 300(0.02)=6 and 200(0.05)=10 defective units. Thus 100(16/500)=3.2%. Averaging the two percentages without their batch weights is incorrect.

## Q2

**Correct answer:** 17
**Concept:** Simultaneous remainders.

The positive numbers congruent to 2 modulo 5 begin 2,7,12,17. Their remainders modulo 7 are 2,0,5,3. The first qualifying number is 17; earlier positive candidates have been exhausted.

**Common misconception:** Satisfying one congruence does not satisfy the other automatically.

## Q3

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Q establishes the discrepant readings; S explains the diagnosis; P describes the repair; R gives the subsequent test. Thus Q,S,P,R is required. B uses “this discrepancy” before its referent and puts the second trial before repair. C diagnoses the defect after the repair and trial. D introduces repair before the problem. Follow explicit references and causal dependencies, not just grammatical possibility.

## Q4

**Correct answer:** 0.25

A6 is retained either on the first roll, probability1/6, or after an odd first roll and a6 on the second, probability(1/2)(1/6)=1/12. These disjoint cases sum to1/4. The reroll rule changes the distribution from a single fair die.

## Q5

**Correct answer:** B

The clause requiring revisions explicitly limits the panel's support, so qualified means conditional or limited, B. A uses another meaning of the word that is not intended here. C contradicts the stated support, and D contradicts the stated conditions. Context distinguishes a qualified endorsement from an unqualified one.

## Q6

**Correct answer:** 12

At time t hours the ratio is 2^(t/3)/3^(t/6)=(4/3)^(t/6). The target16/9=(4/3)² therefore occurs at t/6=2, or12 hours. Since the base4/3 exceeds1, the ratio increases strictly and this is the first such time. Comparing only the two named multiplication factors ignores their different time intervals.

## Q7

**Correct answer:** 16 (exact)
**Concept:** Counting orders satisfying cyclic inequalities.

All four assertions cannot be true, since they form a strict cycle; all four cannot be false for the same reason in reverse. Exactly three true assertions occur in four orders: choose which assertion is false, and the other three force a single chain. Reversing each order gives four orders with exactly one true assertion. The remaining 4!−4−4=16 have exactly two true assertions.

**Common misconception:** The four pairwise comparisons are constrained by transitivity, so their truth values are not independent coin tosses.

## Q8

**Correct answer:** 2

The first rotation leaves the original−x face pointing−x. The second positive y rotation maps−x to+z. Hence the original−x face ends upward, code2. Equivalently the composite maps(x,y,z) to(y,−z,−x), and solving for output(0,0,1) gives input(−1,0,0). The axes are fixed world axes, not changing body axes.

## Q9

**Correct answer:** -50

From a1 to a101 there are100 updates. Group them as(1−2)+(3−4)+...+(99−100). Each of50 pairs contributes−1, so a101=−50. There are100 increments, not101, because the initial term is already specified.

## Q10

**Correct answer:** 256

Concept: constrained optimization over integers. The volume is V(x)=x(20−2x)(12−2x). Positive dimensions restrict x to 1,2,3,4,5. Corresponding volumes are 180,256,252,192,100; the maximum is 256 at x=2. The maximizing integer must be checked rather than reporting an unconstrained stationary point.

## Q11

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Finite cancellation monoids.

Left multiplication by a is injective by cancellation and hence onto on the finite set (A). Thus some b satisfies ab=e. Now a(ba)=(ab)a=a=ae; cancel a to get ba=e. Every element has a two-sided inverse, proving B and D. Noncommutative finite groups, such as the permutations of three elements under composition, refute C.

**Common misconception:** Finiteness is crucial when converting an injective self-map into a surjective one.

## Q12

**Correct answer:** C

**Concept:** Databases — File organization

If the first record is at slot 0, the 16 records occupy two pages. If it starts at any slot 1 through7, the 16 consecutive records cross into a third data page. Thus at most three data pages are needed, and this is attainable. Add two index reads for a largest total of 5.

- **A:** False: this counts only the worst-case data pages and omits the index reads.
- **B:** False: it assumes the range begins exactly at a page boundary.
- **C:** True: three data pages plus two index pages attain the maximum.
- **D:** False: sixteen consecutive records cannot span four eight-record pages.

**Common misconception:** A contiguous record range can span one extra page because its first record need not be page-aligned.

## Q13

**Correct answer:** 4

**Concept:** Serialization delay.

A 1000-byte packet contains 8000 bits. At 2×10⁶ bits/s it takes 0.004 seconds, or four ms.

**Common misconception:** Dividing bytes by a bit rate without multiplying by eight.

## Q14

**Correct answer:** 12

**Concept:** Cache address decomposition.

There are 4096/64=64 lines, requiring six index bits. A 64-byte line needs six offset bits. The remaining 24−6−6=12 bits form the tag.

**Common misconception:** Counting the total data bytes as the number of cache lines.

## Q15

**Correct answer:** A, C

Linearity gives H(c+e)=Hc+He=He for a codeword c. Thus C is true. If e is a nonzero codeword, He=0 and the change is undetected, proving A and disproving B,D. A zero syndrome means code membership, not absence of error.

## Q16

**Correct answer:** 3

No singleton satisfies every factor: P misses(Q+R), Q misses(P+R), and R misses(P+Q). Each two-element subset satisfies all factors, giving covers{P,Q},{P,R},{Q,R}. Thus minimum cardinality is2 and three minimum covers exist. The three-element cover is valid but not minimum; repeated selections do not add new covers.

## Q17

**Correct answer:** 1.718 (range 1.7175–1.7185)
**Concept:** Mean value theorem.

The secant slope is (1−0)/(e−1). Since f′(c)=1/c, equality gives c=e−1=1.7182818… . This lies strictly between 1 and e and rounds to 1.718.

**Common misconception:** The mean value theorem point need not be the midpoint of the interval.

## Q18

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Transposition reverses product order, giving Aᵀ=UᵀLᵀ, so A is true. Set y=Lᵀx; solve Uᵀy=b first, then Lᵀx=y, proving C. Reversing those solves in B generally solves the wrong product because the factors need not commute. Transposing a unit lower-triangular matrix gives unit upper triangular, proving D.

## Q19

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. A base tree uses S -> aSb with the inner S -> epsilon.
2. Replace the root with S -> SS, placing the previous tree on one child and S -> epsilon on the other. The yield remains ab.
3. Repeating this operation creates arbitrarily large finite trees with the same yield, so their count is infinite.
- Original option A: The base tree is not unique; an empty sibling adds a second shape.
- Original option B: The construction can be repeated after two trees have been obtained.
- Original option C: There is no finite size bound on added empty siblings.
- Original option D: The unbounded family consists of distinct finite trees.

## Q20

**Correct answer:** A, C

The direct path costs 2, while s→b→a costs 5−4=1, proving A. Settling a at 2 before exploring b can prevent correction, proving C. The graph is acyclic, refuting B. Its shortest path to a has two edges despite an available one-edge path, refuting D. Negative edges, even without a negative cycle, invalidate the usual Dijkstra settling guarantee.

## Q21

**Correct answer:** 15
**Concept:** Static storage across recursive and successive calls.

During f(2), the three local a values are 1,2,3, yielding x=6. The static k remains 3. During f(1), the values are 4,5, yielding y=9. The printed sum is 15. Each invocation's local a retains its own value while k is shared across calls.

**Common misconception:** A static local is initialized once, not once per invocation or once per top-level call.

## Q22

**Correct answer:** 3

**Concept:** Stable ordering within equal keys.

The key-one records remain B,D, and the key-two records remain A,C. Output is (1,B),(1,D),(2,A),(2,C), placing A third.

**Common misconception:** Reordering equal-key records after sorting by the primary key.

## Q23

**Correct answer:** 4

Concept: priority encoding. Code 10 requires D3=0 and D2=1. D1 and D0 are arbitrary, giving 2²=4 patterns. Validity is automatically one because D2 is asserted. Lower-priority asserted inputs do not change the code.

## Q24

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

F(x)=integral0^x 2t dt=x². Integrating again over[0,1] gives1/3, rounded0.3333. The outer integral is of the accumulated function F, not directly of f.

## Q25

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

## Q26

**Correct answer:** 21

The parameter p is a copy of the caller's pointer. Inside change it advances from a+1 to a+3 and replaces a[3] by a[2]+a[3]=7+9=16. The caller's p still points to a[1], whose value is 5. Thus the print computes 5+16=21. Passing a pointer by value permits mutation of its target but does not permit rebinding the caller's pointer through the local parameter alone.

## Q27

**Correct answer:** 768

**Concept:** Burst count and occupied bus time.

The transfer has 4096/16=256 bursts. Each occupies three bus cycles, so occupied time is 256×3=768 cycles. No additional interburst delay is specified or requested.

**Common misconception:** Confusing elapsed transfer time with occupied bus cycles.

## Q28

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Array size versus string termination.

The stored bytes are 'a', an explicit null, 'b', 'c', and the implicit terminating null: five bytes. strlen stops at the first null and returns one. A gets both values wrong; C counts through the embedded null; D omits the implicit terminator from the array size.

**Common misconception:** Treating every byte of a character array as part of its C string.

## Q29

**Correct answer:** A

**Concept:** Leaf chains in B+ trees.

Sibling links allow a scan to continue directly to the next leaf, establishing A. B is not a B+ tree invariant; C describes no ordinary single-root B+ tree; D removes needed navigation separators and does not explain scanning.

**Common misconception:** Assuming every successive key retrieval must begin at the root.

## Q30

**Correct answer:** A, B, D

Popping Z on empty input accepts epsilon(A). Reading ab pushes X and then removes it, restoring Z; a final empty-input pop accepts(B). The same two-step cycle can repeat, accepting abab(D). On aabb, after the first a the top is X, and there is no move for another a, so C is rejected. Popping Z before input ends strands the remaining input and does not cause acceptance under the stated convention.

## Q31

**Correct answer:** 256

**Concept:** Buddy alignment and external fragmentation.

Offset0's256-byte buddy is offset256, which remains allocated. Offset512's buddy is offset768, also allocated. The two free blocks are not buddies and cannot coalesce. Thus there are512 free bytes in total, but the largest satisfiable single request is256 bytes.

**Misconception:** Equating total free space with the largest available contiguous buddy block.

## Q32

**Correct answer:** 1

The first edge recovers111→000. Six more edges advance six times modulo5, ending at001, value1. Directly treating111 as a modulo5 numeric state ignores the explicit illegal-state recovery transition.

## Q33

**Correct answer:** A, B

Both forms derive only ab and ac, proving A. FIRST(A)={b} and FIRST(B)={c}, so one lookahead selects an X alternative, proving B. The original S alternatives both start with a, making C false. Left factoring changes common-prefix decision structure but does not generally eliminate ambiguity, making D false.

## Q34

**Correct answer:** 0.25

**Concept:** Derivative of an inverse function.

Since f(1)=2, g(2)=1. Differentiate f(g(y))=y: g′(y)=1/f′(g(y)). With f′(x)=3x²+1, g′(2)=1/4.

**Common misconception:** Evaluating f′ at 2 rather than at g(2).

## Q35

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: attribute dependency ordering. X is the left child, but its inherited value depends on right sibling Y's synthesized attribute, violating the usual L-attributed restriction, A. Y is independent of X, so there is no forced cycle; compute Y.v first, then X.i, making C true and B false. Attribute dependencies do not establish syntactic ambiguity, so D is false. A valid evaluation order need not be the standard left-to-right attributed order.

## Q36

**Correct answer:** 11

**Concept:** Pipeline completion plus load-use stalls.

Five instructions in five stages take 5+5−1=9 cycles without stalls. The first load's consumer adds one stall, and the second load's immediate consumer adds another. The intervening ALU dependencies are forwarded, including the address dependency into the second load. Total 11 cycles.

**Common misconception:** Stalling for ALU dependencies already covered by forwarding, or omitting one load-use penalty.

## Q37

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: keys and lossless decomposition. C cannot be derived, so every key includes C. Either A or B then supplies the other; C supplies D. Exactly AC and BC are minimal keys (A). Determinants A,B,C are not superkeys of R, so B is false. Split off AB using A→B, leaving ACD; split that using C→D into CD and AC. Both binary splits are lossless, and AB preserves A→B and B→A while CD preserves C→D, so C is true. AB and CD alone lose the association between A and C: two original rows with distinct A and C values can recombine into four rows, so D is false. Dependency preservation alone does not prove losslessness.

## Q38

**Correct answer:** A, C

The order of x divides both4 and6, hence divides2, proving x²=e and C. It also divides the odd group order, so it cannot be2; its order is1, giving x=e and A. B,D contradict that order. The two exponent equations alone would allow order2; the odd-order hypothesis eliminates it.

## Q39

**Correct answer:** 2

The original orbit is2,10,6,2,... because gcd(8,12)=4. Those three slots are occupied. With step5 the probes begin2,7; slot7 is empty. Thus two probes suffice. A table can have free slots while a non-coprime probe step fails to reach them.

## Q40

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

## Q41

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

T3 is younger than holder T2, so wait-die aborts T3. T1 is older than T2 and is permitted to wait. This is B; A,D apply one rule indiscriminately, while C reverses the age comparison. The scenario specifies wait-die, not wound-wait.

## Q42

**Correct answer:** A, B, D
**Concept:** Lossy decomposition of ternary relationships.

All three original tuples survive. Their projections additionally support (s1,p1,j2): each of its three pairs appears somewhere. No other new tuple is possible: s2 has only p1 and j2, and pair (p2,j1) is absent. The join therefore has four tuples. Each original SP pair appears once and determines J. A,B,D hold; the spurious tuple itself refutes C.

**Common misconception:** Pairwise compatibility does not prove that a three-way combination occurred in the original relation.

## Q43

**Correct answer:** 18

Descending through three nonbase calls makes c=3; the base returns3. Unwinding, c becomes4 and returns3+4=7; then c=5 and return7+5=12; finally c=6 and return12+6=18. The shared counter is not restored on return.

## Q44

**Correct answer:** 513

The effective address is 100+12−8=104. Little-endian order places byte01 in bits 7..0 and02 in bits 15..8. The low16 bits are 0x0201=2×256+1=513. Computing the address and interpreting the byte order are separate steps.

## Q45

**Correct answer:** 7

f and g reference the same closure and captured x, so their first calls return1 and2. h has its own environment and returns1. The final f call advances the first environment to3. Sum1+2+1+3=7. Copying a closure reference is not creating a fresh capture environment.

## Q46

**Correct answer:** A, C

The duplicated and inherited descriptors refer to the same open file description under the stated semantics. Its offset is shared, so A,C are true and B false. Closing one descriptor drops one reference; other open references remain valid, refuting D. Descriptor-table entries and open file descriptions are distinct levels of state.

## Q47

**Correct answer:** 3

Compute t1=a+d, t2=b+c, result=t1*t2: two additions and one multiplication. The factorized expression has three binary internal nodes, each requiring an operation in this representation. Factoring is valid under the stated mathematical-integer semantics; machine overflow or floating-point reassociation would require separate justification.

## Q48

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Unsigned addition gives 0x80+0xFE+1=0x17F, so the low byte is 0x7F and carry C=1. Therefore A is true and B is false. Signed subtraction is −128−1=−129, outside [−128,127], so V=1 and D is false. Carry and signed overflow answer different questions.

## Q49

**Correct answer:** 1

Deleting e leaves six edges and retains connectivity on six vertices. A spanning tree needs five edges and exists in every connected graph, so one further appropriate edge removal suffices. Arbitrarily deleting a bridge would not be an appropriate choice.

## Q50

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Regular and context-free languages are closed under homomorphism, including erasing homomorphisms, so A,B are true. Erasing all symbols turns every string into ε; a nonempty input language therefore maps to{ε}, proving D and providing a counterexample to C. Homomorphisms can discard the structure responsible for nonregularity.

## Q51

**Correct answer:** 266240

**Concept:** Direct and indirect addressing capacity.

The indirect block stores 1024/4=256 data-block pointers. Together with four direct pointers, the inode addresses 260 data blocks, or 260×1024=266240 bytes. The indirect block itself is metadata and is not another file-data block.

**Common misconception:** Counting the pointer block as part of addressable file content.

## Q52

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

## Q53

**Correct answer:** 700

Concept: gap placement with repeated symbols. First arrange BBBCCC in 6!/(3!3!)=20 ways. The six symbols create seven gaps, including ends. Choose three distinct gaps for one A each: C(7,3)=35. Total=20·35=700. Identical A symbols are not separately permuted; multiple As in one gap would violate the restriction.

## Q54

**Correct answer:** 15.9375

The stored signed integer runs from−128 to127. Scaling gives endpoints−8 and127/16=7.9375, so the interval width is7.9375−(−8)=15.9375. There are256 representable points but only255 gaps between the extreme values. Confusing point count with interval width gives16 incorrectly.

## Q55

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The regular pumping lemma requires0<|y| and |xy|≤p, so1≤d≤p, proving A. Pumping to two copies adds d to p², and0<d≤p<2p+1 is smaller than the next-square gap. Thus B is true and the pumped word is outside L for every permitted decomposition. C violates the nonempty requirement. D is false since p²≥p for p≥1. The gap argument handles all decompositions, not one chosen substring.

## Q56

**Correct answer:** 1

Close-on-exec is a descriptor flag. Descriptor3 is closed by successful exec, while descriptor4 was not flagged and remains. Both initially referred to the same open-file description, but their flags are distinct. One descriptor remains.

## Q57

**Correct answer:** 0.25

**Concept:** Exactly one transmitter.

Choose the transmitting station in four ways. Each specified one-transmitter outcome has probability (1/2)^4=1/16. Thus success probability is 4/16=1/4.

**Common misconception:** Counting a slot with two transmissions as two successes instead of a collision.

## Q58

**Correct answer:** 9

**Concept:** Synchronous distance-vector updates with stale information.

Using initial (1,2,2), round one yields A=min(1+2,1+2)=3, B=min(1+1,1+2)=2, C=2. From (3,2,2), round two yields A=3, B=min(4,3)=3, C=3. The sum is nine. Every router uses the same previous-round snapshot, not updates already computed within the current round.

**Common misconception:** Mixing synchronous rounds with sequential in-place updates or silently applying poison reverse.

## Q59

**Correct answer:** 32

Values are a0=1,a1=1,a2=2,a3=4,a4=8,a5=16,a6=32. For n≥2, subtracting consecutive prefix-sum recurrences gives an=2a(n−1). The doubling begins after the exceptional initial pair.

## Q60

**Correct answer:** 4
**Concept:** Packet scheduling when paths diverge.

On S→R, A occupies 0–1 ms, B 1–2, and C 2–3. On R→D, A occupies 1–2; B does not use this link. C is unavailable until time 3, so it occupies 3–4. Arrival completes at 4 ms.

**Common misconception:** An idle downstream link cannot forward a packet before the upstream transmission finishes.

## Q61

**Correct answer:** 5.375
**Concept:** Synthesized attributes for positional notation.

The integer part evaluates as ((1×2)+0)×2+1=5. For the fraction, process the right recursion from its epsilon base: the final 1 gives 1/2; the preceding 1 gives (1+1/2)/2=3/4; the initial 0 gives (0+3/4)/2=3/8. The complete value is 5+3/8=5.375.

**Common misconception:** Fractional digits are weighted by decreasing powers of two; their recurrence differs from the integer-part recurrence.

## Q62

**Correct answer:** 8

**Concept:** Pointer-to-row indexing.

p+1 points to the second three-element row; *(*(p+1)+2) is its third element, 6. (*p)[1] is the second element of the first row, 2. Their sum is eight.

**Common misconception:** Advancing a pointer-to-array by one integer instead of by one full row.

## Q63

**Correct answer:** 4

After successive iterations, (slow,fast) is(1,2),(2,4),(3,2),(4,4). The first tested equality is at node4. Initial equality is deliberately not tested, and the meeting point need not be the cycle entrance node2.

## Q64

**Correct answer:** 8

With four significant binary bits, representable values near8 are8=1.000×2³ and9=1.001×2³, spacing1. The exact sum8.5 is halfway; ties-to-even picks8 because its trailing significand bit is0. The second addition again rounds8.5 to8. Thus the result is8, although performing the exact sum first would give9. Rounding after each operation is consequential.

## Q65

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: Boolean sensitivity. F(0,y,z)=yz; F(1,y,z)=y+z. Their XOR is one exactly when y and z differ, giving y XOR z (B). The substituted expression has no x (C). A fails at y=z=1 because the difference is zero but OR is one; D fails at y=1,z=0 because the difference is one but AND is zero. Boolean difference uses XOR, not ordinary subtraction.

