# GATE CS 2027 — Full-Length Mock Test 025

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; other questions carry two marks. Each MCQ has exactly one correct answer; an incorrect MCQ loses one-third of its marks. MSQs require every correct option, without partial credit. MSQs and NATs have no negative marking. Unattempted questions score zero. GA carries15 marks, Engineering Mathematics13 and core CS72. Numerical answers are exact unless precision is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

A writer intends to compare the cost of repairing a machine with the cost of replacing that machine, not with the machine itself. Which sentence makes the comparison explicit and parallel?

A. Repairing the machine costs less than the replacement machine.
B. The cost of repairing the machine is lower than that of replacing it.
C. Repairing costs less than the machine is replaced.
D. The machine is cheaper than repairing it costs less.

### Q2. [1 Mark] [NAT]

A mixture contains milk and water in the ratio3:2 by volume. Ten litres are removed after thorough mixing and replaced by ten litres of pure water. The final ratio is1:1, and total volume is unchanged. What was the initial total volume, in litres?

**Answer format:** Exact number.

### Q3. [1 Mark] [MSQ]

Among employees, every auditor is a reviewer, and no reviewer is an intern. At least one auditor exists. Which statements must follow?

A. At least one reviewer is not an intern.
B. Every non-intern is an auditor.
C. No auditor is an intern.
D. At least one intern exists.

### Q4. [1 Mark] [NAT]

A planar figure consists of the three labelled points A=(0,0), B=(2,0), C=(0,1). It is reflected in the line y=x and then translated by(1,−1). What is the x-coordinate of the image of C minus the y-coordinate of the image of B?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

A transport report says: “The new service is faster for passengers who board at either endpoint. Intermediate-stop passengers may wait longer because fewer vehicles stop there.” Which policy conclusion exceeds what the passage establishes?

A. Benefits can differ by boarding location.
B. Endpoint journey speed alone does not describe every passenger's experience.
C. Every intermediate-stop passenger necessarily has a longer total journey.
D. Reduced stopping frequency may increase some waiting times.

### Q6. [2 Marks] [NAT]

Six distinct books consist of three mathematics books and three literature books. They are arranged on a shelf so that the mathematics books occur in alphabetical order relative to one another, and no two literature books are adjacent. The literature books have no relative-order restriction. How many arrangements are possible?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A firm reports revenue and cost as follows: year1 revenue120, cost90; year2 revenue150, cost120, in the same units. Profit margin is profit divided by revenue. By how many percentage points did the margin decrease from year1 to year2?

**Answer format:** Exact number of percentage points.

### Q8. [2 Marks] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left across x=4 and the top half down across y=4. From the folded stack, remove the triangle with vertices(4,4),(3,4),(4,3), cutting through all layers. After unfolding, a single hole is formed at the centre. What is the square of that hole's perimeter?

**Answer format:** Integer square units.
### Q9. [2 Marks] [MCQ]

A report states: “The valve was closed before the pressure was measured. The pressure measurement preceded replacing the gauge. After the replacement, the valve was reopened.” Which event must lie between valve closure and gauge replacement?

A. Reopening the valve.
B. Measuring the pressure.
C. A second valve closure.
D. No event is forced between them.

### Q10. [2 Marks] [NAT]

A fair six-sided die is rolled twice independently. Given that the larger of the two results is4, what is the probability that their sum is even? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A rooted binary tree has eight leaves and three nodes with exactly one child. Every other non-leaf has exactly two children. How many vertices does the tree have in total?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

A partially ordered set has elements0,a,b,1, with0<a<1 and0<b<1; a and b are incomparable. Which statements are correct?

A. a and b have meet0 and join1.
B. The poset is a total order.
C. The poset is a lattice.
D. There is no upper bound of both a and b.

### Q13. [1 Mark] [NAT]

A factorization PA=LU uses a permutation matrix P that interchanges exactly one pair of rows. L is unit lower triangular, and U has diagonal entries1,2,3. What is det(A)?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

Table T(k,v) has rows(1,10),(1,NULL),(2,NULL). How many rows are returned?

```sql
SELECT k FROM T GROUP BY k HAVING COUNT(v) = 0;
```

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

A link sends packets of1000 payload bits plus a100-bit header at1100 bits per millisecond. Packets are continuously available and there are no other delays or losses. What payload throughput, in bits per millisecond, is achieved?

**Answer format:** Exact number.

### Q16. [1 Mark] [NAT]

Let f be continuous on[0,1], and define F(x)=the integral of f(t) from0 to x. If f(x)=2x and F(0)=0, what is the integral of F(x) from0 to1?

**Answer format:** Decimal rounded to four places.

### Q17. [1 Mark] [MSQ]

The only use of scalar x after this fragment is return x. Variables are ordinary integers and expressions have no side effects.

```text
x = a + b
x = c + d
return x
```

Which statements are correct?

A. The first assignment's computed value is dead.
B. The first assignment can be removed under the stated assumptions.
C. Both assigned values are simultaneously live before return.
D. The second assignment is dead because x was previously assigned.

### Q18. [1 Mark] [NAT]

A control store has256 words. Each word contains eight independent control bits and a binary address field naming any word. No other fields exist. How many bits does the entire control store contain?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A byte-addressed memory uses2048×8-bit chips. Two chips are selected in parallel to provide a16-bit data path, and four such pairs provide successive address ranges. What is the total memory capacity, in bytes?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

An L1 miss is served by L2 with conditional hit probability0.8. An L2 miss causes a main-memory access. If L1's miss probability is0.1, what fraction of all accesses reach main memory?

**Answer format:** Exact decimal.


### Q21. [1 Mark] [MSQ]

Two threads use a mutex to protect a counter. The counter is initialized once before either starts. Each thread locks, reads, increments, writes and unlocks exactly once. Which statements are correct under ordinary correct mutex semantics?

A. The two increment regions cannot overlap.
B. The final value is the initial value plus2.
C. The mutex by itself specifies which thread increments first.
D. Removing the lock but retaining the unlock preserves the synchronization guarantee.

### Q22. [1 Mark] [MSQ]

Over alphabet{a,b}, let R=a*b* and L={a^n b^n:n≥0}. Which statements are correct?

A. L is a subset of R.
B. Every subset of a regular language is regular.
C. R is regular but L is not.
D. The inclusion L⊆R proves that L is finite.

### Q23. [1 Mark] [MCQ]

An array contains n−1 copies of1 and one copy of0 at an unknown position. It is promised to be a rotation of a nondecreasing array. In the worst case, how many array entries must a deterministic algorithm inspect to locate the0, when n−1 unsuccessful inspections allow its position to be inferred?

A. Θ(1)
B. Θ(log n)
C. Θ(n)
D. Θ(n log n)

### Q24. [1 Mark] [MSQ]

A programming language specifies that every evaluation of a volatile memory read is observable, even if the returned values happen to be equal. For two successive expressions x=read_volatile(p) and y=read_volatile(p), which statements are correct?

A. Equal returned values alone justify replacing the second read by y=x.
B. Such replacement removes an observable operation.
C. Ordinary expression-value equality is insufficient for this optimization.
D. Volatile reads are guaranteed never to return equal values.

### Q25. [1 Mark] [NAT]

A BST has root20, left child10, right child30, and node10 has right child15. A right rotation is performed at20. How many nodes are visited by a successful ordinary search for30 after the rotation, including root and target?

**Answer format:** Integer.

### Q26. [1 Mark] [MCQ]

Resource type A has two instances and B one. P holds one A and requests B; Q holds B and requests one A. The other A instance is free. A process releases its resources after receiving its requested resource and finishing. Which statement is correct?

A. The cycle in the resource graph necessarily implies deadlock.
B. Q can receive the free A and finish, allowing P to proceed.
C. No process can receive any resource.
D. P must be aborted for any progress.

### Q27. [1 Mark] [MSQ]

A foreign key has two columns(x,y) and uses the stated rule: if either referencing component is NULL, no referenced-row match is required; otherwise the pair must match. Which inserted pairs can pass the foreign-key check when the referenced table is empty?

A. (NULL,5)
B. (7,NULL)
C. (NULL,NULL)
D. (7,5)

### Q28. [1 Mark] [NAT]

A two-bit synchronous counter uses transitions00→01→10→00 and11→00. What is the maximum number of clock edges needed to enter the repeating three-state cycle from an arbitrary initial state?

**Answer format:** Integer; entering at time0 requires zero edges.

### Q29. [1 Mark] [NAT]

For the unary regular language {a^(3k):k≥0}, what is the smallest positive pumping length satisfying the regular pumping lemma, including |xy|≤p and |y|>0?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

At a scheduling decision, nonpreemptive highest-response-ratio-next uses score(waiting time+service time)/service time. Ready jobs P,Q,R have(waiting,service) pairs(6,3),(8,4),(5,1). Which job is selected?

A. P
B. Q
C. R
D. All have equal score.

### Q31. [1 Mark] [NAT]

A dataset has population mean4 and variance9. Each observation x is replaced by y=10−2x. What is E[Y²], interpreting E as the empirical population average?

**Answer format:** Exact number.

### Q32. [1 Mark] [NAT]

A block contains four data bits followed by one even-parity bit. Exactly one of the five transmitted bits is flipped. How many different one-bit error patterns are undetected by the parity check?

**Answer format:** Integer.

### Q33. [1 Mark] [MSQ]

A directed graph has a DFS forest. Which statements are correct?

A. An edge from a vertex to a currently active ancestor on the recursion stack certifies a directed cycle.
B. Every edge to a previously finished vertex certifies a directed cycle.
C. A DAG has no DFS back edge under the ancestor definition.
D. A graph with one back edge is necessarily strongly connected.

### Q34. [1 Mark] [NAT]

On the real numbers other than−1, define x*y=x+y+xy. This operation forms a group with identity0. What is the inverse of3 under this operation?

**Answer format:** Exact decimal.
### Q35. [1 Mark] [NAT]

An eight-bit two's-complement fixed-point value has three fractional bits and raw bit pattern11110100. What real value does it represent?

**Answer format:** Exact decimal.

### Q36. [2 Marks] [NAT]

A connected undirected graph has six vertices and seven edges. Removing a particular edge e leaves it connected. How many edges must then be removed from the remaining graph to obtain a spanning tree, if removals may be chosen appropriately?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

A total computable function maps every pair(machine M,input w) to a machine N that ignores its own input, simulates M on w and accepts if that simulation accepts. Which statements are correct?

A. If M accepts w, N recognizes all strings.
B. If M does not accept w, N recognizes the empty language.
C. A decider for whether N's language is empty would decide arbitrary machine acceptance.
D. The construction requires deciding whether M accepts w before producing N.

### Q38. [2 Marks] [MSQ]

In a connected undirected weighted graph, an edge e is the unique heaviest edge of a cycle. Which statements are correct?

A. e belongs to every MST.
B. e belongs to no MST.
C. Deleting e leaves the graph connected.
D. The conclusion in B remains valid with “unique heaviest” replaced by merely “one of the heaviest”.

### Q39. [2 Marks] [NAT]

A disk head moves at one cylinder per time unit, initially at0. It begins serving a request at100 nonpreemptively. At time10, a new request at20 arrives. Once the first request completes, it serves the new request directly. At what time does the request at20 complete?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A binary min-heap contains seven distinct keys in a one-based array. How many positions could contain the maximum key, considering all valid heaps of that size?

**Answer format:** Integer.

### Q41. [2 Marks] [MSQ]

A lexer uses longest match among tokens '<','<=','<<','=' and identifiers. Which statements about input x<<=y are correct?

A. After identifier x, the next token is'<<'.
B. The next token after'<<' is'='.
C. The lexer must invent a'<<=' token because three symbols are adjacent.
D. Choosing'<' first would violate longest match among the stated tokens.

### Q42. [2 Marks] [NAT]

For R(A,B,C), dependencies are A→B and B→C. How many of the seven nonempty subsets of{A,B,C} are superkeys?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A directed graph has edges s→a(4),s→b(1),b→a(1),a→t(2),b→t(8). How many edges are in its unique shortest s-to-t path?

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

For a DFA, states p and q are equivalent if every suffix yields the same acceptance result from both. Which statements are correct?

A. If p is accepting and q rejecting, ε distinguishes them.
B. Having the same transitions on one input symbol alone guarantees equivalence.
C. If p,q are equivalent, their successors on any given symbol are equivalent.
D. Two unreachable states must be equivalent to each other.

### Q45. [2 Marks] [NAT]

A sequential file stores250 records of120 bytes in4096-byte blocks with a16-byte header per block. Records do not span blocks. How many data blocks are required?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A simple undirected graph has degree sequence(3,3,2,2,2). How many edge entries are stored in ordinary adjacency lists when each edge is recorded at both endpoints?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

Two stations independently choose one of eight slots uniformly after a collision. If they collide again, they independently choose one of sixteen slots uniformly. What is the probability that both retries collide?

**Answer format:** Exact decimal.

### Q48. [2 Marks] [MSQ]

In a binary floating-point format with round-to-nearest, ties-to-even and finite precision, which statements are correct?

A. Addition is necessarily associative for all finite inputs whose computations stay finite.
B. Adding a sufficiently small positive number to a sufficiently large positive number can leave the stored result unchanged.
C. Cancellation of nearby numbers can reveal error already present in their approximations.
D. Every integer of arbitrary size is represented exactly.

### Q49. [2 Marks] [NAT]

A shift-reduce parser has recognized the right-hand side E+T of production E→E+T. The three grammar symbols occupy three stack entries, and reduction pops all three and pushes one E entry. By how many grammar-symbol entries does the stack size decrease?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

Fixed partitions have sizes8,12,20 KiB. Processes of sizes7,10,18 KiB are assigned to them respectively. What is total internal fragmentation, in KiB?

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

A B+ tree index has all data entries in leaves, and linked leaves support ordered scans. Which statements are correct?

A. Searching once for the lower range bound can be followed by leaf-link traversal for the rest of the range.
B. Every subsequent leaf necessarily requires a fresh root-to-leaf search.
C. Internal separator keys can duplicate key values present in leaves.
D. Leaf links by themselves eliminate the need to locate the first relevant leaf.

### Q52. [2 Marks] [NAT]

For Boolean variables a,b,c, how many assignments make a XOR b XOR c differ from(a OR b OR c)?

**Answer format:** Integer.

### Q53. [2 Marks] [MCQ]

Which expression is guaranteed to stay within the same C array object when a is an array of four integers and p=a+4? Forming a one-past pointer is permitted, but dereferencing it is not.

A. *p
B. *(p−1)
C. *(p+1)
D. a[4]

### Q54. [2 Marks] [NAT]

A fully associative cache with LRU holds three blocks and initially contains A,B,C, with A least recent and C most recent. References are A,D,B. How many misses occur?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

How many length-five binary strings have exactly two1s and begin and end with different bits?

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

A DMA device writes a memory buffer while a CPU has an old cached copy. Assume the cache is not coherent with the device and no synchronization action is taken. Which statements are correct?

A. The CPU can read stale data from its cache after DMA completes.
B. DMA completion alone under these assumptions guarantees the cached copy was updated.
C. A suitable cache-invalidation protocol can be necessary before CPU consumption.
D. Physical memory sharing necessarily implies hardware cache coherence.

### Q57. [2 Marks] [NAT]

A distance-vector router has neighbours A and B with link costs2 and5. Their advertised distances to destination d are7 and3 respectively. No other routes exist. What distance does the router select?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A sequence has a0=1 and an=sum(a_i for i=0,...,n−1) for n≥1. What is a6?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A pipeline has four stages with delays2,5,3,4 ns and a1 ns register overhead per stage boundary included in its clock period. It processes ten independent operations with one operation entering per cycle after start. What is total time from the first entry until the tenth result, counting four cycles for the first result?

**Answer format:** Integer nanoseconds.

### Q60. [2 Marks] [NAT]

Processes P and Q each reference two private pages. The interleaved reference sequence is P1,Q1,P2,Q2,P1,Q1,P2,Q2. Compare three initially empty frames managed by global FIFO with local FIFO allocating two frames exclusively to P and one exclusively to Q. How many more page faults occur under the global allocation?

**Answer format:** Integer.
### Q61. [2 Marks] [MSQ]

A Karnaugh-map group fixes variable a=1 and c=0 while leaving b and d free. Which statements are correct?

A. The group represents product a(NOT c).
B. It covers four minterms.
C. Its product must include b and d because they vary.
D. It can legally include specified zero cells in an exact SOP implementation without don't-cares.

### Q62. [2 Marks] [NAT]

Grammar S→aS | b generates exactly one b at the end. How many leftmost derivation steps produce aaab?

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

Consider ordinary IPv4 fragmentation. Payload means the fragment's bytes after its own IP header. Which statements are correct?

A. A fragment with MF=1 must have a payload length divisible by8.
B. A final fragment may have a payload length that is not divisible by8.
C. The fragment-offset field directly gives a byte count without scaling.
D. A fragment's own IP header bytes are not included when locating its payload using the fragment offset.
### Q64. [2 Marks] [MSQ]

For propositions p,q,r, suppose p implies q and q implies r. Which statements follow?

A. p implies r.
B. NOT r implies NOT p.
C. r implies p.
D. p AND NOT r is unsatisfiable together with the premises.

### Q65. [2 Marks] [NAT]

A comparison-based search probes a sorted array of15 distinct keys by repeatedly choosing the middle of the remaining interval. What is the maximum number of key comparisons for a successful search?

**Answer format:** Integer.


---

## ANSWER KEY — MOCK TEST 025

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 60 |
| 3 | MSQ | 1 | A, C |
| 4 | NAT | 1 | 1 |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 24 |
| 7 | NAT | 2 | 5 |
| 8 | NAT | 2 | 32 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 0.4286 (accepted range 0.42855–0.42865) |
| 11 | NAT | 1 | 18 |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | -6 |
| 14 | NAT | 1 | 1 |
| 15 | NAT | 1 | 1000 |
| 16 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 17 | MSQ | 1 | A, B |
| 18 | NAT | 1 | 4096 |
| 19 | NAT | 1 | 16384 |
| 20 | NAT | 1 | 0.02 |
| 21 | MSQ | 1 | A, B |
| 22 | MSQ | 1 | A, C |
| 23 | MCQ | 1 | C |
| 24 | MSQ | 1 | B, C |
| 25 | NAT | 1 | 3 |
| 26 | MCQ | 1 | B |
| 27 | MSQ | 1 | A, B, C |
| 28 | NAT | 1 | 1 |
| 29 | NAT | 1 | 3 |
| 30 | MCQ | 1 | C |
| 31 | NAT | 1 | 40 |
| 32 | NAT | 1 | 0 |
| 33 | MSQ | 1 | A, C |
| 34 | NAT | 1 | -0.75 |
| 35 | NAT | 1 | -1.5 |
| 36 | NAT | 2 | 1 |
| 37 | MSQ | 2 | A, B, C |
| 38 | MSQ | 2 | B, C |
| 39 | NAT | 2 | 180 |
| 40 | NAT | 2 | 4 |
| 41 | MSQ | 2 | A, B, D |
| 42 | NAT | 2 | 4 |
| 43 | NAT | 2 | 3 |
| 44 | MSQ | 2 | A, C |
| 45 | NAT | 2 | 8 |
| 46 | NAT | 2 | 12 |
| 47 | NAT | 2 | 0.0078125 |
| 48 | MSQ | 2 | B, C |
| 49 | NAT | 2 | 2 |
| 50 | NAT | 2 | 5 |
| 51 | MSQ | 2 | A, C |
| 52 | NAT | 2 | 3 |
| 53 | MCQ | 2 | B |
| 54 | NAT | 2 | 2 |
| 55 | NAT | 2 | 6 |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 8 |
| 58 | NAT | 2 | 32 |
| 59 | NAT | 2 | 78 |
| 60 | NAT | 2 | 2 |
| 61 | MSQ | 2 | A, B |
| 62 | NAT | 2 | 4 |
| 63 | MSQ | 2 | A, B, D |
| 64 | MSQ | 2 | A, B, D |
| 65 | NAT | 2 | 4 |


