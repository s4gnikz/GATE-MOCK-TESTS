# GATE CS 2027 — Full-Length Mock Test 018

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all remaining questions carry two. MCQs have one correct option and a penalty of one-third of their marks for an incorrect answer. MSQs require all correct options, without partial credit or negative marking. NATs have no negative marking. Unattempted questions score zero. General Aptitude contributes 15 marks, mathematics 13 and core CS 72. Numerical answers are exact unless a rounding format is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“The panel vacillated between the two proposals, repeatedly reversing its tentative preference.” Which word best replaces vacillated without changing the meaning?

A. Wavered
B. Collaborated
C. Converged
D. Disappeared

### Q2. [1 Mark] [NAT]

What is the largest nonnegative integer n such that 2ⁿ divides 12! exactly?

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

A compiler produced correct output on every program in a finite test suite. No proof of correctness is available. Which inference is justified solely by this observation?

A. It is correct on every possible program.
B. No incorrect output was observed on the tested programs.
C. Every untested program must fail.
D. A larger test suite cannot reveal a fault.

### Q4. [1 Mark] [NAT]

A 2×5 rectangular board is tiled completely with identical 1×2 dominoes, with no overlaps. Exactly three dominoes are vertical, each covering an entire height-two column. How many distinct tilings satisfy this condition? Board positions are fixed; mirror images count separately when different.

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A sequence has a1=2, a2=6 and a(n+2)=2a(n+1)−a(n)+2 for n≥1. Find a6.

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

An open rectangular box is made by cutting equal squares of integer side x from the four corners of a 20 cm by 12 cm sheet and folding the remaining flaps. Here x is a positive integer and the box must have positive dimensions. What is the largest possible volume in cubic centimetres?

**Answer format:** Integer.

### Q7. [2 Marks] [MSQ]

A notice states: “Only applicants who submitted both forms were interviewed. Every interviewed applicant received a decision.” Assume both statements are true. Which conclusions necessarily follow?

A. No applicant who failed to submit both forms was interviewed.
B. An applicant who received no decision was not interviewed.
C. Every applicant who submitted both forms was interviewed.
D. Every applicant who received a decision was interviewed.

### Q8. [2 Marks] [NAT]

A shop expects unit sales to fall by 20% from last month. This month every item will also be sold at a 10% discount on its new sticker price; last month all items sold at their old sticker price. All items have the same price within each month. What percentage increase in sticker price is required to keep sales revenue unchanged? Round to two decimal places.

**Answer format:** Number to 2 decimal places, without the percent sign.

### Q9. [2 Marks] [MSQ]

Exactly two of boxes A,B,C,D contain prizes. Four labels state: A, “Exactly one of A and B contains a prize”; B, “C contains a prize”; C, “D contains no prize”; D, “A contains a prize.” Exactly two labels are true. Which conclusions necessarily follow?

A. A contains a prize.
B. B contains a prize.
C. C contains no prize.
D. D contains no prize.

### Q10. [2 Marks] [MCQ]

A plane transformation T maps (x,y) to (1−y,x). Starting at (1,0), apply T exactly 2027 times. What is the final point?

A. (1,1)
B. (0,1)
C. (0,0)
D. (1,0)

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

An unknown Boolean condition selects one of two branches. The first assigns x=2 and y=x; the second assigns x=3 and y=x. Immediately after the branches join, z=x−y is evaluated with exact arithmetic. What value is guaranteed for z even though neither x nor y individually has a unique constant value at the join?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

For powers of two n, a recursive algorithm has three recursive calls on size n/2, nonrecursive work Θ(n²), and constant work at n=1. Which statements are true?

A. Its total work is Θ(n²).
B. Its total work is Θ(n² log n).
C. Its recursion tree has n^(log₂3) leaves.
D. Its recursion tree has n internal levels before reaching size one.

### Q13. [1 Mark] [MSQ]

Which register dependences can register renaming eliminate by assigning distinct physical destinations, without changing the required flow of produced values to their consumers?

A. A true read-after-write dependence between a producer and its consumer.
B. A write-after-read name dependence.
C. The control dependence on an unresolved branch.
D. A write-after-write name dependence.

### Q14. [1 Mark] [MCQ]

Which sequence can be the preorder traversal of a BST with distinct keys and the ordinary strict ordering property?

A. 40,20,10,30,60,50,70
B. 40,20,50,10,60,30,70
C. 40,60,50,20,10,30,70
D. 40,20,30,10,60,50,70

### Q15. [1 Mark] [NAT]

A word-addressed machine executes an indirect indexed load defined as R2←M[M[R1+8]]. Initially R1=100, M[108]=200 and M[200]=17. What value is loaded into R2?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A three-input majority gate outputs one exactly when at least two inputs are one. Its input is currently 011. Among the three possible single-input-bit flips, how many change the gate's output?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A has rows (2,1),(6,5). In its factorization A=LU without row swaps, L is lower triangular with unit diagonal and U is upper triangular. Find L21+U22.

**Answer format:** Integer.

### Q18. [1 Mark] [MCQ]

T1 writes X; T2 then reads that uncommitted value and commits; T1 subsequently aborts. Which statement is correct?

A. The schedule is recoverable because T2 committed first.
B. T2's read is guaranteed to be unaffected by T1's abort.
C. The schedule is not recoverable because T2 committed before the transaction whose value it read.
D. An abort cannot affect values read by another transaction.

### Q19. [1 Mark] [NAT]

An integrable real function on [0,1] satisfies f(x)+f(1−x)=x²+(1−x)² for every x in that interval. Evaluate ∫₀¹ f(x) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q20. [1 Mark] [NAT]

Seven distinct keys are assigned to array indices 1–7 of a binary max-heap, with children 2i and 2i+1 where present. How many distinct valid key assignments are possible? The seven key values are fixed, and left/right positions are distinguished.

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

For the following straight-line code, which variables are live immediately after the second statement? Use ordinary syntactic liveness on this code as written, before dead-code elimination; there are no implicit uses at return.

```text
x = a+b
y = x*c
x = d
return y
```

A. x
B. d
C. c
D. y

### Q22. [1 Mark] [NAT]

A directed graph has adjacency lists s:[a,b], a:[c,d], b:[d], c:[], d:[e], e:[]. BFS starts at s, scans each list in the displayed order and marks a vertex when enqueuing it. At the instant d is first enqueued, how many vertices are already in the queue immediately before that enqueue?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A random variable X has mean 10 and variance 4. For Z=3X−2, find E[Z²].

**Answer format:** Integer.

### Q24. [1 Mark] [MSQ]

Which statements about socket receive results are correct? Calls request a positive number of bytes and encounter no errors unless explicitly stated.

A. On a connected TCP stream, returning zero after buffered input is exhausted indicates an orderly end of incoming data.
B. Each successful TCP receive must return exactly one complete application message.
C. Receiving a zero-length UDP datagram can return zero without implying that the sender has closed a connection.
D. TCP preserves the sender's write-call boundaries as receive-call boundaries.

### Q25. [1 Mark] [MCQ]

Two transactions execute r1(X),w1(X),r2(X),w2(Y),r1(Y), then both commit, with operations listed in execution order. Which statement about conflict serializability is correct?

A. Equivalent to T1 followed by T2 because T1 first accesses X.
B. Equivalent to T2 followed by T1 because T2 writes Y.
C. Serializable because reads never participate in conflicts.
D. Not conflict-serializable because the precedence graph contains both T1→T2 and T2→T1.

### Q26. [1 Mark] [NAT]

Under multiplication modulo 12, the units form a group {1,5,7,11}. How many elements generate this entire group by repeated multiplication?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A buddy allocator starts with one free 64 KiB block and rounds each request up to a power-of-two block size. It successfully allocates requests of 9 KiB, 17 KiB and 5 KiB, without metadata overhead. What is the total internal fragmentation in KiB inside these three allocated blocks?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

A resolver caches an authoritative negative DNS response for a name with an unexpired negative-cache TTL. The name is then created at the authoritative server. Assuming no forced refresh or invalidation, why may the resolver temporarily continue reporting that the name does not exist?

A. DNS names can never be created after the first query.
B. TCP forbids any change to DNS records.
C. The cached negative result may be reused until its TTL expires.
D. Every negative DNS response has an infinite lifetime.

### Q29. [1 Mark] [NAT]

Delete a perfect matching from the complete bipartite graph K3,3. What is the size of a minimum vertex cover of the remaining graph?

**Answer format:** Integer.

### Q30. [1 Mark] [MSQ]

Let L1={aⁿbⁿ:n≥0} and L2={aⁿb^(2n):n≥0}. Which statements are true?

A. L1∪L2 is context-free.
B. L1∩L2={ε}.
C. Every intersection of two context-free languages is context-free.
D. L1L2 is context-free.

### Q31. [1 Mark] [NAT]

One application message of 1000 bytes is carried in one TCP segment with a 20-byte TCP header, one IPv4 packet with a 20-byte IP header, and one Ethernet frame with a 14-byte header and four-byte FCS. There are no other headers, padding or fragmentation. Excluding preamble and inter-frame gap, how many bytes are transmitted in the frame?

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

For connected undirected weighted graphs, which statements are correct?

A. Repeated edge weights make a unique MST impossible.
B. Pairwise distinct edge weights guarantee a unique MST.
C. If the graph itself is a tree, it has a unique spanning tree regardless of repeated weights.
D. A globally heaviest edge can never belong to an MST, even if it is a bridge.

### Q33. [1 Mark] [MCQ]

Two processes use the same virtual page number but map it to different physical frames. A processor's TLB has no address-space tags. Which action can prevent stale translations from the first process being used by the second on a context switch?

A. Retain all translations merely because the virtual page numbers match.
B. Flush the relevant TLB translations when changing address spaces.
C. Change every physical memory byte to zero.
D. Assume every TLB hit automatically consults the new page table again.

### Q34. [1 Mark] [NAT]

A synchronous two-bit machine updates Q0′=NOT Q0 and Q1′=Q1 XOR Q0, using the old state for both expressions. Starting at Q1Q0=10, what unsigned integer does its state represent after five clock edges?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

Consider L={aⁿbᵐ:n,m≥0 and n≠m}. For an arbitrary positive proposed regular pumping length p, choose w=aᵖb^(p+p!). Every valid split w=xyz with |xy|≤p and |y|>0 has y=aᵏ for some 1≤k≤p. Which pumping exponent i makes xy^i z have equal a and b counts and therefore leave L?

A. i=p!
B. i=1+p!/k
C. i=1−p!/k
D. i=k+1

### Q36. [2 Marks] [MSQ]

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

### Q37. [2 Marks] [NAT]

A lexer recognizes identifiers `[a-z]+`, integers `[0-9]+`, the keyword `if`, and the single-character token `+`. It uses longest match; an exact tie between an identifier and the keyword is resolved in favour of the keyword. There is no rule requiring whitespace between tokens. How many tokens does it produce for `ifx12if+007`?

**Answer format:** Integer.

### Q38. [2 Marks] [MCQ]

An eight-bit ALU compares signed two's-complement operands A=0x80 and B=0x01 by computing A−B modulo 256. Let N be the result's sign bit, V the signed subtraction-overflow flag, and L the correct signed-less-than result. Which triple (N,V,L) is correct?

A. (1,0,1)
B. (0,0,0)
C. (1,1,0)
D. (0,1,1)

### Q39. [2 Marks] [MSQ]

For a Turing machine started on a blank tape, consider the property that it eventually enters a designated state PRINT. Which statements are true for arbitrary encoded machines?

A. The set of machines having the property is recognizable.
B. Simulating a machine for a sufficiently large fixed number of steps decides the property for every machine.
C. The property is undecidable, since a machine can simulate an arbitrary machine/input pair and enter PRINT exactly when that simulation halts.
D. The complement is also recognizable.

### Q40. [2 Marks] [NAT]

Binary words of length six containing exactly three ones are considered equivalent when one is a cyclic rotation of the other. Reflections are not identified. Count the equivalence classes whose words have least rotational period exactly six; words invariant under a smaller positive rotation are excluded.

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A microinstruction independently selects one of nine source choices, one of five ALU choices, and any subset of eight destination registers, including the empty subset. A format with separate fixed-width binary source and ALU fields plus an eight-bit destination mask is compared with an unrestricted single binary field encoding all legal combinations. How many bits does the separate-field format require in excess of the minimum single-field width?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

Over alphabet {0,1}, accept a word exactly when it contains exactly one position at which two adjacent symbols are equal. Overlapping adjacent pairs count separately: 000 has two such positions. What is the number of states in the minimal complete DFA, including a rejecting sink?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A sparse file uses 4096-byte blocks and four-byte pointers. Its inode has eight direct pointers, one single-indirect pointer and one double-indirect pointer. Logical block numbers start at zero. Starting with no allocated data or indirect blocks, one byte is written in logical block 1032, then one byte in logical block 2061. Only necessary data and pointer blocks are allocated; holes consume no blocks, and the existing inode is not counted. How many blocks have been allocated after both writes?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A slotted switch has two inputs and two outputs O1,O2. Initially input I1 holds packets [A destined for O1, B destined for O2] in that order, and I2 holds [C destined for O1]. No packets arrive later. A packet occupies one whole slot; each input and each output serves at most one packet per slot. O1 is unavailable in slots 1 and 2 and available thereafter; O2 is always available. Ties for O1 favour I1. Compare strict FIFO input queues (only a head packet is eligible) with separate queues per output at each input (B can bypass A). By how many slots does FIFO delay B's departure relative to the separate-queue design?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

Grammar E→E+E | E*E | n allows all binary parenthesizations and specifies no precedence. Each n is a numeric literal with its usual value; + and * have ordinary integer meanings. How many distinct numerical values arise from parse trees for `1+2*3+4`?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

A byte-addressed 16-bit address space contains a 16 KiB chip at 0x0000–0x3FFF and an 8 KiB chip at 0x4000–0x5FFF. Both chips use active-high enables and are fully decoded, with A15 the most significant address bit. Which statements are correct?

A. The 16 KiB chip's enable can be NOT A15 AND NOT A14.
B. The 8 KiB chip's enable can be NOT A15 AND A14, without considering A13.
C. Exactly 32 KiB of the address space is unmapped by these chips.
D. The 8 KiB chip's enable can be NOT A15 AND A14 AND NOT A13.

### Q47. [2 Marks] [MSQ]

For grammar S→AB, A→aA | ε, B→bBc | ε, with start symbol S and end marker $, which statements are correct?

A. The grammar is LL(1).
B. c belongs to FOLLOW(A).
C. FOLLOW(B)={c,$}.
D. The production A→ε must be selected on lookahead a in an LL(1) table.

### Q48. [2 Marks] [NAT]

A CRC uses generator G(x)=x³+x+1 over GF(2). In a fixed 15-bit transmitted word, exactly two distinct bit positions are inverted. How many unordered pairs of error positions produce an error polynomial divisible by G(x), and thus go undetected? Positions are numbered 0 through 14 by powers of x.

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

How many ordered compositions of 8 use only parts 1 and 2 and never place two parts of size 2 consecutively? For example, 2,1,2 is allowed for total 5, while 1,2,2 is not.

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

How many truth assignments to p,q,r,s,t satisfy all five clauses `(p OR q)`, `(NOT p OR r)`, `(NOT q OR r)`, `(NOT r OR s)` and `(NOT s OR t)`?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

An ER relationship assigns each of five distinct employees to exactly one of four distinct departments. Every department must have at least one employee. How many different relationship instances satisfy these participation and cardinality constraints?

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

A directed graph has edges s→a of weight 2, s→b of weight 5, b→a of weight −4, a→t of weight 3 and b→t of weight 1. A standard Dijkstra implementation finalizes vertices in increasing tentative-distance order, breaks the a/b/t ties by choosing t before b, never reopens a finalized vertex, and stops when t is finalized. Which statements are true?

A. The true shortest s-to-t distance is 5.
B. The true shortest s-to-t distance is 4.
C. This graph contains a negative directed cycle.
D. The specified implementation returns 5.

### Q53. [2 Marks] [NAT]

A directed multigraph has adjacency-count matrix with rows (1,2,0), (0,0,3), (1,0,0). Entries count distinct parallel edges, and walks distinguish different edge choices. How many length-three walks start and end at vertex 1?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

What integer is printed? All pointed-to objects remain alive.

```c
void change(int **p, int *q) {
    **p += 2;
    *p = q;
    **p += 3;
}
/* Inside main: */
int x=4, y=7;
int *p=&x;
change(&p, &y);
printf("%d", x+y+*p);
```

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A four-bit signed fixed-point format has no fractional bits and uses saturating addition: results above 7 become 7, and results below −8 become −8. Let ⊕ denote this addition. For a=6,b=5,c=−4, what is `a⊕(b⊕c) − ((a⊕b)⊕c)`, with the final subtraction performed as an exact ordinary integer subtraction?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

A hypothetical CSMA/CD link transmits at 100 million bits per second with a minimum frame of 512 bits. Signal propagation speed in the cable is 200 million metres per second. In addition to cable propagation, devices introduce 0.4 microseconds of delay in each direction. Requiring the minimum-frame transmission time to be at least the worst-case round-trip delay, what is the maximum cable length in metres?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

Under set semantics let R(A,B)={(1,x),(2,y)}, S(B) be empty, and U(A)={1,2,3}. Standard relational division R÷S uses candidate A values from π_A(R). Separately, a query selects each A in U for which no B in S lacks a matching tuple in R. Which statements are true?

A. R÷S returns {1,2}.
B. R÷S returns {1,2,3}.
C. The separately described query returns {1,2,3}.
D. Both results must be empty because S is empty.

### Q58. [2 Marks] [MSQ]

Two ascending lists each contain three distinct keys, and all six keys are distinct. Only pairwise comparisons between keys are permitted to determine their merged order. Which statements are true?

A. There are 6! possible merged orders consistent with the internal list orders.
B. There are 20 possible interleavings consistent with the internal list orders.
C. Four binary-outcome comparisons suffice in the worst case for every input.
D. Ordinary two-list merging achieves the optimal worst-case count of five comparisons.

### Q59. [2 Marks] [NAT]

A global integer x initially equals zero. Run visit(3) below, with exact arithmetic. What is the sum of all printed integers?

```text
visit(n):
    if n == 0:
        print(x)
        return
    x = x+1
    visit(n-1)
    x = x-1
    visit(n-1)
```

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

Let A(a) have rows (1,a,0), (0,1,a), (a,0,1), where a is real. Consider A(a)x=(1,1,1)ᵀ. Which statements are true?

A. A(a) is singular for every real a.
B. det(A(a))=1+a³.
C. At a=−1, the displayed system has infinitely many solutions.
D. At a=−1, A(a) has rank two.

### Q61. [2 Marks] [MSQ]

Choose a,b independently and uniformly from {0,1,2,3,4}, and define h(x)=(ax+b) mod 5 on the same domain. For two distinct fixed keys x,y, which statements are true?

A. For each ordered pair (r,s) of output values, exactly one pair (a,b) gives h(x)=r,h(y)=s.
B. Every function in this family is a permutation of the domain.
C. The probability h(x)=h(y) is 1/5.
D. After conditioning on a≠0, h(x) and h(y) remain independent uniform variables.

### Q62. [2 Marks] [NAT]

A binary floating-point format has three significant bits including the leading one, minimum normal exponent −2, gradual underflow and round-to-nearest ties-to-even. Compute 0.25×0.25, round to the format, then multiply that stored result by 0.5 and round again. What is the absolute relative error of the final stored result compared with the exact real product 0.25×0.25×0.5?

**Answer format:** Exact finite decimal.

### Q63. [2 Marks] [MCQ]

A regular file contains bytes ABCDE. Descriptor p opens it at offset zero; q=dup(p); descriptor r comes from a separate open of the same file, also at zero. With no intervening operations, execute read(p,2), read(q,1), seek(r,1 from start), read(r,2), read(p,1). All reads succeed fully. What are the byte strings from the four reads in order?

A. AB; A; BC; A
B. AB; C; BC; E
C. AB; C; DE; D
D. AB; C; BC; D

### Q64. [2 Marks] [NAT]

A process has ordinary private integer x=2 and an integer y=3 in an explicitly shared memory mapping. It forks. The child sets x=10 and y=20, then exits. After waiting for that child, the parent starts one thread that executes x=x+y and then joins it. No other changes occur. What is the parent's final x?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

For a Boolean function F(x,y,z), define its Boolean difference with respect to a variable as the XOR of its restrictions when that variable is zero and one. How many functions satisfy all of the following: the difference with respect to x equals y for every y,z; the difference with respect to z equals one for every x,y; and F(0,0,0)=0?

**Answer format:** Integer.

## ANSWER KEY — MOCK TEST 018

NAT answers are exact except for the stated rounded ranges.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 10 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 4 |
| 5 | NAT | 1 | 42 |
| 6 | NAT | 2 | 256 |
| 7 | MSQ | 2 | A, B |
| 8 | NAT | 2 | 38.89 (range 38.885–38.895) |
| 9 | MSQ | 2 | A, C |
| 10 | MCQ | 2 | C |
| 11 | NAT | 1 | 0 |
| 12 | MSQ | 1 | A, C |
| 13 | MSQ | 1 | B, D |
| 14 | MCQ | 1 | A |
| 15 | NAT | 1 | 17 |
| 16 | NAT | 1 | 2 |
| 17 | NAT | 1 | 5 |
| 18 | MCQ | 1 | C |
| 19 | NAT | 1 | 0.3333 (range 0.33325–0.33335) |
| 20 | NAT | 1 | 80 |
| 21 | MSQ | 1 | B, D |
| 22 | NAT | 1 | 2 |
| 23 | NAT | 1 | 820 |
| 24 | MSQ | 1 | A, C |
| 25 | MCQ | 1 | D |
| 26 | NAT | 1 | 0 |
| 27 | NAT | 1 | 25 |
| 28 | MCQ | 1 | C |
| 29 | NAT | 1 | 3 |
| 30 | MSQ | 1 | A, B, D |
| 31 | NAT | 1 | 1058 |
| 32 | MSQ | 1 | B, C |
| 33 | MCQ | 1 | B |
| 34 | NAT | 1 | 3 |
| 35 | MCQ | 1 | B |
| 36 | MSQ | 2 | B, C |
| 37 | NAT | 2 | 5 |
| 38 | MCQ | 2 | D |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 3 |
| 41 | NAT | 2 | 1 |
| 42 | NAT | 2 | 6 |
| 43 | NAT | 2 | 5 |
| 44 | NAT | 2 | 3 |
| 45 | NAT | 2 | 4 |
| 46 | MSQ | 2 | A, D |
| 47 | MSQ | 2 | A, C |
| 48 | NAT | 2 | 9 |
| 49 | NAT | 2 | 19 |
| 50 | NAT | 2 | 3 |
| 51 | NAT | 2 | 240 |
| 52 | MSQ | 2 | B, D |
| 53 | NAT | 2 | 7 |
| 54 | NAT | 2 | 26 |
| 55 | NAT | 2 | 4 |
| 56 | NAT | 2 | 432 |
| 57 | MSQ | 2 | A, C |
| 58 | MSQ | 2 | B, D |
| 59 | NAT | 2 | 12 |
| 60 | MSQ | 2 | B, D |
| 61 | MSQ | 2 | A, C |
| 62 | NAT | 2 | 1 |
| 63 | MCQ | 2 | D |
| 64 | NAT | 2 | 22 |
| 65 | NAT | 2 | 2 |

