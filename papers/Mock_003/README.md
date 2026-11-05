# GATE CS 2027 — Full-Length Mock Test 003

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

- MCQ: select exactly one of four options. An incorrect one-mark MCQ loses 1/3 mark; an incorrect two-mark MCQ loses 2/3 mark.
- MSQ: select all correct options. No partial credit and no negative marking.
- NAT: enter a numerical value using the stated precision. No negative marking.
- Unattempted questions receive zero marks. Unless stated otherwise, arithmetic is exact and logarithm bases are as indicated.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

After a library extended its evening hours, the number of evening visits increased, while total weekly visits remained unchanged. A report concludes that the extension attracted additional weekly visitors. Which criticism is best supported by the information given?

A. Evening visits cannot increase unless weekly visits increase.  
B. Some visits may have shifted from daytime to evening, and visit counts do not identify distinct visitors.  
C. The extension must have reduced the number of distinct visitors.  
D. Every evening visitor previously visited during daytime.

### Q2. [1 Mark] [NAT]

Five distinct books A,B,C,D,E are placed in a row. A must appear somewhere before B, and C and D must not be adjacent. How many arrangements satisfy both conditions?

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

The table gives successful applications divided by total applications for two programmes. Every application belongs to exactly one programme.

| Programme | Year 1 | Year 2 |
|---|---:|---:|
| P | 80/100 | 9/10 |
| Q | 20/100 | 27/90 |

Which statements follow from the table?

A. Each programme's success percentage increased.  
B. The combined success percentage increased.  
C. Programme Q's share of all applications increased.  
D. The table proves that an individual applicant's chance of success increased because of a policy change.

### Q4. [1 Mark] [MCQ]

A square sheet occupies 0≤x≤8, 0≤y≤8. Fold the right half onto the left along x=4, then fold the upper half onto the lower along y=4. A point hole is punched at (1,3) in the folded sheet through all layers. After unfolding, what is the greatest distance between two holes?

A. 6  
B. 2√10  
C. 8  
D. 4√5

### Q5. [1 Mark] [MCQ]

Arrange these sentences into the most coherent chronological paragraph, using the references “that inspection” and “second inspection” consistently.

P. This second inspection found no leak.  
Q. The crew replaced the cracked valve and inspected the pipe again.  
R. A pressure drop first prompted an inspection.  
S. That inspection identified a crack in the valve.

A. R,Q,S,P  
B. S,R,Q,P  
C. R,S,Q,P  
D. Q,P,R,S

### Q6. [2 Marks] [MCQ]

A fair coin selects one of two boxes. Box I contains two red balls and one blue ball; Box II contains one red ball and two blue balls. Two balls are drawn uniformly without replacement from the selected box. Given that at least one drawn ball is red, what is the probability that both are red?

A. 1/6  
B. 1/3  
C. 1/5  
D. 2/5

### Q7. [2 Marks] [MCQ]

A policy states: “Unless the permit is renewed before Monday, the pilot must stop on Monday. Renewal alone does not authorize expansion; an independent review is also required.” Assume the policy is followed and the pilot continues on Tuesday. Which conclusion is justified?

A. An independent review must already have authorized expansion.  
B. The permit was renewed before Monday, but authorization for expansion cannot be inferred.  
C. Continuing the pilot automatically authorizes expansion.  
D. The permit could have remained unrenewed because an independent review replaces renewal.

### Q8. [2 Marks] [MSQ]

For which of the following real values of x is the equation log_x(16)=log_2(x) defined and true?

A. 4  
B. 1/4  
C. −4  
D. 1

### Q9. [2 Marks] [NAT]

Four distinct tasks A,B,C,D are placed in a linear order. Consider the four assertions: A is before B; B is before C; C is before D; D is before A. How many task orders make exactly two assertions true?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

A solid cube is assembled from 27 unit cubes in a 3×3×3 arrangement. Remove the central unit cube of each of its six faces, leaving all other unit cubes in place. Count every face of a remaining unit cube that is adjacent to empty space, including space within the resulting openings. What is the total exposed area in square units?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Which of the following problems have an algorithm that always halts and answers correctly? Machines have finite descriptions; Turing machines are deterministic.

A. Given a Turing machine and an input, determine whether it halts within 100 transitions.  
B. Given a Turing machine and an input, determine whether it eventually halts.  
C. Given a DFA over {0,1}, determine whether it accepts every binary string.  
D. Given a Turing machine, determine whether it halts on every input.

### Q12. [1 Mark] [MCQ]

A byte-addressed system maps four 4 KiB×8 memory chips consecutively to addresses 0x8000–0xBFFF. Chips are numbered 0 through 3 in increasing base-address order. Which pair gives the chip number and the offset within that chip for address 0x9ABC?

A. (0,0x9ABC)  
B. (2,0xABC)  
C. (1,0x1ABC)  
D. (1,0xABC)

### Q13. [1 Mark] [MCQ]

Define f(x)=(e^x−1)/x for x<0, and f(x)=a+bx for x≥0. Which pair (a,b) makes f differentiable at 0?

A. (1,1/2)  
B. (0,1)  
C. (1,1)  
D. (1/2,1)

### Q14. [1 Mark] [NAT]

X takes values 0 and 1, and Y=1−X. If E[X+2Y]=1.7, what is Var(X+2Y)?

**Answer format:** Decimal rounded to two places.

### Q15. [1 Mark] [MCQ]

Integer division discards the fractional part. What sequence is printed by visit(4)?

```text
visit(n):
    if n == 0: return
    visit(n / 2)
    print(n)
    visit((n - 1) / 2)
```

A. 1,2,1,4  
B. 1,2,4,1  
C. 4,2,1,1  
D. 1,2,3,4

### Q16. [1 Mark] [NAT]

Starting with one process, the following code executes. Every fork succeeds, returns 0 only in its new child, and returns a positive child identifier in its parent. Every process reaches the final line once. How many processes execute work()?

```c
int p = fork();
if (p == 0) fork();
fork();
work();
```

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

A hash table has indices 0–6, hash h(k)=k mod 7, and linear probing. Insert 10,17,24 into an empty table, then delete 17 by leaving a tombstone. A successful search for 24 must continue past tombstones. Afterwards insert 31, known absent, reusing the first available tombstone. What are the number of slots inspected in the search for 24 and the index occupied by 31?

A. (2,4)  
B. (3,4)  
C. (3,6)  
D. (2,5)

### Q18. [1 Mark] [MSQ]

Two threads each execute the following two-iteration loop on shared x, initially 0. Each read and write is atomic, the computation uses a private register r, and execution is a sequentially consistent interleaving preserving each thread's order.

```text
repeat twice:
    r = x
    x = r + 1
```

Which values of x are possible after both threads finish?

A. 1  
B. 2  
C. 3  
D. 4

### Q19. [1 Mark] [NAT]

Let g permute {1,2,3} cyclically: g(1)=2, g(2)=3, g(3)=1. How many functions f:{1,2,3}→{1,2,3} satisfy f(g(x))=g(f(x)) for every x?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

A real 4×4 matrix M satisfies M²=I and trace(M)=0. Which statements must hold?

A. det(M)=1.  
B. rank(M−I)=2.  
C. M is diagonalizable over the real numbers.  
D. M is symmetric.

### Q21. [1 Mark] [MSQ]

Every employee belongs to exactly one department; a department may have zero or more employees. Employee and department identifiers are unique in their respective entity sets. A relation Membership(E,D) contains exactly the employee–department memberships. Which statements must hold?

A. E→D holds in Membership.  
B. D→E holds in Membership.  
C. Projecting Membership on D returns every department identifier.  
D. Projecting Membership on E returns every employee identifier.

### Q22. [1 Mark] [MCQ]

A 4-to-1 multiplexer has select bits A,B, with A more significant. Its data inputs for select values 00,01,10,11 are C, NOT C, 1,0 respectively. Minterms are numbered using A,B,C with A most significant. Which set is the output's on-set?

A. {0,3,4,5}  
B. {1,2,4,5}  
C. {1,2,6,7}  
D. {0,1,2,5}

### Q23. [1 Mark] [MCQ]

An expression translator uses this grammar and emits postfix code. For E→E−T it emits the left E's code, then T's code, then “−”. For E→T and T→digit it emits the child's code and the digit respectively. What is emitted for 8−3−2?

A. 8 3 2 − −  
B. − − 8 3 2  
C. 8 3 − 2 −  
D. 8 − 3 − 2

### Q24. [1 Mark] [MSQ]

An established TCP connection carries five bytes. The sender issues successful send calls containing three bytes and then two bytes, in that order. No connection closure or error occurs. The receiver uses blocking recv calls with a buffer capacity of five bytes. Which receive patterns are possible, considering TCP byte-stream semantics?

A. One recv returns all five bytes.  
B. Two recv calls return one byte and then four bytes.  
C. A recv returns zero solely because no bytes have arrived yet.  
D. The receiver obtains the two-byte send's bytes before the three-byte send's bytes.

### Q25. [1 Mark] [MSQ]

A synchronous two-bit machine updates (q1,q0) to (q0,q1 XOR q0) on each clock edge. Its reset state is 01. Which statements are correct?

A. The reset trajectory has period 3.  
B. State 00 is reached after three edges from reset.  
C. State 10 is reached after two edges from reset.  
D. q1 and q0 are complements throughout the reset trajectory.

### Q26. [1 Mark] [NAT]

R(A,B)={(1,2),(1,3),(2,3)}. Using set semantics, form T(A,C) by joining R(A,B) with a renamed copy R(B,C) on B and projecting on A,C. Rename R's B attribute to C before taking the difference T−R. How many tuples are in this difference?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

In a lexically scoped language, procedures Q and R are both immediately nested inside P. P declares x; Q and R do not declare x. During the calls P→Q→R, R accesses P's x. Static links point to the most recent activation of the immediately enclosing lexical procedure; dynamic links point to the caller. From R's activation, how many static links and dynamic links, respectively, lead to P's activation?

A. (2,1)  
B. (1,1)  
C. (2,2)  
D. (1,2)

### Q28. [1 Mark] [NAT]

B is a 3×4 array of four-byte elements stored in row-major order, with B[0][0] at byte address 1000. A transposed view C is defined by C[i][j]=B[j][i], without copying any elements. What is address(C[1][2])−address(C[0][1]), in bytes?

**Answer format:** Integer.

### Q29. [1 Mark] [MCQ]

A circular singly linked list has traversal 1→2→3→4→1, and tail points to node 4. Execute tail.next=tail.next.next. Then insert a new node 5 immediately after tail and set tail to this new node. What traversal starts at the new head tail.next?

A. 1,2,3,4,5  
B. 5,2,3,4  
C. 2,3,4,5  
D. 2,3,5,4

### Q30. [1 Mark] [MSQ]

Every memory access first spends 1 ns at L1. An L1 miss spends an additional 9 ns at L2; an L2 miss spends another 90 ns at memory. The L1 hit probability is 0.8, and the L2 hit probability conditional on an L1 miss is 0.5. Which statements are correct?

A. The probability of an L1 miss followed by an L2 hit is 0.1.  
B. The probability of accessing main memory is 0.1.  
C. The average access time is 11.8 ns.  
D. Half of all original accesses are L2 hits.

### Q31. [1 Mark] [MCQ]

How many times is work() called asymptotically, for positive integer n?

```text
for i = 1 to n:
    j = i
    while j <= n:
        work()
        j = j + i
```

A. Θ(n)  
B. Θ(n²)  
C. Θ(log n)  
D. Θ(n log n)

### Q32. [1 Mark] [MCQ]

A parent creates a pipe and forks two children, both inheriting both pipe ends. The parent closes its write end and reads. Child I writes a finite message and closes both ends. Child II closes its read end but keeps its write end open indefinitely without writing. After consuming Child I's entire message, what happens to the parent's next blocking read, assuming no signals or errors?

A. It immediately returns end-of-file because Child I finished.  
B. It blocks because a write end remains open.  
C. It returns the last byte repeatedly.  
D. It necessarily raises a broken-pipe error.

### Q33. [1 Mark] [NAT]

An HTTP client first opens a new TCP connection and obtains a base HTML document. It then opens exactly three new TCP connections in parallel for six images, requesting one image per connection at a time and reusing each connection for its second image. There is no pipelining. Each TCP handshake takes one RTT, and each request-response takes one RTT. RTT is 40 ms for every connection. Ignore DNS, transmission time, TLS and processing. What is the minimum time from starting the HTML connection until all images arrive, in milliseconds?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

For real c, let f(x)=x³−3x²+cx on [0,2]. What is the smallest c for which f is nondecreasing throughout this interval?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A DFA over {0,1} must accept exactly the nonempty strings whose binary numerical value is divisible by 3. Leading zeros are allowed; the empty string must be rejected. How many states does a minimal complete DFA need?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A direct-mapped cache has two 16-byte lines, is initially empty, and uses write-back with write allocation. Arrays A and B each contain four four-byte words. A begins at byte address 0 and B at byte address 32. Execute, for i=0,1,2,3, in this order: read A[i], write B[i], read A[i]. Each miss transfers one whole block from memory; each dirty eviction writes one whole block to memory. Ignore all other traffic and do not flush the cache afterwards. How many bytes are transferred between cache and memory in total?

**Answer format:** Integer.

### Q37. [2 Marks] [MCQ]

Student(S)={(1),(2)}, Enrollment(S,C)={(1,X)}, and Required(C) is empty. No constraint requires an enrolled course to be in Required. Compare:

- QI: all Student identifiers s such that for every c in Required, (s,c) is in Enrollment.
- QII: relational division Enrollment ÷ Required, with candidate S values taken from the projection of Enrollment on S.

Using set semantics, what are the results (QI,QII)?

A. (empty,empty)  
B. ({1},{1})  
C. ({1,2},{1,2})  
D. ({1,2},{1})

### Q38. [2 Marks] [MSQ]

Sales(dept,amount) contains (A,10),(A,NULL),(A,20),(B,NULL),(B,NULL),(C,5). Standard SQL NULL and aggregate semantics apply. Consider:

```sql
SELECT dept, SUM(amount) AS total
FROM Sales
GROUP BY dept
HAVING COUNT(*) > COUNT(amount) AND SUM(amount) > 10;
```

Which statements are correct?

A. The query returns exactly one row.  
B. The row for A has total 30.  
C. The query returns B with total 0.  
D. Replacing COUNT(amount) in the HAVING clause by COUNT(*) makes the result empty.

### Q39. [2 Marks] [MCQ]

A hidden source is chosen once: source I with probability 1/3, source II with probability 2/3. Conditional on that source, trials are independent; success probability is 1/4 for I and 1/2 for II. Given exactly two successes in the first three trials, what is the probability of success on the fourth trial?

A. 1/2  
B. 35/76  
C. 3/19  
D. 7/16

### Q40. [2 Marks] [NAT]

Short-circuit intermediate code evaluates P AND (Q OR R) from left to right, skipping operands whose values cannot affect the result. P,Q,R are independent Boolean inputs, each true with probability 1/2. What is the expected number of input predicates evaluated?

**Answer format:** Decimal rounded to two places.

### Q41. [2 Marks] [NAT]

A queue is implemented by input stack I and output stack O. Enqueue pushes onto I. Dequeue transfers every element of I to O only when O is empty, then pops O. Initially both stacks are empty. Perform: enqueue 1–6; dequeue twice; enqueue 7–9; dequeue four times; enqueue 10; dequeue twice. Each individual stack push or pop costs one unit; no other operations are counted. What is the total cost?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Consider the positive divisors of 60, ordered by divisibility. The least and greatest elements are 1 and 60. A complement of d is a divisor e with meet(d,e)=1 and join(d,e)=60. Which statements are correct?

A. This partially ordered set is a lattice.  
B. Every element has a complement.  
C. Exactly eight elements have complements.  
D. The lattice is distributive.

### Q43. [2 Marks] [MCQ]

Weighted activities have half-open time intervals, so one may start when another finishes:

| Activity | Interval | Weight |
|---|---|---:|
| A | [0,2) | 4 |
| B | [1,3) | 5 |
| C | [2,4) | 4 |
| D | [3,5) | 5 |
| E | [4,6) | 4 |
| F | [5,6) | 3 |

An earliest-finish greedy algorithm repeatedly chooses the compatible activity finishing first, breaking a tie by the earlier start. What pair gives (greedy total weight, maximum possible total weight)?

A. (12,12)  
B. (13,13)  
C. (12,13)  
D. (11,13)

### Q44. [2 Marks] [MCQ]

An eight-bit two's-complement fixed-point format has four fractional bits. Multiply the values encoded by 0xE6 and 0x1C using an exact intermediate result, then round once to the nearest representable value, breaking a tie toward an even least significant retained bit. No overflow occurs. What is the final encoded byte?

A. 0xD3  
B. 0xD2  
C. 0x2E  
D. 0xD4

### Q45. [2 Marks] [NAT]

A TCP segment contains 1000 data bytes and a 20-byte TCP header. It is carried in an IPv4 datagram with a 20-byte header and no options. A router fragments this datagram for a link whose IP MTU is 600 bytes, using the minimum number of fragments and the largest permitted first-fragment payload. Each link frame adds a 14-byte header and a four-byte trailer. Ignore padding, preambles and gaps. How many bytes are transmitted on this link for all fragments, including these headers and trailers?

**Answer format:** Integer.

### Q46. [2 Marks] [MCQ]

The block below uses exact integer arithmetic, ordinary scalars and no aliases. An optimizer may share identical expressions, treating multiplication as commutative, and remove unnecessary copies. It must preserve all returned values. It may not use distributivity or introduce operations other than the displayed additions and multiplications. What are the minimum numbers of multiplications and additions, respectively?

```text
a = x * y
b = y * x
c = a + z
d = b + z
x = x + 1
e = x * y
f = e + z
return (c,d,f)
```

A. (1,2)  
B. (2,2)  
C. (2,3)  
D. (3,3)

### Q47. [2 Marks] [NAT]

Let A have rows (2,1,1), (4,3,3), (8,7,9). Solve Ax=b for b=(4,10,30)ᵀ using exact arithmetic. What is the second component of x?

**Answer format:** Integer, possibly negative.

### Q48. [2 Marks] [MSQ]

For the grammar S→SS | a, consider the string aaaaa. Parse trees are ordered, and derivations are finite. Which statements are correct?

A. It has exactly 14 parse trees.  
B. It has exactly 14 leftmost derivations.  
C. Counting leftmost and rightmost derivations produces 28 different parse trees.  
D. The language generated by the grammar is regular.

### Q49. [2 Marks] [MSQ]

Parent(a,b) has the single row (1,2), with composite primary key (a,b). Child(a,b,qty) has a composite foreign key referencing Parent with MATCH SIMPLE, and CHECK(qty>0). All Child columns allow NULL. MATCH SIMPLE skips the referential check when either foreign-key component is NULL; a CHECK rejects only FALSE, not UNKNOWN. Starting with an empty Child table, which individual insertions succeed?

A. (1,NULL,5)  
B. (NULL,9,−1)  
C. (9,9,NULL)  
D. (1,2,NULL)

### Q50. [2 Marks] [NAT]

A full binary tree has exactly eight leaves; every internal node has exactly two children. Height is the largest number of edges on a root-to-leaf path. How many distinct height values are possible among such trees?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

A robot must advance exactly eight units. Each move advances either one or two units, and two two-unit moves may not be consecutive. Different ordered move sequences are counted separately. How many valid sequences exist?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

Insert the six distinct keys 1–6 into an initially empty ordinary binary search tree, with no rotations. How many insertion permutations have root 3 and final height exactly 2, measured in edges?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

A pushdown machine starts with an empty stack. Reading a pushes one X. Reading b nondeterministically pops either one X or two X symbols; a move requiring unavailable symbols is disallowed. There are no other choices or epsilon moves. It accepts exactly when the entire input is consumed and the stack is empty. How many accepting computations exist on the input shown below? Spaces separate blocks for readability and are not input symbols.

```text
aa b a b aaaa bbb
```

Computations are distinct if their choices of one-symbol versus two-symbol pops differ.

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A 4000-byte message is divided into n equal-payload packets, each with an additional 100-byte header. Choose n among the positive divisors of 4000. Packets traverse three store-and-forward links with rates 1,2,1 megabits per second, in that order. Each link serves packets in order; different links can operate simultaneously. There are no other delays or traffic, and one megabit is 10⁶ bits. Which n minimizes the time until the entire message reaches the destination?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

A binary floating-point system has four significant bits including the leading 1, unbounded exponents, and round-to-nearest with ties to even after each addition. Starting at x=8, perform x=x+0.5 sixteen times. Which statements are correct?

A. The final stored x is 8.  
B. The exact real-arithmetic result would be 16.  
C. Every one of the sixteen additions is exact in this format.  
D. Instead adding 2 to the initial x four times gives stored result 16.

### Q56. [2 Marks] [MSQ]

A producer performs V(s) twice and terminates. A consumer performs P(s), prints X, performs P(s), and prints X again. Initially s=0. Operations are atomic; scheduling is fair. For a counting semaphore, V increments its count. For the binary version in this question, V sets its value to 1 even if already 1; a successful P changes 1 to 0, otherwise blocks. Which statements are correct?

A. With the counting semaphore, the consumer eventually prints twice.  
B. With the binary semaphore, the consumer can print once and then remain blocked forever.  
C. With the binary semaphore, the consumer can print twice.  
D. With the counting semaphore, the consumer can remain blocked forever without printing, after the producer has terminated.

### Q57. [2 Marks] [NAT]

A DMA device delivers one word every 2 microseconds. The processor is interrupted after each batch of k words. Processing a batch takes 8+k microseconds, including all overhead, and starts as soon as that batch completes if the processor is free. DMA continues into other buffers while processing occurs. There is no other work. Require a steady state without growing backlog and a latency of at most 40 microseconds from arrival of the first word of each batch to completion of processing that batch. How many positive integers k satisfy both requirements?

**Answer format:** Integer.

### Q58. [2 Marks] [MSQ]

A CRC uses generator G(x)=x³+x+1 over GF(2). An error is undetected exactly when its nonzero error polynomial is divisible by G. Which statements are correct?

A. Error x⁷+1 is undetected.  
B. Error x⁶+1 is undetected.  
C. Every single-bit error is detected.  
D. Every nonzero burst error of length at most three bits is detected.

### Q59. [2 Marks] [MSQ]

A Banker's-algorithm system has two resource types. Current available resources are (1,1). Allocation and remaining need are:

| Process | Allocation | Remaining need |
|---|---|---|
| P0 | (1,0) | (1,2) |
| P1 | (0,1) | (2,0) |
| P2 | (1,1) | (1,1) |

Consider each request independently from the displayed state. Which statements are correct?

A. The current state has exactly two safe process-completion orders.  
B. Granting P0's request (1,0) would make the state unsafe.  
C. Granting P1's request (1,0) leaves a safe state.  
D. Granting P2's request (1,0) leaves a safe state.

### Q60. [2 Marks] [MSQ]

For 0≤t≤1, define I(t)=∫₀¹|x−t| dx. Which statements are correct?

A. The minimum of I(t) is 1/4, attained only at t=1/2.  
B. I(t)+I(1−t)≥1/2 for all t in [0,1].  
C. ∫₀¹I(t) dt=1/2.  
D. The set of t in [0,1] satisfying I(t)≤5/16 is an interval of length 1/2.

### Q61. [2 Marks] [MCQ]

Let L be the binary strings containing equally many 0s and 1s. Define K={w: there exists z in 0* such that wz is in L}. Which description of K is correct? Counts refer to w.

A. Number of 0s equals number of 1s.  
B. Number of 0s is at most number of 1s.  
C. Number of 0s is at least number of 1s.  
D. Every binary string belongs to K.

### Q62. [2 Marks] [NAT]

A Boolean function f of three variables is monotone if changing any input from 0 to 1 without changing the others cannot change its output from 1 to 0. It is self-dual if f(NOT x,NOT y,NOT z)=NOT f(x,y,z). How many Boolean functions satisfy both properties? Variables are labelled; permuting them can produce a different function.

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A single CPU uses round-robin scheduling with quantum 2 and zero switching overhead. Processes A,B,C have (arrival,burst) values (0,5),(1,4),(2,2). At a quantum boundary, new arrivals join the ready queue before the preempted running process is requeued. A process whose burst finishes is not requeued. What is the mean waiting time?

**Answer format:** Decimal rounded to two places.

### Q64. [2 Marks] [MCQ]

For n a power of two, consider the following routine. Each work() and every arithmetic or control operation takes constant time. What is its asymptotic running time?

```text
F(n):
    if n <= 1: return
    F(n/2)
    F(n/2)
    for i = 1 to n:
        for j = 1 to i:
            k = 1
            while k <= i:
                work()
                k = 2*k
```

A. Θ(n log n)  
B. Θ(n²)  
C. Θ(n² log n)  
D. Θ(n² (log n)²)

### Q65. [2 Marks] [MSQ]

Consider the following code. Each call to more() returns an arbitrary Boolean value and does not change x. Consider only terminating executions. A conventional constant-propagation analysis tracks a single constant per variable or “not constant”; it joins distinct incoming constants as “not constant” and computes a fixed point over the loop.

```text
x = 1
while more():
    x = 2
y = x
```

Which statements are correct?

A. At the loop header, this analysis establishes x=1 at its fixed point.  
B. Immediately after the body assignment, this analysis establishes x=2.  
C. On every terminating execution, the final y is 2.  
D. Replacing the while loop with a do-while loop executing x=2 before its first call to more() removes final value y=1 from the possible outcomes.

---

## ANSWER KEY — MOCK TEST 003

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 36 (exact) |
| 3 | MSQ | 1 | A, C |
| 4 | MCQ | 1 | B |
| 5 | MCQ | 1 | C |
| 6 | MCQ | 2 | C |
| 7 | MCQ | 2 | B |
| 8 | MSQ | 2 | A, B |
| 9 | NAT | 2 | 16 (exact) |
| 10 | NAT | 2 | 78 (exact) |
| 11 | MSQ | 1 | A, C |
| 12 | MCQ | 1 | D |
| 13 | MCQ | 1 | A |
| 14 | NAT | 1 | 0.21 (two decimals) |
| 15 | MCQ | 1 | B |
| 16 | NAT | 1 | 6 (exact) |
| 17 | MCQ | 1 | B |
| 18 | MSQ | 1 | B, C, D |
| 19 | NAT | 1 | 3 (exact) |
| 20 | MSQ | 1 | A, B, C |
| 21 | MSQ | 1 | A, D |
| 22 | MCQ | 1 | B |
| 23 | MCQ | 1 | C |
| 24 | MSQ | 1 | A, B |
| 25 | MSQ | 1 | A, C |
| 26 | NAT | 1 | 0 (exact) |
| 27 | MCQ | 1 | D |
| 28 | NAT | 1 | 20 (exact) |
| 29 | MCQ | 1 | C |
| 30 | MSQ | 1 | A, B, C |
| 31 | MCQ | 1 | D |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 200 (exact) |
| 34 | NAT | 1 | 3 (exact) |
| 35 | NAT | 1 | 4 (exact) |
| 36 | NAT | 2 | 208 (exact) |
| 37 | MCQ | 2 | D |
| 38 | MSQ | 2 | A, B, D |
| 39 | MCQ | 2 | B |
| 40 | NAT | 2 | 1.75 (two decimals) |
| 41 | NAT | 2 | 38 (exact) |
| 42 | MSQ | 2 | A, C, D |
| 43 | MCQ | 2 | C |
| 44 | MCQ | 2 | B |
| 45 | NAT | 2 | 1096 (exact) |
| 46 | MCQ | 2 | C |
| 47 | NAT | 2 | -2 (exact) |
| 48 | MSQ | 2 | A, B, D |
| 49 | MSQ | 2 | A, D |
| 50 | NAT | 2 | 5 (exact) |
| 51 | NAT | 2 | 19 (exact) |
| 52 | NAT | 2 | 40 (exact) |
| 53 | NAT | 2 | 9 (exact) |
| 54 | NAT | 2 | 8 (exact) |
| 55 | MSQ | 2 | A, B, D |
| 56 | MSQ | 2 | A, B, C |
| 57 | NAT | 2 | 4 (exact) |
| 58 | MSQ | 2 | A, C, D |
| 59 | MSQ | 2 | A, B, D |
| 60 | MSQ | 2 | A, B, D |
| 61 | MCQ | 2 | B |
| 62 | NAT | 2 | 4 (exact) |
| 63 | NAT | 2 | 4.33 (two decimals) |
| 64 | MCQ | 2 | C |
| 65 | MSQ | 2 | B, D |


