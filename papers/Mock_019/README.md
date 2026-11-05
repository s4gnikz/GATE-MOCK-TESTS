# GATE CS 2027 — Full-Length Mock Test 019

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the others carry two. MCQs have exactly one correct option and lose one-third of their marks for an incorrect answer. MSQs require all correct options, without partial credit or negative marking. NATs have no negative marking. Unattempted questions score zero. General Aptitude carries 15 marks, mathematics 13 and core CS 72. Numerical answers are exact unless rounding is explicitly requested.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

A report states: “The survey's volunteers reported shorter commutes than the city average. Because participation was voluntary, the survey alone cannot establish that the same pattern holds among all residents.” Which conclusion best respects this qualification?

A. Every resident has a shorter-than-average commute.
B. Voluntary participation guarantees a representative sample.
C. The volunteers' result is an observation whose generalization requires further evidence.
D. Every volunteer's response must be false.

### Q2. [1 Mark] [NAT]

How many four-digit positive integers use each of the digits 0,1,2,3 exactly once and are divisible by four? A leading zero is not permitted.

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

Twenty-five observations fall in intervals [0,10), [10,20), [20,30), [30,40), with respective frequencies 4,6,10,5. Which interval necessarily contains the median?

A. [0,10)
B. [10,20)
C. [20,30)
D. [30,40)

### Q4. [1 Mark] [NAT]

A paper strip has coordinate 0≤x≤8. Fold its part x>5 leftwards across x=5. Then fold every layer lying at x<3 rightwards across x=3. Punch through all layers at the resulting position x=4 and fully unfold. What is the mean of the original x-coordinates of all distinct punctures?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

Four events are A, data collection; B, instrument calibration; C, result certification; D, publication. The only constraints are A before C, B before C and C before D. Which lists exactly the possible chronological orders?

A. ABCD only
B. ABCD and BACD
C. ACBD and BCAD
D. All 24 permutations

### Q6. [2 Marks] [NAT]

Two people independently choose a uniformly random three-element subset of {1,2,3,4,5}. Given that their chosen subsets are not identical, what is the probability that their union contains all five elements? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q7. [2 Marks] [MCQ]

“The disinterested adjudicator sanctioned the revised procedure, while remaining critical of its cost.” In this sentence, disinterested means impartial and sanctioned means approved. Which paraphrase preserves both meanings and the final qualification?

A. The bored adjudicator punished the revision because of its cost.
B. The impartial adjudicator rejected the procedure and praised its cost.
C. The adjudicator approved the procedure only after losing interest in all its consequences.
D. The impartial adjudicator approved the procedure but still criticized its cost.

### Q8. [2 Marks] [NAT]

Machine A produces four units on day one and doubles its daily output each following day. Machine B produces one unit on day one and triples its daily output each following day. What is the first positive integer n for which B's cumulative output over days 1 through n exceeds A's cumulative output over those days?

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

A three-letter code is formed by reversing the word, then advancing the first letter by one, the second by two and the third by three positions in the cyclic English alphabet. The same procedure is applied twice to CAT. What is the final code?

A. UCE
B. ECV
C. FEX
D. DBU

### Q10. [2 Marks] [NAT]

A 3×3×3 cube of unit cubes is painted on all six outer faces. All eight corner unit cubes are then removed. Of the exposed unit-square faces of the remaining solid, what fraction are painted? Include newly exposed faces and round to four decimal places.

**Answer format:** Number to 4 decimal places.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Two blocking message queues A and B each have capacity one and are initially empty. Process P sends two messages to A before receiving from B. Process Q sends two messages to B before receiving from A. Both processes are eventually scheduled, and neither removes messages in any other way. What happens?

A. Both processes necessarily complete because the queues start empty.
B. Only P can block; Q cannot.
C. Both eventually block on their second send, with neither able to reach its receive.
D. Sending to a full queue automatically deletes the older message.

### Q12. [1 Mark] [NAT]

A cache miss fetches eight consecutive words. The memory returns the first requested word after 12 cycles and each subsequent word one cycle later. The CPU needs word offset 6 of the line. Compare a fill starting at offset 0 and proceeding in increasing order with critical-word-first delivery starting at offset 6. The CPU resumes as soon as its requested word arrives. How many cycles earlier can it resume with critical-word-first delivery?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A ticket lock stores next-ticket and currently-served ticket numbers modulo eight. Every new contender obtains the next ticket and advances that counter atomically, then enters when its ticket equals the currently-served value. The owner has not yet released the lock and no previously issued ticket has completed. What is the smallest total number of outstanding contenders, including the current owner, that can give another contender the owner's ticket through counter wraparound?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

An integer array initially contains [1,2,3,4,5,6]. A memmove-style operation copies its first four elements into positions 2 through 5, using zero-based positions and preserving the original source values even where source and destination overlap. What value is at position 5 afterward?

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

Four routers S,A,B,C have undirected links SA,SB,AC,BC,AB. S originates one new link-state advertisement and sends it on every incident link. Each other router, on its first receipt, forwards one copy on every incident link except the one on which that first copy arrived; later duplicates are discarded without forwarding. Links are reliable, and acknowledgement traffic is ignored. How many advertisement transmissions occur in total, counting each direction separately?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A three-variable Boolean function has ON minterms 1,3,5, with variable order abc and a most significant. All other minterms are OFF except minterm 7, which may first be treated as a don't-care. What is the increase in minimum SOP literal count when minterm 7 is instead required to be OFF? Count repeated literal occurrences separately.

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

A prime-implicant chart has columns 1,2,3 and rows P covering {1,2}, Q covering {2,3}, R covering {1,3}. All columns must be covered. Which statements are true?

A. P is essential because it covers two columns.
B. No prime implicant is essential.
C. Two rows suffice to cover all columns.
D. The absence of an essential prime implicant means no cover exists.

### Q18. [1 Mark] [MSQ]

A dynamic array starts with capacity one. Appending to a full array allocates a new array of twice the capacity and copies all existing elements; other appends take constant time. Which statements hold over n appends starting empty?

A. The total copying work is O(n).
B. The total copying work is necessarily Θ(n log n).
C. A single append can take Θ(n) time when the current number of elements is proportional to n.
D. Every individual append has worst-case constant time.

### Q19. [1 Mark] [NAT]

Weighted intervals are [0,4) with weight 9, [0,2) with weight 4 and [2,4) with weight 4. Nonoverlapping intervals may share an endpoint. An algorithm repeatedly selects the available interval with earliest finish time, then removes conflicting intervals. By how much is its total weight below the optimum?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

A nondeterministic PDA accepts by final state only after consuming the entire input. In a conversion to empty-stack acceptance, a fresh protected bottom marker is placed below the original stack, and from an original final state the machine may enter a new mode that uses only epsilon transitions to pop all remaining stack symbols, including that marker. Empty-stack acceptance also requires all input consumed. Which statements are correct?

A. The drain mode can successfully finish an accepting computation after the entire input has been consumed in an original final state.
B. Entering drain mode with unread input automatically accepts that input as well.
C. The new bottom marker must be treated as an ordinary original-stack symbol by every old transition, without restriction.
D. The requirement to consume all input prevents a drained stack reached too early from accepting a remaining suffix.

### Q21. [1 Mark] [NAT]

R(A,B)={(1,a),(1,b),(2,a),(3,a),(3,b),(3,c)}. Count A values satisfying: there exist distinct y,z with R(A,y) and R(A,z), and for every w, R(A,w) implies w=y or w=z.

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

Evaluate the real limit as x→0 of `(sqrt(1+x)−sqrt(1−x))/x`.

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

SQL table T(g,x) has rows (A,NULL),(A,NULL),(B,1),(B,NULL),(C,1),(C,1). How many groups are returned by this query under standard SQL NULL semantics?

```sql
SELECT g FROM T
GROUP BY g
HAVING COUNT(DISTINCT x)=1 AND COUNT(*)>COUNT(x);
```

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

An IPv4 receiver has received two fragments of one datagram. The first has offset 0, payload length 80 bytes and MF=1. The other has offset 12 (in the standard eight-byte units), payload length 24 bytes and MF=0. No other fragments have arrived. How many payload bytes are missing between the received regions?

**Answer format:** Integer.

### Q25. [1 Mark] [MSQ]

In a production S→XY, the inherited attribute X.i is defined to equal the synthesized attribute Y.v. Y.v depends only on the tokens in Y's subtree and on no attributes of X. Which statements are correct?

A. This rule violates the usual L-attributed restriction for an inherited attribute of X.
B. This dependency necessarily creates a cycle in the attribute graph.
C. A suitable evaluation order can compute Y.v before assigning X.i.
D. The grammar must be syntactically ambiguous because this attribute rule exists.

### Q26. [1 Mark] [NAT]

A continuous random variable X has density f(x)=c x(1−x) for 0<x<1 and zero elsewhere, with c chosen to normalize the density. Find E[X²].

**Answer format:** Exact finite decimal.

### Q27. [1 Mark] [NAT]

A permutation f of {1,2,3,4,5} maps 1→2, 2→3, 3→1, 4→5 and 5→4. How many fixed points does the composition f^2026 have, where the exponent denotes repeated composition?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A cache contains exactly one four-word line, initially invalid. It uses write-back and write-allocate. A word-store miss fetches the entire target line before updating the word; evicting a dirty line writes the entire line to memory. The accesses are store to block 0, store to block 1, load from block 0. Each access is to one word, blocks 0 and 1 differ, and there is no final cache flush. How many complete cache-line transfers between memory and cache occur, counting reads and write-backs?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A real matrix has rows (0,−2),(1,3). Find the trace of its inverse.

**Answer format:** Exact finite decimal.

### Q30. [1 Mark] [NAT]

Two disjoint circular singly linked lists have nodes labelled 1,2 and 3,4 respectively, with links 1→2→1 and 3→4→3. Swap the next pointers stored in nodes 1 and 3, leaving all other pointers unchanged. Starting from node 1, which node label is reached after exactly two next-pointer traversals?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

Let h be a homomorphism from binary words to words over {a,b}, defined by h(0)=ab and h(1)=aabb. How many binary words w satisfy h(w)∈a*b*? Include the empty word when applicable.

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

Procedure P makes a call as its final action, passing the address of a local variable x to callee Q. Q dereferences that address during the call. Which statements about optimizing this call are correct?

A. P's frame may always be discarded and overwritten before Q reads x, solely because the call is in tail position.
B. Any transformation must preserve the addressed object's value and valid storage for Q's use.
C. Q cannot observe x because callees never receive pointers to caller variables.
D. Tail position alone is insufficient to justify overwriting all storage in P's frame.

### Q33. [1 Mark] [MCQ]

A differentiable function on [0,3] has f(0)=1 and satisfies 2≤f′(x)≤5 throughout (0,3). Which value of f(3) is possible?

A. 6
B. 10
C. 17
D. 20

### Q34. [1 Mark] [NAT]

A four-input priority encoder gives highest priority to D3, then D2, D1,D0, and outputs the two-bit index of the highest asserted input. Its validity output is one whenever any input is one. How many four-bit input patterns produce code 10 with validity one?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

For L={ε,a³}∪{aⁿ:n≥5}, find the smallest positive regular pumping length p. The requirement is: every w∈L with |w|≥p has a decomposition w=xyz with |xy|≤p, |y|>0, and xyⁱz∈L for every integer i≥0.

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

A SQL table has nullable columns a,b, CHECK(a+b>0), UNIQUE(a,b), and a composite foreign key (a,b) with MATCH SIMPLE semantics. For this question, UNIQUE treats tuples containing NULL as distinct, CHECK rejects only FALSE, and MATCH SIMPLE skips the referenced-row check if any referencing column is NULL. The referenced table is empty. Which statements are true?

A. Inserting (NULL,−5) can satisfy all these constraints.
B. CHECK(a+b>0) alone forces both columns to be non-null.
C. Two copies of (NULL,−5) can coexist under the specified UNIQUE semantics.
D. Inserting (1,1) satisfies the foreign key despite the empty referenced table.

### Q37. [2 Marks] [NAT]

A fair coin selects whether a second experiment uses two or three independent tosses of another fair coin. You are told only that the second experiment contained at least one head. What is the conditional probability that it used three tosses? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q38. [2 Marks] [MSQ]

Relation R(A,B,C) contains exactly (1,x,p),(1,y,q),(2,x,p),(2,y,r). Which functional dependencies hold on this relation instance?

A. A→C
B. AB→C
C. C→A
D. C→B

### Q39. [2 Marks] [NAT]

Five jobs in fixed order have (cost,value) pairs (4,9),(2,7),(3,8),(3,10),(2,6). Select exactly two jobs, with no two adjacent in the order, and total cost at most seven. What is the maximum total value?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A binary-input transducer outputs, after reading each input bit, that bit XOR the preceding input bit; before the first input the preceding bit is defined to be zero. Implement it as a deterministic Moore machine whose output after each input is determined by its reached state. The initial state's output before any input is ignored. What is the minimum number of states?

**Answer format:** Integer.

### Q41. [2 Marks] [MCQ]

An interrupt source sets a single pending bit on each event; setting an already-set bit has no extra effect. Interrupts are masked until time 5. Events occur at times 1,2,3,6. On entering a handler the bit is cleared; each handler lasts two time units, and events during it can set the bit again. A pending interrupt is handled immediately when unmasked and no handler is running. Which pair gives the number of handler invocations and the final handler's completion time?

A. (4,13)
B. (2,9)
C. (1,7)
D. (3,11)

### Q42. [2 Marks] [MSQ]

Suppose a hypothetical oracle correctly answers whether any supplied ordinary Turing machine halts on any supplied input. Fix an ordinary recognizer M of a language L. Which tasks become possible using this oracle?

A. Decide whether any given word belongs to L by first querying whether M halts and, when it does, simulating its outcome.
B. Conclude that M must already halt on every word without querying the oracle.
C. Enumerate the complement of L by testing words one by one with the resulting oracle-assisted decision procedure.
D. Replace all oracle calls by one universal fixed finite simulation-time bound for ordinary machines.

### Q43. [2 Marks] [NAT]

Partition this three-address code into maximal basic blocks using the usual leader rules. Count distinct directed edges between the resulting blocks, including both outcomes of conditional branches. There are no exceptional-control-flow edges.

```text
1: i = 0
2: if i >= n goto 9
3: if a[i] < 0 goto 7
4: s = s + a[i]
5: i = i + 1
6: goto 2
7: i = i + 2
8: goto 2
9: return s
```

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

An NFA has states p,q,r, initial state p and sole accepting state r. Its transitions are δ(p,0)={p,q}, δ(p,1)={p}, δ(q,0)=δ(q,1)={r}, and δ(r,0)=δ(r,1)=∅. There are no epsilon transitions. Which statements are true?

A. After reading 010, the reachable-state set is {p,q}.
B. The NFA accepts 010 because some earlier prefix reached r.
C. Subset construction has exactly four reachable subsets.
D. The recognized language consists of binary words whose second-last symbol is zero.

### Q45. [2 Marks] [MSQ]

A stack stores data and a separate stack of minima. On push(x), it pushes x on the minima stack only when that stack is empty or x is strictly smaller than its top. On pop, it removes the minima top whenever the popped data value equals it. Which statements are correct?

A. The sequence push(3),push(1),push(1),pop makes the reported minimum incorrect.
B. The algorithm is correct for arbitrary duplicate values without modification.
C. Pushing onto the minima stack also when x equals its top repairs this duplicate-minimum problem.
D. Removing the equality check from pop, so that the minima stack is never popped, repairs all cases.

### Q46. [2 Marks] [MSQ]

A forwarding table routes 10.2.0.0/25 and 10.2.0.128/25 to next hop H, and 10.2.0.64/26 to next hop J. A default route goes to K. Replace the two /25 entries by 10.2.0.0/24→H while retaining the /26 exception and default. Under longest-prefix matching, which statements are true?

A. Every destination keeps the same next hop.
B. The /24 aggregate overrides the /26 exception because it was inserted later.
C. Destinations outside 10.2.0.0/24 continue using the default route.
D. Removing the /26 exception as well would preserve every destination's next hop.

### Q47. [2 Marks] [MCQ]

A binary tree is height-balanced if the heights of the two child subtrees at every node differ by at most one. An empty subtree has height −1 and a leaf height zero. Among such trees of height five, choose one with the minimum possible number of nodes. Which pair gives its number of nodes and its number of leaves?

A. (31,16)
B. (20,8)
C. (12,5)
D. (20,10)

### Q48. [2 Marks] [NAT]

In grammar S→ABA, A→a | ε, B→b | ε, eliminate epsilon productions while preserving ε in the language by allowing S→ε. Obtain S alternatives by deleting any subset of nullable occurrences from ABA, retain distinct resulting right-hand sides only, and retain S→ε once. How many distinct productions have left-hand side S after this step?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

Six independent multiplication operations feed six additions into a running accumulator, in multiplication order. A multiply takes three cycles; an add takes one cycle, and an add may begin when its multiply and the previous accumulator add have finished. Different functional units overlap. Multiplications start as early as the multiplier permits, beginning at time zero. Compare a pipelined multiplier accepting a new operation every cycle with an unpipelined multiplier accepting one every three cycles. How many cycles earlier does the sixth addition finish in the pipelined design?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

An eight-bit signed two's-complement fixed-point word has four fractional bits and represents −1.375. Convert it to a format with two fractional bits by an arithmetic right shift of its signed raw integer by two positions, defined to round toward negative infinity. Compare the represented result with conversion obtained by dividing the raw integer by four and truncating toward zero. What is the absolute difference of the two represented real values?

**Answer format:** Exact finite decimal.

### Q51. [2 Marks] [MSQ]

For resource types A,B, three processes have allocations P:(0,1), Q:(1,0), R:(1,1) and remaining maximum needs P:(1,0), Q:(0,2), R:(1,1). Available resources are initially (0,0). Apply the standard safety test: a process whose remaining need is available may finish and release its allocation. Which statements are true?

A. The initial state is unsafe.
B. Adding one available unit of B makes the state safe.
C. Adding one available unit of A makes the state safe.
D. An unsafe maximum-claim state alone proves that the processes are already deadlocked on actual requests.

### Q52. [2 Marks] [NAT]

Integers x range over all four-bit signed values −8 through 7. Evaluate `y=(2*x)/2` by first multiplying with four-bit two's-complement wraparound, then dividing the resulting signed value by two using exact division on even integers. For how many x values is y=x?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

A comparison tournament finds the largest of seven distinct keys using six comparisons. The eventual winner received one initial bye and participated in exactly two comparisons. Using only the recorded results plus further key comparisons, what is the minimum total number of comparisons, including the original six, sufficient to identify both the largest and second-largest keys in the worst case under this condition?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A poset consists of pairs (i,j), where i∈{1,2} and j∈{1,2,3}, with (i,j)≤(k,l) iff i≤k and j≤l. How many downward-closed subsets does it have, including the empty set? A subset is downward-closed when containing an element implies containing every smaller element.

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

Five CPU-bound processes are permanently ready in round-robin order. A quantum lasts q positive integer milliseconds, and each intervening context switch costs one millisecond. At time zero the first process starts without an initial switch. Require useful CPU time to be at least 80% of steady-state elapsed time, and require the fifth process to begin its first quantum no later than time 20. What value of q satisfies both requirements?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

A machine's ADD (R)+,(R)+ instruction first reads the source word at address R and increments R by four, then reads the destination word at the new R and increments R by four again, finally writing the sum to that destination's captured address. Initially R=100, M[100]=3 and M[104]=5. Which pair gives the final R and M[104]?

A. (104,6)
B. (108,6)
C. (108,8)
D. (104,8)

### Q57. [2 Marks] [NAT]

A slotted page has 4096 bytes, a fixed 32-byte header and twelve existing four-byte slot entries. Existing records occupy 3900 bytes in total. Compaction may collect all free bytes, but existing records and slots remain. Inserting one new record needs one new four-byte slot entry. What is the largest new record size in bytes that can fit after compaction?

**Answer format:** Integer.

### Q58. [2 Marks] [MSQ]

Exact integer variable x starts at zero. A loop executes `x=1-x` an arbitrary finite number of times, possibly zero. After the loop, y=x*(x−1) is evaluated. Which statements are true?

A. x is necessarily zero after the loop.
B. x is always either zero or one after the loop.
C. y is always zero and may be replaced by that constant.
D. y can equal one if the iteration count is odd.

### Q59. [2 Marks] [NAT]

For solving Ax=b, a factorization PA=LU is supplied. P swaps the first two rows, b=(1,2,3)ᵀ, L has rows (1,0,0),(2,1,0),(−1,3,1), and U has rows (2,1,−1),(0,3,2),(0,0,4). Find the third component of x.

**Answer format:** Exact finite decimal.

### Q60. [2 Marks] [MSQ]

An undirected multigraph has vertices u,v and two distinct parallel edges between them. A cycle of length two using the two distinct edges is considered a cycle. DFS tracks the edge used to enter each vertex. Which statements are true?

A. The graph contains a cycle under the stated convention.
B. Ignoring every edge to the parent vertex is always a correct cycle-detection rule for multigraphs.
C. Ignoring only the entering edge, rather than every edge to its parent endpoint, permits detection of the other parallel edge.
D. The second edge cannot affect cycle existence because it has the same endpoints.

### Q61. [2 Marks] [MSQ]

A disk uses SSTF. Its head starts at track 0 with requests pending at tracks 1 and 100. Each time it services track 1 a fresh request for track 0 arrives immediately, and each time it services track 0 a fresh request for track 1 arrives immediately. No other requests arrive; service takes zero time and movement is positive time. Which statements are true?

A. The track-100 request can remain unserved forever under this arrival pattern.
B. SSTF guarantees a finite waiting bound solely because it selects the nearest request.
C. A fixed finite request set with no new arrivals can reproduce this infinite starvation while each service removes one request.
D. The continued supply of nearby requests is essential to this particular starvation construction.

### Q62. [2 Marks] [NAT]

A BST stores keys 1–15 in a perfectly balanced shape: root 8, recursively choosing the midpoint as each subtree root. Run this range-search procedure with lo=6, hi=10. Count non-null calls, including calls on nodes whose keys are not reported.

```text
search(node):
    if node is null: return
    if node.key > lo: search(node.left)
    if lo <= node.key <= hi: report(node.key)
    if node.key < hi: search(node.right)
```

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

An eight-bit binary floating-point encoding has one sign bit, a three-bit biased exponent and four fraction bits, with the usual sign-and-magnitude ordering of finite magnitudes. Consider only finite, nonzero represented values. Let raw be the unsigned eight-bit encoding. Define T(raw) as the eight-bit bitwise complement of raw for negative values, and raw XOR 0x80 for positive values. Which statements are true?

A. Sorting raw as unsigned integers gives increasing numerical order across both signs.
B. Within positive values, unsigned raw order agrees with numerical order.
C. Within negative values, larger unsigned raw always represents a numerically larger value.
D. Sorting T(raw) as unsigned integers gives increasing numerical order across both signs.

### Q64. [2 Marks] [MCQ]

Six simultaneous UDP flows use six distinct internal source IP/port pairs; three connect to remote endpoint X and three to a different endpoint Y. Each public IPv4 address provides four usable external ports. Under policy I, each internal source pair needs its own external port independent of remote endpoint. Under policy II, an external port may be reused for X and Y, and reverse lookup includes that remote endpoint. What are the minimum public-address counts under policies I and II respectively?

A. (1,1)
B. (2,1)
C. (2,2)
D. (3,2)

### Q65. [2 Marks] [NAT]

Evaluate ∫₀¹ max(x²,1−x) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.


## ANSWER KEY — MOCK TEST 019

NAT answers are exact except for the specified rounded ranges.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 4 |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 5 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 0.3333 (range 0.33325–0.33335) |
| 7 | MCQ | 2 | D |
| 8 | NAT | 2 | 6 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 0.5556 (range 0.55555–0.55565) |
| 11 | MCQ | 1 | C |
| 12 | NAT | 1 | 6 |
| 13 | NAT | 1 | 9 |
| 14 | NAT | 1 | 4 |
| 15 | NAT | 1 | 7 |
| 16 | NAT | 1 | 3 |
| 17 | MSQ | 1 | B, C |
| 18 | MSQ | 1 | A, C |
| 19 | NAT | 1 | 1 |
| 20 | MSQ | 1 | A, D |
| 21 | NAT | 1 | 1 |
| 22 | NAT | 1 | 1 |
| 23 | NAT | 1 | 1 |
| 24 | NAT | 1 | 16 |
| 25 | MSQ | 1 | A, C |
| 26 | NAT | 1 | 0.3 |
| 27 | NAT | 1 | 2 |
| 28 | NAT | 1 | 5 |
| 29 | NAT | 1 | 1.5 |
| 30 | NAT | 1 | 3 |
| 31 | NAT | 1 | 3 |
| 32 | MSQ | 1 | B, D |
| 33 | MCQ | 1 | B |
| 34 | NAT | 1 | 4 |
| 35 | NAT | 1 | 3 |
| 36 | MSQ | 2 | A, C |
| 37 | NAT | 2 | 0.5385 (range 0.53845–0.53855) |
| 38 | MSQ | 2 | B, D |
| 39 | NAT | 2 | 19 |
| 40 | NAT | 2 | 4 |
| 41 | MCQ | 2 | B |
| 42 | MSQ | 2 | A, C |
| 43 | NAT | 2 | 7 |
| 44 | MSQ | 2 | A, C, D |
| 45 | MSQ | 2 | A, C |
| 46 | MSQ | 2 | A, C |
| 47 | MCQ | 2 | B |
| 48 | NAT | 2 | 7 |
| 49 | NAT | 2 | 10 |
| 50 | NAT | 2 | 0.25 |
| 51 | MSQ | 2 | A, C |
| 52 | NAT | 2 | 8 |
| 53 | NAT | 2 | 7 |
| 54 | NAT | 2 | 10 |
| 55 | NAT | 2 | 4 |
| 56 | MCQ | 2 | C |
| 57 | NAT | 2 | 112 |
| 58 | MSQ | 2 | B, C |
| 59 | NAT | 2 | 3.5 |
| 60 | MSQ | 2 | A, C |
| 61 | MSQ | 2 | A, D |
| 62 | NAT | 2 | 7 |
| 63 | MSQ | 2 | B, D |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 0.6817 (range 0.68165–0.68175) |
