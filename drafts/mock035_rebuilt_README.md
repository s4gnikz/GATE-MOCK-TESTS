# GATE CS 2027 — Full-Length Mock Test 035

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes 15 marks, Engineering Mathematics 13, and core Computer Science 72.

MCQs have exactly one correct option. For MSQs select all and only the correct options; there is no partial credit. Incorrect MCQs lose one third of their marks. MSQ and NAT questions have no negative marking. Unattempted questions receive zero. Follow the stated NAT precision. The answer key follows Question 65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“Complaints about bus delays fell after an online complaint form was introduced. During the same period, submitting a complaint began to require an account, and the number of completed complaint submissions fell. No independent measurements of bus arrival times were collected.” Which conclusion is best supported?

A. Buses necessarily became more punctual.
B. Every person who stopped submitting complaints encountered punctual buses.
C. The complaint count alone cannot distinguish improved punctuality from reduced reporting.
D. Requiring an account necessarily made buses less punctual.

### Q2. [1 Mark] [NAT]

Six distinct people A,B,C,D,E,F sit around a circular table with six equally spaced seats. Arrangements differing only by rotation are identical; mirror images are distinct. A and B must sit opposite one another, and C and D must be adjacent. How many arrangements satisfy both restrictions?

**Answer format:** Exact integer.

### Q3. [1 Mark] [NAT]

A report lists the following mutually exclusive journey categories. A journey is chosen uniformly from all recorded journeys. What is the probability that it is a delayed journey lasting more than 20 minutes?

| Duration | Total journeys | Delayed journeys |
|---|---:|---:|
| At most 20 minutes | 40 | 6 |
| More than 20, at most 40 minutes | 35 | 14 |
| More than 40 minutes | 25 | 10 |

**Answer format:** Exact decimal.

### Q4. [1 Mark] [NAT]

A thin square sheet occupies 0≤x≤4, 0≤y≤4. Fold the right half onto the left along x=2, then the top half onto the bottom along y=2. From the resulting folded square, remove the entire horizontal strip 0≤x≤2, 0.5<y<1 through every layer. After unfolding, how many connected pieces of paper remain? The cuts extend fully to both side edges of the folded square.

**Answer format:** Exact integer.

### Q5. [1 Mark] [MSQ]

Four events occur once each: filing F, inspection I, approval A, and publication P. Filing precedes both inspection and approval. Publication follows both inspection and approval. No order between inspection and approval is specified. Which conclusions necessarily follow?

A. Filing is the first of these four events.
B. Inspection immediately precedes approval.
C. Publication is the last of these four events.
D. Exactly two orders of these four events satisfy the conditions.

### Q6. [2 Marks] [NAT]

Three independent fair six-sided dice are rolled. It is known that exactly two dice have the same value and that the largest of the three values is 5. What is the conditional probability that the sum of the three values is odd?

**Answer format:** Exact decimal.

### Q7. [2 Marks] [MCQ]

“The panel sought a disinterested assessor: the assessor needed to examine the evidence carefully but have no financial stake in the outcome.” Which replacement best preserves the intended meaning of “disinterested” here?

A. indifferent to the evidence
B. impartial regarding the outcome
C. inexperienced in assessment
D. certain that the proposal would fail

### Q8. [2 Marks] [NAT]

A positive real number x satisfies log2(x)+log4(x)=log2(7x−36). Determine the sum of all real values of x satisfying the equation. The logarithms must all be defined.

**Answer format:** Exact integer.

### Q9. [2 Marks] [MSQ]

For a finite list of integers, operation R reverses the list, and operation N negates every entry without changing the order. A student claims that applying R then N always gives the same list as applying N then R. Which statements hold?

A. Checking the claim on one list of length three proves it for lists of every length.
B. The claim holds because each final position contains the negative of the same original entry under either order.
C. Applying the combined operation twice restores every original list.
D. The claim implies that reversing a list always leaves it unchanged.

### Q10. [2 Marks] [NAT]

Four unit cubes occupy grid positions (0,0,0), (1,0,0), (1,1,0), and (1,1,1). A position (i,j,k) denotes the cube [i,i+1]×[j,j+1]×[k,k+1]. What is the total exposed surface area of their union, in square units? Shared full faces are internal; contact along an edge does not hide any face area.

**Answer format:** Exact integer.


---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

For x≠0, define f(x)=(|x|−x)/x, and set f(0)=k. Which statement holds?

A. k=0 makes f continuous at 0.
B. k=−2 makes f differentiable at 0.
C. No real k makes f continuous at 0.
D. Every real k makes f continuous at 0.

### Q12. [1 Mark] [NAT]

A DFA has states0,1,2,3, start state0 and only accepting state0. On symbol a it moves from state i to(i+1) mod4; on symbol b it moves to(i+2) mod4. How many length-three strings over {a,b} are accepted?

**Answer format:** Exact integer.

### Q13. [1 Mark] [NAT]

A random variable X takes values 0,1,2 with probabilities1/4,1/2,1/4. Define Y=1 if X=1, and Y=0 otherwise. What is the covariance Cov(X,Y)?

**Answer format:** Exact integer.

### Q14. [1 Mark] [MSQ]

Functions f:A→B and g:B→A satisfy g composed with f=identity on A. No finiteness assumption is made. Which statements necessarily hold?

A. f is injective.
B. f is surjective onto B.
C. g is surjective onto A.
D. f composed with g=identity on B.

### Q15. [1 Mark] [NAT]

A binary floating-point system has four significant bits, including the leading1, and supports normalized positive numbers of the form1.b1b2b3×2^e. How many representable numbers lie in the closed interval[1.75,2.5]? Assume all needed exponents exist.

**Answer format:** Exact integer.

### Q16. [1 Mark] [MSQ]

A table T(id,code) declares id as its primary key and code as NOT NULL, but code is not declared UNIQUE. Initially it contains(1,'X'),(2,'Y'). Which individual insertions, each considered independently on this original table, satisfy both stated constraints?

A. (3,'X')
B. (2,'Z')
C. (4,NULL)
D. (4,'Z')

### Q17. [1 Mark] [MCQ]

Relation R(A,B,C) has exactly the functional dependencies implied by AB→C and C→B. Assuming atomic attribute values, which classification is correct?

A. R is in BCNF because every attribute belongs to a key.
B. R is in3NF but not BCNF.
C. R violates2NF because C→B has a single-attribute determinant.
D. A alone is a candidate key.

### Q18. [1 Mark] [NAT]

A zero-indexed array A contains the permutation [2,0,4,1,3]. A separate array B of length five is filled by executing B[A[i]]=i for i=0,1,2,3,4. What is the value of B[B[0]] afterward?

**Answer format:** Exact integer.

### Q19. [1 Mark] [NAT]

A TCP sender's next unsent byte has sequence number5000. It receives a cumulative ACK with acknowledgment number4200 and advertised window600 bytes. Assume no sequence-number wraparound and that the congestion window imposes no tighter restriction. How many new bytes may it send immediately, without retransmitting already sent bytes?

**Answer format:** Exact integer.

### Q20. [1 Mark] [NAT]

A real2×2 matrix A has trace5 and determinant6. What is trace(A²)?

**Answer format:** Exact integer.

### Q21. [1 Mark] [MSQ]

Boolean function F(x,y,z)=(x OR y) AND(NOT x OR z). Which statements hold?

A. If x=0, then F=y.
B. If x=1, then F=z.
C. F always equals y AND z.
D. F always equals x XOR y XOR z.

### Q22. [1 Mark] [MCQ]

A device sets a level-triggered interrupt request while its completion-status bit is 1. An interrupt handler acknowledges the CPU interrupt controller but leaves the device status bit unchanged. Assuming the controller permits subsequent delivery, what behavior is possible after return from the handler?

A. Another interrupt is delivered because the device still asserts its request.
B. The device's status bit necessarily clears when the CPU acknowledges its controller.
C. The device's completed transfer is automatically undone.
D. The interrupt line necessarily changes into an edge-triggered source.

### Q23. [1 Mark] [NAT]

A singly linked list is A→B→C→D→NULL. Pointer p initially refers to A and pointer q initially refers to C. Execute these assignments in order:

```text
p.next = q.next;
q.next = p;
```

How many distinct nodes are reachable by following next pointers starting from q, counting q itself?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MSQ]

Grammar G has start symbol S and productions S→aSb | aS | epsilon. Which strings are generated?

A. aab
B. abb
C. aaabb
D. ba

### Q25. [1 Mark] [NAT]

A scheduler uses shortest remaining processing time, with zero switching cost. Job A arrives at 0 with burst7, B at 2 with burst2, and C at 3 with burst1. A tie retains the currently running job. At what time does A complete?

**Answer format:** Exact integer.

### Q26. [1 Mark] [MCQ]

For n≥2, consider the following pseudocode, with constant-time integer operations:

```text
j=1;
for i=1 to n:
    while j<=i:
        j=2*j;
```

What is the tight asymptotic running time?

A. Theta(log n)
B. Theta(n log n)
C. Theta(n)
D. Theta(n²)

### Q27. [1 Mark] [MSQ]

A connected TCP socket receives the peer's orderly write shutdown after all previously transmitted bytes have arrived. The local application has read all those bytes. No reset or error occurs. Which statements hold?

A. A subsequent positive-length receive can return0 to indicate end of stream.
B. The local application must interpret that0 return as a received zero-valued data byte.
C. The local endpoint may still send data if its own write direction remains open and the peer continues receiving.
D. TCP necessarily delivers a separate application record for the shutdown.

### Q28. [1 Mark] [NAT]

A stack stores pairs(value,current minimum). Pushing x stores(x,min(x,previous minimum)); on an empty stack it stores(x,x). Execute push5,push2,push2,pop,push4,pop,pop. What minimum is stored in the final top pair?

**Answer format:** Exact integer.

### Q29. [1 Mark] [NAT]

A fixed-length file uses unspanned records of 90 bytes and blocks of 512 bytes, with no headers. It currently contains 12 records packed into the fewest possible blocks. How many additional records can be inserted without allocating another block, if records may be rearranged within the allocated blocks?

**Answer format:** Exact integer.

### Q30. [1 Mark] [MCQ]

A greedy coin algorithm repeatedly takes the largest denomination not exceeding the remaining amount. With denominations1,4,6 and target8, how many more coins does greedy use than an optimal solution?

A. 0
B. 1
C. 2
D. 3

### Q31. [1 Mark] [NAT]

A differentiable function f on[0,2] has f(0)=1 and f(2)=7, and f'(x)≤3 everywhere on(0,2). What is f(1)?

**Answer format:** Exact integer.

### Q32. [1 Mark] [MSQ]

Procedure outer contains local variable x and returns an inner function that later reads x. The language permits that returned function to be called after outer returns. Which statements hold for a correct implementation?

A. The lifetime of captured x must extend beyond outer's return when the returned function still needs it.
B. A pointer into an already reclaimed stack frame always suffices to implement the returned function.
C. An environment stored outside the reclaimed stack frame can preserve x.
D. The inner function must read a new unrelated variable named x from its caller's frame.

### Q33. [1 Mark] [NAT]

A stack-machine translation evaluates postfix expression a b + c d − * using PUSH for operands and binary operators that pop two values and push one result. What is the maximum operand-stack depth, starting empty?

**Answer format:** Exact integer.

### Q34. [1 Mark] [MCQ]

A processor issues instructions out of order but commits their architectural results in program order using a reorder buffer. Which mechanism chiefly prevents a younger completed instruction from exposing its architectural result before an older faulting instruction is resolved?

A. In-order commit from the reorder buffer.
B. Issuing every ready instruction as soon as possible.
C. Increasing the number of execution units.
D. Predicting every branch as taken.

### Q35. [1 Mark] [NAT]

A disk scheduler selects the pending request requiring the least head movement. The head begins at 50. Requests at 45 and80 are pending at time0. After servicing45, but before the next selection, a new request at 44 arrives. No other arrivals occur. What total head movement occurs before all three requests finish?

**Answer format:** Exact integer.

### Q36. [2 Marks] [NAT]

An urn initially contains one red and one blue ball. Draw a ball uniformly, replace it, and add one extra ball of the same color. Then draw a second ball uniformly from the three balls now present. Given that the second ball is red, what is the probability that the first was blue?

**Answer format:** Decimal rounded to four places.

### Q37. [2 Marks] [NAT]

A buddy allocator manages one aligned1024-byte region and rounds each request up to a power of two, with no headers. It allocates A=200 bytes at address0, B=200 bytes at address256, and C=400 bytes at address512. After freeing A and B, what is the largest new single request, in bytes, that can be satisfied without freeing C?

**Answer format:** Exact integer.

### Q38. [2 Marks] [NAT]

A three-variable Boolean function has1-minterms {0,2,6}, don't-care minterms {4}, and0-minterms {1,3,5,7}. A is the most significant bit and C the least significant. After obtaining a minimum-literal SOP, what value does that implementation assign to minterm 4?

**Answer format:** Exact integer,0 or1.

### Q39. [2 Marks] [NAT]

A byte-addressed machine loads a32-bit word using effective address Rbase+4×Rindex−8. Initially Rbase=100 and Rindex=3. Memory bytes at addresses104 through111 are 01,02,03,04,05,06,07,08 in hexadecimal. The machine is little-endian. What is the decimal value of the least significant16 bits of the loaded word?

**Answer format:** Exact integer.

### Q40. [2 Marks] [MSQ]

A client has a fresh cached DNS address for host h and an HTTP cache entry for a resource on h. The HTTP entry is stale but has an entity tag. Which statements hold?

A. Revalidating the HTTP entry need not require a fresh DNS query.
B. A conditional request can allow the server to confirm reuse of the cached body without resending that body.
C. A valid DNS cache entry guarantees that every cached HTTP resource for h is fresh.
D. Receiving an HTTP response automatically renews the DNS record's TTL.

### Q41. [2 Marks] [NAT]

An application sends600 bytes over UDP. UDP adds8 bytes, IPv4 adds20 bytes with no options, and a link protocol adds18 bytes per frame. The link permits at most 400 bytes of IP packet per frame. The sender creates IPv4 fragments with the largest legal payloads, including the UDP header in the original IP payload. How many bytes in total are transmitted in the link frames? Ignore preambles and interframe gaps.

**Answer format:** Exact integer.

### Q42. [2 Marks] [MSQ]

In a tabular Boolean minimization, a dash in a four-bit cube denotes a free variable. The ON-set is {0,1,2,3,8,9}, the don't-care set is {10}, and all remaining minterms are OFF. Which operations are valid? A combined cube must contain no OFF minterm.

A. Combine 000- and 001- to obtain 00--.
B. Combine 00-- and 100- to obtain -0--.
C. Combine 00-0 and 10-0 to obtain -0-0.
D. Combine -00- and -010 to obtain -0--.
### Q43. [2 Marks] [NAT]

A B+ tree root has two leaf children, containing[2,5] and[8,11]. Leaves hold at most 3 keys. Inserting into a full leaf first forms four sorted keys, then splits them into two leaves with two keys each. The first key of the new right leaf is copied to the parent. Internal nodes can have at most 3 children. Insert 6, then7. How many keys are in the root afterward?

**Answer format:** Exact integer.

### Q44. [2 Marks] [NAT]

A path graph has vertex weights 4,7,5,6,3 in order. Select a set of vertices with no two adjacent, maximizing the total weight. How many different vertex sets attain the optimum? Vertices are distinguished by their positions, even if weights were equal.

**Answer format:** Exact integer.

### Q45. [2 Marks] [MSQ]

A write-ahead logging system uses undo and redo records. A transaction's commit record is forced to stable storage before success is reported, but its changed data pages need not yet be on disk. Which statements hold?

A. Redo may be required after a crash for a transaction already reported committed.
B. A dirty data page may be written before its corresponding update log record is durable without violating write-ahead logging.
C. Forcing the commit record can ensure earlier records in the same sequential log are durable as well.
D. A committed transaction must be undone merely because its data page was not flushed before the crash.

### Q46. [2 Marks] [NAT]

Order the divisors of 30 by divisibility. How many maximal chains run from 1 to 30? A chain is maximal when no further divisor can be inserted between successive elements.

**Answer format:** Exact integer.

### Q47. [2 Marks] [NAT]

A rooted tree has root r with children a,b. Node a has children c,d, and b has child e; c,d,e are leaves. A vertex's depth is its edge distance from the root. If the same undirected tree is rerooted at c, by how much does the sum of all six vertex depths increase?

**Answer format:** Exact integer.

### Q48. [2 Marks] [MCQ]

A PDA recognizing balanced parentheses pushes on '(' and pops on ')', rejecting a pop from an empty stack; it accepts only with empty stack after all input. A proposed modification accepts immediately whenever the stack first becomes empty after consuming at least one symbol, even if input remains. Which input demonstrates that the modification accepts a string rejected by the original?

A. (())
B. ()()
C. ())
D. ((

### Q49. [2 Marks] [NAT]

An unsigned4-bit comparator is implemented by comparing the two most significant bits first, then the two least significant bits only if the first pair is equal. Over all256 equally likely ordered input pairs(A,B), how many require the second comparison?

**Answer format:** Exact integer.

### Q50. [2 Marks] [MSQ]

In an expression language, evaluating an operand may have side effects; && and || evaluate left to right and short-circuit. Values are Boolean. Which rewrites preserve both returned value and operand side effects in every execution?

A. false && f() → false
B. f() && false → false
C. true || f() → true
D. f() || true → true

### Q51. [2 Marks] [NAT]

An8-bit ALU adds unsigned inputs200 and100 and retains only eight result bits. Let C be its carry-out bit. Interpret the retained result as a signed two's-complement integer R. What is R+256C?

**Answer format:** Exact integer.

### Q52. [2 Marks] [MSQ]

For a language L, define its prefix set Pref(L)={u: there exists v such that uv belongs to L}. Which statements hold?

A. If L is regular, Pref(L) is regular.
B. For a DFA of L, marking all states from which an accepting state is reachable as accepting recognizes Pref(L).
C. Pref(L) always equals L.
D. If L is empty, Pref(L) contains epsilon.

### Q53. [2 Marks] [NAT]

A comparison algorithm recursively divides an array of n=32 elements into equal halves. At every non-leaf call it first solves both halves and then compares every element in the left half with every element in the right half, once per pair. A one-element call makes no comparisons. How many comparisons occur in total?

**Answer format:** Exact integer.

### Q54. [2 Marks] [NAT]

A microprogram has a two-entry return stack, initially empty. Instruction CALL pushes the following address and branches; RETURN pops and branches to that address. Starting at address0, execute:

```text
0: CALL 4
1: HALT
4: CALL 8
5: RETURN
8: RETURN
```

Every listed microinstruction takes one cycle. How many cycles elapse through HALT?

**Answer format:** Exact integer.

### Q55. [2 Marks] [NAT]

Insert keys8,4,12,2,6,10,14,5 into an initially empty BST without rotations. Delete8 by replacing its key with its inorder successor and deleting that successor's original node. What is the edge distance from the new root to key5 afterward?

**Answer format:** Exact integer.

### Q56. [2 Marks] [MSQ]

A compiler analyzes the loop below using a non-relational constant lattice, meeting different constants as “nonconstant.” It does not unroll the loop or track relationships between variables. Input n is an arbitrary nonnegative integer.

```text
x=0; y=0;
repeat n times:
    x=x+1;
    y=y+1;
z=x-y;
```

Which statements hold?

A. Concrete execution always sets z=0.
B. The stated abstraction necessarily retains x=y at the loop exit.
C. Joining the entry values with the first-iteration values makes both x and y nonconstant.
D. The program can set z=1 for some nonnegative n.

### Q57. [2 Marks] [NAT]

At the exit of the following straight-line block, only r is live. Assignments are evaluated sequentially.

```text
a=b+c;
d=a+e;
a=f;
r=d+a;
```

How many distinct variables are live at block entry?

**Answer format:** Exact integer.

### Q58. [2 Marks] [NAT]

A min-heap contains the array[1,3,2,8,7,4,5]. Replace its root by 9, then restore heap order by repeatedly swapping the current key with its smaller child while that child is smaller. How many swaps occur?

**Answer format:** Exact integer.

### Q59. [2 Marks] [MCQ]

Transactions have timestamps T1=10,T2=20,T3=30, with lower meaning older. A wait-die lock manager lets an older requester wait for a younger holder but aborts a younger requester asking for an older holder's lock. T2 holds X, T3 requests X, then T1 requests X. What happens to these two requests, assuming T2 still holds X?

A. Both requesters wait.
B. T3 aborts and T1 waits.
C. T3 waits and T1 aborts.
D. Both requesters abort.

### Q60. [2 Marks] [NAT]

Two packets of 1000 bits each traverse two store-and-forward links. The first link transmits at 1000 bits/s and the second at 2000 bits/s. Both packets are initially available at the source. There is no propagation or processing delay. How many seconds after transmission begins does the second packet finish arriving at the destination?

**Answer format:** Exact decimal.

### Q61. [2 Marks] [NAT]

For a matrix A, pivoted elimination gives PA=LU, where P swaps rows1 and2,

```text
L=[1 0; 2 1],    U=[1 3; 0 2].
```

Solve Ax=b for b=(7,2)ᵀ. What is x1?

**Answer format:** Exact decimal.

### Q62. [2 Marks] [MSQ]

Let L={a^m b^n : m and n are positive integers, and m divides n}. For an arbitrary integer p≥2 choose w=a^p b^p. Consider every decomposition w=xyz satisfying |xy|≤p and |y|≥1. Which choices of pumping exponent i guarantee that xy^i z is outside L for every such decomposition?

A. i=0
B. i=1
C. i=2
D. i=p+2
### Q63. [2 Marks] [NAT]

A TLB lookup takes 2 ns and each physical memory access takes 50 ns, with no overlap. The page table has two levels in memory. A TLB hit needs only the final data access; a miss needs two page-table accesses followed by the data access. All pages are resident. If the TLB hit probability is 0.9, what is the mean access time in ns?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

Let I be the integral from 0 to 1 of x/(1+x²) dx, and J the integral from 0 to 1 of x³/(1+x²) dx. What is I+J?

**Answer format:** Exact decimal.

### Q65. [2 Marks] [NAT]

An undirected graph has edges sa,sb,ac,bc,cd,ad. BFS from s records distances and counts the number of shortest paths to each vertex. What is the number of shortest s-to-d paths?

**Answer format:** Exact integer.


---

## ANSWER KEY — MOCK TEST 035

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 8 |
| 3 | NAT | 1 | 0.24 |
| 4 | NAT | 1 | 3 |
| 5 | MSQ | 1 | A, C, D |
| 6 | NAT | 2 | 0.75 |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 45 |
| 9 | MSQ | 2 | B, C |
| 10 | NAT | 2 | 18 |
| 11 | MCQ | 1 | C |
| 12 | NAT | 1 | 3 |
| 13 | NAT | 1 | 0 |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 5 |
| 16 | MSQ | 1 | A, D |
| 17 | MCQ | 1 | B |
| 18 | NAT | 1 | 3 |
| 19 | NAT | 1 | 0 |
| 20 | NAT | 1 | 13 |
| 21 | MSQ | 1 | A, B |
| 22 | MCQ | 1 | A |
| 23 | NAT | 1 | 3 |
| 24 | MSQ | 1 | A, C |
| 25 | NAT | 1 | 10 |
| 26 | MCQ | 1 | C |
| 27 | MSQ | 1 | A, C |
| 28 | NAT | 1 | 5 |
| 29 | NAT | 1 | 3 |
| 30 | MCQ | 1 | B |
| 31 | NAT | 1 | 4 |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 3 |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 42 |
| 36 | NAT | 2 | 0.3333 (accepted range 0.33325–0.33335) |
| 37 | NAT | 2 | 512 |
| 38 | NAT | 2 | 1 |
| 39 | NAT | 2 | 513 |
| 40 | MSQ | 2 | A, B |
| 41 | NAT | 2 | 684 |
| 42 | MSQ | 2 | A, C |
| 43 | NAT | 2 | 2 |
| 44 | NAT | 2 | 1 |
| 45 | MSQ | 2 | A, C |
| 46 | NAT | 2 | 6 |
| 47 | NAT | 2 | 4 |
| 48 | MCQ | 2 | C |
| 49 | NAT | 2 | 64 |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 300 |
| 52 | MSQ | 2 | A, B |
| 53 | NAT | 2 | 496 |
| 54 | NAT | 2 | 5 |
| 55 | NAT | 2 | 3 |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 4 |
| 58 | NAT | 2 | 2 |
| 59 | MCQ | 2 | B |
| 60 | NAT | 2 | 2.5 |
| 61 | NAT | 2 | -2.5 |
| 62 | MSQ | 2 | C, D |
| 63 | NAT | 2 | 62 |
| 64 | NAT | 2 | 0.5 |
| 65 | NAT | 2 | 1 |


