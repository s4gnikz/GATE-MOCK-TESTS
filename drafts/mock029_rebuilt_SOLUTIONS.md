# Worked Solutions — Mock Test 029

## Q1

**Correct answer:** 3

M must be last because P precedes C and both C,K precede M. Among the first three events, P must precede C while K can be before both, between them, or after both. Orders are KPCM,PKCM,PCKM, giving3. No condition places calibration after permission unless the report states it.

## Q2

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

The conditioned orders are123,132,231, each equally likely. Only123 also has its second number below its third. Thus the probability is1/3. The two adjacent comparisons are not independent; they share the middle card.

## Q3

**Correct answer:** B

Contingent on means dependent on fulfilment of the condition, so B preserves the meaning. A removes the dependency, C substitutes a temporal statement, and D says the outcome holds regardless of the condition. A condition is not the same as a chronological relation.

## Q4

**Correct answer:** 12

8^5/4²=2^15/2^4=2^11. A power2^k has a1 followed by k zeroes in binary, so there are12 digits. The exponent counts trailing zeroes, not total digits.

## Q5

**Correct answer:** 9

The domain starts with3,5,7, all prime. The next odd integer9=3×3 is composite, so it is the smallest counterexample. The integer1 is excluded by the conjecture's domain and cannot serve as a counterexample to this statement.

## Q6

**Correct answer:** 5

Write the array as[[a,b],[c,d]]. Since the second row and second column have maxima1, b,c,d are at most1. The first row and first column maxima2 force a=2. Remaining conditions are max(c,d)=1 and max(b,d)=1. If d=1, b,c can each be0 or1, giving4 arrays. If d=0, both b,c must be1, giving1 more. Total5. Orthographic maxima do not uniquely determine hidden column heights.

## Q7

**Correct answer:** -50

From a1 to a101 there are100 updates. Group them as(1−2)+(3−4)+...+(99−100). Each of50 pairs contributes−1, so a101=−50. There are100 increments, not101, because the initial term is already specified.

## Q8

**Correct answer:** 22

Each square has perimeter16. Two sides of the first lie inside the other for lengths3 and2; two sides of the second lie inside the first for the same lengths. Remove those10 units from the summed perimeter32 to get22. The overlap area6 does not itself determine how much boundary to subtract without its side lengths.

## Q9

**Correct answer:** C

The subject immediately following the introductory participial phrase should be the person who performed the digitizing: the archivist. C supplies that subject and preserves the intended claim. A makes searching the apparent digitizer, B makes the facility the digitizer and changes the claim, and D makes the documents the digitizer. A passive main clause does not automatically repair a dangling introductory modifier.

## Q10

**Correct answer:** 10.9375

Initial salt mass is10kg. After evaporation,80kg of solution still contains10kg salt, so its concentration is12.5%. Removing10kg removes1.25kg salt, leaving8.75kg salt in70kg solution. Adding10kg water restores total mass80kg, so the final percentage is100·8.75/80=10.9375. Replacement restores the post-evaporation mass, not the original100kg.


## Q11

**Correct answer:** 4

Each diagonal entry counts two-edge walks returning to its vertex. The reciprocal pairs a,b and c,d each contribute two such walks. Other directed edges have no reverse partner, so trace(M²)=4. Ordinary multiplication counts walks, not Boolean reachability alone.

## Q12

**Correct answer:** A, C

The store's MEM stage follows the load's MEM stage by one cycle, allowing the stated bypass, proving A. Without it the store may have to wait for a register-file update, proving C. B contradicts the independent address assumption; D ignores the forwarding opportunity. A consumer's required stage determines the hazard.

## Q13

**Correct answer:** 6

All generated residues are even. They include0,4,8 from multiples of4, and6,10,2 after adding6. These are all six even residues. Nonnegative coefficients suffice because arithmetic wraps modulo12.

## Q14

**Correct answer:** B, C

A missing transition previously rejected the word, so its complement must accept it, proving C. Complete the original machine with a rejecting sink and then complement every state, including that sink: B. A leaves such words rejected; D wrongly leaves the new sink rejecting. Complementation requires total transition behaviour.

## Q15

**Correct answer:** 6

Every vertex loses one of its three edges, leaving degree2. The resulting six-vertex graph is a single cycle of length6. A spanning tree results by deleting any one of its six edges, giving6 trees. Degree2 alone would not guarantee one cycle for arbitrary larger bipartite graphs; here two separate simple bipartite cycles would require at least eight vertices.

## Q16

**Correct answer:** 9

There are C(6,2)=15 pairs of positions. Exactly six are adjacent pairs, including positions6 and1. Thus15−6=9. Rotational equivalence is not imposed.

## Q17

**Correct answer:** A, B, D

The store may change an operand, invalidating the earlier result, so A is true and C false. Excluding both aliases preserves the operands, proving B. Recomputing after the store uses their updated values, proving D. Availability depends on intervening effects.

## Q18

**Correct answer:** 1

The first edge sends7 to0. Thereafter the cycle is0,1,2,3,4,5. Thirteen further edges advance by13 modulo6=1, giving1. The initial invalid state contributes a transient step.

## Q19

**Correct answer:** A, C

The cycle cannot lie on any s-to-t walk, since no cycle vertex can reach t. Its repetitions therefore cannot lower the s-to-t cost, proving C; examples with no other negative cycles have finite distance, proving A. B incorrectly spreads its effect to all reachable vertices. D contradicts the stated existence of a path. A says “can,” not that other negative cycles are excluded.

## Q20

**Correct answer:** 2

NOT EXISTS retains A's1 and NULL: neither has a TRUE equality match in B. It rejects2. NOT IN retains none:2 has a match and the other comparisons involve UNKNOWN due to NULL. Counts2 and0 differ by2. UNKNOWN is not TRUE in a WHERE filter.

## Q21

**Correct answer:** 1

Reachable nonterminals are S,A,B. A is productive through a. B has no terminating production: every derivation retains B, so neither B nor S is productive. C is productive but unreachable. Only A satisfies both conditions, giving1. Reachability and productivity are independent checks.
## Q22

**Correct answer:** A, C

Wakeup does not certify the predicate, and another thread can act before mutex reacquisition, so A,C hold. B omits the needed recheck. D contradicts the specified reacquisition. Waiting should normally occur inside a predicate-checking loop.

## Q23

**Correct answer:** C

304 validates reuse of the stored representation rather than supplying a replacement body; C follows. A confuses status metadata with content, B confuses validation with deletion, and D assumes a body that the validation response does not supply.

## Q24

**Correct answer:** 8

p++ advances by one entire three-int row. Thus (*p)[1]=5 and p[-1][2]=3, summing to8. Pointer arithmetic scales by the pointed-to row type.

## Q25

**Correct answer:** 92

The base is104, after the four-byte instruction. The displacement is−3·4=−12 bytes. Target104−12=92. Both the reference point and displacement units matter.

## Q26

**Correct answer:** A, C

Each link supplies its own framing, so A,C are true. Its checksum must correspond to its own frame rather than blindly copying the incoming one, refuting B. Changing encapsulation does not require changing the application message, refuting D.

## Q27

**Correct answer:** 28

The real sum is1.75, represented by integer1.75·16=28. Its positive eight-bit code also has unsigned interpretation28. The requested answer is the code, not the real sum.

## Q28

**Correct answer:** A, C

Two's-complement overflow is carry into the sign bit XOR carry out, proving A. Opposite-signed operands produce a sum between them, so C is true. For four bits,1111+0001 has carry but no signed overflow, refuting B. A valid negative result refutes D.

## Q29

**Correct answer:** 0

The x5 coefficient is a5−a4−2a3, exactly zero by the recurrence. Indeed the full product equals1, since the initial x coefficient is a1−a0=0. Coefficient cancellation avoids computing the entire sequence.

## Q30

**Correct answer:** A, B

SET NULL attempts the null assignment, proving A, but NOT NULL then forbids it, proving B. Constraints do not silently override one another, refuting C. SET NULL is not CASCADE deletion, refuting D. Compatible referential actions and column constraints are necessary for the operation to succeed.

## Q31

**Correct answer:** 1

The first qualifying value7 is at position1; positions2 and3 also qualify but are not first. This is a lower-bound search, not an arbitrary successful match.

## Q32

**Correct answer:** A, C

Both instances are held and neither holder can release under the given rule, so A. An allowed release would supply the outstanding request of one process, proving C. B ignores exhaustion of all instances. D counts an already allocated instance as an additional available one.

## Q33

**Correct answer:** 2

At the first character, >> matches two characters; >>= does not match because the third character is >. The remaining >= is one token. Total2. Maximal munch is applied anew at each current position.

## Q34

**Correct answer:** A, C

A uniform truth of either predicate guarantees their pointwise disjunction, proving A. One common witness proves both existential claims, proving C. On domain{1,2}, let P hold only at1 and Q only at2: this refutes both B and D. Separate witnesses need not coincide.

## Q35

**Correct answer:** 6

Each of three id tokens reduces to T, accounting for3 reductions. The first T reduces to E, and each of two additions reduces E+T to E, adding3. Total6. Shifts are not reductions.

## Q36

**Correct answer:** 2

Work modulo2. (u+v)(v+w)+uw simplifies to uv+v+vw=v(u+1+w). It is1 precisely when v=1 and u=w, giving(0,1,0) and(1,1,1). The duplicate uw terms cancel in parity arithmetic.

## Q37

**Correct answer:** A, D

Matching consumes one input symbol per stored symbol, so a successful branch's guess splits the length equally, proving A. Immediate guessing accepts ε, proving D. Acceptance is existential, refuting B. Immediate guessing leaves no symbols to match a nonempty input, refuting C.

## Q38

**Correct answer:** 1

Near8 the spacing is2. The exact sum9 is a tie between8 and10, rounded to8 because its significand low bit is even. The first expression is therefore0. The value1−8=−7 is exactly representable with three significant bits, so the second expression becomes8−7=1 exactly. The absolute difference is1. Reassociation changes intermediate rounding.

## Q39

**Correct answer:** 7.3333 (accepted range 7.33325–7.33335)

Execution intervals are A0–2,B2–4,C4–5,A5–7,B7–8,A8–9. Completion times are A9,B8,C5, and all arrivals are0. Mean turnaround is22/3≈7.3333. Waiting time would additionally subtract CPU bursts.

## Q40

**Correct answer:** A, C

Rank is2 with three variables, so nullity is1: A true, D false. A consistent system's solutions are one particular solution plus that one-dimensional nullspace, an affine line, proving C and refuting B. Consistency does not imply uniqueness.

## Q41

**Correct answer:** 0.1667 (accepted range 0.16665–0.16675)

Taylor expansion gives exp(x)=1+x+x²/2+x³/6+O(x4). Thus f(x)=1/2+x/6+O(x²), requiring f(0)=1/2 and giving derivative1/6. The continuous extension value and its derivative are different coefficients.

## Q42

**Correct answer:** 18

Descending through three nonbase calls makes c=3; the base returns3. Unwinding, c becomes4 and returns3+4=7; then c=5 and return7+5=12; finally c=6 and return12+6=18. The shared counter is not restored on return.

## Q43

**Correct answer:** A, B, D

Expansion gives xz+(NOT x)y+yz; the consensus term yz is redundant, yielding A,B. If y=z, selection by x yields that common value, proving D. For x=1,y=0,z=1, F=1 while yz=0, refuting C.

## Q44

**Correct answer:** 3

h1(22)=0 and h2(22)=3. Probes visit0,3,6; the first two are occupied and6 is empty. Count includes that successful third probe. Occupied slots1 and5 are not on this prefix of the probe sequence.

## Q45

**Correct answer:** 80

Each of the40 entries gains exactly two bits, so capacity increases80 bits. The original next-address width is ceiling(log2 40)=6 and does not change. Recomputing the whole capacity is unnecessary for the difference.

## Q46

**Correct answer:** A, C, D

Doubling w gives even length, proving A. abba is an even palindrome but its halves ab and ba differ, refuting B. abab=(ab)(ab) is not a palindrome, proving C. Reversing ww gives reverse(w)reverse(w), proving D. Repetition and reflection are different symmetries.

## Q47

**Correct answer:** B, C

One word says nothing about a uniform bound and all sufficiently long words, proving B and refuting A. The pumping condition is necessary but not sufficient for regularity, proving C. To refute regularity with the lemma one must defeat every allowed decomposition of an appropriately chosen word, not merely one, refuting D.

## Q48

**Correct answer:** 90

The head chooses45 first (distance5), then70 (25 rather than35 to10), then10 (60). Total5+25+60=90. Nearest-first is recomputed at each new head position.

## Q49

**Correct answer:** 3072

The valid mappings use distinct frames3,7,9. Pages0 and4 alias frame3, so counting virtual pages would double-count its addresses. Three frames each supply1024 distinct byte addresses, total3072.

## Q50

**Correct answer:** A, C

Later by-reference accesses need live storage, proving A. Lifetime-preserving allocation or another valid mechanism can supply it, proving C. A dangling pointer to reused stack storage does not suffice, refuting B. Lexical visibility is not a storage-lifetime guarantee, refuting D.

## Q51

**Correct answer:** 2

The cycles are0→1→3→0 and2→5→4→2. They partition all six indices, so there are2 cycles. The omitted residue6 maps to itself in the full modulo7 mapping but is not an array index here.

## Q52

**Correct answer:** D

For k²≤i<(k+1)², the step is k and the band's width is2k+1. Thus a constant number of iterations suffices to leave each band, giving O(sqrt(n)) over the bands. Each step before termination is at most sqrt(n), while total increase must be at least n−1, giving Ω(sqrt(n)). Together this proves D. A is too small; B,C overestimate growth by treating the increment as constant. Perfect-square boundaries change step size gradually, not multiplicatively.
## Q53

**Correct answer:** 3.2

Serialization takes1200/600=2 seconds and1200/1200=1 second. Store-and-forward requires both for this one packet. Add two propagation delays of0.1, giving3.2 seconds. There is no packet splitting to permit overlapping transmission of separate packets.

## Q54

**Correct answer:** 3

Compute t=a+b, u=t*t, x=u+t: three binary operations. Sharing avoids reevaluating a+b. All three distinct required operations remain under this stated local optimization.

## Q55

**Correct answer:** A, C

C cannot be derived, so keys must contain it. A or B then determines the other, giving candidate keys AC,BC; A true and B false. Every attribute is prime, so the dependencies satisfy3NF, proving C. A and B individually are not superkeys, violating BCNF, refuting D. Prime right-hand attributes can permit3NF without BCNF.

## Q56

**Correct answer:** 6

The sparse index has100 entries, occupying100/20=5 pages. Fetching all five plus the one data page costs6 reads. The stipulated access strategy fetches the entire index; a different index search strategy would be a different cost model.

## Q57

**Correct answer:** 24

There are2·3=6 leaves, each with4 data entries, so24. Internal separator copies are routing metadata and are excluded from the data count.

## Q58

**Correct answer:** A, B

The error is explicitly a multiple of g, so its remainder is zero, proving A. Adding it to a valid codeword leaves a divisible polynomial, proving B. C contradicts this construction. The polynomial has three nonzero terms at shifted degrees, not one, refuting D. CRC detection depends on divisibility, not merely on nonzero errors.

## Q59

**Correct answer:** 16

Bits15–12 are fixed and bits7–0 must equal0x35. Four ignored bits11–8 can take any of16 patterns, yielding16 aliases. These do not represent additional device storage.

## Q60

**Correct answer:** 0.1944 (accepted range 0.19435–0.19445)

E[W]=P(X=Y=1)=1/6. E[Z]=1/2+1/3=5/6. ZW is2 when both succeed and0 otherwise, so E[ZW]=1/3. Covariance is1/3−(5/6)(1/6)=7/36≈0.194444. Independence of X,Y does not make their derived variables Z,W independent.

## Q61

**Correct answer:** 10

An idempotent function fixes every point in its image. Choose its nonempty image of size k, then send each remaining point to any image point. Count sum C(3,k)k^(3−k) for k=1,2,3:3+6+1=10. The image choices and fixed-point requirements are linked, not independent arbitrary mappings.

## Q62

**Correct answer:** 0.375

Six ordered pairs have absolute difference1: (0,1),(1,0),(1,2),(2,1),(2,3),(3,2). Out of16 equally likely pairs, probability6/16=0.375. Either station may have the larger counter.

## Q63

**Correct answer:** A, C

Exchanging selected lower-ratio weight for available higher-ratio weight improves value, proving the ratio rule in A. It fills whole items before at most one fractional final item, proving C. Absolute value ignores weight, refuting B. Indivisible packing may require a lower-ratio combination to use capacity better, refuting D; for capacity4, items(3,5),(2,3),(2,3) give such a counterexample.

## Q64

**Correct answer:** 3

The first write occupies a slot from0 until5; the second enters at1 and waits for memory, occupying the other slot. At cycle2 the buffer is full. The first completion at5 frees a slot, so the third store waits5−2=3 cycles. Excluding the in-service write would contradict the given capacity definition.

## Q65

**Correct answer:** 3

t saves C. Then B.next becomes E, and D.next becomes C, creating a separate C↔D cycle. From A the reachable chain is A→B→E→NULL, containing3 distinct nodes. The newly created cycle is not reachable from the head.

