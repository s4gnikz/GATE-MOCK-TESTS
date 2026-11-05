# GATE CS 2027 — Full-Length Mock Test 007

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all other questions carry two marks each. An MCQ has exactly one correct option and an MSQ has multiple correct options. Select all correct MSQ options; no partial credit is given. An incorrect MCQ loses one-third of its marks. Incorrect MSQ, NAT, and unattempted questions score zero. NAT precision is specified individually. General Aptitude carries 15 marks, Engineering Mathematics 13 marks, and core Computer Science 72 marks. Assume exact arithmetic in pseudocode unless stated otherwise.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Which sentence unambiguously states that the researchers, rather than the samples, were exhausted when they repeated the experiment?

A. Exhausted, the experiment was repeated on the samples by the researchers.
B. The exhausted researchers repeated the experiment on the samples.
C. The researchers repeated the experiment on the exhausted samples.
D. Repeated by the researchers, the exhausted experiment used the samples.

### Q2. [1 Mark] [NAT]

A's and B's present ages are in ratio 4:3. After eight years their ages will be in ratio 6:5. What is their present age difference in years?

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

Three nonempty groups have mean scores 40,60,80. Their sizes are positive integers but otherwise unspecified. Which statements must hold for the combined mean μ?

A. 40<μ<80.
B. μ=60.
C. μ can equal 60 for some group sizes.
D. μ is always at least 60.

### Q4. [1 Mark] [NAT]

A planar shape consists of the four points (1,0),(0,1),(−1,0),(0,−1), with the first point coloured red and the other three blue. A rotation is a symmetry only if it maps the coloured point set to itself, preserving colours. How many rotations about the origin through angles in [0,360) degrees are symmetries?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

Arrange these events into the only order consistent with their stated dependencies: P: restore a backup after locating the fault; Q: test the restored system; R: locate the fault using diagnostic logs; S: reopen access only after the test succeeds.

A. P,R,Q,S
B. R,P,S,Q
C. R,P,Q,S
D. Q,R,P,S

### Q6. [2 Marks] [NAT]

Five distinct people A,B,C,D,E occupy five seats in a row. C must occupy an end seat, and A and B must not be adjacent. How many seating orders satisfy both requirements?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A product's price is increased by 20%. It is then reduced by a percentage r of the increased price so that the final price is 10% below the original price. Find r.

**Answer format:** Integer percentage.

### Q8. [2 Marks] [NAT]

Two distinct numbers are selected uniformly as an unordered pair from {1,2,3,4,5,6}. Given that their product is even, what is the probability that their sum is even?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MSQ]

A switch is either ON or OFF. A says, “The switch is ON.” B says, “A's statement is false.” C says, “The switch is OFF.” Exactly two of the three statements are true. Which conclusions follow?

A. The switch is OFF.
B. A and B are both truthful.
C. B and C are truthful.
D. The information is inconsistent.

### Q10. [2 Marks] [NAT]

Three distinct integers are chosen uniformly from {1,…,8}. What is the expected value of the smallest chosen integer?

**Answer format:** Exact finite decimal.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

On {1,2,3,4}, a relation initially contains (1,2),(2,1),(2,3),(3,4). How many ordered pairs are in its reflexive transitive closure?

**Answer format:** Integer.

### Q12. [1 Mark] [MCQ]

A sorted array is [1,2,2,2,4,4,7]. A lower-bound search returns the first index whose key is at least x, while an upper-bound search returns the first index whose key is greater than x. Both return 7 if no such index exists, and indexing starts at zero. What pair is returned for x=4?

A. (3,5)
B. (4,5)
C. (4,6)
D. (5,6)

### Q13. [1 Mark] [MSQ]

M is a finite monoid with identity e and satisfies left cancellation: ax=ay implies x=y. Which statements must hold?

A. For each a, the map x↦ax is onto M.
B. Every a has a two-sided inverse.
C. M must be commutative.
D. M is a group.

### Q14. [1 Mark] [NAT]

Find the limit as x tends to zero of (sin x−x)/x³. Angles are in radians. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q15. [1 Mark] [NAT]

A directed acyclic graph on A,B,C,D has edges A→C, B→C, B→D and no others. How many topological orderings does it have?

**Answer format:** Integer.

### Q16. [1 Mark] [MCQ]

Over {a,b}, L consists of strings whose every even-numbered position contains a, numbering positions from one. Odd positions are unrestricted; ε belongs to L. What is the minimum number of states in a complete DFA for L?

A. 2
B. 3
C. 4
D. 5

### Q17. [1 Mark] [NAT]

For Boolean inputs x,y let F(x,y)=xy and define G=F(x,y) XOR F(NOT x,y) XOR F(x,NOT y) XOR F(NOT x,NOT y). On how many of the four input assignments is G=1?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

A virtually indexed, physically tagged cache has 32 KiB data capacity and 64-byte lines. Pages are 4 KiB. To keep every set-index bit within the page offset, what is the minimum power-of-two associativity? Ignore all metadata and use conventional contiguous offset/index fields.

**Answer format:** Integer number of ways.

### Q19. [1 Mark] [MCQ]

SQL table L(id) contains 1,2 and table R(id,v) contains (1,0),(1,5). What rows are returned by the following query, using ordinary SQL bag semantics?

```sql
SELECT L.id, R.v
FROM L LEFT JOIN R ON L.id=R.id AND R.v>0;
```

A. (1,5) only
B. (1,0),(1,5),(2,NULL)
C. (1,5),(2,NULL)
D. (1,NULL),(2,NULL)

### Q20. [1 Mark] [MSQ]

A frame appends one even-parity bit to its data. The receiver checks even parity over the entire received frame. Which corruption patterns are always detected?

A. Exactly one flipped bit anywhere in the frame.
B. Exactly two flipped data bits.
C. Exactly three flipped bits anywhere in the frame.
D. Any nonempty set of flipped bits.

### Q21. [1 Mark] [MCQ]

A scheduler assigns smaller numeric priority to more urgent jobs. Every waiting job's priority decreases by one per time unit, while a running job's priority is unchanged. Which problem is this aging rule principally intended to mitigate?

A. Deadlock caused by inconsistent mutex acquisition order.
B. Starvation of low-priority jobs under repeated arrivals of more urgent work.
C. Internal fragmentation in a page.
D. Loss of a dirty cache line during DMA.

### Q22. [1 Mark] [MSQ]

Let h map both a and b to the single symbol 0 and extend by concatenation. For L={aⁿbⁿ:n≥0}, which statements are correct?

A. h(L)={0²ⁿ:n≥0}.
B. h(L) is regular.
C. Since h(L) is regular, L must be regular.
D. h erases every input symbol.

### Q23. [1 Mark] [NAT]

Independent Poisson variables X,Y have means 2 and 3. Find E[X | X+Y=3].

**Answer format:** Exact finite decimal.

### Q24. [1 Mark] [NAT]

A protocol numbers frames modulo 16. The receiver currently expects 14 and accepts only the next in-order frame, discarding every other arrival. Frames arrive with sequence numbers 15,14,0,15,0,1, in that order. What sequence number does it expect at the end?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

A real upper-triangular 3×3 matrix A has diagonal entries 1,2,3; entries above the diagonal are arbitrary. Find det(A²−A−I), where I is the identity.

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

A 16-bit instruction format uses eight bits for an opcode and four bits for each of two register operands. Exactly 200 opcode patterns are assigned to these two-register instructions. All remaining opcode patterns are used as prefixes for instructions with no operands, with their remaining eight bits extending the opcode. What is the maximum number of distinct no-operand instructions?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A memory access normally takes 200 ns. Independently, a fraction p of accesses incur an additional 10 ms page-fault delay. Ignoring other overhead, what is the greatest p for which mean access time is at most 240 ns?

**Answer format:** Exact finite decimal.

### Q28. [1 Mark] [MSQ]

A binary min-heap stores seven distinct keys in indices 1–7, with children 2i and 2i+1. Which positions can contain the second-smallest key in some valid heap?

A. 2
B. 3
C. 4
D. 7

### Q29. [1 Mark] [MCQ]

A SQL column x has constraint `CHECK (x>0)` but no NOT NULL constraint. Under standard CHECK semantics, which values satisfy the constraint?

A. Positive integers only.
B. Positive integers and NULL.
C. Zero, positive integers, and NULL.
D. Every integer and NULL.

### Q30. [1 Mark] [MCQ]

For grammar A→Aa | Ab | c, which regular expression describes its language?

A. (a|b)*c
B. c(a|b)*
C. a*b*c
D. c(ab)*

### Q31. [1 Mark] [MCQ]

A three-bit reflected Gray code g2g1g0 encodes binary b2b1b0 by g2=b2, g1=b2 XOR b1, g0=b1 XOR b0. The present Gray word is 101. What Gray word encodes the next larger binary integer, without wraparound?

A. 110
B. 111
C. 100
D. 001

### Q32. [1 Mark] [MCQ]

Assume unsigned char has exactly eight bits. What is the behaviour of this C loop?

```c
unsigned char i = 250;
while (i < 255) {
    i = i + 2;
}
```

A. It terminates with i=255.
B. It never terminates.
C. It terminates with i=0.
D. The addition necessarily causes undefined signed overflow.

### Q33. [1 Mark] [MSQ]

In a basic block, p and q are pointers to valid int objects and may alias. Consider `t=*p; *q=7; u=*p;`. There is no concurrency or volatile access. Which statements are correct?

A. Replacing the final load by u=t is valid whenever p and q are proved to point to different objects.
B. The replacement is valid for all possible aliases and initial values.
C. If p=q and the initial pointed-to value is 3, the original block ends with t=3,u=7.
D. A store through q cannot affect a subsequent load through p because the pointer names differ.

### Q34. [1 Mark] [NAT]

Memory has four banks, with word address w mapped to bank w mod 4. A bank stays busy for four cycles after a request starts; its result becomes available exactly four cycles after the start. Only one request may start per cycle. Requests to words 0,4,8,12 are issued in order as early as permitted, beginning at time 0. At what cycle time is the last result available?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

A process opens a file descriptor, sets its close-on-exec flag, and forks. The child successfully execs a new program. The parent does not exec or close the descriptor. Which statement is correct?

A. The descriptor is closed in both processes by the child's exec.
B. It remains open in the parent but is closed in the child during exec.
C. The flag prevents fork from creating a child.
D. The descriptor must remain open in the child because it was inherited.

### Q36. [2 Marks] [MCQ]

For powers of two n≥4, a recurrence is T(n)=3T(n/2)+n²/log₂n, with positive constant base costs for n≤2. What is its asymptotic order?

A. Θ(n²)
B. Θ(n²/log n)
C. Θ(n^(log₂3) log n)
D. Θ(n² log log n)

### Q37. [2 Marks] [MSQ]

The input sequence 1,2,3,4,5 is passed through one stack. Each input may be pushed only in this order; a pop emits the current top. Which output permutations are possible?

A. 3,2,1,5,4
B. 3,1,2,4,5
C. 2,4,3,5,1
D. 4,2,3,1,5

### Q38. [2 Marks] [NAT]

Each reference first spends 1 ns searching a TLB. A TLB miss, occurring on 10% of references, adds a 200 ns page-table walk before the data-cache lookup. Every data-cache lookup takes 2 ns; a data-cache miss, occurring on 5% of references, adds 50 ns. These delays do not overlap, and there are no page faults. What is the mean reference time in ns?

**Answer format:** Exact finite decimal.

### Q39. [2 Marks] [NAT]

Integers a,b,c,d independently range over the full eight-bit two's-complement range. What is the minimum signed two's-complement width sufficient to represent every exact value of ab−cd, without overflow?

**Answer format:** Integer bits.

### Q40. [2 Marks] [MSQ]

Consider the simple complete bipartite graph K2,3. A Hamiltonian path visits every vertex exactly once; an Euler trail uses every edge exactly once. Which statements are correct?

A. It has an Euler trail.
B. It has an Euler circuit.
C. It has a Hamiltonian path.
D. It has no Hamiltonian cycle.

### Q41. [2 Marks] [NAT]

A relation R(A,B,C) uses domains of sizes 3,4,5, respectively, and satisfies AB→C and AC→B. Tuples are distinct. What is the maximum possible number of tuples in R?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

Two processes arrive at time 0. A has CPU burst 2, then I/O lasting 3, then CPU burst 2. B has one CPU burst of 4. The CPU uses nonpreemptive FCFS, choosing A first; I/O overlaps CPU work and has no contention. Switching costs are zero. What is their average total ready-queue waiting time?

**Answer format:** Exact finite decimal time units.

### Q43. [2 Marks] [MCQ]

A wait-die lock policy lets an older requesting transaction wait for a younger holder, but aborts a younger requester when the holder is older. Transactions T1,T2,T3 have timestamps 1,2,3, respectively (smaller is older). T2 holds x and T3 holds y. T1 requests x, then T2 requests y, then T3 requests a different item z held by T1. No locks are released before the last request. Which transaction is aborted by these requests?

A. T1 only
B. T2 only
C. T3 only
D. None

### Q44. [2 Marks] [NAT]

A microinstruction has 16 independent control bits, a field selecting one of eight branch conditions, and two absolute next-address fields for true and false outcomes. The control store holds 256 microinstructions. With fixed-width fields and no shared encoding, how many bits does one microinstruction require?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A uniformly random permutation of {1,2,3,4,5} is chosen. Given that 1 is not fixed, what is the probability that the permutation has exactly one fixed point?

**Answer format:** Exact finite decimal.

### Q46. [2 Marks] [NAT]

Among all monic real quadratics p(x)=x²+ax+b, what is the smallest possible value of max{|p(x)|: −1≤x≤1}?

**Answer format:** Exact finite decimal.

### Q47. [2 Marks] [MCQ]

A singly linked list is 1→2→3→4→5→NULL. Pointers p and q initially refer to nodes 2 and 4. Execute the following assignments in the displayed order, with t a temporary pointer:

```text
t = p.next
p.next = q.next
q.next = t
```

Starting at node 1 afterward, what happens when next links are followed?

A. The traversal is 1,2,5 and then NULL.
B. The traversal is 1,2,3,4,5 and then NULL.
C. The traversal is 1,2,4,3,5 and then NULL.
D. The traversal enters a cycle containing node 1.

### Q48. [2 Marks] [NAT]

A processor can execute one multiplication at a time on a multiplier and one addition at a time on a separate adder. Multiplications take 3 cycles and additions 1 cycle. Operations are nonpreemptive and a dependent operation starts no earlier than its predecessors' completion. Compute independent products P=a*b and Q=c*d, then R=P+e, and finally S=R+Q. All operands a,b,c,d,e are ready at time 0. What is the earliest completion time of S?

**Answer format:** Integer cycles from time 0.

### Q49. [2 Marks] [NAT]

A disk uses C-SCAN on cylinders 0–99, moving upward. Initially the head is at 40 and requests are pending at 10,30,50,90. No new requests arrive. It services upward requests, travels to 99, jumps to 0, and then resumes upward service. Count the jump as head movement; service time is zero. How many cylinders does the head travel before all requests are served?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

A TCP sender learns that the path MTU is 1280 bytes and wishes to send full-sized IPv4 packets without fragmentation. IPv4 and TCP each use a 20-byte header, with no options or other encapsulation. The application has 3000 bytes ready. What is the payload size, in bytes, of the final packet when earlier packets use the maximum permitted payload?

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

A directed weighted graph contains s→a (1), a→b (−2), b→a (1), b→c (4), and s→t (5), with no other edges. Which statements are correct?

A. There is no finite minimum weight among s-to-c walks.
B. The shortest s-to-t path has weight 5.
C. The negative cycle makes every vertex's distance from s equal to minus infinity.
D. c can reach a negative cycle.

### Q52. [2 Marks] [MCQ]

A compiler may reuse the caller's activation record for a tail call when no work remains after the callee returns and no live local address must survive. Which recursive return expression is eligible under exact integers and ordinary call-by-value semantics, assuming the recursive call otherwise meets these conditions?

A. `return 1 + f(n-1);`
B. `return f(n-1) * n;`
C. `return f(n-1, acc*n);`
D. `return g(f(n-1));`

### Q53. [2 Marks] [NAT]

A binary search tree contains ordered keys a<b<c. Successful search probabilities are 0.2,0.5,0.3, respectively, with no unsuccessful searches. Each comparison with a node costs one unit, including the successful comparison. What is the minimum expected search cost over all BST shapes?

**Answer format:** Exact finite decimal.

### Q54. [2 Marks] [NAT]

A paged machine uses 1 KiB pages and two page-table levels. Its six-bit virtual page number splits into a two-bit root index and a four-bit leaf index. For root index 2, the root entry selects a leaf table whose entry 3 maps to physical frame 9. What physical byte address corresponds to virtual byte address (35×1024)+17? All mentioned mappings are valid.

**Answer format:** Integer.

### Q55. [2 Marks] [MCQ]

A receiver expects byte 1000. Segments containing bytes 1100–1199,1200–1299,1300–1399 arrive before the segment containing 1000–1099. It immediately sends a cumulative ACK for each arrival and buffers out-of-order bytes. No bytes are lost. What ACK numbers are sent for these four arrivals in order?

A. 1200,1300,1400,1100
B. 1000,1000,1000,1400
C. 1100,1200,1300,1400
D. 1000,1100,1200,1300

### Q56. [2 Marks] [MSQ]

Let L be context-free and R regular over the same alphabet. Which languages are guaranteed context-free?

A. L∩R
B. L minus R
C. R minus L
D. L∪R

### Q57. [2 Marks] [NAT]

An expression parser uses grammar E→E−E | num. It resolves every shift/reduce conflict on `−` by shifting. What value does it assign to `20−5−3` using exact arithmetic?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A simple undirected graph has 64 vertices and m edges. An adjacency matrix uses one bit per possible ordered vertex pair. An adjacency-list representation uses one 32-bit head pointer per vertex and one 32-bit neighbour entry for each direction of every edge, with no other storage. What is the largest integer m for which the list uses strictly fewer bits than the matrix?

**Answer format:** Integer.

### Q59. [2 Marks] [MCQ]

An ε-NFA has initial state p, final state r, ε-transitions p→q and q→p, and an a-transition q→r. There are no other transitions. Which statement is correct?

A. The language is infinite because there is an ε-cycle.
B. The language is {a}, although there are infinitely many finite accepting runs on a.
C. The empty string is accepted because p and q form a cycle.
D. No string is accepted because the ε-cycle prevents progress.

### Q60. [2 Marks] [NAT]

A four-variable Boolean function, indexed by ABCD with A most significant, is 1 exactly when the Hamming weight of ABCD is 2. There are no don't-cares. What is the minimum number of product terms in a two-level sum-of-products expression for the function? Complemented literals are allowed.

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

Independent coin tosses alternate between two coins: odd-numbered tosses have P(H)=1/2 and even-numbered tosses have P(H)=1/4. Tossing starts at toss 1 and stops immediately when two consecutive heads first occur. What is the expected number of tosses? Round to three decimal places.

**Answer format:** Number to 3 decimal places.

### Q62. [2 Marks] [NAT]

A positive binary floating-point format has two exponent bits and two stored fraction bits. Exponent fields 01 and 10 represent normalized values (1.f)×2^(E−1), where E is the unsigned exponent-field value. Field 00 represents subnormals (0.f)×2⁰; field 11 is reserved. What is the ratio of the largest finite positive value to the smallest positive value?

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

Table T(x) contains 1,2,3. Table U(y) is initially empty. Standard SQL `x > ALL (SELECT y FROM U)` is evaluated for each T row. Which statements are correct?

A. Initially all three T rows pass the predicate.
B. Initially no T row passes because there is nothing to compare.
C. If U is replaced by the single row NULL, no T row passes the WHERE filter.
D. If U is replaced by the single row 2, exactly the row x=3 passes.

### Q64. [2 Marks] [MSQ]

A recognizer for L1 and a recognizer for L2 may loop on nonmembers. Which proposed procedures recognize the stated languages for every such pair of recognizers?

A. For L1∪L2, interleave one step of each recognizer and accept when either accepts.
B. For L1∪L2, run the first recognizer to completion before starting the second, accepting if either accepts.
C. For L1∩L2, run the first until it accepts, then the second until it accepts, and then accept.
D. For the complement of L1, accept if its recognizer has not accepted after one million steps.

### Q65. [2 Marks] [MSQ]

Routers have converged exact shortest distances d(v) to destination t. Each router v≠t selects a next hop u satisfying d(v)=w(v,u)+d(u). All relevant distances are finite. Which statements are correct?

A. If all link costs are strictly positive, the selected next-hop graph cannot contain a directed cycle.
B. If zero-cost links are allowed, independent tie choices can create a forwarding cycle despite correct distances.
C. Correct distances alone prevent forwarding cycles for every set of nonnegative link costs.
D. With positive costs, distance strictly decreases at every selected hop.

## ANSWER KEY — MOCK TEST 007

Integer and exact-decimal NAT values are exact; rounded values have the explicit accepted ranges below.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 4 |
| 3 | MSQ | 1 | A, C |
| 4 | NAT | 1 | 1 |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 24 |
| 7 | NAT | 2 | 25 |
| 8 | NAT | 2 | 0.25 |
| 9 | MSQ | 2 | A, C |
| 10 | NAT | 2 | 2.25 |
| 11 | NAT | 1 | 11 |
| 12 | MCQ | 1 | C |
| 13 | MSQ | 1 | A, B, D |
| 14 | NAT | 1 | -0.1667 (range -0.16675–-0.16665) |
| 15 | NAT | 1 | 5 |
| 16 | MCQ | 1 | B |
| 17 | NAT | 1 | 4 |
| 18 | NAT | 1 | 8 |
| 19 | MCQ | 1 | C |
| 20 | MSQ | 1 | A, C |
| 21 | MCQ | 1 | B |
| 22 | MSQ | 1 | A, B |
| 23 | NAT | 1 | 1.2 |
| 24 | NAT | 1 | 2 |
| 25 | NAT | 1 | -5 |
| 26 | NAT | 1 | 14336 |
| 27 | NAT | 1 | 0.000004 |
| 28 | MSQ | 1 | A, B |
| 29 | MCQ | 1 | B |
| 30 | MCQ | 1 | B |
| 31 | MCQ | 1 | C |
| 32 | MCQ | 1 | B |
| 33 | MSQ | 1 | A, C |
| 34 | NAT | 1 | 16 |
| 35 | MCQ | 1 | B |
| 36 | MCQ | 2 | B |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 25.5 |
| 39 | NAT | 2 | 16 |
| 40 | MSQ | 2 | A, C, D |
| 41 | NAT | 2 | 12 |
| 42 | NAT | 2 | 1.5 |
| 43 | MCQ | 2 | C |
| 44 | NAT | 2 | 35 |
| 45 | NAT | 2 | 0.375 |
| 46 | NAT | 2 | 0.5 |
| 47 | MCQ | 2 | A |
| 48 | NAT | 2 | 7 |
| 49 | NAT | 2 | 188 |
| 50 | NAT | 2 | 520 |
| 51 | MSQ | 2 | A, B |
| 52 | MCQ | 2 | C |
| 53 | NAT | 2 | 1.5 |
| 54 | NAT | 2 | 9233 |
| 55 | MCQ | 2 | B |
| 56 | MSQ | 2 | A, B, D |
| 57 | NAT | 2 | 18 |
| 58 | NAT | 2 | 31 |
| 59 | MCQ | 2 | B |
| 60 | NAT | 2 | 6 |
| 61 | NAT | 2 | 11.273 (range 11.2725–11.2735) |
| 62 | NAT | 2 | 14 |
| 63 | MSQ | 2 | A, C, D |
| 64 | MSQ | 2 | A, C |
| 65 | MSQ | 2 | A, B, D |

