# Worked Solutions — Mock Test 074

## Q1

**Correct answer:** A, C
**Concept:** Exhaustive consistency of statements.

If the prize is in A, the three truth values are false,false,true: valid. If it is in B, they are true,false,true: invalid. If it is in C, they are false,true,false: valid. Hence A and C are possible locations, B is impossible, and label A is false in every valid case. Options A,C hold; B,D do not.

**Common misconception:** Exactly one true statement need not determine a unique location.

## Q2

**Correct answer:** 12

8^5/4²=2^15/2^4=2^11. A power2^k has a1 followed by k zeroes in binary, so there are12 digits. The exponent counts trailing zeroes, not total digits.

## Q3

**Correct answer:** 60

Let the initial volume be V. The removed ten litres contain6 litres of milk. The final milk volume is0.6V−6, and the final total remains V. A1:1 ratio requires0.6V−6=0.5V, so V=60. Water replacement restores volume but not milk.

## Q4

**Correct answer:** 41

The increments for n=1,2,3,4 are2,6,12,20. Starting at1 gives a5=1+2+6+12+20=41. Four increments connect the first term to the fifth.

## Q5

**Correct answer:** 3

M must be last because P precedes C and both C,K precede M. Among the first three events, P must precede C while K can be before both, between them, or after both. Orders are KPCM,PKCM,PCKM, giving3. No condition places calibration after permission unless the report states it.

## Q6

**Correct answer:** A, B

Concept: implications and contrapositives. Interviewed implies both forms, and interviewed implies decision. Their contrapositives give A and B. C reverses the first implication; D reverses the second. Neither converse is supplied. “Only applicants who” specifies a necessary condition, not a guarantee of interview.

## Q7

**Correct answer:** A, B

In A the head subject is singular each, requiring has. In B the head is plural reports; the parenthetical phrase does not change that, so have is correct. C incorrectly lets plural reports govern a sentence whose head is each. D incorrectly lets the singular parenthetical each override the plural main subject. Thus A,B are correct and C,D are not.

## Q8

**Correct answer:** 5

Track orientations in the order(top,bottom,north,south,east,west). Initially they are(1,6,2,5,3,4). After north:(5,2,1,6,3,4); east:(4,3,1,6,5,2); south:(1,6,3,4,5,2); west:(5,2,3,4,6,1). The final top is5. A closed path of rolls need not restore orientation.

## Q9

**Correct answer:** 0.5556 (range 0.55555–0.55565)

Concept: surface changes after removal. The original painted surface has 6·9=54 unit faces. Eight removed corners each remove three painted faces, leaving 54−24=30 painted faces. Each removed corner exposes three previously internal faces, adding 24 unpainted faces. Exposed total=54, and painted fraction=30/54=5/9=0.555555…. Round to 0.5556; range 0.55555–0.55565. Remaining surface is not merely the original surface minus the removed faces.

## Q10

**Correct answer:** 5

Profits are30 in each year, but margins are30/120=25% and30/150=20%. The decrease is5 percentage points. Unchanged profit does not imply unchanged profit margin, and a percentage-point difference is not a relative percentage change.

## Q11

**Correct answer:** 6

**Concept:** Inversions under stable partition.

Each odd-before-even pair must cross once: 1 precedes three evens, 3 precedes two, and 5 precedes one. Thus at least six adjacent swaps are necessary. Moving each even left across preceding odds attains this bound and preserves both internal orders.

**Common misconception:** Counting displaced elements instead of pair crossings.

## Q12

**Correct answer:** A

**Concept:** Atomicity of an invariant-preserving update sequence.

The pair may be inconsistent after the first update and before the second. If that interval is unprotected, another thread can observe it, giving A. B,C,D make false claims about mutex capabilities or implicit atomicity.

**Common misconception:** Protecting individual assignments while leaving the multi-field invariant temporarily exposed.

## Q13

**Correct answer:** 2
**Concept:** In-order acceptance across sequence wraparound.

The first 15 is discarded; 14 is accepted, making 15 expected. The first 0 is discarded; then 15 is accepted, followed by 0 and 1. The next expected value is 2. Discarded frames do not remain buffered under the given rule.

**Common misconception:** This receiver cannot advance through a previously discarded out-of-order frame when a gap later closes.

## Q14

**Correct answer:** 1

Rank-nullity gives nullity3−2=1. A nonempty solution set is one particular solution plus the null space, an affine line. Consistency is necessary to speak of a nonempty affine solution set.

## Q15

**Correct answer:** A, B

Concept: limits on dense subsets. Since |f(x)|=|x|, f tends to zero at zero and f(0)=0, proving A. For nonzero x, the difference quotient f(x)/x is 1 on rationals and −1 on irrationals; rational and irrational inputs occur arbitrarily close to zero, so this quotient has no limit and no derivative exists. B is true and D false. At one the rational and irrational limits are 1 and −1, so C is false. Continuity of the function does not force its difference quotient to converge.

## Q16

**Correct answer:** A, C

Concept: divide-and-conquer tree sums. Level j has 3ʲ calls of size n/2ʲ, costing Θ(n²(3/4)ʲ). Summing this decreasing geometric series gives Θ(n²), A; B incorrectly adds a logarithmic factor. The depth is log₂n and the number of leaves 3^(log₂n)=n^(log₂3), C. D confuses logarithmic depth with n levels.

## Q17

**Correct answer:** 3

The successive depths are 1 after a,2 after b,1 after +,2 after c,3 after d,2 after −,and1 after *. The maximum is 3. An operator reduces the depth by one because it consumes two values and produces one, not because it simply pops both without replacement.

## Q18

**Correct answer:** A

An element is pushed onto I, transferred once to O and eventually popped; it is never returned to I. A is true. A transfer can take linear time in the current size, disproving B's worst-case claim. Reversal puts the oldest element on top, preserving FIFO and disproving C. Enqueue can push I regardless of O, so D is false. Amortized constant cost differs from per-operation worst-case cost.

## Q19

**Correct answer:** A, C

The empty string begins and ends with an empty stack, so A is true. Every accepted prefix avoids a pop from empty, establishing C. Equal totals are insufficient: '())(' has equal totals but its third character tries to pop an empty stack. Thus B and D are false. Global balance and prefix balance are separate requirements.

## Q20

**Correct answer:** 52

**Concept:** Variance of an independent linear combination.

Independence removes the covariance term, and the constant contributes no variance. Thus Var(2X−3Y+7)=2²×4+(−3)²×4=16+36=52.

**Common misconception:** Carrying the negative coefficient into variance without squaring it.

## Q21

**Correct answer:** A, B, C

**Concept:** Closure under finite changes.

Finite F is regular. Union and difference of regular languages are regular, establishing A and B. F−L is finite, establishing C directly. D fails by taking L empty and a nonregular superset, such as {aⁿbⁿ}.

**Common misconception:** Assuming an arbitrary superset inherits a subset's language class.

## Q22

**Correct answer:** C
**Concept:** CPU execution-time comparison.

Ignoring the common factor N/10⁹, P's time is 1.5/3=0.5 and Q's time is 0.8×2/4=0.4. Speedup is old time divided by new time: 0.5/0.4=1.25. C is correct; A is its reciprocal, while B,D omit or miscombine factors.

**Common misconception:** Clock rate or CPI alone does not determine performance when instruction counts differ.

## Q23

**Correct answer:** A
**Concept:** Intersection and equivalence closure.

No pair of distinct elements shares a block in both partitions, so R∩S consists of the six reflexive pairs. In R∪S, the links 1–2–3–4–5–6 connect every element. Transitivity therefore puts all six into one class in T, giving 6²=36 ordered pairs. Only A has both counts. B omits reflexivity; C incorrectly retains nonreflexive intersection pairs; D does not complete transitivity.

**Common misconception:** The union of equivalence relations need not itself be transitive.

## Q24

**Correct answer:** D

Q can progress and release S; P can then proceed. No request from Q leads back to P, so there is no cycle. D is correct. A equates waiting with deadlock, B invents a missing circular edge, and C invents a request not stated. A blocked process need not belong to a deadlock.

## Q25

**Correct answer:** 2

**Concept:** DISTINCT combined with NULL exclusion in COUNT.

The distinct non-NULL values are 2 and 5. NULL is not counted by COUNT(expression), so the result is two.

**Common misconception:** Counting NULL as another distinct numeric value.

## Q26

**Correct answer:** 18

Concept: tree edge count and handshaking. A tree on ten vertices has nine edges; each contributes two to the degree sum. Total=2·9=18. Counting edges only once gives the wrong degree sum.

## Q27

**Correct answer:** A, C

**Concept:** Scope and cost of interrupt masking.

A is the specified masking effect. An interrupt arriving during a longer masked interval may wait longer, proving C. Masking on one CPU does not stop other CPUs, refuting B, and it does not change ordinary memory operations into atomic multi-CPU operations, refuting D.

**Common misconception:** Treating local interrupt exclusion as a complete multiprocessor lock.

## Q28

**Correct answer:** A, C

Distributivity holds in arithmetic modulo2^n, so A is valid even across wrapping. Multiplication by0 is always defined and zero, proving C. B changes an undefined zero-divided-by-zero expression into a defined constant, so it does not preserve definedness. For n=2,x=1,y=0, the two orders in D give1 and3, refuting D.

## Q29

**Correct answer:** A, C

The outputs encode the count of true inputs: s is its low bit and k its high bit, proving A. Complementing three inputs changes count m to3−m, complementing both bits, proving C. k is1 for counts2 and3, so B is false. Several triples share a count, so D is false. These are full-adder outputs, not an injective code for the input triple.

## Q30

**Correct answer:** A, C
**Concept:** Sequential state evolution.

Starting at 01: 01→11→10→01. Its period is three, and the second state after reset is 10. A,C are true. State 00 is a separate fixed point, never reached from reset, so B is false. At 11 the bits are equal, refuting D.

**Common misconception:** Reset selects one state-cycle component; not every representable state is reachable from it.

## Q31

**Correct answer:** A, B

For NULL, x>0 is UNKNOWN, which this CHECK accepts, proving A and refuting C. A non-NULL integer passes exactly when it is positive, proving B. NOT NULL would exclude the previously permitted NULL, refuting D. SQL CHECK acceptance differs from WHERE filtering of UNKNOWN.

## Q32

**Correct answer:** C

At the join, x merges 2 with 7 and y merges 7 with 2. Each becomes nonconstant in the stated abstraction. Their correlation is discarded, so the analysis cannot infer z=9. Actual execution gives 9 in both branches. A,B incorrectly retain branch-specific constants; D combines values from incompatible branches.

## Q33

**Correct answer:** 8 (exact)
**Concept:** Pipeline overlap with a load-use stall.

Three instructions in five stages take 3+5−1=7 cycles without stalls. The LOAD-to-first-ADD dependence adds one bubble. The second ADD obtains its operands by the stated forwarding, adding none. Total eight cycles.

**Common misconception:** A dependency does not imply a stall when forwarding supplies the value at the required stage.

## Q34

**Correct answer:** 25

A rank-one matrix can be written uvᵀ. Its trace is vᵀu=5. Squaring gives A²=u(vᵀu)vᵀ=5A, so trace(A²)=5·5=25. The identity depends on rank one; squaring the trace is not valid for arbitrary matrices.

## Q35

**Correct answer:** A

**Concept:** DNS record types.

AAAA records associate names with IPv6 addresses, A. Ethernet addresses, TCP sequence information and HTTP bodies belong to different mechanisms, eliminating B,C,D.

**Common misconception:** Confusing address resolution at different network layers.

## Q36

**Correct answer:** 2

**Concept:** Candidate-key closure and minimality.

C never appears on a dependency's right-hand side, so every key must contain C. It must also contain A or B: without either, neither can be derived. AC determines B and D, while BC first determines A and then D. Both are minimal. Every other key contains one of these, so exactly two candidate keys exist.

**Common misconception:** Counting nonminimal superkeys as candidate keys.

## Q37

**Correct answer:** 112

Concept: slotted-page free space. Existing occupancy is 32+12·4+3900=3980 bytes, leaving 116. The new slot consumes four, leaving 112 bytes for its record. Compaction can gather fragmented free space but cannot eliminate existing metadata.

## Q38

**Correct answer:** A, B

v's discovery and finish interval lies strictly inside u's, so it is a descendant, proving A. An edge from that descendant to u is a back edge, proving B. An edge u→v can skip intervening descendants and be forward rather than tree, refuting C. During v's exploration w would be undiscovered; an edge v→w would then discover w before v finished at7, contradicting w's discovery time10, so D is false. DFS intervals impose restrictions beyond merely labelling edges after the fact.

## Q39

**Correct answer:** B
**Concept:** Cumulative acknowledgments with reordering.

Until bytes 1000–1099 arrive, byte 1000 remains the first missing byte, so each of the first three ACKs is 1000. Once that segment arrives, buffered data make all bytes through 1399 contiguous, so the ACK advances to 1400. B matches; A,C,D incorrectly acknowledge across a gap or ignore buffered data.

**Common misconception:** Duplicate ACKs can result from reordering without actual packet loss.

## Q40

**Correct answer:** A, C
**Concept:** Recoverability versus dirty reads.

T2 commits after the transaction whose value it read, so the displayed schedule is recoverable (A). Its read nevertheless occurs before T1 commits, making it a dirty read and refuting cascadelessness (B). If T1 instead aborted after that read, T2 could need rollback (C). The displayed commit order directly refutes D.

**Common misconception:** Recoverable schedules can still permit cascading aborts.

## Q41

**Correct answer:** 10

Concept: queue order at a quantum boundary. Timeline: P 0–2; Q 2–4; R 4–5; P 5–7; Q 7–8; P 8–9. At time 2 the queue is Q,R,P by the specified arrival rule. Completion times are 9,8,5. Waiting times C−arrival−burst are 4,4,2, total ten. A boundary convention can change later queue order and must not be assumed silently.

## Q42

**Correct answer:** B

**Concept:** Theory of Computation — Pumping lemma

A permitted decomposition has |xy|<=p and |y|>=1, so k=|y| satisfies 1<=k<=p. Pumping y twice changes the length to p^2+k. It exceeds p^2 and is at most p^2+p, strictly less than p^2+2p+1=(p+1)^2. There is no square strictly between consecutive squares, so every permitted decomposition fails when pumped twice.

A wrongly requires k=p. B gives the necessary argument for every permitted decomposition. C treats a single bad decomposition as sufficient even though the pumping lemma promises only the existence of a good one. D is false: pumping down subtracts an arbitrary k between 1 and p, not necessarily 2p-1.

- **A:** False: wrongly fixes |y| = p instead of considering all decompositions with 1 <= |y| <= p.
- **B:** True: for every valid decomposition, pumping twice gives length p^2 + |y| with p^2 < p^2 + |y| < (p+1)^2, which cannot be a square.
- **C:** False: testing only one specific decomposition is insufficient to disprove regularity via the pumping lemma.
- **D:** False: pumping down does not necessarily land at (p-1)^2.

**Common misconception:** Refuting a pumping property requires defeating every allowed decomposition of the selected word.

## Q43

**Correct answer:** 258

LOOK travels50→70→20, distance20+50=70. SCAN travels50→199→20, distance149+179=328. The excess is328−70=258, twice the unnecessary outward distance199−70. Both stop at20 because no requests remain; do not add a final sweep to cylinder0.

## Q44

**Correct answer:** B

**Concept:** Liveness kill and use sets.

Assignment defines a new x and does not use old x; its right-hand side uses y and z. Thus the transfer removes x from live-out and adds y,z, B. A conflates old and new values; C reverses uses and definitions; D treats liveness as preventing assignment.

**Common misconception:** Keeping a variable's old value live merely because its newly assigned value is needed later.

## Q45

**Correct answer:** 2 (exact)

**Concept:** Theory of Computation — Turing machines and undecidability

Set 1 is recognizable by simulating M on 01 and accepting if M accepts. Set 4 is recognizable by dovetailing simulations of M on all binary strings and accepting as soon as one enters q.

Set 2 is not recognizable: given a machine N and input w, construct M which, on any input other than 01, simulates N(w) and accepts exactly if that simulation halts; on 01 it rejects. Then M belongs to set 2 exactly when N(w) does not halt. A recognizer for set 2 would recognize the complement of the halting problem, which is impossible.

Set 3 is also not recognizable. Given N,w, let M on input x simulate N(w) for |x| steps. If that bounded simulation has not halted, M halts; if it has halted, M loops forever. If N(w) never halts, M halts on every input. If N(w) halts after t steps, M loops on every sufficiently long input. Thus membership again recognizes nonhalting if set 3 were recognizable. Exactly sets 1 and 4 are recognizable, giving 2. The designated-state construction uses a computably inserted fresh q, so no accidental visit is required.

**Common misconception:** A finite existential witness can be dovetailed; universal termination and absence of accepted counterexamples cannot in general be recognized.

## Q46

**Correct answer:** 80

**Concept:** Interleaving subtree insertion sequences.

Root 4 must be first. Choose three of the remaining six positions for left-subtree keys, in choose(6,3)=20 ways. Within the left subtree, 2 must precede 1 and 3, whose order has two choices. The right subtree similarly has two orders after 6. Total 20×2×2=80.

**Common misconception:** Requiring all left-subtree insertions to precede all right-subtree insertions.

## Q47

**Correct answer:** A, B, C

**Concept:** Algorithms — Minimum spanning trees and constrained counting

1. A spanning tree needs five edges and must connect the two triangles. Four unit edges and one weight-2 connector give weight 6. A lighter tree cannot connect all six vertices, since every connector weighs at least 2.
2. For weight 6, choose a spanning tree in each triangle in 3 ways each, then one of AD, BE, CF in 3 ways. This gives 3×3×3=27.
3. A weight-7 tree has either four unit edges and AE, or three unit edges and two weight-2 connectors. The first case gives 3×3=9.
4. In the second case choose the two connectors in 3 ways. The three unit edges must split as two in one triangle and one in the other: taking all three from a triangle would create a cycle. There are 2 choices of which triangle gets two edges, 3 choices of its spanning tree, and 2 choices of the other triangle's single edge. That edge must attach its otherwise unconnected third vertex to a connector endpoint. Thus this case contributes 3×2×3×2=36.
5. Total weight-7 trees: 9+36=45.

- **A:** Correct: the lower bound 6 is attained.
- **B:** Correct: the three independent choices give 27 distinct edge sets.
- **C:** Correct: the two disjoint weight compositions give 45 trees.
- **D:** Incorrect: a spanning tree in each triangle together with AE has weight 7 and uses no weight-2 edge.

**Common misconception:** Equal-weight edges create multiple optima, and counting the next weight requires checking connectivity and cycles, not just the number of chosen edges.

## Q48

**Correct answer:** 2 (exact)

**Concept:** Engineering Mathematics — Extrema and mean value theorem

1. f_a'(x)=4g(x), where g(x)=x^3-a*x+1. Two strict minima of this quartic require three distinct real roots of g, with alternating derivative signs -,+,-,+.
2. For a<=0, g is increasing and has only one root. For a>0 its turning points are at +/-sqrt(a/3). Its local maximum is 1+2(a/3)^(3/2)>0, and its local minimum is 1-2(a/3)^(3/2).
3. Three distinct roots exist exactly when 1-2(a/3)^(3/2)<0, equivalently a^3>27/4. The threshold is approximately 1.88988, so the smallest integer is 2. At equality a repeated stationary point does not give a second strict minimum.

**Common misconception:** Stationary points must be classified; a repeated derivative root need not be an extremum.

## Q49

**Correct answer:** 2

After replacement,9 first swaps with smaller child2 at index 3. It then swaps with smaller child4 at index 6 and reaches a leaf. The final heap is[2,3,4,8,7,9,5]. Two swaps occur. The smaller child must be chosen to preserve heap order with both children.

## Q50

**Correct answer:** 3

Deleting6 leaves [8], below the two-key minimum. The right sibling [10,12,14] has three keys, so it lends10, yielding[8,10] and[12,14]. No leaf is merged and the root retains three children. Root separator values must be adjusted, but that does not alter the child count.

## Q51

**Correct answer:** A

**Concept:** Completion, complementation, and state distinguishability.

The original language is a^k for k≥2. Add a dead state for every missing b transition, with self-loops on both symbols. Complementing accepting states gives a complete four-state DFA. The four original-language states corresponding to prefixes ε,a,aa,b are distinguishable: a separates ε from a; ε separates aa from ε or a; and an appropriate a-suffix separates b from each nondead prefix. Complementation preserves distinguishability. Thus four is minimal; B is too small and C,D exceed the exhibited minimum.

**Common misconception:** Complementing the accepting set of a partial DFA without first representing rejecting undefined transitions.

## Q52

**Correct answer:** A, C, D

The Boolean matrix merges all parallel edges into one true entry, losing multiplicities(A,D). Therefore its row sum can undercount outdegree, disproving B. Parallel-edge multiplicity does not change whether a path exists, so collapsing them preserves reachability(C). Multiplicity matters for degrees and edge counts even when it does not matter for reachability.

## Q53

**Correct answer:** B

**Concept:** Linked-list reversal invariants.

After saving next, point cur back to prev, move prev to the newly reversed head cur, then advance cur to saved next. This is B. A advances too soon and rewires the wrong node; C also rewires the successor and can dereference null; D retains the forward link and moves both pointers to the successor, performing no reversal.

**Common misconception:** Updating traversal pointers before preserving and reversing the current node's link.

## Q54

**Correct answer:** A

**Concept:** Operating Systems — Contiguous allocation and coalescing

1. First-fit allocates A at [0,50). B cannot fit the remaining [50,60), so it occupies [100,135).
2. Freeing A and X joins [0,50), [50,60), and [60,100) into [0,100). B prevents further merging. The other holes have sizes 45 and 40. The largest is 100.
3. Best-fit also puts A at [0,50), since the 60-unit hole is the smallest that fits 50. It puts B in the 40-unit hole at [200,235).
4. When A and X are freed, the entire interval [0,180) becomes free: the original [100,180) hole was never occupied. Y prevents merging beyond 180. The largest hole is 180.

- **A:** Correct: the maxima are 100 and 180.
- **B:** Incorrect: best-fit leaves [100,180) available for coalescing.
- **C:** Incorrect: first-fit's B blocks the interval at address 100.
- **D:** Incorrect: it reverses the two outcomes.

**Common misconception:** A choice that leaves a smaller immediate remainder can improve a later allocation by preserving holes that will coalesce after deallocation.

## Q55

**Correct answer:** 0.3679 (range 0.36785–0.36795)
**Concept:** Tangent intercepts and area minimization.

The tangent is y=(ln a+1)x−a. Its intercepts are −a and a/(ln a+1), so area is a²/[2(ln a+1)] for the given positive denominator. Set u=ln a+1>0: area is e^(2u−2)/(2u). Its logarithmic derivative is 2−1/u, negative below u=1/2 and positive above. Thus the global minimum is at a=e^(−1/2), with area e⁻¹≈0.367879, rounding to 0.3679.

**Common misconception:** Use the magnitude of the negative vertical intercept when computing the triangle's positive area.

## Q56

**Correct answer:** B
**Concept:** Saturation versus modular overflow.

S saturates 7+3 to 7, then adds −5 to obtain 2. W represents 10 as signed −6, then wraps −6−5=−11 to signed 5. Thus (2,5). A delays saturation until the end; C fails to wrap the second W addition; D reports intermediate values.

**Common misconception:** Applying overflow rules after each operation differs from applying them only to the final exact result.

## Q57

**Correct answer:** 2

a must be first and d last. The middle elements b,c are incomparable and can occur in either order. Thus the extensions are a,b,c,d and a,c,b,d, giving2. A linear extension must preserve existing comparisons but can choose an order for incomparable elements.

## Q58

**Correct answer:** 6

The tokens are ID(ifif), EQEQ(==), EQ(=), keyword(if), EQ(=), ID(iff). Longest match prevents splitting ifif or iff into a keyword plus suffix. Three consecutive equals signs yield a two-character token followed by a one-character token. There are six tokens in total.

## Q59

**Correct answer:** 1.7

For k equal packets of length L across h equal store-and-forward links, the total is(k+h−1)L/r because packets pipeline after the first packet traverses all links. Three packets each contain2000+100=2100 bytes, taking5×2.1=10.5 ms. Six packets each contain1000+100=1100 bytes, taking8×1.1=8.8 ms. The saving is1.7 ms. Smaller packets improve pipeline fill time but increase total header bytes.

## Q60

**Correct answer:** C
**Concept:** Conditional HTTP validation.

A matching entity tag permits the server to report that the cached representation may be reused without transferring the full representation body. The client still sends the request and receives the validation response, so a network round trip remains (C). A confuses validation with a fresh local-cache hit. B incorrectly assigns a representation body to 304. D makes an unsupported claim about unrelated caches.

**Common misconception:** Saving transferred bytes and eliminating network latency are different benefits.

## Q61

**Correct answer:** B

**Concept:** Computer Organization and Architecture — Hardwired and microprogrammed control

The START pulse must be outside the wait loop. The loop must avoid repeating the register increment, and DATA must be sampled only after READY establishes completion. Routine B issues START once, waits in a control-only state, and executes the data transfer and increment exactly once afterward.

A repeats START and the increment during waiting. B satisfies all requirements. C starts only once but increments on each wait-loop visit. D does not wait and can sample invalid data if memory takes longer than the start cycle.

- **A:** False: repeats START and the pointer increment on each wait-loop cycle.
- **B:** True: routine B asserts START once, waits for READY, and transfers data and increments exactly once.
- **C:** False: asserts START once but repeatedly increments the pointer while polling.
- **D:** False: fails to poll READY and may sample invalid data if memory access is slow.

**Common misconception:** A control-state self-loop reexecutes that state's data-path operations every cycle.

## Q62

**Correct answer:** C

Concept: zero-weight cycles and walks. Every s-to-t walk must pay 1 entering a and 2 leaving b for t. Repeating a→b→a adds zero; hence infinitely many walks attain weight 3 (C). A would require an exploitable negative cycle; B ignores zero-cost repetitions; D overlooks s→a→b→t. Paths and walks have different counting behavior.

## Q63

**Correct answer:** B, C

Write L=[[1,0],[l,1]] and U=[[u,v],[0,w]]. Matching A forces u=0 and lu=1, impossible. Nonzero determinant−1 still proves invertibility, making C true and A false. Swapping rows gives[[1,1],[0,1]], already upper triangular, so L=I works and B is true. Invertibility guarantees a unique solution for every b, disproving D. Failure of unpivoted elimination is not singularity.

## Q64

**Correct answer:** B
**Concept:** Signed fixed-point multiplication and ties-to-even.

0xE6 represents −26/16=−1.625, and 0x1C represents 28/16=1.75. Their product is −2.84375, exactly halfway between −45/16 and −46/16. The even retained integer is −46, giving −2.875 and byte 256−46=210=0xD2. A is the odd tie neighbour; C loses the sign; D rounds to an unrelated representable value.

**Common misconception:** Ties-to-even uses the retained integer's low bit, including for negative values; it is not simply rounding toward zero.

## Q65

**Correct answer:** 0.125

The smallest normal is1.00×2^−2=1/4. With p=3, adjacent significands differ by1/4 of that binade's scale, so subnormal spacing is2^−4=1/16. The target3/32 lies halfway between1/16 and2/16. Ties-to-even chooses coefficient2, giving1/8=0.125. Gradual underflow keeps this spacing below the minimum normal.

