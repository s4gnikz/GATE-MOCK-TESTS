# Worked Solutions — Mock Test 027

## Q1

**Correct answer:** C

The statement quantifies over tested villages only. It directly excludes a tested failure, giving C. A extends the claim to untested villages, B invents a failure, and D invents a comparison. Missing observations do not establish either safety or danger.

## Q2

**Correct answer:** 6

Choose the two people receiving their own umbrellas in C(4,2)=6 ways. The remaining two must exchange umbrellas, a unique assignment; giving either their own would give both their own. Thus6 assignments qualify. Choosing two correct recipients does not allow arbitrary assignments to the rest.

## Q3

**Correct answer:** 50

Let Monday's production be N. Its rejected count is0.2N. Tuesday rejects0.1(2N)=0.2N. Monday contributes half of the combined0.4N rejects, or50%. Rejection rates and contributions to the rejected total use different denominators.

## Q4

**Correct answer:** 4

Reflecting the punched centre across x=2 and y=2 gives centres(1,1),(1,3),(3,1),(3,3). Their hull is a square of side2 and area4. The area of the hull concerns the centres, not the total area removed by the small holes.

## Q5

**Correct answer:** A

R introduces the measurement, Q introduces repetition, P refers to that second measurement, and S draws the resulting decision. A has that sequence. B introduces repetition before the first measurement and delays its result; C begins with an unexplained second reading; D discusses a second reading before the repetition occurs. Pronoun references and cause–effect order constrain the sequence.

## Q6

**Correct answer:** 2.0000 (accepted range 1.99995–2.00005)

Let T be the draw on which the first blue appears. T can be1,2,3,4. The tail-sum identity gives E[T]=P(T>0)+P(T>1)+P(T>2)+P(T>3). These probabilities are1,3/5,(3/5)(2/4)=3/10, and(3/5)(2/4)(1/3)=1/10. Their sum is2. Drawing without replacement changes the probabilities after each red; a constant-probability geometric model is inappropriate.

## Q7

**Correct answer:** B

Suggestive evidence provides support without establishing certainty; a provisional recommendation can be revised. B preserves both meanings. A upgrades both to certainty and finality, C reverses the evidentiary direction, and D substitutes irrelevance and unanimity, neither stated. The qualifying words control the strength of the claim.

## Q8

**Correct answer:** 12

At time t hours the ratio is 2^(t/3)/3^(t/6)=(4/3)^(t/6). The target16/9=(4/3)² therefore occurs at t/6=2, or12 hours. Since the base4/3 exceeds1, the ratio increases strictly and this is the first such time. Comparing only the two named multiplication factors ignores their different time intervals.

## Q9

**Correct answer:** A, C, D

Substitution gives3,7,13, establishing A; at4 the rule gives16+4+1=21, proving D. The extra product vanishes at1,2,3 but not at4, so C is true and B false. Finite observations can support a pattern without uniquely determining its continuation.

## Q10

**Correct answer:** 24

The four top faces contribute4. Exterior vertical boundaries contribute twice the sum of all heights because each column has two outer sides:2(3+1+2+2)=16. Internal height differences contribute |3−1|+|2−2|+|3−2|+|1−2|=4. Thus the exposed area is4+16+4=24. Hidden interfaces between equal-height columns contribute no exposed area.


## Q11

**Correct answer:** A, C

For non-NULL a values, UNIQUE excludes repetitions, proving A. NOT NULL on b proves C but imposes no uniqueness, so B is false. Neither constraint requires every value to occur, so D is false. Constraints restrict stored rows; they do not populate absent rows.

## Q12

**Correct answer:** 12

Move5 to the root and remove its old final slot, leaving[5,7,4,12,9,6]. Its smaller child is4, so swap to get[4,7,5,12,9,6]. At index3,5≤6, so stop. Indices2 and3 contain7 and5, summing to12. Deleting the array's first element by shifting would not implement heap deletion.

## Q13

**Correct answer:** B, C

Incoming x is overwritten before use, so A is false. Incoming y is used to compute the new x and again in z, proving B. Both new x and y are needed by the second assignment, proving C. After z is assigned, only z is needed for the return, so D is false. Liveness concerns the current value's future use before redefinition, not whether the variable name occurs anywhere later.

## Q14

**Correct answer:** 0.7854 (accepted range 0.78535–0.78545)

Write the integral as I. Replacing x by1−x leaves the denominator unchanged and yields numerator1−x. Adding the two forms gives2I=∫0¹ dx/[x²+(1−x)²]. Put u=2x−1; the last integral becomes∫(−1 to1) du/(1+u²)=π/2. Hence I=π/4≈0.785398. Symmetry replaces the numerator, not the denominator by a constant.

## Q15

**Correct answer:** D

Substitute z=y: F=xy+(NOT x)y=y(x+NOT x)=y. Thus D is correct. A depends on an unrelated selector, B complements the required value, and C changes with x. When a multiplexer's two data inputs agree, its selector cannot affect its output.

## Q16

**Correct answer:** 2

References0 and1 miss into lines0 and1. Block4 replaces0. The next1 hits,0 misses and replaces4, and the final1 hits. There are2 hits. Conflicts in line0 do not evict block1 from its distinct line.

## Q17

**Correct answer:** B, C

Updating b changes the expression's operand value and kills the old a+b result's availability; C is true and A false. No operand changes between q and r, so r may reuse q, proving B. D ignores operand redefinitions. Common-subexpression elimination requires matching values, not merely matching text.

## Q18

**Correct answer:** 4

Alphabetical DFS follows a→b→d→c→e. At d, c is the next unvisited neighbour; at c, a and d are already visited. The tree path to e has four edges. The direct graph path a→c→e is shorter but is not the DFS-tree path requested.

## Q19

**Correct answer:** B, C

A cycle supplies an alternate route between e's endpoints, so deleting e preserves connectivity, proving B. If a spanning tree used e, deleting e creates a cut; another edge on the cycle crosses that cut and is lighter, permitting a lower-weight tree. Thus C is true and A false. A still heavier edge may lie elsewhere, so D is false. The exclusion concerns its cycle, not a global maximum.

## Q20

**Correct answer:** C

Forwarding onto a new Ethernet link requires a new frame with the router's outgoing source MAC address and the appropriate next-hop destination MAC address. C is correct. A describes end-to-end IPv4 addresses, B transport ports, and D application data, none of which this stated forwarding operation necessarily replaces. IPv4 TTL changes, but it is not one of the offered pairs.

## Q21

**Correct answer:** 1

After adding c, the three-edge route costs4+3c and the direct edge costs5+c. Direct is strictly cheaper when5+c<4+3c, or c>1/2. The smallest positive integer is1. Adding a constant per edge does not add the same amount to paths with different edge counts.

## Q22

**Correct answer:** A, C

Atomic operations serialize their counter updates. The first sees0 and sets1; the second sees1 and sets2. A,C follow, while B contradicts atomicity. A thread can start earlier but execute its atomic instruction later, refuting D. Thread start order is not the atomic operation's execution order.

## Q23

**Correct answer:** 3

The block needs64/8=8 transactions. Relinquishments occur after transactions2,4,6. At transaction8 the transfer finishes immediately, so it adds no precompletion relinquishment. Counting four two-transaction groups without excluding final completion produces an off-by-one error.

## Q24

**Correct answer:** 1.5

Each packet takes0.5 seconds per link. Packet1 uses the links over[0,0.5] and[0.5,1]; packet2 uses them over[0.5,1] and[1,1.5]. Completion is1.5 seconds. Store-and-forward prevents forwarding a packet before its full arrival, but different links can transmit different packets concurrently.

## Q25

**Correct answer:** A, C

Each aSb adds one of each symbol, SS concatenates strings with equal counts, and ε has equal counts; hence A. Taking each S in SS to ab generates abab, proving C and refuting B. Every generated prefix has at least as many a's as b's, preserved by both constructions, so ba is impossible and D false. Equal total counts alone do not describe the language completely.

## Q26

**Correct answer:** 4

Begin with A. A→B adds B, B→C adds C, and now AC→D applies, adding D. The closure is ABCD and has size4. A composite left side can become usable after other dependencies expand the closure.

## Q27

**Correct answer:** D

Q can progress and release S; P can then proceed. No request from Q leads back to P, so there is no cycle. D is correct. A equates waiting with deadlock, B invents a missing circular edge, and C invents a request not stated. A blocked process need not belong to a deadlock.

## Q28

**Correct answer:** 4

For low bits u,v the function is uv+(NOT u)(NOT v). Each product has two literals, giving4. Neither product can drop a low-bit literal without also covering an unequal-bit assignment. The unrestricted high bits disappear in minimization; retaining them would increase literal count needlessly.

## Q29

**Correct answer:** 0.8

With five observations and median0, one sorted observation is0. Every other squared observation is at most1. Mean0 makes population variance equal to the mean square, so it is at most4/5. The data−1,−1,0,1,1 achieve the bound and satisfy both mean and median conditions. Bounding each square without using the required zero would give an unattainable bound1.

## Q30

**Correct answer:** 8

The14 neighbour entries equal the total degree sum. The three given degrees sum to6, leaving14−6=8. The double recording is already included in14; doubling it again would count each edge four times.

## Q31

**Correct answer:** A, C, D

Since each element is its own inverse, (ab)^(−1)=b^(−1)a^(−1)=ba, proving A. If they commute, (ab)²=a²b²=e; ab≠e because a≠b, so its order is2, proving C. Conversely order2 gives ab=(ab)^(−1)=ba, proving D. Noncommuting transpositions in a permutation group satisfy the individual square conditions, refuting B. Individual involutions need not commute.

## Q32

**Correct answer:** A, B

A matching without cd cannot perfectly match either odd triangle. Thus any perfect matching must use cd, after which edges ab and ef complete one; A,B are true. Each triangle is an odd cycle, so C is false. Covering all edges inside each triangle requires at least two of its vertices, hence at least4 overall; choosing b,c,d,e achieves4, refuting D. Matching and vertex-cover sizes need not agree in a nonbipartite graph.

## Q33

**Correct answer:** 0

Two distinct flips toggle parity twice and restore even parity. Every one of the six pairs therefore escapes the check. An error-detecting parity bit detects odd-weight errors, not all nonzero errors.

## Q34

**Correct answer:** B

Every a adds a marker and every b removes one. Accepting only after input exhaustion and no unmatched markers enforces equal counts, so B is needed. A accepts prematurely, C wrongly excludes ε and does not enforce equal counts, and D discards the necessary count information. A correct recognizer also rejects an attempted pop without an unmatched marker.

## Q35

**Correct answer:** 4

Including4 excludes3 and5. Choose two remaining elements from{1,2,6,7}; the only prohibited pairs are{1,2} and{6,7}. Thus C(4,2)−2=4. They are{1,4,6},{1,4,7},{2,4,6},{2,4,7}. Avoiding neighbours of4 is necessary but not enough; the selected other pair must also be nonconsecutive.

## Q36

**Correct answer:** A, C, D

REAL accepts digits followed by a dot and zero further digits, so it consumes the two-character lexeme consisting of1 followed by a dot. This beats the one-character INTEGER, proving A. One dot remains before2; neither RANGE nor any other rule matches there, proving C. Priority resolves equal lengths at the same starting position; RANGE cannot start at the initial digit, so B is false. Requiring a digit after REAL's dot prevents that initial real match, allowing INTEGER1, RANGE.., INTEGER2, proving D. Longest match can consume punctuation needed by a later token.

## Q37

**Correct answer:** A, C

Appending b's can complete exactly strings a^i b^j with i≥j≥0, so K is that language. aaab has3≥1, proving A; abb has1<2 and cannot be repaired by more b's, refuting B. A grammar S→aSb | A, A→aA | ε generates K, proving C. For any i<j, the suffix b^j distinguishes prefixes a^i and a^j: only the latter completes a word in K. Infinitely many distinguishable prefixes imply nonregularity, refuting D. Right quotient by a regular language preserves context-freeness, but does not force regularity.

## Q38

**Correct answer:** 9

If k length-two tiles are used, there are6−2k unit tiles. These unit tiles create7−2k gaps, including both ends; put at most one long tile in each gap. Thus k=0 gives1, k=1 gives C(5,1)=5, k=2 gives C(3,2)=3, and k=3 is impossible. Total1+5+3=9. Counting unrestricted tilings would wrongly allow adjacent length-two tiles.

## Q39

**Correct answer:** 1

FIRST(B)={a,b}, so FOLLOW(A)={a,b}. A→aA enters cell(A,a); A→ε enters both(A,a) and(A,b), creating exactly one conflicting cell(A,a). The two B alternatives have disjoint FIRST sets{b} and{a}. S has only one production. The number of conflicted cells is1, even though the epsilon production populates two cells.

## Q40

**Correct answer:** 174

View R as a3×3 zero-one matrix. Every row must be nonzero, giving7³=343 matrices. Exclude matrices with an all-one column. For each specified all-one column the other six entries are free, giving2^6=64; for each pair of such columns,2^3=8; for all three,1. Inclusion–exclusion gives3·64−3·8+1=169 excluded matrices. Hence343−169=174. Once a column is all-one, the row condition is automatically satisfied; imposing it again on the remaining columns would undercount.

## Q41

**Correct answer:** B, C, D

Au=u−u(vᵀu)=0, so A is singular and A is false. If Ax=0 then x=u(vᵀx), putting x in span(u); conversely every such multiple is killed, proving B. Also vᵀA=0, so solvability requires vᵀb=0; when that holds, Ab=b and x=b works, proving C. Expanding A²=I−2uvᵀ+u(vᵀu)vᵀ=I−uvᵀ proves D. This is a projection, not necessarily an orthogonal projection because u and v need not coincide.

## Q42

**Correct answer:** B

Swapping q[0] and q[1] swaps the pointers only: they now point to v[0] and u[0]. Incrementing q[0] makes it point to v[1]. The assignment adds u[0]=1 to v[1]=4, leaving v[1]=5 and u[0]=1. B follows. A,D incorrectly change u[0]; C misses the final addition. Moving pointers does not move array elements.

## Q43

**Correct answer:** 14

The first instruction uses EX in cycle3. Instruction2 occupies EX in cycles4–6; subsequent EX occupancies are7 for instruction3,8 for instruction4,9–11 for instruction5, and12 for instruction6. Instruction6 then uses MEM13 and WB14. Equivalently, six ordinary instructions need6+4=10 cycles and the two extended EX occupancies add2 each. There is one shared EX resource, so the multiplications cannot overlap there.

## Q44

**Correct answer:** 4

R covers0,3 and S covers1,2, so together they cover all minterms at cost2+2=4. No single implicant covers all four minterms. Since every implicant costs at least2, every cover using at least two costs at least4. Thus the exhibited cover is optimal. Selecting the largest coverage row P first would lead to a cost5 cover and miss the lower literal cost.

## Q45

**Correct answer:** 5

Let C(n) count calls with argument2 within F(n). C(0)=C(1)=0 and C(2)=1. For n>2, C(n)=C(n−1)+C(n−2), so C(3)=1,C(4)=2,C(5)=3,C(6)=5. Counting distinct arguments would give one occurrence of2 and ignore repeated evaluation without memoization.

## Q46

**Correct answer:** 1032

The first effective address is1000+8·3+8=1032, so Rj=7. Then Ri=5. The second address is1000+8·5−8=1032. Addresses use byte offsets and the scale8 converts the index from words; treating the displacement as a word count would change both accesses.

## Q47

**Correct answer:** A, C, D

Bitwise NOT1111 is0000, so addition gives0111+0000+1=1000, without a fifth-bit carry. A is true and B false. Signed values are7−(−1)=8, outside the four-bit signed range, proving C. Unsigned values are7−15<0, requiring a borrow, proving D. Carry, unsigned borrow and signed overflow are related but distinct flags.

## Q48

**Correct answer:** 2.25

A runs0–5. At5, C's burst1 is shorter than B's2, so C runs5–6. D arrives at6 and runs6–7, then B runs7–9. Waiting times for A,B,C,D are0,6,3,0. Their average is9/4=2.25. Nonpreemptive scheduling does not interrupt A when shorter jobs arrive.

## Q49

**Correct answer:** 70

The head travels50→70 first, a distance20. The new request60 arrives behind the upward-moving head at65 and waits for reversal. It then travels70→60→20, a distance50. Total70. LOOK reverses at70 rather than travelling to the physical endpoint99, and the late request does not cause early reversal.

## Q50

**Correct answer:** 16

A rounds to16KiB at[0,16), B to16KiB at[16,32), and C to32KiB at[32,64). Freeing A releases its16KiB block. Its buddy is B's occupied block, so no coalescence is possible. The largest satisfiable request is16KiB. Total free capacity and largest contiguous buddy block are not interchangeable.

## Q51

**Correct answer:** 300

The latest collision indication requires a round trip of2·12=24 microseconds. At100×10^6 bits/s this corresponds to2400 bits, or300 bytes. Using the one-way delay would halve the required frame and could let transmission finish before collision detection.

## Q52

**Correct answer:** A, C

A establishes descending score order first; the later stable department sort groups departments while retaining that score order and original tie order within each. C directly uses the desired composite key and stability, so both work. B makes score the primary final key and can intermix departments. D reverses the original order of equal-key records, which later stable sorts retain rather than restore. Stable multi-pass sorting processes the least significant key first.

## Q53

**Correct answer:** 7

There are four distinct referenced data pages:7,19,44,80. Buffer retention permits one read of each despite multiple qualifying records. Adding3 index reads gives7. Charging one data-page read per record would overcount repeated pages; a noncovering index still requires fetching the distinct data pages.

## Q54

**Correct answer:** 21

The first pass gives prefix sums[1,3,6,10,15,21]. The descending second pass subtracts the still-unmodified preceding prefix from each entry, reconstructing[1,2,3,4,5,6]. Its sum is21. If the second pass ran upward, preceding entries would already be changed and would not be the needed prefixes.

## Q55

**Correct answer:** A, C

The first p symbols are all a, and y is nonempty within them, so A is true. Removing y decreases only the a count, establishing C for every permitted decomposition. A regular-language pumping guarantee is existential over a suitable decomposition; disproving one convenient decomposition is insufficient, so B is false. The pumping length must work for every sufficiently long language word and cannot be reset to suit later choices, refuting D. Correct quantifier order is essential.

## Q56

**Correct answer:** 5

The two NANDs producing u,v give v=p AND q, so F=NOT(pqr). With p stuck0, F is always1. With p stuck1, F=NOT(qr)=ac OR bc=c(a OR b). This is1 on exactly011,101,111, agreeing with the stuck0 copy there. On the other five assignments it is0, so the copies differ5 times. Comparing each faulty copy separately to the fault-free function would answer a different question.

## Q57

**Correct answer:** 13

The definition weights a newly appended bit by the length already seen, so the leftmost bit is least significant. For10110 the value is1·2^0+0·2^1+1·2^2+1·2^3+0·2^4=13. A usual left-to-right binary interpretation would give22, but the semantic rule here explicitly uses the opposite positional orientation.

## Q58

**Correct answer:** 9

Before failure X chooses Z at cost5+0=5, while Y's advertised7 is consistent with cost2 to X plus X's5. After the X–Z link fails, the stored alternative is2+7=9 via Y. That information is stale and creates a route pointing back toward X, but the stipulated distance-vector calculation still advertises9. Reasoning from actual current reachability rather than the stored advertisement would miss the specified protocol behaviour.

## Q59

**Correct answer:** 6

On MTU620 the maximum aligned payload is600, so the original payload becomes three600-byte fragments. On MTU420 the maximum aligned payload is400. Each existing600-byte fragment splits into400 and200 bytes; both are multiples of8, so the original-fragment more-fragments status is consistent even for a final piece of a nonfinal original fragment. Six fragments reach the destination. Recombining payload across first-hop fragment boundaries to obtain five fragments is not allowed without reassembly.

## Q60

**Correct answer:** A, C

Given a decider for L, compute the reduction f(M,w) and run that decider to decide HALT, proving C. Since HALT is undecidable, A follows. The reduction provides hardness, not an upper bound on L's recognizability, so B need not hold. Likewise it does not supply the reverse reduction in D. A one-way reduction must not be silently reversed.

## Q61

**Correct answer:** 2

Inserting35 changes the right leaf to[30,35,40,50], which splits into[30,35] and[40,50]; separator40 is added, leaving root keys[30,40]. Inserting45 yields[40,45,50] without overflow. Inserting15 yields[10,15,20] without overflow. The root thus retains2 separators and3 children. The copied key remains in its leaf; B+ leaf splitting does not remove it as a data key.

## Q62

**Correct answer:** 0.375

For x>0, rationalization gives f(x)=1/(sqrt(1+x)+1), whose limit at0 is1/2. Continuity therefore requires b=1/2. Its right derivative at0 is −1/[2sqrt(1+0)(sqrt(1+0)+1)²]=−1/8. The left derivative is a, so differentiability requires a=−1/8. Hence a+b=3/8=0.375. Matching only the function values establishes continuity but not differentiability.

## Q63

**Correct answer:** 2

Insertions place0,7,14,1 in slots0,1,2,3. Clearing slot1 makes a search for14 start at0, inspect key0, then stop at empty1 before reaching2. A search for1 starts at empty1 and also fails. Key0 remains findable immediately. Thus two stored keys become false absences. A tombstone would preserve continuation through the deleted slot.

## Q64

**Correct answer:** 3

Using old-state bits simultaneously gives00→01→11→00. The first positive return occurs after3 edges. Updating A and then using its new value for B would describe a different sequential computation, not this synchronous circuit.

## Q65

**Correct answer:** C

For outer value i=n/2^r, r=0..k, the inner loop executes r+1 times. The total is1+2+...+(k+1)=(k+1)(k+2)/2, or Θ(k²)=Θ((log n)²). Thus C is correct. A misses the growing inner count, while B,D overestimate it by treating geometric index values as linearly many iterations.
