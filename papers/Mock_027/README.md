# GATE CS 2027 — Full-Length Mock Test 027

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Attempt all questions within 180 minutes. Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes15 marks, Engineering Mathematics13, and core CS72.

MCQ questions have exactly one correct option. MSQ questions have more than one correct option; select all and only the correct options for credit. An incorrect one-mark MCQ loses1/3 mark; an incorrect two-mark MCQ loses2/3 mark. MSQ and NAT questions have no negative marking and no partial credit. Unattempted questions receive zero. NAT answers must follow the specified precision; integer and exact-decimal answers require exact values. Unless stated otherwise, arithmetic in mathematical descriptions is exact. The answer key follows Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

A report states: “Every village whose water supply was tested met the safety standard. Some villages could not be reached during the survey.” Which conclusion is justified by these statements alone?

A. Every village met the safety standard.
B. At least one untested village failed the standard.
C. No tested village failed the standard.
D. The untested villages had safer water than the tested villages.

### Q2. [1 Mark] [NAT]

Four people each leave an identical-looking umbrella in a stand. The umbrellas have different owners. At departure, each person takes one umbrella. How many assignments give exactly two people their own umbrellas?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A factory reports that20% of the items produced on Monday were rejected. On Tuesday it produced twice as many items, and10% were rejected. What percentage of the two days' rejected items came from Monday?

**Answer format:** Exact percentage, without the percent sign.

### Q4. [1 Mark] [NAT]

A square sheet occupies 0≤x≤4, 0≤y≤4. First its left half is folded onto its right half along x=2. Then the lower half of the folded packet is folded upward along y=2. A small circular hole is punched through all layers at (3,3), away from all edges. After unfolding, what is the area of the convex hull of the hole centres?

**Answer format:** Integer square units.

### Q5. [1 Mark] [MCQ]

Arrange the sentences into a coherent paragraph.

P: This second reading was lower than the first.
Q: To check the surprising result, she repeated the measurement.
R: Mira measured the room's temperature using a newly calibrated sensor.
S: She therefore decided to investigate the conditions before reporting either value.

A. R,Q,P,S
B. Q,R,S,P
C. P,S,R,Q
D. R,P,Q,S

### Q6. [2 Marks] [NAT]

A box contains three red and two blue counters. Counters are drawn without replacement until the first blue counter appears. What is the expected number of counters drawn, including that first blue counter?

**Answer format:** Decimal rounded to four places.

### Q7. [2 Marks] [MCQ]

“The panel described the evidence as suggestive rather than conclusive; its recommendation was consequently provisional.” Which revision preserves both the strength of the evidence and the status of the recommendation?

A. The evidence proved the claim, so the recommendation was final.
B. The evidence offered some support, so the recommendation remained open to revision.
C. The evidence disproved the claim, so the recommendation was withdrawn.
D. The evidence was irrelevant, so the recommendation was unanimous.

### Q8. [2 Marks] [NAT]

A positive quantity doubles every three hours. Another positive quantity triples every six hours. They begin with equal values. After how many hours does the ratio of the first quantity to the second first reach16/9? Growth is continuous with these constant exponential rates.

**Answer format:** Exact number of hours.

### Q9. [2 Marks] [MSQ]

A proposed rule maps every integer n to n²+n+1. Observations for inputs1,2,3 give outputs3,7,13. Which statements are correct?

A. The proposed rule agrees with all three observations.
B. These observations uniquely establish the rule for every integer input.
C. Adding (n−1)(n−2)(n−3) to the proposed rule gives another rule agreeing with the observations.
D. The proposed rule predicts21 at input4.

### Q10. [2 Marks] [NAT]

Unit cubes are stacked on a 2×2 base with column heights [[3,1],[2,2]]. Adjacent entries in a row or column represent face-adjacent columns. All columns start on the same horizontal plane. Excluding the bottom faces on that plane, how many unit-square faces of the solid are exposed?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A table T(a,b) has a UNIQUE constraint on a and a separate NOT NULL constraint on b. Values of a are restricted to non-NULL values in the instances considered. Which statements must hold in every legal instance?

A. No two rows have the same a value.
B. Every b value occurs in at most one row.
C. Every row has a non-NULL b value.
D. Every possible non-NULL a value appears in a row.

### Q12. [1 Mark] [NAT]

An array-based binary min-heap is [2,7,4,12,9,6,5], using one-based indices. Delete the minimum by moving the last element to the root and repeatedly exchanging it with its smaller child until the heap property holds. What is the sum of the values at indices2 and3 afterward?

**Answer format:** Integer.

### Q13. [1 Mark] [MSQ]

At entry to a block, x and y have defined values. The block is:

```text
x = y + 1
z = x + y
return z
```

No other use follows. Which statements are correct under standard liveness analysis?

A. The incoming value of x is live at block entry.
B. The incoming value of y is live at block entry.
C. Immediately after the first assignment, both x and y are live.
D. Immediately after the second assignment, y is live.

### Q14. [1 Mark] [NAT]

Evaluate the definite integral from0 to1 of x/[x²+(1−x)²] with respect to x.

**Answer format:** Decimal rounded to four places.

### Q15. [1 Mark] [MCQ]

For Boolean variables x,y,z, let F=(x AND y) OR ((NOT x) AND z). When y=z, which expression always equals F?

A. x
B. NOT y
C. x XOR y
D. y

### Q16. [1 Mark] [NAT]

A direct-mapped cache has four lines, one word per line, with block number b mapped to line b modulo4. Initially empty, it receives word-block references0,1,4,1,0,1. How many hits occur?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

Assume mathematical integer arithmetic and no aliasing. In the code below, which statements are correct?

```text
p = a + b
b = b + 1
q = a + b
r = a + b
```

A. q may always be replaced by p.
B. r may be replaced by q.
C. The assignment to b kills availability of the original a+b value for q.
D. The repeated textual spelling alone proves all three sums equal.

### Q18. [1 Mark] [NAT]

A depth-first search starts at vertex a in an undirected graph with edges ab,ac,bd,cd,ce. Neighbours are examined alphabetically. How many tree edges lie on the DFS-tree path from a to e?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

A connected undirected graph has distinct edge weights, and e is the unique heaviest edge on a cycle. Which statements are correct?

A. Every spanning tree contains e.
B. Deleting e leaves the graph connected.
C. No minimum spanning tree contains e.
D. e must be the heaviest edge of the entire graph.

### Q20. [1 Mark] [MCQ]

A router forwards an IPv4 datagram from one Ethernet link to another. Assume no tunnelling or network address translation. Which pair of fields is necessarily replaced with values appropriate to the outgoing link?

A. Source and destination IPv4 addresses
B. Source and destination TCP port numbers
C. Ethernet source and destination MAC addresses
D. Application sequence numbers

### Q21. [1 Mark] [NAT]

A directed graph has edges s→a of weight0, a→b of weight0, b→t of weight4, and s→t of weight5. A programmer adds the same positive integer c to every edge weight before finding a shortest path. What is the smallest c for which the direct edge s→t becomes strictly cheaper than the three-edge route?

**Answer format:** Integer.
### Q22. [1 Mark] [MSQ]

Two threads execute atomic fetch-and-add(counter,1), each exactly once, with counter initially0. Each operation returns the value before its increment. Which statements must hold after both finish?

A. The final counter is2.
B. Both operations return0.
C. The two returned values are0 and1 in some order.
D. The thread that starts first must receive0, even if it is delayed before executing its atomic operation.

### Q23. [1 Mark] [NAT]

A DMA controller transfers a block of64 bytes using eight-byte bus transactions. After every two DMA transactions it relinquishes the bus, except that it finishes immediately after its last transaction. How many relinquishments occur before transfer completion?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Two store-and-forward links in series each transmit at1000 bits/s. Propagation and processing delays are zero. A1000-bit message is split into two equal packets with no headers. Transmission starts at time0. At what time, in seconds, does the last bit reach the destination?

**Answer format:** Exact decimal.

### Q25. [1 Mark] [MSQ]

For the grammar S→aSb | SS | ε, which statements are correct?

A. Every generated string contains equally many a's and b's.
B. Every generated string has all a's before all b's.
C. The string abab is generated.
D. The string ba is generated.

### Q26. [1 Mark] [NAT]

On R(A,B,C,D), the functional dependencies are A→B, B→C and AC→D. How many attributes are in the closure of A under these dependencies?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

P holds a single-instance resource R and waits for S. Q holds the single instance of S but is running and will release it without requesting another resource. No other processes or requests exist. Which statement is justified?

A. P and Q are already deadlocked because P waits.
B. A circular wait exists through R and S.
C. Q must be waiting for R implicitly.
D. The stated resource situation does not form a deadlock.

### Q28. [1 Mark] [NAT]

A four-variable Boolean function is1 exactly when the two least significant input bits are equal; the two other bits are unrestricted. In a minimum sum-of-products representation without don't-cares, what is the total number of literal occurrences?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

Five real observations all lie in [−1,1], have mean0, and have median0. What is the largest possible population variance?

**Answer format:** Exact decimal.
### Q30. [1 Mark] [NAT]

An undirected simple graph with six vertices is stored in adjacency lists, with each undirected edge recorded at both endpoints. There are14 neighbour entries. Three vertices have degrees1,2,3. What is the sum of the degrees of the other three vertices?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

In a group, distinct nonidentity elements a,b satisfy a²=b²=e. Which statements are correct?

A. (ab)^(−1)=ba.
B. The group must be abelian.
C. If a and b commute, ab has order2.
D. If ab has order2, a and b commute.

### Q32. [1 Mark] [MSQ]

An undirected graph consists of triangles abc and def together with the single connecting edge cd. Which statements are correct?

A. It has a perfect matching.
B. Every perfect matching contains cd.
C. It is bipartite.
D. Its minimum vertex cover has size3.

### Q33. [1 Mark] [NAT]

A binary error-detecting code consists of all four-bit words having even parity. A valid transmitted word suffers exactly two distinct bit flips. How many of the six possible error-position pairs are detected by an even-parity check?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

A pushdown automaton recognizes {a^n b^n : n≥0}. It pushes one marker per a, then pops one per b, rejecting any a after a b. Which extra condition is needed to avoid accepting strings with fewer b's than a's?

A. Accept as soon as the first b is read.
B. At end of input, require that no unmatched a markers remain.
C. Require at least one input symbol.
D. Ignore the stack once any b has been read.

### Q35. [1 Mark] [NAT]

How many three-element subsets of {1,2,3,4,5,6,7} contain4 and contain no pair of consecutive integers?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

A lexer uses maximal munch, breaking equal-length ties by rule priority. Its tokens include INTEGER=[0-9]+, REAL=[0-9]+\.[0-9]*, and RANGE=\.\., where an escaped dot denotes a literal dot. A single dot is not a token. For input1..2, which statements are correct?

A. The first token under these rules is REAL with lexeme `1.`.
B. Giving RANGE highest priority makes the first token INTEGER with lexeme1.
C. After the first token, scanning encounters a dot at which no token can start.
D. Requiring at least one digit after the dot in REAL would allow the tokenization INTEGER,RANGE,INTEGER.

### Q37. [2 Marks] [MSQ]

Let L={a^n b^n : n≥0}, and define K={w : there exists z in b* such that wz is in L}. Which statements are correct?

A. aaab belongs to K.
B. abb belongs to K.
C. K is context-free.
D. K is regular.
### Q38. [2 Marks] [NAT]

A strip of length6 is tiled with unit tiles and length-two tiles. Two length-two tiles may not be adjacent. Tiles of the same length are indistinguishable. How many different left-to-right tilings exist?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

Construct the usual predictive parsing table for grammar S→AB, A→aA | ε, B→bB | a, with start symbol S and end marker $. Count cells that contain more than one production; count a conflicting cell once regardless of how many productions it contains. How many such cells are there?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

On domain D={1,2,3}, how many binary relations R satisfy (for every x there exists y with R(x,y)) but do not satisfy (there exists y such that R(x,y) for every x)?

**Answer format:** Integer.

### Q41. [2 Marks] [MSQ]

Let u,v be nonzero real column vectors of length3 satisfying vᵀu=1, and let A=I−uvᵀ. Which statements are correct?

A. A is invertible.
B. The nullspace of A is precisely the span of u.
C. Ax=b is solvable exactly when vᵀb=0.
D. A²=A.

### Q42. [2 Marks] [MCQ]

What does this C program print? All pointer accesses are valid.

```c
#include <stdio.h>
int main(void) {
    int u[] = {1, 3, 5}, v[] = {2, 4, 6};
    int *p[] = {u, v};
    int **q = p;
    int *tmp = q[0];
    q[0] = q[1];
    q[1] = tmp;
    q[0]++;
    *q[0] += *q[1];
    printf("%d %d\n", v[1], u[0]);
    return 0;
}
```

A. 4 2
B. 5 1
C. 4 1
D. 5 2
### Q43. [2 Marks] [NAT]

An in-order five-stage pipeline has stages IF,ID,EX,MEM,WB. Every stage takes one cycle except EX for a multiplication, which occupies EX for three consecutive cycles. While EX is occupied, an instruction in ID and all following instructions stall. Each instruction uses MEM and WB for one cycle even if it has no memory operation. There are no data dependencies, branches, or memory stalls, and no separate multiplier. Six instructions execute, with multiplications at positions2 and5 and ordinary instructions elsewhere. Starting with instruction1 in IF in cycle1, in which cycle does instruction6 finish WB?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A Boolean minimization problem has prime implicants P,Q,R,S. Their covered required minterms and literal costs are:

| Implicant | Covered minterms | Literal cost |
|---|---|---:|
| P | 0,1,2 | 3 |
| Q | 2,3 | 2 |
| R | 0,3 | 2 |
| S | 1,2 | 2 |

All required minterms are0,1,2,3. A cover may use only these implicants. What is the minimum total literal cost of a cover?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

For nonnegative integers n, the function below performs no memoization. Count every call, including calls that immediately return.

```text
F(n):
    if n <= 1: return n
    return F(n-1) + F(n-2)
```

When F(6) is evaluated, how many calls have argument2?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A byte-addressed machine uses eight-byte words. A load instruction's effective byte address is Rb+8Ri+d. Initially Rb=1000 and Ri=3. Memory at byte address1032 holds the integer7. Execute LOAD Rj,[Rb+8Ri+8], then set Ri=Rj−2, then execute LOAD Rk,[Rb+8Ri−8]. What is the effective byte address of the second load?

**Answer format:** Integer.

### Q47. [2 Marks] [MSQ]

A four-bit two's-complement ALU computes subtraction as A+(bitwise NOT B)+1 and discards the final carry. For A=0111 and B=1111, which statements are correct?

A. The four result bits are1000.
B. There is a final carry-out of1.
C. Signed overflow occurs.
D. Interpreting the operands as unsigned integers, the subtraction needs a borrow.

### Q48. [2 Marks] [NAT]

A single CPU uses nonpreemptive shortest-job-first scheduling. At each completion it chooses the ready process with the smallest CPU burst. Processes are A(arrival0,burst5), B(1,2), C(2,1), D(6,1). Ties use earlier arrival. There is no context-switch overhead. What is the average waiting time of the four processes?

**Answer format:** Exact decimal in time units.

### Q49. [2 Marks] [NAT]

A disk head starts at cylinder50 moving upward on cylinders0 through99. Requests70 and20 are pending. A request60 arrives exactly when the head reaches65. The head moves one cylinder per time unit and service takes zero time. Under LOOK it continues upward to the last pending request in that direction, then reverses; it does not reverse early for a new request behind it. What total distance is travelled before all three requests are served?

**Answer format:** Integer cylinders.

### Q50. [2 Marks] [NAT]

An initially free64-KiB region is managed by a binary buddy allocator. Each request is rounded up to the smallest power-of-two KiB block that fits it. Splitting always allocates the lowest-address available suitable descendant; free buddies coalesce immediately. Requests A=9KiB, B=9KiB, C=17KiB are allocated in that order. A is then freed. What is the size, in KiB, of the largest request that can now be satisfied without freeing B or C?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

In an idealized CSMA/CD network, the farthest stations have a one-way propagation time of12 microseconds. A100-Mbit/s transmitter must still be transmitting at the latest possible collision-detection instant. Ignoring all encoding overhead and assuming a collision can occur just before a distant station first senses the transmission, what is the minimum frame length in bytes?

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

Records have fields (department,score,id). A stable sorting routine is available. The desired order is department ascending, then score descending, preserving original order for records tied on both fields. Which procedures always achieve that order?

A. Stable sort by score descending, then stable sort by department ascending.
B. Stable sort by department ascending, then stable sort by score descending.
C. One stable sort using the lexicographic key (department,negative score).
D. First reverse the entire input, then use procedure A.

### Q53. [2 Marks] [NAT]

A heap file has100 data pages. A noncovering secondary index identifies8 qualifying records, whose record identifiers refer to pages7,7,19,44,44,44,80,80. The index lookup costs3 page reads. The buffer is initially empty but can retain all accessed pages. Ignoring output writes and counting each distinct fetched page once, how many page reads are needed to retrieve all qualifying records using this index?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

An array A[0..5] is initially [1,2,3,4,5,6]. The following assignments are performed in the stated order, in place:

```text
for i = 1 to 5:
    A[i] = A[i] + A[i-1]
for i = 5 down to 1:
    A[i] = A[i] - A[i-1]
```

What is the sum of A's elements afterward?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

A proposed proof that {a^n b^n : n≥0} is not regular takes pumping length p and word a^p b^p. Which statements correctly describe the regular-language pumping lemma argument?

A. Every permitted decomposition with |xy|≤p and |y|>0 has y consisting only of a's.
B. Choosing the one convenient decomposition x=ε,y=a is sufficient by itself.
C. For every permitted decomposition, pumping y zero times produces a word outside the language.
D. The pumping length may be chosen after seeing an arbitrary decomposition of an arbitrarily short word.

### Q56. [2 Marks] [NAT]

For Boolean inputs a,b,c, a circuit computes p=NAND(a,b), q=NAND(a,c), r=NAND(b,c), u=NAND(p,q), v=NAND(u,u), and F=NAND(v,r). Consider two otherwise identical faulty copies: in one, p is permanently0; in the other, p is permanently1. All other gates work normally. For how many of the eight input assignments do the two faulty copies produce different F outputs?

**Answer format:** Integer.
### Q57. [2 Marks] [NAT]

A syntax-directed definition for binary strings uses S→S1 b and S→b, where b is0 or1. For S→b, set S.val=b and S.len=1. For S→S1 b, set S.val=S1.val+2^(S1.len)·b and S.len=S1.len+1. What is S.val for the string10110?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A distance-vector router X has neighbours Y and Z with link costs2 and5. Their advertised distances to destination D are respectively7 and0, so X initially routes through Z. The X–Z link fails; X receives no new advertisement from Y before recomputing. Y's advertised7 was itself based on routing through X before the failure. Using the stored advertisements exactly as stated, what distance does X now advertise to D? No split horizon or poison reverse is used.

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

An IPv4 datagram has a20-byte header and1800 bytes of payload. It traverses a link with MTU620 bytes, then one with MTU420 bytes. All fragments use20-byte headers; fragments are not reassembled between links. Each router makes each nonfinal fragment as large as permitted by eight-byte alignment. How many fragments reach the destination?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

Let HALT={(M,w): M eventually halts on w}. Assume a computable many-one reduction from HALT to a language L. Which conclusions follow?

A. L cannot be decidable.
B. L must be recursively enumerable.
C. A decider for L would yield a decider for HALT.
D. The existence of this reduction alone guarantees a computable many-one reduction from L to HALT.

### Q61. [2 Marks] [NAT]

A B+ tree has maximum three keys per leaf and maximum four children per internal node. Leaves hold data keys only. Insert into a leaf in sorted order; when it reaches four keys, split into two leaves with two keys each and copy the smallest key of the right leaf upward. Initially the root has separator30 and two leaves [10,20] and [30,40,50]. Insert35, then45, then15. No deletion occurs. How many separator keys are in the root at the end?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

For real constants a,b, define f(x)=(sqrt(1+x)−1)/x when x>0 and f(x)=ax+b when x≤0. Choose a,b so that f is differentiable at0. What is a+b?

**Answer format:** Exact decimal.
### Q63. [2 Marks] [NAT]

A hash table has slots0 through6 and uses linear probing with h(k)=k modulo7. Insert keys0,7,14,1 in that order. Delete7 by marking its slot EMPTY rather than using a tombstone or moving entries. A search stops at the first EMPTY slot. How many of the remaining three stored keys are now incorrectly reported absent by their ordinary searches?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A synchronous circuit has two flip-flops storing bits A,B. Their next-state equations are A'=A XOR B and B'=NOT A, both evaluated from the old state. Starting at(A,B)=(0,0), what is the smallest positive number of clock edges after which the circuit returns to(0,0)?

**Answer format:** Integer.

### Q65. [2 Marks] [MCQ]

For n=2^k with k≥1, determine the tight asymptotic running time of this code. Every execution of work() costs one unit.

```text
i = n
while i >= 1:
    j = i
    while j <= n:
        work()
        j = 2*j
    i = i/2
```

A. Θ(log n)
B. Θ(n)
C. Θ((log n)²)
D. Θ(n log n)





---

## ANSWER KEY — MOCK TEST 027

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 6 |
| 3 | NAT | 1 | 50 |
| 4 | NAT | 1 | 4 |
| 5 | MCQ | 1 | A |
| 6 | NAT | 2 | 2.0000 (accepted range 1.99995–2.00005) |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 12 |
| 9 | MSQ | 2 | A, C, D |
| 10 | NAT | 2 | 24 |
| 11 | MSQ | 1 | A, C |
| 12 | NAT | 1 | 12 |
| 13 | MSQ | 1 | B, C |
| 14 | NAT | 1 | 0.7854 (accepted range 0.78535–0.78545) |
| 15 | MCQ | 1 | D |
| 16 | NAT | 1 | 2 |
| 17 | MSQ | 1 | B, C |
| 18 | NAT | 1 | 4 |
| 19 | MSQ | 1 | B, C |
| 20 | MCQ | 1 | C |
| 21 | NAT | 1 | 1 |
| 22 | MSQ | 1 | A, C |
| 23 | NAT | 1 | 3 |
| 24 | NAT | 1 | 1.5 |
| 25 | MSQ | 1 | A, C |
| 26 | NAT | 1 | 4 |
| 27 | MCQ | 1 | D |
| 28 | NAT | 1 | 4 |
| 29 | NAT | 1 | 0.8 |
| 30 | NAT | 1 | 8 |
| 31 | MSQ | 1 | A, C, D |
| 32 | MSQ | 1 | A, B |
| 33 | NAT | 1 | 0 |
| 34 | MCQ | 1 | B |
| 35 | NAT | 1 | 4 |
| 36 | MSQ | 2 | A, C, D |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 9 |
| 39 | NAT | 2 | 1 |
| 40 | NAT | 2 | 174 |
| 41 | MSQ | 2 | B, C, D |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 14 |
| 44 | NAT | 2 | 4 |
| 45 | NAT | 2 | 5 |
| 46 | NAT | 2 | 1032 |
| 47 | MSQ | 2 | A, C, D |
| 48 | NAT | 2 | 2.25 |
| 49 | NAT | 2 | 70 |
| 50 | NAT | 2 | 16 |
| 51 | NAT | 2 | 300 |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 7 |
| 54 | NAT | 2 | 21 |
| 55 | MSQ | 2 | A, C |
| 56 | NAT | 2 | 5 |
| 57 | NAT | 2 | 13 |
| 58 | NAT | 2 | 9 |
| 59 | NAT | 2 | 6 |
| 60 | MSQ | 2 | A, C |
| 61 | NAT | 2 | 2 |
| 62 | NAT | 2 | 0.375 |
| 63 | NAT | 2 | 2 |
| 64 | NAT | 2 | 3 |
| 65 | MCQ | 2 | C |
