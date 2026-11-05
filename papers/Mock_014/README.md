# GATE CS 2027 — Full-Length Mock Test 014

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the remaining questions carry two marks each. MCQs have exactly one correct option. MSQs have multiple correct options and award no partial credit. An incorrect MCQ loses one-third of its marks; incorrect MSQ/NAT answers and unattempted questions score zero. General Aptitude, Engineering Mathematics and core CS carry 15,13,72 marks respectively. Follow the stated numerical precision. Unless otherwise specified, calculations are exact and diagrams are replaced by complete structural descriptions.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Every certified sample was tested. Some tested samples were rejected. Which conclusion must follow?

A. Some certified samples were rejected.
B. Every tested sample was certified.
C. No untested sample was certified.
D. Every rejected sample was certified.

### Q2. [1 Mark] [MCQ]

A planar figure is reflected across the x-axis and then across the line y=x. Which coordinate rule describes the combined transformation?

A. (x,y)→(−y,x)
B. (x,y)→(y,−x)
C. (x,y)→(−x,−y)
D. (x,y)→(x,−y)

### Q3. [1 Mark] [MCQ]

“A train service reduced the average delay but increased the maximum delay.” Which statement follows from these two statistics alone?

A. Every passenger experienced a shorter delay.
B. At least one statistic improved while the worst observed delay became larger.
C. The statistics are mathematically inconsistent.
D. The median delay necessarily increased.

### Q4. [1 Mark] [NAT]

Five distinct books are arranged on a shelf. Two specified books must have exactly one book between them. How many arrangements satisfy this condition?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A store's revenue is 120 units on each of two days, but it sells 30 items on day one and 20 on day two. What is the average revenue per item across both days?

**Answer format:** Exact finite decimal.

### Q6. [2 Marks] [NAT]

A square sheet is folded along both its horizontal and vertical midlines into four layers. A single triangular notch is cut at the folded corner that corresponds to the centre of the original sheet, with equal cuts along the two fold edges. After complete unfolding, how many sides does the resulting central hole have? The cuts are straight and do not reach any outer boundary.

**Answer format:** Integer.

### Q7. [2 Marks] [MCQ]

Arrange the following troubleshooting steps coherently: P, verify that the replacement resolves the fault; Q, isolate the faulty component using measurements; R, replace the isolated component; S, observe and record the original symptom.

A. S–Q–R–P
B. Q–P–S–R
C. R–S–P–Q
D. P–Q–R–S

### Q8. [2 Marks] [NAT]

A bag contains four distinct red balls and two distinct blue balls. Three balls are selected uniformly without replacement. Given that the selection contains at least one blue ball, what is the probability that it contains exactly one blue ball?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MCQ]

“The report is concise but not cursory: it omits repetition while addressing every required issue.” What distinction is emphasized?

A. Brevity need not imply superficial treatment.
B. Concise reports necessarily omit required issues.
C. Cursory reports must be longer than complete reports.
D. Repetition is necessary for completeness.

### Q10. [2 Marks] [NAT]

Two positive numbers have product 64 and satisfy log₂x−log₂y=2. Find x+y.

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A segmented address has segment number 2 and offset 120. Segment 2 has base 4000 and limit 100, where valid offsets are 0 through limit−1. What is the correct outcome of translation?

A. Physical address 4120.
B. Physical address 4100.
C. An address-bound violation.
D. Physical address 120.

### Q12. [1 Mark] [NAT]

Grammar S→aSbb | ε generates a word with 12 terminal symbols. How many a symbols does that word contain?

**Answer format:** Integer.

### Q13. [1 Mark] [MCQ]

A client asks DNS for an AAAA record. Which result type is being requested?

A. An IPv6 address associated with the name.
B. An Ethernet hardware address.
C. A TCP acknowledgment number.
D. The text of an HTTP response body.

### Q14. [1 Mark] [MSQ]

A network-layer service can deliver datagrams out of order and may lose them. Which responsibilities can a reliable transport protocol implement above it?

A. Detect missing data and retransmit it.
B. Reassemble a delivered byte stream in order.
C. Guarantee that no physical link ever experiences a bit error.
D. Eliminate the need to distinguish simultaneous application endpoints.

### Q15. [1 Mark] [NAT]

Let A=uvᵀ, where u=(1,2,−1)ᵀ and v=(2,0,3)ᵀ. What is the sum of the squares of A's three eigenvalues, counted with algebraic multiplicity?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A control store contains 512 microinstructions, each 40 bits wide. How many bits are needed to address a microinstruction within that store?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

A compiler lowers `if (p) x=a; else x=b; use(x);` to a control-flow graph. What must both branch arms do before the common use(x) block?

A. Define x along their respective paths.
B. Execute both assignments unconditionally in source order.
C. Eliminate the branch condition regardless of its value.
D. Assign the same constant to x in every case.

### Q18. [1 Mark] [NAT]

A three-to-eight decoder has active-high one-hot outputs D0 through D7. Input bits are 101₂. What integer index identifies its asserted output?

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

A doubly linked list has adjacent non-sentinel nodes P,X,N. Removing X while preserving the list requires which neighbour updates?

A. P.next=N and N.prev=P.
B. P.prev=N and N.next=P.
C. P.next=X and N.prev=X.
D. P.next=P and N.prev=N.

### Q20. [1 Mark] [NAT]

An edit-distance algorithm allows insertion, deletion and substitution, each of cost one. What is the minimum edit distance from `cat` to `cut`?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A 32-bit-wide memory module is constructed from chips each organized as 1024 words × 8 bits. How many chips are needed to obtain 1024 words × 32 bits, with all chips sharing address inputs?

**Answer format:** Integer.

### Q22. [1 Mark] [MSQ]

In a standard B+ tree in which all data entries are stored at leaves, which statements hold?

A. Internal separator keys can appear again at the leaf level.
B. All leaves are at the same depth.
C. Every successful lookup must stop at an internal separator without reaching any leaf.
D. The root must always have exactly the same minimum occupancy as a nonroot internal node.

### Q23. [1 Mark] [NAT]

A link carries 2 million bits per second. A 1000-byte packet takes how many milliseconds to serialize onto the link, ignoring overhead and propagation?

**Answer format:** Integer milliseconds.

### Q24. [1 Mark] [MCQ]

A translation lookaside buffer misses, but the page-table entry shows that the page is resident and accessible. Which statement is correct?

A. A TLB miss necessarily requires disk I/O.
B. The translation can be obtained from the page table without a page fault.
C. The virtual address must be invalid.
D. The access must terminate the process.

### Q25. [1 Mark] [NAT]

For x>0, f(x)=ln x−x/2. At what x does f attain its global maximum?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

P(B)=0.5, P(A|B)=0.6 and P(A|not B)=0.2. Find P(B|A).

**Answer format:** Exact finite decimal.

### Q27. [1 Mark] [NAT]

In the lattice of positive divisors of 30 ordered by divisibility, an element y complements 6 if gcd(6,y)=1 and lcm(6,y)=30. Find y.

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A matrix has Doolittle factorization A=LU with diagonal entries of L all one and diagonal entries of U equal to 2,−3,4. No row permutation is used. Find det(A).

**Answer format:** Integer.

### Q29. [1 Mark] [MCQ]

A PDA for balanced parentheses pushes on '(' and pops on ')'. Which extra condition is needed besides having an empty stack at the end, assuming a separate bottom marker?

A. No prefix may attempt to pop below the bottom marker.
B. The input must have odd length.
C. Every '(' must be immediately followed by ')'.
D. The stack may contain only two items throughout the input.

### Q30. [1 Mark] [NAT]

A four-bit ring counter circulates a single 1 through its flip-flops, starting at 1000. How many clock edges are needed to return to 1000 for the first time?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

For exact integer arithmetic with no side effects, which local replacements preserve a variable x's value for all x?

A. x+0 → x
B. x*1 → x
C. x*0 → x
D. x−x → 0

### Q32. [1 Mark] [MCQ]

A committed transaction's update is lost after a crash despite the system acknowledging its commit. Which ACID property is directly violated?

A. Durability
B. Atomicity necessarily, even if every update of that transaction was lost together
C. Isolation only
D. No property, because crashes are excluded from ACID concerns

### Q33. [1 Mark] [NAT]

A divide-and-conquer procedure on 16 elements repeatedly splits each nontrivial problem into equal halves until size one. How many leaves are in its recursion tree?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

Which operation is guaranteed to preserve context-freeness for two context-free languages L1,L2?

A. Union
B. Intersection in every case
C. Complement in every case
D. Set difference in every case

### Q35. [1 Mark] [NAT]

Starting with an empty stack, process tokens `5 2 - 3 *` as a postfix arithmetic expression, with binary operators popping the right operand first. What value remains?

**Answer format:** Integer.

### Q36. [2 Marks] [MCQ]

For the unary language L={a^(n²):n≥0}, a pumping proof chooses a^(p²) and a pumped segment of length d with 1≤d≤p. Why does pumping once extra give a contradiction?

A. p²+d lies strictly between p² and (p+1)², so it is not a square.
B. p²+d is always less than p².
C. Every unary language is finite.
D. Pumping is prohibited for unary alphabets.

### Q37. [2 Marks] [MSQ]

A loop begins with x=0 and repeatedly executes `x=x+1` while an input-dependent condition holds. A simple forward constant-propagation analysis joins facts from the initial edge and loop back edge at the header. Which statements are correct?

A. x need not be a single known constant at the loop header after the fixed point is reached.
B. Treating x as zero on every header visit is sound merely because its initializer is zero.
C. Different iterations can reach the header with different x values.
D. Constant propagation alone necessarily computes the exact iteration count for every input condition.

### Q38. [2 Marks] [NAT]

A signed eight-bit fixed-point format has three fractional bits. An exact real result of 17 is converted to this format using saturation to the largest representable value on positive overflow. What real value is stored?

**Answer format:** Exact finite decimal.

### Q39. [2 Marks] [NAT]

A cache miss adds 40 cycles to a base execution of one cycle per instruction. An optimization reduces misses per instruction from 0.04 to 0.01 but increases the instruction count by 20%. Clock period is unchanged and no penalties overlap. What is the ratio of old execution time to new execution time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q40. [2 Marks] [MSQ]

A machine M is described together with a finite input x and a nonnegative integer bound k. Which questions are decidable uniformly from this data?

A. Does M accept x within k steps?
B. Does M halt on x within k steps?
C. Does M eventually halt on x with no bound?
D. Does the simulation visit the same full configuration twice within its first k steps?

### Q41. [2 Marks] [NAT]

A lock manager uses shared and exclusive locks. Initially T1 holds S(A), T2 holds S(A) and S(B), and T3 holds S(B). T1 then requests X(B); T3 requests X(A); T2 requests an upgrade to X(A). All three requests wait, all existing locks are retained, and a request waits only for incompatible locks held by other transactions. How many directed edges are in the wait-for graph, counting each ordered pair once?

**Answer format:** Integer.

### Q42. [2 Marks] [MCQ]

A variable x is live after statement `x = y+z`. Which statement describes the liveness transfer across this assignment, ignoring other live variables?

A. Old x must remain live before the statement solely because new x is live after it.
B. Old x is killed by the assignment, while y and z are used and become live before it.
C. y and z are killed because they appear on the right-hand side.
D. The statement cannot define x because x is already live.

### Q43. [2 Marks] [NAT]

A ternary relationship R(A,B,C) has exactly the four tuples (0,0,0),(0,1,1),(1,0,1),(1,1,0). It is replaced by its three binary projections on AB, BC and AC. Under set semantics, naturally join these projections on their common attributes. How many tuples in the join were not in the original relationship?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A normalized binary floating-point format has three significant bits including the leading 1 and rounds to nearest, ties to even. Exponents cover the required range. What is the absolute rounding error when storing exact value 7.5?

**Answer format:** Exact finite decimal.

### Q45. [2 Marks] [NAT]

A BFS starts at s in an undirected graph with edges sa,sb,ac,ad,bd,be. Vertices are marked when first enqueued; neighbours may be scanned in any order. Count distinct full discovery orders, including s. How many are possible? Different adjacency scans producing the same discovery order count only once.

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

Evaluate ∫₀¹ ln(1+x)/(1+x) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q47. [2 Marks] [MSQ]

Boolean function F=(x+y)(x+z). Which expressions are equivalent to F?

A. x+yz
B. x(y+z)
C. (x+y)(x+z)(x+y+z)
D. xy+xz

### Q48. [2 Marks] [NAT]

A rooted tree has 15 vertices. Every internal vertex has exactly three children. How many leaves does it have?

**Answer format:** Enter -1 if no such tree exists; otherwise enter the number of leaves.

### Q49. [2 Marks] [NAT]

A file uses a linked allocation scheme with 512-byte disk blocks, of which four bytes in every block store the next-block pointer. How many blocks are required to store 2033 data bytes? No extra file header is stored inside these blocks.

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

A direct-mapped cache has eight lines. A loop repeatedly reads blocks 0,8,16 in that order, for ten complete iterations. The cache starts empty and maps a block to its number modulo eight. How many cache hits occur in the entire loop?

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

After a successful fork, both processes execute `counter++`, where counter was an ordinary private global integer equal to 5 before fork. There is no shared-memory mapping. After both increments, what are their counter values?

A. Each process has value 6 in its own address space.
B. Both necessarily observe a shared value 7.
C. The child must have value 1.
D. The parent must retain value 5.

### Q52. [2 Marks] [NAT]

Five observations have sum 20 and sum of squares 90. One observation equal to 6 is removed. What is the population variance of the remaining four observations, using divisor four?

**Answer format:** Exact finite decimal.

### Q53. [2 Marks] [NAT]

In the additive group Z8×Z2, how many elements have order exactly four?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A block contains a 3×4 array of data bits. Separate parity bits check every row and every column. Exactly four distinct data bits flip, and no parity bit changes. How many four-position error patterns go undetected by all row and column parity checks?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

A process has two threads sharing ordinary memory. Each executes the non-atomic operation `x = x+1` once, starting from x=0, with separate load/add/store steps and sequentially consistent interleaving. Which final values of x are possible?

A. 0
B. 1
C. 2
D. 3

### Q56. [2 Marks] [NAT]

During a 1000-cycle interval, a DMA controller steals one memory-bus cycle in every group of five cycles. A CPU instruction stream requires the bus every cycle and otherwise could complete one instruction per cycle. Assume a stolen cycle stalls exactly one instruction opportunity, with no other stalls. How many instructions complete during the interval?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

Consider `t=a+b; if (p) a=0; u=a+b;`, with ordinary nonaliased scalars and both branches feasible. Which statements hold?

A. Replacing the final expression by t unconditionally is generally unsound.
B. On the path where p is false, the earlier value t remains available for the final expression.
C. On the path where p is true, t necessarily equals the new a+b for all initial values.
D. Common-subexpression availability must account for definitions along paths.

### Q58. [2 Marks] [NAT]

Under set semantics, R(A,B)={(1,x),(1,y),(2,x),(3,x),(3,y)} and S(B)={x,y}. How many tuples are in relational division R÷S?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

In a BST subtree, root x has left subtree A and right child y. Node y has left subtree B and right subtree C. A contains 4 nodes, B 6 nodes and C 9 nodes. Perform a standard left rotation at x, making y the new subtree root. Every key is equally likely in a successful search, and a key at depth d from the full-tree root costs d+1 comparisons. What is the change (new minus old) in the sum of successful-search comparison counts over all keys in the full tree?

**Answer format:** Integer, possibly negative.

### Q60. [2 Marks] [NAT]

An undirected graph consists of the four-cycle a–b–c–d–a and diagonal a–c. Every edge has weight one. How many distinct minimum spanning trees does it have?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

In one slotted random-access attempt, four stations independently transmit with probability 1/2. A success occurs exactly when one station transmits. What is the probability of success in this slot?

**Answer format:** Exact finite decimal.

### Q62. [2 Marks] [MCQ]

A binary min-heap contains distinct keys. Decreasing the key at an arbitrary nonroot index may violate heap order with which nodes first?

A. Its parent; upward restoration may be needed.
B. Only its children; downward restoration is always required.
C. Every node necessarily becomes invalid.
D. No heap-order violation can result from decreasing a key.

### Q63. [2 Marks] [NAT]

A router knows an undirected network with edges AB=1, AC=4, BC=2, BD=5, CD=1. Using complete link-state information, what is the shortest-path distance from A to D?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

For regular expressions over {a,b}, which identities hold as language equalities, with ε denoting the empty word?

A. (a*)*=a*
B. (a|b)*=a*b*
C. εa=a
D. (ab)*=a*b*

### Q65. [2 Marks] [NAT]

How many labelled trees on vertices 1,…,6 have degrees d1=3,d2=2,d3=2,d4=d5=d6=1?

**Answer format:** Integer.

## ANSWER KEY — MOCK TEST 014

NAT answers are exact except where an accepted rounded range is shown.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MCQ | 1 | A |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 36 |
| 5 | NAT | 1 | 4.8 |
| 6 | NAT | 2 | 4 |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 0.75 |
| 9 | MCQ | 2 | A |
| 10 | NAT | 2 | 20 |
| 11 | MCQ | 1 | C |
| 12 | NAT | 1 | 4 |
| 13 | MCQ | 1 | A |
| 14 | MSQ | 1 | A, B |
| 15 | NAT | 1 | 1 |
| 16 | NAT | 1 | 9 |
| 17 | MCQ | 1 | A |
| 18 | NAT | 1 | 5 |
| 19 | MCQ | 1 | A |
| 20 | NAT | 1 | 1 |
| 21 | NAT | 1 | 4 |
| 22 | MSQ | 1 | A, B |
| 23 | NAT | 1 | 4 |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 2 |
| 26 | NAT | 1 | 0.75 |
| 27 | NAT | 1 | 5 |
| 28 | NAT | 1 | -24 |
| 29 | MCQ | 1 | A |
| 30 | NAT | 1 | 4 |
| 31 | MSQ | 1 | A, B, D |
| 32 | MCQ | 1 | A |
| 33 | NAT | 1 | 16 |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 9 |
| 36 | MCQ | 2 | A |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 15.875 |
| 39 | NAT | 2 | 1.5476 (range 1.54755–1.54765) |
| 40 | MSQ | 2 | A, B, D |
| 41 | NAT | 2 | 5 |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 4 |
| 44 | NAT | 2 | 0.5 |
| 45 | NAT | 2 | 4 |
| 46 | NAT | 2 | 0.2402 (range 0.24015–0.24025) |
| 47 | MSQ | 2 | A, C |
| 48 | NAT | 2 | -1 |
| 49 | NAT | 2 | 5 |
| 50 | NAT | 2 | 0 |
| 51 | MCQ | 2 | A |
| 52 | NAT | 2 | 1.25 |
| 53 | NAT | 2 | 4 |
| 54 | NAT | 2 | 18 |
| 55 | MSQ | 2 | B, C |
| 56 | NAT | 2 | 800 |
| 57 | MSQ | 2 | A, B, D |
| 58 | NAT | 2 | 2 |
| 59 | NAT | 2 | -5 |
| 60 | NAT | 2 | 8 |
| 61 | NAT | 2 | 0.25 |
| 62 | MCQ | 2 | A |
| 63 | NAT | 2 | 4 |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 12 |

