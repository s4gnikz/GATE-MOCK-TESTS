# Worked Solutions — Mock Test 059

## Q1

**Correct answer:** C

Concept: scope of evidence. The report explicitly permits average passenger delay to fall while average car time rises, so C follows. A replaces averages by a claim about every traveller; B asserts an unmeasured effect; D extrapolates one corridor to all corridors. Preserve both the population and the qualifier of a reported result.

## Q2

**Correct answer:** 36

**Concept:** Positional constraints on permutations.

The specified books occupy one of three position pairs: (1,3),(2,4),(3,5). Orient the two books in two ways, then arrange the other three in 3! ways. Total 3×2×6=36.

**Common misconception:** Treating the specified books as adjacent when exactly one intervening book is required.

## Q3

**Correct answer:** 45

Among respondents,120×0.75=90 support. The minimum occurs if none of the80 nonrespondents support, giving90/200=45%. The response rate prevents treating75% as a guaranteed percentage of the whole invited group.

## Q4

**Correct answer:** 17
**Concept:** Simultaneous remainders.

The positive numbers congruent to 2 modulo 5 begin 2,7,12,17. Their remainders modulo 7 are 2,0,5,3. The first qualifying number is 17; earlier positive candidates have been exhausted.

**Common misconception:** Satisfying one congruence does not satisfy the other automatically.

## Q5

**Correct answer:** A

R introduces the measurement, Q introduces repetition, P refers to that second measurement, and S draws the resulting decision. A has that sequence. B introduces repetition before the first measurement and delays its result; C begins with an unexplained second reading; D discusses a second reading before the repetition occurs. Pronoun references and cause–effect order constrain the sequence.

## Q6

**Correct answer:** 4.5

Card3 always contributes3. Each of cards1 and2 precedes card3 with probability1/2 and then contributes its label. By linearity, the expected sum is3+1/2+2/2=4.5. Independence between the inclusion events is unnecessary.

## Q7

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: contextual meanings and qualification. D uses impartial for disinterested, approved for sanctioned, and retains criticism of cost. A changes both meanings; B reverses approval and criticism; C incorrectly treats impartiality as loss of interest. Approval of a procedure need not endorse every aspect of it.

## Q8

**Correct answer:** 1

Put t=log2(x), so log4(x)=t/2. Then t²/2=8, giving t=4 or−4. Hence x=16 or1/16, whose product is1. Positive x does not imply a positive logarithm, so the negative t solution must not be discarded.

## Q9

**Correct answer:** A

Concept: confounding and comparison groups. A compares products with similar prior sales but differing advertising exposure, helping separate prior popularity from advertising. B provides labels without comparison data; C is irrelevant to the stated causal relationship; D removes the comparison group. A helps assess causality but does not alone establish a randomized causal effect.

## Q10

**Correct answer:** 12

**Concept:** Painted cuboid edges.

Exactly-two-face cubes occur along edges excluding corners. Four edges parallel to the length contribute 4(4−2)=8, four parallel to width contribute 4(3−2)=4, and four parallel to height contribute 4(2−2)=0. The total is 12.

**Common misconception:** Counting corner cubes, which have three painted faces.

## Q11

**Correct answer:** 0.25

**Concept:** Covariance with an indicator.

E[X]=3.5 and E[Y]=1/2. Only even outcomes contribute to XY, so E[XY]=(2+4+6)/6=2. Therefore Cov(X,Y)=2−3.5/2=0.25.

**Common misconception:** Assuming a function of X is independent of X.

## Q12

**Correct answer:** -8192

The minimum12-bit signed value is−2^11=−2048. Scaling by four bytes gives−8192. Signed range and displacement scaling are separate steps.

## Q13

**Correct answer:** 25

Concept: buddy rounding and internal fragmentation. Requests receive blocks of 16,32,8 KiB. Wasted space inside them is (16−9)+(32−17)+(8−5)=7+15+3=25 KiB. The remaining free eight KiB is not internal fragmentation inside allocated blocks.

## Q14

**Correct answer:** 5 (exact)
**Concept:** Updating first and second moments.

The original sum is 50. The remaining sum is 4×11=44, so the removed observation is 6. The original sum of squares is 5(8+10²)=540. Removing 6² leaves 504. New variance is 504/4−11²=126−121=5.

**Common misconception:** Variance cannot be updated using only the mean without tracking the second moment.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first receive discards DE under the given truncation rule. The next queued datagram is FG, which fits, so A is correct. B,C,D all incorrectly retain discarded bytes or combine separate datagrams. Datagram boundaries differ from stream byte buffering.

## Q16

**Correct answer:** 8

**Concept:** Directed adjacency entries.

Each directed edge is stored once, so eight edges require eight entries. Vertex headers are explicitly excluded; undirected doubling does not apply.

**Common misconception:** Automatically multiplying every adjacency-list edge count by two.

## Q17

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Don't-cares may be used to enlarge useful cubes, proving A, but they need not be covered, refuting B. OFF inputs must remain0, so C is true. Covering only don't-cares cannot satisfy an additional required ON input and is not mandatory, refuting D. Optimization freedom is not an additional output requirement.

## Q18

**Correct answer:** 4

**Concept:** Binary-search decision depth.

The balanced successful-search tree for fifteen entries has levels with 1,2,4,8 entries. A deepest entry needs four comparisons. The midpoint choice yields these exact sizes.

**Common misconception:** Using floor(log₂15)=3 without accounting for the first comparison level.

## Q19

**Correct answer:** 200 (exact)
**Concept:** HTTP connection reuse and parallel rounds.

The HTML costs one handshake plus one request-response: 80 ms. Each of three parallel image connections then costs 80 ms for its first image. Their second images need only another request-response, 40 ms. Total 80+80+40=200 ms.

**Common misconception:** Persistent connections save the second handshake, but non-pipelined dependent requests still consume another RTT.

## Q20

**Correct answer:** A, C

Every equal-block string belongs to a*b*, but L is the standard nonregular equal-count language while R is regular. Thus A,C are true. This example disproves B; L is infinite, disproving D. Regular supersets may contain nonregular subsets.

## Q21

**Correct answer:** 4
**Concept:** Exhaustive Boolean complement combinations.

For any x,y, the four argument pairs in the XOR are exactly 00,01,10,11 in some order. AND is 1 on exactly one of them. Therefore their XOR is always 1, on all four assignments.

**Common misconception:** Complementing both coordinates produces the full input table here, not four independent unknown values.

## Q22

**Correct answer:** 5

The initial root-to-leaf path costs three reads. Each of the two leaf-link advances costs one additional leaf read. Total5. Repeating a root search for every leaf would overcount under the specified linked traversal.

## Q23

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The entire five-character input matches ID, so maximal munch selects one identifier(B). The shorter initial match IF loses despite keyword priority, which applies only on equal-length matches. A,C split before the longest match ends; D contradicts the permitted digits after the first letter. Token priority and longest-match selection serve different roles.

## Q24

**Correct answer:** 8

p++ advances by one entire three-int row. Thus (*p)[1]=5 and p[-1][2]=3, summing to8. Pointer arithmetic scales by the pointed-to row type.

## Q25

**Correct answer:** 4

Successive powers modulo 10 are 2,4,8,6. The first identity value 6 occurs at exponent 4. The identity of this group is 6 rather than the integer 1; using the ambient multiplication identity would incorrectly suggest no finite order.

## Q26

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Probe-cycle length.

The visited slots are 1,5,9,3,7, then 1 again. The period is 10/gcd(10,4)=5. Hence B holds: empty even slots cannot be reached. A and C give incorrect period lengths. D is false because the arithmetic sequence is independent of table contents.

**Common misconception:** Assuming every nonzero step visits the entire table.

## Q27

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Matching, vertex cover and bipartiteness.

Edges {a,2},{b,3},{c,1} give a size-three matching. No matching exceeds the smaller side's size three, proving A. The side {a,b,c} is a vertex cover, disproving B. The graph remains bipartite and has edges, so its chromatic number is exactly two, proving C. A matching cannot cover an odd number of vertices, refuting D.

**Common misconception:** Deleting selected cross-edges does not necessarily reduce maximum matching size.

## Q28

**Correct answer:** 37

**Concept:** Logical shift and unsigned interpretation.

10010110₂ shifted right twice with zero fill becomes 00100101₂, equal to 32+4+1=37.

**Common misconception:** Sign-extending as if an arithmetic shift had been requested.

## Q29

**Correct answer:** 4

Start with{1,2,3}, sum6. Replacing any chosen i by i+3 adds3 and flips parity. The sum is even when the number of replacements is even: choose0 or2 of the three pairs, giving1+3=4 subsets. Selecting exactly one from each pair is a constraint separate from selecting three arbitrary elements.

## Q30

**Correct answer:** 3
**Concept:** Postorder expression translation.

The parenthesized sum yields `a b +`; unary minus then appends `neg`; multiplication appends `c *`. The full sequence is `a b + neg c *`, leaving three tokens before neg.

**Common misconception:** A unary operator in postfix still follows its entire operand expression, not merely the first identifier.

## Q31

**Correct answer:** 3

Recoverability requires commit(T1) before commit(T2). Exactly half of the six permutations have this order:123,132,312. T3 may be before, between or after the dependent pair. Read-from dependencies constrain commit order even when a third transaction is independent.

## Q32

**Correct answer:** 12
**Concept:** An inessential Boolean variable.

Each of the six qualifying four-variable assignments permits either value of the fifth variable. The count doubles to 12.

**Common misconception:** Independence from an input means both values replicate each output-table entry.

## Q33

**Correct answer:** A, C

**Concept:** Computer Networks — Layering

1. Ordinary routing keeps the end-to-end IPv4 destination and TCP port unchanged.
2. Forwarding decrements TTL and constructs an Ethernet frame for the outgoing LAN's next hop.
3. Therefore A and C hold; the incoming and outgoing link-layer destinations need not match.

- **A:** No address translation occurs.
- **B:** The outgoing frame addresses the next hop on a different LAN, not necessarily the incoming destination MAC.
- **C:** The stated assumptions ensure ordinary forwarding with a one-hop decrement.
- **D:** TCP ports identify endpoints; a transit router does not replace them.

**Common misconception:** Link-layer next-hop addressing must be distinguished from end-to-end addressing.

## Q34

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The lemma's requirement concerns language words at least as long as the pumping length. None exist at length≥21, so the implication is vacuously satisfied, giving C. A,B invent long words or substrings. D incorrectly excludes finite regular languages from the condition.

## Q35

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Alternation gives each simulation unbounded progress, so an acceptance by either is eventually observed: A,C are true. Both may run forever without acceptance, disproving B. The acceptance rule is either, not both, so it neither implements intersection nor guarantees a decision; D is false.

## Q36

**Correct answer:** 0.5333 (range 0.53325–0.53335)

**Concept:** Exponential races and memorylessness.

The first event time min(X,Y) is exponential with rate 5, with mean 1/5. Conditional on X winning the race, the first-event time retains this distribution: its conditional density is 5e^(−5t). By memorylessness, Y's remaining time then has mean 1/3. Under X<Y, the maximum is Y, so its conditional mean is 1/5+1/3=8/15=0.533333…. Accepted range: 0.53325–0.53335.

**Common misconception:** Using the unconditional mean of Y after conditioning on Y being the later event.

## Q37

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The parent retains its three threads. Only the calling thread is replicated into the child, which therefore starts with one thread. B is correct; A,C,D have incorrect thread counts. A copied address space can contain synchronization objects representing the old multithreaded state, but this does not recreate the other threads.

## Q38

**Correct answer:** 4

**Concept:** Recursion-tree argument sizes.

The root 10 splits equally into 5,5. Each 5 splits unequally into 2,3. Each 2 splits equally into 1,1; each 3 splits unequally into 1,2. Thus the two size-5 calls and two size-3 calls are exactly the unequal splits, totalling four.

**Common misconception:** Counting only distinct odd lengths instead of separate calls with those lengths.

## Q39

**Correct answer:** 896

Encoded widths are3 for eight choices,3 for five choices and4 for arbitrary enable subsets, total10. Horizontal width is8+5+4=17. Saving7 bits per word across128 words gives896 bits. Independent enables cannot be reduced to the logarithm of four because all16 subsets must be representable.

## Q40

**Correct answer:** 32
**Concept:** Leaf splitting and separator maintenance.

Insert 15 into the left leaf to obtain [5,10,15]. Inserting 12 overflows it to [5,10,12,15], which splits into [5,10] and [12,15]. The root separators become 12 and 20. Inserting 30 changes the last leaf to [20,25,30] without splitting or changing its minimum. The root separator sum is 12+20=32.

**Common misconception:** A leaf split promotes a separator copy; the separator key remains in the leaf under the stated B+ tree rule.

## Q41

**Correct answer:** 2.5

The first link delivers packet1 at 1s and packet2 at 2s. The second link sends packet1 during1–1.5s, then waits for packet2, which it sends during2–2.5s. Completion is 2.5s. Different link rates prevent treating both links as sharing a single packet transmission time.

## Q42

**Correct answer:** 21

The first pass gives prefix sums[1,3,6,10,15,21]. The descending second pass subtracts the still-unmodified preceding prefix from each entry, reconstructing[1,2,3,4,5,6]. Its sum is21. If the second pass ran upward, preceding entries would already be changed and would not be the needed prefixes.

## Q43

**Correct answer:** 7

Concept: product states and distinguishability. Track a-count zero or one, together with length modulo three: six states. A second a enters one permanent sink. All seven are reachable. Different residues with the same count can be separated by a suitable suffix: only b symbols for count one, or one a plus enough bs for count zero. A zero-count state and a one-count state are separated by a suffix containing exactly one a that completes a multiple-of-three length for the zero-count state; it sends the other to the sink. Every nonsink state has an accepting continuation. Thus no states merge and seven is minimal.

## Q44

**Correct answer:** 4

Each binary projection contains every one of the four possible bit pairs. Their join therefore permits all2³=8 triples. Only four were originally present, giving4 spurious additional triples. Pairwise relationships cannot encode the original parity-like ternary restriction by themselves.

## Q45

**Correct answer:** 5

**Concept:** Parse trees and Catalan recurrence.

Let C(n) count trees with n leaves. C(1)=1, and splitting the root's ordered children gives C(n)=Σ C(i)C(n−i). Thus C(2)=1, C(3)=2 and C(4)=1×2+1×1+2×1=5.

**Common misconception:** Counting derivation schedules instead of distinct tree structures.

## Q46

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Engineering Mathematics — Propositional and predicate logic

1. E lets us follow an R-edge indefinitely from any vertex. Finiteness forces a repeated vertex, hence a directed cycle. Under T, a directed cycle yields a self-loop, contradicting I. Thus A and C have no finite nonempty model, irrespective of F.
2. B has a two-element model {u,v} with only R(u,v) and R(v,u). Every element has one successor; the relation is symmetric and irreflexive.
3. D has a singleton model {u} with R(u,u). It satisfies E, T and S; irreflexivity was not required.

- **A:** A finite successor chain repeats, and transitivity then violates irreflexivity.
- **B:** The two-element swap relation is a witness.
- **C:** Adding functionality cannot repair the E,T,I contradiction.
- **D:** The singleton reflexive relation is a witness.

**Common misconception:** Finiteness changes satisfiability: an irreflexive transitive relation can have successors everywhere on an infinite ordered domain.

## Q47

**Correct answer:** 3

t saves C. Then B.next becomes E, and D.next becomes C, creating a separate C↔D cycle. From A the reachable chain is A→B→E→NULL, containing3 distinct nodes. The newly created cycle is not reachable from the head.

## Q48

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Because g has nonzero constant term and degree 3, it cannot divide a monomial, establishing A. A burst of length at most 3 has the form x^k b(x), with nonzero constant term and degree(b)≤2. Since gcd(g,x)=1 and degree(b)<3, it cannot be divisible by g, establishing B. Polynomial division gives x^7+1 = (x^3+x+1)(x^4+x²+x+1), so a two-bit error seven positions apart is undetected, establishing C. The polynomial g itself is an undetected three-bit error, refuting D. Equivalently g(1)=1, so x+1 is not a factor and the universal odd-error guarantee does not hold.
- Original option A: True: a generator with constant term 1 and positive degree cannot divide a single monomial.
- Original option B: True: after removing the x^k shift, a burst of length ≤3 has degree below that of g.
- Original option C: True: g divides x^7+1, and multiplying by x^k only shifts the same error.
- Original option D: False: e(x)=g(x) has three nonzero coefficients and is undetected.

## Q49

**Correct answer:** 13

The rule attaches each next bit at the next higher binary position, so the leftmost bit is least significant. The value is1×2⁰+0×2¹+1×2²+1×2³+0×2⁴=13. The ordinary most-significant-bit-first interpretation gives a different number because it would multiply the old value by2 instead.

## Q50

**Correct answer:** 3

**Concept:** Consistency after combining dependent variables.

Put u=x+z. The distinct equations become u+ty=1 and tu+y=0. Their determinant is 1−t². For t≠±1 they have a solution, and x,z can split u arbitrarily. At t=1 the same left side would equal both 1 and 0; at t=−1 one equation's left side is the negative of the other's, but the right sides are incompatible. The consistent integer values are −2,0,2: three.

**Common misconception:** Declaring every singular coefficient matrix inconsistent, or failing to inspect the singular cases separately.

## Q51

**Correct answer:** 4

**Concept:** Address aliasing under incomplete decoding.

The low twelve bits are fixed to 0x123, and A15,A14 are fixed to 1,0. A13,A12 can independently be 00,01,10,11, producing addresses 0x8123,0x9123,0xA123,0xB123. All select the same location. There are four aliases.

**Common misconception:** Assuming every machine address bit is decoded uniquely by a chip.

## Q52

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A distinguishing future sequence disproves equivalence, so B is true. Equivalent Moore states must have equal current outputs and equivalent successors for each input, proving C. Equal output now alone leaves future behavior unconstrained, making A false. Encodings are internal labels, not external observations, so D is false.

## Q53

**Correct answer:** B

**Concept:** Per-activation storage.

Each active recursive call needs its own x, and stack activation records provide these separate slots with return-time reclamation, B. A overwrites older calls' values, C falsely forbids locals, and D ignores assignments to a variable.

**Common misconception:** Allocating one slot per function rather than one per active call.

## Q54

**Correct answer:** 3

**Concept:** Continuity required before derivative matching.

Differentiability implies continuity, so the left limit b must equal f(0)=1. The right derivative of e^(2x) at zero is 2. The left derivative of ax+b is a, hence a=2. Therefore a+b=3.

**Common misconception:** Matching slopes while neglecting the function-value continuity condition.

## Q55

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The OR evaluates its right operand exactly when its left operand is false. The left operand is false when x=0 or when x is nonzero and the quotient is at most 2, so A holds. For B use x=2,y=5,z=0: the original quotient is 2, so the original evaluates z++ and returns false, leaving z=1; the proposed comparison 5>4 is true, so it returns true without incrementing z. C is unsafe because x=0 would cause division by zero, an operation the original never evaluates. If x=0 the AND is false without division, so the right operand is evaluated and D follows. Side-effect freedom alone never justifies speculating an operation that can fail.
- Original option A: True: these are precisely the paths on which the left side of OR is false.
- Original option B: False: x=2,y=5,z=0 is a counterexample due to integer truncation and short-circuit effects.
- Original option C: False: the transformation introduces division by zero when x=0.
- Original option D: True: no division occurs, and the postfix increment is evaluated once.

## Q56

**Correct answer:** 5.75

The six-bit signed scaled range is−32..31, or−8..7.75 after dividing by4. The first sum is4.5, the second exact sum9 saturates to7.75, and the final subtraction2 yields5.75. Summing first and saturating only once would incorrectly give7. Saturation is applied after each operation as specified.

## Q57

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The duplicated and inherited descriptors refer to the same open file description under the stated semantics. Its offset is shared, so A,C are true and B false. Closing one descriptor drops one reference; other open references remain valid, refuting D. Descriptor-table entries and open file descriptions are distinct levels of state.

## Q58

**Correct answer:** 0.5

**Concept:** Rounding across an exponent boundary.

With three significant bits, 7 and 8 are adjacent representable values surrounding 7.5. The exact value is halfway. Ties-to-even selects 8 (1.00₂×2³), whose retained final bit is even; either nearest endpoint has absolute error 0.5, which is the requested quantity.

**Common misconception:** Assuming fixed spacing continues unchanged beyond the exponent boundary or reporting signed rather than absolute error.

## Q59

**Correct answer:** 1

Concept: relational anti-semijoin. π_A(R)={1,2,3}. Joining on B with {x,y} keeps the first three tuples and projects to {1,2}. Difference={3}, cardinality one. This selects A values having no match at all, not those failing to match every S value.

## Q60

**Correct answer:** 9
**Concept:** Exact insertion-sort comparison counting.

Inserting 1 compares against 5 once. Inserting 4 compares against 5 then 1: two comparisons. Inserting 2 compares against 5,4,1: three. Inserting 3 compares against 5,4,2: three. Total 1+2+3+3=9. Successful shifts and the final failed key comparison are both comparisons, but reaching the boundary adds no key comparison.

**Common misconception:** The number of key comparisons can exceed the number of shifts.

## Q61

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Dovetailing and enumeration of recognizable languages.

Dovetailing eventually performs every finite number of steps of every started simulation, so each accepting computation is eventually found (A). If L is finite, other simulations may loop forever and there is no general way to detect that no further member will be found; B is false. With L empty no simulation accepts, so an infinite silent run is possible (C). Waiting for a nonmember to print never terminates, refuting D.

**Common misconception:** An enumeration is evidence of membership when an item appears, not evidence of nonmembership when it has not yet appeared.

## Q62

**Correct answer:** 2.8

The common data access costs80 ns. The old average is2+80+0.05×160=90 ns. The new average is4+80+0.02×160=87.2 ns. The saving is2.8 ns. Account for the slower probe on every access, not just on misses.

## Q63

**Correct answer:** C
**Concept:** Limits of the unweighted interval greedy rule.

Earliest finish chooses A then C, then E rather than F because E starts earlier in the finish-time tie. Its weight is 12. For the optimum, the best compatible predecessor totals at A,B,C,D,E,F are 4,5,8,10,12,13. In particular B,D,F attain 13. Thus C gives (12,13). A misses the better weighted solution; B attributes it to the greedy rule; D miscounts the greedy choices.

**Common misconception:** Maximizing the number of compatible intervals does not maximize their total weight.

## Q64

**Correct answer:** 0.25

**Concept:** Exactly one transmitter.

Choose the transmitting station in four ways. Each specified one-transmitter outcome has probability (1/2)^4=1/16. Thus success probability is 4/16=1/4.

**Common misconception:** Counting a slot with two transmissions as two successes instead of a collision.

## Q65

**Correct answer:** 3

The first fork yields a parent with x=0 and child with x=1. Only the x=0 parent executes the second fork, producing one additional process. Each of the resulting three processes reaches the print once. Private x values prevent the first child's assignment from suppressing the parent's second fork.

