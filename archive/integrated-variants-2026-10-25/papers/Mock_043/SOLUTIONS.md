# Worked Solutions — Mock Test 043

## Q1

**Correct answer:** C

The stated rise in evening visits and fall in morning visits establish a timing redistribution, C. Aggregate counts do not identify visitors, so A,B are not supported. Unchanged total visits do not rule out convenience or other benefits, so D is not supported. Visits and distinct users are different quantities.

## Q2

**Correct answer:** 6

Choose the two people receiving their own umbrellas in C(4,2)=6 ways. The remaining two must exchange umbrellas, a unique assignment; giving either their own would give both their own. Thus6 assignments qualify. Choosing two correct recipients does not allow arbitrary assignments to the rest.

## Q3

**Correct answer:** 4.8

**Concept:** Aggregate rate.

Combined revenue is 240 and combined items 50. The rate is 240/50=4.8. Averaging the separate daily rates 4 and 6 without their item weights would be incorrect.

**Common misconception:** Averaging ratios with unequal denominators.

## Q4

**Correct answer:** A

Concept: composition of reflections. Reflection across y=x swaps coordinates, giving (0,2). Reflection across x=1 changes x to 2−x, giving (2,2). A is correct. B changes the second coordinate incorrectly; C stops after the first reflection; D introduces an unwarranted vertical reflection. Reflection order matters.

## Q5

**Correct answer:** A

Q introduces the missing entries and the comparison. P supplies that comparison's result, S uses the result to restore the entries, and R verifies the completed restoration. Thus Q,P,S,R is coherent. B mentions the result before introducing the comparison, C restores using evidence not yet supplied, and D verifies restoration before it occurs. The explicit restrictions exclude an unstated earlier operation that might otherwise rescue a different order.

## Q6

**Correct answer:** B

**Concept:** General Aptitude — Elementary probability and statistics

1. In Bag I, P(RR)=6/15 and P(same)=7/15. In Bag II, P(RR)=1/10 and P(same)=4/10.
2. Before conditioning, P(RR)=(1/2)(6/15+1/10)=1/4, and P(same)=(1/2)(7/15+4/10)=13/30.
3. Since RR is a subset of same, P(RR | same)=(1/4)/(13/30)=15/26.

- **A:** Conditioning on same does not leave red and blue equally likely.
- **B:** The ratio of the mixture probabilities is 15/26.
- **C:** This is not the ratio P(RR)/P(same).
- **D:** Conditioning cannot be replaced by the initial proportion in a bag.

**Common misconception:** Conditional probabilities from different bags cannot be averaged without updating their weights.

## Q7

**Correct answer:** B

The assessor must attend carefully to evidence while lacking a financial stake, so the intended quality is impartiality(B). A contradicts careful examination; C concerns competence, which is not specified; D introduces a predetermined negative conclusion, contrary to impartiality. “Disinterested” in this context does not mean “uninterested.”

## Q8

**Correct answer:** 6

Concept: comparing geometric sums. After n days, A has 4(2ⁿ−1) units and B has (3ⁿ−1)/2. For n=1 through 5 these pairs are (4,1),(12,4),(28,13),(60,40),(124,121); B has not exceeded A. At n=6 they are (252,364), giving the first crossing. Comparing daily outputs alone would give an earlier, incorrect answer.

## Q9

**Correct answer:** C

**Concept:** Comparison groups and causal uncertainty.

A shared external factor is compatible with both decreases, so C states the justified limitation. A attributes the whole effect without isolating causes; B claims exact absence of an effect without adequate evidence; D extrapolates a universal relationship from one period.

**Common misconception:** Replacing an unsupported positive causal claim with an equally unsupported zero-effect claim.

## Q10

**Correct answer:** 72

The original exterior area is54. Removing the six face-centre cubes removes six outward faces, leaving48. Each of those removed cubes exposes four faces on retained adjacent cubes, adding24. Its inward neighbour is the removed central cube, so there is no additional retained face in that direction. The central cube's six neighbours are all removed. Total48+24=72. Count retained-to-empty interfaces, not the surfaces of removed cubes.

## Q11

**Correct answer:** A

**Concept:** Longest valid token prefix.

The longest valid initial token is >=, leaving >, so A follows. B invents an undeclared => token, C invents an undeclared full token, and D discards a valid trailing token.

**Common misconception:** Treating longest match as permission to create tokens absent from the lexical specification.

## Q12

**Correct answer:** 24

**Concept:** Alignment and final padding.

c occupies offset 0. i starts at 4 and occupies 4–7. d starts at 8 and occupies 8–15. e occupies 16. The end offset is 17, rounded up to 24 for eight-byte total alignment.

**Common misconception:** Summing object sizes without accounting for internal and trailing padding.

## Q13

**Correct answer:** 839

The fragment starts at75·8=600 bytes. Its240-byte payload occupies offsets600 through600+240−1=839. The final byte has an inclusive offset, one less than the next byte's position.

## Q14

**Correct answer:** C

Scores are(6+3)/3=3, (8+4)/4=3 and(5+1)/1=6. R has the largest, so C is correct; P,Q do not win and D incorrectly equates all scores. Waiting time is normalized by service demand.

## Q15

**Correct answer:** A, C

**Concept:** Scope and cost of interrupt masking.

A is the specified masking effect. An interrupt arriving during a longer masked interval may wait longer, proving C. Masking on one CPU does not stop other CPUs, refuting B, and it does not change ordinary memory operations into atomic multi-CPU operations, refuting D.

**Common misconception:** Treating local interrupt exclusion as a complete multiprocessor lock.

## Q16

**Correct answer:** A, B

Both forms derive only ab and ac, proving A. FIRST(A)={b} and FIRST(B)={c}, so one lookahead selects an X alternative, proving B. The original S alternatives both start with a, making C false. Left factoring changes common-prefix decision structure but does not generally eliminate ambiguity, making D false.

## Q17

**Correct answer:** B
**Concept:** SSTF fairness under ongoing arrivals.

Repeated nearby requests can always offer a shorter seek than the distant request. The scheduler can keep choosing them forever, proving B. A's bound ignores future arrivals. C confuses local efficiency with fairness. D only resolves equal distances and cannot defeat strictly nearer arrivals.

**Common misconception:** A finite queue argument cannot establish starvation freedom under unbounded new arrivals.

## Q18

**Correct answer:** B

The candidate keys are AB and AC: A must be present, and either B or C supplies the other via the dependencies. All attributes are prime. Thus C→B satisfies3NF through its prime right-hand attribute, but C is not a superkey, violating BCNF. B is correct; A confuses primeness with determinant superkey status. C mistakes determinant size for a partial dependency of a nonprime attribute, and D omits needed B or C.

## Q19

**Correct answer:** 3

Integrating the identity gives integral(f(x))+integral(f(1−x))=6. Substitution u=1−x makes the two integrals equal, so each is3. No pointwise symmetry of f itself is required.

## Q20

**Correct answer:** 1 (exact)
**Concept:** MST repair after an edge deletion.

Initially use AB=1, either AC or BC at 2, and either AD or CD at 3: weight 6. Without AB, both AC and BC are needed to connect B to A through C, together with a weight-three D edge, giving 7. Increase: one.

**Common misconception:** The cost increase is a replacement tradeoff, not the deleted edge's entire contribution.

## Q21

**Correct answer:** B
**Concept:** Heap deletion and sift-down.

Move 3 to the root and remove the last slot: [3,8,7,6,5,4]. Swap with larger child 8, then larger child 6, giving [8,6,7,3,5,4]. A unnecessarily sorts the keys; C violates root heap order; D swaps the wrong lower-level elements.

**Common misconception:** A heap is partially ordered; deleting its root does not sort the remaining array.

## Q22

**Correct answer:** 1

The flawed algorithm settles a at distance2, then t at4, before b at5. It refuses b's later improvement of a to1. The true path s→b→a→t has weight5−4+2=3. The excess is4−3=1. The graph has no cycle; a negative edge alone can invalidate Dijkstra's settling argument.

## Q23

**Correct answer:** 14336
**Concept:** Expanding opcodes.

Of 256 eight-bit prefixes, 56 remain after assigning 200 two-register opcodes. Each unused prefix can extend through all 256 patterns in the remaining eight bits. The maximum is 56×256=14336 no-operand instructions, with no collision with assigned register-format prefixes.

**Common misconception:** The register fields become opcode bits only under unused leading prefixes.

## Q24

**Correct answer:** 7.6 (exact)

**Concept:** Engineering Mathematics — Descriptive statistics

1. The combined mean is (3*2+2*7)/5=4.
2. The mean square in A is 2+2^2=6, and that in B is 1+7^2=50. The combined mean square is (3*6+2*50)/5=118/5.
3. Subtract the square of the combined mean: 118/5-16=38/5=7.6.

**Common misconception:** Pooling variances requires accounting for different group means as well as group sizes.

## Q25

**Correct answer:** 6

For idempotence, every image element y=f(x) must satisfy f(y)=y. Choose the two image elements in C(3,2)=3 ways and fix each. The remaining element may map to either of them, giving two choices. Total3×2=6. Merely choosing a two-element image does not complete the function; its non-image argument still needs an output.

## Q26

**Correct answer:** 3
**Concept:** Antichains and a chain-cover upper bound.

The set {4,5,6} is an antichain, establishing a lower bound of three. Partition the entire poset into chains {1,2,4}, {3,6}, and {5}. Any antichain contains at most one member of each chain, giving an upper bound of three. The maximum is exactly three.

**Common misconception:** Exhibiting a large antichain alone does not prove it is largest; an upper bound is also needed.

## Q27

**Correct answer:** A
**Concept:** Full-adder outputs.

With x=y=1, the total is 2+c. Its low bit is c and its carry is always one, yielding A. B incorrectly complements the sum; C,D incorrectly make carry depend on c.

**Common misconception:** Carry indicates a total of at least two, which is already guaranteed by x=y=1.

## Q28

**Correct answer:** 11

For x=0, odd y can be1,3,5,7, giving4 choices with z determined. For x=1 the same four choices fit. For x=2, y may be1,3,5, giving3. Total4+4+3=11. The upper bound on x and parity condition prevent direct unrestricted stars-and-bars counting.

## Q29

**Correct answer:** 4 (exact)
**Concept:** DFA residual states and the empty string.

Use the three remainder states with transition r→(2r+b) mod 3, accepting remainder 0. Add a separate nonaccepting initial state whose transitions on 0,1 go to remainders 0,1. All four are reachable.

Remainder 0 is distinguished from the others by the empty suffix. Remainders 1 and 2 are distinguished by suffix 1: only remainder 1 reaches zero. The initial state differs from remainders 1 and 2 by suffix 0, which it accepts but they reject. Thus four states are necessary as well as sufficient.

**Common misconception:** Rejecting the empty representation can require separating the initial state from numeric remainder zero.

## Q30

**Correct answer:** 20.5

**Concept:** Expected successful sequential search cost.

There are 1000/25=40 equally populated blocks, making the target block uniform among positions 1 through 40. Expected reads are (1+40)/2=20.5.

**Common misconception:** Using half the block count without the endpoint correction for a successful search.

## Q31

**Correct answer:** 17

Concept: indirect effective addressing. R1+8=108; its memory content is the effective address 200. Loading M[200] yields 17. Reporting 200 would omit the second dereference explicitly required by the instruction.

## Q32

**Correct answer:** B

**Concept:** Prefix block boundaries.

A /26 leaves six host bits, so this block covers final octets 128–191. Only 160 lies inside. A is below, C begins the next block, and D changes the preceding octet.

**Common misconception:** Including the first address of the next subnet in the current block.

## Q33

**Correct answer:** -4

011111 represents stored integer31. Incrementing modulo64 gives100000, the six-bit signed value−32. Scaling by1/8 yields−4. The arithmetic is wrapping, not saturating at the largest positive representable value.

## Q34

**Correct answer:** 4

Each diagonal entry counts two-edge walks returning to its vertex. The reciprocal pairs a,b and c,d each contribute two such walks. Other directed edges have no reverse partner, so trace(M²)=4. Ordinary multiplication counts walks, not Boolean reachability alone.

## Q35

**Correct answer:** D
**Concept:** Asymmetric signed range.

The eight-bit signed range is −128 to 127. Negating 10000000 wraps back to 10000000, although mathematical +128 is outside that range. Zero (A) also negates to itself but its negation is representable. 127 and −1 (B,C) have representable, different negatives. Only D satisfies both conditions.

**Common misconception:** Two's-complement ranges have one more negative value than positive values.

## Q36

**Correct answer:** A, C

Concept: external connection identity and checksum coverage. With identical public IP and remote endpoint, two simultaneous translated TCP connections need distinct external source ports (A). Distinct remote endpoints can disambiguate a reused external port if the NAT's mapping and lookup support that policy (C). TCP's checksum includes a pseudo-header containing IP addresses, so B is false. Two internal hosts may share a local source port, so D is false. A port is only one component of a connection identifier.

## Q37

**Correct answer:** 16 (exact)

**Concept:** Operating Systems — Virtual memory

Each second-level table covers 1024 virtual page numbers. Directory indices are floor(VPN/1024): the four mapped pages use indices 0,0,1,1023. Thus three distinct second-level tables are needed, in addition to one directory. Four pages times 4 KiB per page gives 16 KiB.

**Common misconception:** Four mapped data pages need not require four second-level tables; shared high-order address bits determine table reuse.

## Q38

**Correct answer:** B
**Concept:** Register coloring and an odd cycle.

A five-cycle has edges but no triangle, so its largest clique has size two. Alternating two colors around the cycle forces equal colors at the closing edge, making two registers insufficient. Three suffice, for example a=1,b=2,c=1,d=2,e=3. B is correct. A misses the odd-cycle obstruction; C,D invent a triangle, and D also overallocates registers.

**Common misconception:** The maximum clique gives a lower bound on required colors, not always an exact answer.

## Q39

**Correct answer:** 16

At total 10, the even number of 3-parts can be zero or two. Zero gives the single all-1 composition. Two consume 6 units, leaving four 1-parts; arranging these six parts gives C(6,2)=15. Total e10=16. More generally E(x) is one half of [1/(1−x−x³)+1/(1−x+x³)], since averaging cancels compositions with an odd number of 3-parts. Ordered compositions count arrangements, not merely partitions.

## Q40

**Correct answer:** B

Swapping q[0] and q[1] swaps the pointers only: they now point to v[0] and u[0]. Incrementing q[0] makes it point to v[1]. The assignment adds u[0]=1 to v[1]=4, leaving v[1]=5 and u[0]=1. B follows. A,D incorrectly change u[0]; C misses the final addition. Moving pointers does not move array elements.

## Q41

**Correct answer:** 2

The first symbol forces the production aSbS. Its displayed b can match the second or fourth symbol of abab. Matching the second leaves the inner S empty and the final S generating ab. Matching the fourth leaves the inner S generating ba and the final S empty. Each two-letter substring has one derivation, and the empty substring must use ε. Thus there are exactly two leftmost derivations. Different orders of expanding nonterminals are excluded by the leftmost requirement.

## Q42

**Correct answer:** 2

Concept: reconstructing a Boolean function from differences. The x difference condition gives F=xy XOR g(y,z), where g=F(0,y,z). The z difference then forces g=z XOR h(y). The specified value at 000 imposes h(0)=0, while h(1) remains free. The two functions are xy XOR z and xy XOR y XOR z. Both directly satisfy all constraints. A Boolean difference determines dependence on one variable but leaves a function of the others to be constrained.

## Q43

**Correct answer:** 18

Descending through three nonbase calls makes c=3; the base returns3. Unwinding, c becomes4 and returns3+4=7; then c=5 and return7+5=12; finally c=6 and return12+6=18. The shared counter is not restored on return.

## Q44

**Correct answer:** B

The first phase stores a prefix; the second must match its reverse, consuming one stack symbol per input symbol. A successful branch therefore divides an even-length palindrome equally. B is true. NPDA acceptance requires some successful branch, not every guess, disproving A. One stack is sufficient, disproving C. End-of-input remains mandatory, disproving D.

## Q45

**Correct answer:** A, B, D

Implication transitivity gives p→r, proving A. Its contrapositive is NOT r→NOT p, proving B. The premises prohibit p true with r false, proving D. The converse r→p need not hold, so C is false. Implication chains do not reverse direction.

## Q46

**Correct answer:** 100

ACK400 covers bytes through399, so the transmitted prefix100–399 is acknowledged. The half-open SACK block covers500–699. The only uncovered transmitted interval is400–499, containing100 bytes. Neither acknowledgment includes byte400 through the cumulative ACK, and the exclusive right endpoint700 is not a transmitted byte here.

## Q47

**Correct answer:** 3

Deleting6 leaves [8], below the two-key minimum. The right sibling [10,12,14] has three keys, so it lends10, yielding[8,10] and[12,14]. No leaf is merged and the root retains three children. Root separator values must be adjusted, but that does not alter the child count.

## Q48

**Correct answer:** 20

The exact unsigned sum is20. Low bits hold4 and carry-out1, reconstructing4+16=20. Carry-out restores the fifth bit omitted from the four-bit result.

## Q49

**Correct answer:** B

Concept: lexical versus dynamic scope. S is declared inside P, so its x is P's x, regardless of the R→S call chain. The two calls return 11 and 12, summing to 23 (B). A omits one increment's effect; C would increment Q's x instead, giving 21+22; D simply uses Q's unchanged value twice. Static links follow declarations, not the immediate caller.

## Q50

**Correct answer:** B

**Concept:** Computer Organization and Architecture — Hardwired and microprogrammed control

Five destinations have 2^5−1=31 nonempty subsets. There are 8×31=248 non-idle bus commands and one idle command, giving 249 commands. Since 128<249≤256, the joint bus field needs 8 bits. Independently, six ALU choices need 3 bits, 128 addresses need 7 bits, and four sequencing conditions need 2 bits. The total is 8+3+7+2=20 bits. A separate source field plus five literal destination-enable bits would consume more bits, but the question explicitly permits a joint binary command encoding.

- **A:** False: the other fields need 12 bits, leaving only seven bus-command bits, which cannot encode 249 commands.
- **B:** True: 8 bits for the 249 bus commands plus 3+7+2 bits for the other fields gives 20.
- **C:** False: 21 bits suffice but are not minimal; joint encoding uses eight bus bits instead of separately encoding source and destination enables.
- **D:** False: the command choices can be binary encoded; 20 bits already suffice.

**Common misconception:** When controls may be encoded jointly, count legal combined commands rather than blindly adding separate control-signal widths.

## Q51

**Correct answer:** A, B, D

The byte offset of B[i,j] is4(5j+i). Its i-stride is4 and j-stride20, proving A and B. A row-major traversal of B advances j first, so consecutive elements generally lie20 bytes apart; C is false. The defined index mapping gives B[2,1]=A[1,2] as aliases, proving D. A transpose view changes strides and index interpretation without rearranging the underlying storage.

## Q52

**Correct answer:** 9

After the key2 pass the order is E,A,C,D,B: A,C,D retain their original relative order within key2=1. The stable key1 pass yields D,B,E,A,C. Therefore A and C occupy positions 4 and 5, whose sum is 9. The last stable pass establishes the primary key; earlier ordering breaks its ties.

## Q53

**Correct answer:** B, C

The stream abc could split as a|bc or ab|c, so B is true. A length field can disambiguate such splits, proving C. TCP preserves bytes and order, not application record boundaries, so A,D are false. Network read sizes cannot replace a framing protocol.

## Q54

**Correct answer:** B
**Concept:** Probe-cycle length and coprimality.

The cycle length is 12/gcd(h2,12). It equals twelve exactly for h2=1,5,7,11. Four of eleven equally likely choices qualify, giving 4/11. A uses twelve rather than eleven choices; C counts non-coprime steps; D ignores short cycles.

**Common misconception:** A nonzero second hash is insufficient when the table size is composite.

## Q55

**Correct answer:** A, B, C

**Concept:** Prime implicants and forbidden expansion.

A covers 0,1; dropping a′ would add minterm 4, and dropping b′ would add 3, both OFF. B covers 2,6; dropping b adds 4 and dropping c′ adds 3, so it is prime. C covers 5,7; dropping a adds 3 and dropping c adds 4, so it is prime. D covers 0,1,4,5 and includes OFF minterm 4, so it is not even an implicant.

**Common misconception:** Checking only that a product covers some ON minterms without checking all of its coverage.

## Q56

**Correct answer:** 1

Subtract the first equation from each of the other two: (t−1)y=1 and(t−1)z=1. For t≠1 these uniquely fix y,z and then x, so the system is consistent with a unique solution. For t=1 both equations demand0=1, making it inconsistent. Exactly one parameter value is inconsistent. The quantity s(t) equals1 whenever a solution exists and does not remove the contradictory exceptional case.

## Q57

**Correct answer:** 1

**Concept:** Essential coverage and minimum covers.

Column 2 is covered only by P, making P mandatory. After P, columns 4,5,6 remain and R covers all three. No single implicant covers all columns, so {P,R} is a two-implicant optimum. Neither Q nor S alone completes P, making that minimum cover unique. The answer counts covers, not implicants, and is one.

**Common misconception:** Reporting the minimum number of implicants instead of the number of minimum covers.

## Q58

**Correct answer:** A, B, D

Since |f(x)|≤x², continuity at0 follows, making A true. The difference quotient f(x)/x=x sin(1/x) tends to0, proving B and D. For nonzero x, f'(x)=2x sin(1/x)−cos(1/x), whose cosine term oscillates without a limit at0; C is false. Differentiability does not force continuity of the derivative.

## Q59

**Correct answer:** A, B, C
**Concept:** Lossless BCNF decomposition versus dependency preservation.

The intersection is A, which determines R1=AB, proving losslessness (A). R1 has key A; R2 has no nontrivial projected dependency with a non-superkey determinant, so both are BCNF (B). To refute preservation of BC→A, take R1={(1,b),(2,b)} and R2={(1,c),(2,c)}. Both obey their projected dependencies, but their join contains (1,b,c),(2,b,c), violating BC→A (C). A alone cannot determine C in the original schema, so it is not a key (D is false).

**Common misconception:** Losslessness and dependency preservation are different properties.

## Q60

**Correct answer:** A

**Concept:** Databases — Concurrency control

Each upgrade needs an exclusive lock, which is incompatible with the other transaction's shared lock. Neither shared lock is released until commit, and neither transaction can progress to commit, so a deadlock is possible. Retaining exclusive locks until commit still prevents dirty reads by other properly locking transactions.

A correctly states both facts. B confuses compatibility of existing shared locks with compatibility of an exclusive upgrade. C is false: releasing the shared lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking. D is false: acquiring an exclusive lock before the read serializes the entire read-modify-write operation, preventing a lost update.

- **A:** True: deadlock is possible due to incompatible lock upgrades, but strict 2PL prevents dirty reads.
- **B:** False: confuses compatibility of existing shared locks with compatibility of exclusive lock upgrades.
- **C:** False: releasing a lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking.
- **D:** False: acquiring an exclusive lock before reading serializes transactions, preventing lost updates.

**Common misconception:** A serializability or recovery guarantee does not imply deadlock freedom.

## Q61

**Correct answer:** B
**Concept:** Bottom-up heap construction.

Processing index 3 swaps 3 with 7, producing [1,2,7,4,5,6,3]. Index 2 swaps 2 with 5, giving [1,5,7,4,2,6,3]. At index 1, swap 1 with 7 and then with 6, yielding [7,5,6,4,2,1,3]. The counts are 1+1+2=4, so B is correct. A counts only root repair, C misses one downward swap, and D overcounts the four actual exchanges.

**Common misconception:** Bottom-up construction first repairs child subtrees; the root must be traced using those updated values.

## Q62

**Correct answer:** B

**Concept:** Directory-link count versus open references.

Removing the two links removes names but the open descriptor still keeps the file available. Closing the last descriptor then leaves no links or open references, permitting reclamation, B. A leaves both a link and an open reference; C and D do not remove the remaining reference.

**Common misconception:** Equating removal of a filename with immediate destruction of an open file's storage.

## Q63

**Correct answer:** 5

Concept: stream framing across reads. Concatenated successful bytes are [3,65,66,67,2,68,69,0]. The first length 3 consumes payload 65,66,67 across two reads. The next length 2 consumes 68,69. Zero ends the stream. Payload total=3+2=5. EINTR contributes no bytes, and read boundaries are not record boundaries.

## Q64

**Correct answer:** B
**Concept:** Right quotient of a language.

Appending k zeros changes counts from (n0,n1) to (n0+k,n1). Equality requires k=n1−n0, which exists as a nonnegative integer exactly when n0≤n1. B is correct. A excludes strings fixable by appending zeros; C reverses the inequality; D wrongly includes w=0, which cannot be balanced by more zeros.

**Common misconception:** The suffix alphabet restricts which count imbalances can be repaired.

## Q65

**Correct answer:** 7
**Concept:** Resource-constrained instruction scheduling.

Run P on the multiplier during 0–3 and Q during 3–6. Compute R on the adder during 3–4, overlapping Q. Then S runs during 6–7. The multiplier's two operations require six cycles total, and S must follow the completion of both products through its dependencies, so finishing before seven is impossible. Seven is attained.

**Common misconception:** Parallel functional units permit overlap, but a final dependent operation still supplies a lower bound after the bottleneck resource finishes.

