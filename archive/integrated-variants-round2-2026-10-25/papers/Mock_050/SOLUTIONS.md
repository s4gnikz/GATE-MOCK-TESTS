# Worked Solutions — Mock Test 050

## Q1

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Vocabulary in context

1. The reviewer supports the objective, so the endorsement is not withdrawn.
2. The requirement of a smaller pilot places a condition on that support. Here “qualified” means limited by reservations, rather than describing professional credentials.

- **A:** This contradicts the explicit condition.
- **B:** This captures support with a limitation.
- **C:** The context gives no information about credentials.
- **D:** Support remains; it has not been withdrawn.

**Common misconception:** A familiar word can have a contextual meaning unrelated to its usual professional use.

## Q2

**Correct answer:** 10

Concept: powers dividing a factorial. Multiples of two contribute six factors, multiples of four contribute three additional factors, and the multiple of eight contributes one more. Thus the exponent is floor(12/2)+floor(12/4)+floor(12/8)=6+3+1=10. Counting just the even factors misses their extra powers of two.

## Q3

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Monotonic threshold selection.

Any measurement above the higher threshold was also above the old one, so the new flagged set is contained in the old set, A. A strict increase (B) and newly flagging all previously unflagged items (C) contradict that inclusion. The set need not become empty, refuting D.

**Common misconception:** Assuming every threshold change strictly changes the selected set.

## Q4

**Correct answer:** 72

The original outside surface has6×9=54 unit faces. Removing the six face-centre cubes removes six old exposed squares, leaving48 exterior squares. Each removed face-centre cube exposes four side faces of neighboring remaining cubes; its inward neighbor is the removed central cube. These six disjoint sets add24 faces. The central removed cube has only removed face-centre cubes as neighbors, so it adds no further boundary against the remaining solid. Total48+24=72. Counting six new faces for every removed cube would count contacts between two removed cubes.

## Q5

**Correct answer:** 17

**Concept:** Applying an alternating recurrence.

The terms are 3,6,5,10,9,18,17. Six updates produce the seventh term, 17.

**Common misconception:** Repeating only one operation or counting the initial term as an update.

## Q6

**Correct answer:** 0.2857 (range 0.28565–0.28575)
**Concept:** Circular adjacency.

Fix one specified person to remove rotational symmetry. The other occupies one of seven remaining positions uniformly, and exactly two are adjacent. Probability is 2/7≈0.285714, rounding to 0.2857.

**Common misconception:** A circle has two adjacent positions around each seat, including the wraparound edge.

## Q7

**Correct answer:** B

B attaches both participial actions to the engineer, who also recommends closure. A makes “cracks” the grammatical subject of having inspected. C incorrectly attributes the recommendation to cracks and misattaches inspection. D explicitly reverses the inspector and inspected object. The introductory modifier must attach to the intended actor.

## Q8

**Correct answer:** 19.2

**Concept:** Repeated dilution.

Each withdrawal removes one fifth of the salt currently present. The initial three litres of salt therefore become 3×(4/5)²=1.92 litres in a restored total volume of ten litres. The percentage is 19.2.

**Common misconception:** Removing the same amount of salt on both withdrawals despite dilution.

## Q9

**Correct answer:** 25
**Concept:** Successive percentage changes.

Normalize the original price to 100. The increased price is 120 and the target is 90. The reduction is 30/120×100=25%, measured against the increased price.

**Common misconception:** The two percentage changes use different bases.

## Q10

**Correct answer:** B

**Concept:** Composition of a rotation and an offset reflection.

R sends(x,y) to(-y,x). Reflection about x=1 sends(u,v) to(2-u,v), so one pair T sends(x,y) to(2+y,x). Applying the pair twice gives T²(x,y)=(x+2,y+2), and four times gives T⁴(x,y)=(x+4,y+4). The final point is(6,5), option B. A incorrectly assumes the composition has order four. C is the result of a half-turn about the origin, which is not the specified composite. D is not obtained by the specified sequence; the intermediate points are(3,2),(4,3),(5,4),(6,5).

**Misconception:** Treating a rotation followed by an offset reflection as a rotation about the origin.

## Q11

**Correct answer:** 12

Move5 to the root and remove its old final slot, leaving[5,7,4,12,9,6]. Its smaller child is4, so swap to get[4,7,5,12,9,6]. At index3,5≤6, so stop. Indices2 and3 contain7 and5, summing to12. Deleting the array's first element by shifting would not implement heap deletion.

## Q12

**Correct answer:** B

The lookup finds the new binding for the reused endpoint, so B describes a possible misdelivery. A assumes unavailable historical mapping information. UDP supplies no universal transport sequence-number protection, disproving C. Expiration is local state management and cannot guarantee absence of delayed datagrams, disproving D.

## Q13

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

## Q14

**Correct answer:** A, B, D

**Concept:** Databases — Relational algebra

1. The product creates every candidate A paired with every required B. Subtracting R identifies a missing required pair; its A is excluded.
2. Originally only A=2 misses y, leaving 1. With empty S there are no missing pairs, so all candidate A values remain.
3. Adding (2,y) makes both candidates qualify. Adding z to S makes both fail because neither has a z pair.

- **A:** Only 1 is paired with every B in S.
- **B:** Universal coverage of an empty required set is vacuously true.
- **C:** The result becomes {(1),(2)}, not {(1)}.
- **D:** Both candidates lack z.

**Common misconception:** Division-like expressions include vacuous truth and candidate-domain restrictions.

## Q15

**Correct answer:** -24

**Concept:** Determinant from triangular factors.

det(L)=1 and det(U)=2×(−3)×4=−24. With no permutation sign to include, det(A)=−24.

**Common misconception:** Adding pivots rather than multiplying them.

## Q16

**Correct answer:** 2

Concept: existential guard plus universal restriction. x=1 has neighbours a,b, both in S; x=2 has only a; x=3 has c, which fails. Hence x=1,2 satisfy the predicate, count two. The existential clause excludes vacuous success for x values with no R tuple.

## Q17

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

F(x)=integral0^x 2t dt=x². Integrating again over[0,1] gives1/3, rounded0.3333. The outer integral is of the accumulated function F, not directly of f.

## Q18

**Correct answer:** 1.25

The stored integers are 46 and 28. Their sum 74 wraps modulo 64 to 10, which decodes as 10/8=1.25. The exact numerical sum is 9.25, outside the format's maximum 63/8. Wraparound is neither saturation nor rounding.

## Q19

**Correct answer:** B
**Concept:** Arithmetic versus logical shifts.

11111011 represents −5. Arithmetic right shift gives 11111101, which is −3; logical right shift gives 01111101, which is 125. B matches. A assumes truncation toward zero for the arithmetic shift; C,D fail to insert zero at the high bit for the logical shift.

**Common misconception:** Arithmetic right shift of a negative odd integer rounds toward negative infinity, unlike truncating integer division in some languages.

## Q20

**Correct answer:** 5
**Concept:** Copy-on-write allocation.

Begin with three physical pages. The parent's first write to logical page 0 adds one copy, and the child's write to page 1 adds another. The parent's second write to its already private page 0 adds none. Total physical pages: 3+1+1=5; logical page 2 remains shared.

**Common misconception:** A repeated write does not copy a page that is already exclusively owned.

## Q21

**Correct answer:** 0

The advertised right edge is 4200+600=4800, below the next unsent sequence5000. Therefore no new bytes fit in the current receiver window. Window shrinkage does not produce a negative allowance; the usable new-data allowance is clamped to zero. Already sent data and retransmission policy are separate issues.

## Q22

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

accept returns a separate connected socket, while the listening socket can keep accepting, D. A incorrectly replaces the listening endpoint; B confuses accepting with application data transmission; C wrongly couples the descriptors' lifetimes. Closing a connected endpoint does not inherently close the listener.

## Q23

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Availability of expressions across calls.

If neither operand can change, the expression value is preserved. A guarantees inaccessible unchanged locals; C supplies a direct effect proof. Unknown effects on mutable globals make B insufficient. D ignores definitions and side effects. Thus A,C hold.

**Common misconception:** Textual equality is only part of common-subexpression eligibility; intervening modifications matter.

## Q24

**Correct answer:** 6.6667 (range 6.66665–6.66675)

Concept: extremal median. Sort the observations. If the median is m, the three largest values sum to at least 3m and the other two are nonnegative. Thus m≤20/3. Values 0,0,20/3,20/3,20/3 attain the bound. Round to 6.6667; range 6.66665–6.66675. A median need not equal the mean.

## Q25

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The cycle cannot lie on any s-to-t walk, since no cycle vertex can reach t. Its repetitions therefore cannot lower the s-to-t cost, proving C; examples with no other negative cycles have finite distance, proving A. B incorrectly spreads its effect to all reachable vertices. D contradicts the stated existence of a path. A says “can,” not that other negative cycles are excluded.

## Q26

**Correct answer:** 16

**Concept:** Structure copying and pointer aliasing.

The array members are copied into t, but the pointer value is copied unchanged. Therefore t.p still points to s.a[0]. Setting t.a[0]=7 changes t's array; writing through t.p sets s.a[0]=9. Their sum is 16.

**Common misconception:** Expecting a copied pointer automatically to point inside the copied structure.

## Q27

**Correct answer:** 2484
**Concept:** Per-datagram overhead.

Each of three packets contains 800+8+20=828 bytes. Total is 3×828=2484. Headers are incurred three times because the application sends three separate datagrams.

**Common misconception:** Header overhead applies per packet, not once per application message.

## Q28

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Stability preserves the input order of equal-key records, proving A and C. It does not impose a complexity bound, so B is false. Sorting must generally reorder unequal keys, disproving D. Stability is a tie-order property.

## Q29

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A finite format has only finitely many representable numbers, whereas a real interval contains infinitely many inputs; rounding maps many distinct inputs to the same value, proving B and refuting A. Finite precision and binary fractional representation matter even within exponent range, proving C and refuting D. Being in range avoids one problem, not every rounding error.

## Q30

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

## Q31

**Correct answer:** 3

Only S→aSb introduces terminals, adding one a and one b per application. The target contains three of each, forcing exactly three applications. It is derivable by concatenating aabb and ab using SS, so the forced count is attainable. Extra SS and epsilon expansions cannot change the required terminal-producing count.

## Q32

**Correct answer:** B
**Concept:** Pipe endpoint lifetime.

End-of-file requires the pipe buffer to be empty and every write-end reference to be closed. Child II still owns one, so the read blocks. A ignores that inherited reference. C is not stream-read behavior. D concerns writing to a pipe with no reader, not this read operation.

**Common misconception:** The process that supplied the data is not necessarily the only process keeping the pipe open.

## Q33

**Correct answer:** 3

**Concept:** Matching bottlenecks and a construction.

The three vertices a,b,c together have only two neighbours, so at most two of them can be matched. Vertex d adds at most one match, giving an upper bound three. The matching a–1,b–2,d–3 attains it.

**Common misconception:** Inferring a perfect matching just because the two bipartition sides have equal size.

## Q34

**Correct answer:** 11

Every directed edge contributes once to outdegree and once to indegree, including a loop. Thus both total degrees equal the edge count11. A loop does not contribute twice to either separate directed degree. The six-vertex count and number of loops do not alter the identity.

## Q35

**Correct answer:** 2

**Concept:** Memory bank selection.

Four chips are needed: 64/16=4. Each chip uses fourteen internal address bits for its 16 KiB locations. The full memory needs sixteen address bits, leaving two to select one of four chips.

**Common misconception:** Confusing data width with address depth.

## Q36

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

F selects y when x=1 and z when x=0. Therefore the two cofactors agree exactly when y=z, proving A. Expanding B's product gives xy+(NOT x)z+yz; the consensus term yz is redundant, so B holds. C fails with x=0,y=1, where F=z. When y=NOT z, F equals z for x=0 and NOT z for x=1, hence F XOR z=x: D. Treating the selector as an ordinary OR input obscures these dependencies.

## Q37

**Correct answer:** A, B, D

A displaced key's probe chain can cross a deleted slot, so turning it into EMPTY would terminate search prematurely(A). Remembering a tombstone while checking the remaining chain avoids duplicate insertion and allows reuse(B). Searches must continue past tombstones, disproving C and explaining the added unsuccessful-search work in D. Deleted and never-used slots have different historical meanings.

## Q38

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

## Q39

**Correct answer:** 4 (exact)

**Concept:** Compiler Design — Syntax-directed translation

The postfix code is `a b + c d e * + *`. Stack depths after successive tokens are 1, 2, 1, 2, 3, 4, 3, 2, 1. The maximum is 4. Equivalently assign a leaf peak 1 and a binary node peak max(left.peak, 1 + right.peak): the left result must remain on the stack throughout evaluation of the right subtree.

**Common misconception:** Expression-tree height alone does not give stack depth without the operand evaluation order.

## Q40

**Correct answer:** 520
**Concept:** MTU budgeting across headers.

Each packet can carry 1280−20−20=1240 application bytes. Two full packets carry 2480 bytes, leaving 3000−2480=520 for the final packet. Headers are outside that requested payload size.

**Common misconception:** TCP payload and total IPv4 packet size are not interchangeable.

## Q41

**Correct answer:** 2

Stack height begins at1, increases by1 on a and decreases by1 on b. An accepted length-five word needs two a's and three b's, with the height positive at every proper prefix. The only such words are aabbb and ababb. Other permutations empty the stack too early, preventing further input consumption. Final count balance alone is insufficient.

## Q42

**Correct answer:** 1

Each of T's two rows with key 1 matches U's single key-1 row, giving two joined rows with non-NULL U.k; both fail the WHERE filter. T's NULL does not equal U's NULL, so it generates one NULL-extended unmatched row, which passes. The result has one row. SQL equality on two NULLs is UNKNOWN, not TRUE.

## Q43

**Correct answer:** B

**Concept:** Closures and environment lifetime.

F and G need separate cells associated with their separate outer activations, and those cells must remain alive while captured. B provides both identity and lifetime. A wrongly merges cells, C leaves dangling references, and D implements caller-dependent lookup rather than lexical capture.

**Common misconception:** Assuming every local variable's lifetime must end when its defining call returns.

## Q44

**Correct answer:** A, D

Inclusion would be violated if an evicted L2 block remained in L1, so a corresponding L1 invalidation can be needed, proving A. L2 can contain blocks absent from L1, refuting B. Exclusivity forbids simultaneous copies, refuting C. Inclusive replication consumes slots without adding distinct blocks, proving D. The policies constrain contents, not merely replacement order.

## Q45

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The two unequal(a,b) assignments give the two products in A, independent of c,d. Each leaves two variables free and covers four inputs, proving C. Their eight inputs do not form one cube: spanning01 and10 while omitting a,b would also cover00 and11 zeros. Thus B and D are false. Power-of-two cardinality is necessary but not sufficient for a valid Karnaugh group.

## Q46

**Correct answer:** 3

All first-sequence blocks map to set0; cycling through three blocks in two LRU ways makes every one of its six references miss. The second sequence maps0 and6 to set0 and3 to set1; all three fit, producing only the three compulsory misses. Difference6−3=3. Total cache capacity is insufficient to predict misses without set placement.

## Q47

**Correct answer:** 1

The semaphore serializes both complete read-modify-write operations. Each increments x exactly once, and the third critical section changes no data. Every completed execution ends with x=2, so there is exactly one distinct final value. The requested count of possible results is1, not the result2 itself.

## Q48

**Correct answer:** 7

**Concept:** A worst-case resource deadlock bound.

With six resources, each process can hold two and wait for its third, producing deadlock. With seven, if all three are unfinished, at most six can be held while each remains short of its maximum; a free instance then permits some waiting process to reach three and finish. After it releases resources, the remaining processes can similarly progress. Equivalently the sufficient bound is Σ(max_i−1)+1=3×2+1=7, and the six-instance construction proves minimality.

**Common misconception:** Requiring all maximum demands simultaneously, or counting scheduling starvation as resource deadlock.

## Q49

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: SQL NULL constraint semantics. For (NULL,−5), the CHECK evaluates UNKNOWN rather than FALSE, and MATCH SIMPLE skips the foreign-key lookup. UNIQUE permits NULL-containing duplicates under the stated rule. Thus A and C hold. B wrongly treats UNKNOWN as a rejection; D fails because non-null (1,1) requires a referenced row and none exists. All three constraint semantics were explicitly specified to avoid database-specific ambiguity.

## Q50

**Correct answer:** 700

Concept: gap placement with repeated symbols. First arrange BBBCCC in 6!/(3!3!)=20 ways. The six symbols create seven gaps, including ends. Choose three distinct gaps for one A each: C(7,3)=35. Total=20·35=700. Identical A symbols are not separately permuted; multiple As in one gap would violate the restriction.

## Q51

**Correct answer:** 40
**Concept:** Fixed-width rotation composed with XOR.

45 is 101101. Rotating left two places yields 110110; XOR 001111 gives 111001 (57). Rotate that left two places to obtain 100111; XOR 001111 gives 101000, which is 40. Both rotations stay within six bits.

**Common misconception:** Rotation wraps discarded high bits into low positions, whereas a shift would discard them.

## Q52

**Correct answer:** B
**Concept:** Cumulative acknowledgments with reordering.

Until bytes 1000–1099 arrive, byte 1000 remains the first missing byte, so each of the first three ACKs is 1000. Once that segment arrives, buffered data make all bytes through 1399 contiguous, so the ACK advances to 1400. B matches; A,C,D incorrectly acknowledge across a gap or ignore buffered data.

**Common misconception:** Duplicate ACKs can result from reordering without actual packet loss.

## Q53

**Correct answer:** 32

Values are a0=1,a1=1,a2=2,a3=4,a4=8,a5=16,a6=32. For n≥2, subtracting consecutive prefix-sum recurrences gives an=2a(n−1). The doubling begins after the exceptional initial pair.

## Q54

**Correct answer:** 6

**Concept:** Preemptive shortest-remaining-time scheduling.

Run J1 on [0,1), J2 on [1,2), J3 on [2,3), J2 on [3,6), then J1 on [6,12). Waiting times from completion−arrival−burst are J1:12−0−7=5; J2:6−1−4=1; J3:3−2−1=0. Total six.

**Common misconception:** Comparing original burst lengths rather than remaining lengths after preemption.

## Q55

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A→D→C already implies AB→C, so deleting AB→C preserves the closure and A is true. Starting from C without C→B reaches no other attribute, so that dependency is not redundant and B is false. A determines D,C,B and is minimal as a singleton, making C true. D reaches C,B but not A, so D is false. Testing redundancy requires closure under the set with the tested dependency removed.

## Q56

**Correct answer:** 800

**Concept:** Cycle stealing as lost issue opportunities.

There are 1000/5=200 stolen cycles. Each removes exactly one otherwise productive cycle, leaving 1000−200=800 completed instructions.

**Common misconception:** Adding a second penalty beyond the one opportunity loss explicitly specified.

## Q57

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

q points to the pointer variable p, so(*q)++ changes p from a+1 to a+2. Then **q names a[2], while*(p−1) is a[1]=4. The update changes a[2] from6 to10; p−a is2. C is correct. A omits both updates, B fails to update p's position, and D adds the wrong array value. Parentheses distinguish incrementing a pointer through another pointer from incrementing an array element.

## Q58

**Correct answer:** A, B

For each i the inner loop visits i,2i,…,floor(n/i)i, proving A. The total is bounded above by nH_n and below by nH_n−n, hence Θ(n log n), proving B and refuting D. Only loop counters and constant-size state are needed; no array of iterations must be stored, so C is false. Counting the inner loop as n iterations independently of its stride overestimates the work.

## Q59

**Correct answer:** 174

View R as a3×3 zero-one matrix. Every row must be nonzero, giving7³=343 matrices. Exclude matrices with an all-one column. For each specified all-one column the other six entries are free, giving2^6=64; for each pair of such columns,2^3=8; for all three,1. Inclusion–exclusion gives3·64−3·8+1=169 excluded matrices. Hence343−169=174. Once a column is all-one, the row condition is automatically satisfied; imposing it again on the remaining columns would undercount.

## Q60

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Context-free languages are closed under intersection with regular languages, proving A. A regular language is context-free, and context-free languages are closed under union and concatenation, proving B,D. They are not generally closed under complement, so C is not guaranteed. The regularity condition on R is essential for the intersection guarantee.

## Q61

**Correct answer:** A

**Concept:** Vacuous pumping conditions for a finite language.

With p=8, no word in L has length at least p, so the condition holds vacuously. For any positive p≤7, word a⁷ is long enough; every valid pumped segment is nonempty, and pumping it twice produces a word longer than seven, outside L. Thus no smaller p works. A is correct, B,C fail this test, and D denies regularity of finite languages.

**Common misconception:** Assuming a pumping lemma must actually pump some word even when all words are shorter than its bound.

## Q62

**Correct answer:** 12

Concept: restored state in recursion. At each level the first branch contributes one to x and the second zero, with the increment restored before the second call. The eight leaves correspond to three binary choices; their x values are 3,2,2,1,2,1,1,0. Sum=12. Alternatively each of three levels contributes one at four leaves, giving 3·4. The global variable is restored across branches despite not being a local variable.

## Q63

**Correct answer:** 2

The cycles are0→1→3→0 and2→5→4→2. They partition all six indices, so there are2 cycles. The omitted residue6 maps to itself in the full modulo7 mapping but is not an array index here.

## Q64

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Rank is2 with three variables, so nullity is1: A true, D false. A consistent system's solutions are one particular solution plus that one-dimensional nullspace, an affine line, proving C and refuting B. Consistency does not imply uniqueness.

## Q65

**Correct answer:** 8 (exact)
**Concept:** Store-and-forward pipelining and packet-size optimization.

Let s=8(4000/n+100)/10⁶ seconds be transmission time on either slow link. The middle link takes s/2. The first packet arrives after 2.5s. Subsequent packets arrive every s because the slow links are the bottlenecks, giving T=(n+1.5)s.

Ignoring a positive constant factor, minimize (n+1.5)(4000/n+100)=4150+100n+6000/n. The continuous minimum is at n=√60, between 7 and 8. The function decreases before that point and increases after. Comparing 7 and 8 gives 100(8−7)+6000(1/8−1/7)<0, so 8 is the integer optimum. It divides 4000 and is therefore permitted. Its total time is 45.6 ms.

**Common misconception:** Smaller packets improve pipelining but increase total header overhead; neither one huge packet nor arbitrarily many small packets is automatically optimal.

