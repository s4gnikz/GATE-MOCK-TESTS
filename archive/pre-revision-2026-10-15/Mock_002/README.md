# GATE CS 2027 — Full-Length Mock Test 002

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

- Attempt all 65 questions within 180 minutes.
- MCQ: select exactly one of four options. Incorrect 1-mark MCQ: −1/3; incorrect 2-mark MCQ: −2/3.
- MSQ: select every correct option. There is no partial credit and no negative marking.
- NAT: enter a numerical answer, using the stated precision. There is no negative marking.
- Unattempted questions receive zero marks.

---

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

A merge-sort call has already sorted its left half as [2,6,9] and its right half as [1,4,8]. The original positions of every left-half element precede every right-half element. A cross inversion is a pair consisting of a left-half value and a smaller right-half value. How many cross inversions must this merge count?

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

A binary search tree stores distinct keys. A node x has both a left and a right child. Its inorder successor s is used when deleting x. Which statements about s in the tree before deletion are necessarily true?

A. s is in the right subtree of x.  
B. s must be a leaf.  
C. s has no left child.  
D. s may have a right child.  

### Q17. [1 Mark] [NAT]

An epsilon-NFA has states 0,1,2,3, initial state0, and these transitions; unlisted transitions have empty target sets.
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

Routers A,B,C use synchronous distance-vector updates for destination C. Link costs are A–B=1, B–C=1 and A–C=10. Initially routes are converged. Link B–C fails immediately before round1. In every round each router recomputes its distance using its still-working links and the neighbours' distances from the end of the preceding round; C always advertises0. No split horizon, poison reverse or triggered intermediate updates are used. What distance does A advertise after round2?

**Answer format:** Numeric value; integer.

### Q21. [1 Mark] [MSQ]

A binary floating-point system retains three significant binary digits, including the leading1. Exponents are unbounded, and every result is rounded to nearest, ties to even. Which statements are correct?

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

For the following straight-line code, a variable is live at a point if its current value may be read later before being overwritten. There are no implicit uses after return. Which set is exactly the set of live variables immediately before the statement x=0?
```text
x = a + b
y = x + c
x = 0
return y
```

A. {y}  
B. {x,y}  
C. {c,y}  
D. {a,b,c,y}  

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

A. 1NF but not2NF  
B. 2NF but not3NF  
C. 3NF but not BCNF  
D. BCNF  

### Q29. [1 Mark] [NAT]

Dataset A contains 3 observations with mean 2 and population variance 2. Dataset B contains 2 observations with mean 7 and population variance 1. What is the population variance of their combined five observations? Use division by the population size, not by one less than that size.

**Answer format:** Numeric value; 1 decimal places.

### Q30. [1 Mark] [NAT]

An IPv4 fragment arrives with total length1020 bytes, header length20 bytes, fragment offset100, and MF=1. A router forwards it through an interface with MTU620 bytes and fragments it into the minimum number of fragments, using the largest permitted payload in the first new fragment. Every outgoing header is20 bytes. What is the fragment-offset field of the second outgoing fragment?

**Answer format:** Numeric value; integer.

### Q31. [1 Mark] [NAT]

A disk has cylinders0 through99. Its head is at50, moving toward larger cylinder numbers. Pending requests are at10,40,70,90; all are present initially and no new requests arrive. LOOK scheduling reverses at the last pending request in its current direction, not at the physical disk boundary. Ignoring rotational latency, what is the total head movement required to serve all four requests?

**Answer format:** Numeric value; integer.

### Q32. [1 Mark] [MCQ]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, each one cycle. There is no forwarding and no automatic stalling. Register writes occur in the first half of a cycle and ID reads in the second half, so ID may read a value written in WB during the same cycle. The instructions below use ordinary integer registers; R0 is always available. What is the minimum total number of NOP instructions that must be inserted without reordering?
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

A sorted data file has fixed-length records, with exactly eight records per data page and no unused slots. A range query matches exactly16 consecutive records in file order. An index lookup requires exactly two page reads and identifies the first matching record's page and slot. Index pages are separate from data pages, no page is initially cached, and scanning the range reads each needed data page once. What is the largest possible total number of page reads, over the possible starting slots?

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

### Q36. [2 Marks] [NAT]

A processor uses 16-bit instructions and has 16 registers. Each register operand occupies four bits. In a two-register instruction, the first eight bits form the opcode. In a one-register instruction, the first twelve bits form the opcode. A zero-register instruction uses all sixteen bits as its opcode. Decoding must be unambiguous: no complete opcode may be a prefix of another complete opcode. Exactly 200 two-register opcodes and 800 one-register opcodes are allocated. What is the maximum number of distinct zero-register instructions that can also be allocated?

**Answer format:** Numeric value; integer.

### Q37. [2 Marks] [NAT]

A B+ tree stores at most three keys in each leaf and at most three child pointers in each internal node. Its root initially has separator keys [20,40] and these three leaves, from left to right:

```text
[5,10,15]   [20,25,30]   [40,45,50]
```

Every separator is the smallest key in its right child subtree. Insert 35 and then 55. A leaf overflowing to four keys splits into two leaves with two keys each. An internal node overflowing to four children splits into two nodes with two children each; the boundary separator moves to its parent. Splitting the root creates a new root. Existing nodes are reused as one of the split halves. How many nodes, including the root and all leaves, exist after both insertions?

**Answer format:** Numeric value; integer.

### Q38. [2 Marks] [MSQ]

A simple undirected graph has vertices A,B,C,D. Edges AB,BC,CD,DA each have weight 1; diagonals AC and BD each have weight 2. Which statements are correct?

A. The graph has exactly four distinct minimum spanning trees.  
B. At least one minimum spanning tree contains AC.  
C. Every minimum spanning tree consists of three edges of weight 1.  
D. If only the weight of AB is reduced to 0, the minimum spanning tree becomes unique.  

### Q39. [2 Marks] [NAT]

Six positions around a circle are filled with two red, two blue and two green beads. Beads of the same colour are indistinguishable. Adjacent positions, including the last and first, must have different colours. Arrangements related by rotation are identified; reflections are counted separately unless a rotation already identifies them. How many arrangements are there?

**Answer format:** Numeric value; integer.

### Q40. [2 Marks] [MCQ]

Let e_n be the number of binary strings of length n that have no consecutive 1s and contain an even number of 1s. The empty string is counted, so e_0=1. Which formal ordinary generating function E(x)=sum over n>=0 of e_n*x^n is correct?

A. (1+x)/(1-x-x^2)  
B. (1-x+x^3)/(1-2x+x^2-x^4)  
C. 1/(1-x-x^2)  
D. (1-x)/(1-2x+x^2-x^4)  

### Q41. [2 Marks] [MCQ]

A router must advertise exactly all IPv4 addresses from 10.4.1.0 through 10.4.6.255, inclusive, using ordinary CIDR prefixes. No address outside this interval may be covered, and no exception routes are allowed. What is the smallest number of prefixes required?

A. 2  
B. 3  
C. 4  
D. 6  

### Q42. [2 Marks] [MSQ]

Two private hosts, 10.0.0.1 and 10.0.0.2, each initiate a TCP connection from local port 5000 to 203.0.113.8 port 443. A NAT gateway uses the single public IPv4 address 198.51.100.6 and assigns distinct public source ports 41001 and 41002 to these connections. Packets are unfragmented. Which statements are correct for this port-translating NAT?

A. A reply arriving at public port 41002 can be mapped back to 10.0.0.2 port 5000.  
B. The remote server sees both connections as originating from the respective private IPv4 addresses.  
C. Translating the source IPv4 address of an outgoing packet requires updating its IPv4 header checksum.  
D. Translating the source IPv4 address and TCP source port requires updating the TCP checksum because both affect its checksum calculation.  

### Q43. [2 Marks] [MCQ]

Free holes, in increasing address order, have sizes 100,500,200,300,600 units. Four processes request 212,417,112,426 units, in that order. Compare first-fit with best-fit, each starting from the original holes. Allocations split holes without overhead; processes never release memory, holes are nonadjacent, and an unsatisfied request is skipped. First-fit scans from the lowest address for every request. What are the largest remaining hole sizes under (first-fit, best-fit), respectively?

A. (300,174)  
B. (183,174)  
C. (300,183)  
D. (174,300)  

### Q44. [2 Marks] [MSQ]

R is a binary relation on a finite nonempty domain. Use the following properties:

- E: for every x there exists y such that R(x,y).
- T: R is transitive.
- I: R is irreflexive.
- S: R is symmetric.
- F: for each x, at most one y satisfies R(x,y).

Which listed combinations admit a model on some finite nonempty domain? Properties not listed in an option impose no condition.

A. E, T, I  
B. E, S, I, F  
C. E, T, I, F  
D. E, T, S  

### Q45. [2 Marks] [MCQ]

An 8-bit ALU computes A-B using A+(NOT B)+1. It reports the low eight result bits, carry-out C, result sign bit N, and signed overflow flag V. Carry-out 1 means no unsigned borrow. For A=10000000 and B=00000001, which pair correctly gives the truth values of (A < B under signed two's-complement interpretation, A < B under unsigned interpretation)?

A. (false,false)  
B. (true,false)  
C. (false,true)  
D. (true,true)  

### Q46. [2 Marks] [NAT]

Consider the following basic block. Pointers p and q each point to a valid ordinary integer object; they may point to the same object. No other thread accesses these objects, and there are no volatile objects. All five scalar outputs a,b,c,d,e and the final memory contents must be preserved for every initial memory state.

```text
a = *p
b = *q
*p = 7
c = *q
d = *p
e = *q
return (a,b,c,d,e)
```

An optimizer may reuse already obtained values and constants, but may not insert pointer comparisons, conditional branches, speculative loads or additional stores. The original store must remain between the initial reads and the final outputs. What is the minimum number of memory-load operations needed by such an equivalent block? Loading a pointer's stored address is not counted; count only reads of the pointed-to integer objects.

**Answer format:** Numeric value; integer.

### Q47. [2 Marks] [MSQ]

The Boolean function F=AB+(NOT A)C is implemented directly as a two-level AND-OR circuit, with a separate inverter generating NOT A. Gate delays are positive and may differ. Only one primary input changes at a time, after the circuit has settled. Which statements are correct?

A. Adding the product term BC does not change the Boolean function.  
B. With B=C=1, a change of A can produce a temporary 0 at the output for some gate delays.  
C. Adding the product term ABC guarantees removal of this possible temporary 0 for every choice of positive gate delays.  
D. Adding the product term BC guarantees removal of this possible temporary 0 during changes of A with B=C=1.  

### Q48. [2 Marks] [MCQ]

For initially committed data items x and y, consider this complete schedule of two transactions, written in time order:

```text
w1(x); r2(x); w2(y); c2; c1
```

Here wi and ri are writes and reads by transaction Ti, and ci is its commit. The read returns the value from the latest preceding write. Which classification is correct?

A. Conflict-serializable and recoverable, but not cascadeless.  
B. Conflict-serializable but not recoverable.  
C. Recoverable but not conflict-serializable.  
D. Cascadeless and conflict-serializable.  

### Q49. [2 Marks] [NAT]

A process uses a 32-bit virtual address with 4 KiB pages. Two-level paging divides the address into a 10-bit directory index, a 10-bit second-level index, and a 12-bit offset. Every directory and second-level table occupies exactly one 4 KiB physical page. A second-level table is allocated only if it contains at least one valid mapping. Exactly virtual page numbers 0,1023,1024 and 1048575 are mapped. No page-table pages are shared. Including the directory but excluding mapped data pages, how many KiB of physical memory do the page tables occupy?

**Answer format:** Numeric value; integer.

### Q50. [2 Marks] [MCQ]

Over alphabet {a,b}, let L={a,ab}. A pushdown automaton starts with one bottom-of-stack symbol. For empty-stack acceptance, a string is accepted only if all input has been consumed and the stack is empty; no transition is possible once the stack is empty. No right-end marker is supplied. Standard determinism forbids a choice between an epsilon transition and an input-consuming transition for the same state and stack top. Which machine model cannot recognize L?

A. A deterministic finite automaton.  
B. A nondeterministic pushdown automaton accepting by empty stack.  
C. A deterministic pushdown automaton accepting by final state.  
D. A deterministic pushdown automaton accepting by empty stack.  

### Q51. [2 Marks] [MSQ]

Let

```text
L1 = { a^n b^n c^m : n,m >= 0 }
L2 = { a^m b^n c^n : n,m >= 0 }.
```

All exponents are integers. Which statements are correct?

A. L1 union L2 is context-free.  
B. L1 intersection L2 is context-free.  
C. The concatenation L1L2 is context-free.  
D. L1 intersection L2 is regular.  

### Q52. [2 Marks] [MCQ]

Seven distinct keys 1,2,3,4,5,6,7 are arranged in the seven array positions of a complete binary max-heap. The root is position 1, and children of position i are positions 2i and 2i+1 whenever present. Two arrangements differ if any array position contains a different key. How many valid max-heap arrangements exist?

A. 40  
B. 64  
C. 80  
D. 120  

### Q53. [2 Marks] [MCQ]

A directed multigraph on vertices 1,2,3 has adjacency matrix M, where Mij is the number of distinct edges from i to j:

```text
M = [0 2 1]
    [1 0 1]
    [0 1 1].
```

A walk of length two is an ordered sequence of two edges with matching intermediate vertex. Count walks that end at their starting vertex, summing over all three possible starting vertices. Parallel edges distinguish walks, a self-loop may be traversed twice, and the starting vertex is part of the walk. How many such walks exist?

A. 4  
B. 5  
C. 7  
D. 9  

### Q54. [2 Marks] [NAT]

Let A be the real 4x4 matrix

```text
A = [0 1 0 0]
    [0 0 1 0]
    [0 0 0 1]
    [1 0 0 0].
```

How many real matrices X simultaneously satisfy X=X^T, AX=XA, X^2=X, and X*(1,1,1,1)^T=0?

**Answer format:** Numeric value; integer.

### Q55. [2 Marks] [MCQ]

Two transactions each increment the same data item x by reading it and later writing the incremented value. Both initially hold compatible shared locks on x and then request an upgrade to an exclusive lock without releasing their shared locks. A transaction retains every lock until commit. Which statement is correct?

A. The upgrades can deadlock even though retaining locks until commit prevents another transaction from reading an uncommitted write.  
B. The second upgrade must succeed because shared locks are compatible.  
C. Releasing each shared lock before requesting its exclusive lock always preserves two-phase locking.  
D. If both transactions instead request an exclusive lock before reading x and hold it until commit, a lost update remains possible in a completed execution.  

### Q56. [2 Marks] [MCQ]

What does the following conforming C program print? All arithmetic fits in int.

```c
#include <stdio.h>
static void change(int **p, int *q) {
    int *t = *p;
    *p = q;
    *t += **p;
    **p += 1;
}
int main(void) {
    int a[3] = {2,5,9};
    int *p = a;
    change(&p, a+1);
    change(&p, a);
    printf("%d %d %d\n", a[0], a[1], (int)(p-a));
    return 0;
}
```

A. 7 13 0  
B. 8 13 0  
C. 8 6 1  
D. The program has undefined behaviour due to pointer aliasing.  

### Q57. [2 Marks] [MCQ]

A lexer has the token rules `a`, `b`, `d`, and `ab*c`, where `b*` means zero or more b symbols. It uses longest match. An implementation reads forward until no token rule can still match, then returns to the most recent accepting position to emit that token. Consider the inputs `ab^n d`, with no spaces and arbitrary integer n>=1. Before returning the first token, how much lookahead beyond the most recent accepting position can this implementation require?

A. At most one character, independently of n.  
B. At most two characters, independently of n.  
C. An amount unbounded as n grows.  
D. Zero, because the rule `a` can be emitted immediately upon reading a.  

### Q58. [2 Marks] [MSQ]

A directed graph has exactly these weighted edges:

```text
s -> a :  2
s -> b :  5
b -> a : -4
a -> t :  2
b -> t : 10
```

For the version of Dijkstra's algorithm in this question, the unsettled vertex with smallest tentative distance is settled, settled vertices are never revised, and the algorithm stops when t is settled. Which statements are correct?

A. The true shortest-path distance from s to t is 3.  
B. The specified Dijkstra algorithm returns 4 on this graph.  
C. Adding 4 to every edge weight leaves the identity of a shortest s-to-t path unchanged.  
D. The negative edge implies that the graph contains a negative-weight directed cycle.  

### Q59. [2 Marks] [MSQ]

Consider the augmented grammar with start symbol S:

```text
S' -> S
S  -> a S b S | epsilon
```

Use standard LL(1), LR(0), and SLR(1) constructions, with end marker $. Which statements are correct?

A. The grammar is LL(1).  
B. The grammar is ambiguous.  
C. The grammar is SLR(1).  
D. The grammar is LR(0).  

### Q60. [2 Marks] [MSQ]

An inode contains four direct pointers, one single-indirect pointer and one double-indirect pointer. A block is 1024 bytes and each pointer is 4 bytes. Indirect blocks contain only pointers. A nonsparse file contains exactly 263 completely full data blocks, numbered logically from 0. Allocate only the indirect blocks needed for these data blocks. The inode is already in memory. Which statements are correct?

A. Exactly three indirect blocks are allocated.  
B. With no other blocks cached, reading the data in logical block 260 requires three block reads, including the data block.  
C. Logical block 259 is reached through the double-indirect pointer.  
D. The file contains 269312 bytes of data.  

### Q61. [2 Marks] [NAT]

A TCP sender's congestion window is 10000 bytes. Its latest received cumulative acknowledgement advertises a receive window of 6500 bytes, measured from that acknowledgement's next expected byte. The sender currently has 4000 bytes outstanding beyond that same acknowledgement. No new acknowledgement or window update arrives. Ignoring implementation restrictions and allowing a final segment smaller than the maximum segment size, how many additional data bytes may it transmit without exceeding either window?

**Answer format:** Numeric value; integer.

### Q62. [2 Marks] [MCQ]

Let L={a^(n^2) : n is a nonnegative integer}. A proof assumes that L is regular, takes a pumping length p>=1, and chooses w=a^(p^2). Which continuation correctly contradicts the regular-language pumping lemma?

A. In every permitted decomposition w=xyz, y must have length p; pumping twice gives a length outside L.  
B. In every permitted decomposition w=xyz, 1<=|y|<=p; pumping twice gives a length strictly between p^2 and (p+1)^2.  
C. It suffices to choose one permitted decomposition with |y|=1 and show that pumping it twice leaves L.  
D. Pumping down always gives the immediately preceding square length (p-1)^2, which contradicts regularity.  

### Q63. [2 Marks] [MCQ]

In the covering stage of tabular Boolean minimization, the following is the complete prime-implicant chart. Column labels denote the six required on-set minterms; don't-care minterms, if any, need not be covered. A mark means the prime implicant covers that required minterm. Use only these prime implicants. Minimize the number of selected product terms first, then the total literal count among covers with that minimum term count.

| Prime implicant | m1 | m2 | m3 | m4 | m5 | m6 | Literals |
|---|---|---|---|---|---|---|---:|
| P1 | X | X | X | | | | 2 |
| P2 | X | | | X | X | | 3 |
| P3 | | X | | X | | X | 3 |
| P4 | | | X | | X | X | 4 |

Which set is selected by this criterion?

A. {P1,P2}  
B. {P1,P3,P4}  
C. {P1,P2,P3}  
D. {P2,P3,P4}  

### Q64. [2 Marks] [MCQ]

A microprogram must start one memory read at the address in MAR, wait until READY=1, copy the returned data into MDR, and increment register R exactly once. All microinstruction operations execute once on every cycle in which that microinstruction is visited. A START pulse begins a transaction; issuing START again before completion begins an unwanted second transaction. READY remains 0 until the transaction completes and then remains 1 until the routine exits. Which routine meets the requirements for every finite memory latency? A branch tests READY at the end of its cycle.

A. U: START; R=R+1; if READY=0 goto U else goto V. V: MDR=DATA; exit.  
B. U: START; goto V. V: if READY=0 goto V else goto W. W: MDR=DATA; R=R+1; exit.  
C. U: START; goto V. V: R=R+1; if READY=0 goto V else goto W. W: MDR=DATA; exit.  
D. U: START; MDR=DATA; R=R+1; exit.  

### Q65. [2 Marks] [MCQ]

Thirteen distinct keys occupy positions 1 through 13. A tournament finds the minimum as follows: in each round, compare consecutive surviving keys in their current order, keep the smaller from each pair, and give the final unpaired key a bye when the number of survivors is odd. Survivors retain their order. After finding the minimum, find the second-smallest by scanning only the keys that lost directly to the minimum, using one fewer comparisons than the number of these keys. Over all possible initial key orders, what are the (minimum, maximum) possible total numbers of comparisons for both stages together?

A. (12,15)  
B. (13,15)  
C. (14,16)  
D. (15,15)  

---

## ANSWER KEY — MOCK TEST 002

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 20 (exact) |
| 3 | MCQ | 1 | B |
| 4 | MCQ | 1 | C |
| 5 | NAT | 1 | 15 (exact) |
| 6 | MCQ | 2 | B |
| 7 | MCQ | 2 | B |
| 8 | MCQ | 2 | B |
| 9 | MSQ | 2 | A, C |
| 10 | MCQ | 2 | B |
| 11 | NAT | 1 | 4 (exact) |
| 12 | MCQ | 1 | C |
| 13 | NAT | 1 | 6 (exact) |
| 14 | MCQ | 1 | B |
| 15 | MCQ | 1 | B |
| 16 | MSQ | 1 | A, C, D |
| 17 | NAT | 1 | 3 (exact) |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | D |
| 20 | NAT | 1 | 4 (exact) |
| 21 | MSQ | 1 | A, C |
| 22 | MSQ | 1 | A, C |
| 23 | MSQ | 1 | A, D |
| 24 | NAT | 1 | 0.667 (exact) |
| 25 | MCQ | 1 | A |
| 26 | MCQ | 1 | C |
| 27 | NAT | 1 | 2 (exact) |
| 28 | MCQ | 1 | C |
| 29 | NAT | 1 | 7.6 (exact) |
| 30 | NAT | 1 | 175 (exact) |
| 31 | NAT | 1 | 120 (exact) |
| 32 | MCQ | 1 | C |
| 33 | MCQ | 1 | D |
| 34 | MCQ | 1 | C |
| 35 | MSQ | 1 | A, B |
| 36 | NAT | 2 | 1536 (exact) |
| 37 | NAT | 2 | 8 (exact) |
| 38 | MSQ | 2 | A, C |
| 39 | NAT | 2 | 5 (exact) |
| 40 | MCQ | 2 | B |
| 41 | MCQ | 2 | C |
| 42 | MSQ | 2 | A, C, D |
| 43 | MCQ | 2 | A |
| 44 | MSQ | 2 | B, D |
| 45 | MCQ | 2 | B |
| 46 | NAT | 2 | 3 (exact) |
| 47 | MSQ | 2 | A, B, D |
| 48 | MCQ | 2 | B |
| 49 | NAT | 2 | 16 (exact) |
| 50 | MCQ | 2 | D |
| 51 | MSQ | 2 | A, C |
| 52 | MCQ | 2 | C |
| 53 | MCQ | 2 | C |
| 54 | NAT | 2 | 4 (exact) |
| 55 | MCQ | 2 | A |
| 56 | MCQ | 2 | B |
| 57 | MCQ | 2 | C |
| 58 | MSQ | 2 | A, B |
| 59 | MSQ | 2 | A, C |
| 60 | MSQ | 2 | A, B, D |
| 61 | NAT | 2 | 2500 (exact) |
| 62 | MCQ | 2 | B |
| 63 | MCQ | 2 | C |
| 64 | MCQ | 2 | B |
| 65 | MCQ | 2 | B |
