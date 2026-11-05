# Worked Solutions — Mock Test 085

## Q1

**Correct answer:** B

The stated order is archive, recalibrate, repeat, compare. Among those events, repeating directly precedes comparison, so B. A,C are earlier, and D never occurs in the account. The question concerns the narrated event ordering, not whether unmentioned activities occurred between them.

## Q2

**Correct answer:** 2.5

The red ball's position is uniform among1,2,3,4, and that position equals the stopping draw count. The mean is(1+2+3+4)/4=2.5. Sampling stops at the red ball but does not bias its initial random position.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: vocabulary in context. Restoring the previous configuration undoes the change, which is B. A is the opposite meaning; C asserts repetition, which reversibility does not require; D contradicts restoration of the previous state. Use the sentence's definition rather than an association with the prefix alone.

## Q4

**Correct answer:** A

The required numerical answer is **2**, so select **A**.

Let the common floor be k≥0. The integer must lie in both[2^k,2^(k+1)) and[3^k,3^(k+1)). For k=0 only x=1 qualifies; for k=1 only x=3 qualifies. For k≥2,3^k≥2^(k+1), since9>8 and the ratio grows by3/2 each step. The intervals are disjoint thereafter. Thus the qualifying integers are1 and3, giving2. Equality of floors does not require equality of logarithms.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q5

**Correct answer:** A, C

The tested integer 37 is directly covered, proving A. No observation concerns 37.5, so both success and failure there remain compatible; C is correct and B is not justified. Temperatures above 100 lie outside the tested set, so D is also unsupported. A finite set of successful tests does not establish behaviour at all untested inputs without further assumptions.

## Q6

**Correct answer:** 5

Write the array as[[a,b],[c,d]]. Since the second row and second column have maxima1, b,c,d are at most1. The first row and first column maxima2 force a=2. Remaining conditions are max(c,d)=1 and max(b,d)=1. If d=1, b,c can each be0 or1, giving4 arrays. If d=0, both b,c must be1, giving1 more. Total5. Orthographic maxima do not uniquely determine hidden column heights.

## Q7

**Correct answer:** 41

**Concept:** Recurrence evaluation and summation.

The first four terms are 2,5,11,23. Their sum is 41. Alternatively a_n+1 doubles at each step, so a_n=3×2^(n−1)−1, and the four-term sum is 3(2⁴−1)−4=41.

**Common misconception:** Reporting the fourth term instead of the requested sum.

## Q8

**Correct answer:** 2

**Concept:** Area constraints with an internal border.

For width w, the planted area is (40−2w)(30−2w)=1200−264=936. This gives w²−35w+66=0, or (w−2)(w−33)=0. Only w=2 satisfies the required width less than 15.

**Common misconception:** Using the outer perimeter times width without subtracting corner overlaps.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Adjacency blocks with relative-order constraints.

Treat PQ as one block. Among R,PQ,S their order is fixed. Insert unrestricted T into one of the four gaps before, between, or after those three objects. Each insertion produces a distinct valid schedule, giving 4. A,C,D miscount the available positions.

**Common misconception:** The PQ block has a fixed internal order and must not be multiplied by 2!.

## Q10

**Correct answer:** A

The required numerical answer is **16**, so select **A**.

Scale cost to100. Marked price is125 and required selling price105. The discount is20 out of125, or16%. Percentages apply to different bases; subtracting25−5 would use the wrong denominator.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 16 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -8 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q11

**Correct answer:** C

When a is processed before b, both c and d are enqueued before b can enqueue e. C puts e between c and d and is impossible. A,D are possible with a's neighbors ordered c,d or d,c. B results when b is processed first, discovering e before a discovers c,d. Equal BFS distance does not make every within-level ordering attainable.

## Q12

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An exclusive lock blocks conflicting reads until the writer ends, preventing those dirty reads and their cascading aborts, so A,B are true. Transactions can still wait cyclically for locks, disproving C. D directly violates retention until commit or abort. Strictness and deadlock freedom are different guarantees.

## Q13

**Correct answer:** 200 (exact)
**Concept:** HTTP connection reuse and parallel rounds.

The HTML costs one handshake plus one request-response: 80 ms. Each of three parallel image connections then costs 80 ms for its first image. Their second images need only another request-response, 40 ms. Total 80+80+40=200 ms.

**Common misconception:** Persistent connections save the second handshake, but non-pipelined dependent requests still consume another RTT.

## Q14

**Correct answer:** 2

Only descendants are forced larger. Index6 has children12 and13 and no deeper descendants within15 positions. Ancestors are smaller, while unrelated positions have no forced ordering relative to this key. Thus the answer is2. Heap order does not sort entire array intervals.

## Q15

**Correct answer:** D

The required numerical answer is **6**, so select **D**.

The floor values are0,1,1,2 for elements1,2,3,4. Equivalence classes therefore have sizes1,2,1. Each contributes its size squared in ordered related pairs, giving1+4+1=6. The middle class includes both off-diagonal orders as well as its two reflexive pairs.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 6 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q16

**Correct answer:** A, C

**Concept:** Dead assignments and liveness.

A states precisely that the assigned value cannot be observed on any outgoing path. With a pure, nontrapping right-hand side, the assignment can be removed. C is the corresponding liveness criterion. B provides a path that may need the value; D has no semantic relevance.

**Common misconception:** Removing an assignment that is unused on only some paths.

## Q17

**Correct answer:** 1.5

Concept: inverse matrix and trace. Determinant is 0·3−(−2)·1=2. The inverse is (1/2) times the matrix with rows (3,2),(−1,0). Its trace is 3/2=1.5. In general trace(A inverse) is not the reciprocal of trace(A).

## Q18

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The language makes each read an observable action, so eliminating one changes behavior even when values match: B,C. This disproves A. Observability imposes no requirement that consecutive values differ, making D false. Value equivalence alone does not establish effect equivalence.

## Q19

**Correct answer:** 4

By the mean value theorem on[0,1], f(1)−1≤3, hence f(1)≤4. Applied on[1,2], 7−f(1)≤3, hence f(1)≥4. Together f(1)=4. The endpoint increase already attains the maximum permitted slope over the full interval; a lower intermediate value would force a later slope above3.

## Q20

**Correct answer:** D

The required numerical answer is **6**, so select **D**.

**Concept:** Process creation and inherited control flow.

The first fork creates two processes. Only its child has p=0, so the conditional fork increases the population to three. Every one of these three executes the unconditional final fork, giving six processes reaching work().

**Common misconception:** Not every fork in source code is executed by the same set of processes.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 6 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q21

**Correct answer:** A

The required numerical answer is **8**, so select **A**.

**Concept:** Free bits in an implicant pattern.

There are three dashes, each independently taking zero or one. Thus the pattern covers 2³=8 minterms.

**Common misconception:** Counting fixed positions instead of free positions.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 8 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q22

**Correct answer:** 1 (exact)
**Concept:** CSR decoding and strong connectivity.

Edges are 0→1,0→3,2→0,2→2,2→3,3→1. Vertex 2 reaches all vertices, and every vertex reaches sink 1. Adding 1→2 makes all vertices mutually reachable. Zero additions cannot suffice because 1 initially has no outgoing edge. Therefore the minimum is one.

**Common misconception:** The self-loop at 2 does not connect it back from other vertices.

## Q23

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Interleaving and lost updates.

For 2, both threads read 0 before either first write, then both read 1 before either second write. For 4, run the threads serially. For 3, let the first pair of increments lose one update, reaching 1, then execute the two remaining increments serially.

Value 1 cannot be final: the final write is a thread's second write. Its preceding read occurs after its first write, which wrote at least 1; no operation writes 0, so that final read is at least 1 and the final write at least 2. Thus A is false and B,C,D are true.

**Common misconception:** Atomic individual accesses do not make a read-modify-write increment atomic.

## Q24

**Correct answer:** 4

The cache has64/4=16 data blocks. Four blocks per set give16/4=4 sets. Associativity counts ways within a set, not the total number of blocks.

## Q25

**Correct answer:** B
**Concept:** Multiplexer truth-table construction.

For AB=00 output C is true only at minterm 1. For AB=01 output NOT C is true at 2. AB=10 gives 4 and 5. AB=11 gives none. Therefore the on-set is {1,2,4,5}. A reverses the first two data inputs, C exchanges select groups 10 and 11, and D does not match the prescribed data inputs.

**Common misconception:** A select bit is not another data input; first identify the selected function, then evaluate C.

## Q26

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: pumping with a common multiple. The pumped a-count is p+(i−1)k. Set this equal to the fixed b-count p+p!, yielding i=1+p!/k. This is a positive integer because every k≤p divides p!, making B correct for every valid split. A does not generally solve the equation; C removes rather than adds the required amount and can be negative; D only adds k², not necessarily p!. The factorial makes one chosen witness handle all permitted pump lengths.

## Q27

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: dovetailing recognizers. Exactly one of L and its complement contains w, so its recognizer eventually accepts. Interleaving steps ensures that acceptance is reached even if the other machine loops; C gives the appropriate answer. A can wait forever on M for a nonmember. B mislabels complement acceptance; D imposes an unjustified time bound. A recognizer need not halt when its answer would be negative.

## Q28

**Correct answer:** B

The required numerical answer is **21**, so select **B**.

**Concept:** Equal-weight spanning trees.

Every spanning tree on four vertices has three edges. With every edge weighted seven, all spanning trees weigh 3×7=21 and are minimum.

**Common misconception:** Counting graph edges rather than the three edges selected by a tree.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 21 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -10 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q29

**Correct answer:** A

The required numerical answer is **36**, so select **A**.

Four pairs and total participation of the four B entities imply that each B entity occurs exactly once. Each chooses an A endpoint, and all three A entities must occur. Count onto functions from a four-element labeled set to a three-element labeled set:3^4−3×2^4+3×1^4=81−48+3=36. Many-to-many permits these instances; it does not require every entity to have more than one partner.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 36 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -18 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q30

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

## Q31

**Correct answer:** 0.75

**Concept:** Total probability followed by Bayes.

P(A)=0.6×0.5+0.2×0.5=0.4. The intersection P(A∩B)=0.3, giving P(B|A)=0.3/0.4=0.75.

**Common misconception:** Reversing a conditional probability without incorporating the marginal probabilities.

## Q32

**Correct answer:** C

The required numerical answer is **8**, so select **C**.

**Concept:** VIPT index constraints.

A page has 12 offset bits, of which six address a byte within a cache line. At most six more can index sets, allowing 64 sets. The cache has 32768/64=512 lines, requiring at least 512/64=8 ways. Eight is a power of two and attains the bound.

**Common misconception:** The page offset must hold both the line-offset and set-index fields.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 8 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q33

**Correct answer:** 8

**Concept:** Complements in an interval of a subset lattice.

Both X and Y must contain 1 and 2. Each of 3,4,5 must be in exactly one of X,Y: neither would violate the union requirement, while both would violate the intersection requirement. The independent choices give 2³=8 ordered pairs.

**Common misconception:** Dividing by two even though pairs are ordered.

## Q34

**Correct answer:** A, C

The only walk from s to t uses s→t and costs5. Vertex a cannot reach t, so its negative loop cannot affect this destination. A and C are true; D is false. Walk costs from s to a decrease without bound through repeated self-loops, disproving B. A negative cycle matters to a destination only if it can also reach that destination.

## Q35

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Forwarding onto a new Ethernet link requires a new frame with the router's outgoing source MAC address and the appropriate next-hop destination MAC address. C is correct. A describes end-to-end IPv4 addresses, B transport ports, and D application data, none of which this stated forwarding operation necessarily replaces. IPv4 TTL changes, but it is not one of the offered pairs.

## Q36

**Correct answer:** 8

An eight-state DFA can store the latest three bits, starting at000 and shifting on each input. All eight states are reachable after three symbols. For two distinct stored triples, consider appending zero, one, or two zeroes: the tested parities are respectively the parity of all three bits, the last two bits, and the last bit. If all three parities agreed between the triples, each bit would agree, contradicting distinctness. Thus some suffix distinguishes every pair, proving that all eight states are necessary. Padding is built into the initial000 state.

## Q37

**Correct answer:** A

The required numerical answer is **4**, so select **A**.

Balanced middle probing on15 keys forms four decision levels with capacities1,2,4,8. A deepest successful key requires four comparisons. Counting splits without the final equality test would undercount.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q38

**Correct answer:** C

The required numerical answer is **0**, so select **C**.

Q can send c because its outgoing channel starts empty. It then receives a, freeing P's channel so P can send b. Q can receive b, and P can receive c; fair scheduling ensures completion. Three total sends and three successful receives leave zero queued messages. P temporarily blocking on its second send does not establish deadlock because Q has a receive available after its first send.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.


## Q39

**Correct answer:** B, C

A distinguishing future sequence disproves equivalence, so B is true. Equivalent Moore states must have equal current outputs and equivalent successors for each input, proving C. Equal output now alone leaves future behavior unconstrained, making A false. Encodings are internal labels, not external observations, so D is false.

## Q40

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The outer R(x,y) requires membership. The negated existential rules out another y value for that same x, so A,C are true. Other x values are irrelevant to this test, making B false. The membership conjunct excludes pairs outside R, making D false. Uniqueness is per x, not a requirement that the whole relation contain one tuple.

## Q41

**Correct answer:** 4
**Concept:** FOLLOW through nullable sequences.

In S→ABc, the suffix after A is Bc. B can start with a via A, d via nullable A followed by D, or b directly; B can also vanish, exposing c. Thus a,b,c,d all enter FOLLOW(A). In B→AD, D contributes d and can vanish, so FOLLOW(B) contributes c, adding nothing new. FOLLOW(A) is exactly {a,b,c,d}, of size four. The trailing c in S prevents an end marker from propagating to these occurrences.

**Common misconception:** A nullable symbol requires examining the entire suffix, not only the next symbol's nonempty FIRST set.

## Q42

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Decidability under a totality promise.

Enumerate strings by length and simulate M on each. Every simulation halts by the promise; if any string is accepted it will eventually be found, proving A. D tests only finitely many strings, so it terminates with either answer.

For B and C, given an arbitrary machine N and input w, construct M that on input x simulates N(w) for |x| steps and accepts exactly if N halts within that bound. M always halts. Its language is nonempty exactly when N(w) halts. A decider for emptiness, or equivalence to the empty language, would therefore decide the halting problem, which is impossible. B and C are false.

**Common misconception:** Confusing termination of each individual test with termination of an infinite search for a negative answer.

## Q43

**Correct answer:** 3
**Concept:** Counting distinct optimal knapsack subsets.

With E selected, four units of capacity remain. The best addition is A+B, value 6, for total value 11. C or D adds only 4 and cannot be paired with A or B within the remaining capacity. Without E, choosing C+D leaves room for exactly one of A,B, also giving value 11 in two ways. Choosing at most one of C,D yields at most A+B+C or A+B+D, value 10. Thus the optimum is 11 and exactly ABE,ACD,BCD attain it.

**Common misconception:** Items with equal weights and values remain distinct when counting subsets.

## Q44

**Correct answer:** A, B, D
**Concept:** A decreasing distance as a loop-prevention invariant.

With w(v,u)>0, d(u)=d(v)−w(v,u)<d(v), proving D; strict decrease around a directed cycle is impossible, proving A. With a zero-cost A–B link and unit-cost links from both A and B to t, both distances are 1. Each may choose the other as an equal-cost next hop, producing a cycle despite exact distances (B). This example refutes C.

**Common misconception:** Nonnegative costs suffice for shortest-distance algorithms, but strict decrease of chosen forwarding distances needs positive costs or an additional tie rule.

## Q45

**Correct answer:** C

The required numerical answer is **11**, so select **C**.

Four retired instructions require 4+4=8 cycles without penalties. The load-use dependence adds one and the taken branch adds two, giving 11. The stated forwarding rule prevents another stall between the ALU instruction and branch. Wrong-path work is already represented by the two-cycle penalty, so it must not be counted again as retired instructions.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 11 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -5 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q46

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Structural description of a grammar's language.

Each S expansion adds a at the front and b at the end; T generates an arbitrary central block of c symbols. Thus the language is {aⁿcᵐbⁿ:n,m≥0}. A and B follow. abcc puts c symbols after b and cannot be generated, so C is false. aacbb has n=2,m=1, proving D.

**Common misconception:** Tracking symbol counts without tracking their ordering restrictions.

## Q47

**Correct answer:** C

**Concept:** Operating Systems — Deadlock

Original needs are P0=(1,2), P1=(1,1), P2=(2,0). With available (1,1), P1 can finish, releasing (0,1), so work becomes (1,2). P0 can then finish, releasing (1,0), making (2,2); P2 then finishes. Thus the original state is safe. Tentatively grant (0,1) to P0: available becomes (1,0), and P0's need becomes (1,1). P1 still needs (1,1) and P2 needs (2,0). No process can finish with (1,0), so the tentative state is unsafe and the request must be deferred. Unsafe does not by itself assert that deadlock has already occurred.

- **A:** False: after the grant P0 needs one B, but no B is available.
- **B:** False: P2 needs two A, but only one A is available.
- **C:** True: the original safe sequence exists, while no process can start the tentative safety reduction.
- **D:** False: P1,P0,P2 is a safe sequence in the original state.

**Common misconception:** A request within availability and maximum claim can still destroy safety.

## Q48

**Correct answer:** D

The required numerical answer is **51**, so select **D**.

**Concept:** Bounded compositions and generating functions.

The answer is the coefficient of x⁵ in (1+x+x²)⁵. Without upper bounds there are C(9,4)=126 solutions. For a chosen bin holding at least three tokens, remove three tokens: C(6,4)=15 remaining solutions. Subtract 5×15=75. Two bins cannot each hold three when the total is five, so no intersection correction is needed. The result is 126−75=51.

**Common misconception:** Identical tokens do not make the distinguishable bins interchangeable.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 51 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -25 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q49

**Correct answer:** A, B

The error is explicitly a multiple of g, so its remainder is zero, proving A. Adding it to a valid codeword leaves a divisible polynomial, proving B. C contradicts this construction. The polynomial has three nonzero terms at shifted degrees, not one, refuting D. CRC detection depends on divisibility, not merely on nonzero errors.

## Q50

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Compiler Design — Lexical analysis

After reading a, the lexer has an accepting position for token a, but ab*c is still possible. It must continue across all n b symbols because a subsequent c would make them part of the longer token. The following d rules out that longer token. No position after the first a was accepting for a token beginning there, so the lexer returns to the position after a. It has inspected n+1 characters beyond that accepting position. This amount is unbounded as n grows.

A and B propose fixed bounds disproved by large n. C is correct. D would violate longest match on inputs that end the prefix with c instead of d.

- **A:** False: proposes a fixed bound of at most one character, disproved by inputs with large n.
- **B:** False: proposes a fixed bound of at most two characters, disproved by inputs with large n.
- **C:** True: before returning token a, the lexer must inspect all n occurrences of b plus character d, requiring n+1 lookahead characters, which is unbounded as n grows.
- **D:** False: violates longest match; token a cannot be emitted immediately because longer candidate ab*c may follow.

**Common misconception:** Recognition by a finite automaton does not guarantee a fixed bound on longest-match backup.

## Q51

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For id=1 only employee 11 passes the ON condition; both counts are 1. For id=2 the left join supplies one NULL-extended row. COUNT(*) counts it, while COUNT(E.eid) ignores its NULL, yielding n=1,m=0. Hence A,B are true and D false. Moving the active filter to WHERE rejects that NULL-extended row, removing id=2 and disproving C. Filtering matches and filtering the joined result have different effects on outer joins.

## Q52

**Correct answer:** 300

The latest collision indication requires a round trip of2·12=24 microseconds. At100×10^6 bits/s this corresponds to2400 bits, or300 bytes. Using the one-way delay would halve the required frame and could let transmission finish before collision detection.

## Q53

**Correct answer:** A

The required numerical answer is **50**, so select **A**.

**Concept:** BST deletion and ancestor relationships.

The inorder predecessor of 20 is 10. Replacing 20 by 10 removes its old leaf, leaving the 30 subtree (with 25 and 35) to the right of the replacement. The inorder successor of root 40 is 50, the minimum in its right subtree. Root becomes 50 and its former leaf is removed. Node 25 remains in the left subtree, while 70 is in the right subtree, so their lowest common ancestor is the new root 50.

**Common misconception:** Key replacement affects later ancestor labels even if much of the tree's shape is unchanged.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 50 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -25 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q54

**Correct answer:** 5

Integration by parts gives integral(x f')=[x f] from0 to2−integral(f)=2f(2)−0f(0)−3=8−3=5. f(0) need not be known because its boundary coefficient is zero. The endpoint and integral information together determine the answer without reconstructing f.

## Q55

**Correct answer:** 16

PUSH7 writes7 at96; PUSH9 writes9 at92. POP sets R=9 and SP=96. The explicit store writes9 at100, not at96. The final POP therefore reads the still-present7 at96 into S, giving R+S=16. The store uses the current SP after the first pop.

## Q56

**Correct answer:** C

The required numerical answer is **2**, so select **C**.

First100+60=160 exceeds127, wraps to−96 and overflows. Then−96−60=−156 is below−128, wraps to100 and also overflows. Both operations signal overflow, although the final wrapped result equals the original x. Algebraic cancellation of the final result does not eliminate intermediate overflow flags.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q57

**Correct answer:** A, B

**Concept:** Foreign keys versus uniqueness and participation.

The primary key is cid, so multiple distinct child rows can share a parent, proving A. A non-NULL foreign key must find a referenced parent, proving B. No constraint forces parents to have children, so C is false. A foreign key need not be unique, refuting D.

**Common misconception:** Importing the referenced key's uniqueness into the referencing column.

## Q58

**Correct answer:** A, C

Concept: nullable productions and FOLLOW propagation. FOLLOW(S)={$}; B ends S's production and occurs before c in its own recursive production, so FOLLOW(B)={c,$}, C. A is followed by nullable B, whose nonempty FIRST is {b}; hence FOLLOW(A)={b,$}, not c, disproving B. A's alternatives use lookahead a versus {b,$}; B's use b versus {c,$}, with no conflicts, proving A. D chooses ε on the lookahead reserved for A→aA and is false.

## Q59

**Correct answer:** D

The required numerical answer is **-4**, so select **D**.

The left-recursive grammar computes(9−4)−2=3. The right-recursive version computes9−(4−2)=7. The difference is3−7=−4. Rewriting a grammar must preserve semantic associativity; subtraction is not associative.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q60

**Correct answer:** D

The required numerical answer is **2**, so select **D**.

The original median is(3+7)/2=5. Replacing one3 by7 or a larger number leaves at least four observations at least7 and yields middle pair7,7, so median7 is attainable. It cannot exceed7: five fixed observations are at most7, so both middle positions remain at most7. The maximum increase is2. An arbitrarily large replacement need not make the median arbitrarily large.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q61

**Correct answer:** 5

**Concept:** Counting a particular base-case leaf.

Let Z(n) count zero-argument calls. Z(0)=1, Z(1)=0 and Z(n)=Z(n−1)+Z(n−2). Thus Z(2),…,Z(6) are 1,1,2,3,5. Only the last count is requested, not the total number of calls.

**Common misconception:** Counting both base cases together.

## Q62

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Near1.5, adjacent representable values are1.375,1.5,1.625, with spacing0.125. The midpoint boundaries are1.4375 and1.5625. The significand of1.5 is1.100, whose last retained bit is even; both ties therefore round to1.5. A,C are included, B is strictly inside the interval, and D is already exactly represented at1.625. Ties on both sides can select the same even significand.

## Q63

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Theory of Computation — Pushdown automata

The finite language L is regular, so a DFA recognizes it. A final-state DPDA can simulate that DFA without using its stack. A nondeterministic empty-stack PDA can choose whether to finish after a or to wait for b and then finish.

A deterministic empty-stack PDA accepting a has a unique computation on that prefix. On input ab it must follow the same computation until the prefix a has been consumed. If it then empties its stack through epsilon transitions, determinism prevents choosing a b-consuming alternative, and no transition can consume b after the stack is empty. Hence it cannot also accept ab. This is the prefix-free obstruction under the stated conventions.

A, B and C can recognize L by the constructions above. D cannot.

- **A:** False: a DFA recognizes the regular language {a, ab}, so a final-state PDA can also recognize it.
- **B:** False: an NPDA can nondeterministically guess whether to accept after a or after ab.
- **C:** False: a DPDA accepting by final state easily recognizes {a, ab}.
- **D:** True: a DPDA accepting by empty stack cannot recognize {a, ab} because it is not prefix-free and no end marker is provided.

**Common misconception:** Final-state and empty-stack acceptance have equivalent power for nondeterministic PDAs, but not automatically for deterministic PDAs without an end marker.

## Q64

**Correct answer:** 5

Concept: subgroup enumeration. Subgroup orders divide six. There is one trivial subgroup, three order-two subgroups generated by the three transpositions, and one order-three subgroup generated by either 3-cycle. All are cyclic and abelian. The only order-six subgroup is S3 itself, which is nonabelian. Total=1+3+1=5. The two 3-cycles generate the same subgroup and must not be counted twice.

## Q65

**Correct answer:** B

For fixed i, the inner work is1+2+4+...+2^floor(log2 i), which lies between i and2i. Summing over i=1..n givesΘ(n²), so B is correct. A counts doubling iterations but ignores their growing work; C multiplies by a spurious log factor; D ignores the outer linear range. Geometric inner workloads must be summed, not bounded by their maximum at every iteration.

