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
