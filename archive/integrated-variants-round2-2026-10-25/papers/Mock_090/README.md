# GATE CS 2027 — Full-Length Mock Test 090

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

In “The researchers preferred the more parsimonious explanation,” parsimonious most appropriately describes an explanation that:

A. refuses to consider any evidence.
B. accounts for the observations with fewer unnecessary assumptions.
C. contains the greatest number of technical terms.
D. is necessarily true because it is shorter.

### Q2. [1 Mark] [NAT]

For positive numbers x and y, log2(x)+log2(y)=7 and log2(x/y)=3. What is x?

**Answer format:** Exact number.

### Q3. [1 Mark] [NAT]

After observing3,5,7, someone conjectures that every odd integer greater than1 is prime. What is the smallest integer satisfying the stated domain that disproves the conjecture?

**Answer format:** Integer.

### Q4. [1 Mark] [NAT]

The central unit square is removed from a3×3 board of unit squares. How many tilings of the remaining eight squares by1×2 dominoes exist? Rotations and reflections of a tiling count as different if the occupied domino pairs differ.

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A sequence is formed by writing one copy of 1, two copies of 2, three copies of 3, and so on. What is the sum of the entries in positions 90 through 94, counting the first entry as position 1?

**Answer format:** Exact integer.

### Q6. [2 Marks] [NAT]

A shortest lattice path from (0,0) to (4,3) uses only unit steps right or up. It must visit (1,1) and must not visit (3,2). How many such paths exist?

**Answer format:** Integer.

### Q7. [2 Marks] [MCQ]

A policy says, “Unless a submission is anonymous, it must include the author's name.” Which submission violates this rule?

A. An anonymous submission without a name.
B. A nonanonymous submission with a name.
C. A nonanonymous submission without a name.
D. An anonymous submission with a name.

### Q8. [2 Marks] [NAT]

An examination awards4 marks for a correct response, subtracts1 for a wrong response and awards0 for an omitted question. A candidate attempted75% of40 questions and scored75 marks. How many attempted responses were wrong?

**Answer format:** Integer.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Five distinct talks A,B,C,D,E are scheduled in positions 1 through 5. C is last. A occurs before C. Exactly one talk lies between B and D. E is neither first nor last. Which statements are true over schedules satisfying all these conditions?

A. A can be fourth.  
B. A must occur before E.  
C. E can be third.  
D. B and D must both occupy odd-numbered positions.

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Solid stacks of unit cubes stand in a 2-by-3 grid. Each stack has a nonnegative integer height and has no gaps. Looking along the two-row direction, the maximum heights in the three columns are 2,3,1 respectively. Looking along the three-column direction, the maximum heights in the two rows are 3,2 respectively. What pair gives the minimum and maximum possible total number of cubes?

A. (7,11)  
B. (6,11)  
C. (6,12)  
D. (8,12)

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A pipeline issues one instruction per cycle except for branch-misprediction stalls. Branches are 20% of instructions, 25% of branches are mispredicted, and every misprediction adds four nonoverlapping stall cycles. Ignoring filling and draining, find its average CPI.

**Answer format:** Exact finite decimal.

### Q12. [1 Mark] [NAT]

A file's logical blocks0,1,2 map to disk blocks40,41,90. A system reads logical blocks0–2 in order. Adjacent disk block numbers can be transferred as one contiguous disk extent. What is the minimum number of extents that contain precisely these requested blocks?

**Answer format:** Integer.

### Q13. [1 Mark] [MSQ]

Which of the following problems have an algorithm that always halts and answers correctly? Machines have finite descriptions; Turing machines are deterministic.

A. Given a Turing machine and an input, determine whether it halts within 100 transitions.  
B. Given a Turing machine and an input, determine whether it eventually halts.  
C. Given a DFA over {0,1}, determine whether it accepts every binary string.  
D. Given a Turing machine, determine whether it halts on every input.

### Q14. [1 Mark] [NAT]

X is binomial with four trials and success probability p, where 0<p<1. Given P(X=0)=P(X=2), find E[X], rounded to three decimal places.

**Answer format:** Number to 3 decimal places.

### Q15. [1 Mark] [NAT]

Memory has four banks, with word address w mapped to bank w mod 4. A bank stays busy for four cycles after a request starts; its result becomes available exactly four cycles after the start. Only one request may start per cycle. Requests to words 0,4,8,12 are issued in order as early as permitted, beginning at time 0. At what cycle time is the last result available?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

Two Ethernet stations independently select a uniformly random integer backoff from {0,1,…,7}. What is the probability that exactly one selects zero?

**Answer format:** Decimal rounded to five places.

### Q17. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For exact integer arithmetic with no side effects, which local replacements preserve a variable x's value for all x?

A. x+0 → x  
B. x*1 → x  
C. x*0 → x  
D. x−x → 0

### Q18. [1 Mark] [NAT]

A sorted file has 64 data blocks. A sparse primary index has one entry per data block and fits in a single memory-resident index block. A key search uses that index to identify the correct data block; keys are distinct. How many disk block reads are needed to retrieve a present record, assuming the data block is not cached?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A B+ tree's root contains separator20 and has two leaf children: [5,10] and [20,30]. The separator is defined as the minimum key of the right child. Each leaf must contain at least one key. After deleting20, which action is required under this separator convention?

A. Merge the leaves because a leaf cannot contain one key.  
B. Change the root separator to30; no merge is required.  
C. Leave separator20 because internal separators must never change.  
D. Remove the root and discard the left leaf.

### Q20. [1 Mark] [NAT]

A combinational block has three-bit input x and three-bit output y. It computes y=x+1 modulo 8. How many of the eight input values cause all three output bits to differ from the corresponding input bits?

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

A language L is accepted by a DFA. Which operations always produce another regular language?

A. Reverse every word of L.
B. Take the complement of L over the same alphabet.
C. Intersect L with an arbitrary context-free language.
D. Concatenate L with itself.

### Q22. [1 Mark] [NAT]

A dynamic program counts ordered sequences of steps of sizes1 or2 whose sum is4, but forbids two consecutive size1 steps. How many sequences are counted?

**Answer format:** Integer.

### Q23. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A real function f is defined on a neighbourhood of0. Which statements are correct?

**Candidates**

**I.** Differentiability at0 implies continuity there.

**II.** Continuity at0 implies differentiability there.

**III.** If both one-sided derivatives at0 exist as finite real numbers, f is continuous at0 even if those derivatives differ.

**IV.** Equal finite one-sided derivatives at0 are insufficient for differentiability there.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II

### Q24. [1 Mark] [NAT]

An algorithm partitions a size-27 input into three equal subproblems at each nontrivial call, stopping at size one. How many internal calls occur in its complete recursion tree?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

A depth-first search starts at vertex a in an undirected graph with edges ab,ac,bd,cd,ce. Neighbours are examined alphabetically. How many tree edges lie on the DFS-tree path from a to e?

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Router A reaches destination D through neighbour B at total cost 5; A also has a direct link to D of cost 8. A currently selects B as next hop. With poisoned reverse, what distance to D does A advertise to B for this selected route?

A. 5  
B. 8  
C. Infinity  
D. The cost of A's link to B only

### Q27. [1 Mark] [NAT]

A rooted binary tree has eight leaves and three nodes with exactly one child. Every other non-leaf has exactly two children. How many vertices does the tree have in total?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A three-variable Boolean function has ON minterms 1,3,5, with variable order abc and a most significant. All other minterms are OFF except minterm 7, which may first be treated as a don't-care. What is the increase in minimum SOP literal count when minterm 7 is instead required to be OFF? Count repeated literal occurrences separately.

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A disk scheduler selects the pending request requiring the least head movement. The head begins at 50. Requests at 45 and80 are pending at time0. After servicing45, but before the next selection, a new request at 44 arrives. No other arrivals occur. What total head movement occurs before all three requests finish?

**Answer format:** Exact integer.

### Q30. [1 Mark] [MCQ]

Which sequence can be the preorder traversal of a BST with distinct keys and the ordinary strict ordering property?

A. 40,20,10,30,60,50,70
B. 40,20,50,10,60,30,70
C. 40,60,50,20,10,30,70
D. 40,20,30,10,60,50,70

### Q31. [1 Mark] [NAT]

X is uniformly distributed over {−2,−1,0,1,2}, and Y=X². What is E[Y²]?

**Answer format:** Exact decimal.

### Q32. [1 Mark] [NAT]

How many functions f:{1,2,3}->{1,2,3} satisfy f(f(x))=f(x) for every x and have exactly two fixed points? A fixed point is an x for which f(x)=x.

**Answer format:** Numeric value; integer.

### Q33. [1 Mark] [NAT]

An unknown Boolean condition selects one of two branches. The first assigns x=2 and y=x; the second assigns x=3 and y=x. Immediately after the branches join, z=x−y is evaluated with exact arithmetic. What value is guaranteed for z even though neither x nor y individually has a unique constant value at the join?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A real2×2 matrix A has trace5 and determinant6. What is trace(A²)?

**Answer format:** Exact integer.

### Q35. [1 Mark] [NAT]

An IPv4 fragment has a 20-byte header, total length 420 bytes, and fragment-offset field 100. At what payload byte offset, measured from the start of the original datagram's payload, does this fragment end? Give the exclusive end offset.

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

An open box is made by removing equal squares of side x from the corners of a 12×12 square sheet and folding the sides. For 0<x<6, what is the maximum box volume?

**Answer format:** Integer cubic units.

### Q37. [2 Marks] [NAT]

A network advertises exactly the address range10.8.0.0 through10.8.5.255, inclusive, using nonoverlapping CIDR prefixes and no addresses outside this range. What is the minimum number of prefixes required?

**Answer format:** Exact integer.

### Q38. [2 Marks] [NAT]

A fair coin selects whether a second experiment uses two or three independent tosses of another fair coin. You are told only that the second experiment contained at least one head. What is the conditional probability that it used three tosses? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q39. [2 Marks] [NAT]

Let D be the positive divisors of 30, ordered by divisibility. How many bijections f:D→D preserve the order in both directions, meaning x divides y if and only if f(x) divides f(y)?

**Answer format:** Integer.

### Q40. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-bit two's-complement ALU computes subtraction as A+(bitwise NOT B)+1 and discards the final carry. For A=0111 and B=1111, which statements are correct?

A. The four result bits are1000.  
B. There is a final carry-out of1.  
C. Signed overflow occurs.  
D. Interpreting the operands as unsigned integers, the subtraction needs a borrow.

### Q41. [2 Marks] [NAT]

Immediately before this fragment, x and y hold arbitrary values. Immediately afterward, both are needed. A compiler gives each of the names x,y,t one fixed register throughout the fragment. Two names that are simultaneously live must use different registers; live ranges may not be split and the assignments may not be rewritten.

```text
t = x
x = y
y = t
```

What is the minimum number of registers under these rules?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

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

### Q43. [2 Marks] [MSQ]

Consider the following complete read/write schedule; commits occur afterwards and are omitted. Subscripts identify transactions. Repeated writes by one transaction are distinct operations. The read returns the value written by the latest preceding write.

```text
w1(x); w2(x); w3(y); w2(y); r4(x); w4(y); w1(x)
```

A view-equivalent serial schedule must preserve the transaction from which every read obtains its value, any reads of initial values, and the final writer of each item. A serial order includes all four transactions, preserving each transaction's internal operation order. Which statements are correct?

A. The displayed schedule is conflict-serializable.  
B. The displayed schedule is view-serializable.  
C. Exactly two transaction orders give view-equivalent serial schedules.  
D. If only the first operation w1(x) is deleted, the resulting schedule has exactly one conflict-equivalent serial transaction order.

### Q44. [2 Marks] [NAT]

A NAT maintains separate TCP and UDP port-allocation pools, each containing the same100 public port numbers on one public IP. Within each protocol a public port may serve only one live internal endpoint; ports are not shared within a protocol even for different remote peers. There are90 live TCP mappings and95 live UDP mappings. How many further mappings can be admitted if new arrivals contain at least100 TCP requests and at least100 UDP requests and no mapping expires?

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

Let A be the4×4 tridiagonal matrix with diagonal entries2, immediate subdiagonal and superdiagonal entries−1, and all other entries0. In its LU factorization without pivoting, with L unit lower triangular, what is U's last diagonal entry?

**Answer format:** Exact decimal.

### Q46. [2 Marks] [NAT]

A B+ tree has a root with two leaf children. The leaves, in order, contain [5,10] and [20,25]. A leaf holds at most three keys; an overflowing four-key leaf splits into two leaves with two keys each. Internal separators are the smallest keys in the nonleftmost child. The root can hold up to three separators. Insert 15, then 12, then 30. What is the sum of the root's separators afterward?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A binary min-heap with fifteen distinct keys uses array indices 1–15. Across all valid assignments of those keys to a heap, how many different indices can contain the third-smallest key?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

A directed graph on vertices0,1,2,3 is stored in CSR form with row offsets[0,2,3,5,5] and neighbour array[1,3,2,0,3]. Reverse every edge and build CSR again, retaining the same vertex order. What is the new row offset for vertex3?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

A directed graph has edges s→a(4),s→b(1),b→a(1),a→t(2),b→t(8). How many edges are in its unique shortest s-to-t path?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

A microsequencer stores a subroutine return address in one link register, with no stack or other saved copy. Main calls micro-subroutine U, which calls V before returning. V returns via the link register, then U also returns through it. How many distinct return addresses must be simultaneously preserved at the moment V is entered for both returns to work correctly?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

A prime-implicant chart has six required columns 1–6 and four available implicants. Their coverage is P:{1,2,3}, Q:{3,4}, R:{4,5,6}, S:{1,5,6}. All implicants have equal cost. How many distinct minimum-cardinality covers of all columns exist?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A TCP sender has cwnd=10 MSS and advertised receive window rwnd=8 MSS. There are already 6 MSS of unacknowledged data. One arriving cumulative acknowledgment acknowledges 2 MSS and advertises rwnd=5 MSS. Assume cwnd stays 10 MSS and no other acknowledgments arrive. What is the maximum additional data, in MSS units, that the sender may transmit immediately after processing this acknowledgment?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

A buddy allocator manages one aligned1024-byte region and rounds each request up to a power of two, with no headers. It allocates A=200 bytes at address0, B=200 bytes at address256, and C=400 bytes at address512. After freeing A and B, what is the largest new single request, in bytes, that can be satisfied without freeing C?

**Answer format:** Exact integer.

### Q54. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider this straight-line fragment. All variables are integers, addresses are valid, and there are no volatile objects or concurrent accesses. Pointer p may refer to a, b, or a distinct variable c. The assignment through p must be retained.

```text
t = a + b;
*p = 0;
u = a + b;
```

Which conditions are each sufficient to replace the last expression a+b by t for every execution satisfying that condition? Assume arithmetic does not overflow.

A. p points to c, which is distinct from a and b.  
B. p points to a, and a was zero immediately before the store.  
C. p points to b, and a was zero immediately before the store.  
D. p points to b, and b was zero immediately before the store.

### Q55. [2 Marks] [NAT]

A lexer recognizes keywords `if`, identifiers matching `[a-z]+`, and single-character operators `<` and `=`. It uses maximal munch, breaking equal-length keyword/identifier ties in favour of the keyword. For input `ifx<if==x`, how many tokens are identifiers? There are no multi-character operators in this language.

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

A resolver caches a CNAME mapping alias.example to host.example at time 0 with TTL 120 seconds, and the target's A record at time 20 with TTL 50 seconds. At time 80 it receives a new request for alias.example. Assume no prefetching, no stale-answer service, and no other cached answers. Cache hits do not refresh TTLs. Which action and remaining TTL are correct?

A. Reuse both records; each has 40 seconds remaining.
B. Reuse the CNAME with 40 seconds remaining and obtain a fresh A record for host.example.
C. Obtain a new CNAME but reuse the A record with 40 seconds remaining.
D. Reuse both records indefinitely because their names have not changed.

### Q57. [2 Marks] [NAT]

Memory has four interleaved banks. Consecutive word addresses use banks 0,1,2,3 cyclically. The controller issues at most one request per cycle; a bank next accepts a request no earlier than six cycles after its previous request. Eight consecutive word reads starting at address zero are issued in order as early as possible. All banks are initially idle and the first request issues at cycle 0. At which cycle does the eighth request issue?

**Answer format:** Integer.

### Q58. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Grammar S→aS | aSbS | ε uses terminals a,b. Which statements are correct?

A. Every generated string has at least as many a's as b's.  
B. Every prefix of every generated string has at least as many a's as b's.  
C. The grammar generates ba.  
D. The grammar generates aab.

### Q59. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Starting with three empty page frames, process the reference string 1,2,3,1,4,2,5. Which statements are correct?

A. FIFO incurs five page faults.  
B. LRU incurs six page faults.  
C. This example proves FIFO never faults more often than LRU on any reference string.  
D. Increasing the frame count cannot increase LRU's faults for a fixed reference string starting empty.

### Q60. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider these C declarations inside a function. No operation shown overflows.

```c
int a[3] = {2,4,6};
int *p = a + 3;
```

Which subsequent expressions have defined behavior?

A. p - a  
B. *(p - 1)  
C. *p  
D. p == a + 3

### Q61. [2 Marks] [MSQ]

A proposed PDA for L={a^n b^n : n≥0} pushes for every a and pops for every b, rejects an attempted pop from empty, and accepts at end exactly when the stack is empty. It has no state recording whether b's have begun, so it allows pushing after popping. Which statements are correct?

A. It accepts abab, which is outside L.
B. Adding a phase distinction that forbids a after the first b can repair the order constraint.
C. Its empty-stack condition alone guarantees all a's precede all b's.
D. It rejects aabb.

### Q62. [2 Marks] [NAT]

A six-bit register represents six valid one-hot states. A recovery circuit maps a word containing at least one 1 to the one-hot word retaining only its highest-index 1 (indices 0 through 5). It maps the all-zero word to the state with bit 0 set. Each of the 64 possible input words is equally likely. What is the probability that the recovered state has index at least 4?

**Answer format:** Exact finite decimal.

### Q63. [2 Marks] [NAT]

A file uses a linked allocation scheme with 512-byte disk blocks, of which four bytes in every block store the next-block pointer. How many blocks are required to store 2033 data bytes? No extra file header is stored inside these blocks.

**Answer format:** Integer.

### Q64. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be context-free and R regular over the same alphabet. Which languages are guaranteed context-free?

A. L∩R  
B. L minus R  
C. R minus L  
D. L∪R

### Q65. [2 Marks] [NAT]

A synchronous circuit has two D flip-flops with state(a,b), initialized to(0,1). Its next state is(a XOR b,a), using old values simultaneously. An output pulse occurs on an edge exactly when the old state is(1,0). How many output pulses occur during the first eight clock edges?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 090

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 32 |
| 3 | NAT | 1 | 9 |
| 4 | NAT | 1 | 2 |
| 5 | NAT | 1 | 68 |
| 6 | NAT | 2 | 8 |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 9 |
| 9 | MSQ | 2 | B, D |
| 10 | MSQ | 2 | A, C, D |
| 11 | NAT | 1 | 1.2 |
| 12 | NAT | 1 | 2 |
| 13 | MSQ | 1 | A, C |
| 14 | NAT | 1 | 1.160 (range 1.1595–1.1605) |
| 15 | NAT | 1 | 16 |
| 16 | NAT | 1 | 0.21875 (five decimals) |
| 17 | MCQ | 1 | C |
| 18 | NAT | 1 | 1 |
| 19 | MSQ | 1 | A, C, D |
| 20 | NAT | 1 | 2 |
| 21 | MSQ | 1 | A, B, D |
| 22 | NAT | 1 | 2 |
| 23 | MCQ | 1 | A |
| 24 | NAT | 1 | 13 |
| 25 | NAT | 1 | 4 |
| 26 | MSQ | 1 | A, B, D |
| 27 | NAT | 1 | 18 |
| 28 | NAT | 1 | 3 |
| 29 | NAT | 1 | 42 |
| 30 | MCQ | 1 | A |
| 31 | NAT | 1 | 6.8 |
| 32 | NAT | 1 | 6 (exact) |
| 33 | NAT | 1 | 0 |
| 34 | NAT | 1 | 13 |
| 35 | NAT | 1 | 1200 |
| 36 | NAT | 2 | 128 |
| 37 | NAT | 2 | 2 |
| 38 | NAT | 2 | 0.5385 (range 0.53845–0.53855) |
| 39 | NAT | 2 | 6 |
| 40 | MCQ | 2 | B |
| 41 | NAT | 2 | 3 |
| 42 | NAT | 2 | 22 |
| 43 | MSQ | 2 | B, C, D |
| 44 | NAT | 2 | 15 |
| 45 | NAT | 2 | 1.25 |
| 46 | NAT | 2 | 32 |
| 47 | NAT | 2 | 6 |
| 48 | NAT | 2 | 3 |
| 49 | NAT | 2 | 3 |
| 50 | NAT | 2 | 2 |
| 51 | NAT | 2 | 1 |
| 52 | NAT | 2 | 1 |
| 53 | NAT | 2 | 512 |
| 54 | MCQ | 2 | C |
| 55 | NAT | 2 | 2 |
| 56 | MCQ | 2 | B |
| 57 | NAT | 2 | 9 |
| 58 | MCQ | 2 | C |
| 59 | MCQ | 2 | C |
| 60 | MCQ | 2 | C |
| 61 | MSQ | 2 | A, B |
| 62 | NAT | 2 | 0.75 |
| 63 | NAT | 2 | 5 |
| 64 | MCQ | 2 | C |
| 65 | NAT | 2 | 3 |
