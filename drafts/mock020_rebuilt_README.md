# GATE CS 2027 — Full-Length Mock Test 020

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the others carry two. An incorrect MCQ loses one-third of its assigned marks. MSQs require all correct options, with no partial credit or negative marking. NATs have no negative marking. Unattempted questions score zero. General Aptitude carries15 marks, Engineering Mathematics13 and core CS72. Numerical answers are exact unless rounding is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

Five consecutive readings should form a sequence whose consecutive differences increase by the same amount. The displayed readings are 3,8,16,25,41. Exactly one reading was copied incorrectly. What is the corrected value of that reading?

**Answer format:** Integer.

### Q2. [1 Mark] [MCQ]

A rectangle is cut along a straight segment joining the midpoint of its top side to its bottom-left corner. The resulting triangle and quadrilateral are separated without further cuts. What is the ratio of the triangle's area to the quadrilateral's area?

A. 1:2
B. 1:3
C. 1:4
D. 2:3

### Q3. [1 Mark] [MCQ]

A notice must express that a visitor may enter only when accompanied by a guide, while making no promise that accompaniment alone guarantees entry. Which sentence states precisely this necessary condition?

A. Every visitor accompanied by a guide may enter.
B. A visitor may enter if and only if accompanied by a guide.
C. A visitor may enter only if accompanied by a guide.
D. A visitor may enter unless accompanied by a guide.

### Q4. [1 Mark] [NAT]

Two tanks initially contain equal volumes of liquid. Tank A contains20% salt and tank B contains40% salt, measured by mass; both liquids have the same density, and mixing preserves total mass. One-quarter of A's original liquid is poured into B and mixed. Then the same mass of the resulting mixture is returned to A. What is A's final salt percentage?

**Answer format:** Percentage as a number, without the percent symbol.

### Q5. [1 Mark] [MSQ]

Four switches P,Q,R,S are either ON or OFF. Exactly two are ON. Whenever P is ON, Q is ON. Whenever R is OFF, S is ON. Which statements must hold?

A. P is OFF.
B. At least one of R and S is ON.
C. Q is ON.
D. If Q is OFF, both R and S are ON.

### Q6. [2 Marks] [MCQ]

On a Cartesian plane, operation R rotates a point90 degrees anticlockwise about the origin, and operation M reflects a point in the vertical line x=1. Starting at(2,1), perform R followed by M repeatedly. Where is the point after four such pairs of operations?

A. (2,1)
B. (6,5)
C. (-2,-1)
D. (0,3)

### Q7. [2 Marks] [MCQ]

A library reports: “After online reservations began, the fraction of issued books returned late fell. However, the number of late returns increased because the number of issued books rose substantially. The figures do not identify what would have happened without online reservations.” Which interpretation is justified?

A. Online reservations caused every borrower to return books sooner.
B. A lower late-return fraction is incompatible with more late returns.
C. The number of timely returns must have fallen.
D. A larger borrowing volume can coexist with a lower late-return fraction and more late returns, without establishing a causal effect.

### Q8. [2 Marks] [MSQ]

The distinct letters A,B,C,D,E are arranged in a row, each exactly once. Let X be the set of arrangements where A and B are adjacent in either order, and Y the set where B and C are adjacent in either order. Which statements are correct?

A. X contains48 arrangements.
B. The intersection of X and Y contains24 arrangements.
C. Exactly72 arrangements belong to at least one of X and Y.
D. Exactly36 arrangements belong to neither X nor Y.

### Q9. [2 Marks] [NAT]

A delivery service has two depots. Their on-time delivery percentages are unchanged between two months: depot A is90% on time and depot B is60% on time. In month1, A handles twice as many deliveries as B. In month2, the service-wide on-time rate is75%. Relative to its month1 share, by what percentage has A's share of all deliveries decreased?

**Answer format:** Percentage decrease as a number, without the percent symbol.

### Q10. [2 Marks] [MCQ]

Six unit squares form a cube net. Their centres on a square grid are A=(0,0), B=(1,0), C=(2,0), D=(3,0), E=(1,1), and F=(1,-1). Squares sharing a full edge are hinged, and the net is folded into a cube with labels on the outside. Which pair of faces is opposite, and which triple can meet at one cube vertex?

A. A and C are opposite; A,B,E can meet.
B. B and C are opposite; A,C,E can meet.
C. E and F are opposite; A,B,C can meet.
D. A and D are opposite; B,E,F can meet.


## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A pushdown automaton accepts by final state after consuming its entire input. A proposed modification erases all its stack symbols immediately whenever it first enters any final state, then continues with the original transitions. The original transitions may depend on the stack top. Which statements are correct?

A. The modification can destroy an accepting computation that must leave a final state and read further input.
B. The modification always preserves the accepted language.
C. Entering a final state before input exhaustion does not by itself accept the input.
D. Every final state in every pushdown automaton must have no outgoing transitions.

### Q12. [1 Mark] [NAT]

For Boolean variables a,b,c, let f(a,b,c)=(a AND b) XOR ((NOT a) AND c). For how many assignments of(b,c) does flipping a change f, regardless of a's initial value?

**Answer format:** Integer.

### Q13. [1 Mark] [MCQ]

An8-bit ALU computes subtraction X−Y as X+(bitwise NOT Y)+1, retaining the low8 bits. Let X=10000000 and Y=00000001. Which combination is correct? Carry-out refers to the ninth bit of this addition, and signed overflow refers to two's-complement interpretation.

A. Result01111111; carry-out0; signed overflow0.
B. Result01111111; carry-out1; signed overflow1.
C. Result10000001; carry-out1; signed overflow0.
D. Result01111111; carry-out0; signed overflow1.

### Q14. [1 Mark] [NAT]

Five real observations have mean10 and population variance8, where the variance is the sum of squared deviations divided by the number of observations. One observation equal to14 is removed. What is the population variance of the remaining four observations?

**Answer format:** Exact number.

### Q15. [1 Mark] [NAT]

A binary buddy allocator manages a contiguous1024-byte region and rounds each allocation up to a power of two. Four256-byte blocks at offsets0,256,512,768 are allocated. The blocks at offsets0 and512 are then freed; the others remain allocated. With no relocation, what is the largest single allocation request, in bytes, that can now be satisfied?

**Answer format:** Integer.

### Q16. [1 Mark] [MSQ]

A process uses two distinct virtual pages v1 and v2 as aliases of the same physical frame. A simplified inverted page table stores exactly one pair(process ID, virtual page number) per physical frame. A lookup searches those stored pairs; no auxiliary alias information exists. Which statements are correct?

A. The simplified table can simultaneously represent both aliases in its one entry for the frame.
B. The physical memory arrangement is possible even though the simplified representation cannot encode both aliases.
C. A mapping structure with a list of aliases per physical frame can address this representation problem.
D. Aliasing requires the two virtual page numbers to be equal.

### Q17. [1 Mark] [NAT]

TCP has outstanding data segments covering byte ranges[1000,1500),[1500,2000),[2000,2500), and[2500,3000). A cumulative ACK with acknowledgment number2500 arrives. There is no selective acknowledgment information. How many bytes among these four segments remain unacknowledged by this ACK?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

Let G be the additive group of integers modulo12. Define a group homomorphism f:G→G by f(x)=8x modulo12. How many cosets of the kernel of f are there in G?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

A bipartite graph has left vertices a,b,c and right vertices1,2,3. Its edges are a–1,a–2,b–2,c–2,c–3. Which statements are correct?

A. The graph has exactly one perfect matching.
B. Removing edge a–2 destroys every perfect matching.
C. Edge b–2 belongs to every perfect matching.
D. Adding edge b–1 creates a second perfect matching.

### Q20. [1 Mark] [MCQ]

A two-level AND–OR circuit implements f=ab+(NOT a)c. Assume b=c=1 and only a changes from0 to1. Gate delays are arbitrary positive values; a and NOT a need not change simultaneously. Which extra product term can be ORed into the output without changing f's Boolean function and eliminates the possible static-1 hazard for this transition?

A. (NOT b)(NOT c)
B. a(NOT c)
C. bc
D. (NOT a)(NOT b)

### Q21. [1 Mark] [MSQ]

An undirected triangle has edges AB of weight1, BC of weight2 and AC of weight3. Each weight w is replaced by w−2. Which statements are correct?

A. The set of minimum spanning trees is unchanged.
B. The set of shortest simple A–C paths is unchanged.
C. The minimum spanning-tree weight decreases by4.
D. Subtracting the same constant always preserves comparisons between paths having different numbers of edges.

### Q22. [1 Mark] [NAT]

A min-heap stores distinct keys in a one-based array of length15. A particular key's array index is known to be6. Ignoring its own position, how many other array positions are guaranteed to contain larger keys solely because of the heap-order property?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A control store has64 microinstructions. Each control word contains a next-address field capable of naming any microinstruction, one of four mutually exclusive ALU operations, and five independent Boolean control signals. All fields use the smallest fixed binary encoding that supports the stated choices. How many bits are required per control word?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

A B+ tree's root contains separator20 and has two leaf children: [5,10] and [20,30]. The separator is defined as the minimum key of the right child. Each leaf must contain at least one key. After deleting20, which action is required under this separator convention?

A. Merge the leaves because a leaf cannot contain one key.
B. Change the root separator to30; no merge is required.
C. Leave separator20 because internal separators must never change.
D. Remove the root and discard the left leaf.

### Q25. [1 Mark] [MSQ]

Consider this basic block; on exit only z is live. Variables have ordinary scalar values, and evaluating expressions has no side effects.

```text
1: x = a + b
2: y = x + c
3: x = d + e
4: z = y + x
```

Which statements are correct?

A. Immediately before line3, the old value of x is live.
B. Immediately before line3, y is live.
C. Both assignments to x contribute to the final z.
D. Line1 can be removed merely because line3 also assigns x.

### Q26. [1 Mark] [NAT]

Four identical256×8-bit RAM chips provide a1024×8-bit byte-addressable memory. Address bits A0–A7 connect to every chip's address pins. A decoder selects a chip using A8,A9. How many chips are selected during one valid byte read, and how many distinct byte addresses can be read? Enter the product of these two numbers.

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

In the following code, p and q point to valid integer objects and may alias. Integer overflow does not occur.

```c
int x = *p + 1;
*q = 9;
int y = *p + 1;
```

Which statements are correct for all allowed executions?

A. Replacing the initialization of y by y=x is always valid.
B. If p and q are proved to point to distinct objects, reusing x for y is valid.
C. If p=q and the original pointed-to value is4, x and y differ.
D. The repeated textual expression alone proves that common-subexpression elimination is valid.

### Q28. [1 Mark] [NAT]

A lexer recognizes identifiers matching a letter followed by zero or more letters or digits, integer literals matching one or more digits, and the operators '=', '==', '>'. It uses longest match and skips spaces. How many tokens does it emit for the input below?

```text
a1===23> b
```

**Answer format:** Integer.

### Q29. [1 Mark] [MCQ]

Transaction T writes x, then transaction U reads that new value of x. T subsequently aborts. Which requirement alone directly forces U to abort too, even if U wrote no data?

A. Cascading recovery after a dirty read.
B. The existence of a read–read conflict.
C. Every read-only transaction must abort.
D. Any two transactions accessing one item must be serialized by aborting both.

### Q30. [1 Mark] [NAT]

How many subsets S of {1,2,3,4,5,6} satisfy the rule that, for each i in {1,2,3}, exactly one of i and i+3 belongs to S, and the sum of elements of S is even?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

Over alphabet {0,1}, let L be the set of strings having equal numbers of0s and1s. Which statements are correct?

A. L is regular.
B. L is context-free.
C. The intersection of L with 0*1* is {0^n1^n : n≥0}.
D. L contains only strings in which every0 precedes every1.

### Q32. [1 Mark] [MCQ]

A connected TCP socket receives application writes of lengths3 and5 bytes from its peer. The receiver calls recv with a buffer of8 bytes. Assume no errors and no end-of-stream, but allow arbitrary legal timing. Which statement is correct?

A. The first recv must return exactly3 bytes.
B. The first recv must return exactly8 bytes.
C. A successful positive return may contain bytes spanning both writes.
D. The receiver can infer write boundaries from TCP's byte stream alone.

### Q33. [1 Mark] [NAT]

A sequence satisfies a0=1 and an=2a(n−1)+1 for n≥1. Let A(x)=sum(an x^n), interpreted as a formal power series. What is the coefficient of x^4 in (1−2x)A(x)?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A directed graph has edges s→a of weight2, s→b of weight5, b→a of weight−4 and a→t of weight2. There are no other edges. A flawed Dijkstra implementation permanently settles vertices and refuses to update a settled vertex. Starting at s, by how much does its reported distance to t exceed the true shortest-path distance?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A directed graph on n=6 vertices is represented by six adjacency lists. Self-loops are allowed, and no ordered pair occurs more than once. The sum of all outdegrees is11 and exactly three edges are self-loops. What is the sum of all indegrees?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

Records carry keys(city,year) and a distinct arrival number. The required order is ascending city, then ascending year, with original arrival order retained when both keys tie. Only single-key sorts are available. Which procedures always meet the requirement?

A. Stable sort by year, then stable sort by city.
B. Stable sort by city, then stable sort by year.
C. Stable sort by arrival number, then stable sort by year, then stable sort by city.
D. Arbitrary unstable sort by year, then stable sort by city.

### Q37. [2 Marks] [NAT]

Every memory reference first probes a TLB for2 ns. On a hit, one memory access of80 ns follows. On a miss, a two-level page-table walk performs two sequential80 ns memory accesses, followed by the actual80 ns data access. The TLB hit rate is95%; page faults do not occur, and no operations overlap. A proposed optimization reduces the miss rate to2% but increases every TLB probe to4 ns. What is the reduction in average reference time, in ns?

**Answer format:** Exact number.

### Q38. [2 Marks] [NAT]

The grammar E→E+E | E*E | id has no precedence or associativity rules. For the token string id+id*id+id, how many distinct parse trees have a '+' production at the root?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

A schedule consists of w1(x),w2(x),w1(x), followed by commits after all writes. There are no reads. The first and last writes belong to T1 and the middle write to T2. All writes assign fixed constants independently of prior values. Which statements are correct?

A. Its conflict graph is acyclic.
B. It is view-equivalent to the serial order T2,T1.
C. It is conflict-serializable.
D. Its final writer of x is T1.

### Q40. [2 Marks] [NAT]

An open-addressed hash table has12 slots numbered0–11. For a particular key the probe sequence is (2+8i) modulo12 for i=0,1,2,... . All slots that this sequence can reach are occupied; all other slots are empty. If the secondary step is replaced by5 while the starting slot remains2, how many probes, including the initial probe, are needed to reach the first empty slot?

**Answer format:** Integer.

### Q41. [2 Marks] [MCQ]

What pair of values is printed? Assume C integer arithmetic is exact for the values used.

```c
#include <stdio.h>
int main(void) {
    int a[] = {2,4,6,8};
    int *p = a + 1;
    int **q = &p;
    (*q)++;
    **q += *(p-1);
    printf("%d %d", a[2], (int)(p-a));
}
```

A. 6 1
B. 10 1
C. 10 2
D. 12 2

### Q42. [2 Marks] [NAT]

In a tabular minimization procedure, the remaining cover-selection problem is the chart below. The column labels are abstract requirements, not binary minterm indices. Every column must be covered. Candidate rows have the stated costs; no other rows are available.

| Implicant | Covered columns | Literal cost |
|---|---|---:|
| P | 1,2 | 2 |
| Q | 2,3 | 2 |
| R | 3,4 | 2 |
| S | 1,4 | 3 |
| T | 1,2,3 | 4 |

Among covers using the minimum possible number of rows, what is the minimum total cost?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A function F(n), for nonnegative integer n, returns immediately for n≤1. Otherwise it calls F(floor(n/2)) and F(ceil(n/2)), then returns. Count every invocation, including base cases. How many invocations are eliminated when computing F(10) if memoization causes each distinct argument to be evaluated only once? A memo-table hit is not counted as an evaluated invocation in the memoized version.

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

An initially empty sparse file has an inode with four direct block pointers and one single-indirect pointer. Blocks are1024 bytes and pointers are4 bytes. A write of one byte at file offset6144 allocates only the necessary data block and any necessary indirect block. Unwritten holes need no data blocks. Exclude the already existing inode. How many bytes of newly allocated blocks are needed?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A ternary relationship R(A,B,C) contains exactly (a1,b1,c1), (a1,b2,c2), (a2,b1,c2). It is replaced by its three binary projections on AB, AC and BC, then reconstructed by their natural join. How many tuples appear in the reconstructed relation but not in R?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

An n-bit ripple-carry adder adds unsigned A and B with carry-in0. Its most significant sum bit is s, carry into that bit is c and carry out is d. The input sign bits, when interpreted as two's complement, are a and b. Which expressions detect signed overflow for every input?

A. c XOR d.
B. d alone.
C. ((NOT a) AND (NOT b) AND s) OR (a AND b AND (NOT s)).
D. a XOR b.

### Q47. [2 Marks] [MSQ]

A proposed proof claims that the regular language a*b* is not regular: “For pumping length p choose a^p b^p. Select a decomposition whose pumped part contains both a and b. Pumping twice destroys the required order.” Which objections correctly identify flaws?

A. A nonregularity proof must defeat every legal decomposition, not just one selected decomposition.
B. Any legal decomposition with prefix-plus-pumped-part length at most p has its pumped part entirely among the a's.
C. The pumping lemma permits an empty pumped part, so the proof must use one.
D. Choosing a string of length2p is forbidden by the pumping lemma.

### Q48. [2 Marks] [MCQ]

For n a positive integer, what is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = i
    while j <= n:
        work()
        j = j + i
```

A. Θ(n)
B. Θ(n log n)
C. Θ(n sqrt(n))
D. Θ(n²)

### Q49. [2 Marks] [NAT]

How many truth assignments to propositions p,q,r,s satisfy all three conditions: p implies q, r implies q, and s is true exactly when p and r have different truth values?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

A process opens a file, obtaining descriptor3 with file offset0, and then duplicates descriptor3 to descriptor4 using dup. It reads6 bytes through descriptor3, seeks through descriptor4 to absolute offset2, and reads3 bytes through descriptor3. All operations succeed fully. What file offset is then observed through descriptor4?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

A syntax-directed translation uses the grammar E→E−T | T and T→digit. The semantic rules are E→E1−T: E.val=E1.val−T.val; E→T: E.val=T.val; T→digit: T.val=the digit's value. For the input9−4−2, a second implementation incorrectly rewrites the grammar to right recursion E→T−E | T and uses ordinary subtraction of the child values. What is the correct implementation's value minus the second implementation's value?

**Answer format:** Integer, possibly negative.

### Q52. [2 Marks] [NAT]

For what real value of k does the following system have infinitely many solutions?

```text
x + y + z = 2
2x + 3y + 4z = 5
3x + 4y + 5z = k
```

**Answer format:** Exact number.

### Q53. [2 Marks] [NAT]

An HTTP client has no DNS cache and needs one DNS lookup taking20 ms. Establishing a TCP connection takes one RTT of40 ms. A base HTML request and response take one additional RTT; transmission times are negligible. The HTML references three small objects on the same server, discovered only after the HTML arrives. A single persistent connection fetches these objects sequentially with one RTT per object, without pipelining. How many milliseconds are saved by pipelining all three object requests together after receiving the HTML? DNS, connection establishment and base retrieval are unchanged.

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

Let f(0)=0 and f(x)=x² sin(1/x) for x≠0. Which statements are correct?

A. f is continuous at0.
B. f is differentiable at0 with derivative0.
C. f' is continuous at0.
D. The limit of f(x)/x as x approaches0 is0.

### Q55. [2 Marks] [MSQ]

Let S be the set of encodings of Turing machines whose recognized language contains the string00. Which statements are correct?

A. S is recognizable by simulating the encoded machine on00.
B. S is decidable because the input string00 has fixed finite length.
C. S is a nontrivial semantic property of recognized languages.
D. Both S and its complement are recognizable.

### Q56. [2 Marks] [NAT]

Independent fair-coin tosses continue until the first head. Let N be the number of tosses, including the head. Given that N is odd, what is E[N]? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q57. [2 Marks] [NAT]

A tunnel adds an outer IPv4 header of20 bytes to each entire inner IPv4 packet. The path MTU for outer packets is1500 bytes. Outer fragmentation is prohibited. The inner packet has an IPv4 header of20 bytes and a TCP header of20 bytes, with no options. What is the largest TCP data payload, in bytes, that fits in one tunneled packet?

**Answer format:** Integer.

### Q58. [2 Marks] [MSQ]

A fully associative cache holds three blocks and starts empty. Compare FIFO replacement with LRU replacement for the block-reference sequence A,B,C,A,D,A. Every reference accesses one whole block, and every miss inserts it. Which statements are correct?

A. Both policies incur exactly four misses.
B. FIFO evicts A on the reference to D.
C. LRU evicts B on the reference to D.
D. The final reference to A misses under FIFO but hits under LRU.

### Q59. [2 Marks] [NAT]

Procedure P is lexically nested inside Main. Procedures Q and R are both lexically nested inside P. During execution, Main calls P, P calls Q, and Q calls R. Each activation has a static link to its immediate lexical parent's activation and a dynamic link to its caller. From R's activation, how many static links must be followed to access a local variable of Main?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A message of6000 data bytes crosses three equal-rate store-and-forward links in sequence. Each link sends1000 bytes per millisecond. There is no propagation or processing delay. Packets have an extra100-byte header and may be pipelined across links. Splitting the message into six equal data packets instead of three equal data packets changes the time until the entire message reaches the destination. How many milliseconds are saved?

**Answer format:** Exact number.

### Q61. [2 Marks] [NAT]

A CPU would execute1000 instructions at a CPI of2. A DMA controller transfers100 words, stealing one CPU cycle per word; each stolen cycle stalls the CPU by exactly one cycle, and there are no other effects. An alternative programmed-I/O method adds four CPU cycles per word and uses no DMA stalls. How many CPU clock cycles does DMA save over programmed I/O for the same computation and transfer?

**Answer format:** Integer.

### Q62. [2 Marks] [MSQ]

Relations Candidate(x)={a,b}, Required(y)=empty, and Completed(x,y)=empty use set semantics. The desired query returns candidates who have completed every required item. Which statements are correct?

A. The result is empty because Completed is empty.
B. The result is {a,b} by vacuous truth.
C. For each candidate, testing that no required item lacks a matching Completed tuple implements the desired condition.
D. Replacing the outer Candidate relation by the x-projection of Completed preserves the result for this instance.

### Q63. [2 Marks] [NAT]

Over alphabet {a,b}, consider the language of strings with an even number of a's whose last symbol is b. The empty string is not in the language. What is the minimum number of states in a complete DFA recognizing it?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

A parent creates a pipe and then forks. Both processes initially inherit both pipe ends. The parent closes its own write end and reads until EOF. The child writes some data and then becomes idle without exiting or closing either descriptor. Assume all data already written have been read. Which statements are correct?

A. The parent's next blocking read must return EOF immediately.
B. The child's still-open write descriptor prevents EOF at the parent.
C. Closing the child's read descriptor alone is sufficient to cause EOF at the parent.
D. If the child closes its write descriptor and no other write descriptors exist, the parent can observe EOF.

### Q65. [2 Marks] [NAT]

An array of length18 is rotated left by8 positions using an in-place cycle algorithm. A move maps each original index i to (i−8) modulo18. The algorithm saves one value in a temporary variable at the start of each disjoint index cycle and then completes that cycle before beginning another. How many times does it need to start a new cycle?

**Answer format:** Integer.


---

## ANSWER KEY — MOCK TEST 020

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 27 |
| 2 | MCQ | 1 | B |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 24 |
| 5 | MSQ | 1 | A, B, D |
| 6 | MCQ | 2 | B |
| 7 | MCQ | 2 | D |
| 8 | MSQ | 2 | A, D |
| 9 | NAT | 2 | 25 |
| 10 | MCQ | 2 | A |
| 11 | MSQ | 1 | A, C |
| 12 | NAT | 1 | 2 |
| 13 | MCQ | 1 | B |
| 14 | NAT | 1 | 5 |
| 15 | NAT | 1 | 256 |
| 16 | MSQ | 1 | B, C |
| 17 | NAT | 1 | 500 |
| 18 | NAT | 1 | 3 |
| 19 | MSQ | 1 | A, C, D |
| 20 | MCQ | 1 | C |
| 21 | MSQ | 1 | A, C |
| 22 | NAT | 1 | 2 |
| 23 | NAT | 1 | 13 |
| 24 | MCQ | 1 | B |
| 25 | MSQ | 1 | B, C |
| 26 | NAT | 1 | 1024 |
| 27 | MSQ | 1 | B, C |
| 28 | NAT | 1 | 6 |
| 29 | MCQ | 1 | A |
| 30 | NAT | 1 | 4 |
| 31 | MSQ | 1 | B, C |
| 32 | MCQ | 1 | C |
| 33 | NAT | 1 | 1 |
| 34 | NAT | 1 | 1 |
| 35 | NAT | 1 | 11 |
| 36 | MSQ | 2 | A, C |
| 37 | NAT | 2 | 2.8 |
| 38 | NAT | 2 | 4 |
| 39 | MSQ | 2 | B, D |
| 40 | NAT | 2 | 2 |
| 41 | MCQ | 2 | C |
| 42 | NAT | 2 | 4 |
| 43 | NAT | 2 | 14 |
| 44 | NAT | 2 | 2048 |
| 45 | NAT | 2 | 1 |
| 46 | MSQ | 2 | A, C |
| 47 | MSQ | 2 | A, B |
| 48 | MCQ | 2 | B |
| 49 | NAT | 2 | 5 |
| 50 | NAT | 2 | 5 |
| 51 | NAT | 2 | -4 |
| 52 | NAT | 2 | 7 |
| 53 | NAT | 2 | 80 |
| 54 | MSQ | 2 | A, B, D |
| 55 | MSQ | 2 | A, C |
| 56 | NAT | 2 | 1.6667 (accepted range 1.66665–1.66675) |
| 57 | NAT | 2 | 1440 |
| 58 | MSQ | 2 | B, C, D |
| 59 | NAT | 2 | 2 |
| 60 | NAT | 2 | 1.7 |
| 61 | NAT | 2 | 300 |
| 62 | MSQ | 2 | B, C |
| 63 | NAT | 2 | 3 |
| 64 | MSQ | 2 | B, D |
| 65 | NAT | 2 | 2 |

