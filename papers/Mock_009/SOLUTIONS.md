# GATE CS 2027 — Mock 009: Worked Solutions

## Q1

**Correct answer:** B

**Concept:** Negating a universal statement.

“Not every” means that at least one submitted report lacks a diagram. Thus B is equivalent. A and C both say none has a diagram, which is stronger; D concerns a report outside the submitted set and need not hold.

**Common misconception:** Negating “all” produces “none” rather than “at least one not”.

## Q2

**Correct answer:** 9

**Concept:** Work-rate conservation.

The job requires 6×8=48 worker-days. The first two days complete 12 worker-days, leaving 36. Four workers require 36/4=9 additional days.

**Common misconception:** Applying the reduced workforce to work already completed.

## Q3

**Correct answer:** C

**Concept:** Necessary conditions with an exception.

For a nonexempt consignment, release implies inspection. C asserts release and denies inspection, violating this implication. A is allowed by the exemption; B is allowed because inspection does not guarantee release; D satisfies the condition regardless of exemption.

**Common misconception:** Reading “only if” as “if and only if”.

## Q4

**Correct answer:** 4.472

**Concept:** Composition of rotations.

An original point (x,y) becomes (−x,−y), then (4+x,2+y). The displacement vector is always (4,2), of length √20=4.47213595…, rounding to 4.472. The accepted range is 4.4715–4.4725.

**Common misconception:** Adding rotation angles while ignoring their different centres.

## Q5

**Correct answer:** 180

**Concept:** Block arrangements with repetitions.

Treat AOO as one block alongside B,L,L,N. These five objects have 5!/2!=60 arrangements. Inside the vowel block there are 3!/2!=3 arrangements. The product is 180.

**Common misconception:** Dividing for the repeated vowels but forgetting the repeated consonant.

## Q6

**Correct answer:** 84

**Concept:** Integer optimization with a capacity constraint.

Let x items use A and 20−x use B. Time is 2x+20−x=20+x≤28, so x≤8. Cost is 3x+5(20−x)=100−2x, decreasing in x. Choose x=8, giving cost 84 and exactly 28 hours.

**Common misconception:** Choosing the cheaper method for every item without checking time feasibility.

## Q7

**Correct answer:** 25

**Concept:** Membership counting and attainability.

There are 80+75+70=225 subject memberships. If t students take all three, the other students contribute at most two memberships each, so 225≤3t+2(100−t), giving t≥25. Equality is attained with 25 in all three, 30 in A and B only, 25 in A and C only, and 20 in B and C only. These groups total 100 and reproduce all three subject totals.

**Common misconception:** Reporting a counting bound without showing it can be achieved.

## Q8

**Correct answer:** 0.5333

**Concept:** Conditional probability by ordered outcomes.

Prime sums 2,3,5,7,11 have respectively 1,2,4,6,2 ordered dice outcomes, totalling 15. Among these, a factor divisible by 3 occurs in zero outcomes for sum 2, zero for sum 3, two for sum 5, four for sum 7, and two for sum 11. Thus the probability is 8/15=0.533333…, rounding to 0.5333. Accepted range: 0.53325–0.53335.

**Common misconception:** Treating the five possible prime sums as equally likely.

## Q9

**Correct answer:** 17

**Concept:** Piecewise tariffs and integer feasibility.

Ten units cost 15+40=55. The remaining budget is 45, permitting floor(45/6)=7 more units. Seventeen units cost 97; eighteen cost 103 and are infeasible.

**Common misconception:** Charging the higher rate on all consumption after crossing the threshold.

## Q10

**Correct answer:** A

**Concept:** Confounding in observational comparisons.

A supplies a pre-existing difference that can explain part of the final gap, undermining attribution of the entire gap to tutoring. B describes a venue, C gives a common assessment, and D describes reporting completeness; none supplies a competing explanation for the score difference.

**Common misconception:** Interpreting a voluntary-treatment comparison as randomized causal evidence.

## Q11

**Correct answer:** 8

**Concept:** Complements in an interval of a subset lattice.

Both X and Y must contain 1 and 2. Each of 3,4,5 must be in exactly one of X,Y: neither would violate the union requirement, while both would violate the intersection requirement. The independent choices give 2³=8 ordered pairs.

**Common misconception:** Dividing by two even though pairs are ordered.

## Q12

**Correct answer:** B

**Concept:** Synchronous binary counting.

All right-hand sides use the old state. The trajectory is 011→100→101→110→111→000. B is therefore correct. A is the state after four edges, C after six, and D after two.

**Common misconception:** Updating bits sequentially within a single clock edge.

## Q13

**Correct answer:** 0

**Concept:** Eigenvectors and singularity.

For v=(1,−1,1,−1)ᵀ, Pv=−v. Consequently (I+P)v=0 with v nonzero, so I+P is singular and has determinant zero.

**Shortcut:** Find a null vector instead of expanding a 4×4 determinant.

**Common misconception:** Assuming that adding the identity to an invertible matrix preserves invertibility.

## Q14

**Correct answer:** 512

**Concept:** Instruction-field bit allocation.

Each register field needs log₂32=5 bits. Three such fields and the immediate use 15+8=23 bits. The remaining nine opcode bits encode 2⁹=512 patterns.

**Common misconception:** Subtracting the number of registers instead of the field width.

## Q15

**Correct answer:** B

**Concept:** Array size versus string termination.

The stored bytes are 'a', an explicit null, 'b', 'c', and the implicit terminating null: five bytes. strlen stops at the first null and returns one. A gets both values wrong; C counts through the embedded null; D omits the implicit terminator from the array size.

**Common misconception:** Treating every byte of a character array as part of its C string.

## Q16

**Correct answer:** 6

**Concept:** Inversions under stable partition.

Each odd-before-even pair must cross once: 1 precedes three evens, 3 precedes two, and 5 precedes one. Thus at least six adjacent swaps are necessary. Moving each even left across preceding odds attains this bound and preserves both internal orders.

**Common misconception:** Counting displaced elements instead of pair crossings.

## Q17

**Correct answer:** A, B, C

**Concept:** Regular-expression union.

A belongs to a*b, using two a symbols. B belongs to ab*, using two b symbols. C belongs to both branches. D starts with b and ends with a, matching neither branch.

**Common misconception:** Applying the star to the entire alternative instead of the preceding symbol.

## Q18

**Correct answer:** 24

**Concept:** Alignment and final padding.

c occupies offset 0. i starts at 4 and occupies 4–7. d starts at 8 and occupies 8–15. e occupies 16. The end offset is 17, rounded up to 24 for eight-byte total alignment.

**Common misconception:** Summing object sizes without accounting for internal and trailing padding.

## Q19

**Correct answer:** B

**Concept:** Inherited descriptors and open file descriptions.

Both descriptors refer to the same open file description, which contains the current offset. B is correct. A describes separately maintained execution state, C incorrectly makes ordinary stack storage shared, and D contradicts the distinct process identities created by fork.

**Common misconception:** Equating a copied descriptor table with separately opened files.

## Q20

**Correct answer:** 0.25

**Concept:** Covariance with an indicator.

E[X]=3.5 and E[Y]=1/2. Only even outcomes contribute to XY, so E[XY]=(2+4+6)/6=2. Therefore Cov(X,Y)=2−3.5/2=0.25.

**Common misconception:** Assuming a function of X is independent of X.

## Q21

**Correct answer:** 0.25

**Concept:** Derivative of an inverse function.

Since f(1)=2, g(2)=1. Differentiate f(g(y))=y: g′(y)=1/f′(g(y)). With f′(x)=3x²+1, g′(2)=1/4.

**Common misconception:** Evaluating f′ at 2 rather than at g(2).

## Q22

**Correct answer:** B

**Concept:** B-tree occupancy bounds.

There are four levels. At minimum occupancy, each internal node has two children and each node has one key: 1+2+4+8=15 keys. At maximum occupancy, each internal node has four children and every node has three keys: 3(1+4+16+64)=255. A uses one fewer level; C confuses leaves with all keys; D counts maximum nodes, not maximum keys.

**Common misconception:** Mixing height measured in edges with height measured in levels.

## Q23

**Correct answer:** B

**Concept:** IPv4 subnet boundaries.

A /27 leaves five host bits and covers addresses 96 through 127. The last address is broadcast, so the highest host is 126. A is broadcast, C lies outside the subnet, and D is valid but not highest.

**Common misconception:** Assigning the all-one host field to a host.

## Q24

**Correct answer:** 3

**Concept:** Priority encoding across updates.

The first selected input is 5. Clearing only that input leaves input 3 asserted, so the next output is 3.

**Common misconception:** Retaining the old priority result after changing the inputs.

## Q25

**Correct answer:** A

**Concept:** Precise exceptions and retirement.

On an older fault, architectural state must exclude younger instructions' effects. Deferring visible stores preserves that boundary, making A correct. It neither fixes load latency (B), removes dependencies (C), nor guarantees predictions (D).

**Common misconception:** Treating speculative execution and architectural commitment as the same event.

## Q26

**Correct answer:** 16

**Concept:** Structure copying and pointer aliasing.

The array members are copied into t, but the pointer value is copied unchanged. Therefore t.p still points to s.a[0]. Setting t.a[0]=7 changes t's array; writing through t.p sets s.a[0]=9. Their sum is 16.

**Common misconception:** Expecting a copied pointer automatically to point inside the copied structure.

## Q27

**Correct answer:** B

**Concept:** Summing work across geometric loop strides.

For strides 1,2,…,n, the inner counts are n,n/2,…,1. Their sum is 2n−1, hence Θ(n). A ignores inner work; C assumes every outer iteration costs n; D likewise fails to account for increasing strides and overcounts further.

**Common misconception:** Multiplying independent-looking loop bounds when the inner bound depends on the outer variable.

## Q28

**Correct answer:** A, C

**Concept:** Finite configuration-space reachability.

Determinism makes a repeated nonhalting configuration repeat its entire future, proving A. Record configurations and stop on acceptance, rejecting halt, or repetition; finiteness ensures one occurs, proving C. Plain simulation can loop forever, refuting B and D.

**Common misconception:** Confusing finitely many possible states with finitely many execution steps.

## Q29

**Correct answer:** A

**Concept:** Left factoring with an empty suffix.

Extract the shared initial a, leaving suffixes b,c,ε. A produces exactly ab,ac,a. B puts the common a at the end; C permits arbitrarily long suffixes; D leaves X unreachable and produces only a.

**Common misconception:** Dropping ε when one production equals the common prefix.

## Q30

**Correct answer:** A

**Concept:** Blocking and CPU dispatch.

Completion removes the reason for blocking, making the process eligible for the CPU, hence ready. It does not terminate the process (B) or guarantee immediate dispatch (C). D describes the opposite direction and the wrong starting state.

**Common misconception:** Assuming an I/O completion necessarily preempts the current process.

## Q31

**Correct answer:** 5

**Concept:** Relationship cardinalities and integer bounds.

With d departments, 3d≤17, so d≤5. Five are achievable with department sizes 3,3,3,3,5.

**Common misconception:** Rounding a maximum feasible count upward.

## Q32

**Correct answer:** A, C

**Concept:** TCP connection demultiplexing.

For these IPv4 TCP connections, both endpoint addresses and ports identify the connection, so C holds and distinct remote endpoints can distinguish them, as A states. A listening service routinely retains the same local endpoint for many established connections, refuting B and D.

**Common misconception:** Treating the server's port as the entire connection identity.

## Q33

**Correct answer:** 6

**Concept:** Homomorphisms from cyclic groups.

The image a of the generator 1 determines the homomorphism. It must satisfy 12a=0 mod 18, equivalently a=0 mod 3. The six images 0,3,6,9,12,15 all work. In general the count is gcd(12,18)=6.

**Common misconception:** Allowing arbitrary generator images without respecting its order.

## Q34

**Correct answer:** B

**Concept:** Shannon expansion and multiplexers.

At x=0, F=yz; at x=1, F=y+z. Thus B supplies the two cofactors. A reverses them; C fails when y=z=1 and x=0; D fails, for example, at x=y=z=0.

**Common misconception:** Interchanging the inputs selected by zero and one.

## Q35

**Correct answer:** A

**Concept:** Structural versus data hazards.

IF and MEM require the same single port concurrently. Forwarding carries operand results but adds no memory port, so A holds and D fails. Neither arithmetic overflow nor a branch/control dependency follows, eliminating B and C.

**Common misconception:** Assuming complete forwarding removes every pipeline stall.

## Q36

**Correct answer:** 22

**Concept:** Shared mutation during recursive descent and return.

Starting at x=1, the calls with n=3,2,1 change x to 4,6,7. The n=0 call returns 7. Returning through n=1 decrements x to 6 and returns 7+6=13; n=2 decrements it to 5 and returns 13+5=18; n=3 decrements it to 4 and returns 18+4=22.

**Common misconception:** Saving a separate pointed-to integer for each activation when only the pointer is passed.

## Q37

**Correct answer:** A, C

**Concept:** Cycle property of minimum spanning trees.

The unique heaviest edge on a cycle cannot be in an MST: removing it from a proposed tree gives a cut crossed by a lighter edge of the cycle, reducing weight. This proves A. The remainder of the cycle also provides an alternate route after removing that edge, proving C. For a graph consisting only of this cycle, both weight-2 edges occur in the MST, refuting B. Additional graph structure can contain equal-cost alternatives, so uniqueness does not follow; D is false.

**Common misconception:** Excluding every edge whose weight is not the minimum on a cycle.

## Q38

**Correct answer:** B

**Concept:** DFA upper and lower state bounds.

Store the last four bits, padding shorter prefixes on the left with zeros. This gives a complete 16-state DFA, accepting exactly when the stored first bit is 1. For a lower bound, take any two distinct four-bit words and a differing position i, numbered from the left. Appending i−1 zeros makes that differing position fourth from the right. The resulting strings differ in acceptance, so all 16 words reach distinguishable states. Exactly 16 states are necessary and sufficient. A is below the lower bound; C and D exceed the exhibited minimum.

**Common misconception:** Counting positions in an NFA as if they were sufficient deterministic memory.

## Q39

**Correct answer:** 225

**Concept:** Counting permutations by cycle type.

The allowed partitions of six into even lengths are 6, 4+2, and 2+2+2. They contribute 5!=120, choose(6,4)×3!×1!=90, and 6!/(2³×3!)=15. The total is 225.

**Common misconception:** Distinguishing the order of disjoint cycles or their cyclic starting points.

## Q40

**Correct answer:** A, C, D

**Concept:** Backward liveness across branching control flow.

On the B2 path, y is read before any redefinition, so A holds. On B3, a,b,c are read; thus D holds and B is false. The old x is read on neither path: B2 never uses it, and B3 overwrites it before use. Hence C holds. Including the pending branch test, the full live set is {a,b,c,y,p}.

**Common misconception:** Treating a value used earlier in the block as necessarily live after its last use.

## Q41

**Correct answer:** 5

**Concept:** Round-robin scheduling with I/O.

The CPU schedule is P:[0,2), Q:[2,4), Q:[4,6), P:[6,8), Q:[8,9). P performs I/O on [2,5), then waits [5,6), giving waiting time 1. Q waits [0,2) and [6,8), giving 4. Their sum is 5. Q is not preempted at time 5 because the I/O completion only enqueues P.

**Common misconception:** Including blocked I/O time in ready-queue waiting time.

## Q42

**Correct answer:** B

**Concept:** Key–foreign-key join cardinality.

Every R tuple finds at least one S tuple by the foreign key and at most one by the key of S. Hence exactly 100 joined tuples result. Set projection cannot collapse them here because the join includes all R attributes: distinct R tuples remain distinct. A contradicts the foreign key; C ignores uniqueness in S; D ignores the exact bound established by both constraints.

**Common misconception:** Assuming every join can expand to the Cartesian-product size regardless of keys.

## Q43

**Correct answer:** 14

**Concept:** Store-and-forward pipelining and queueing.

Link 1 transmissions finish at times 3,4,6, so complete packets reach the router at 5,6,8. Link 2 sends A during [5,6), B during [6,10), then C during [10,12). C's last bit takes two more milliseconds to reach the destination, arriving at 14.

**Common misconception:** Adding per-packet delays without accounting for concurrent links and the router queue.

## Q44

**Correct answer:** A, B, D

**Concept:** Signed overflow in two's-complement addition.

For equal-sign operands, a result with the opposite sign is outside the signed range, giving A and B. The equivalent bit-level test is XOR of carry into and out of the sign bit, giving D. Opposite-sign addition stays within the signed range, so C is false.

**Common misconception:** Using the carry-out bit alone as the signed overflow flag.

## Q45

**Correct answer:** A, B, D

**Concept:** Commuting idempotents and joint eigenspaces.

An idempotent is diagonalizable with eigenvalues 0 and 1. Commuting idempotents preserve one another's eigenspaces and can be diagonalized together. Let k be the dimension where both eigenvalues are 1. The dimensions for joint eigenvalues (1,1),(1,0),(0,1),(0,0) are k,3−k,2−k,k−1. Nonnegativity forces k=1 or 2. Thus rank(E−F)=5−2k is 3 or 1 (A), trace(E+F)=3+2=5 (B), and rank(EF)=k need not be 2 (C false). If k=1, E+F has eigenvalues 2,1,1,1 and determinant 2; if k=2 it has a zero eigenvalue and determinant 0 (D).

**Common misconception:** Identifying the product's rank with the smaller rank without considering the intersection.

## Q46

**Correct answer:** 1.2308

**Concept:** CPI versus elapsed instruction time.

A's CPI is 1+0.30×0.10×20=1.6, giving 1.6 ns per instruction. B's CPI is 1+0.30×0.05×20=1.3. For period T, require 1.3T≤1.6, or T≤16/13=1.230769… ns. Rounded answer 1.2308; accepted range 1.23075–1.23085.

**Common misconception:** Comparing CPIs without accounting for different clock periods.

## Q47

**Correct answer:** B

**Concept:** Linked-list reversal invariants.

After saving next, point cur back to prev, move prev to the newly reversed head cur, then advance cur to saved next. This is B. A advances too soon and rewires the wrong node; C also rewires the successor and can dereference null; D retains the forward link and moves both pointers to the successor, performing no reversal.

**Common misconception:** Updating traversal pointers before preserving and reversing the current node's link.

## Q48

**Correct answer:** 37

**Concept:** Huffman merge-cost identity.

Merge 2 and 3 to get 5, then 5 and 7 to get 12, then 12 and 8 to get 20. Each merge adds one code bit to every leaf beneath it, so the weighted path length is 5+12+20=37. Equivalently the lengths are 3,3,2,1 and 2×3+3×3+7×2+8×1=37.

**Common misconception:** Summing only the final root weight rather than all merge weights.

## Q49

**Correct answer:** A, D

**Concept:** Decidability under a totality promise.

Enumerate strings by length and simulate M on each. Every simulation halts by the promise; if any string is accepted it will eventually be found, proving A. D tests only finitely many strings, so it terminates with either answer.

For B and C, given an arbitrary machine N and input w, construct M that on input x simulates N(w) for |x| steps and accepts exactly if N halts within that bound. M always halts. Its language is nonempty exactly when N(w) halts. A decider for emptiness, or equivalence to the empty language, would therefore decide the halting problem, which is impossible. B and C are false.

**Common misconception:** Confusing termination of each individual test with termination of an infinite search for a negative answer.

## Q50

**Correct answer:** 4

**Concept:** Register requirements for expression trees.

Each leaf needs one register. Each two-leaf sum needs two. At each multiplication, after one sum is retained in a register, evaluating its sibling sum needs two additional registers, so each product needs three. At the root, retaining one product while evaluating the other requires 1+3=4 registers. This ordering attains four. Whichever product is evaluated first, the other still requires three while the first remains live, proving four is minimal under the stated restrictions.

**Common misconception:** Taking the maximum child requirement without counting a retained sibling result.

## Q51

**Correct answer:** B

**Concept:** Virtual reservation and demand allocation.

An address range can be validly reserved before private physical frames are allocated; first writes trigger backing allocation. This proves B and refutes A. Address translation allows distinct virtual and physical addresses, refuting C, and first-write faults on valid mappings refute D.

**Common misconception:** Treating a valid virtual mapping as proof that its private physical storage is already present.

## Q52

**Correct answer:** A, C

**Concept:** Isolation anomalies and locking.

Observing different committed values of the same row is a nonrepeatable read, establishing A. It need not involve uncommitted data, so B is false. A continuously held shared lock prevents a conflicting exclusive lock, establishing C under the given locking rules. Updating an existing row suffices; insertion is not required, so D is false.

**Common misconception:** Conflating a dirty read, a nonrepeatable read, and a phantom.

## Q53

**Correct answer:** 0.1111

**Concept:** Nested retransmissions and acknowledgment loss.

Ignore failed data attempts when counting arrivals: each successful data arrival independently ends the procedure with probability 0.9, when its acknowledgment arrives. The number of arrivals is geometric with mean 1/0.9=10/9. Excluding the first gives 1/9=0.111111… duplicates. Data losses affect the number of attempts but not this arrival count. Accepted range: 0.11105–0.11115.

**Common misconception:** Using the full-attempt failure probability to count receiver duplicates, including packets that never arrived.

## Q54

**Correct answer:** C

**Concept:** State-cycle analysis and input counting.

Input 1 cycles 01→10→11→01, while input 0 resets to 01. Acceptance therefore requires the trailing run of ones to have length divisible by three. At length five, a string containing a zero is accepted with trailing run length 0 or 3: respectively 16 strings ending in 0 and two ending in 0111 (one free prefix bit). The all-one string has five trailing ones and is rejected. Total 18, option C. A omits the trailing-three case; B includes only one of its two prefixes; D exceeds the exhaustive count.

**Common misconception:** Counting all ones rather than only those after the last reset.

## Q55

**Correct answer:** 0.5333

**Concept:** Exponential races and memorylessness.

The first event time min(X,Y) is exponential with rate 5, with mean 1/5. Conditional on X winning the race, the first-event time retains this distribution: its conditional density is 5e^(−5t). By memorylessness, Y's remaining time then has mean 1/3. Under X<Y, the maximum is Y, so its conditional mean is 1/5+1/3=8/15=0.533333…. Accepted range: 0.53325–0.53335.

**Common misconception:** Using the unconditional mean of Y after conditioning on Y being the later event.

## Q56

**Correct answer:** 8

**Concept:** Set mapping and independent LRU histories.

The block sequence is 0,2,0,4,2,1,3,5,1. In set 0, references 0,2,0,4,2 produce miss,miss,hit,miss,miss: accessing 0 refreshes it, so 4 evicts 2, which later must be fetched again. In set 1, references 1,3,5,1 are all misses: 5 evicts 1. Thus four misses per set give eight fetches.

**Common misconception:** Maintaining one global LRU order instead of a replacement order within each set.

## Q57

**Correct answer:** A, C

**Concept:** Ancestor bounds during BST search.

After 50,20,40, the next node must lie strictly between 40 and 50, so 48 is possible (A). After 20 the upper bound 50 still applies, excluding 55 (B false). After 47 the interval becomes (40,47), proving C. Successive left and right choices are allowed when all ancestor bounds remain satisfied, so D is false.

**Common misconception:** Checking only the immediately previous comparison and forgetting older bounds.

## Q58

**Correct answer:** B

**Concept:** Longest-path dynamic programming in a DAG.

Initialize the source distance to zero and unreachable distances to negative infinity; process reachable edges in topological order. Every predecessor distance is final before a vertex is processed, so maximizing over incoming paths is correct regardless of negative weights. This proves B and refutes A. Path lengths in edges may differ (C false), and converting to an undirected graph destroys the acyclic dependency structure (D false).

**Common misconception:** Transferring restrictions of greedy shortest-path algorithms to topological dynamic programming.

## Q59

**Correct answer:** 2

**Concept:** Generated strings versus derivations.

After m nonempty productions the string is a^m b^k with m≤k≤2m. Length six requires m+k=6, so m can be 2 or 3. The two words are a²b⁴ and a³b³. Different production choices cannot introduce another word with the same pair of counts because all a symbols precede all b symbols.

**Common misconception:** Counting production sequences separately even when their terminal strings coincide.

## Q60

**Correct answer:** -0.3333

**Concept:** Integral constraints and quadratic extrema.

The constraints give a+b+1=0 and a/3+b/2+1=0. Substitution gives a=3, b=−4. Therefore f(x)=3x²−4x+1 has its minimum at x=2/3 inside the interval, with value −1/3. The endpoints give 1 and 0, both larger. Rounded answer −0.3333; accepted range −0.33335–−0.33325.

**Common misconception:** Checking only endpoints or solving the integral equation without the endpoint condition.

## Q61

**Correct answer:** B

**Concept:** Copy propagation and killed facts.

Before the assignment y=5, x and y have the same value, so the use in z may be replaced. Afterwards x still has the original y while y has 5, so a direct replacement in w is generally wrong. B is correct. A ignores the redefinition; C assumes every initial y equals 5; D forbids the valid first substitution.

**Common misconception:** Treating a copy assignment as a permanent alias relationship.

## Q62

**Correct answer:** 3

**Concept:** Wait-for graph cycles.

The edges are P→Q, Q→R, R→P and S→Q. P,Q,R form a directed cycle. S depends on it but no path returns to S, so S is not on a cycle. Exactly three processes satisfy the question, even though S cannot make progress either under the stated rules.

**Common misconception:** Equating every process blocked behind a cycle with membership in the cycle itself.

## Q63

**Correct answer:** 5

**Concept:** SQL bag semantics.

Each of the two copies of 1 joins to 2 and 3, contributing four rows. The single 2 joins to 3, contributing one more. Equal values do not join under strict inequality. Total five rows.

**Common misconception:** Deduplicating input values when neither DISTINCT nor a set operation is present.

## Q64

**Correct answer:** B

**Concept:** Independently expiring DNS records.

The CNAME expires at time 120, so at time 80 it has 40 seconds remaining. The A record expires at 20+50=70 and is already stale. Reuse the live alias mapping but resolve its target afresh: B. A wrongly assigns the CNAME's lifetime to the A record; C reverses which record expired; D disregards TTL expiry altogether.

**Common misconception:** Treating a cached alias chain as one record with one shared expiration time.

## Q65

**Correct answer:** 0.75

**Concept:** Priority recovery and preimage counting.

The recovered index is at least 4 exactly when bit 5 or bit 4 is 1. Of the four patterns of these top bits, three qualify. The lower four bits are arbitrary, so 3×16=48 inputs qualify out of 64. Probability 48/64=0.75. The special all-zero recovery does not qualify.

**Common misconception:** Assuming equally likely input words produce equally likely recovered one-hot states.
