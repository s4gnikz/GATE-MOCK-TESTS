## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

The reviewer gave the proposal a “qualified endorsement”: she supported its objective but required a smaller pilot before implementation. In this context, “qualified” most nearly means:

A. supported without any reservations  
B. conditional on stated reservations  
C. written by a certified professional  
D. withdrawn after reconsideration  

### Q2. [1 Mark] [NAT]

A culture grows exponentially at a constant rate. Its population becomes eight times its initial value in 12 hours. Starting from the same initial population, after how many hours will it become 32 times its initial value?

**Answer format:** Numeric value; integer.

### Q3. [1 Mark] [MCQ]

An inspector accepts or rejects cards using one of the four candidate rules below. Each card has one colour, one shape, and is either filled or hollow. Observations are:

| Colour | Shape | Appearance | Decision |
|---|---|---|---|
| Red | Circle | Filled | Reject |
| Red | Circle | Hollow | Accept |
| Red | Square | Filled | Accept |
| Blue | Circle | Filled | Reject |
| Blue | Circle | Hollow | Reject |

Which candidate rule agrees with every observation?

A. Accept if the card is red and is either circular or filled, including when both hold.  
B. Accept if the card is red and exactly one of “circular” and “filled” holds.  
C. Accept if exactly one of “circular” and “filled” holds, regardless of colour.  
D. Accept if the card is red or circular, including when both hold.  

### Q4. [1 Mark] [MCQ]

A cube has six distinct face labels A,B,C,D,E,F. Three valid orientations are listed as (top, front, right): (A,B,C), (A,D,E), and (F,B,E). Which face is opposite B? Rotating the cube does not change its labels.

A. A  
B. C  
C. D  
D. E  

### Q5. [1 Mark] [NAT]

A numerical sequence begins a1=2 and a2=5. For every integer n>=3, its rule is a_n=2*a_(n-1)-a_(n-2)+n. What is a5-a4?

**Answer format:** Numeric value; integer.

### Q6. [2 Marks] [MCQ]

A rectangular garden is 16 m long and 10 m wide. A path of uniform width is laid inside all four edges, leaving a smaller rectangular planted region. The path occupies 88 square metres. What is the width of the path?

A. 1 m  
B. 2 m  
C. 3 m  
D. 4 m  

### Q7. [2 Marks] [MCQ]

Choose the revision that is grammatically correct and preserves both intended meanings: Mira did not leave earlier, so she missed the train; Mira, not the meeting, reached the office late.

Original: “If Mira had left earlier, she will catch the train. Having reached the office late, the meeting had already begun.”

A. If Mira left earlier, she will catch the train. Having reached the office late, the meeting began.  
B. If Mira had left earlier, she would have caught the train. When Mira reached the office late, the meeting had already begun.  
C. If Mira had left earlier, she would catch the train. Having reached the office late, the meeting had begun.  
D. If Mira would have left earlier, she caught the train. When the meeting reached the office late, Mira had begun.  

### Q8. [2 Marks] [MCQ]

A tank contains 120 litres of a well-mixed milk-water mixture in the ratio 3:2. First, 30 litres are removed and replaced with water. After thorough mixing, 20 litres are removed and replaced with pure milk. What is the final ratio of milk to water? Volumes are additive.

A. 11:13  
B. 13:11  
C. 3:2  
D. 7:5  

### Q9. [2 Marks] [MSQ]

Five distinct talks A,B,C,D,E are scheduled in positions 1 through 5. C is last. A occurs before C. Exactly one talk lies between B and D. E is neither first nor last. Which statements are true over schedules satisfying all these conditions?

A. A can be fourth.  
B. A must occur before E.  
C. E can be third.  
D. B and D must both occupy odd-numbered positions.  

### Q10. [2 Marks] [MCQ]

Solid stacks of unit cubes stand in a 2-by-3 grid. Each stack has a nonnegative integer height and has no gaps. Looking along the two-row direction, the maximum heights in the three columns are 2,3,1 respectively. Looking along the three-column direction, the maximum heights in the two rows are 3,2 respectively. What pair gives the minimum and maximum possible total number of cubes?

A. (7,11)  
B. (6,11)  
C. (6,12)  
D. (8,12)  

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A cache has two sets, two lines per set, and uses least-recently-used replacement within each set. Memory block b maps to set b mod 2. The cache is initially empty. The processor reads blocks 0, 2, 0, 4, 2 in that order. Every miss loads the requested block. How many cache misses occur?

**Answer format:** Numeric value; integer.

### Q12. [1 Mark] [MCQ]

A rooted binary tree has five distinct node labels. Its preorder traversal is A,B,C,D,E and its postorder traversal is C,B,E,D,A. Left and right child positions are distinguished. How many different binary trees have both of these traversals?

A. 1  
B. 2  
C. 4  
D. 8  

### Q13. [1 Mark] [NAT]

Two increasing runs contain four and three distinct keys respectively, with all seven keys different. Every original left-run position precedes every right-run position. Exactly five cross inversions exist, where a cross inversion is a left key greater than a right key. Standard merging compares the first remaining keys, emits the smaller, and stops comparisons as soon as either run is exhausted. What is the minimum possible number of key comparisons?

**Answer format:** Numeric value; integer.

### Q14. [1 Mark] [MCQ]

A processor has a write-back data cache with no hardware coherence with DMA. It modifies a buffer, leaving the buffer's cache lines dirty, and then asks a DMA controller to copy that buffer from main memory to a device. The processor will not modify the buffer again during the transfer. Which action before starting DMA ensures that the device receives the updated data?

A. Invalidate the dirty lines without writing them back.  
B. Write back all dirty buffer lines and wait for completion.  
C. Disable device-completion interrupts.  
D. Wait for a DMA-completion interrupt before starting the DMA transfer.  

### Q15. [1 Mark] [MCQ]

A depth-first search of a directed graph records discovery and finish times. Vertex u has interval [2,9] and vertex v has interval [4,7]. The graph contains an edge v→u. Which conclusion is necessarily correct?

A. The edge v→u is a tree edge.  
B. The graph contains a directed cycle.  
C. The edge v→u must be a cross edge.  
D. The graph must be acyclic because the intervals are nested.  

### Q16. [1 Mark] [MSQ]

A binary search tree stores distinct keys. A node x has both a left and a right child. Its inorder successor s is used when deleting x. Which statements about s in the tree before deletion are correct?

A. s is in the right subtree of x.  
B. s must be a leaf.  
C. s has no left child.  
D. s may have a right child.  

### Q17. [1 Mark] [NAT]

An epsilon-NFA has states 0,1,2,3, initial state 0, and these transitions; unlisted transitions have empty target sets.
```text
0 --a--> 0,1
1 --epsilon--> 2
2 --b--> 3
3 --epsilon--> 1
```
After consuming the entire input aab, take epsilon closure. How many states are in the resulting active-state set?

**Answer format:** Numeric value; integer.

### Q18. [1 Mark] [MCQ]

The following basic block uses exact mathematical integers and ordinary scalar variables, with no aliases or externally visible intermediate states. All three final variable values must be preserved. Which replacement is equivalent for every initial value of b and c?
```text
a = b + c
b = a - c
c = a - b
```

A. a = b + c  
B. a = b + c; b = c  
C. a = b + c; c = a  
D. a = b + c; b = a; c = 0  

### Q19. [1 Mark] [MCQ]

For the grammar S→aS | Sb | ab, which listed string has two distinct ordered parse trees? Only finite parse trees are counted.

A. ab  
B. aab  
C. abb  
D. aabb  

### Q20. [1 Mark] [NAT]

Routers A,B,C use synchronous distance-vector updates for destination C. Link costs are A–B=1, B–C=1 and A–C=10. Initially routes are converged. Link B–C fails immediately before round 1. In every round each router recomputes its distance using its still-working links and the neighbours' distances from the end of the preceding round; C always advertises 0. No split horizon, poison reverse or triggered intermediate updates are used. What distance does A advertise after round 2?

**Answer format:** Numeric value; integer.

### Q21. [1 Mark] [MSQ]

A binary floating-point system retains three significant binary digits, including the leading 1. Exponents are unbounded, and every result is rounded to nearest, ties to even. Which statements are correct?

A. The exact value 1.125 rounds to 1.0.  
B. Consecutive representable numbers in [2,4) are separated by 0.25.  
C. Adding represented values 1.75 and 0.25 yields exactly 2.0.  
D. Every integer from 0 through 9 is represented exactly.  

### Q22. [1 Mark] [MSQ]

For real t let

```text
A(t) = [1  2  1]
       [2  t  3]
       [1  3  1].
```

Use Doolittle elimination, with unit diagonal in L and no row exchanges unless an option explicitly permits one. Which statements are correct?

A. det(A(t))=-1 for every real t.  
B. An unpivoted factorization A=LU with unit lower-triangular L exists for every real t.  
C. At t=4, exchanging rows 2 and 3 after eliminating column 1 allows elimination to finish without a zero pivot.  
D. At t=5, the final diagonal entry U33 is 1.  

### Q23. [1 Mark] [MSQ]

Consider this program with exact integers and an arbitrary Boolean input flag. A conventional nonrelational constant-propagation analysis tracks, for each variable separately, either a single constant or 'not constant'; at a join, distinct incoming constants become 'not constant'.
```text
if flag:
    x = 2; y = 3
else:
    x = 3; y = 2
z = x + y
```
Which statements are correct?

A. Every execution assigns5 to z.  
B. The stated analysis finds x constant at the join.  
C. The stated analysis necessarily infers z=5 directly from the joined abstract values of x and y.  
D. Moving the assignment z=x+y into the end of each branch allows the stated analysis to find z=5 after the join.  

### Q24. [1 Mark] [NAT]

Evaluate the integral from 0 to 1 of max(x,1-2x) with respect to x. Round the result to three decimal places.

**Answer format:** Numeric value; 3 decimal places.

### Q25. [1 Mark] [MCQ]

A variable is live if its current value may be read along a subsequent control-flow path before being overwritten. In the code below, x, y, z and flag are ordinary variables, and there are no implicit uses after return. Which set contains exactly the variables live at P, immediately before y = z?

```text
L: x = y
   if flag goto K
P: y = z
   goto L
K: return x
```

A. {z, flag}  
B. {x, z, flag}  
C. {y, z, flag}  
D. {x, y, z, flag}  

### Q26. [1 Mark] [MCQ]

Let F(x,y,z)=x XOR (y AND z). Define D(x,y,z)=F(x,y,z) XOR F(x,NOT y,z). Which expression equals D for every Boolean input?

A. x  
B. y  
C. z  
D. NOT z  

### Q27. [1 Mark] [NAT]

Three processes have (arrival time, CPU burst length) A=(0,7), B=(2,4), C=(4,1), in time units. A single CPU uses preemptive shortest-remaining-time-first scheduling with zero switching overhead. No process performs I/O. Waiting time is completion time minus arrival time minus burst length. What is the average waiting time?

**Answer format:** Numeric value; integer.

### Q28. [1 Mark] [MCQ]

Relation R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which is its highest normal form among the choices below? Assume atomic attribute values.

A. 1NF but not 2NF  
B. 2NF but not 3NF  
C. 3NF but not BCNF  
D. BCNF  

### Q29. [1 Mark] [NAT]

Dataset A contains 3 observations with mean 2 and population variance 2. Dataset B contains 2 observations with mean 7 and population variance 1. What is the population variance of their combined five observations? Use division by the population size, not by one less than that size.

**Answer format:** Numeric value; 1 decimal place.

### Q30. [1 Mark] [NAT]

An IPv4 fragment arrives with total length 1020 bytes, header length 20 bytes, fragment offset 100, and MF=1. A router forwards it through an interface with MTU 620 bytes and fragments it into the minimum number of fragments, using the largest permitted payload in the first new fragment. Every outgoing header is 20 bytes. What is the fragment-offset field of the second outgoing fragment?

**Answer format:** Numeric value; integer.

### Q31. [1 Mark] [NAT]

A disk has cylinders 0 through 99. At time 0, its head is at cylinder 50, moving toward larger numbers, with requests pending at 70, 90 and 10. Seek speed is one cylinder per time unit; service and reversal take zero time. A new request for cylinder 95 arrives at time 45. LOOK continues in its current direction while any request is pending ahead, and otherwise reverses. New arrivals join the queue without causing an early reversal. What total head movement serves all four requests?

**Answer format:** Numeric value; integer.

### Q32. [1 Mark] [MCQ]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, each one cycle. There is no forwarding and no automatic stalling. Register writes occur in the first half of a cycle and ID reads in the second half, so ID may read a value written in WB during the same cycle. The instructions below use ordinary integer registers; R0 is always available. What is the minimum total number of NOP instructions that must be inserted without reordering to guarantee correct results for arbitrary initial register values?
```text
ADD R1,R0,R0
ADD R2,R1,R0
ADD R3,R2,R0
```

A. 2  
B. 3  
C. 4  
D. 6  

### Q33. [1 Mark] [MCQ]

On the set of residues {0,1,2,3,4} modulo 5, define permutations f(x)=2x mod 5 and g(x)=(x+1) mod 5. Let h=f composed with g composed with f-inverse composed with g-inverse; the rightmost map acts first. What is the smallest positive integer k for which h applied k times is the identity?

A. 1  
B. 2  
C. 4  
D. 5  

### Q34. [1 Mark] [MCQ]

A sorted data file has fixed-length records, with exactly eight records per data page and no unused slots. A range query matches exactly 16 consecutive records in file order. An index lookup requires exactly two page reads and identifies the first matching record's page and slot. Index pages are separate from data pages, no page is initially cached, and scanning the range reads each needed data page once. What is the largest possible total number of page reads, over the possible starting slots?

A. 3  
B. 4  
C. 5  
D. 6  

### Q35. [1 Mark] [MSQ]

G is a connected simple undirected graph with degree multiset {3,3,2,2,2,2}. Which statements must hold?

A. G has exactly 7 edges.  
B. G has an Euler trail that uses every edge exactly once.  
C. G is bipartite.  
D. G has a Hamiltonian cycle.  




