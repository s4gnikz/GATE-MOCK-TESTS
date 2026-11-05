# Worked Solutions — Mock Test 045

## Q1

**Correct answer:** A

**Concept:** Cause, intermediate effect, observation, interpretation.

Q disconnects power; S describes the lost signal; P is the alarm response; R interprets the test. B places the response first, C begins with a consequence before its cause, and D states the conclusion before the observed result. A gives the causal order.

**Common misconception:** Ignoring the events referred to by “then” and “this”.

## Q2

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

The conditioned orders are123,132,231, each equally likely. Only123 also has its second number below its third. Thus the probability is1/3. The two adjacent comparisons are not independent; they share the middle card.

## Q3

**Correct answer:** B

**Concept:** Contextual vocabulary.

A conclusion open to revision is tentative, B. Irrevocable means it cannot be reversed; unrelated concerns relevance; unanimous concerns agreement among people. None of A,C,D expresses the stated revisability.

**Common misconception:** Selecting a word associated with authority rather than with uncertainty.

## Q4

**Correct answer:** 4.25

Let t=log_2(x), so t≠0. Change of base gives log_x(16)=4/t. Thus t²=4, with t=2 or −2, giving x=4 or 1/4. Both are positive and different from 1. Their sum is 17/4=4.25. Logarithm bases below 1 are valid; discarding the negative value of t would lose a solution.

## Q5

**Correct answer:** B

**Concept:** Induction versus universal deduction.

The observations support a tentative pattern restricted to the observed circumstances, as B says. A generalizes across every route and bus; C makes an unsupported dry-weather claim; D treats association as proof of a unique cause. None of those stronger claims follows.

**Common misconception:** Turning repeated observations into a logically necessary universal statement.

## Q6

**Correct answer:** A, B, C

The bounds on row 2 and column 2 force h(1,1)=3. The other three heights are each 1 or 2, with at least one 2 in row 2 and at least one 2 in column 2. Heights arranged as [3,1;1,2], [3,2;1,2], and [3,2;2,2] satisfy all views and give totals 7,8,9, proving A,B,C. The componentwise upper bounds sum to 9, excluding D. Projection maxima constrain columns but do not uniquely determine volume.

## Q7

**Correct answer:** 0.6444 (accepted range 0.64435–0.64445)

Use1/[n(n+2)]=(1/2)(1/n−1/(n+2)). All middle terms cancel, leaving(1/2)(1+1/2−1/9−1/10)=29/45≈0.644444. The gap of two leaves two terms at each end, not just one.

## Q8

**Correct answer:** 256

Concept: constrained optimization over integers. The volume is V(x)=x(20−2x)(12−2x). Positive dimensions restrict x to 1,2,3,4,5. Corresponding volumes are 180,256,252,192,100; the maximum is 256 at x=2. The maximizing integer must be checked rather than reporting an unconstrained stationary point.

## Q9

**Correct answer:** B
**Concept:** Adjacency blocks with relative-order constraints.

Treat PQ as one block. Among R,PQ,S their order is fixed. Insert unrestricted T into one of the four gaps before, between, or after those three objects. Each insertion produces a distinct valid schedule, giving 4. A,C,D miscount the available positions.

**Common misconception:** The PQ block has a fixed internal order and must not be multiplied by 2!.

## Q10

**Correct answer:** 24
**Concept:** Adjacency exclusion.

Choose C's end seat in two ways. For each choice, the four remaining people have 4!=24 orders, of which 2×3!=12 place AB or BA together as a block. Therefore 2(24−12)=24 valid orders remain.

**Common misconception:** Exclude both internal orders of an adjacent pair.

## Q11

**Correct answer:** A
**Concept:** Counting shortest paths across BFS layers.

The layers are {s}, {a,b}, {c,d}, {t}, so the shortest length is three. The numbers of shortest paths to a,b are 1,1; to c,d they are 1,2; and to t the sum is 1+2=3. Equivalently, the paths are s-a-c-t, s-a-d-t, and s-b-d-t. A is correct. B counts only the two predecessors of t, C miscounts layers as edges, and D counts a nonexistent route through b-c.

**Common misconception:** A BFS parent tree stores one witness path per vertex, not necessarily all shortest paths.

## Q12

**Correct answer:** A, C, D

Since each element is its own inverse, (ab)^(−1)=b^(−1)a^(−1)=ba, proving A. If they commute, (ab)²=a²b²=e; ab≠e because a≠b, so its order is2, proving C. Conversely order2 gives ab=(ab)^(−1)=ba, proving D. Noncommuting transpositions in a permutation group satisfy the individual square conditions, refuting B. Individual involutions need not commute.

## Q13

**Correct answer:** 6

Shifting1011 yields0110 after discarding the outgoing1. Its sign bit is0, so its signed value is6. This wraps the original signed−5 rather than computing an exact unbounded multiplication by two.

## Q14

**Correct answer:** A, D

The four minterms are0000,0010,1000,1010. A and C vary independently, while B=D=0 throughout. Thus they form a four-cell cube represented by (NOT B)(NOT D), proving A,D and refuting B,C. Karnaugh-map grouping follows Gray-code adjacency, including wraparound, rather than ordinary consecutive decimal labels.

## Q15

**Correct answer:** 6

The tokens are a1, ==, =, 23, >, b. Longest match takes two of the three consecutive equals signs first. Neither the identifier rule nor integer rule permits the entire input to be combined. Thus there are6 tokens. Token boundaries need not coincide with spaces.

## Q16

**Correct answer:** A, B

**Concept:** Engineering Mathematics — Graph connectivity matching and colouring

1. The degree sum is 14, so the handshake lemma gives 7 edges.
2. G is connected and has exactly two odd-degree vertices. It therefore has an open Euler trail.
3. For a counterexample to both remaining assertions, take two disjoint triangles and connect one vertex of each by one bridge. The bridge endpoints have degree 3 and all others degree 2. The triangles exclude bipartiteness; the bridge excludes a Hamiltonian cycle.

- **A:** Each undirected edge contributes twice to the degree sum.
- **B:** Connectedness and exactly two odd vertices are sufficient.
- **C:** The two-triangle bridge construction has an odd cycle.
- **D:** A Hamiltonian cycle cannot cross a bridge and return without reusing it.

**Common misconception:** A degree sequence can force an Euler trail without forcing bipartiteness or a Hamiltonian cycle.

## Q17

**Correct answer:** A, C

A full link-state database supports independent shortest-path computation from each router, proving A. The source differs, so the resulting trees and next hops can differ, proving C and refuting D. B describes distance-vector-style information rather than the stated topology database. Shared input topology is not a shared source vertex.

## Q18

**Correct answer:** 36 (exact)
**Concept:** Surjections after identifying domain elements.

Treat {1,2} as one effective element, giving four labelled units mapping onto three labels. Inclusion-exclusion yields 3⁴−3×2⁴+3×1⁴=81−48+3=36.

**Common misconception:** The equality constraint reduces the number of independently assigned domain units; it does not reduce the codomain.

## Q19

**Correct answer:** 4

**Concept:** Product of generating functions.

Expanding gives Σ_(i≥0)x^i times Σ_(j≥0)x^(2j). The coefficient counts nonnegative solutions to i+2j=7, with j=0,1,2,3. There are four.

**Common misconception:** Using ordered partitions into arbitrary positive parts instead of the two generating factors' choices.

## Q20

**Correct answer:** A, C

Concept: left factoring versus ambiguity. Both S alternatives start with a, producing the LL(1) conflict in A. Factoring a leaves X alternatives distinguished by b and c, so C is true. The language consists only of ab and ac and has an unambiguous grammar, disproving B. A deterministic parser exists, disproving D. A predictive-table conflict need not mean an ambiguous language.

## Q21

**Correct answer:** B, C

Concept: essential prime implicants. Every column is covered by two rows, so no row uniquely covers a required minterm; B is true and A false. Any two rows cover all three columns, proving C. D is false: a cover need not contain an essential row. Covering many columns alone does not establish essentiality.

## Q22

**Correct answer:** 14

Estimated order is A,B,C. Actual waiting times are0,8,9, totaling17. Knowing actual bursts, execute B,C,A or C,B,A; waiting times are0,1,2, totaling3. The difference is14. Estimates choose the order, while actual durations determine the resulting waits.

## Q23

**Correct answer:** 175 (exact)

**Concept:** Computer Networks — IPv4 fragmentation

The incoming payload is 1000 bytes. Each new fragment can hold620-20=600 payload bytes, and600 is divisible by 8. The first retains offset 100. The second begins600 bytes later, so its offset is 100+600/8=175. Offsets remain relative to the original datagram, not relative to the incoming fragment.

**Common misconception:** Refragmentation adds to the existing fragment offset rather than restarting at zero.

## Q24

**Correct answer:** 9

**Concept:** Address width versus word width.

Selecting among 512=2⁹ microinstructions requires nine bits. The 40-bit microinstruction width determines storage per entry, not the number of address bits.

**Common misconception:** Using microinstruction width as its address width.

## Q25

**Correct answer:** A, B, D

A finite union of singleton strings has a regular expression and hence a DFA, proving A,D. Regular languages are context-free, proving B. A finite language need not contain ε, so C is false. Finiteness guarantees recognizability classes, not particular members.

## Q26

**Correct answer:** 32
**Concept:** Powers of a rank-one matrix.

A²=2A, so induction gives A⁵=2⁴A. Its trace is 16×2=32. Equivalently, A's eigenvalues are 2 and 0, whose fifth powers sum to 32.

**Common misconception:** Matrix powers do not mean taking powers of individual entries.

## Q27

**Correct answer:** 3

For p=1 or2, string a³ is long enough but every permitted nonempty pumped part has length1 or2; pumping down leaves a nonmultiple-of-three length. For p=3, every eligible string has at least three a's; choose y=a³, and every pump changes the length by a multiple of three. Thus3 is both necessary and sufficient.

## Q28

**Correct answer:** A

**Concept:** LOOK direction and reversal point.

Starting upward, the head serves 55 then 70, reverses at the final pending request, and serves 30 then 10. A matches. B reverses too soon; C changes direction before serving all upward requests; D skips nearer upward request 55 on its outward pass.

**Common misconception:** Confusing LOOK with shortest-seek-first or with movement to the disk's physical endpoint.

## Q29

**Correct answer:** 21

The parameter p is a copy of the caller's pointer. Inside change it advances from a+1 to a+3 and replaces a[3] by a[2]+a[3]=7+9=16. The caller's p still points to a[1], whose value is 5. Thus the print computes 5+16=21. Passing a pointer by value permits mutation of its target but does not permit rebinding the caller's pointer through the local parameter alone.

## Q30

**Correct answer:** 3

Each block holds floor(512/90)=5 unspanned records. Twelve records require three blocks, with capacity 15. Therefore three additional records fit without another block. The unused62 bytes per full block cannot combine across boundaries to hold a record because spanning is prohibited.

## Q31

**Correct answer:** D
**Concept:** Output-sensitive lower bounds.

There are C(n,2)=n(n−1)/2 distinct pairs to emit. Constant work per output gives Ω(n²), so D is the tight bound from output size. A,B,C are asymptotically weaker and do not express the tight output-size requirement.

**Common misconception:** An efficient internal algorithm cannot avoid the time needed to materialize its required output.

## Q32

**Correct answer:** B
**Concept:** Linear probing and deletion markers.

All inserted keys hash to 3, occupying indices 3,4,5. Deleting 17 leaves a tombstone at 4. Searching 24 examines 3,4,5: three probes. The known-absent 31 then occupies tombstone 4. A and D stop the search too early; C ignores the reusable tombstone.

**Common misconception:** A tombstone may be reused by insertion but cannot terminate a lookup chain.

## Q33

**Correct answer:** 96

The /25 route covers128 addresses, from.128 through.255. The more-specific /27 route removes32 addresses,.160 through.191, from B's traffic. Thus128−32=96 addresses go to B. These routing counts include network/broadcast-looking addresses because the question counts address matches, not assignable hosts.

## Q34

**Correct answer:** A, C
**Concept:** Domain independence in relational calculus.

E1 is exactly the fixed tuples of R, so enlarging an external domain adds nothing to it (A). E2 contains all domain values not in R; any new domain value enters it, proving C and refuting B. E1 need not include domain values absent from R, refuting D.

**Common misconception:** Unrestricted negation can make a query depend on values not stored in the database.

## Q35

**Correct answer:** A

**Concept:** Programming and Data Structures — Recursion

1. Induction gives f(n)=n: the even case restores 2(n/2), and the odd case restores 2 floor(n/2)+1.
2. The call chain is 45,22,11,5,2,1, which contains six active calls at its deepest point.

- **A:** Both the induction and explicit chain give this pair.
- **B:** It counts five recursive edges instead of six calls.
- **C:** The odd branches preserve the discarded low-order bits.
- **D:** The branches do not append 1 at even n.

**Common misconception:** Recursion depth counts frames, which is one greater than the number of recursive edges.

## Q36

**Correct answer:** 15

TCP has10 free ports and UDP has5 free ports. Their independent namespaces let these capacities be used simultaneously, adding15 mappings. Excess TCP requests cannot consume UDP-only free capacity under the stipulated per-protocol rule. Remote peer differences do not expand either pool because sharing within a protocol is expressly prohibited.

## Q37

**Correct answer:** 448 (exact)

**Concept:** Algorithms — Asymptotic time and space complexity

At a fixed width w, the base loop has n/(2w) iterations because w is a power of two smaller than n. Each iteration calls touch w times, so each width contributes n/2 = 64 calls. The widths are 1, 2, 4, 8, 16, 32, 64: seven levels. Hence the exact count is 64 × 7 = 448. The work is Θ(n log n), even though individual inner-loop lengths vary.

**Common misconception:** Multiplying the largest bounds of all loops ignores the inverse relationship between the number of blocks and block width.

## Q38

**Correct answer:** 5.625

Each101 part has length3 and value5 by the concatenation rule. The returned value is5+5/8=5.625. The fractional part is scaled by its digit length, including any leading zeros, not by its numerical magnitude.

## Q39

**Correct answer:** B, C
**Concept:** Object lifetime after function return.

A's automatic scalar and D's automatic array cease to exist when their functions return; their pointers do not permit later access to live objects. B's static object persists throughout program execution. C's allocated object persists until freed, which the question excludes before the first access. Thus B,C are valid and A,D are not.

**Common misconception:** Returning an address does not extend the lifetime of the object at that address.

## Q40

**Correct answer:** A, B, C

The third left-hand side is the sum of the first two, requiring t=3. The first two rows are independent, leaving one free variable when consistent. Subtracting twice the first equation from the second gives −x1+x3=0. Equivalently, solutions are (s,1−2s,s) for arbitrary real s. Thus A,B,C hold. Rank is 2, not 3, so D is false.

## Q41

**Correct answer:** 22

**Concept:** Congestion-window timing within rounds.

The first four rounds transmit windows 4,5,6,7 MSS, increasing only after each round. Total 4+5+6+7=22 MSS.

**Common misconception:** Applying the first increase before transmitting the first window.

## Q42

**Correct answer:** A, C

Reusing the same tag can match an old virtual-page entry and produce an obsolete frame, making A true. Invalidating the tag's entries removes those stale hits, so C is true. ASIDs distinguish concurrently assigned address spaces only when reuse is managed; B is false. The lookup key in the question omits the page-table base, so changing that base alone does not guarantee a miss, making D false.

## Q43

**Correct answer:** A, B

There are finitely many strings in each bounded-length set. Run M on every candidate; the promise guarantees every run finishes, allowing A,B to be decided. The promise does not bound the number of inputs. For undecidability, construct a total machine that simulates a chosen machine on a fixed input for |w| steps. Accepting iff it has halted makes emptiness equivalent to nonhalting; accepting iff it has not halted makes universality equivalent to nonhalting. Thus C,D remain undecidable even on promised total machines. A per-input termination guarantee is not a bound on all inputs collectively.

## Q44

**Correct answer:** 0.375

For x>0, rationalization gives f(x)=1/(sqrt(1+x)+1), whose limit at0 is1/2. Continuity therefore requires b=1/2. Its right derivative at0 is −1/[2sqrt(1+0)(sqrt(1+0)+1)²]=−1/8. The left derivative is a, so differentiability requires a=−1/8. Hence a+b=3/8=0.375. Matching only the function values establishes continuity but not differentiability.

## Q45

**Correct answer:** A, C

An earliest-finishing interval ends no later than the first chosen interval in an optimum, leaving at least as much remaining scheduling time, proving A. Half-open endpoints allow back-to-back compatibility, proving C. Weighted objectives can prefer a later-finishing higher-value interval, so B is false. A long interval can block many short intervals, disproving D. The exchange proof relies on the equal-value cardinality objective.

## Q46

**Correct answer:** B

**Concept:** Listening versus connected sockets.

Accept returns connected sockets with their own lifetimes. Closing the listening socket stops accepting new connections through it but does not itself close c1,c2, proving B and refuting A. No descriptor is automatically promoted to a listener (C), and the established connections retain separate byte streams (D).

**Common misconception:** Treating all accepted connections as the same socket as the listener.

## Q47

**Correct answer:** A, B

At a shared suffix, linking the same node again can make its next pointer refer to itself or to an earlier shared node, proving A and refuting D. When current pointers are equal, their entire remaining suffix is the same physical list and can be attached once, proving B. Distinct nodes may contain equal values, refuting C. An in-place merge relies on aliasing assumptions as well as sort order.

## Q48

**Correct answer:** 7

After push7, m=7. Push3 stores −1 and sets m=3; push5 stores5. Push−2 stores−7 and sets m=−2. Popping−7 returns−2 and restores m=2(−2)−(−7)=3. Popping5 returns5. Push1 stores−1 and sets m=1. Its pop returns1 and restores m=3; the next stored−1 pop returns3 and restores m=7. Returned values sum −2+5+1+3=7. Encoded negative entries are restoration information, not the logical popped values.

## Q49

**Correct answer:** 10

**Concept:** Lexical environment identity versus caller environment.

Q1 retains the environment of P1, the activation that created it. Its x is therefore P1.x=10, even though P2 with another x is the caller.

**Common misconception:** Resolving lexical variables from the most recent caller's activation.

## Q50

**Correct answer:** A, C
**Concept:** Recovery conditions versus serializability.

T2 reads from T1 and commits after T1; T3 reads from T2 and commits after T2, so the schedule is recoverable. Both reads occur before the producing transaction commits, so it is neither cascadeless nor strict. Conflict edges are T1→T2→T3 with no cycle. Thus A,C hold and B,D fail.

**Common misconception:** Recoverability permits dirty reads if commit dependencies are respected; cascadelessness does not.

## Q51

**Correct answer:** B

**Concept:** Independently expiring DNS records.

The CNAME expires at time 120, so at time 80 it has 40 seconds remaining. The A record expires at 20+50=70 and is already stale. Reuse the live alias mapping but resolve its target afresh: B. A wrongly assigns the CNAME's lifetime to the A record; C reverses which record expired; D disregards TTL expiry altogether.

**Common misconception:** Treating a cached alias chain as one record with one shared expiration time.

## Q52

**Correct answer:** 16

Bits15–12 are fixed and bits7–0 must equal0x35. Four ignored bits11–8 can take any of16 patterns, yielding16 aliases. These do not represent additional device storage.

## Q53

**Correct answer:** 0.1944 (accepted range 0.19435–0.19445)

E[W]=P(X=Y=1)=1/6. E[Z]=1/2+1/3=5/6. ZW is2 when both succeed and0 otherwise, so E[ZW]=1/3. Covariance is1/3−(5/6)(1/6)=7/36≈0.194444. Independence of X,Y does not make their derived variables Z,W independent.

## Q54

**Correct answer:** 62

A hit costs 2+50=52ns. A miss costs 2+3×50=152ns. The weighted mean is 0.9×52+0.1×152=62ns. Resident pages avoid disk faults, but a TLB miss still pays page-table memory accesses.

## Q55

**Correct answer:** C
**Concept:** Uses before overwrites.

The first x value is used immediately in y=x*c before being overwritten, and y is then returned. Neither definition is dead, so C holds. A,D ignore the intervening use of x; B ignores return y. The later x=0 may itself be dead under the stated observability assumption, but that is not one of the two assignments asked about.

**Common misconception:** A later overwrite does not kill earlier uses that already consumed the previous value.

## Q56

**Correct answer:** A, C
**Concept:** Directory links versus open-file references.

An open descriptor keeps the unlinked file available until the reference is released, proving A and refuting B. Removed pathnames no longer resolve to it, proving C. Open descriptors are not directory hard links; the hard-link count is zero, refuting D.

**Common misconception:** Removing a name is not necessarily the same as immediately destroying the referenced data.

## Q57

**Correct answer:** 4

The LCS length is2, attainable by AA or BA. The unequal length-three strings cannot have a common subsequence of length3. Shortest common supersequence length is3+3−2=4, attained for example by ABAA. Aligning an LCS avoids duplicating those matched characters.

## Q58

**Correct answer:** 3

Concept: overlapping sequence detection. Prefixes ending at positions 3,5,7 end in 101. The outputs sum to three. Resetting the detector as though it could not reuse the final 1 would lose overlaps.

## Q59

**Correct answer:** C

**Concept:** Precedence cycles and observed reads.

r1(X) before w2(X) gives T1→T2. r2(Y) before w1(Y) gives T2→T1. The cycle refutes both serial orders in A and B. In serial T1,T2, T2 reads Y=1; in serial T2,T1, T1 reads X=1, so neither reproduces both zero reads. Thus C holds. D overlooks read–write conflicts across transactions.

**Common misconception:** Checking only write–write conflicts.

## Q60

**Correct answer:** 4

Concept: nonassociativity of saturation. b⊕c=1, then a⊕1=7. In the other grouping a⊕b saturates 11 to 7, then 7⊕(−4)=3. Exact final difference=7−3=4. Saturated intermediate information cannot be recovered by a later subtraction.

## Q61

**Correct answer:** 16

Choose f(1) arbitrarily in four ways; commutation forces f(2)=τ(f(1)). Since3 and4 are fixed by τ, their images must also be fixed by τ, giving two choices each from{3,4}. These choices satisfy every equation independently, so there are4×2×2=16 functions. Images of fixed points are constrained, while the swapped pair's image is determined by one free choice.

## Q62

**Correct answer:** B

**Concept:** Virtual reservation and demand allocation.

An address range can be validly reserved before private physical frames are allocated; first writes trigger backing allocation. This proves B and refutes A. Address translation allows distinct virtual and physical addresses, refuting C, and first-write faults on valid mappings refute D.

**Common misconception:** Treating a valid virtual mapping as proof that its private physical storage is already present.

## Q63

**Correct answer:** A, C
**Concept:** Eliminating nongenerating and unreachable grammar symbols.

B has no terminating alternative: every derivation from B retains a B. Thus S→AB cannot produce a terminal string. All successful derivations use S→C, which generates exactly c*, proving A. Only S and C occur in successful derivations, proving C. Although A is separately reachable and generating, its only reachable context includes the nonterminating B; it is not useful, refuting B. D generates a terminal string but is unreachable from S, refuting D.

**Common misconception:** Reachability and generation tested in the unpruned grammar are not independently sufficient; remove nongenerating productions before recomputing reachability.

## Q64

**Correct answer:** 14

A parse tree with five terminal leaves is an ordered full binary tree with four binary internal nodes. Let t1=1 and tn=Σ(i=1..n−1) ti t(n−i). Then t2=1,t3=2,t4=5, and t5=5+2+2+5=14. Different expansion orders of the same tree are not additional trees; counting derivation sequences would overcount.

## Q65

**Correct answer:** 2

After hit A, recency order is B,C,A. D misses and evicts B, leaving C,A,D. B then misses and evicts C. Two misses occur. Hits update LRU order even though no data is loaded.

