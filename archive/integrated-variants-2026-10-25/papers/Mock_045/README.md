# GATE CS 2027 — Full-Length Mock Test 045

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

Choose the order that gives the clearest causal sequence.

P. The alarm then sounded as designed.
Q. The technician first disconnected the sensor's power supply.
R. This demonstrated that the system detected the simulated failure.
S. The disconnection removed the sensor's normal signal.

A. Q–S–P–R
B. P–Q–R–S
C. S–R–Q–P
D. Q–R–S–P

### Q2. [1 Mark] [NAT]

Cards labelled1,2,3 are placed in uniformly random order. Given that the first card's number is smaller than the second card's number, what is the probability that the second card's number is smaller than the third card's number?

**Answer format:** Decimal rounded to four places.

### Q3. [1 Mark] [MCQ]

“The conclusion is provisional and may be revised after further trials.” Which word is closest in meaning to provisional here?

A. Irrevocable
B. Tentative
C. Unrelated
D. Unanimous

### Q4. [1 Mark] [NAT]

For real x>0 with x≠1, solve log_x(16)=log_2(x). What is the sum of all valid solutions x?

**Answer format:** Exact decimal.

### Q5. [1 Mark] [MCQ]

Every one of twelve sampled buses on a route arrived late on a rainy morning. Which conclusion is supported without treating this sample as a proof about every bus?

A. Rain makes every bus on every route late.
B. The observations suggest lateness on this route under these conditions, but do not establish a universal rule.
C. No bus on this route can arrive on time in dry weather.
D. Rain is proven to be the only possible cause of lateness.

### Q6. [2 Marks] [MSQ]

Unit cubes form four vertical columns on a 2×2 grid, with no gaps within a column. All four columns are nonempty. Let h(i,j) be the positive integer height in row i, column j. Orthographic views establish

```text
max(h(1,1),h(1,2)) = 3
max(h(2,1),h(2,2)) = 2
max(h(1,1),h(2,1)) = 3
max(h(1,2),h(2,2)) = 2
```

Which total numbers of cubes are possible?

A. 7
B. 8
C. 9
D. 10

### Q7. [2 Marks] [NAT]

Evaluate the sum from n=1 to8 of1/[n(n+2)].

**Answer format:** Decimal rounded to four places.

### Q8. [2 Marks] [NAT]

An open rectangular box is made by cutting equal squares of integer side x from the four corners of a 20 cm by 12 cm sheet and folding the remaining flaps. Here x is a positive integer and the box must have positive dimensions. What is the largest possible volume in cubic centimetres?

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

Five presentations P,Q,R,S,T occupy five consecutive slots, one per slot. Q occurs immediately after P. R occurs before P, and S occurs after Q. How many schedules satisfy these restrictions?

A. 2
B. 4
C. 6
D. 8

### Q10. [2 Marks] [NAT]

Five distinct people A,B,C,D,E occupy five seats in a row. C must occupy an end seat, and A and B must not be adjacent. How many seating orders satisfy both requirements?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

An unweighted directed graph has exactly the edges s→a, s→b, a→c, a→d, b→d, c→t, d→t. Which pair gives the shortest s-to-t path length in edges and the number of distinct shortest s-to-t paths?

A. (3,3)
B. (3,2)
C. (4,3)
D. (3,4)

### Q12. [1 Mark] [MSQ]

In a group, distinct nonidentity elements a,b satisfy a²=b²=e. Which statements are correct?

A. (ab)^(−1)=ba.
B. The group must be abelian.
C. If a and b commute, ab has order2.
D. If ab has order2, a and b commute.

### Q13. [1 Mark] [NAT]

A four-bit ALU performs a logical left shift by one on bit pattern1011, discarding the outgoing most significant bit and filling the low bit with0. Interpret the result as a signed two's-complement integer. What value results?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

A four-variable function, with bit order A,B,C,D from most to least significant, is1 exactly at minterms0,2,8,10. Which statements are correct?

A. These four minterms form a single valid four-cell Karnaugh-map group.
B. A must be fixed to one value throughout that group.
C. C must be fixed to one value throughout that group.
D. The group is represented by (NOT B) AND (NOT D).

### Q15. [1 Mark] [NAT]

A lexer recognizes identifiers matching a letter followed by zero or more letters or digits, integer literals matching one or more digits, and the operators '=', '==', '>'. It uses longest match and skips spaces. How many tokens does it emit for the input below?

```text
a1===23> b
```

**Answer format:** Integer.

### Q16. [1 Mark] [MSQ]

G is a connected simple undirected graph with degree multiset {3,3,2,2,2,2}. Which statements must hold?

A. G has exactly 7 edges.  
B. G has an Euler trail that uses every edge exactly once.  
C. G is bipartite.  
D. G has a Hamiltonian cycle.

### Q17. [1 Mark] [MSQ]

A router runs link-state routing. Assume all routers have received the same complete link-state database and use the same positive link costs. Which statements are correct?

A. Routers can independently compute shortest paths from that database.
B. Each router needs only its neighbours' currently advertised distances, with no topology information.
C. Different source routers may obtain different shortest-path trees from the same database.
D. Identical topology information forces every router to choose the same next hop for a fixed destination.

### Q18. [1 Mark] [NAT]

How many surjective functions f:{1,2,3,4,5}→{a,b,c} satisfy f(1)=f(2)?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

What is the coefficient of x⁷ in the formal power series 1/((1−x)(1−x²))?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

For grammar S→aA | aB, A→b, B→c, which statements are true?

A. The two S alternatives conflict in an LL(1) predictive table.
B. The generated language is inherently ambiguous.
C. Replacing the grammar by S→aX, X→b | c gives an LL(1) grammar for the same language.
D. No deterministic parser can recognize the generated language.

### Q21. [1 Mark] [MSQ]

A prime-implicant chart has columns 1,2,3 and rows P covering {1,2}, Q covering {2,3}, R covering {1,3}. All columns must be covered. Which statements are true?

A. P is essential because it covers two columns.
B. No prime implicant is essential.
C. Two rows suffice to cover all columns.
D. The absence of an essential prime implicant means no cover exists.

### Q22. [1 Mark] [NAT]

Three jobs arrive at0. Estimated CPU bursts for A,B,C are1,2,3, while actual bursts are8,1,1. A nonpreemptive scheduler executes jobs by increasing estimate. What is its total waiting time minus the minimum total waiting time attainable with knowledge of the actual bursts? There is no switching overhead.

**Answer format:** Integer time units.

### Q23. [1 Mark] [NAT]

An IPv4 fragment arrives with total length 1020 bytes, header length 20 bytes, fragment offset 100, and MF=1. A router forwards it through an interface with MTU 620 bytes and fragments it into the minimum number of fragments, using the largest permitted payload in the first new fragment. Every outgoing header is 20 bytes. What is the fragment-offset field of the second outgoing fragment?

**Answer format:** Numeric value; integer.

### Q24. [1 Mark] [NAT]

A control store contains 512 microinstructions, each 40 bits wide. How many bits are needed to address a microinstruction within that store?

**Answer format:** Integer.

### Q25. [1 Mark] [MSQ]

L is a finite language over a finite alphabet. Which statements necessarily hold?

A. L is regular.
B. L is context-free.
C. L contains the empty string.
D. Some DFA recognizes L.

### Q26. [1 Mark] [NAT]

Let A have rows (1,1),(1,1). Find trace(A⁵).

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

For the unary regular language {a^(3k):k≥0}, what is the smallest positive pumping length satisfying the regular pumping lemma, including |xy|≤p and |y|>0?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

A disk scheduler uses LOOK, moving toward increasing cylinder numbers. The head is at 40; pending requests are 10,30,55,70. No further requests arrive. Which service order follows?

A. 55,70,30,10
B. 30,10,55,70
C. 55,30,70,10
D. 70,55,30,10

### Q29. [1 Mark] [NAT]

What value is printed by this C program? All accesses are within the array.

```c
#include <stdio.h>
void change(int *p) {
    p += 2;
    *p = *(p - 1) + *p;
}
int main(void) {
    int a[4] = {3, 5, 7, 9};
    int *p = a + 1;
    change(p);
    printf("%d", *p + a[3]);
    return 0;
}
```

**Answer format:** Exact integer.

### Q30. [1 Mark] [NAT]

A fixed-length file uses unspanned records of 90 bytes and blocks of 512 bytes, with no headers. It currently contains 12 records packed into the fewest possible blocks. How many additional records can be inserted without allocating another block, if records may be rearranged within the allocated blocks?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MCQ]

An algorithm outputs every unordered pair of distinct elements from an n-element input, with one constant-time operation per emitted pair. What is the tight asymptotic lower bound arising from output size alone?

A. Ω(log n)
B. Ω(n)
C. Ω(n log n)
D. Ω(n²)

### Q32. [1 Mark] [MCQ]

A hash table has indices 0–6, hash h(k)=k mod 7, and linear probing. Insert 10,17,24 into an empty table, then delete 17 by leaving a tombstone. A successful search for 24 must continue past tombstones. Afterwards insert 31, known absent, reusing the first available tombstone. What are the number of slots inspected in the search for 24 and the index occupied by 31?

A. (2,4)  
B. (3,4)  
C. (3,6)  
D. (2,5)

### Q33. [1 Mark] [NAT]

A router has routes192.0.2.0/24→A,192.0.2.128/25→B and192.0.2.160/27→C, using longest-prefix match. How many addresses in192.0.2.0/24 are forwarded to B?

**Answer format:** Integer address count; include all addresses in the ranges.

### Q34. [1 Mark] [MSQ]

For a unary relation R(x), compare tuple-calculus expressions E1={t | R(t)} and E2={t | NOT R(t)}. Values of t range over an external domain containing the active domain of R. Which statements are correct?

A. E1 is unchanged if the external domain is enlarged without changing R.
B. E2 is unchanged under every such enlargement.
C. E2 can gain tuples when the external domain is enlarged.
D. E1 necessarily returns every element of the external domain.

### Q35. [1 Mark] [MCQ]

Consider this recursive function on a positive integer n. Arithmetic is exact.

```text
f(n):
    if n == 1: return 1
    r = f(floor(n/2))
    if n is even: return 2*r
    else: return 2*r + 1
```

Which pair gives f(45) and the number of simultaneous active calls at maximum recursion depth, including the initial and base calls?

A. (45,6)  
B. (45,5)  
C. (32,6)  
D. (63,6)

### Q36. [2 Marks] [NAT]

A NAT maintains separate TCP and UDP port-allocation pools, each containing the same100 public port numbers on one public IP. Within each protocol a public port may serve only one live internal endpoint; ports are not shared within a protocol even for different remote peers. There are90 live TCP mappings and95 live UDP mappings. How many further mappings can be admitted if new arrivals contain at least100 TCP requests and at least100 UDP requests and no mapping expires?

**Answer format:** Exact integer.

### Q37. [2 Marks] [NAT]

For n = 128, consider the following pseudocode, where all bounds are integers. The operation `touch` takes one unit of time. How many times is `touch` executed?
```text
width = 1
while width < n:
    base = 0
    while base < n:
        for offset = 0 to width-1 inclusive:
            touch(base + offset)
        base = base + 2*width
    width = 2*width
```


**Answer format:** Numeric value; integer.

### Q38. [2 Marks] [NAT]

A translation for binary digit strings synthesizes attributes len and val. A single bit b has len=1,val=b; concatenating strings X,Y gives len=X.len+Y.len and val=X.val·2^(Y.len)+Y.val. The parsed representation of101.101 treats the parts on either side of the point as separate strings and returns left.val+right.val/2^(right.len). What value is returned?

**Answer format:** Exact decimal.

### Q39. [2 Marks] [MSQ]

In C, a function returns a pointer in each of the following independent versions. Assume allocations succeed and no frees occur before the caller's first access. Which versions permit the caller to access a live int object through the returned pointer after the function returns?

A. `int *f(void) { int x=7; return &x; }`
B. `int *f(void) { static int x=7; return &x; }`
C. `int *f(void) { int *p=malloc(sizeof *p); *p=7; return p; }` with the proper standard header.
D. `int *f(void) { int a[1]={7}; return a; }`

### Q40. [2 Marks] [MSQ]

For real t consider

```text
x1 + x2 + x3 = 1
x1 + 2x2 + 3x3 = 2
2x1 + 3x2 + 4x3 = t
```

Which statements are correct?

A. The system is consistent exactly when t=3.
B. When t=3, there are infinitely many solutions.
C. Every solution satisfies x1=x3.
D. When t=3, the coefficient matrix is invertible.

### Q41. [2 Marks] [NAT]

In an idealized TCP congestion-avoidance model, cwnd starts at 4 MSS. Each complete loss-free RTT acknowledges the entire current window, then cwnd increases by exactly 1 MSS. The receiver window never limits transmission. How many MSS are transmitted over the first four RTTs? Count each round's transmitted data before its increase.

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

A TLB entry is keyed by(ASID, virtual page). A process with ASID5 terminates, leaving cached translations. A new process is assigned ASID5 with a different page table; the old translations are not invalidated. Which statements are correct?

A. A stale entry can translate the new process's address to an old physical frame.
B. The ASID field by itself makes reuse safe forever.
C. Invalidating entries for the reused ASID before execution prevents this stale-entry problem.
D. Merely changing the page-table base necessarily makes all old ASID-tagged entries miss.

### Q43. [2 Marks] [MSQ]

An algorithm is given a Turing machine M promised to halt on every input and an integer n≥0. Which tasks can be decided by an algorithm that terminates on every promised input?

A. Determine whether M accepts every binary string of length exactly n.
B. Determine whether M accepts at least one binary string of length at most n.
C. Determine whether M accepts every binary string of arbitrary length.
D. Determine whether M accepts no binary strings of arbitrary length.

### Q44. [2 Marks] [NAT]

For real constants a,b, define f(x)=(sqrt(1+x)−1)/x when x>0 and f(x)=ax+b when x≤0. Choose a,b so that f is differentiable at0. What is a+b?

**Answer format:** Exact decimal.

### Q45. [2 Marks] [MSQ]

In the interval-scheduling problem, intervals are half-open and all have equal value. Which statements are correct about choosing a compatible interval with earliest finishing time at each step?

A. An exchange argument can replace the first interval of an optimal solution by an earliest-finishing interval without reducing the number still schedulable afterward.
B. The same rule necessarily maximizes total value when intervals have arbitrary positive weights.
C. Half-open intervals ending and starting at the same time are compatible.
D. Choosing the longest interval first is always equivalent to earliest finish.

### Q46. [2 Marks] [MCQ]

A TCP server has a listening socket and accepts two connections, producing descriptors c1 and c2. It then closes only the listening socket. No shutdown is applied to c1 or c2. Which statement is correct?

A. Both accepted connections necessarily close immediately.
B. c1 and c2 remain usable; closing the listener does not itself close those connected sockets.
C. c1 becomes a new listening socket automatically.
D. The two clients must now share one TCP byte stream.

### Q47. [2 Marks] [MSQ]

Two sorted singly linked lists have distinct prefix nodes but share the same suffix nodes. A standard in-place merge is written assuming disjoint lists: it links the smaller current node to the result, advances that list pointer, and repeats, without testing pointer equality. Which statements are correct?

A. Shared nodes can make the merge create a cycle or fail to terminate.
B. If both current pointers are equal, appending that shared suffix once and terminating avoids duplicate processing of that suffix.
C. Equality of node values alone proves that two pointers refer to the same node.
D. Sortedness alone guarantees safety of this disjoint-list merge on shared-suffix inputs.

### Q48. [2 Marks] [NAT]

A stack stores integers using the following minimum-encoding scheme. The first push stores the value and sets m to it. To push x<m, store 2x−m and set m=x; otherwise store x. When popping a stored value y<m, return the old m and then set m=2m−y; otherwise return y and leave m unchanged. Arithmetic has unlimited precision. Starting empty, execute push(7), push(3), push(5), push(−2), pop(), pop(), push(1), pop(), pop(). What is the sum of the four returned values?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

Under lexical scope, an outer procedure activation P1 has local x=10 and creates a nested procedure Q1 that refers to P1.x. A later separate activation P2 has local x=20 and calls Q1, passing no x parameter. Environments are retained correctly for nested procedures. What value of x does Q1 read?

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

Reads return the latest preceding write in this schedule:

```text
w1(x); r2(x); w2(y); r3(y); c1; c2; c3
```

Which properties hold?

A. Recoverability.  
B. Cascadelessness.  
C. Conflict serializability.  
D. Strictness.

### Q51. [2 Marks] [MCQ]

A resolver caches a CNAME mapping alias.example to host.example at time 0 with TTL 120 seconds, and the target's A record at time 20 with TTL 50 seconds. At time 80 it receives a new request for alias.example. Assume no prefetching, no stale-answer service, and no other cached answers. Cache hits do not refresh TTLs. Which action and remaining TTL are correct?

A. Reuse both records; each has 40 seconds remaining.
B. Reuse the CNAME with 40 seconds remaining and obtain a fresh A record for host.example.
C. Obtain a new CNAME but reuse the A record with 40 seconds remaining.
D. Reuse both records indefinitely because their names have not changed.

### Q52. [2 Marks] [NAT]

A byte-addressed device has256 byte locations. Its chip-select decoder matches address bits15–12 to1010, while address bits11–8 are ignored; bits7–0 address the device. Within the16-bit address space, how many distinct CPU byte addresses alias device offset0x35?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

Independent Bernoulli random variables X,Y have success probabilities1/2 and1/3. Define Z=X+Y and W=XY. What is Cov(Z,W)?

**Answer format:** Decimal rounded to four places.

### Q54. [2 Marks] [NAT]

A TLB lookup takes 2 ns and each physical memory access takes 50 ns, with no overlap. The page table has two levels in memory. A TLB hit needs only the final data access; a miss needs two page-table accesses followed by the data access. All pages are resident. If the TLB hit probability is 0.9, what is the mean access time in ns?

**Answer format:** Exact integer.

### Q55. [2 Marks] [MCQ]

A basic block ends with `x=a+b; y=x*c; x=0; return y;`, using exact scalar arithmetic and no externally observable intermediate assignments. Which first assignment is dead solely because x is overwritten later?

A. x=a+b is dead.
B. y=x*c is dead.
C. Neither of these assignments is dead: y uses the first x value and return uses y.
D. Both are dead.

### Q56. [2 Marks] [MSQ]

On a Unix-style file system, an ordinary file has two hard-link names and an open descriptor. Both names are unlinked, but the descriptor remains open and has suitable access permission. No other references exist. Which statements are correct?

A. Reading the file's data through the open descriptor remains possible.  
B. The file's data blocks must be freed immediately after the second unlink.  
C. Opening either removed pathname fails unless a new directory entry is created there.  
D. The inode's hard-link count remains 1 because an open descriptor is a hard link.

### Q57. [2 Marks] [NAT]

A longest-common-subsequence computation compares strings ABA and BAA. What is the length of a shortest common supersequence of the two strings?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A sequential detector outputs one exactly when the prefix read so far ends in 101; otherwise it outputs zero. Overlapping occurrences are detected. Starting with no input history, how many one outputs occur while reading 1010101, one bit per clock?

**Answer format:** Integer.

### Q59. [2 Marks] [MCQ]

Initially X=Y=0. Transactions perform r1(X), r2(Y), w1(Y=1), w2(X=1), and then both commit. Each read sees the initial value. Which statement is correct?

A. The schedule is conflict serializable in order T1,T2.
B. The schedule is conflict serializable in order T2,T1.
C. The precedence graph has a cycle, and neither serial order reproduces both reads.
D. No conflict exists because the writes target different items.

### Q60. [2 Marks] [NAT]

A four-bit signed fixed-point format has no fractional bits and uses saturating addition: results above 7 become 7, and results below −8 become −8. Let ⊕ denote this addition. For a=6,b=5,c=−4, what is `a⊕(b⊕c) − ((a⊕b)⊕c)`, with the final subtraction performed as an exact ordinary integer subtraction?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

On A={1,2,3,4}, let τ interchange1 and2 and fix3 and4. How many functions f:A→A satisfy f(τ(x))=τ(f(x)) for every x?

**Answer format:** Integer.

### Q62. [2 Marks] [MCQ]

A process's virtual address space contains a mapped region that is much larger than currently used physical memory. Pages are allocated on first write. Which statement is correct?

A. Every reserved virtual page necessarily already occupies a private physical frame.
B. Reserving address space and committing physical backing may occur at different times.
C. Virtual addresses must equal physical addresses in this arrangement.
D. The process cannot ever fault on a valid mapped virtual address.

### Q63. [2 Marks] [MSQ]

Consider a CFG with start S and productions S→AB | C, A→aA | a, B→bB, C→cC | ε, D→d. A useful nonterminal must occur in some derivation from S that ends in a terminal string. Which statements are correct?

A. The generated language is c*.
B. A is useful because it is reachable from S and generates terminal strings.
C. Exactly two nonterminals are useful.
D. D is useful because it generates d.

### Q64. [2 Marks] [NAT]

For the grammar S→SS | a, how many distinct parse trees generate a string of five a's? Count trees, not different orders of expanding independent nodes.

**Answer format:** Exact integer.

### Q65. [2 Marks] [NAT]

A fully associative cache with LRU holds three blocks and initially contains A,B,C, with A least recent and C most recent. References are A,D,B. How many misses occur?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 045

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 4.25 |
| 5 | MCQ | 1 | B |
| 6 | MSQ | 2 | A, B, C |
| 7 | NAT | 2 | 0.6444 (accepted range 0.64435–0.64445) |
| 8 | NAT | 2 | 256 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 24 |
| 11 | MCQ | 1 | A |
| 12 | MSQ | 1 | A, C, D |
| 13 | NAT | 1 | 6 |
| 14 | MSQ | 1 | A, D |
| 15 | NAT | 1 | 6 |
| 16 | MSQ | 1 | A, B |
| 17 | MSQ | 1 | A, C |
| 18 | NAT | 1 | 36 (exact) |
| 19 | NAT | 1 | 4 |
| 20 | MSQ | 1 | A, C |
| 21 | MSQ | 1 | B, C |
| 22 | NAT | 1 | 14 |
| 23 | NAT | 1 | 175 (exact) |
| 24 | NAT | 1 | 9 |
| 25 | MSQ | 1 | A, B, D |
| 26 | NAT | 1 | 32 |
| 27 | NAT | 1 | 3 |
| 28 | MCQ | 1 | A |
| 29 | NAT | 1 | 21 |
| 30 | NAT | 1 | 3 |
| 31 | MCQ | 1 | D |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 96 |
| 34 | MSQ | 1 | A, C |
| 35 | MCQ | 1 | A |
| 36 | NAT | 2 | 15 |
| 37 | NAT | 2 | 448 (exact) |
| 38 | NAT | 2 | 5.625 |
| 39 | MSQ | 2 | B, C |
| 40 | MSQ | 2 | A, B, C |
| 41 | NAT | 2 | 22 |
| 42 | MSQ | 2 | A, C |
| 43 | MSQ | 2 | A, B |
| 44 | NAT | 2 | 0.375 |
| 45 | MSQ | 2 | A, C |
| 46 | MCQ | 2 | B |
| 47 | MSQ | 2 | A, B |
| 48 | NAT | 2 | 7 |
| 49 | NAT | 2 | 10 |
| 50 | MSQ | 2 | A, C |
| 51 | MCQ | 2 | B |
| 52 | NAT | 2 | 16 |
| 53 | NAT | 2 | 0.1944 (accepted range 0.19435–0.19445) |
| 54 | NAT | 2 | 62 |
| 55 | MCQ | 2 | C |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 4 |
| 58 | NAT | 2 | 3 |
| 59 | MCQ | 2 | C |
| 60 | NAT | 2 | 4 |
| 61 | NAT | 2 | 16 |
| 62 | MCQ | 2 | B |
| 63 | MSQ | 2 | A, C |
| 64 | NAT | 2 | 14 |
| 65 | NAT | 2 | 2 |
