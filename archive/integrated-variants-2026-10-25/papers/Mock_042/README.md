# GATE CS 2027 — Full-Length Mock Test 042

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard (target)

## General Instructions

- Attempt the paper within 180 minutes.
- Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each.
- General Aptitude contributes 15 marks, Engineering Mathematics 13 marks, and core Computer Science 72 marks.
- MCQ: choose exactly one option. Incorrect one-mark MCQs lose 1/3 mark; incorrect two-mark MCQs lose 2/3 mark.
- MSQ: select all and only the correct options. There is no partial credit and no negative marking.
- NAT: enter the numerical answer at the stated precision. There is no negative marking.
- Unattempted questions receive zero. The answer key follows Question 65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

In “The researchers preferred the more parsimonious explanation,” parsimonious most appropriately describes an explanation that:

A. refuses to consider any evidence.
B. accounts for the observations with fewer unnecessary assumptions.
C. contains the greatest number of technical terms.
D. is necessarily true because it is shorter.

### Q2. [1 Mark] [MCQ]

An arrow initially points in the positive x direction in a coordinate plane. First reflect the entire plane in the line y=x. Then rotate it clockwise by 90 degrees about the origin. Finally reflect it in the y-axis. In which direction does the arrow point?

A. Positive x
B. Negative x
C. Positive y
D. Negative y

### Q3. [1 Mark] [MSQ]

A rule is claimed for every positive integer n: if n leaves remainder1 upon division by3, then n² leaves remainder1 upon division by3. Which observations are logically valid?

A. Writing n=3k+1 and expanding its square proves the claim for all eligible n.
B. Checking n=1,4,7 proves the universal claim without any further argument.
C. A number with remainder2 can also have a square with remainder1.
D. The converse follows solely because the forward implication holds.

### Q4. [1 Mark] [MCQ]

A cube has six distinct face labels A,B,C,D,E,F. Three valid orientations are listed as (top, front, right): (A,B,C), (A,D,E), and (F,B,E). Which face is opposite B? Rotating the cube does not change its labels.

A. A  
B. C  
C. D  
D. E

### Q5. [1 Mark] [NAT]

A sequence starts at 4. Its successive increments are the prime numbers in increasing order, beginning with 2. What is its sixth term?

**Answer format:** Integer.

### Q6. [2 Marks] [MCQ]

A rectangular garden is 16 m long and 10 m wide. A path of uniform width is laid inside all four edges, leaving a smaller rectangular planted region. The path occupies 88 square metres. What is the width of the path?

A. 1 m  
B. 2 m  
C. 3 m  
D. 4 m

### Q7. [2 Marks] [MCQ]

An editor wants to say that the archivist digitized the files and then found them easier to search. Which revision correctly expresses that meaning without a dangling modifier?

A. Having digitized the files, searching was easier for the archivist.
B. Having digitized the files, the search facility became faster.
C. Having digitized the files, the archivist found them easier to search.
D. Having digitized the files, the documents were easier for the archivist to search.

### Q8. [2 Marks] [NAT]

Every item in a batch costs a retailer ₹80, and the listed selling price is ₹100. The retailer sells three-fifths of the batch at the listed price, then sells all remaining items at one discounted price. The overall profit is 12.5% of the batch's total cost. What percentage discount from the listed price was used for the remaining items? Ignore taxes and other costs.

**Answer format:** Exact integer.

### Q9. [2 Marks] [MSQ]

Exactly two of boxes A,B,C,D contain prizes. Four labels state: A, “Exactly one of A and B contains a prize”; B, “C contains a prize”; C, “D contains no prize”; D, “A contains a prize.” Exactly two labels are true. Which conclusions necessarily follow?

A. A contains a prize.
B. B contains a prize.
C. C contains no prize.
D. D contains no prize.

### Q10. [2 Marks] [MCQ]

A pattern consists of four distinctly labelled points at coordinates P=(0,0), Q=(2,0), R=(0,1), S=(1,1). First reflect it in the line x=y; then rotate it clockwise through 90 degrees about the origin. Which single transformation gives the same final positions for all four labels?

A. Reflection in the x-axis.
B. Reflection in the y-axis.
C. Rotation through 180 degrees about the origin.
D. Translation by (1,−1).

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A function recursively calls itself. Its local scalar variable v must have a separate value for each active call. Which storage arrangement directly supports this requirement?

A. One shared static cell for v with no saving.
B. A separate v slot in each activation record.
C. A single constant compiled into the program.
D. The caller's instruction address used as v's only storage.

### Q12. [1 Mark] [NAT]

A tree has eight vertices of degree 3, five vertices of degree 2, and all remaining vertices of degree 1. How many leaves does it have?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A process opens the same file twice, obtaining independent open file descriptions at offset0, with descriptors a and b. It reads3 bytes through a, then executes dup2(a,b), replacing b's reference by a duplicate of a. It next reads2 bytes through b. All reads return the requested counts. What offset is now observed through a?

**Answer format:** Integer bytes.

### Q14. [1 Mark] [MCQ]

In C, let `int a[4]={2,4,6,8}; int *p=a+1;`. Which expression evaluates to 6 without undefined behaviour?

A. *p++
B. *(p+1)
C. *p+1
D. *(p-1)

### Q15. [1 Mark] [MCQ]

Define f(x)=(e^x−1)/x for x<0, and f(x)=a+bx for x≥0. Which pair (a,b) makes f differentiable at 0?

A. (1,1/2)  
B. (0,1)  
C. (1,1)  
D. (1/2,1)

### Q16. [1 Mark] [MCQ]

A 4-bit adder-subtractor computes A+(B XOR ssss)+s and keeps the low four result bits. Its carry-out is C and its two's-complement signed overflow flag is V. For A=0111, B=1010 and s=1, which triple (result,C,V) is correct?

A. (1101,1,0)  
B. (1101,0,0)  
C. (0011,1,1)  
D. (1101,0,1)

### Q17. [1 Mark] [MSQ]

Every employee belongs to exactly one department; a department may have zero or more employees. Employee and department identifiers are unique in their respective entity sets. A relation Membership(E,D) contains exactly the employee–department memberships. Which statements must hold?

A. E→D holds in Membership.  
B. D→E holds in Membership.  
C. Projecting Membership on D returns every department identifier.  
D. Projecting Membership on E returns every employee identifier.

### Q18. [1 Mark] [MCQ]

A router forwards an IPv4 datagram from one Ethernet link to another. Assume no tunnelling or network address translation. Which pair of fields is necessarily replaced with values appropriate to the outgoing link?

A. Source and destination IPv4 addresses
B. Source and destination TCP port numbers
C. Ethernet source and destination MAC addresses
D. Application sequence numbers

### Q19. [1 Mark] [NAT]

A translator emits three-address code for (a+b)*(a+b)+(a+b), reusing each already computed identical pure subexpression. Inputs are available in variables; assignments that perform no arithmetic are not counted. What is the minimum number of arithmetic instructions using only binary + and * and no algebraic reassociation?

**Answer format:** Exact integer.

### Q20. [1 Mark] [NAT]

A microinstruction independently selects at most one of three signals in group A, at most one of five signals in group B, and any subset of two further independent signals. Each group needs an explicit “none” encoding. Encode each group in its own minimum-width binary field and the further signals as individual bits. How many control bits are required?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

For n=16, how many times does work() execute?

```text
i = n
while i > 0:
    for j = 1 to i:
        work()
    i = floor(i/2)
```

**Answer format:** Integer.

### Q22. [1 Mark] [MCQ]

Initially head points to node A in the singly linked list A→B→C→NULL. Consider these assignments, evaluated in order:

```text
p = head.next
head.next = p.next
p.next = head
head = p
```

Which list is reachable from head afterward?

A. A→C→B→NULL
B. B→A→C→NULL
C. B→C→A→NULL
D. A→B→C→NULL

### Q23. [1 Mark] [NAT]

A continuous random variable X has density f(x)=c x(1−x) for 0<x<1 and zero elsewhere, with c chosen to normalize the density. Find E[X²].

**Answer format:** Exact finite decimal.

### Q24. [1 Mark] [MCQ]

A synchronous three-bit binary counter has next-state equations q0′=NOT q0, q1′=q1 XOR q0, q2′=q2 XOR (q1 AND q0). Starting in 011, what is its state after five clock edges?

A. 111
B. 000
C. 001
D. 101

### Q25. [1 Mark] [NAT]

Under set semantics R(A)={1,2,3}, S(A)={2,4}, and T(A)={1,4}. How many tuples are in (R−S)∪(S∩T)?

**Answer format:** Integer.

### Q26. [1 Mark] [MCQ]

Over {a,b}, L consists of strings whose every even-numbered position contains a, numbering positions from one. Odd positions are unrestricted; ε belongs to L. What is the minimum number of states in a complete DFA for L?

A. 2
B. 3
C. 4
D. 5

### Q27. [1 Mark] [NAT]

On set{1,2,3,4}, define xRy exactly when floor(x/2)=floor(y/2). How many ordered pairs belong to R?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

Consider ordinary integer variables with no overflow or side effects:

```text
x = a * 0
y = x + b
x = 7
return y
```

Which replacement computes the same returned value for all inputs?

A. return 7+b
B. return a+b
C. return b
D. return 0

### Q29. [1 Mark] [NAT]

A link carries 2 million bits per second. A 1000-byte packet takes how many milliseconds to serialize onto the link, ignoring overhead and propagation?

**Answer format:** Integer milliseconds.

### Q30. [1 Mark] [MCQ]

A greedy coin algorithm repeatedly takes the largest denomination not exceeding the remaining amount. With denominations1,4,6 and target8, how many more coins does greedy use than an optimal solution?

A. 0
B. 1
C. 2
D. 3

### Q31. [1 Mark] [MCQ]

A scheduler assigns smaller numeric priority to more urgent jobs. Every waiting job's priority decreases by one per time unit, while a running job's priority is unchanged. Which problem is this aging rule principally intended to mitigate?

A. Deadlock caused by inconsistent mutex acquisition order.
B. Starvation of low-priority jobs under repeated arrivals of more urgent work.
C. Internal fragmentation in a page.
D. Loss of a dirty cache line during DMA.

### Q32. [1 Mark] [MSQ]

Which Boolean expressions equal x for all x,y?

A. x+xy
B. x(x+y)
C. x+y
D. x XOR x

### Q33. [1 Mark] [MCQ]

A two-level AND–OR circuit implements f=ab+(NOT a)c. Assume b=c=1 and only a changes from0 to1. Gate delays are arbitrary positive values; a and NOT a need not change simultaneously. Which extra product term can be ORed into the output without changing f's Boolean function and eliminates the possible static-1 hazard for this transition?

A. (NOT b)(NOT c)
B. a(NOT c)
C. bc
D. (NOT a)(NOT b)

### Q34. [1 Mark] [NAT]

A real matrix has rows (0,−2),(1,3). Find the trace of its inverse.

**Answer format:** Exact finite decimal.

### Q35. [1 Mark] [MCQ]

For a PDA accepting by empty stack with all input consumed, why must the input-consumption condition be checked explicitly?

A. Emptying the stack while unread input remains is not by itself acceptance under this convention.
B. A stack can never be empty.
C. Input is always consumed in one transition.
D. Empty-stack acceptance requires a finite input alphabet of exactly one symbol.

### Q36. [2 Marks] [NAT]

Inputs 1,2,3,4 enter a single stack in that order. Each input is pushed exactly once and each is popped exactly once; pops produce an output permutation. How many distinct output permutations are possible if the stack may never hold more than two items?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A CRC uses generator g(x)=x²+x+1 over GF(2). A seven-bit frame suffers exactly two distinct bit flips, at positions chosen from0 through6. How many unordered position pairs produce an undetected error?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

Matrices A,B,C have dimensions10×2,2×20,20×3. Scalar multiplication count for multiplying an r×s matrix by an s×t matrix is rst. How many scalar multiplications are saved by choosing the cheaper parenthesization of ABC instead of the more expensive one?

**Answer format:** Integer.

### Q39. [2 Marks] [MCQ]

A compiler analyzes `if (p) x=2; else x=3; y=x-x;`, with exact integer arithmetic and no aliases. Which statement distinguishes simple constant propagation from an algebraic simplification?

A. At the merge x is a single known constant 2.
B. A nonrelational constant-only analysis that evaluates operations only on constant operands may leave y unknown, while the identity x−x=0 proves y is zero.
C. y can equal 1 because x has two possible values.
D. Algebraic simplification is invalid because p is unknown.

### Q40. [2 Marks] [NAT]

Four symbols have frequencies 2,3,7,8. A binary Huffman code is built by repeatedly merging the two smallest weights. What is the sum over symbols of frequency times codeword length?

**Answer format:** Integer.

### Q41. [2 Marks] [MSQ]

Unary relations R and S are finite. Compare query F={x : R(x) AND NOT S(x)} with query G={x : NOT S(x)} over an unrestricted infinite domain. Which statements are correct?

A. F is contained in the active domain of R.
B. G can return infinitely many values.
C. The occurrence of NOT makes F necessarily unsafe.
D. Positive range restriction by R is relevant to F's domain independence.

### Q42. [2 Marks] [NAT]

For real a, define f_a(x)=x^4-2a*x^2+4x on the whole real line. What is the smallest integer a for which f_a has two distinct strict local minima?

**Answer format:** Numeric value; integer.

### Q43. [2 Marks] [MSQ]

A condition D has probability0.1. Two tests are independent conditional on whether D holds. Each test is positive with probability0.9 given D and0.2 given NOT D. Which statements are correct?

A. The two positive-result indicators are independent without conditioning.
B. The probability both tests are positive is0.117.
C. Given both positive, P(D)=9/13.
D. Given one positive, a second positive leaves P(D) unchanged.

### Q44. [2 Marks] [NAT]

An unweighted tree has edges AB, AC, BD, BE, CF, FG and FH. Distance is the number of edges on the unique path. How many unordered pairs of distinct vertices have distance equal to the tree's diameter, its largest vertex-pair distance?

**Answer format:** Integer.

### Q45. [2 Marks] [MSQ]

In tabular Boolean minimization, a dash represents an eliminated variable. A direct combination is allowed when two patterns have identical dash positions and differ in exactly one nondash bit. Which pairs can be directly combined in a single step?

A. 01-10 and 01-11
B. 01-10 and 011-0
C. 0--10 and 1--11
D. 0--10 and 1--10

### Q46. [2 Marks] [NAT]

Immediately before this fragment, x and y hold arbitrary values. Immediately afterward, both are needed. A compiler gives each of the names x,y,t one fixed register throughout the fragment. Two names that are simultaneously live must use different registers; live ranges may not be split and the assignments may not be rewritten.

```text
t = x
x = y
y = t
```

What is the minimum number of registers under these rules?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

An algorithm splits a size-n problem, where n is a power of two, into two half-size subproblems and then merges in Θ(n/log₂n) time for n≥4. Its running time satisfies T(n)=2T(n/2)+Θ(n/log₂n), with constant base cases at n≤2. What is the tight bound?

A. Θ(n)
B. Θ(n log log n)
C. Θ(n log n)
D. Θ(n²)

### Q48. [2 Marks] [NAT]

Two stations independently choose one of eight slots uniformly after a collision. If they collide again, they independently choose one of sixteen slots uniformly. What is the probability that both retries collide?

**Answer format:** Exact decimal.

### Q49. [2 Marks] [MCQ]

Let L consist of binary strings of length at least four whose fourth symbol from the right is 1. What is the number of states in a smallest complete DFA for L?

A. 5
B. 16
C. 17
D. 32

### Q50. [2 Marks] [MCQ]

Three processes P, Q and R use two initially empty pipes X and Y. Initially P owns X's write end and Y's read end; Q owns X's read end and Y's write end; R owns an additional copy of X's write end. No other descriptors for these pipes exist. A read-until-EOF operation returns only after all data has been consumed and every write descriptor for that pipe is closed. Pipe capacities exceed all data written here. All processes are eventually scheduled; there are no errors or signals.

- P writes one byte to X, closes its X writer, then reads Y until EOF, then terminates.
- Q reads X until EOF, then writes one byte to Y, closes its Y writer and terminates.
- R waits for P to terminate, then closes its X writer and terminates.

Which single change, with all other operations unchanged, is sufficient to ensure that all three processes terminate?

A. Increase the capacity of X.  
B. Have P wait for R to terminate immediately before P reads Y.  
C. Move R's close of the X writer to immediately before R waits for P.  
D. Have Q close its Y writer only after P terminates.

### Q51. [2 Marks] [NAT]

A program spends 40% of its original execution time in a component that can be accelerated. The remaining 60% is unchanged. To make the whole program exactly 25% faster, by what factor must that component be accelerated? Interpret “25% faster” as speedup 1.25.

**Answer format:** Integer factor.

### Q52. [2 Marks] [MSQ]

Let L={a^m b^n : m and n are positive integers, and m divides n}. For an arbitrary integer p≥2 choose w=a^p b^p. Consider every decomposition w=xyz satisfying |xy|≤p and |y|≥1. Which choices of pumping exponent i guarantee that xy^i z is outside L for every such decomposition?

A. i=0
B. i=1
C. i=2
D. i=p+2

### Q53. [2 Marks] [MCQ]

Table T(k,v) contains exactly these rows; NULL denotes the SQL null value, and duplicates are retained:
```text
(1,10), (1,NULL), (1,10), (2,NULL), (2,NULL), (3,5)
```
What rows, in any order, does the following standard SQL query return?
```sql
SELECT k, COUNT(*) AS n, COUNT(v) AS c
FROM T
GROUP BY k
HAVING COUNT(v) < COUNT(*) AND SUM(v) >= 10;
```

A. (1,3,2) only  
B. (1,3,2) and (2,2,0)  
C. (1,2,1) only  
D. No rows

### Q54. [2 Marks] [NAT]

A poset has elements a,b,c,d with a<b, a<c, b<d and c<d, and no other comparabilities except those forced by transitivity and reflexivity. How many linear extensions does it have?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

A completed depth-first search of a directed graph assigns discovery/finish times u:(2,9), v:(4,7), and w:(10,13), using one global clock. Which statements are correct?

A. v is a descendant of u in the DFS forest.
B. If edge v→u exists, it is a back edge.
C. If edge u→v exists, it must be a tree edge rather than a forward edge.
D. An edge v→w could be present with these timestamps in that completed DFS.

### Q56. [2 Marks] [MSQ]

Consider A=[[0,1],[1,1]]. An unpivoted factorization A=LU is sought with L unit lower triangular and U upper triangular. Which statements are correct?

A. Such an LU factorization exists because det(A) is nonzero.
B. Interchanging the rows allows a unit-lower/upper factorization.
C. A is invertible even though the stated unpivoted factorization is impossible.
D. The obstruction proves that the linear system Ax=b has no solution for some real b.

### Q57. [2 Marks] [MSQ]

A fully associative cache holds three blocks and starts empty. Compare FIFO replacement with LRU replacement for the block-reference sequence A,B,C,A,D,A. Every reference accesses one whole block, and every miss inserts it. Which statements are correct?

A. Both policies incur exactly four misses.
B. FIFO evicts A on the reference to D.
C. LRU evicts B on the reference to D.
D. The final reference to A misses under FIFO but hits under LRU.

### Q58. [2 Marks] [MSQ]

A reusable barrier for two threads uses shared integer count, initially 0, and shared Boolean sense, initially false. Each thread has its own local Boolean mySense, initially false. The following operations execute under sequential consistency; increment-and-test is atomic.

```text
mySense = NOT mySense;
if atomic_increment(count) == 2 {
    count = 0;
    sense = mySense;
} else {
    while sense != mySense { }
}
```

Only these two threads use the barrier, and each calls it sequentially once per phase. Which statements hold?

A. The sense change releases the waiting thread for the current phase.
B. The last arriving thread must reset count before publishing the changed sense.
C. A fast thread may complete the next barrier without the other thread reaching it.
D. Separate local mySense values distinguish consecutive barrier phases.

### Q59. [2 Marks] [MCQ]

A wait-die lock policy lets an older requesting transaction wait for a younger holder, but aborts a younger requester when the holder is older. Transactions T1,T2,T3 have timestamps 1,2,3, respectively (smaller is older). T2 holds x and T3 holds y. T1 requests x, then T2 requests y, then T3 requests a different item z held by T1. No locks are released before the last request. Which transaction is aborted by these requests?

A. T1 only
B. T2 only
C. T3 only
D. None

### Q60. [2 Marks] [NAT]

A router knows an undirected network with edges AB=1, AC=4, BC=2, BD=5, CD=1. Using complete link-state information, what is the shortest-path distance from A to D?

**Answer format:** Integer.

### Q61. [2 Marks] [MCQ]

A full-adder sum bit is implemented using a 4-to-1 mux with select bits a,b and remaining input c. Which data inputs (D0,D1,D2,D3) are correct?

A. (0,c,c,1)
B. (c,c′,c′,c)
C. (c′,c,c,c′)
D. (0,0,1,1)

### Q62. [2 Marks] [MCQ]

There are two instances of resource type R and one instance of S. P holds one R and requests S. Q holds S and requests one R. The other R is free. Requests can be granted using any available instance, and a process can finish and release its resources after its pending request is granted. Which statement is correct?

A. P and Q are necessarily deadlocked because their resource-type graph contains a cycle.
B. Granting the free R to Q permits Q to finish, after which P can finish.
C. No process can finish unless a held resource is preempted.
D. The free R is unusable because P already holds an R instance.

### Q63. [2 Marks] [MSQ]

A binary search tree stores distinct keys. An algorithm claims that checking only “each left child is smaller than its parent and each right child is larger” is sufficient to validate the whole BST. Which statements are correct?

A. The local condition is necessary.
B. The local condition is sufficient.
C. A tree with root10, left child5 and5's right child12 is a counterexample to sufficiency.
D. Propagating ancestor-imposed lower and upper bounds can detect the counterexample.

### Q64. [2 Marks] [MSQ]

A synchronous three-bit counter has transitions 0→1→2→3→4→5→0, and both unused states 6 and 7 transition to 0. Bits are q2q1q0 in binary. Which statements are correct?

A. From every initial bit pattern, the counter eventually enters the six-state cycle.  
B. An unused state remains unchanged until an external reset.  
C. On the steady cycle, q2 is 1 for one third of the clock intervals.  
D. On the steady cycle, q0 alternates at every clock edge.

### Q65. [2 Marks] [MSQ]

Consider exact integer arithmetic and the following code. The condition may be either true or false; no operations have hidden side effects.

```text
p = a+b
if condition:
    a = a+1
    t = a+b
else:
    t = p
z = a+b
```

Which statements hold for arbitrary initial a,b?

A. The final right-hand side can always be replaced by p.
B. The final right-hand side can always be replaced by t.
C. On both incoming paths, t equals the current a+b at the join.
D. The final right-hand side can always be replaced by p+1.

---

## ANSWER KEY — MOCK TEST 042

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MCQ | 1 | B |
| 3 | MSQ | 1 | A, C |
| 4 | MCQ | 1 | C |
| 5 | NAT | 1 | 32 |
| 6 | MCQ | 2 | B |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 25 |
| 9 | MSQ | 2 | A, C |
| 10 | MCQ | 2 | A |
| 11 | MCQ | 1 | B |
| 12 | NAT | 1 | 10 |
| 13 | NAT | 1 | 5 |
| 14 | MCQ | 1 | B |
| 15 | MCQ | 1 | A |
| 16 | MCQ | 1 | D |
| 17 | MSQ | 1 | A, D |
| 18 | MCQ | 1 | C |
| 19 | NAT | 1 | 3 |
| 20 | NAT | 1 | 7 |
| 21 | NAT | 1 | 31 |
| 22 | MCQ | 1 | B |
| 23 | NAT | 1 | 0.3 |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 3 |
| 26 | MCQ | 1 | B |
| 27 | NAT | 1 | 6 |
| 28 | MCQ | 1 | C |
| 29 | NAT | 1 | 4 |
| 30 | MCQ | 1 | B |
| 31 | MCQ | 1 | B |
| 32 | MSQ | 1 | A, B |
| 33 | MCQ | 1 | C |
| 34 | NAT | 1 | 1.5 |
| 35 | MCQ | 1 | A |
| 36 | NAT | 2 | 8 |
| 37 | NAT | 2 | 5 |
| 38 | NAT | 2 | 820 |
| 39 | MCQ | 2 | B |
| 40 | NAT | 2 | 37 |
| 41 | MSQ | 2 | A, B, D |
| 42 | NAT | 2 | 2 (exact) |
| 43 | MSQ | 2 | B, C |
| 44 | NAT | 2 | 4 |
| 45 | MSQ | 2 | A, D |
| 46 | NAT | 2 | 3 |
| 47 | MCQ | 2 | B |
| 48 | NAT | 2 | 0.0078125 |
| 49 | MCQ | 2 | B |
| 50 | MCQ | 2 | C |
| 51 | NAT | 2 | 2 |
| 52 | MSQ | 2 | C, D |
| 53 | MCQ | 2 | A |
| 54 | NAT | 2 | 2 |
| 55 | MSQ | 2 | A, B |
| 56 | MSQ | 2 | B, C |
| 57 | MSQ | 2 | B, C, D |
| 58 | MSQ | 2 | A, B, D |
| 59 | MCQ | 2 | C |
| 60 | NAT | 2 | 4 |
| 61 | MCQ | 2 | B |
| 62 | MCQ | 2 | B |
| 63 | MSQ | 2 | A, C, D |
| 64 | MSQ | 2 | A, C, D |
| 65 | MSQ | 2 | B, C |
