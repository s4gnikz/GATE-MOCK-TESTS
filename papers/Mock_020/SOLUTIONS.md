# Worked Solutions — GATE CS 2027 Mock Test 020

## Q1

**Correct answer:** 27

**Concept:** Constant second differences with an erroneous observation.

The first three terms give differences5 and8. Continuing with difference increment3 gives the sequence3,8,16,27,41, which changes only the fourth observation. This repair is unique: any two quadratic sequences agreeing at three distinct positions are identical, whereas two proposed one-position repairs would agree at at least three of the five positions. Thus no different constant-second-difference repair exists.

**Misconception:** Extending a pattern without checking the remaining observations or uniqueness.

## Q2

**Correct answer:** B

**Concept:** Area ratios with a shared height.

Write the rectangle's dimensions as width w and height h. The triangle has base w/2 along the top edge and perpendicular height h, hence area wh/4. The quadrilateral occupies3wh/4. The ratio is1:3, option B. A, C and D would allocate respectively one-third, one-fifth and two-fifths of the rectangle to the triangle, inconsistent with its base and height.

**Misconception:** Taking the ratio of the top-edge lengths as the ratio of areas.

## Q3

**Correct answer:** C

**Concept:** Necessary versus sufficient conditions in English.

“May enter only if accompanied” asserts entry implies accompaniment, without asserting its converse. C is correct. A asserts the converse, making accompaniment sufficient. B asserts both directions. D uses “unless” to authorize entry in the absence of accompaniment and does not express the required condition.

**Misconception:** Interchanging “if” and “only if”.

## Q4

**Correct answer:** 24

**Concept:** Successive transfers with changing concentration.

Scale each initial tank to100 mass units. Transfer25 units from A, containing5 units of salt. B now has125 units containing45 units of salt, so its concentration is36%. The25 units returned contain9 units of salt. A finishes with100 units and15+9=24 salt units, giving24%.

**Misconception:** Assuming that equal masses exchanged imply equal salt masses exchanged.

## Q5

**Correct answer:** A, B, D

**Concept:** Combining implication with a cardinality constraint.

If P were ON, Q would be ON, forcing R and S OFF because exactly two switches are ON. But R OFF would require S ON, a contradiction. Hence A is true. The implication R OFF implies S ON forbids R and S both OFF, so B is true. Q need not be ON: R,S ON with P,Q OFF is valid, making C false. If Q is OFF, P must also be OFF, and the two ON switches must be R and S; D is true. The complete valid ON pairs are QR, QS and RS.

**Misconception:** Applying implications separately while ignoring the exact-count constraint.

## Q6

**Correct answer:** B

**Concept:** Composition of a rotation and an offset reflection.

R sends(x,y) to(-y,x). Reflection about x=1 sends(u,v) to(2-u,v), so one pair T sends(x,y) to(2+y,x). Applying the pair twice gives T²(x,y)=(x+2,y+2), and four times gives T⁴(x,y)=(x+4,y+4). The final point is(6,5), option B. A incorrectly assumes the composition has order four. C is the result of a half-turn about the origin, which is not the specified composite. D is not obtained by the specified sequence; the intermediate points are(3,2),(4,3),(5,4),(6,5).

**Misconception:** Treating a rotation followed by an offset reflection as a rotation about the origin.

## Q7

**Correct answer:** D

**Concept:** Distinguishing a rate, a count and causal evidence.

For example,100 issued books with20 late returns gives20%;200 issued books with30 late returns gives15%. Thus a declining fraction can accompany an increasing count. The passage also explicitly withholds a causal conclusion, making D correct. A invents both causality and a claim about every borrower. B contradicts the numerical possibility. C is false: if total volume rises while the timely fraction also rises, the timely count rises, not falls.

**Misconception:** Comparing percentages without their denominators, or treating an observed before/after change as causal proof.

## Q8

**Correct answer:** A, D

**Concept:** Inclusion–exclusion for overlapping adjacency constraints.

Treat AB or BA as one block. There are2×4!=48 arrangements in X, so A is true; Y also has48. For both adjacency conditions, B must be between A and C, giving the blocks ABC or CBA. Alongside D and E, this yields2×3!=12 arrangements, not24, so B is false. The union has48+48−12=84, so C's72 is false. There are5!=120 total arrangements, leaving120−84=36 in neither set, making D true.

**Misconception:** Counting overlapping adjacency blocks as if B could be used twice independently.

## Q9

**Correct answer:** 25

**Concept:** Weighted averages and relative percentage changes.

A's initial share is2/3. If its new share is x, the combined rate is0.9x+0.6(1−x)=0.75, giving x=1/2. The relative fall is[(2/3−1/2)/(2/3)]×100=25%. The change in percentage points is16 2/3, which is not the requested relative percentage decrease.

**Misconception:** Confusing a change in share with the percentage change of that share.

## Q10

**Correct answer:** A

**Concept:** Opposite faces and vertex incidence after folding a cube net.

The four squares A,B,C,D wrap around the cube as a belt. Positions two apart in this belt are opposite: A opposite C, and B opposite D. The two remaining squares E,F close the top and bottom and are opposite. A,B,E take one face from each opposite pair and meet at a vertex. Thus A is correct. B incorrectly makes adjacent B,C opposite and its proposed triple includes opposite A,C. C has the correct opposite pair E,F, but its proposed triple includes opposite A,C. D gives a wrong opposite pair A,D and a triple containing opposite E,F.

**Misconception:** Using distance on the flat net instead of adjacency on the folded cube.

## Q11

**Correct answer:** A, C

**Concept:** Input exhaustion and state/stack-dependent continuation.

A final state may be visited with unread input. Acceptance still requires consuming all the input, so C is true. If a later transition requires a particular stack top that the modification erased, a formerly accepting continuation can disappear; A is true. This counterexample disproves B's universal claim. Final states need not be terminal and may have outgoing transitions, so D is false.

**Misconception:** Confusing entering a final state with successful acceptance regardless of remaining input.

## Q12

**Correct answer:** 2

**Concept:** Boolean dependence on a variable.

The two product terms cannot both be1. At a=1, f=b; at a=0, f=c. Flipping a changes the output precisely when b differs from c: assignments(0,1) and(1,0). Thus there are2 assignments.

**Misconception:** Counting both initial values of a even though the question asks for assignments to(b,c).

## Q13

**Correct answer:** B

**Concept:** Distinct meanings of unsigned carry and signed overflow.

The unsigned addition is128+254+1=383=256+127. Thus the low bits are01111111 and carry-out is1. Signed interpretation computes−128−1=−129, outside the signed8-bit range, so overflow is1. B states all three correctly. A misses carry and overflow. C has the wrong result and overflow. D gives the right result and overflow but the wrong carry-out.

**Misconception:** Assuming that carry-out and signed overflow are mutually exclusive or equivalent indicators.

## Q14

**Correct answer:** 5

**Concept:** Reconstructing raw second moments when removing an observation.

The original sum is50. Population variance8 implies the sum of squares is5(8+10²)=540. Removing14 leaves sum36 and sum of squares344 for four observations, with mean9. The new variance is344/4−9²=86−81=5.

**Misconception:** Subtracting the removed squared deviation while retaining the old mean.

## Q15

**Correct answer:** 256

**Concept:** Buddy alignment and external fragmentation.

Offset0's256-byte buddy is offset256, which remains allocated. Offset512's buddy is offset768, also allocated. The two free blocks are not buddies and cannot coalesce. Thus there are512 free bytes in total, but the largest satisfiable single request is256 bytes.

**Misconception:** Equating total free space with the largest available contiguous buddy block.

## Q16

**Correct answer:** B, C

**Concept:** Physical sharing versus metadata representation.

A frame may have several virtual aliases, making B true. A single stored pair can equal only one of the two distinct(process, virtual-page) pairs, so A is false. Retaining a list of aliases permits lookup of both and resolves this particular representation problem, so C is true. Different virtual page numbers can map to the same physical frame; D is false.

**Misconception:** Treating a limitation of a simplified page-table format as a hardware prohibition on sharing.

## Q17

**Correct answer:** 500

**Concept:** Cumulative acknowledgment boundaries.

ACK2500 acknowledges every byte below2500, covering the first three listed segments. Only[2500,3000), of length500, remains unacknowledged among the listed bytes. The acknowledgment number names the next expected byte, not the last received byte.

**Misconception:** Counting byte2500 as acknowledged or assuming the ACK covers only one segment.

## Q18

**Correct answer:** 3

**Concept:** Kernel cosets and the image of a homomorphism.

The kernel solves8x≡0 modulo12, equivalently x≡0 modulo3. It contains0,3,6,9 and has size4. The number of kernel cosets is12/4=3, also the size of the image{0,4,8}.

**Misconception:** Returning the number of kernel elements instead of its index.

## Q19

**Correct answer:** A, C, D

**Concept:** Forced edges and alternative perfect matchings.

Vertex b has only neighbour2, so every perfect matching uses b–2. Then a must use1 and c must use3, giving exactly one perfect matching. A and C are true. Edge a–2 is unused in that matching, so removing it does not destroy the matching; B is false. Adding b–1 allows the additional matching a–2,b–1,c–3, so D is true.

**Misconception:** Assuming every edge incident to a matched vertex is essential to the matching.

## Q20

**Correct answer:** C

**Concept:** Consensus term and static hazards.

When b=c=1, the function should stay1 while a changes. Unequal delays can briefly make both original product outputs0. The term bc is continuously1 during the transition and covers that gap. It is logically redundant: whenever bc=1, either a=1 makes ab=1 or a=0 makes(NOT a)c=1. Thus C removes this hazard without changing the function. A and D incorrectly turn the function on at a=b=c=0. B incorrectly turns it on at a=1,b=c=0. They also do not provide the required stable cover during the specified transition.

**Misconception:** Equating Boolean equivalence with identical transient circuit behaviour.

## Q21

**Correct answer:** A, C

Every spanning tree has two edges, so all tree weights fall by4: A and C are true. Initially A–C and A–B–C both have weight3; afterward their weights are1 and−1, respectively. The shortest-path set changes, making B false and disproving D. The misconception is extending a fixed-edge-count argument to paths of different lengths.

## Q22

**Correct answer:** 2

Only descendants are forced larger. Index6 has children12 and13 and no deeper descendants within15 positions. Ancestors are smaller, while unrelated positions have no forced ordering relative to this key. Thus the answer is2. Heap order does not sort entire array intervals.

## Q23

**Correct answer:** 13

The next address needs log2(64)=6 bits. Four ALU choices need2 bits. Five independently selectable signals need5 bits. Total6+2+5=13. Independent signals cannot be encoded as a single choice among five alternatives.

## Q24

**Correct answer:** B

The right leaf becomes[30], which satisfies the stated minimum occupancy. Its minimum changes to30, so the separator must change to30. B is correct. A assumes an unstated occupancy bound; C violates the explicit separator convention; D discards valid keys. Separator repair and underflow repair are distinct operations.

## Q25

**Correct answer:** B, C

Before line3, y must survive to line4, so B is true. The old x has already been used to compute y and is overwritten at line3 before its next direct use, making A false. Line1 affects y and thereby z; line3 affects the other operand of z, so C is true and D false. A value may cease to be live even though an earlier computation using it still contributes to the output.

## Q26

**Correct answer:** 1024

The two high address bits decode to one of four chip enables. Each read selects one chip, while10 address bits distinguish1024 bytes. Product1×1024=1024. Parallel connection of address pins does not mean that all chips should drive the data bus simultaneously.

## Q27

**Correct answer:** B, C

A store through q may modify the object read through p. If p=q and its old value is4, x=5 while y=10, proving C and disproving A. Proven distinct objects prevent this store from changing *p, so B is true. D ignores aliasing and is false. Availability of an expression depends on memory effects, not just matching source text.

## Q28

**Correct answer:** 6

The tokens are a1, ==, =, 23, >, b. Longest match takes two of the three consecutive equals signs first. Neither the identifier rule nor integer rule permits the entire input to be combined. Thus there are6 tokens. Token boundaries need not coincide with spaces.

## Q29

**Correct answer:** A

U used an uncommitted value that disappears when T aborts. Cascading recovery therefore rolls back U's dependent execution, even if U wrote nothing. A is correct. B invents a conflict: read–read pairs are not conflicts. C and D assert unjustified universal abort rules. Read-only does not mean immune to dirty data.

## Q30

**Correct answer:** 4

Start with{1,2,3}, sum6. Replacing any chosen i by i+3 adds3 and flips parity. The sum is even when the number of replacements is even: choose0 or2 of the three pairs, giving1+3=4 subsets. Selecting exactly one from each pair is a constraint separate from selecting three arbitrary elements.

## Q31

**Correct answer:** B, C

A pushdown automaton can maintain unmatched symbols: push when the incoming symbol agrees with the stack top and pop when it differs, accepting when no unmatched symbols remain. Thus B is true. Restricting to 0*1* gives exactly0^n1^n, so C is true. If L were regular, its intersection with the regular language0*1* would be regular, contradicting the standard pumping argument for0^n1^n; A is false. The string10 is a counterexample to D. Equal counts do not impose symbol order.

## Q32

**Correct answer:** C

TCP provides an ordered byte stream. A read can return some available bytes, including bytes spanning application writes. Thus C is true. Timing can prevent the first call from gathering either particular length, so A and B are not guaranteed. TCP does not preserve write boundaries, making D false. Applications needing records must provide framing.

## Q33

**Correct answer:** 1

For n≥1, the coefficient of x^n in(1−2x)A(x) is an−2a(n−1)=1. In particular the coefficient at degree4 is1. Equivalently,(1−2x)A(x)=1/(1−x). Formal power-series manipulation does not require a numerical convergence radius.

## Q34

**Correct answer:** 1

The flawed algorithm settles a at distance2, then t at4, before b at5. It refuses b's later improvement of a to1. The true path s→b→a→t has weight5−4+2=3. The excess is4−3=1. The graph has no cycle; a negative edge alone can invalidate Dijkstra's settling argument.

## Q35

**Correct answer:** 11

Every directed edge contributes once to outdegree and once to indegree, including a loop. Thus both total degrees equal the edge count11. A loop does not contribute twice to either separate directed degree. The six-vertex count and number of loops do not alter the identity.

## Q36

**Correct answer:** A, C

Stable least-significant-key-first sorting preserves the year order within each city and retains arrival order for exact ties, so A is true. Explicitly restoring arrival order before the same two stable passes also works, so C is true. B makes year the primary key and can interleave cities incorrectly. D can destroy arrival order for equal keys, and a later stable city sort will preserve that damage. Stability matters for ties, not just for the primary ordering.

## Q37

**Correct answer:** 2.8

The common data access costs80 ns. The old average is2+80+0.05×160=90 ns. The new average is4+80+0.02×160=87.2 ns. The saving is2.8 ns. Account for the slower probe on every access, not just on misses.

## Q38

**Correct answer:** 4

The root can split at either plus sign. Splitting at the first leaves three operands with two operators on the right, admitting two binary parenthesizations. Splitting at the last similarly admits two on the left. These are disjoint cases, yielding4. Splitting at the multiplication yields the fifth possible parse tree, which is excluded by the root requirement. No unstated precedence convention applies.

## Q39

**Correct answer:** B, D

The first two writes give an edge T1→T2; the last two give T2→T1. The graph has a cycle, so A and C are false. There are no read-from relationships to preserve, and T1 is the final writer. Serial order T2,T1 has the same final writer, so B and D are true. Blind writes permit view equivalence even when conflict serializability fails.

## Q40

**Correct answer:** 2

The original orbit is2,10,6,2,... because gcd(8,12)=4. Those three slots are occupied. With step5 the probes begin2,7; slot7 is empty. Thus two probes suffice. A table can have free slots while a non-coprime probe step fails to reach them.

## Q41

**Correct answer:** C

q points to the pointer variable p, so(*q)++ changes p from a+1 to a+2. Then **q names a[2], while*(p−1) is a[1]=4. The update changes a[2] from6 to10; p−a is2. C is correct. A omits both updates, B fails to update p's position, and D adds the wrong array value. Parentheses distinguish incrementing a pointer through another pointer from incrementing an array element.

## Q42

**Correct answer:** 4

No single row covers all four columns. Two rows suffice: P covers1,2 and R covers3,4, total cost4. Every row costs at least2, so no two-row cover costs less than4. This proves both the minimum row count and the secondary cost optimum. A greedy choice of the largest row T is not required and would incur at least6 with another row.

## Q43

**Correct answer:** 14

For n≥1 the recursion has n leaves, all with argument1, because each split preserves the sum of arguments and eventually reaches ones. A full binary tree with10 leaves has19 invocations. The distinct arguments reached are10,5,3,2,1: five evaluations under the specified memoization convention. The reduction is19−5=14. Calls that merely find memoized results are explicitly excluded from the second count.

## Q44

**Correct answer:** 2048

Offset6144 is in logical block6, using zero-based block numbering. The four direct pointers cover blocks0–3; block6 needs the single-indirect structure. Allocate one1024-byte indirect block and one1024-byte data block. Sparse holes require no intervening data blocks, giving2048 bytes. Logical file length is not allocated storage size.

## Q45

**Correct answer:** 1

For A=a1, the AB projection permits b1,b2 and AC permits c1,c2. BC permits(b1,c1),(b1,c2),(b2,c2), yielding three tuples, including new tuple(a1,b1,c2). For A=a2, only b1 and c2 are permitted, yielding the original third tuple. The join therefore has four tuples, only one spurious. Pairwise relationships need not determine a ternary relationship losslessly.

## Q46

**Correct answer:** A, C

Signed overflow is carry into the sign position XOR carry out, so A is true. Equivalently it occurs when equal-sign operands produce the opposite sign, exactly C's formula. Carry-out alone is unsigned overflow: all-ones plus1 has carry-out1 but represents−1+1=0 without signed overflow, disproving B. Opposite-sign addition cannot overflow, while D is1 exactly for opposite signs, so D is false. Unsigned and signed interpretations use the same bits but different range tests.

## Q47

**Correct answer:** A, B

The pumping lemma guarantees the existence of a suitable decomposition for each sufficiently long string. To refute regularity one must defeat every permitted decomposition, so A is true. The bound |xy|≤p forces nonempty y wholly into the first block of a's, so B is true. The lemma requires |y|>0, making C false. It allows every string of length at least p, including2p, making D false. Quantifier order is essential to pumping arguments.

## Q48

**Correct answer:** B

For fixed i, the loop executes floor(n/i) times. Summing gives sum from1 to n of floor(n/i). This lies between nHn−n and nHn, where Hn=Θ(log n), so the total isΘ(n log n). B is correct. A ignores the harmonic factor; C and D exceed the tight growth rate. Varying strides prevent multiplication of two uniform loop bounds.

## Q49

**Correct answer:** 5

When p=r=false, q is free: two choices. When at least one of p,r is true, q must be true: three choices for(p,r). In all cases s is uniquely their XOR. Hence2+3=5 assignments. The equivalence defining s does not double the number of choices.

## Q50

**Correct answer:** 5

dup creates another descriptor referring to the same open-file description, including its shared offset. The first read sets it to6; the seek sets it to2; the final read advances it to5. Descriptor4 therefore observes5. Separate descriptor numbers do not imply separate file offsets.

## Q51

**Correct answer:** -4

The left-recursive grammar computes(9−4)−2=3. The right-recursive version computes9−(4−2)=7. The difference is3−7=−4. Rewriting a grammar must preserve semantic associativity; subtraction is not associative.

## Q52

**Correct answer:** 7

The third coefficient row equals the sum of the first two rows. Consistency therefore requires k=2+5=7. The first two rows are independent, so at k=7 the rank is2 with three unknowns, giving infinitely many solutions. For other k the dependent left sides conflict with the right sides. Zero determinant alone would not establish consistency.

## Q53

**Correct answer:** 80

Sequential object retrieval costs3×40=120 ms after the HTML. Pipelining costs one40 ms RTT under the stated negligible-size model. The saved time is80 ms. The common DNS20, handshake40 and base40 cancel; totals are220 versus140 ms. Do not re-charge connection establishment for each object on a persistent connection.

## Q54

**Correct answer:** A, B, D

Since |f(x)|≤x², continuity at0 follows, making A true. The difference quotient f(x)/x=x sin(1/x) tends to0, proving B and D. For nonzero x, f'(x)=2x sin(1/x)−cos(1/x), whose cosine term oscillates without a limit at0; C is false. Differentiability does not force continuity of the derivative.

## Q55

**Correct answer:** A, C

Simulate the machine on00 and accept its encoding if it accepts00; this recognizes S, so A is true. Membership depends only on the recognized language and holds for some languages but not others, so C is true. By the undecidability of nontrivial semantic language properties, S is undecidable, disproving B. Equivalently one can reduce arbitrary machine acceptance to acceptance on the fixed string by embedding the original machine and input in a new machine. If both S and its complement were recognizable, dovetailing their recognizers would decide S, so D is false. A fixed input length does not bound computation time.

## Q56

**Correct answer:** 1.6667 (accepted range 1.66665–1.66675)

P(N=2k+1)=2^{−(2k+1)} for k≥0. The odd probability is(1/2)/(1−1/4)=2/3. Conditional on being odd, K=(N−1)/2 has probabilities(3/4)(1/4)^k and mean(1/4)/(3/4)=1/3. Therefore E[N|odd]=1+2/3=5/3≈1.6667. Conditioning on parity changes the distribution and cannot be handled by rounding the unconditional mean.

## Q57

**Correct answer:** 1440

The1500-byte outer packet contains a20-byte tunnel header plus the inner20-byte IP header,20-byte TCP header and payload. Hence the payload bound is1500−20−20−20=1440. All three headers consume the outer MTU; the inner packet is not exempt from the tunnel overhead.

## Q58

**Correct answer:** B, C, D

After A,B,C all three slots are full. The second A is a hit. FIFO retains insertion order A,B,C and evicts A for D, so B is true; its final A misses, giving five misses. LRU updates A's recency and evicts B for D, so C is true; its final A hits, giving four misses. D is true and A is false. A cache hit affects LRU recency but not FIFO insertion order.

## Q59

**Correct answer:** 2

R's lexical parent is P, not its caller Q. Its static link therefore reaches P; P's static link reaches Main. Two links suffice. Dynamic links would instead follow R→Q→P→Main. Static scope follows declaration nesting rather than the calling sequence.

## Q60

**Correct answer:** 1.7

For k equal packets of length L across h equal store-and-forward links, the total is(k+h−1)L/r because packets pipeline after the first packet traverses all links. Three packets each contain2000+100=2100 bytes, taking5×2.1=10.5 ms. Six packets each contain1000+100=1100 bytes, taking8×1.1=8.8 ms. The saving is1.7 ms. Smaller packets improve pipeline fill time but increase total header bytes.

## Q61

**Correct answer:** 300

Base computation costs1000×2=2000 cycles. DMA adds100 stall cycles, total2100. Programmed I/O adds400 cycles, total2400. DMA saves300 cycles. The baseline CPI must be combined with the respective transfer overhead, not multiplied by it.

## Q62

**Correct answer:** B, C

No required item can be a counterexample when Required is empty, so both candidates qualify: B is true and A false. C expresses precisely the absence of a missing requirement. Completed's x-projection is empty, which would remove both candidates from consideration; D is false. Universal conditions require a separately specified candidate domain, especially when the requirement set is empty.

## Q63

**Correct answer:** 3

Use states E0 for even a-count and no final b, E1 for even a-count and final b, and O for odd a-count regardless of final symbol. Only E1 accepts. On a, E0/E1 go to O and O goes to E0; on b, E0/E1 go to E1 and O stays O. All are reachable by ε,b,a. E1 is distinguished from the other two by ε, and E0 from O by suffix b. Thus three states are necessary and sufficient. A naive product has four states, but the two odd-count states are equivalent.

## Q64

**Correct answer:** B, D

After buffered data are exhausted, pipe EOF requires every write-end reference to be closed. The child still has one, so B is true and A false. Closing its read end does not remove that writer, making C false. Closing its write end with no other writers permits EOF, making D true. An idle writer is different from a closed writer.

## Q65

**Correct answer:** 2

Repeated movement by−8 modulo18 partitions indices into gcd(18,8)=2 cycles, each of length9. One consists of the even indices and one of the odd indices. The algorithm starts one cycle per component, hence twice. The rotation amount alone is not the number of disjoint cycles.
