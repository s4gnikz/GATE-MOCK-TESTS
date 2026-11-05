# GATE CS 2027 — Full-Length Mock Test 060

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

### Q1. [1 Mark] [NAT]

A sequence begins a1=1,a2=2 and satisfies a(n+2)=a(n+1)+a(n). How many of its first twelve terms are odd?

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A rectangle has perimeter 30 and diagonal length √125. What is its area?

**Answer format:** Integer square units.

### Q3. [1 Mark] [MCQ]

Choose the pair that completes the sentence grammatically.

Each of the instruments that ___ damaged during transport ___ now been recalibrated.

A. were; has  
B. was; have  
C. were; have  
D. was; has

### Q4. [1 Mark] [NAT]

Two funds initially contain amounts in the ratio 3:5. Twenty percent of the second fund is transferred to the first. What is the new ratio of the first amount to the second, expressed as a numerical quotient?

**Answer format:** Integer.

### Q5. [1 Mark] [MSQ]

Some A are B. Every B is C. No C is D. Which conclusions necessarily follow?

A. Every A is C.  
B. Some A are not D.  
C. Some D are A.  
D. No B is D.

### Q6. [2 Marks] [NAT]

A point is transformed by T(x,y)=(y,−x), a clockwise quarter-turn about the origin, and by U(x,y)=(x+2,y). Starting from(1,1), compare two results: first T then U, and first U then T. What is the squared Euclidean distance between these two final points?

**Answer format:** Exact integer.

### Q7. [2 Marks] [MCQ]

“A new policy reduced average processing time, but the study did not measure the number of incorrect decisions.” Which claim is justified by the study as described?

A. Processing became faster on average, while the effect on decision accuracy remains unmeasured.
B. Decision accuracy necessarily improved.
C. Every decision became faster and more accurate.
D. Incorrect decisions necessarily increased.

### Q8. [2 Marks] [NAT]

Four students each receive one distinct project, with assignments chosen from all 4! possibilities. Exactly two students must receive their first-choice project. The four first-choice projects are all different. How many assignments satisfy this requirement?

**Answer format:** Exact integer.

### Q9. [2 Marks] [NAT]

A service centre completed 18 of 20 jobs on Monday and 12 of 20 on Tuesday. On Wednesday it completes every job it receives. What is the minimum number of Wednesday jobs needed to make the combined three-day completion rate at least 80%?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

Two fair six-sided dice are rolled. Given that their sum is prime, what is the probability that their product is divisible by 3? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Router R uses a distance-vector update. Its link costs to neighbours U and V are 2 and 5. They advertise distances 7 and 3, respectively, to destination D. R has no other route to D. If the link to V fails and U's advertisement is unchanged, what distance does R compute for D in its next update?

A. 7
B. 8
C. 9
D. Infinity

### Q12. [1 Mark] [MSQ]

A compiler removes an assignment to scalar x as dead code. The right-hand side has no side effects, exceptions, or observable traps. Which conditions support removal?

A. On every outgoing path, x is redefined before its current value is read, or execution ends without reading it.
B. x is read on at least one outgoing path before redefinition.
C. x is not live immediately after the assignment.
D. x has a short variable name.

### Q13. [1 Mark] [NAT]

X takes values−2 and2 with equal probability. Let Y=X². What is Var(Y)?

**Answer format:** Exact number.

### Q14. [1 Mark] [MSQ]

Processes communicate through a bounded message queue. A send blocks when the queue is full, and a receive blocks when it is empty. Which statements are correct?

A. A blocked sender can become eligible to proceed after a receive removes an item.
B. Bounded buffering alone guarantees absence of deadlock in every application using the queue.
C. Blocking communication can synchronize processes without busy waiting by the blocked process.
D. The queue can hold arbitrarily many unreceived messages.

### Q15. [1 Mark] [MSQ]

For0/1 knapsack, an implementation uses one array dp[c], initially zero. For each item of positive weight w and value v, it updates dp[c]=max(dp[c],dp[c−w]+v). Which statements are correct?

A. Scanning c downward from capacity to w prevents reuse of the current item.
B. Scanning upward can allow the same item to be used repeatedly.
C. Either direction always computes the0/1 optimum.
D. With a single item of weight2 and value3 and capacity4, an upward scan gives dp[4]=6.

### Q16. [1 Mark] [NAT]

An IPv4 receiver has received two fragments of one datagram. The first has offset 0, payload length 80 bytes and MF=1. The other has offset 12 (in the standard eight-byte units), payload length 24 bytes and MF=0. No other fragments have arrived. How many payload bytes are missing between the received regions?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

Let F(x,y,z)=x XOR (y AND z). Define D(x,y,z)=F(x,y,z) XOR F(x,NOT y,z). Which expression equals D for every Boolean input?

A. x  
B. y  
C. z  
D. NOT z

### Q18. [1 Mark] [MCQ]

A two-level AND–OR circuit implements F=AB+(NOT A)C. Only A changes while B=C=1. Gate delays are positive and unequal. Which single redundant product term can be added to eliminate the possible static-1 hazard for this transition without changing F?

A. AC  
B. (NOT B)C  
C. BC  
D. A(NOT C)

### Q19. [1 Mark] [NAT]

A direct-mapped cache has four lines and starts empty. Block b maps to line b modulo4. For references0,4,0,4, how many are conflict misses after excluding the first access to each distinct block as compulsory?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

How many functions f:{1,2,3}->{1,2,3} satisfy f(f(x))=f(x) for every x and have exactly two fixed points? A fixed point is an x for which f(x)=x.

**Answer format:** Numeric value; integer.

### Q21. [1 Mark] [NAT]

Let A=uvᵀ, where u=(1,2,−1)ᵀ and v=(2,0,3)ᵀ. What is the sum of the squares of A's three eigenvalues, counted with algebraic multiplicity?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A sliding-window minimum algorithm maintains a deque of indices. Before inserting each new index i, it removes expired indices from the front, then removes indices from the back while their values are at least the new value, then appends i. The window length is3. Starting empty, process values[4,2,3,1] from left to right. How many removals from the back occur in total?

**Answer format:** Integer.

### Q23. [1 Mark] [MSQ]

In a basic block, p and q are pointers to valid int objects and may alias. Consider `t=*p; *q=7; u=*p;`. There is no concurrency or volatile access. Which statements are correct?

A. Replacing the final load by u=t is valid whenever p and q are proved to point to different objects.
B. The replacement is valid for all possible aliases and initial values.
C. If p=q and the initial pointed-to value is 3, the original block ends with t=3,u=7.
D. A store through q cannot affect a subsequent load through p because the pointer names differ.

### Q24. [1 Mark] [MSQ]

In tabular Boolean minimization, two implicants may be combined in one step only if their dash positions agree and exactly one remaining binary position differs. Which pairs can be combined in one step?

A. 0-01 and 1-01  
B. -001 and --11  
C. -001 and -011  
D. 0101 and 1010

### Q25. [1 Mark] [MCQ]

A SQL column x has constraint `CHECK (x>0)` but no NOT NULL constraint. Under standard CHECK semantics, which values satisfy the constraint?

A. Positive integers only.
B. Positive integers and NULL.
C. Zero, positive integers, and NULL.
D. Every integer and NULL.

### Q26. [1 Mark] [MSQ]

Let L be regular and F finite over the same alphabet. Which languages are necessarily regular?

A. L∪F
B. L−F
C. F−L
D. Every language containing L as a subset.

### Q27. [1 Mark] [NAT]

A differentiable function f on the real line satisfies f(0)=0 and f'(x)≥2 for every real x. What is the smallest possible value of f(3)−f(−1)?

**Answer format:** Exact number.

### Q28. [1 Mark] [NAT]

A hidden bit H is equally likely to be 0 or 1. Conditional on H, two sensors independently report H with probability 3/4 and report the other bit otherwise. The sensors agree. What is the probability that their common report equals H?

**Answer format:** Exact decimal.

### Q29. [1 Mark] [NAT]

An algorithm partitions a size-27 input into three equal subproblems at each nontrivial call, stopping at size one. How many internal calls occur in its complete recursion tree?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

A counting semaphore initialized to 3 controls access to identical resources. Each successful wait decrements it and each release signals it once. With no erroneous extra signals, what does initialization to 3 represent?

A. At most three concurrent resource holders can be admitted.
B. Exactly three processes must execute wait simultaneously.
C. Every process must wait three times before entering.
D. No process can ever block.

### Q31. [1 Mark] [MSQ]

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

### Q32. [1 Mark] [MCQ]

Consider L={aⁿbᵐ:n,m≥0 and n≠m}. For an arbitrary positive proposed regular pumping length p, choose w=aᵖb^(p+p!). Every valid split w=xyz with |xy|≤p and |y|>0 has y=aᵏ for some 1≤k≤p. Which pumping exponent i makes xy^i z have equal a and b counts and therefore leave L?

A. i=p!
B. i=1+p!/k
C. i=1−p!/k
D. i=k+1

### Q33. [1 Mark] [MSQ]

SQL table R has non-null values 1,2,3 in column x. Table S has values 2 and NULL in column y. Which statements are correct under standard SQL three-valued logic?

A. `SELECT x FROM R WHERE x NOT IN (SELECT y FROM S)` returns no rows.
B. `SELECT x FROM R WHERE NOT EXISTS (SELECT 1 FROM S WHERE S.y=R.x)` returns 1 and 3.
C. `SELECT COUNT(y) FROM S` returns 2.
D. The predicate `NULL=NULL` evaluates to TRUE.

### Q34. [1 Mark] [NAT]

A binary tree has distinct node labels. Its preorder traversal is A,B,D,E,C,F and its postorder traversal is D,E,B,F,C,A. Left and right child positions are distinguished, and a node may have only one child. How many binary trees have both of these traversals?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

A device sets a level-triggered interrupt request while its completion-status bit is 1. An interrupt handler acknowledges the CPU interrupt controller but leaves the device status bit unchanged. Assuming the controller permits subsequent delivery, what behavior is possible after return from the handler?

A. Another interrupt is delivered because the device still asserts its request.
B. The device's status bit necessarily clears when the CPU acknowledges its controller.
C. The device's completed transfer is automatically undone.
D. The interrupt line necessarily changes into an edge-triggered source.

### Q36. [2 Marks] [NAT]

For matrix-chain multiplication, four matrices have dimensions 5×10,10×3,3×12,12×5. Count scalar multiplications in the usual way: multiplying p×q by q×r costs pqr. What is the minimum scalar-multiplication cost for their product?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Two Turing machines recognize languages L1,L2 over a finite alphabet, but may loop on nonmembers. Which assertions hold?

A. Nonemptiness of L1 intersect L2 can be recognized by dovetailing simulations on all strings.
B. Running both machines to completion on each string before considering the next always recognizes nonemptiness of their intersection.
C. If both accept some common string, a fair dovetailing search eventually finds one.
D. Failure to find a common accepted string after any finite amount of simulation proves their intersection empty.

### Q38. [2 Marks] [NAT]

In the divisibility poset of positive divisors of 72, how many elements x satisfy gcd(x,12)=6 and lcm(x,12)=72?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

Insert the six distinct keys 1–6 into an initially empty ordinary binary search tree, with no rotations. How many insertion permutations have root 3 and final height exactly 2, measured in edges?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A B+ tree has maximum three keys per leaf and maximum four children per internal node. Leaves hold data keys only. Insert into a leaf in sorted order; when it reaches four keys, split into two leaves with two keys each and copy the smallest key of the right leaf upward. Initially the root has separator30 and two leaves [10,20] and [30,40,50]. Insert35, then45, then15. No deletion occurs. How many separator keys are in the root at the end?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A 1 Mbit/s output link receives a burst of three 1000-bit packets simultaneously at time 0 and thereafter no packets. It transmits nonpreemptively at full rate. A packet's queueing delay excludes its own transmission time and includes only waiting before transmission begins. What is the average queueing delay, in milliseconds, of these three packets?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

A parent creates a pipe and then forks. Both processes initially inherit both pipe ends. The parent closes its own write end and reads until EOF. The child writes some data and then becomes idle without exiting or closing either descriptor. Assume all data already written have been read. Which statements are correct?

A. The parent's next blocking read must return EOF immediately.
B. The child's still-open write descriptor prevents EOF at the parent.
C. Closing the child's read descriptor alone is sufficient to cause EOF at the parent.
D. If the child closes its write descriptor and no other write descriptors exist, the parent can observe EOF.

### Q43. [2 Marks] [NAT]

A data-only L1 cache holds two blocks; a unified L2 holds three. Both are fully associative with LRU replacement and initially empty. L2 is inclusive: evicting a block invalidates any L1 copy. A data L1 miss accesses L2 and updates its LRU order; an L1 hit does not access L2. Instruction accesses bypass L1 and access/update only L2. Every L2 miss fetches one block from memory. Accesses are data A, data B, data A, instruction C, instruction D, data A. All block labels are distinct. How many memory block fetches occur?

**Answer format:** Integer memory block fetches.

### Q44. [2 Marks] [MSQ]

A binary min-heap contains distinct keys. Its array uses one-based indexing. Which statements must hold for every heap of at least seven elements?

A. The second-smallest key is at index2 or3.
B. The third-smallest key is necessarily at index4 or5.
C. The parent of a node always has a smaller key than that node.
D. The array is globally sorted in increasing order.

### Q45. [2 Marks] [NAT]

An eight-input Boolean function is the parity of all eight inputs. Only two-input XOR gates are available. Every gate has unit delay and unlimited fanout; wire delay is zero. Among circuits with the minimum possible number of XOR gates, what is the minimum worst-case input-to-output delay?

**Answer format:** Integer gate delays.

### Q46. [2 Marks] [NAT]

For solving Ax=b, a factorization PA=LU is supplied. P swaps the first two rows, b=(1,2,3)ᵀ, L has rows (1,0,0),(2,1,0),(−1,3,1), and U has rows (2,1,−1),(0,3,2),(0,0,4). Find the third component of x.

**Answer format:** Exact finite decimal.

### Q47. [2 Marks] [MCQ]

A router receives destination 172.16.5.200. Its routes are 172.16.0.0/16→A, 172.16.4.0/22→B, 172.16.5.128/25→C, and a default route→D. A forwarding policy first chooses the longest matching prefix; among equal-length matches it chooses the lowest metric. The /25 route has metric 100 and the /22 route metric 1. Which next hop is selected, and why?

A. B, because metric 1 is smaller than 100.
B. C, because prefix length is considered before metric.
C. A, because a /16 covers more addresses.
D. D, because the overlapping routes are ambiguous.

### Q48. [2 Marks] [MSQ]

For a DFA, states p and q are equivalent if every suffix yields the same acceptance result from both. Which statements are correct?

A. If p is accepting and q rejecting, ε distinguishes them.
B. Having the same transitions on one input symbol alone guarantees equivalence.
C. If p,q are equivalent, their successors on any given symbol are equivalent.
D. Two unreachable states must be equivalent to each other.

### Q49. [2 Marks] [NAT]

Let I be the integral from 0 to 1 of x/(1+x²) dx, and J the integral from 0 to 1 of x³/(1+x²) dx. What is I+J?

**Answer format:** Exact decimal.

### Q50. [2 Marks] [MSQ]

R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which statements are correct?

A. AC and BC are candidate keys.
B. A alone is a candidate key.
C. R is in3NF.
D. R is in BCNF.

### Q51. [2 Marks] [NAT]

A synchronous four-bit register has next-state rule(a,b,c,d)→(b,c,d,a XOR b), evaluated from the old state. Starting from0001, what is the smallest positive number of clock edges after which the register returns to0001?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A byte-addressed machine uses eight-byte words. A load instruction's effective byte address is Rb+8Ri+d. Initially Rb=1000 and Ri=3. Memory at byte address1032 holds the integer7. Execute LOAD Rj,[Rb+8Ri+8], then set Ri=Rj−2, then execute LOAD Rk,[Rb+8Ri−8]. What is the effective byte address of the second load?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

Four processes have resource demands: P holds A and requests B; Q holds B and requests C; R holds C and requests A; S holds D and requests B. Each resource has one instance, requests block, and no process releases its held resource before receiving its request. How many processes lie on a directed cycle in the wait-for graph?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

A block computes t=a+b, then branches. Path P executes a=a+1, while path Q changes neither a nor b. At the join, u=a+b is computed. Arithmetic is over mathematical integers. Which statements are correct?

A. On path P, the join expression equals t+1.
B. Replacing u by t on both paths is valid.
C. The original t is overwritten by updating a.
D. Selecting t+1 for path P and t for path Q preserves u.

### Q55. [2 Marks] [NAT]

A signed fixed-point representation stores an eight-bit two's-complement integer scaled by1/16. What is the width of its representable real interval, defined as largest value minus smallest value?

**Answer format:** Exact decimal.

### Q56. [2 Marks] [NAT]

A lexer uses maximal munch. Its tokens are ID=[a-z]+, EQ='=', and EQEQ='=='. Keyword 'if' takes precedence over ID only when both match the same longest lexeme. Whitespace is ignored. How many tokens result from this input?

```text
ifif===if = iff
```

**Answer format:** Exact integer.

### Q57. [2 Marks] [NAT]

What integer does this conforming C program print? Each recursive call shares the same pointed-to integer.

```c
#include <stdio.h>
int f(int n, int *p) {
    if (n == 0) return *p;
    *p += n;
    int a = f(n-1, p);
    *p -= 1;
    return a + *p;
}
int main(void) {
    int x = 1;
    printf("%d\n", f(3, &x));
    return 0;
}
```

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A directed graph has edges s→a of weight 3, s→b of weight 8, a→b of weight −4, b→c of weight 2, and a→c of weight 7. Reweight each edge by w'(u,v)=w(u,v)+h(u)−h(v), with h(s)=0, h(a)=0, h(b)=−4, h(c)=−2. What is the shortest-path distance from s to c in the reweighted graph?

**Answer format:** Exact integer.

### Q59. [2 Marks] [NAT]

Two disjoint groups each contain the same number of observations. Their means are2 and8, and their population variances are1 and9 respectively. What is the population variance of all observations combined?

**Answer format:** Exact number.

### Q60. [2 Marks] [NAT]

A512-byte slotted page has a32-byte fixed header and six retained four-byte slot entries. Each record must occupy a contiguous region. Its six records, in adjacent physical order, have lengths60,70,80,50,40,30 bytes. All remaining free space is one contiguous gap between the slot directory and records. Delete the adjacent80-byte and50-byte records, retaining their slot entries. A new record must use a new four-byte slot entry. What is the increase in the maximum insertable record length if the remaining records may be compacted, compared with insertion without moving them?

**Answer format:** Integer bytes.

### Q61. [2 Marks] [MSQ]

A disk uses SSTF. Its head starts at track 0 with requests pending at tracks 1 and 100. Each time it services track 1 a fresh request for track 0 arrives immediately, and each time it services track 0 a fresh request for track 1 arrives immediately. No other requests arrive; service takes zero time and movement is positive time. Which statements are true?

A. The track-100 request can remain unserved forever under this arrival pattern.
B. SSTF guarantees a finite waiting bound solely because it selects the nearest request.
C. A fixed finite request set with no new arrivals can reproduce this infinite starvation while each service removes one request.
D. The continued supply of nearby requests is essential to this particular starvation construction.

### Q62. [2 Marks] [NAT]

The grammar E→E+E | E*E | id has no precedence or associativity rules. For the token string id+id*id+id, how many distinct parse trees have a '+' production at the root?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

An ALU implements unsigned eight-bit subtraction A−B by adding A, the bitwise complement of B, and 1. Let A=37 and B=91. What unsigned integer is represented by the retained eight result bits?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

An undirected simple graph has 64 vertices and m edges. Compare a bit-packed adjacency matrix of exactly 64² bits with an adjacency-list representation using 32 bits for each of 65 header/offset entries and 16 bits for each of the 2m neighbour entries. Ignore all other overhead. What is the smallest integer m for which the matrix occupies strictly less storage than these lists?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A TCP sender's next new data byte has sequence number 5001. Its latest cumulative acknowledgement is ACK=1001, meaning that byte 1001 is next expected. The advertised receive window is 6000 bytes and the congestion window is 8000 bytes.

The sender transmits the maximum permitted amount of new data. It then receives ACK=3001 with an advertised receive window of 3500 bytes and an updated congestion window of 10000 bytes, and again transmits the maximum permitted new data. Finally, it receives ACK=5501 with an advertised receive window of 5000 bytes and an updated congestion window of 4500 bytes, and again sends as much new data as permitted.

There are no other transmissions, acknowledgements or window changes. Each advertised receive window starts at its ACK number. Ignore sequence-number wraparound and segment-size restrictions. Data already sent may lie beyond the right edge of a newly reduced receive window; it remains outstanding. How many new data bytes are transmitted in total across these three sending opportunities?

**Answer format:** Numeric value; integer.

---

## ANSWER KEY — MOCK TEST 060

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 8 |
| 2 | NAT | 1 | 50 |
| 3 | MCQ | 1 | A |
| 4 | NAT | 1 | 1 |
| 5 | MSQ | 1 | B, D |
| 6 | NAT | 2 | 8 |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 6 |
| 9 | NAT | 2 | 10 |
| 10 | NAT | 2 | 0.5333 (range 0.53325–0.53335) |
| 11 | MCQ | 1 | C |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 0 |
| 14 | MSQ | 1 | A, C |
| 15 | MSQ | 1 | A, B, D |
| 16 | NAT | 1 | 16 |
| 17 | MCQ | 1 | C |
| 18 | MCQ | 1 | C |
| 19 | NAT | 1 | 2 |
| 20 | NAT | 1 | 6 (exact) |
| 21 | NAT | 1 | 1 |
| 22 | NAT | 1 | 3 |
| 23 | MSQ | 1 | A, C |
| 24 | MSQ | 1 | A, C |
| 25 | MCQ | 1 | B |
| 26 | MSQ | 1 | A, B, C |
| 27 | NAT | 1 | 8 |
| 28 | NAT | 1 | 0.9 |
| 29 | NAT | 1 | 13 |
| 30 | MCQ | 1 | A |
| 31 | MSQ | 1 | A, B |
| 32 | MCQ | 1 | B |
| 33 | MSQ | 1 | A, B |
| 34 | NAT | 1 | 2 |
| 35 | MCQ | 1 | A |
| 36 | NAT | 2 | 405 |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 0 |
| 39 | NAT | 2 | 40 (exact) |
| 40 | NAT | 2 | 2 |
| 41 | NAT | 2 | 1 |
| 42 | MSQ | 2 | B, D |
| 43 | NAT | 2 | 5 |
| 44 | MSQ | 2 | A, C |
| 45 | NAT | 2 | 3 |
| 46 | NAT | 2 | 3.5 |
| 47 | MCQ | 2 | B |
| 48 | MSQ | 2 | A, C |
| 49 | NAT | 2 | 0.5 |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 15 |
| 52 | NAT | 2 | 1032 |
| 53 | NAT | 2 | 3 |
| 54 | MSQ | 2 | A, D |
| 55 | NAT | 2 | 15.9375 |
| 56 | NAT | 2 | 6 |
| 57 | NAT | 2 | 22 |
| 58 | NAT | 2 | 3 |
| 59 | NAT | 2 | 14 |
| 60 | NAT | 2 | 122 |
| 61 | MSQ | 2 | A, D |
| 62 | NAT | 2 | 4 |
| 63 | NAT | 2 | 202 |
| 64 | NAT | 2 | 64 |
| 65 | NAT | 2 | 5000 (exact) |
