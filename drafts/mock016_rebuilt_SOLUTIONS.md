# Worked Solutions — Mock Test 016

## Q1
**Correct answer:** 3.2

Concept: weighted percentages. The two batches contain 300(0.02)=6 and 200(0.05)=10 defective units. Thus 100(16/500)=3.2%. Averaging the two percentages without their batch weights is incorrect.

## Q2
**Correct answer:** A

Concept: composition of reflections. Reflection across y=x swaps coordinates, giving (0,2). Reflection across x=1 changes x to 2−x, giving (2,2). A is correct. B changes the second coordinate incorrectly; C stops after the first reflection; D introduces an unwarranted vertical reflection. Reflection order matters.

## Q3
**Correct answer:** B

Concept: logical sequencing. Comparing the result with the requirement (S) reveals a mismatch; identify its source (Q), revise that step (R), and test the revision (P). B follows these dependencies. A tests before revision and identification; C revises before identification; D tests before the stated revision and places the initial comparison last. Distinguish discovery from verification.

## Q4
**Correct answer:** 0.4167

Concept: equally likely ordered outcomes. For first results 1 through 6, there are respectively 5,4,3,2,1,0 larger second results. Probability=15/36=5/12=0.416666…. Rounded answer 0.4167; accepted range 0.41665–0.41675. Equality outcomes must be excluded before splitting the remaining probability equally.

## Q5
**Correct answer:** B

Concept: vocabulary in context. Restoring the previous configuration undoes the change, which is B. A is the opposite meaning; C asserts repetition, which reversibility does not require; D contradicts restoration of the previous state. Use the sentence's definition rather than an association with the prefix alone.

## Q6
**Correct answer:** 108

Concept: successive percentage changes. After two years the value is 1.44 times the original. After the fall it is 1.44(0.75)=1.08 times the original, or 108%. The annual growth factor is 1.2, but recovering it is unnecessary. Subtracting 25 percentage points from 144 confuses the reference base.

## Q7
**Correct answer:** A

Concept: confounding and comparison groups. A compares products with similar prior sales but differing advertising exposure, helping separate prior popularity from advertising. B provides labels without comparison data; C is irrelevant to the stated causal relationship; D removes the comparison group. A helps assess causality but does not alone establish a randomized causal effect.

## Q8
**Correct answer:** 7

Concept: rotational orbits. The central square is fixed. Every other square has four distinct positions under quarter turns: a noncentral square is not fixed by a half turn. Therefore there are 1+24/4=7 orbits. Dividing all 25 squares by four would neglect the fixed centre.

## Q9
**Correct answer:** 31

Concept: telescoping a recurrence. a5=a1+1²+2²+3²+4²=1+30=31. The last increment is 4², since the recurrence's left index is n+1. Including 5² is an off-by-one error.

## Q10
**Correct answer:** 8

Concept: chord geometry. The perpendicular from the centre to the chord has length 3 and bisects the chord. A right triangle gives half-length sqrt(5²−3²)=4, so the chord length is 8. The difference of radii is not half the chord.

## Q11
**Correct answer:** B

Concept: constant propagation. All feasible incoming paths establish x=4, so 3x−2=12−2=10. B is correct. A omits the subtraction; C is not the expression's value; D denies the justified substitution. A value known on only one incoming path would not suffice.

## Q12
**Correct answer:** 4

Concept: counting ordered compositions. Without a 3, only 1,1,1,1,1 works. With one 3, the remaining two 1s give 3,1,1; 1,3,1; 1,1,3. Two 3s exceed 5. Total four sequences. Counting unordered multisets would yield only two.

## Q13
**Correct answer:** 0.9

Concept: Bayesian prediction. Likelihoods of HH are 1/4 for the fair coin and 1 for the double-headed coin. Equal priors yield posterior probabilities 1/5 and 4/5. Predictive probability=(1/5)(1/2)+(4/5)(1)=9/10. The third toss is not independent of the observed evidence after marginalizing over the unknown coin.

## Q14
**Correct answer:** B

Concept: CPU execution time. Time depends on instruction count, CPI and clock period. A higher hit rate can lower memory stalls while a longer period raises time per cycle; their net effect needs magnitudes. B is correct. A asserts an unproved net benefit; C has no basis; D contradicts the permitted tradeoff. A single performance metric cannot determine elapsed time.

## Q15
**Correct answer:** 13

Concept: recursion-tree accounting. Internal levels have input sizes 27,9,3 and contain 1,3,9 calls. Leaves have size one and are excluded. Internal calls=1+3+9=13. Counting all calls would include 27 additional leaves.

## Q16
**Correct answer:** 2

Concept: antichains and chain bounds. Partition the divisors into chains 1|2|4|12 and 3|6. An antichain contains at most one element from each, hence size at most two. The incomparable pair {3,4} attains two. The number of divisors is not the width.

## Q17
**Correct answer:** A, C

Concept: pivoting in LU decomposition. det(A)=−1, so A is nonsingular (A true). Write L=[[1,0],[l,1]] and U=[[u,v],[0,w]]. From the first row u=0,v=1, but then (LU)21=lu=0, contradicting A21=1; B is false. Swapping rows gives the identity, factored as I·I, so C is true. This nonsingular matrix itself disproves D. Invertibility does not guarantee a nonzero first pivot.

## Q18
**Correct answer:** A

Concept: HTTP representation selection. The request-header value can select different representations even for an unchanged URL; lookup must respect that variation (A). B confuses selection with freshness; C contradicts the request-header premise; D incorrectly assigns an application-layer selection rule to TCP sequence arithmetic. Resource identity and representation selection are distinct.

## Q19
**Correct answer:** B

Concept: recognizability versus decidability. The existing acceptance guarantee plus halting rejection for every nonmember gives a correct total decision procedure (B). A only describes tape symbols; C gives a single successful case; D holds for recognizers that may loop and therefore is insufficient. Deciders must halt on all inputs.

## Q20
**Correct answer:** 64

Concept: cache geometry. The cache contains 16384/64=256 lines. Four lines per set give 256/4=64 sets. Associativity counts lines per set, not bytes per set.

## Q21
**Correct answer:** A

Concept: contiguous allocation. Free space is split into separate holes, neither large enough, which is external fragmentation (A). B concerns waste inside allocated blocks and no such block was allocated; C is unnecessary; D has no connection to the allocation failure. Total free capacity is not the maximum contiguous capacity.

## Q22
**Correct answer:** A, B

Concept: dirty-page eviction. A modified page may need write-back to preserve its latest contents (A). A clean page with an identical backing copy can be discarded (B). A fault may evict either clean or dirty pages, or use a free frame, so C is false. Policies may use recency or other criteria; dirty status is not a universal selection rule, so D is false. Victim selection and preservation of its contents are separate decisions.

## Q23
**Correct answer:** A

Concept: transport demultiplexing. Ports identify application endpoints on a host, in combination with transport/address context (A). B concerns link framing; C hardware pins; D processor addressing. These are not transport-port roles. A port number by itself is not a globally unique connection identifier.

## Q24
**Correct answer:** 0.3466

Concept: substitution in integration. Let u=1+x², du=2x dx. The integral is (1/2)∫₁² du/u=(ln 2)/2=0.34657359…. Round to 0.3466; accepted range 0.34655–0.34665. The factor 1/2 comes from differentiating x².

## Q25
**Correct answer:** 7

Concept: B+ internal-node separators. Six ordered separators partition the search domain into seven child intervals, so k+1=7 pointers. This is an internal node, not a leaf's record-pointer count.

## Q26
**Correct answer:** A

Concept: transaction atomicity. Atomicity requires the transfer's updates to take effect together or not at all. Persisting only the debit violates A. B and C are not transaction requirements. D mistakes partial success for an atomic outcome. Merely retaining a durable partial update is not sufficient.

## Q27
**Correct answer:** 2

Concept: hard links. Removing one directory entry decrements the number of links by one, from three to two. The other names still reference the same file. Removing one name does not necessarily delete the underlying file.

## Q28
**Correct answer:** A, B

Concept: absorption. x+xy=x(1+y)=x, and x(x+y)=xx+xy=x+xy=x, so A and B hold. C fails at x=0,y=1. D is always zero and fails at x=1. Boolean addition is OR, not arithmetic addition.

## Q29
**Correct answer:** 6

Concept: stack tracing. The three pops return 2, then 3, then 1. Their sum is 6. Last-in-first-out order determines individual outputs even though their total equals the sum of all pushed values here.

## Q30
**Correct answer:** A

Concept: asynchronous I/O notification. Completion can raise an interrupt for the CPU (A). B destroys processor state; C corrupts addressing; D prevents useful transfer activity. None is a completion-notification mechanism. DMA transfers data independently but can still notify software when done.

## Q31
**Correct answer:** A

Concept: dead stores. No operation reads the first stored value before the second assignment overwrites it; removing that store preserves behavior (A). B invents an invalidity rule; C contradicts print's use of x; D would remove the value that print requires. The side-effect assumption is essential.

## Q32
**Correct answer:** 1

Concept: implicant dimension. Eight=2³ minterms vary over three of the four coordinates. One coordinate remains fixed and supplies the sole literal. A valid cube is necessary; an arbitrary collection of eight minterms need not simplify this way.

## Q33
**Correct answer:** B

Concept: regular-expression membership. baab=(ba)(ab), and it begins with b so cannot lie in (ab)*; B is correct. A=(ab)(ab) belongs to both languages. C's first pair aa is neither allowed block. D has odd length and cannot be concatenated two-letter blocks. Splitting into the specified blocks is the relevant test.

## Q34
**Correct answer:** 6.6667

Concept: extremal median. Sort the observations. If the median is m, the three largest values sum to at least 3m and the other two are nonnegative. Thus m≤20/3. Values 0,0,20/3,20/3,20/3 attain the bound. Round to 6.6667; range 6.66665–6.66675. A median need not equal the mean.

## Q35
**Correct answer:** 18

Concept: tree edge count and handshaking. A tree on ten vertices has nine edges; each contributes two to the degree sum. Total=2·9=18. Counting edges only once gives the wrong degree sum.

## Q36
**Correct answer:** 1.1886

Concept: pipeline throughput versus fill time. Old period=5+0.2=5.2 ns; new period=max(1,2,3,4,2.5,2.5)+0.2=4.2 ns. Twenty instructions take 24 old cycles and 25 new cycles. Ratio=(24·5.2)/(25·4.2)=124.8/105=1.188571…. Round to 1.1886; range 1.18855–1.18865. Clock-period ratio alone neglects the extra fill cycle.

## Q37
**Correct answer:** A, B

Concept: CFG language and ambiguity. Productions create only a symbols, and repeated concatenation generates any number, including zero, so A holds. A tree for a can be wrapped as S→SS with one child deriving ε, repeatedly, producing infinitely many distinct trees; B holds. That also disproves C. An LL(1) grammar is unambiguous, and this grammar additionally has immediate left recursion, so D fails. Infinitely many derivations here correspond to genuinely different trees, not merely different expansion orders.

## Q38
**Correct answer:** 102

Concept: variable instruction lengths and branch base. Branch starts at 100+2+4=106; next-instruction address=108. Displacement is −3·2=−6 bytes. Target=108−6=102. Neither branch-start addressing nor treating the displacement as bytes matches the stated architecture.

## Q39
**Correct answer:** A, C

Concept: locking conditions. Unlock-S(A) starts the shrinking phase; later lock-S(C) violates basic 2PL (A true, B false). X(B) is released after commit, meeting the specifically defined exclusive-lock retention condition (C true). Retaining X(B) does not remove the new shared-lock acquisition, so D is false. The question separates strictness of release from the full strict-2PL protocol.

## Q40
**Correct answer:** B

Concept: DFS interval nesting. v's entire interval lies inside u's, so v is a descendant of u. An edge from ancestor to descendant that is not a tree edge is forward (B). A would point to an ancestor; C connects unrelated DFS subtrees and requires disjoint intervals; D denies ordinary descendant nesting. Edge direction is crucial.

## Q41
**Correct answer:** 3

Concept: weighted covering. Q+R covers all columns at cost 2+1=3. No cost below three works: the only cost-two choices are Q alone, missing 1, or R+S, missing 2; any cost-one choice also fails. Thus three is optimal. Minimizing cost need not coincide with an arbitrary minimum-cardinality cover.

## Q42
**Correct answer:** B

Concept: BST deletion and successor. The original root's successor is 45, the leftmost node in its right subtree. Copy 45 to the root and replace node 45's original link from 50 by its child 47. Thus 47's parent is 50. With no right subtree, its next inorder node is its ancestor 50. B gives (50,50). A and D leave the old parent relation; C and D skip the closer successor 50. Copying the successor key does not move its entire subtree to the root.

## Q43
**Correct answer:** 5

Concept: stream framing across reads. Concatenated successful bytes are [3,65,66,67,2,68,69,0]. The first length 3 consumes payload 65,66,67 across two reads. The next length 2 consumes 68,69. Zero ends the stream. Payload total=3+2=5. EINTR contributes no bytes, and read boundaries are not record boundaries.

## Q44
**Correct answer:** 5

Concept: subgroup enumeration. Subgroup orders divide six. There is one trivial subgroup, three order-two subgroups generated by the three transpositions, and one order-three subgroup generated by either 3-cycle. All are cyclic and abelian. The only order-six subgroup is S3 itself, which is nonabelian. Total=1+3+1=5. The two 3-cycles generate the same subgroup and must not be counted twice.

## Q45
**Correct answer:** 1

Concept: spanning trees of a cycle. Every spanning tree deletes exactly one cycle edge. Total edge weight=22. Unconstrained minimum deletes 7, yielding 15; with 7 required, delete the largest other edge, 6, yielding 16. Additional cost=1. Strictly, the constrained object is a minimum-weight spanning tree subject to the requirement; no unconstrained MST here contains 7.

## Q46
**Correct answer:** C

Concept: zero-weight cycles and walks. Every s-to-t walk must pay 1 entering a and 2 leaving b for t. Repeating a→b→a adds zero; hence infinitely many walks attain weight 3 (C). A would require an exploitable negative cycle; B ignores zero-cost repetitions; D overlooks s→a→b→t. Paths and walks have different counting behavior.

## Q47
**Correct answer:** 4

Concept: coloring a wheel. The odd cycle needs three colors. Its universal neighbour cannot use any color appearing on the cycle, so a fourth is necessary. A three-coloring of the cycle plus a fresh hub color achieves four. Treating the cycle as bipartite misses the lower bound.

## Q48
**Correct answer:** 700

Concept: gap placement with repeated symbols. First arrange BBBCCC in 6!/(3!3!)=20 ways. The six symbols create seven gaps, including ends. Choose three distinct gaps for one A each: C(7,3)=35. Total=20·35=700. Identical A symbols are not separately permuted; multiple As in one gap would violate the restriction.

## Q49
**Correct answer:** A, C

Concept: alias-sensitive optimization. When i≠j, the store does not modify A[i], so reuse p (A). When i=j, the last load reads 7 (C). Without a proven relation, the i=j case with old value not 7 defeats B. The same case defeats D. Equal expression text does not ensure an unchanged memory value across a store.

## Q50
**Correct answer:** 6

Concept: gate-arrival analysis. Ripple: C1=max(1,max(2,0)+1)+1=4; subsequent carry times are 6,8,10. Expanded C4=G3+P3G2+P3P2G1+P3P2P1G0+P3P2P1P0C0. Each nontrivial product is ready at time 3 with unlimited fan-in; the final OR is ready at 4. Gain=10−4=6. Applying binary-gate tree delays would contradict the unlimited-fan-in model.

## Q51
**Correct answer:** B

Concept: Shannon decomposition of parity. Sum=a XOR b XOR c. For ab=00,01,10,11 it is c,c′,c′,c, hence B. A is the carry-out input pattern, not sum. C complements every required output. D gives only a, independent of b and c. Separate sum and carry functions.

## Q52
**Correct answer:** 10

Concept: packet pipelining and overhead. One packet transmission takes (10000/k+100)/R. The first packet crosses two links in two such intervals, then one finishes per interval; completion takes (k+1)(10000/k+100)/R. Its k-dependent part is 100k+10000/k, at least 2sqrt(100·10000)=2000, with equality at k=10. Ten divides 10000, so the continuous optimum is also feasible. Ignoring headers incorrectly favors indefinitely smaller packets.

## Q53
**Correct answer:** 3

Concept: overlapping sequence detection. Prefixes ending at positions 3,5,7 end in 101. The outputs sum to three. Resetting the detector as though it could not reuse the final 1 would lose overlaps.

## Q54
**Correct answer:** A, C

Concept: fair search of nondeterministic computations. With finite branching each finite depth has finitely many nodes, so BFS eventually reaches any finite accepting branch (A). DFS can stay forever on an epsilon loop (C), disproving B. For a rejected input an infinite nonaccepting computation tree can keep naive BFS running forever, disproving D. CFL membership is decidable by other constructions; this does not make every naive simulation a decider.

## Q55
**Correct answer:** 6

Concept: cardinality under two functional constraints. For each fixed A, the B–C pairs form a matching: neither a B nor a C can occur twice with different partners. Maximum matching size=min(3,4)=3. Two A values allow 2·3=6 tuples, attained by using three distinct B–C pairs for each A. Multiplying domain sizes ignores the dependencies.

## Q56
**Correct answer:** A, D

Concept: closure and its limits. If Lᴿ were context-free, reversing again would make L context-free, a contradiction; A holds. Erasing every symbol maps nonempty L to {ε}, which is regular; non-context-free L is necessarily nonempty. Thus D holds and B fails. Intersecting with the empty regular language gives the empty context-free language, disproving C. Closure theorems must be applied in the correct direction.

## Q57
**Correct answer:** 6

Concept: process-tree control flow. Only the original parent continues the loop. Its three children break at i=0,1,2 and print those values; the parent prints 3. Sum=0+1+2+3=6. Doubling the process count every iteration would ignore the children's break statements.

## Q58
**Correct answer:** 254

Concept: one's-complement checksum. FE+02=100 hexadecimal. End-around carry adds the overflow one to the low byte 00, yielding 01. Its eight-bit complement is FE=254. Dropping carry would wrongly produce FF; two's-complement negation is also a different operation.

## Q59
**Correct answer:** A

Concept: balanced delimiters and finite memory. Distinct unmatched-OPEN counts require distinct future numbers of CLOSE tokens. An unbounded family cannot be represented by finitely many states (A). B falsely says finite inputs require infinitely many steps; C falsely calls a two-token alphabet infinite; D falsely generalizes to ordinary nonnested comments, which can be recognized by finite-state methods. It is unbounded nesting, not comments as such, that causes the limitation.

## Q60
**Correct answer:** 1

Concept: relational anti-semijoin. π_A(R)={1,2,3}. Joining on B with {x,y} keeps the first three tuples and projects to {1,2}. Difference={3}, cardinality one. This selects A values having no match at all, not those failing to match every S value.

## Q61
**Correct answer:** 6

Concept: heap order and rank. The root contains the smallest key. A node at depth at least three has at least three distinct smaller ancestors and cannot hold the third-smallest. The remaining candidate indices are 2–7. At index 2 or 3, place the second-smallest at its sibling. At any index 4–7, place the second-smallest at its parent; put the smallest at the root, then complete the heap with larger keys in increasing depth order. All six candidates are achievable. A heap does not order siblings.

## Q62
**Correct answer:** 2

Concept: normalized recurrences and generating sums. Divide by 2ⁿ: b_n=b_(n−1)+n/2ⁿ, b0=0. Thus b_n=Σ(k=1..n)k/2ᵏ. From Σk xᵏ=x/(1−x)² for |x|<1, the limit at x=1/2 is two. Equivalently a_n=2^(n+1)−n−2. Solving only the homogeneous recurrence would miss the limiting coefficient.

## Q63
**Correct answer:** 64

Concept: representation storage thresholds. Matrix storage=4096 bits. Lists require 65·32+2m·16=2080+32m. Strict inequality 4096<2080+32m means m>63. Therefore the smallest integer is 64, feasible for a 64-vertex simple graph. At m=63 the sizes tie, which does not satisfy the question.

## Q64
**Correct answer:** A, C

Concept: semaphore acquisition order. Consumer can hold mutex while waiting on initially zero full; producer then waits for that mutex and cannot insert/signall full (A). Code containing signal operations does not make them reachable, so B is false. Waiting for an available item before acquiring mutex removes this circular acquisition order (C). full must initially count zero available items; setting it to N misrepresents the empty buffer (D false). A resource should not be held while waiting for the condition that needs another process to acquire it.

## Q65
**Correct answer:** A

Concept: switch learning followed by forwarding. First learn A→3 and forward to known B→2. Then B's frame to A goes to 3. C's frame to unknown D floods to 1,2,4, excluding ingress 3. Finally learn D→4 and forward to known C→3. A lists these sets. B retains A's stale entry; C floods back onto ingress; D assumes an unknown D location and then ignores known C. Learning uses the source, lookup uses the destination.
