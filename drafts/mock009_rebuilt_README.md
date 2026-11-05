# GATE CS 2027 — Full-Length Mock Test 009

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the remaining questions carry two marks each. Each MCQ has exactly one correct answer. Each MSQ has multiple correct answers; select all and only those answers, with no partial credit. An incorrect MCQ loses one-third of the question's marks. Incorrect MSQs, NATs, and unattempted questions receive zero. NAT precision is stated in each question. GA contributes 15 marks, Engineering Mathematics 13, and core CS 72. Arithmetic is exact unless explicitly specified otherwise.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“Not every submitted report contains a diagram.” Which statement is logically equivalent?

A. No submitted report contains a diagram.
B. At least one submitted report contains no diagram.
C. Every submitted report contains no diagram.
D. At least one report containing a diagram was not submitted.

### Q2. [1 Mark] [NAT]

Six equally efficient workers can complete a job in eight days. They work for two days, after which two workers leave. How many additional days do the remaining workers need? Work is divisible and each worker's daily rate is constant.

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

A rule says, “A consignment will be released only if it is inspected, unless it is exempt.” Which situation necessarily violates the rule?

A. An exempt consignment is released without inspection.
B. A nonexempt consignment is inspected but not released.
C. A nonexempt consignment is released without inspection.
D. An exempt consignment is inspected before release.

### Q4. [1 Mark] [NAT]

Every point of a planar figure is first rotated by 180 degrees about (0,0), then by 180 degrees about (2,1). By what distance is each point displaced from its original location? Round to three decimal places.

**Answer format:** Number to 3 decimal places.

### Q5. [1 Mark] [NAT]

How many distinct arrangements of the letters of BALLOON have all three vowels together? Repeated copies of the same letter are indistinguishable.

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

A workshop must produce exactly 20 items using two methods. Method A takes two hours and costs 3 units per item; method B takes one hour and costs 5 units per item. The total processing-time budget is 28 hours, with no overlap of work. What is the minimum total cost?

**Answer format:** Integer cost units.

### Q7. [2 Marks] [NAT]

Of 100 students, 80 study subject A, 75 study B, and 70 study C. What is the smallest possible number who study all three subjects?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

Two fair six-sided dice are rolled. Given that their sum is prime, what is the probability that their product is divisible by 3? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q9. [2 Marks] [NAT]

A tariff charges 4 units for each of the first ten units consumed and 6 units for each additional unit. Consumption is an integer. A bill also includes a fixed charge of 15. What is the largest consumption whose total bill does not exceed 100?

**Answer format:** Integer units consumed.

### Q10. [2 Marks] [MCQ]

A school introduced optional tutoring. Participants subsequently scored higher than nonparticipants. The report concludes that tutoring caused the entire observed score difference. Which additional finding most directly weakens this conclusion?

A. Participants already had higher scores before tutoring began.
B. The tutoring sessions occurred in classrooms.
C. Both groups took the same final examination.
D. The report stated each group's size.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Let A={1,2} and B={1,2,3,4,5}. Consider the set of all X satisfying A⊆X⊆B, ordered by inclusion. How many ordered pairs (X,Y) satisfy X∩Y=A and X∪Y=B?

**Answer format:** Integer.

### Q12. [1 Mark] [MCQ]

A synchronous three-bit binary counter has next-state equations q0′=NOT q0, q1′=q1 XOR q0, q2′=q2 XOR (q1 AND q0). Starting in 011, what is its state after five clock edges?

A. 111
B. 000
C. 001
D. 101

### Q13. [1 Mark] [NAT]

P is the 4×4 permutation matrix that cyclically shifts coordinates: P(x1,x2,x3,x4)ᵀ=(x4,x1,x2,x3)ᵀ. Find det(I+P).

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A fixed 32-bit instruction contains three register fields, each able to name any of 32 registers, an eight-bit immediate field, and an opcode occupying all remaining bits. What is the maximum number of distinct opcode patterns?

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

In C, `char s[]="a\0bc";` is declared. What are sizeof(s) and strlen(s), respectively? The proper standard header is included.

A. (4,4)
B. (5,1)
C. (5,4)
D. (4,1)

### Q16. [1 Mark] [NAT]

Starting with [1,2,3,4,5,6], perform a stable partition that puts all even values before all odd values while preserving order within each group. Only swaps of adjacent elements are permitted. What is the minimum number of swaps?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

Which words belong to the language denoted by a*b | ab*?

A. aab
B. abb
C. ab
D. ba

### Q18. [1 Mark] [NAT]

A compiler lays out local objects in declaration order at increasing offsets from zero: char c, int i, double d, char e. Sizes and required alignments are respectively (1,1),(4,4),(8,8),(1,1) bytes. Each object's start is rounded up to its required alignment, and total local storage is rounded up to a multiple of eight. How many bytes are allocated?

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

A parent opens an ordinary file and then forks. Neither process closes or duplicates the inherited descriptor. Which property is shared through the inherited open file description?

A. The processes' program counters.
B. The file offset associated with those descriptors.
C. Every local variable in their stacks.
D. Their process identifiers.

### Q20. [1 Mark] [NAT]

X is the score on a fair six-sided die. Let Y be 1 when X is even and 0 otherwise. Find Cov(X,Y).

**Answer format:** Exact finite decimal.

### Q21. [1 Mark] [NAT]

Let f(x)=x³+x on the real line, and let g be its inverse. Find g′(2).

**Answer format:** Exact finite decimal.

### Q22. [1 Mark] [MCQ]

A B-tree has minimum degree t=2: every nonroot node has 1–3 keys, an internal node with k keys has k+1 children, and a nonleaf root has at least two children. Height is three edges from root to every leaf. Which pair gives the minimum and maximum possible total numbers of keys?

A. (7,63)
B. (15,255)
C. (8,64)
D. (15,85)

### Q23. [1 Mark] [MCQ]

An ordinary IPv4 subnet is 192.168.1.96/27, with its all-zero and all-one host fields reserved for network and broadcast addresses. Which is the highest assignable host address?

A. 192.168.1.127
B. 192.168.1.126
C. 192.168.1.128
D. 192.168.1.125

### Q24. [1 Mark] [NAT]

An eight-input priority encoder returns the index of the highest-numbered asserted input, with indices 0–7. Initially inputs 3 and 5 are asserted. The selected input is cleared, and the encoder is evaluated again. What is the second output index?

**Answer format:** Integer.

### Q25. [1 Mark] [MCQ]

An out-of-order processor retires instructions in program order. Stores may execute speculatively but do not modify architecturally visible memory until retirement. Why is this restriction useful for precise exceptions?

A. It ensures a younger store cannot become visible before an older faulting instruction is handled.
B. It makes every load take one cycle.
C. It eliminates all data dependencies.
D. It guarantees that speculative branches are always predicted correctly.

### Q26. [1 Mark] [NAT]

What integer is printed by this conforming C program?

```c
#include <stdio.h>
struct S { int a[2]; int *p; };
int main(void) {
    struct S s = {{1,2}, 0};
    s.p = s.a;
    struct S t = s;
    t.a[0] = 7;
    *t.p = 9;
    printf("%d\n", s.a[0] + t.a[0]);
    return 0;
}
```

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

For n a positive power of two, count executions of `work()`:

```text
i = 1
while i <= n:
    j = 0
    while j < n:
        work()
        j = j + i
    i = 2*i
```

What is the tight asymptotic count?

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(n²)

### Q28. [1 Mark] [MSQ]

A deterministic machine on each fixed input has only finitely many possible configurations, and its full transition relation can be simulated effectively. Which statements are correct?

A. Repeating an identical nonhalting configuration proves that the subsequent computation loops.
B. Simulating until it halts, without checking repeats, necessarily terminates.
C. Recording visited configurations permits deciding whether this computation eventually accepts.
D. Finiteness alone makes every computation halt.

### Q29. [1 Mark] [MCQ]

Which grammar is the direct left-factored equivalent of S→ab | ac | a, with ε denoting the empty string?

A. S→aX; X→b | c | ε
B. S→Xa; X→b | c | ε
C. S→aX; X→bX | cX | ε
D. S→a; X→b | c

### Q30. [1 Mark] [MCQ]

A process is blocked solely waiting for a disk read. The read completes successfully while another process runs on the CPU. What is the usual immediate process-state transition for the waiting process?

A. Blocked to ready.
B. Blocked to terminated.
C. Blocked directly to running in every case.
D. Ready to blocked.

### Q31. [1 Mark] [NAT]

An ER relationship assigns each of 17 employees to exactly one department, and each department must have at least three assigned employees. Departments with no assigned employees are forbidden. What is the largest possible number of departments?

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

Two established TCP connections terminate at the same server IPv4 address and local port. Which statements are correct?

A. They may be distinguished by different remote IPv4 addresses or remote ports.
B. The shared local port alone forces the two connections to be the same connection.
C. The connection-identifying four-tuple includes both endpoint addresses and both endpoint ports.
D. Every established server-side connection must use a different local port.

### Q33. [1 Mark] [NAT]

How many group homomorphisms exist from the additive group Z12 to the additive group Z18?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

The three-input majority function is F=xy+xz+yz. A two-to-one multiplexer selects D0 when x=0 and D1 when x=1. Which pair (D0,D1) realizes F?

A. (y OR z, y AND z)
B. (y AND z, y OR z)
C. (y XOR z, y AND z)
D. (NOT y, z)

### Q35. [1 Mark] [MCQ]

A five-stage pipeline uses one single-ported memory for both IF instruction fetch and MEM data access. A load instruction is in MEM while a younger instruction needs IF during the same cycle. Even with complete data forwarding, what remains?

A. A structural conflict for the memory port.
B. A mandatory arithmetic overflow.
C. A control hazard caused by every load.
D. No possible conflict because forwarding duplicates the memory port.

### Q36. [2 Marks] [NAT]

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

### Q37. [2 Marks] [MSQ]

An undirected weighted graph has a cycle whose edge weights are 1,2,2,5. Other edges may exist. Which statements necessarily hold?

A. The weight-5 edge on this cycle belongs to no minimum spanning tree of a connected graph containing it.
B. Every weight-2 edge on the cycle belongs to no minimum spanning tree.
C. Removing that weight-5 edge preserves connectivity of its original connected component.
D. The minimum spanning tree is necessarily unique.

### Q38. [2 Marks] [MCQ]

Let L consist of binary strings of length at least four whose fourth symbol from the right is 1. What is the number of states in a smallest complete DFA for L?

A. 5
B. 16
C. 17
D. 32

### Q39. [2 Marks] [NAT]

How many permutations of six labelled elements have only even-length cycles in their disjoint-cycle decomposition?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

Consider the following control-flow graph. Variables are ordinary scalars without aliases, both branches are feasible, and only the returned value is observable. A variable is live at a point if some path from that point reads its current value before redefining it.

```text
B1: x = a+b
    y = x*c
    if p goto B2 else B3
B2: z = y+1
    goto B4
B3: x = a-b
    z = x+c
    goto B4
B4: return z
```

At the point immediately after `y=x*c` and before the conditional, which statements are correct?

A. y is live.
B. c is dead.
C. x is dead.
D. a is live.

### Q41. [2 Marks] [NAT]

Processes P and Q arrive at time 0, with P initially ahead of Q. Round-robin scheduling uses a quantum of 2 time units and zero context-switch cost. P executes a CPU burst of 2, performs I/O for 3, then executes a CPU burst of 2 and terminates. Q has one CPU burst of 5. A process finishing I/O joins the tail of the ready queue without preempting the running process. A quantum-expired process also joins the tail. What is the sum of their waiting times in the ready queue? I/O time is not waiting time.

**Answer format:** Integer time units.

### Q42. [2 Marks] [MCQ]

Relations R(A,B) and S(B,C) each contain 100 tuples. B is a key of S, and every R.B value references an existing S.B value. No additional constraints are given. Under set semantics, how many tuples must R⋈S contain?

A. 0
B. 100
C. 10,000
D. It cannot be determined even under these constraints.

### Q43. [2 Marks] [NAT]

Packets A, B and C are sent back-to-back in that order through two links and a store-and-forward router. Their transmission times on link 1 are respectively 3, 1 and 2 ms; on link 2 they are respectively 1, 4 and 2 ms. Each link has a propagation delay of 2 ms. The router forwards complete packets in arrival order as soon as link 2 is free. Links operate concurrently; processing time is zero. How many milliseconds after the first bit of A leaves the source does the last bit of C reach the destination?

**Answer format:** Integer milliseconds.

### Q44. [2 Marks] [MSQ]

An n-bit two's-complement adder adds two operands and retains n result bits. Which conditions imply signed overflow?

A. Two positive operands produce a negative result.
B. Two negative operands produce a nonnegative result.
C. A positive and a negative operand produce a negative result.
D. The carry into the sign bit differs from the carry out of the sign bit.

### Q45. [2 Marks] [MSQ]

Real 4×4 matrices E,F satisfy E²=E, F²=F, EF=FE, rank(E)=3, and rank(F)=2. Which statements must hold?

A. rank(E−F) is either 1 or 3.
B. trace(E+F)=5.
C. rank(EF)=2 in every case.
D. det(E+F) is either 0 or 2.

### Q46. [2 Marks] [NAT]

Processor A has a 1 ns clock and base CPI 1. Loads constitute 30% of instructions, and 10% of loads incur a 20-cycle penalty in addition to base execution. Processor B halves the load-miss probability, retains base CPI 1 and the 20-cycle penalty, but may have a longer clock period. Penalties do not overlap and there are no other stalls. What is the largest clock period for B, in ns, for which its mean instruction time is no greater than A's? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q47. [2 Marks] [MCQ]

A singly linked list must be reversed in place. The code maintains pointers prev,cur,next and uses three assignments per iteration after saving next=cur.next. Which order preserves access to the remaining unreversed suffix?

A. cur=cur.next; cur.next=prev; prev=cur
B. cur.next=prev; prev=cur; cur=next
C. prev=cur; cur=next; cur.next=prev
D. cur.next=next; prev=next; cur=prev

### Q48. [2 Marks] [NAT]

Four symbols have frequencies 2,3,7,8. A binary Huffman code is built by repeatedly merging the two smallest weights. What is the sum over symbols of frequency times codeword length?

**Answer format:** Integer.

### Q49. [2 Marks] [MSQ]

An input describes a Turing machine M over {0,1}, with the promise that M halts on every input string. Algorithms below need only behave correctly on machines satisfying the promise. Which statements are correct?

A. Nonemptiness of L(M) is semidecidable by testing strings and eventually accepting whenever an accepted string exists.
B. Emptiness of L(M) is decidable solely because every individual simulation halts.
C. Equivalence of L(M) to the empty language is decidable under this promise.
D. Whether M accepts at least one string of length at most ten is decidable.

### Q50. [2 Marks] [NAT]

A code generator evaluates the expression tree

```text
((a+b)*(c+d)) + ((e+f)*(g+h))
```

All eight leaves are distinct values initially in memory. Loading a leaf requires one register. Each binary operation requires its two operands in registers and may overwrite either operand. Subtrees may be evaluated in either order, but tree operations may not be reassociated, recomputed, or interleaved between sibling subtrees, and no intermediate value may be spilled to memory. What is the minimum number of registers required?

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

A process's virtual address space contains a mapped region that is much larger than currently used physical memory. Pages are allocated on first write. Which statement is correct?

A. Every reserved virtual page necessarily already occupies a private physical frame.
B. Reserving address space and committing physical backing may occur at different times.
C. Virtual addresses must equal physical addresses in this arrangement.
D. The process cannot ever fault on a valid mapped virtual address.

### Q52. [2 Marks] [MSQ]

A transaction reads row x twice. Another transaction commits a change to x between the reads. Which statements are correct?

A. If the first transaction observes different committed values, this is a nonrepeatable read.
B. Such an observation necessarily means the first read saw uncommitted data.
C. Holding an appropriate shared lock on x throughout both reads prevents an intervening conflicting exclusive write lock under ordinary locking rules.
D. A nonrepeatable read necessarily involves inserting a new row rather than updating x.

### Q53. [2 Marks] [NAT]

A stop-and-wait sender retransmits one packet until it receives an acknowledgment. Each data transmission is independently lost with probability 0.2. Each successfully received copy triggers an acknowledgment, independently lost with probability 0.1. An unsuccessful attempt times out before the next begins; there are no delayed packets or acknowledgments. Count every receiver arrival, including duplicates. What is the expected number of duplicate arrivals before the sender stops, excluding the first received copy? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q54. [2 Marks] [MCQ]

A synchronous two-flip-flop machine starts at (q1,q0)=(0,1). On input 0 its next state is (0,1). On input 1 its next state is (q1 XOR q0, q1). After processing exactly five input bits, it accepts if its state is (0,1). How many of the 32 input strings are accepted?

A. 16
B. 17
C. 18
D. 20

### Q55. [2 Marks] [NAT]

X and Y are independent exponential random variables with rates 2 and 3, respectively. Find E[max(X,Y) | X<Y], rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q56. [2 Marks] [NAT]

An initially empty cache has two sets, two lines per set, and 16 bytes per line. A byte address belongs to block floor(address/16), mapped to set (block number mod 2). The cache uses LRU replacement within each set. Each miss fetches the referenced block; all accesses below are reads, in order:

```text
0, 32, 0, 64, 32, 16, 48, 80, 16
```

How many block fetches from memory occur?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

An ordinary binary search tree stores distinct integers. A search for key 45 visits keys 50,20,40,47,45 in that order. Which additional statement is consistent with the BST search constraints?

A. The next node after 40 could instead have been 48.
B. The next node after 20 could instead have been 55.
C. Every node visited after 47 on this search must have key below 47 and above 40 until 45 is found.
D. The path is impossible because it changes direction more than once.

### Q58. [2 Marks] [MCQ]

An algorithm for a directed acyclic graph computes longest paths by processing vertices in topological order and relaxing outgoing edges using maximum instead of minimum. Edge weights may be negative. Which statement is correct?

A. Negative edges invalidate this dynamic program even in a DAG.
B. A topological order ensures all predecessors are processed before a vertex, so the recurrence is valid.
C. The algorithm requires all paths to have the same number of edges.
D. The graph must first be converted to an undirected graph.

### Q59. [2 Marks] [NAT]

Grammar S→aSb | aSbb | ε generates a block of a symbols followed by b symbols. How many distinct terminal strings of length exactly six does it generate? Count strings, not derivations.

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A quadratic f(x)=ax²+bx+1 satisfies f(1)=0 and ∫₀¹f(x)dx=0. Find its minimum value on [0,1], rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q61. [2 Marks] [MCQ]

A compiler performs copy propagation on `x=y; z=x+1; y=5; w=x+1;`, with exact ordinary scalar variables and no aliases. Which replacement of both uses of x is valid for every initial y?

A. Replace both by the current y without any saved value.
B. Replace only the use in z by y; the later use needs the old value represented by x or another saved copy.
C. Replace both by 5.
D. Replace neither use under any circumstances.

### Q62. [2 Marks] [NAT]

Four processes have resource demands: P holds A and requests B; Q holds B and requests C; R holds C and requests A; S holds D and requests B. Each resource has one instance, requests block, and no process releases its held resource before receiving its request. How many processes lie on a directed cycle in the wait-for graph?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

Table T(x) contains the multiset {1,1,2,3}. A query self-joins two aliases of T on `L.x < R.x` and returns all matching pairs without DISTINCT. How many rows does it return?

**Answer format:** Integer.

### Q64. [2 Marks] [MCQ]

A resolver caches a CNAME mapping alias.example to host.example at time 0 with TTL 120 seconds, and the target's A record at time 20 with TTL 50 seconds. At time 80 it receives a new request for alias.example. Assume no prefetching, no stale-answer service, and no other cached answers. Cache hits do not refresh TTLs. Which action and remaining TTL are correct?

A. Reuse both records; each has 40 seconds remaining.
B. Reuse the CNAME with 40 seconds remaining and obtain a fresh A record for host.example.
C. Obtain a new CNAME but reuse the A record with 40 seconds remaining.
D. Reuse both records indefinitely because their names have not changed.

### Q65. [2 Marks] [NAT]

A six-bit register represents six valid one-hot states. A recovery circuit maps a word containing at least one 1 to the one-hot word retaining only its highest-index 1 (indices 0 through 5). It maps the all-zero word to the state with bit 0 set. Each of the 64 possible input words is equally likely. What is the probability that the recovered state has index at least 4?

**Answer format:** Exact finite decimal.

## ANSWER KEY — MOCK TEST 009

Integer and exact-decimal NAT answers are exact; accepted ranges are supplied for rounded answers.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 9 |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 4.472 (range 4.4715–4.4725) |
| 5 | NAT | 1 | 180 |
| 6 | NAT | 2 | 84 |
| 7 | NAT | 2 | 25 |
| 8 | NAT | 2 | 0.5333 (range 0.53325–0.53335) |
| 9 | NAT | 2 | 17 |
| 10 | MCQ | 2 | A |
| 11 | NAT | 1 | 8 |
| 12 | MCQ | 1 | B |
| 13 | NAT | 1 | 0 |
| 14 | NAT | 1 | 512 |
| 15 | MCQ | 1 | B |
| 16 | NAT | 1 | 6 |
| 17 | MSQ | 1 | A, B, C |
| 18 | NAT | 1 | 24 |
| 19 | MCQ | 1 | B |
| 20 | NAT | 1 | 0.25 |
| 21 | NAT | 1 | 0.25 |
| 22 | MCQ | 1 | B |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 3 |
| 25 | MCQ | 1 | A |
| 26 | NAT | 1 | 16 |
| 27 | MCQ | 1 | B |
| 28 | MSQ | 1 | A, C |
| 29 | MCQ | 1 | A |
| 30 | MCQ | 1 | A |
| 31 | NAT | 1 | 5 |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 6 |
| 34 | MCQ | 1 | B |
| 35 | MCQ | 1 | A |
| 36 | NAT | 2 | 22 |
| 37 | MSQ | 2 | A, C |
| 38 | MCQ | 2 | B |
| 39 | NAT | 2 | 225 |
| 40 | MSQ | 2 | A, C, D |
| 41 | NAT | 2 | 5 |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 14 |
| 44 | MSQ | 2 | A, B, D |
| 45 | MSQ | 2 | A, B, D |
| 46 | NAT | 2 | 1.2308 (range 1.23075–1.23085) |
| 47 | MCQ | 2 | B |
| 48 | NAT | 2 | 37 |
| 49 | MSQ | 2 | A, D |
| 50 | NAT | 2 | 4 |
| 51 | MCQ | 2 | B |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 0.1111 (range 0.11105–0.11115) |
| 54 | MCQ | 2 | C |
| 55 | NAT | 2 | 0.5333 (range 0.53325–0.53335) |
| 56 | NAT | 2 | 8 |
| 57 | MSQ | 2 | A, C |
| 58 | MCQ | 2 | B |
| 59 | NAT | 2 | 2 |
| 60 | NAT | 2 | -0.3333 (range -0.33335–-0.33325) |
| 61 | MCQ | 2 | B |
| 62 | NAT | 2 | 3 |
| 63 | NAT | 2 | 5 |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 0.75 |

