# Worked Solutions — Mock Test 070

## Q1

**Correct answer:** A, C

An existing auditor is a reviewer and therefore not an intern, proving A. The same containment/exclusion argument applies to all auditors, proving C. Non-interns need not be auditors, so B is not implied. Nothing requires interns to exist, so D is not implied. Existential information must be carried only through justified set inclusions.

## Q2

**Correct answer:** 1

Reflection exchanges coordinates. C becomes(1,0), then(2,−1); B becomes(0,2), then(1,1). The requested difference is2−1=1. Apply translation after reflection, as specified.

## Q3

**Correct answer:** B

**Concept:** Different statistics describe different features.

The average improved while the largest delay increased, precisely B. A need not hold because a worse maximum exists. Such changes can coexist, refuting C, and they do not determine the median, refuting D.

**Common misconception:** Assuming a smaller mean forces every observation or every other statistic to decrease.

## Q4

**Correct answer:** 2

Fix one specified person to remove rotations. The other specified person must sit opposite. The two remaining distinct people can occupy the remaining seats in2! ways. Reflections are distinct, so these two are not identified.

## Q5

**Correct answer:** 50

Let Monday's production be N. Its rejected count is0.2N. Tuesday rejects0.1(2N)=0.2N. Monday contributes half of the combined0.4N rejects, or50%. Rejection rates and contributions to the rejected total use different denominators.

## Q6

**Correct answer:** 3

**Concept:** Unfolded cuts and connectivity.

The cut removes [1,2] and its reflection [10,11]. The remaining positive-length intervals are [0,1), (2,10), and (11,12], giving three pieces. Boundary conventions do not affect the count under the stated rule.

**Common misconception:** Counting cuts rather than resulting connected components.

## Q7

**Correct answer:** 4

Chronological order is S,Q,P,R. In the current order, the inverted pairs are(P,Q),(P,S),(Q,S),(R,S): four. Each adjacent exchange can remove at most one inversion, giving a lower bound of four. Move S left three places to obtain S,P,Q,R, then exchange P,Q; four operations attain the bound. Rearranging arbitrary distant paragraphs in one step is not allowed.

## Q8

**Correct answer:** 0.4444 (accepted range 0.44435–0.44445)

Of C(4,2)=6 equally likely ball pairs, two are monochromatic, so P(record1)=1/3 and P(record0)=2/3. Independent repetitions differ in either order, giving2×(1/3)(2/3)=4/9≈0.4444. Restoring the bag makes the repetitions independent despite dependence within each draw pair.

## Q9

**Correct answer:** 4
**Concept:** Tournament totals and a deficit invariant.

There are C(6,2)=15 matches. A decisive match contributes three points in total, whereas a draw contributes two. With no draws the total would be 45; each draw lowers it by one. Thus 45−41=4 matches were drawn.

**Common misconception:** A drawn match awards one point to each of two teams, not one point in total.

## Q10

**Correct answer:** 8

Divisibility by6 forces a≥1 and b≥1. For b=1, the bound2^a≤24 permits a=1,2,3,4. For b=2, it permits2^a≤8, giving three choices. For b=3, only a=1 works; b≥4 permits none. Unique prime factorization makes these4+3+1=8 distinct integers. The bound N≤72 does not require N to divide72.

## Q11

**Correct answer:** 6

The call chain is F(7),G(5),F(4),G(2),F(1),G(−1). The last returns1 and each of the five preceding calls adds1, so F(7)=6. The two functions reduce their arguments by different amounts.

## Q12

**Correct answer:** 4

Concept: overlapping copies. The preserved source sequence 1,2,3,4 replaces positions 2,3,4,5, giving [1,2,1,2,3,4]. Position 5 contains four. A naive forward assignment loop would not implement the stated overlap-preserving semantics.

## Q13

**Correct answer:** 2
**Concept:** In-order acceptance across sequence wraparound.

The first 15 is discarded; 14 is accepted, making 15 expected. The first 0 is discarded; then 15 is accepted, followed by 0 and 1. The next expected value is 2. Discarded frames do not remain buffered under the given rule.

**Common misconception:** This receiver cannot advance through a previously discarded out-of-order frame when a gap later closes.

## Q14

**Correct answer:** 988

The eight-bit signed displacement11111100 represents−4. Scaling gives−16 bytes; the PC base is1000+4=1004. The target is1004−16=988. Both sign extension and the specified next-instruction PC convention affect the answer.

## Q15

**Correct answer:** B

Lexical scope identifies Outer regardless of which procedure calls Inner, so the static link in B locates the intended activation. A follows call history to Caller. C follows recency without lexical meaning. D cannot by itself locate a non-global activation's local x. Dynamic and static nesting need not coincide.

## Q16

**Correct answer:** A, C

Atomic operations serialize their counter updates. The first sees0 and sets1; the second sees1 and sets2. A,C follow, while B contradicts atomicity. A thread can start earlier but execute its atomic instruction later, refuting D. Thread start order is not the atomic operation's execution order.

## Q17

**Correct answer:** 2

**Concept:** Articulation vertices.

Removing c separates the a,b edge from d,e. Removing d separates e from the triangle. Removing a or b leaves a connected path through the other triangle vertices; removing endpoint e also leaves a connected graph. Exactly c,d qualify.

**Common misconception:** Equating all vertices incident on cycle edges with articulation points.

## Q18

**Correct answer:** A, B

The full sum is A+(2^w−1−B)+1=A−B+2^w, so its low bits give the modular difference, proving A. Its carry-out is1 precisely when A≥B, the no-borrow case, proving B. This does not diagnose signed overflow, making C false. Identical low differences can arise with and without borrow, disproving D.

## Q19

**Correct answer:** 2

NOT EXISTS retains A's1 and NULL: neither has a TRUE equality match in B. It rejects2. NOT IN retains none:2 has a match and the other comparisons involve UNKNOWN due to NULL. Counts2 and0 differ by2. UNKNOWN is not TRUE in a WHERE filter.

## Q20

**Correct answer:** 4

Alphabetical DFS follows a→b→d→c→e. At d, c is the next unvisited neighbour; at c, a and d are already visited. The tree path to e has four edges. The direct graph path a→c→e is shorter but is not the DFS-tree path requested.

## Q21

**Correct answer:** 6

**Concept:** Surjections by excluding constant maps.

There are 2³=8 functions in total. Exactly two omit a target element: the two constant maps. The remaining six are onto.

**Common misconception:** Treating distinct domain elements as indistinguishable.

## Q22

**Correct answer:** 4

A can produce0,1,2 or3 copies of a, with B producing the remainder. Each split has a unique parse within A and B, giving four trees. Although each component grammar is unambiguous, their concatenation has an ambiguous boundary.

## Q23

**Correct answer:** 160

Divide by2^n and set bn=an/2^n. The recurrence becomes bn=b(n−1)+1 with b0=0, so bn=n. Hence a5=5×32=160. The forcing term grows at the same rate as the homogeneous multiplier and contributes the additional factor n.

## Q24

**Correct answer:** A, C, D

The nullable foreign key permits NULL, proving A. A non-null value must match an existing id, proving D; its own id is a possible match, proving C. Mutual references between two existing rows also satisfy the foreign key, disproving B. Referential integrity does not impose an acyclic hierarchy.

## Q25

**Correct answer:** B

**Concept:** Summing work across geometric loop strides.

For strides 1,2,…,n, the inner counts are n,n/2,…,1. Their sum is 2n−1, hence Θ(n). A ignores inner work; C assumes every outer iteration costs n; D likewise fails to account for increasing strides and overcounts further.

**Common misconception:** Multiplying independent-looking loop bounds when the inner bound depends on the outer variable.

## Q26

**Correct answer:** 2

One resource remains free. It can satisfy either process's outstanding request; that process then finishes and releases its two resources. Both processes are possible first finishers, so the answer is2. Holding one resource each does not imply deadlock while a suitable resource is still free.

## Q27

**Correct answer:** A, C

Negating NOT p OR q gives p AND NOT q, so A is true. Under p=true, p XOR q equals NOT q; under p=false, conjunction with p is false, proving C equivalent. B is the original implication and D represents the opposite asymmetric case.

## Q28

**Correct answer:** A

**Concept:** Preserving expression availability across unrelated assignments.

Neither a nor b changes between t and u, so t is the correct replacement, A. c=d+e need not equal a+b, refuting B and C. D leaves a use of an undefined replacement value.

**Common misconception:** Assuming every intervening assignment invalidates every available expression.

## Q29

**Correct answer:** 6 (exact)
**Concept:** Process creation and inherited control flow.

The first fork creates two processes. Only its child has p=0, so the conditional fork increases the population to three. Every one of these three executes the unconditional final fork, giving six processes reaching work().

**Common misconception:** Not every fork in source code is executed by the same set of processes.

## Q30

**Correct answer:** 3

Simultaneous updates give 00→01→11→00. There are three distinct states. In particular, B' uses the old A, not A' computed at the same edge.

## Q31

**Correct answer:** 16

Every binary word can be split into initial a's followed by zero or more blocks consisting of b and the run of a's immediately after it. Thus the expression denotes all words over {a,b}, and there are 2^4=16 length-four words. Repeated stars do not impose a limit on the number of b's.

## Q32

**Correct answer:** 3

The midpoints are3,1,0. The first two comparisons move r to3 then1; the third sees1<2 and moves l to1. The interval is then empty. Total3 comparisons. The equal values require searching toward the left boundary, not returning at the first equality.

## Q33

**Correct answer:** 1.160 (range 1.1595–1.1605)
**Concept:** Identifying a binomial parameter.

The equality is (1−p)⁴=6p²(1−p)². Since 0<p<1, cancel (1−p)² and take positive square roots: 1−p=√6 p. Thus p=1/(1+√6), and E[X]=4p≈1.159591794, rounding to 1.160.

**Common misconception:** A binomial probability includes the combinatorial factor C(4,2)=6.

## Q34

**Correct answer:** 4096

An address selecting one of256 words needs8 bits. Add eight independent control bits for16 per word. Total256×16=4096 bits. The word count and word width must both be included.

## Q35

**Correct answer:** 0.21875 (five decimals)
**Concept:** Independent backoff events.

Either the first chooses zero and the second does not, or vice versa. These disjoint cases give 2×(1/8)×(7/8)=7/32=0.21875.

**Common misconception:** “Exactly one” excludes the case in which both stations choose zero.

## Q36

**Correct answer:** 48

Concept: online SCAN arrivals. The head reaches 99 at time 49. At time 30 it is already at 80, so the new track-70 request waits for reversal. Returning from 99 to 70 takes 29 ms, giving service time 78. Waiting since arrival is 78−30=48 ms. LOOK would reverse differently; the stated physical-endpoint rule must be used.

## Q37

**Correct answer:** A, B, D
**Concept:** Array pointer arithmetic boundaries.

p+4 points to the last element (A). p+5 is the permitted one-past pointer (B), though dereferencing it would be invalid. Subtracting two from that pointer returns to element 3 (D). p+6 lies beyond the allowed array-or-one-past range, so even forming it is not permitted (C false).

**Common misconception:** A pointer may be valid to form but invalid to dereference.

## Q38

**Correct answer:** 21

**Concept:** Floyd meeting time and reset phase.

Once both pointers are in the cycle, their positions agree when the slow step count is a multiple of five. The first such count at least the prefix length three is five, so phase one has five iterations and 15 traversals. Resetting one pointer to the head makes them meet at the entry after three paired steps, adding six traversals. Total 21.

**Common misconception:** Counting iterations as traversals or counting the pointer reset as walking the prefix.

## Q39

**Correct answer:** A, C

Tabular combination requires identical dash positions and exactly one differing fixed bit. A combines {0,1} and {2,3}; its cube covers precisely four ON minterms. C combines {0,2} with {8,10}; allowing the don't-care 10 gives the valid cube {0,2,8,10}. B's inputs have different dash positions and different sizes. Its proposed cube also includes OFF minterm 11. D likewise combines unequal dash patterns, and its proposed cube includes 11. Thus A and C are valid; B and D are invalid. Don't-care minterms may assist grouping, but OFF minterms never may.

## Q40

**Correct answer:** 5

Unused space inside the allocated partitions is8−7=1,12−10=2 and20−18=2 KiB, summing5. This is internal waste within allocated partitions, not separate free holes.

## Q41

**Correct answer:** 18

**Concept:** Undetected patterns under row and column parity.

Every affected row and column must contain an even number of flipped bits. With four distinct data-bit errors, this forces the four corners of a rectangle: two chosen rows and two chosen columns. There are choose(3,2)choose(4,2)=3×6=18 such patterns. Each rectangle flips two bits in every affected row and column, so all pass parity checks.

**Common misconception:** Assuming two-dimensional parity detects every four-bit error.

## Q42

**Correct answer:** 2

Addresses6,7 map to local row floor(address/4)=1; addresses8,9 map to row2. The banks are2,3,0,1, but only two distinct rows are involved. An unaligned word may cross a local-row boundary even when each byte maps to a different bank.

## Q43

**Correct answer:** 86

Normalize original time to100 units. Memory stalls become40/2=20; other time becomes60×1.1=66. Total86 units, or86% of original time. Applying the10% slowdown to the entire workload would overstate the penalty.

## Q44

**Correct answer:** -2

There are six monotone paths. In move order RRDD,RDRD,RDDR,DRRD,DRDR,DDRR, their best costs after zeroing one visited cell are4,−1,−2,−2,−2,4. Thus the minimum is−2. For example RDDR visits costs0,5,−4,2,0 and zeroes5. A dynamic program can track whether the replacement has already been used. Zeroing the negative cost would increase, not reduce, the sum.

## Q45

**Correct answer:** 5.3333 (range 5.33325–5.33335)

**Concept:** Nonpreemptive scheduling with later arrivals.

J1 starts at zero and runs to five. Both others are then ready, so J3 runs 5–6 and J2 runs 6–8. Turnaround times are 5,7,4 respectively, averaging 16/3=5.333333…. Accepted range: 5.33325–5.33335.

**Common misconception:** Preempting J1 when a shorter job arrives despite the nonpreemptive policy.

## Q46

**Correct answer:** 6

**Concept:** Grammar generation and distinct terminal strings.

Each nonempty production introduces one a and one b, so length-four strings must have two of each: there are at most choose(4,2)=6. All six are generated: aabb via a(S=ab)b(S=ε); abab via a(S=ε)b(S=ab); abba via a(S=ε)b(S=ba); and their symbol-swapped versions bbaa,baba,baab using the second production. Thus the count is six regardless of ambiguity.

**Common misconception:** Counting parse trees or assuming the balance condition alone proves all balanced strings are generated.

## Q47

**Correct answer:** B, C

A conditional can avoid evaluating an unsafe expression. Unconditionally evaluating it can introduce invalid division even if the eventual selected arithmetic value seems unchanged. Hence B,C are true and A false. D is false precisely because branch removal can introduce extra evaluations. Safety and side effects must be checked in addition to value identities; the stated proof is relevant, not a universal sufficient condition for all transformations.

## Q48

**Correct answer:** A, C

**Concept:** Stack recognition and homomorphism closure.

A deterministic PDA pushes the prefix until #, then pops and compares each following bit, accepting exactly on a complete match; thus A holds. Mapping # to ε is a homomorphism, and CFLs are closed under homomorphism, proving C. A finite automaton cannot remember arbitrary prefixes: distinct prefixes x,y are distinguished by suffix #xᴿ, so infinitely many distinguishable prefixes refute regularity in B. D confuses individually finite inputs with a uniform finite memory bound.

**Common misconception:** Believing a visible midpoint removes the need to remember unbounded prefix content.

## Q49

**Correct answer:** 6

Concept: block boundary accounting. Starting at slot 7 leaves three records in the first block; the remaining twenty fill two more blocks. Data reads=3. Add the three distinct index reads for a total of six. Dividing 23 by ten and rounding happens to give three here, but the starting offset must still be checked: generally use ceil((offset+count)/capacity).

## Q50

**Correct answer:** 7

Concept: tournament certificates for second maximum. Only keys directly defeated by the overall winner can be second largest; every other key lost to another nonmaximum key. Here there are exactly two such candidates. One further comparison determines the larger, and in the worst case that comparison is necessary because their mutual order is not fixed by the separate winning subtrees. Total=6+1=7. The winner's path length, not just total input size, controls the final selection cost.

## Q51

**Correct answer:** 80

**Concept:** Interleaving subtree insertion sequences.

Root 4 must be first. Choose three of the remaining six positions for left-subtree keys, in choose(6,3)=20 ways. Within the left subtree, 2 must precede 1 and 3, whose order has two choices. The right subtree similarly has two orders after 6. Total 20×2×2=80.

**Common misconception:** Requiring all left-subtree insertions to precede all right-subtree insertions.

## Q52

**Correct answer:** 64

The first write to each of the two blocks causes one16-byte write-allocate fetch, totaling32 bytes. The other two writes hit those lines. Flushing writes the two dirty blocks once each, adding32 bytes. Total traffic is64 bytes. One-byte stores do not imply one-byte memory transfers under the given full-block policy.

## Q53

**Correct answer:** 2

Each block holds4000/80=50 records, so the file has20 data blocks. Its20 sparse entries occupy320 bytes and fit in one index block. A successful lookup reads that block and one data block: two reads. Record count affects index size, but does not require scanning all data blocks.

## Q54

**Correct answer:** 5
**Concept:** Counting trees with required and forbidden edges.

K4 has 4²=16 spanning trees, each with three edges. By symmetry each of six edges belongs to 16×3/6=8 trees. Trees containing both AB and AC already connect A,B,C; D may attach by AD,BD,or CD, giving three trees. Thus trees containing AB but not AC number 8−3=5. The subtraction concerns the intersection of the required and forbidden conditions.

**Common misconception:** Required edges sharing a vertex do not behave like independent events in a uniformly selected spanning tree.

## Q55

**Correct answer:** 3

Concept: head-of-line blocking. Under FIFO, A blocks B while O1 is unavailable in slots 1–2. I1 wins O1 in slot 3 and sends A. B then uses O2 in slot 4, concurrently with C on O1. With separate output queues, B is eligible immediately and leaves in slot 1. Departure-slot difference=4−1=3. An idle output alone does not imply that a FIFO input exposes a packet for it.

## Q56

**Correct answer:** 5 (exact)

**Concept:** Engineering Mathematics — Counting

1. First label the six positions. Without adjacency restrictions there are 6!/(2!2!2!)=90 colourings. For a given colour to occupy adjacent positions, choose its edge in 6 ways and place the other two pairs in 6 ways: 36 colourings.
2. For two specified colours both to be adjacent, choose the first edge in 6 ways and a disjoint edge in 3 ways: 18. For all three pairs to be adjacent, choose one of the two perfect matchings of the 6-cycle, then assign the colours in 3!=6 ways: 12. Inclusion-exclusion gives 90-3*36+3*18-12=24 valid labelled colourings.
3. Six of these have the form XYZXYZ, where X,Y,Z are different. They have rotation orbits of size 3, giving two arrangements. Every other valid colouring has six distinct rotations: periods 1 and 2 are incompatible with two of each colour. The other 18 colourings give three arrangements.
4. Total arrangements = 2+3=5.

**Common misconception:** Dividing by six blindly fails when some colourings have rotational symmetry.

## Q57

**Correct answer:** A, B

The assignment x=0 proves the condition true. The other branch and input call are unreachable, and y=4 gives z=16. Thus A,B. C would execute dead code unnecessarily and alter behavior; D ignores feasibility and confuses syntactic assignment presence with possible execution. Reachability can increase the precision of constant propagation.

## Q58

**Correct answer:** A, C

A selects a subset of finite R. C is exactly membership in R because its witness must equal x, so it too is finite. B is the complement of the finite union R∪S and is infinite. D is true for every x when S is empty, hence need not be finite. Quantifying over an empty relation can turn a universal condition into an unbounded result.

## Q59

**Correct answer:** 2

**Concept:** Full binary-tree leaf identities.

With i internal nodes and l leaves, l=i+1 and i+l=19, giving l=10. The four internal nodes with two leaf children account for eight leaves whose siblings are leaves. The other two leaves each have an internal-node sibling.

**Common misconception:** Counting parents rather than leaves when subtracting the sibling pairs.

## Q60

**Correct answer:** A, D

Concept: closure and its limits. If Lᴿ were context-free, reversing again would make L context-free, a contradiction; A holds. Erasing every symbol maps nonempty L to {ε}, which is regular; non-context-free L is necessarily nonempty. Thus D holds and B fails. Intersecting with the empty regular language gives the empty context-free language, disproving C. Closure theorems must be applied in the correct direction.

## Q61

**Correct answer:** D

Changing the IPv4 source address affects the IPv4 header checksum. The TCP checksum covers both its header, including the source port, and a pseudo-header containing IP addresses, so it also changes. D is correct. A omits TCP's pseudo-header/header changes; B omits the IP header change; C wrongly treats checksums as covering only payload. Incremental checksum updates are possible, but both fields require adjustment.

## Q62

**Correct answer:** 6
**Concept:** Isolated on-set minterms.

There are C(4,2)=6 on-set minterms. Flipping any one bit changes Hamming weight to one or three, both off-set. Therefore no implicant can omit even one literal without covering a forbidden neighbour. Each product term covers just one on-set minterm, so exactly six terms are necessary and sufficient.

**Common misconception:** A visually symmetric function need not have a compact two-level SOP representation.

## Q63

**Correct answer:** B, D

Concept: determinant and augmented consistency. Expansion gives det A=1+a³, B, nonzero for real a≠−1, disproving A. At −1 the rows sum to zero but the first two are independent, so rank is two, D. The right-hand sides sum to three, contradicting that row dependency; the displayed system is inconsistent, not infinitely soluble, so C is false. A singular matrix alone does not determine the number of solutions.

## Q64

**Correct answer:** A, C

Signed overflow is carry into the sign position XOR carry out, so A is true. Equivalently it occurs when equal-sign operands produce the opposite sign, exactly C's formula. Carry-out alone is unsigned overflow: all-ones plus1 has carry-out1 but represents−1+1=0 without signed overflow, disproving B. Opposite-sign addition cannot overflow, while D is1 exactly for opposite signs, so D is false. Unsigned and signed interpretations use the same bits but different range tests.

## Q65

**Correct answer:** 54

Concept: rank-one eigenspaces. For any x in the three-dimensional kernel of vᵀ, Ax=x. Also Au=u+u(vᵀu)=0. Since vᵀu≠0, u is outside that kernel, completing a basis. Thus A has eigenvalues 1,1,1,0; A+2I has 3,3,3,2. Determinant=3³·2=54. Adding 2I shifts every eigenvalue, not the determinant by two.

