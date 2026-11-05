# GATE CS 2027 — Full-Length Mock Test 089

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

Choose the sentence that unambiguously states that the technician, rather than the instrument, was in a hurry.

A. Being in a hurry, the instrument was checked by the technician.
B. The instrument was checked in a hurry that belonged to the technician.
C. In a hurry, the technician checked the instrument.
D. The technician checked the instrument that was in a hurry.

### Q2. [1 Mark] [NAT]

An article costs a seller ₹80 and is marked at ₹100. It is sold at a 10% discount on the marked price. What percentage of the actual selling price is profit?

**Answer format:** Percentage rounded to two decimal places.

### Q3. [1 Mark] [MCQ]

Exactly one of statements P and Q is true. P says “The key is in drawer 1.” Q says “The key is not in drawer 2.” The key is in exactly one of drawers 1,2,3. Where is it?

A. Drawer 1
B. Drawer 2
C. Drawer 3
D. The premises permit all three drawers.

### Q4. [1 Mark] [MCQ]

A triangular tile has labelled vertices P=(1,1), Q=(3,1), R=(1,2) in a Cartesian plane. First reflect the tile in the x-axis. Then rotate the result clockwise by 90 degrees about the origin. Which ordered triple gives the final positions of P, Q and R?

A. ((-1,-1),(-1,-3),(-2,-1))  
B. ((1,1),(1,3),(2,1))  
C. ((1,-1),(1,-3),(2,-1))  
D. ((-1,1),(-1,3),(-2,1))

### Q5. [1 Mark] [MCQ]

After a library extended its evening hours, the number of evening visits increased, while total weekly visits remained unchanged. A report concludes that the extension attracted additional weekly visitors. Which criticism is best supported by the information given?

A. Evening visits cannot increase unless weekly visits increase.  
B. Some visits may have shifted from daytime to evening, and visit counts do not identify distinct visitors.  
C. The extension must have reduced the number of distinct visitors.  
D. Every evening visitor previously visited during daytime.

### Q6. [2 Marks] [NAT]

A committee of four is selected from five engineers and three designers. It must contain at least two engineers and at least one designer. How many committees are possible?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A firm reports revenue and cost as follows: year1 revenue120, cost90; year2 revenue150, cost120, in the same units. Profit margin is profit divided by revenue. By how many percentage points did the margin decrease from year1 to year2?

**Answer format:** Exact number of percentage points.

### Q8. [2 Marks] [NAT]

A rectangular sheet spans0≤x≤8 and0≤y≤2. Fold the left half onto the right along x=4. Then fold the part of that packet with6≤x≤8 onto4≤x≤6 along x=6. Cut straight through all layers along x=5 for the full height of the folded packet. After unfolding and separating along the cuts, how many connected pieces remain? Creases alone do not separate pieces.

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

Four events occurred once each: calibration C, inspection I, trial T, and release R. Calibration preceded trial; inspection immediately followed calibration; release occurred after inspection but before trial. Which order is consistent?

A. C,I,R,T
B. C,R,I,T
C. I,C,R,T
D. C,I,T,R

### Q10. [2 Marks] [NAT]

Two people independently choose a uniformly random three-element subset of {1,2,3,4,5}. Given that their chosen subsets are not identical, what is the probability that their union contains all five elements? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

On the set {1,2,3,6,12}, order elements by divisibility. What is the join (least upper bound) of2 and3 in this partially ordered set?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

For three Boolean variables a,b,c, the on-set is {000,001} and the don't-care set is {010,011}; every other input is in the off-set. Among prime implicants that cover at least one on-set input, how many literals does the largest such cube contain?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

SQL table A(k) contains1,2,NULL; B(k) contains2,NULL. Compare the counts returned by these predicates on rows of A: NOT EXISTS(SELECT 1 FROM B WHERE B.k=A.k), and A.k NOT IN(SELECT k FROM B). Using ordinary SQL three-valued logic, what is the first count minus the second?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

Initially one single-threaded process executes the following pseudocode. Every fork succeeds; a child returns0 from fork, and the parent returns a positive value. No process exits early.

```text
x = fork();
if x == 0 {
    fork();
} else {
    fork();
    fork();
}
```

How many processes, including the original, reach the end?

**Answer format:** Exact integer.

### Q15. [1 Mark] [NAT]

A=LU, where L is unit lower triangular and U is upper triangular with diagonal entries2,−3,4. No row permutation is involved. What is det(A)?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A directed graph on n=6 vertices is represented by six adjacency lists. Self-loops are allowed, and no ordered pair occurs more than once. The sum of all outdegrees is11 and exactly three edges are self-loops. What is the sum of all indegrees?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

A connected TCP socket receives the peer's orderly write shutdown after all previously transmitted bytes have arrived. The local application has read all those bytes. No reset or error occurs. Which statements hold?

A. A subsequent positive-length receive can return0 to indicate end of stream.
B. The local application must interpret that0 return as a received zero-valued data byte.
C. The local endpoint may still send data if its own write direction remains open and the peer continues receiving.
D. TCP necessarily delivers a separate application record for the shutdown.

### Q18. [1 Mark] [NAT]

A three-input majority gate outputs one exactly when at least two inputs are one. Its input is currently 011. Among the three possible single-input-bit flips, how many change the gate's output?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A control store contains 512 microinstructions, each 40 bits wide. How many bits are needed to address a microinstruction within that store?

**Answer format:** Integer.

### Q20. [1 Mark] [MCQ]

Two processes share a memory region but use no synchronization. Why does shared-memory IPC alone not guarantee a correct producer–consumer protocol?

A. Shared memory cannot store more than one byte.
B. Visibility of common storage does not by itself ensure correct ordering or mutual exclusion.
C. The two processes necessarily have identical register values.
D. Sharing storage automatically serializes all accesses.

### Q21. [1 Mark] [NAT]

A directed graph has edges s→a of weight0, a→b of weight0, b→t of weight4, and s→t of weight5. A programmer adds the same positive integer c to every edge weight before finding a shortest path. What is the smallest c for which the direct edge s→t becomes strictly cheaper than the three-edge route?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A real upper-triangular 3×3 matrix A has diagonal entries 1,2,3; entries above the diagonal are arbitrary. Find det(A²−A−I), where I is the identity.

**Answer format:** Integer.

### Q23. [1 Mark] [MCQ]

SQL table L(id) contains 1,2 and table R(id,v) contains (1,0),(1,5). What rows are returned by the following query, using ordinary SQL bag semantics?

```sql
SELECT L.id, R.v
FROM L LEFT JOIN R ON L.id=R.id AND R.v>0;
```

A. (1,5) only
B. (1,0),(1,5),(2,NULL)
C. (1,5),(2,NULL)
D. (1,NULL),(2,NULL)

### Q24. [1 Mark] [MCQ]

An algorithm outputs every unordered pair of distinct elements from an n-element input, with one constant-time operation per emitted pair. What is the tight asymptotic lower bound arising from output size alone?

A. Ω(log n)
B. Ω(n)
C. Ω(n log n)
D. Ω(n²)

### Q25. [1 Mark] [NAT]

Five nonnegative real observations have total 20. What is the greatest possible median? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q26. [1 Mark] [MSQ]

In a group, distinct nonidentity elements a,b satisfy a²=b²=e. Which statements are correct?

A. (ab)^(−1)=ba.
B. The group must be abelian.
C. If a and b commute, ab has order2.
D. If ab has order2, a and b commute.

### Q27. [1 Mark] [NAT]

An NFA has states s,a,b,c, start state s, and only c accepting. Its transitions are s —ε→ a, a —ε→ b, b —0→ b, b —1→ c, and c —1→ c. There are no other transitions. How many strings of length three are accepted?

**Answer format:** Integer.

### Q28. [1 Mark] [MSQ]

A browser already knows a server's IP address and establishes a new TCP connection to request an HTTP resource. The server responds with a redirection to a different hostname. Which statements hold?

A. The initial request need not perform a new DNS query if its address is already usable.
B. The redirect guarantees that the original server's IP address is valid for the new hostname.
C. Following the redirect may require resolving the new hostname.
D. An HTTP redirect changes the destination address of the already transmitted request.

### Q29. [1 Mark] [NAT]

A memory system must contain1024 words of16 bits each. Available chips each contain256 words of8 bits. How many chips are required, assuming ordinary depth and width expansion without redundancy?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

Assume conventional C semantics and representable integer values. What is the final value of a[1]?

```c
int a[3] = {1,2,3};
int *p = a;
int x = *p++;
*p += x;
```

**Answer format:** Integer.

### Q31. [1 Mark] [MCQ]

A lexical analyzer distinguishes an identifier token from a symbol-table entry. Which statement is correct?

A. Every occurrence of the same identifier spelling must create a permanently distinct name entry regardless of scope or implementation.
B. Token recognition and name binding are different tasks; returning an identifier token does not alone determine which declaration it denotes.
C. Recognizing a token proves that the entire program is type-correct.
D. Whitespace must always be emitted as an identifier token.

### Q32. [1 Mark] [NAT]

For the augmented grammar S'→S, S→CC, C→cC | d, let I0 be the LR(0) closure of S'→·S. How many items are in GOTO(I0,C), including closure items?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

A recursive function is mathematically defined by f(0)=0, f(1)=1 and f(n)=f(n−1)−f(n−2) for n≥2. Find f(2027).

**Answer format:** Integer, possibly negative.

### Q34. [1 Mark] [NAT]

R(x,y) contains (1,a),(1,b),(2,a),(3,c), and S contains a,b. Over these domains, how many x values satisfy `(∃y R(x,y)) AND (∀z (R(x,z) → S(z)))`?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

For the grammar S→AB, A→aA | ε, B→aB | ε, how many distinct parse trees generate the terminal string aaa?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

How many permutations of six labelled elements have only even-length cycles in their disjoint-cycle decomposition?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

A linear-probing hash table uses EMPTY for never-used slots and DELETED for tombstones. Searches stop at EMPTY, but continue past DELETED. Which claims hold?

A. Replacing a deleted occupied slot by EMPTY can make another existing key unreachable by search.
B. An insertion can remember the first DELETED slot, continue searching for an existing copy of its key, then reuse that slot if the key is absent.
C. A search can always stop at DELETED because it no longer contains a key.
D. Tombstones can increase the number of probes in an unsuccessful search.

### Q38. [2 Marks] [MSQ]

A deterministic PDA has a designated set of final states. Acceptance by final state requires all input to be consumed, and the stack may remain nonempty. Which assertions are valid?

A. Every language accepted by such a machine is context-free.
B. Every context-free language can be accepted by some deterministic PDA.
C. A nondeterministic PDA can accept the same language using empty-stack acceptance instead.
D. Simply declaring all states final always preserves the accepted language.

### Q39. [2 Marks] [MSQ]

Over alphabet {a,b,c}, define

```text
L = { a^i b^j c^k : i,j,k >= 0 and (i=j or j=k) }
R = { a^i b^j c^k : i,j,k >= 0 and j<=2 }
S = { a^n b^m c^n : n,m >= 0 }.
```

All exponents are integers, and L minus R denotes set difference. Which statements are correct?

A. L intersect R is regular.  
B. L minus R is regular.  
C. L minus R is context-free.  
D. L intersect S is context-free.

### Q40. [2 Marks] [NAT]

A program spends 40% of its original execution time in a component that can be accelerated. The remaining 60% is unchanged. To make the whole program exactly 25% faster, by what factor must that component be accelerated? Interpret “25% faster” as speedup 1.25.

**Answer format:** Integer factor.

### Q41. [2 Marks] [NAT]

Table A(k) contains1,1,2 and table B(k) contains1,1,3, with no NULLs. Under SQL bag semantics, how many rows does SELECT A.k FROM A JOIN B ON A.k=B.k return?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A tunnel adds an outer IPv4 header of20 bytes to each entire inner IPv4 packet. The path MTU for outer packets is1500 bytes. Outer fragmentation is prohibited. The inner packet has an IPv4 header of20 bytes and a TCP header of20 bytes, with no options. What is the largest TCP data payload, in bytes, that fits in one tunneled packet?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

Six distinct books are arranged on a shelf. Books A and B must have exactly one book between them, and books C and D must be adjacent. How many arrangements satisfy both conditions?

**Answer format:** Exact integer.

### Q44. [2 Marks] [NAT]

A synchronous three-bit register has next state(a,b,c)→(b,c,NOT a). It starts at000. Its output is1 exactly when the current state has two1 bits. Count output1 states among the first twelve states observed, including the initial state as observation1.

**Answer format:** Integer.

### Q45. [2 Marks] [MCQ]

Two initially empty tables P(id,qid) and Q(id,pid) have non-NULL foreign keys P.qid→Q.id and Q.pid→P.id. A transaction inserts P(1,1) and Q(1,1). What difference can deferred checking make, assuming both foreign keys permit checking at commit?

A. It allows both rows to be inserted and the final mutually referencing state to satisfy the constraints, whereas immediate checking would reject whichever insert occurs first.
B. It permits either foreign key to remain broken permanently after commit.
C. It removes the requirement that referenced keys exist at commit.
D. It forces both tables to remain empty.

### Q46. [2 Marks] [NAT]

Two unsigned eight-bit fixed-point operands each have four fractional bits. Their encoded integers are 24 and 20. Their exact product is rescaled to the same format by dividing the integer product by 16 and rounding to nearest, with ties to even. What encoded integer is stored? No overflow occurs.

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A two-way set-associative cache has two sets and one block per way. Block b maps to set b modulo2, and each set uses LRU replacement. Starting empty, access blocks0,2,1,0,4,2,1. How many misses occur?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

A sequence satisfies a0=0 and a_n=2a_(n−1)+n for n≥1. Find lim as n→∞ of a_n/2ⁿ.

**Answer format:** Integer.

### Q49. [2 Marks] [MCQ]

Let n=2^(2^k) for positive integer k. Arithmetic on the loop variables has unit cost. What is the asymptotic number of work() calls?

```text
i = 2
while i < n:
    for j = 1 to i:
        work()
    i = i*i
```

A. Θ(log log n)  
B. Θ(√n)  
C. Θ(n)  
D. Θ(n log log n)

### Q50. [2 Marks] [NAT]

A cache has 64-byte lines and is initially empty. A packed row-major 16×16 array of four-byte elements begins on a line boundary. A loop reads every element exactly once in column-major order (all rows of column 0, then all rows of column 1, and so on). The cache is fully associative with eight lines and LRU replacement; no other memory accesses occur. How many cache misses occur?

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

Eight nonpreemptive activities have the following half-open time intervals; an activity may begin exactly when another finishes.

| Activity | Interval |
|---|---|
| A | [0,3) |
| B | [1,2) |
| C | [2,4) |
| D | [3,5) |
| E | [4,6) |
| F | [5,7) |
| G | [6,8) |
| H | [7,9) |

Let m be the maximum number of mutually nonoverlapping activities that can be selected, and let r be the number of distinct activity subsets attaining this maximum. What is (m,r)?

A. (3,4)  
B. (4,4)  
C. (4,5)  
D. (5,1)

### Q52. [2 Marks] [NAT]

The shared integer x is initially 0. Three threads execute exactly once:
```text
A: rA = x;  x = 2*rA + 1;
B: rB = x;  x = rB + 3;
C: rC = x;  x = rC + 5;
```
Each displayed read and each displayed write is separately atomic. Local registers are private. Execution is sequentially consistent, and a thread's read precedes its write. After all six operations have completed, how many distinct final values of x are possible?

**Answer format:** Numeric value; integer.

### Q53. [2 Marks] [NAT]

A syntax-directed definition assigns each bit string X two attributes: length X.len and fraction X.val. For a single bit b, len=1 and val=b/2. For concatenation X=YZ, the rules are X.len=Y.len+Z.len and X.val=Y.val+Z.val/2^(Y.len). A parse tree concatenates Y=10 and Z=11. What is X.val?

**Answer format:** Exact decimal.

### Q54. [2 Marks] [MCQ]

Consider the schedule `w1(x), w2(x), w1(x), w2(y), r3(y), w3(z)`, followed by commits of all three transactions. The subscripts identify transactions; writes are blind writes of distinct values. There are no other reads or writes. For view equivalence, preserve every read-from relationship and the identity of the final writer of each item. Which pair correctly states whether the schedule is conflict serializable and the number of serial transaction orders view equivalent to it?

A. Not conflict serializable; 2 orders
B. Conflict serializable; 2 orders
C. Not conflict serializable; 0 orders
D. Conflict serializable; 1 order

### Q55. [2 Marks] [MSQ]

In C, a function returns a pointer in each of the following independent versions. Assume allocations succeed and no frees occur before the caller's first access. Which versions permit the caller to access a live int object through the returned pointer after the function returns?

A. `int *f(void) { int x=7; return &x; }`
B. `int *f(void) { static int x=7; return &x; }`
C. `int *f(void) { int *p=malloc(sizeof *p); *p=7; return p; }` with the proper standard header.
D. `int *f(void) { int a[1]={7}; return a; }`

### Q56. [2 Marks] [MSQ]

An eight-bit binary floating-point encoding has one sign bit, a three-bit biased exponent and four fraction bits, with the usual sign-and-magnitude ordering of finite magnitudes. Consider only finite, nonzero represented values. Let raw be the unsigned eight-bit encoding. Define T(raw) as the eight-bit bitwise complement of raw for negative values, and raw XOR 0x80 for positive values. Which statements are true?

A. Sorting raw as unsigned integers gives increasing numerical order across both signs.
B. Within positive values, unsigned raw order agrees with numerical order.
C. Within negative values, larger unsigned raw always represents a numerically larger value.
D. Sorting T(raw) as unsigned integers gives increasing numerical order across both signs.

### Q57. [2 Marks] [MCQ]

A language permits a function to return a nested function that refers to its local variable x. Two separate calls to the outer function return functions F and G, capturing different x variables. Both returned functions are called after the outer calls have returned. Which implementation preserves lexical scoping and separate mutable x variables?

A. Put every captured x in the same global cell.
B. Keep each captured environment alive beyond the outer call and associate the appropriate environment with each returned function.
C. Keep only a pointer into the outer function's discarded stack frame.
D. Copy the current value of x anew from the most recent caller whenever F or G is invoked.

### Q58. [2 Marks] [NAT]

A packet of1200 bits travels through two store-and-forward links, with rates600 and1200 bits/s respectively. Each link has propagation delay0.1 seconds. There is no queueing or processing delay. What is the time from starting transmission on link1 until the final bit arrives at the destination?

**Answer format:** Exact seconds.

### Q59. [2 Marks] [NAT]

A single resource type has R identical reusable instances. Three processes each need at most three instances in total, may request one at a time, never release before completion, and finish once their total demand is met. What is the smallest R that guarantees absence of resource deadlock for every allocation state consistent with these maximum demands? Scheduling fairness is not being asked about.

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

Two identical CPUs schedule four nonpreemptive jobs, all arriving at time 0. Jobs A and B, with bursts 4 and 3, can run only on CPU 0. Job D, with burst 2, can run only on CPU 1. Job C, with burst 2, can run on either CPU. There is no I/O or switching overhead and jobs cannot migrate once started. What is the minimum possible sum of all four ready-queue waiting times?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

A queue is implemented by input stack I and output stack O. Enqueue pushes onto I. Dequeue transfers every element of I to O only when O is empty, then pops O. Initially both stacks are empty. Perform: enqueue 1–6; dequeue twice; enqueue 7–9; dequeue four times; enqueue 10; dequeue twice. Each individual stack push or pop costs one unit; no other operations are counted. What is the total cost?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A CRC uses generator g(x)=x²+x+1 over GF(2). A seven-bit frame suffers exactly two distinct bit flips, at positions chosen from0 through6. How many unordered position pairs produce an undetected error?

**Answer format:** Integer.

### Q63. [2 Marks] [MCQ]

For the unary language L={a^(n²):n≥0}, a pumping proof chooses a^(p²) and a pumped segment of length d with 1≤d≤p. Why does pumping once extra give a contradiction?

A. p²+d lies strictly between p² and (p+1)², so it is not a square.
B. p²+d is always less than p².
C. Every unary language is finite.
D. Pumping is prohibited for unary alphabets.

### Q64. [2 Marks] [MCQ]

A basic block ends with `x=a+b; y=x*c; x=0; return y;`, using exact scalar arithmetic and no externally observable intermediate assignments. Which first assignment is dead solely because x is overwritten later?

A. x=a+b is dead.
B. y=x*c is dead.
C. Neither of these assignments is dead: y uses the first x value and return uses y.
D. Both are dead.

### Q65. [2 Marks] [NAT]

How many truth assignments to p,q,r,s,t satisfy all five clauses `(p OR q)`, `(NOT p OR r)`, `(NOT q OR r)`, `(NOT r OR s)` and `(NOT s OR t)`?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 089

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 11.11 (two decimals) |
| 3 | MCQ | 1 | C |
| 4 | MCQ | 1 | A |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 60 |
| 7 | NAT | 2 | 5 |
| 8 | NAT | 2 | 5 |
| 9 | MCQ | 2 | A |
| 10 | NAT | 2 | 0.3333 (range 0.33325–0.33335) |
| 11 | NAT | 1 | 6 |
| 12 | NAT | 1 | 1 |
| 13 | NAT | 1 | 2 |
| 14 | NAT | 1 | 6 |
| 15 | NAT | 1 | -24 |
| 16 | NAT | 1 | 11 |
| 17 | MSQ | 1 | A, C |
| 18 | NAT | 1 | 2 |
| 19 | NAT | 1 | 9 |
| 20 | MCQ | 1 | B |
| 21 | NAT | 1 | 1 |
| 22 | NAT | 1 | -5 |
| 23 | MCQ | 1 | C |
| 24 | MCQ | 1 | D |
| 25 | NAT | 1 | 6.6667 (range 6.66665–6.66675) |
| 26 | MSQ | 1 | A, C, D |
| 27 | NAT | 1 | 3 |
| 28 | MSQ | 1 | A, C |
| 29 | NAT | 1 | 8 |
| 30 | NAT | 1 | 3 |
| 31 | MCQ | 1 | B |
| 32 | NAT | 1 | 3 |
| 33 | NAT | 1 | -1 |
| 34 | NAT | 1 | 2 |
| 35 | NAT | 1 | 4 |
| 36 | NAT | 2 | 225 |
| 37 | MSQ | 2 | A, B, D |
| 38 | MSQ | 2 | A, C |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 2 |
| 41 | NAT | 2 | 4 |
| 42 | NAT | 2 | 1440 |
| 43 | NAT | 2 | 48 |
| 44 | NAT | 2 | 4 |
| 45 | MCQ | 2 | A |
| 46 | NAT | 2 | 30 |
| 47 | NAT | 2 | 5 |
| 48 | NAT | 2 | 2 |
| 49 | MCQ | 2 | B |
| 50 | NAT | 2 | 256 |
| 51 | MCQ | 2 | C |
| 52 | NAT | 2 | 12 (exact) |
| 53 | NAT | 2 | 0.6875 |
| 54 | MCQ | 2 | A |
| 55 | MSQ | 2 | B, C |
| 56 | MSQ | 2 | B, D |
| 57 | MCQ | 2 | B |
| 58 | NAT | 2 | 3.2 |
| 59 | NAT | 2 | 7 |
| 60 | NAT | 2 | 5 |
| 61 | NAT | 2 | 38 (exact) |
| 62 | NAT | 2 | 5 |
| 63 | MCQ | 2 | A |
| 64 | MCQ | 2 | C |
| 65 | NAT | 2 | 3 |
