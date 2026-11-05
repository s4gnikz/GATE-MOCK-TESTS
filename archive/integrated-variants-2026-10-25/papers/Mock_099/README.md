# GATE CS 2027 — Full-Length Mock Test 099

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

“Complaints about bus delays fell after an online complaint form was introduced. During the same period, submitting a complaint began to require an account, and the number of completed complaint submissions fell. No independent measurements of bus arrival times were collected.” Which conclusion is best supported?

A. Buses necessarily became more punctual.
B. Every person who stopped submitting complaints encountered punctual buses.
C. The complaint count alone cannot distinguish improved punctuality from reduced reporting.
D. Requiring an account necessarily made buses less punctual.

### Q2. [1 Mark] [NAT]

How many four-digit positive integers use each of the digits 0,1,2,3 exactly once and are divisible by four? A leading zero is not permitted.

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

Among25 recorded journey times,7 are at most10 minutes,19 are at most20 minutes, and all25 are at most30 minutes. A journey is selected uniformly from those lasting more than10 minutes. What is the probability that it lasted at most20 minutes?

**Answer format:** Decimal rounded to four places.

### Q4. [1 Mark] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left across x=4 and then the top half down across y=4. A point-sized hole is punched at(4,2), on one fold line but not the other. How many distinct point holes appear after unfolding? Ignore the hole's radius and count distinct coordinates only.

**Answer format:** Integer.

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

A three-question quiz has four options per question and exactly one correct option each. A student independently guesses uniformly on every question. Each correct answer scores 3 and each wrong answer scores −1. Given that the student's total score is positive, what is the probability that exactly two answers were correct? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q7. [2 Marks] [MCQ]

“The report is concise but not cursory: it omits repetition while addressing every required issue.” What distinction is emphasized?

A. Brevity need not imply superficial treatment.
B. Concise reports necessarily omit required issues.
C. Cursory reports must be longer than complete reports.
D. Repetition is necessary for completeness.

### Q8. [2 Marks] [NAT]

A candidate answers 40 one-mark MCQs. Of these, 30 are correct and 10 incorrect; each incorrect answer loses 1/3 mark. The candidate also answers 20 two-mark MCQs. What is the minimum number of correct answers among those 20 needed for a total score of at least 50? Every remaining answer among the 20 is incorrect and loses 2/3 mark.

**Answer format:** Integer.

### Q9. [2 Marks] [MSQ]

For real numbers a,b, define a⋆b=2a+b. Which identities or implications hold for all real a,b,c?

A. (a⋆b)⋆c=a⋆(b⋆c)
B. a⋆b=b⋆a
C. If a⋆b=a⋆c, then b=c.
D. a⋆(b+c)=(a⋆b)+c

### Q10. [2 Marks] [NAT]

A 4×4 grid of unit squares is coloured like a chessboard, with adjacent squares having opposite colours. How many axis-aligned 2×2 subgrids contain exactly two squares of each colour?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A recursive algorithm on an input of size16 calls itself on sizes n/2 and n/4 whenever n≥4, and stops immediately for n<4. How many leaf calls occur?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

Over alphabet{a,b}, let R=a*b* and L={a^n b^n:n≥0}. Which statements are correct?

A. L is a subset of R.
B. Every subset of a regular language is regular.
C. R is regular but L is not.
D. The inclusion L⊆R proves that L is finite.

### Q13. [1 Mark] [NAT]

An IPv4 fragment arrives with total length 1020 bytes, header length 20 bytes, fragment offset 100, and MF=1. A router forwards it through an interface with MTU 620 bytes and fragments it into the minimum number of fragments, using the largest permitted payload in the first new fragment. Every outgoing header is 20 bytes. What is the fragment-offset field of the second outgoing fragment?

**Answer format:** Numeric value; integer.

### Q14. [1 Mark] [NAT]

An undirected graph has vertices 1–5 and edges {1,2},{2,3},{3,4},{4,2},{1,5}. How many articulation vertices does it have? Removing an articulation vertex and its incident edges increases the number of connected components.

**Answer format:** Integer.

### Q15. [1 Mark] [MSQ]

For relation R(A,B,C), the functional dependencies are exactly those implied by AB→C and C→A. Which attribute sets are candidate keys?

A. AB
B. AC
C. BC
D. C

### Q16. [1 Mark] [MSQ]

The following code operates on ordinary integer variables; assignment copies a value and does not create an alias.

```text
x = 4
y = x
x = 9
z = y + x
```

Which statements are correct?

A. z is13.
B. y is9 at the end.
C. The value assigned by the first line contributes to z.
D. Changing x on line3 also changes y.

### Q17. [1 Mark] [NAT]

A synchronous three-bit state register is interpreted as an unsigned integer q. At every clock edge, q becomes0 if q≥5, and otherwise becomes q+1. Starting with q=7 before the first edge, what is q after14 edges?

**Answer format:** Integer.

### Q18. [1 Mark] [MCQ]

Which grammar is the direct left-factored equivalent of S→ab | ac | a, with ε denoting the empty string?

A. S→aX; X→b | c | ε
B. S→Xa; X→b | c | ε
C. S→aX; X→bX | cX | ε
D. S→a; X→b | c

### Q19. [1 Mark] [NAT]

Let f(x)=x² sin(1/x) for x≠0 and f(0)=0. What is f'(0)?

**Answer format:** Exact integer.

### Q20. [1 Mark] [NAT]

A fair coin is tossed twice. X is the number of heads, and Y is1 if the tosses differ and0 otherwise. What is Cov(X,Y)?

**Answer format:** Exact number.

### Q21. [1 Mark] [MCQ]

For the grammar S→aSb | bSa | ε, which description is exact?

A. All strings with equally many a and b symbols.
B. All even-length palindromes over {a,b}.
C. All strings whose second half is the symbolwise complement of the reverse of the first half.
D. All strings of the form aⁿbⁿ only.

### Q22. [1 Mark] [NAT]

Table T(g,v) contains (A,2),(A,NULL),(B,5),(B,7). How many groups remain after `GROUP BY g HAVING COUNT(v)=2`?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A direct-mapped cache has four lines, one word per line, with block number b mapped to line b modulo4. Initially empty, it receives word-block references0,1,4,1,0,1. How many hits occur?

**Answer format:** Integer.

### Q24. [1 Mark] [MSQ]

A transmitted binary word contains data bits followed by one even-parity bit. The receiver checks only whether the parity of the whole received word is even. Which errors are always detected?

A. Exactly one data bit flips.
B. Exactly two data bits flip.
C. Exactly one data bit and the parity bit flip.
D. Exactly three distinct bits of the word flip.

### Q25. [1 Mark] [NAT]

An inode has a link count of3. One pathname is renamed within the same file system without replacing an existing destination, and another pathname is then unlinked. Assume no other directory changes. What is the inode's final hard-link count?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

A signed six-bit two's-complement fixed-point value has two fractional bits. What is the greatest positive real number it can represent?

**Answer format:** Exact finite decimal.

### Q27. [1 Mark] [NAT]

Let R={(1,2),(2,3),(3,1)}. Its composition R∘R contains (x,z) when some y satisfies (x,y)∈R and (y,z)∈R. How many pairs belong to R∩(R∘R)?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

A quicksort variant partitions a subarray into keys less than, equal to, and greater than its pivot, in time Θ(m) for a subarray of length m. It recurses only on the less-than and greater-than parts. What is its running time on n equal keys?

A. Θ(1)
B. Θ(log n)
C. Θ(n)
D. Θ(n²)

### Q29. [1 Mark] [NAT]

A real4×4 matrix P satisfies P²=P and trace(P)=3. What is the dimension of the null space of I−P?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

A binary min-heap stored from index 1 is [2,5,3,9,7,8]. Insert 1 by placing it at the next free index and repeatedly exchanging it with its parent while smaller. How many exchanges occur?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

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

### Q32. [1 Mark] [NAT]

A memory access normally takes 200 ns. Independently, a fraction p of accesses incur an additional 10 ms page-fault delay. Ignoring other overhead, what is the greatest p for which mean access time is at most 240 ns?

**Answer format:** Exact finite decimal.

### Q33. [1 Mark] [NAT]

For real c, let f(x)=x³−3x²+cx on [0,2]. What is the smallest c for which f is nondecreasing throughout this interval?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A peripheral produces one byte every10 microseconds. The CPU polls every25 microseconds, reading and clearing all available bytes instantly. Initially the buffer is empty and a poll occurs at time0; arrivals start at time10. What minimum buffer capacity in bytes avoids overflow indefinitely? If an arrival and poll coincide, the arrival occurs first.

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

An eight-input priority encoder returns the index of the highest-numbered asserted input, with indices 0–7. Initially inputs 3 and 5 are asserted. The selected input is cleared, and the encoder is evaluated again. What is the second output index?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

Box A is selected with probability 1/3 and box B with probability 2/3. A contains three red and two blue balls; B contains one red and four blue balls. Two balls are drawn without replacement from the selected box. Given that exactly one is red, what is the probability that the selected box was A? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q37. [2 Marks] [NAT]

A sender has transmitted bytes100 through699 inclusive. It receives a cumulative TCP ACK with acknowledgment number400 and a selective acknowledgment block[500,700). Ignoring retransmission policy, how many transmitted bytes remain neither cumulatively acknowledged nor covered by that SACK block?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

A disk head starts at track 50 moving upward at one track per ms on tracks 0–99. It uses SCAN: it continues to physical endpoint 99 before reversing, even if no pending request lies farther upward. At time zero requests exist at tracks 60 and 20. A new request for track 70 arrives at time 30 ms, after the head has passed track 70. Service takes zero time; direction does not change for the new arrival. How many ms does the new request wait from arrival to service?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

Languages A and B satisfy A≤mB: a total computable function f obeys x∈A iff f(x)∈B. Which implications necessarily hold?

A. If B is decidable, A is decidable.
B. If A is decidable, B is decidable.
C. If A is not recognizable, B is not recognizable.
D. If B is not recognizable, A is not recognizable.

### Q40. [2 Marks] [NAT]

A scalar pipeline can issue one instruction per cycle. A multiply produces its result three cycles after its issue; an add produces its result one cycle after issue. A consumer may issue in the cycle its last operand becomes available. Consider independent multiplies M1,M2 followed by add A consuming both, then add B consuming A. Issue M1 at cycle0 and schedule as early as possible, without other hazards. In what cycle does B's result become available?

**Answer format:** Integer cycle number.

### Q41. [2 Marks] [NAT]

A poset consists of pairs (i,j), where i∈{1,2} and j∈{1,2,3}, with (i,j)≤(k,l) iff i≤k and j≤l. How many downward-closed subsets does it have, including the empty set? A subset is downward-closed when containing an element implies containing every smaller element.

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Parent(a,b) has the single row (1,2), with composite primary key (a,b). Child(a,b,qty) has a composite foreign key referencing Parent with MATCH SIMPLE, and CHECK(qty>0). All Child columns allow NULL. MATCH SIMPLE skips the referential check when either foreign-key component is NULL; a CHECK rejects only FALSE, not UNKNOWN. Starting with an empty Child table, which individual insertions succeed?

A. (1,NULL,5)  
B. (NULL,9,−1)  
C. (9,9,NULL)  
D. (1,2,NULL)

### Q43. [2 Marks] [NAT]

A normalized binary floating-point format has three significant bits including the leading 1 and rounds to nearest, ties to even. Exponents cover the required range. What is the absolute rounding error when storing exact value 7.5?

**Answer format:** Exact finite decimal.

### Q44. [2 Marks] [MSQ]

In this control-flow fragment, a and b are not modified, and arithmetic has no side effects or overflow:

```text
if flag:
    t = a + b
else:
    u = a + b
v = a + b
```

Which statements are correct?

A. The expression a+b has been evaluated on every path reaching the assignment to v.
B. Replacing v=a+b with v=t is always valid even if t is undefined on the else path.
C. A compiler may compute a+b into one common temporary before the branch and use it on both paths and afterward.
D. Replacing v=a+b with v=u is always valid even if u is undefined on the then path.

### Q45. [2 Marks] [NAT]

A directed multigraph has adjacency-count matrix with rows (1,2,0), (0,0,3), (1,0,0). Entries count distinct parallel edges, and walks distinguish different edge choices. How many length-three walks start and end at vertex 1?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

For resource types A,B, three processes have allocations P:(0,1), Q:(1,0), R:(1,1) and remaining maximum needs P:(1,0), Q:(0,2), R:(1,1). Available resources are initially (0,0). Apply the standard safety test: a process whose remaining need is available may finish and release its allocation. Which statements are true?

A. The initial state is unsafe.
B. Adding one available unit of B makes the state safe.
C. Adding one available unit of A makes the state safe.
D. An unsafe maximum-claim state alone proves that the processes are already deadlocked on actual requests.

### Q47. [2 Marks] [NAT]

A circuit-switched transfer has setup time1ms and then sends L payload bits at2 Mbit/s with no other overhead. A packet-switched alternative has no setup, sends at1 Mbit/s, and adds100 header bits per packet with at most900 payload bits per packet. Packets are filled except possibly the last; ignore all other delays. What is the smallest positive integer L for which the circuit-switched transfer finishes strictly earlier?

**Answer format:** Integer bits.

### Q48. [2 Marks] [MSQ]

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

### Q49. [2 Marks] [NAT]

For a matrix A, pivoted elimination gives PA=LU, where P swaps rows1 and2,

```text
L=[1 0; 2 1],    U=[1 3; 0 2].
```

Solve Ax=b for b=(7,2)ᵀ. What is x1?

**Answer format:** Exact decimal.

### Q50. [2 Marks] [NAT]

Round-robin scheduling has quantum2, zero overhead, and a ready queue initially[A,B,C]. All arrive at0, with CPU bursts A=5,B=3,C=1. A process with remaining work joins the queue tail after its quantum. What is the mean turnaround time?

**Answer format:** Decimal rounded to four places.

### Q51. [2 Marks] [NAT]

A machine uses byte addresses. An instruction has a signed eight-bit displacement, measured in four-byte words relative to the address immediately after the instruction. The next-instruction address is 1000 and the displacement field is 11110110₂. What is the effective target byte address?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

Insertion sort on an array of distinct values shifts an earlier element right whenever it is greater than the current key. Count only these shifts, not key placements or failed comparisons. An initial array is formed by concatenating ascending blocks [4,5,6], [1,2,3], and [7,8]. How many shifts does insertion sort perform?

**Answer format:** Exact integer.

### Q53. [2 Marks] [MCQ]

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

### Q54. [2 Marks] [NAT]

Each reference first spends 1 ns searching a TLB. A TLB miss, occurring on 10% of references, adds a 200 ns page-table walk before the data-cache lookup. Every data-cache lookup takes 2 ns; a data-cache miss, occurring on 5% of references, adds 50 ns. These delays do not overlap, and there are no page faults. What is the mean reference time in ns?

**Answer format:** Exact finite decimal.

### Q55. [2 Marks] [MSQ]

A client has a fresh cached DNS address for host h and an HTTP cache entry for a resource on h. The HTTP entry is stale but has an entity tag. Which statements hold?

A. Revalidating the HTTP entry need not require a fresh DNS query.
B. A conditional request can allow the server to confirm reuse of the cached body without resending that body.
C. A valid DNS cache entry guarantees that every cached HTTP resource for h is fresh.
D. Receiving an HTTP response automatically renews the DNS record's TTL.

### Q56. [2 Marks] [MSQ]

For a DFA, states p and q are equivalent if every suffix yields the same acceptance result from both. Which statements are correct?

A. If p is accepting and q rejecting, ε distinguishes them.
B. Having the same transitions on one input symbol alone guarantees equivalence.
C. If p,q are equivalent, their successors on any given symbol are equivalent.
D. Two unreachable states must be equivalent to each other.

### Q57. [2 Marks] [NAT]

A continuous function f on[0,1] satisfies f(x)+f(1−x)=x(1−x) for all x in[0,1]. What is the integral of f from0 to1?

**Answer format:** Decimal rounded to four places.

### Q58. [2 Marks] [MSQ]

A lexer uses maximal munch, breaking equal-length ties by rule priority. Its tokens include INTEGER=[0-9]+, REAL=[0-9]+\.[0-9]*, and RANGE=\.\., where an escaped dot denotes a literal dot. A single dot is not a token. For input1..2, which statements are correct?

A. The first token under these rules is REAL with lexeme `1.`.
B. Giving RANGE highest priority makes the first token INTEGER with lexeme1.
C. After the first token, scanning encounters a dot at which no token can start.
D. Requiring at least one digit after the dot in REAL would allow the tokenization INTEGER,RANGE,INTEGER.

### Q59. [2 Marks] [NAT]

For Boolean variables x,y,z, define F=(x XOR y) AND (y XOR z). How many input triples make F=1?

**Answer format:** Exact integer.

### Q60. [2 Marks] [NAT]

The following pseudocode uses a reference to one shared integer x. Arithmetic is exact.

```text
f(n, reference x):
    if n = 0: return x
    x = x + 1
    a = f(n - 1, x)
    x = x + a
    return x
```

Initially x=1. After evaluating f(3,x), what is the final value of x?

**Answer format:** Exact integer.

### Q61. [2 Marks] [MSQ]

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

### Q62. [2 Marks] [MSQ]

R(A,B,C) has dependencies A→B and B→C. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless with respect to the dependencies.
B. The dependencies are preserved by enforcing them separately in R1 and R2.
C. R itself is in BCNF under the given dependencies.
D. Both decomposed relations are in BCNF under their projected dependencies.

### Q63. [2 Marks] [NAT]

An eight-bit unsigned multiplier retains only the low eight product bits. For a fixed odd input a=13, how many inputs b in {0,…,255} produce output 0? Count b values, not ordered pairs of inputs.

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A 2 GHz processor executes 10⁹ instructions with average CPI 1.2. A compiler transformation reduces instruction count by 20% but increases average CPI to 1.4. What is the execution-time reduction in milliseconds at the same clock frequency?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Grammar E→E+E | E*E | n allows all binary parenthesizations and specifies no precedence. Each n is a numeric literal with its usual value; + and * have ordinary integer meanings. How many distinct numerical values arise from parse trees for `1+2*3+4`?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 099

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 4 |
| 3 | NAT | 1 | 0.6667 (accepted range 0.66665–0.66675) |
| 4 | NAT | 1 | 2 |
| 5 | MCQ | 1 | A |
| 6 | NAT | 2 | 0.2432 (range 0.24315–0.24325) |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 14 |
| 9 | MSQ | 2 | C, D |
| 10 | NAT | 2 | 9 |
| 11 | NAT | 1 | 5 |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 175 (exact) |
| 14 | NAT | 1 | 2 (exact) |
| 15 | MSQ | 1 | A, C |
| 16 | MSQ | 1 | A, C |
| 17 | NAT | 1 | 1 |
| 18 | MCQ | 1 | A |
| 19 | NAT | 1 | 0 |
| 20 | NAT | 1 | 0 |
| 21 | MCQ | 1 | C |
| 22 | NAT | 1 | 1 |
| 23 | NAT | 1 | 2 |
| 24 | MSQ | 1 | A, D |
| 25 | NAT | 1 | 2 |
| 26 | NAT | 1 | 7.75 |
| 27 | NAT | 1 | 0 |
| 28 | MCQ | 1 | C |
| 29 | NAT | 1 | 3 |
| 30 | NAT | 1 | 2 |
| 31 | MSQ | 1 | B, C |
| 32 | NAT | 1 | 0.000004 |
| 33 | NAT | 1 | 3 (exact) |
| 34 | NAT | 1 | 3 |
| 35 | NAT | 1 | 3 |
| 36 | NAT | 2 | 0.4286 (range 0.42855–0.42865) |
| 37 | NAT | 2 | 100 |
| 38 | NAT | 2 | 48 |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 6 |
| 41 | NAT | 2 | 10 |
| 42 | MSQ | 2 | A, D |
| 43 | NAT | 2 | 0.5 |
| 44 | MSQ | 2 | A, C |
| 45 | NAT | 2 | 7 |
| 46 | MSQ | 2 | A, C |
| 47 | NAT | 2 | 1601 |
| 48 | MSQ | 2 | A, B |
| 49 | NAT | 2 | -2.5 |
| 50 | NAT | 2 | 7.3333 (accepted range 7.33325–7.33335) |
| 51 | NAT | 2 | 960 |
| 52 | NAT | 2 | 9 |
| 53 | MCQ | 2 | C |
| 54 | NAT | 2 | 25.5 |
| 55 | MSQ | 2 | A, B |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 0.0833 (accepted range 0.08325–0.08335) |
| 58 | MSQ | 2 | A, C, D |
| 59 | NAT | 2 | 2 |
| 60 | NAT | 2 | 32 |
| 61 | MSQ | 2 | A, C |
| 62 | MSQ | 2 | A, B, D |
| 63 | NAT | 2 | 1 |
| 64 | NAT | 2 | 40 |
| 65 | NAT | 2 | 4 |
