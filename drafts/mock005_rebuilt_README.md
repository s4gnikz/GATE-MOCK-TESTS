# GATE CS 2027 — Full-Length Mock Test 005

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

- Attempt all 65 questions. Q1–Q5 and Q11–Q35 carry one mark each; the remaining questions carry two marks each.
- MCQ questions have exactly one correct option. An incorrect one-mark MCQ loses 1/3 mark; an incorrect two-mark MCQ loses 2/3 mark.
- MSQ questions have more than one correct option. Select all and only the correct options. There is no partial credit or negative marking.
- NAT questions have no options. Enter the requested numeric value and use the precision specified in the question. Incorrect NAT answers receive zero.
- Unattempted questions receive zero. Unless stated otherwise, arithmetic in pseudocode is exact, logarithms used in asymptotic expressions have any fixed base greater than one, and graphs are finite.
- General Aptitude carries 15 marks, Engineering Mathematics 13 marks, and core Computer Science 72 marks.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Choose the sentence in which the opening phrase clearly modifies the intended subject and the list has parallel grammatical form.

A. After examining the records, several errors were found by Mira in dates, to calculate totals, and filing.
B. After examining the records, the totals were checked by Mira and correcting dates.
C. After examining the records, Mira corrected the dates, recalculated the totals, and reorganized the files.
D. After examining the records, correcting the dates, the totals were recalculated by Mira.

### Q2. [1 Mark] [NAT]

Two inlet pipes, working alone, fill an empty tank in 6 hours and 9 hours. With both inlets and a leak open, an initially empty tank fills in 4 hours. All rates are constant. How many hours would the leak alone take to empty a full tank?

**Answer format:** Integer hours.

### Q3. [1 Mark] [MSQ]

Exactly one of three boxes A,B,C contains a prize. Their labels say, respectively, “The prize is in B,” “The prize is in C,” and “The prize is not in C.” Exactly one label is true. Which statements follow?

A. The prize may be in A.
B. The prize must be in C.
C. The prize cannot be in B.
D. The label on A must be true.

### Q4. [1 Mark] [MCQ]

An arrow initially points in the positive x direction in a coordinate plane. First reflect the entire plane in the line y=x. Then rotate it clockwise by 90 degrees about the origin. Finally reflect it in the y-axis. In which direction does the arrow point?

A. Positive x
B. Negative x
C. Positive y
D. Negative y

### Q5. [1 Mark] [MCQ]

A report states: “Every approved application was received before the deadline. Several applications received before the deadline were rejected.” Which inference is justified?

A. Receiving an application before the deadline guarantees approval.
B. Every rejected application arrived after the deadline.
C. No application was approved.
D. Timely receipt was necessary but not sufficient for approval in this set of applications.

### Q6. [2 Marks] [NAT]

A shop buys equal numbers of two items at Rs. 60 and Rs. 100 per item. It sells every cheaper item at a 25% profit and every costlier item at a 10% loss, with no other costs. What is the overall profit percentage? Round to three decimal places.

**Answer format:** Percentage to 3 decimal places.

### Q7. [2 Marks] [MCQ]

In a group of 20 workers the mean daily output is 30 units. After removing the five workers with the lowest outputs, the mean of the remaining workers is 34. A second group of five workers, each producing 28 units, joins those remaining workers. What is the difference between the new 20-worker mean and the mean of the five removed workers?

A. 12.5 units
B. 14.5 units
C. 16 units
D. 18 units

### Q8. [2 Marks] [NAT]

A shortest lattice path from (0,0) to (4,3) uses only unit steps right or up. It must visit (1,1) and must not visit (3,2). How many such paths exist?

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

Five presentations P,Q,R,S,T occupy five consecutive slots, one per slot. Q occurs immediately after P. R occurs before P, and S occurs after Q. How many schedules satisfy these restrictions?

A. 2
B. 4
C. 6
D. 8

### Q10. [2 Marks] [NAT]

A bag contains two red and two blue balls. Balls are drawn uniformly without replacement until the first red ball is drawn, and then drawing stops. What is the expected number of balls left in the bag? Round to three decimal places.

**Answer format:** Number to 3 decimal places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Over {0,1}, let L be denoted by the regular expression (0|11)*. Which statements are correct?

A. Every maximal contiguous run of 1s in a string in L has even length.
B. Every binary string with an even total number of 1s belongs to L.
C. 110011 belongs to L.
D. 101 belongs to L.

### Q12. [1 Mark] [MCQ]

Records initially occur as (a,2),(b,1),(a,1),(b,2), where the first component is a letter key and the second a numeric key. First stably sort by the letter in ascending order, and then stably sort by the number in ascending order. What is the final sequence?

A. (a,1),(a,2),(b,1),(b,2)
B. (b,1),(a,1),(a,2),(b,2)
C. (a,1),(b,1),(a,2),(b,2)
D. (b,1),(a,1),(b,2),(a,2)

### Q13. [1 Mark] [NAT]

A lexically scoped language permits variable shadowing. In the code below, each declaration introduces a distinct variable and declarations take effect immediately. How many distinct declared variables are referenced by the three print expressions, collectively?

```text
var x;
var y;
{
    var x;
    print(x);
    {
        var y;
        print(x + y);
    }
    print(y);
}
```

**Answer format:** Integer.

### Q14. [1 Mark] [MCQ]

Equivalence relations R and S on {1,2,3,4,5,6} have partitions {{1,2},{3,4},{5,6}} and {{1},{2,3},{4,5},{6}}, respectively. Let T be the smallest equivalence relation containing R∪S. How many ordered pairs are in R∩S and T, respectively?

A. 6 and 36
B. 0 and 30
C. 12 and 36
D. 6 and 18

### Q15. [1 Mark] [NAT]

A processor uses byte addressing and little-endian 32-bit words. Bytes at addresses 100 through 103 are hexadecimal 12,34,56,78. It loads the 32-bit word at 100, shifts that unsigned value right by 16 bits, and stores the low 16 bits at addresses 102–103 in little-endian order. What decimal value is then in byte 102?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

Let A be the real matrix with rows (0,−1),(1,0), and I the 2×2 identity. What is det(I+A+A²)?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

Two balls are drawn without replacement from a bag containing two red and two blue balls. Let X and Y be the indicators that the first and second drawn balls, respectively, are red. Find Cov(X,Y), rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q18. [1 Mark] [NAT]

A checksum scheme adds 16-bit unsigned words using one's-complement addition: every carry beyond bit 15 is added back to the low 16 bits. The checksum is the bitwise complement of the final 16-bit sum. For the two words hexadecimal FFFF and 0001, what is the checksum's decimal value?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A process with three private writable pages forks using copy-on-write. Initially all three physical pages are shared between parent and child. The parent writes page 0, the child writes page 1, and the parent writes page 0 again. Neither process exits. A first write to a shared page makes one physical copy; a write to an exclusively owned page makes none. How many physical pages now hold these processes' three logical pages each?

**Answer format:** Integer.

### Q20. [1 Mark] [MCQ]

For one program, processor P executes N instructions at CPI=1.5 and 3 GHz. Processor Q executes 0.8N instructions at CPI=2 and 4 GHz. Ignore all other delays. What is Q's speedup over P?

A. 0.8
B. 1.0
C. 1.25
D. 1.5

### Q21. [1 Mark] [NAT]

An IPv4 address set consists exactly of 192.0.2.32 through 192.0.2.95 inclusive. What is the smallest number of CIDR blocks whose union is exactly this set, with no extra addresses?

**Answer format:** Integer.

### Q22. [1 Mark] [MSQ]

Under SQL's usual three-valued logic, table T(x) contains rows 1,2,NULL, and table U(y) contains rows 2,NULL. Which statements are correct?

A. `SELECT x FROM T WHERE x NOT IN (SELECT y FROM U)` returns no rows.
B. `SELECT x FROM T WHERE NOT EXISTS (SELECT 1 FROM U WHERE U.y=T.x)` returns the rows 1 and NULL.
C. Removing NULL from U makes the NOT IN query return both 1 and NULL.
D. Replacing NOT IN with IN in the first query returns three rows.

### Q23. [1 Mark] [MSQ]

Two threads acquire initially free nonrecursive mutexes A and B. Thread P acquires A then B; thread Q acquires B then A. Each releases both only after acquiring both. Which statements are correct?

A. A deadlock is possible.
B. Every interleaving deadlocks.
C. Changing Q to acquire A then B eliminates deadlock in this two-thread, two-mutex program.
D. Releasing a mutex immediately after acquiring it preserves the original protection of a critical section that requires both mutexes together.

### Q24. [1 Mark] [MCQ]

An eight-bit two's-complement negation computes the low eight bits of NOT x plus 1. For which input is the signed result equal to the signed input even though the mathematical negation is not representable?

A. 00000000
B. 01111111
C. 11111111
D. 10000000

### Q25. [1 Mark] [MSQ]

For relation R(A,B,C), the functional dependencies are exactly those implied by AB→C and C→A. Which attribute sets are candidate keys?

A. AB
B. AC
C. BC
D. C

### Q26. [1 Mark] [MCQ]

What does this conforming C program print? Array indices are valid and all arithmetic is representable.

```c
#include <stdio.h>
void f(int a[], int n) {
    int *p = a;
    a = a + 1;
    a[n-2] = p[0] + a[0];
}
int main(void) {
    int x[] = {4,7,9};
    f(x,3);
    printf("%d %d\n", x[0],x[2]);
    return 0;
}
```

A. 7 11
B. 4 11
C. 4 9
D. 11 9

### Q27. [1 Mark] [NAT]

What is the smallest size of a nonempty finite domain D on which a binary relation R can make `∀x∃y R(x,y)` true but `∃y∀x R(x,y)` false? Both quantifiers range over D.

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

For f(x)=ln x on [1,e], the mean value theorem gives a point c in (1,e) satisfying f′(c)=(f(e)−f(1))/(e−1). What is c, rounded to three decimal places?

**Answer format:** Number to 3 decimal places.

### Q29. [1 Mark] [NAT]

A singly linked structure has successor sequence 0→1→2→3→4→5→3→4→5→… . Floyd's algorithm starts both pointers at node 0. In each iteration the slow pointer advances once and the fast pointer advances twice, then equality is tested. At which node do they first meet?

**Answer format:** Integer node label.

### Q30. [1 Mark] [MCQ]

For the grammar S→aSb | bSa | ε, which description is exact?

A. All strings with equally many a and b symbols.
B. All even-length palindromes over {a,b}.
C. All strings whose second half is the symbolwise complement of the reverse of the first half.
D. All strings of the form aⁿbⁿ only.

### Q31. [1 Mark] [NAT]

A combinational block has three-bit input x and three-bit output y. It computes y=x+1 modulo 8. How many of the eight input values cause all three output bits to differ from the corresponding input bits?

**Answer format:** Integer.

### Q32. [1 Mark] [MCQ]

An undirected connected graph has distinct edge weights except that two edges share a weight. Which assertion is necessarily true?

A. It has at least two minimum spanning trees.
B. Every maximum-weight edge is absent from every minimum spanning tree.
C. Any edge that is uniquely lightest across some cut belongs to every minimum spanning tree.
D. Kruskal's algorithm fails unless all weights are distinct.

### Q33. [1 Mark] [NAT]

A recursive DNS resolver caches a record with TTL 120 seconds at time 0. A cache hit does not reset its expiry. A client requests it at times 50,119,121 and 200 seconds. Refreshes are instantaneous and reset the cached TTL to 120. How many upstream fetches occur because of these four requests, excluding the initial fetch at time 0?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

Let U be an undecidable but recognizable language. Which statements are correct?

A. U's complement cannot also be recognizable.
B. U must be infinite.
C. Every subset of U is recognizable.
D. U cannot contain any decidable infinite subset.

### Q35. [1 Mark] [MCQ]

An LL(1) parser is built for S→A b, A→a A | ε. The stack top is A and lookahead is b. Which action is correct?

A. Consume b and retain A on the stack.
B. Apply A→ε without consuming input.
C. Apply A→aA.
D. Report an error because b is not in FIRST(aA).

### Q36. [2 Marks] [NAT]

A syntax-directed definition evaluates a binary numeral by left-recursive production B→B₁ digit, with B.val=2×B₁.val+digit.val. A leaf digit has its numeric value. To support a binary point, production N→B . F uses N.val=B.val+F.val, and F→digit F₁ uses F.val=(digit.val+F₁.val)/2, with F→ε assigned 0. What value is assigned to `101.011`? Enter the exact decimal value.

**Answer format:** Exact finite decimal.

### Q37. [2 Marks] [MSQ]

Consider exact integers, pure arithmetic, and an arbitrary input n. A compiler proposes moving the division in this loop to just before the loop:

```text
i = 0
while i < n:
    t = 100 / n
    use(t)
    i = i + 1
```

Integer division truncates toward zero; division by zero traps. `use` does not modify n. Which statements are correct?

A. The expression 100/n is loop invariant.
B. Unconditionally hoisting it is semantics-preserving for every integer n.
C. Hoisting it inside a preceding `if n > 0` guard preserves division behaviour and use results.
D. Invariance alone is insufficient to justify evaluating the expression on a path where the original did not evaluate it.

### Q38. [2 Marks] [NAT]

Five distinguishable bins each hold at most two identical tokens. In how many ways can exactly five tokens be distributed among the bins?

**Answer format:** Integer.

### Q39. [2 Marks] [MCQ]

A table has rows (department,salary): (A,10),(A,10),(A,20),(B,20),(B,NULL). Consider:

```sql
SELECT department
FROM T
GROUP BY department
HAVING COUNT(DISTINCT salary) = 2
   AND SUM(salary) > 30;
```

Which result is returned under standard SQL aggregate rules?

A. No rows
B. A only
C. B only
D. A and B

### Q40. [2 Marks] [NAT]

A sender uses selective-repeat ARQ with 3-bit sequence numbers and sender and receiver windows both of size 4. The receiver initially expects sequence numbers 0–3. It receives 0,2,3,1 in that order, with no corruption or loss. After each arrival it delivers all newly available contiguous packets in order and slides its window. What is the lower edge of its receive window after all four arrivals?

**Answer format:** Integer sequence number.

### Q41. [2 Marks] [MSQ]

A real 3×3 matrix A satisfies A³=0 and A²≠0. Which statements must hold?

A. rank(A)=2.
B. rank(A²)=1.
C. A has an eigenvalue equal to 1.
D. (I−A)⁻¹=I+A+A².

### Q42. [2 Marks] [MCQ]

A complete binary tree is stored in an array with root index 1 and children 2i,2i+1. It has 100 nodes. What is the number of nodes in the subtree rooted at index 6, including that root?

A. 15
B. 20
C. 21
D. 31

### Q43. [2 Marks] [MSQ]

Consider a CFG with start S and productions S→AB | C, A→aA | a, B→bB, C→cC | ε, D→d. A useful nonterminal must occur in some derivation from S that ends in a terminal string. Which statements are correct?

A. The generated language is c*.
B. A is useful because it is reachable from S and generates terminal strings.
C. Exactly two nonterminals are useful.
D. D is useful because it generates d.

### Q44. [2 Marks] [NAT]

Four jobs have processing times and deadlines (p,d): A=(2,4), B=(3,6), C=(1,3), D=(2,7). All are available at time 0 on one nonpreemptive machine. There are no idle times or setup costs. Lateness is completion time minus deadline, and maximum lateness is the largest lateness among jobs. What is the minimum achievable maximum lateness?

**Answer format:** Integer time units.

### Q45. [2 Marks] [MCQ]

A TCP connection has congestion window 10,000 bytes and advertised receive window 7,000 bytes. Its oldest unacknowledged sequence number is 20,000 and the next unsent byte has sequence number 25,000. There is no wraparound. An ACK arrives with acknowledgment number 23,000 and advertised receive window 4,000; assume the congestion window remains unchanged and no data are sent before processing it. How many additional data bytes may be sent immediately?

A. 1,000
B. 2,000
C. 4,000
D. 5,000

### Q46. [2 Marks] [NAT]

A cache has 64-byte lines and is initially empty. A packed row-major 16×16 array of four-byte elements begins on a line boundary. A loop reads every element exactly once in column-major order (all rows of column 0, then all rows of column 1, and so on). The cache is fully associative with eight lines and LRU replacement; no other memory accesses occur. How many cache misses occur?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

A machine has a 1 ns clock, ideal CPI=1, and no overlapping stalls. Conditional branches are 20% of instructions. A static predictor predicts not taken; 60% of branches are taken, and each misprediction costs three additional cycles. A new predictor mispredicts 10% of all branches but requires a 1.1 ns clock; all other CPI contributions stay unchanged. Approximately what is the new processor's speedup over the old one on the same instruction stream?

A. 0.857
B. 1.166
C. 1.283
D. 1.360

### Q48. [2 Marks] [NAT]

A recursive procedure on a list segment performs a postorder traversal: it first visits the left half, then the right half, then emits one marker. A segment of size 1 emits a marker and returns. For a segment of size n>1, the halves have sizes floor(n/2) and ceil(n/2). Starting with n=13, how many markers have been emitted immediately before the root invocation emits its marker?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

X and Y are independent uniform random variables on [0,1]. Find E[min(X,Y) | X+Y>1]. Enter the exact decimal value.

**Answer format:** Exact finite decimal.

### Q50. [2 Marks] [MCQ]

Let L={aⁱbʲcᵏ : i,j,k≥0 and i=j or j=k}. Which statement is correct?

A. L is not context-free because it contains aⁿbⁿcⁿ.
B. L is regular because the condition uses “or.”
C. L is context-free, but its intersection with {aⁿbⁿcⁿ:n≥0} is not context-free.
D. L is finite.

### Q51. [2 Marks] [NAT]

For matrix-chain multiplication, four matrices have dimensions 5×10,10×3,3×12,12×5. Count scalar multiplications in the usual way: multiplying p×q by q×r costs pqr. What is the minimum scalar-multiplication cost for their product?

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

Use set semantics. R(A,B) contains (1,x),(2,x), and S(B,C) contains (x,p),(x,q). The natural join J=R⋈S is formed. Which statements are correct?

A. J has four tuples.
B. A→C holds in J.
C. Projecting J onto (A,B) recovers R exactly.
D. B is a candidate key of J.

### Q53. [2 Marks] [NAT]

Evaluate a binary expression tree using two rules: evaluate both children recursively, retain the first child's result while evaluating the second, then combine the results in one register and release the other. Leaves require one register. Child evaluation order may be chosen independently at each node, and no spilling or recomputation is allowed. The expression is `(a+b)*((c+d)+(e+f))`, with all leaves distinct. What is the minimum number of registers needed?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

Let L be recognized by a Turing machine that may loop on nonmembers. A second machine enumerates all strings, simulates the recognizer on them by dovetailing, and prints a string when its simulation accepts. Which statements are correct?

A. Every member of L is eventually printed.
B. The enumerator must halt when L is finite.
C. If L is empty, the enumerator may run forever without printing anything.
D. Waiting for a fixed input to appear in this enumeration decides membership in L for every recognizable L.

### Q55. [2 Marks] [MCQ]

Three processes each need at most three instances of a single resource type. Instances are identical, acquisitions are one at a time, and a process releases all its instances only when it has obtained its full requirement and completes. What is the smallest total number of instances that guarantees no resource deadlock for every allocation reachable under these rules, assuming runnable processes eventually run?

A. 6
B. 7
C. 8
D. 9

### Q56. [2 Marks] [NAT]

A synchronous three-bit shift register has next-state equations q2′=q1, q1′=q0, q0′=q2 XOR q0. Starting in state q2q1q0=001, after how many clock edges does it first return to 001?

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

In a binary tree with distinct keys, each node has a parent pointer. Given a pointer to x, an algorithm finds the next node in preorder traversal: if x has a left child, return it; otherwise, if x has a right child, return it; otherwise ascend. During ascent, when the current node is a left child and its parent has a right child, return that right child; if the root is passed, return NULL. What is the total time for starting at the root and repeatedly applying this algorithm until NULL, for a tree of n nodes?

A. Θ(log n) for every tree
B. Θ(n)
C. Θ(n log n) for every tree
D. Θ(n²) for a path-shaped tree

### Q58. [2 Marks] [NAT]

A processor services a device by polling every 50 microseconds. Each poll costs 2 microseconds of CPU time whether or not data are ready. Alternatively, interrupts occur at an average rate of 4,000 per second, each costing 8 microseconds of CPU time including service. Ignore other costs and overlap. What percentage of one second of CPU time is saved by using interrupts instead of polling? Enter the difference in percentage points.

**Answer format:** Number to 1 decimal place.

### Q59. [2 Marks] [MSQ]

A binary floating-point format has four significant bits including the leading 1, unbounded exponents, and round-to-nearest, ties-to-even after each operation. Let a=16, b=1, c=−16, all exactly representable. Which statements are correct?

A. The computed value of (a+b)+c is 0.
B. The computed value of a+(b+c) is 1.
C. Both parenthesizations must agree because no overflow occurs.
D. The exact real-arithmetic value of a+b+c is 1.

### Q60. [2 Marks] [MSQ]

Two processes share a bounded queue initially empty, a mutex M initially 1, a counting semaphore E initially equal to the positive capacity, and a counting semaphore F initially 0. A proposed consumer performs `wait(M); wait(F); remove; signal(E); signal(M)`. A producer performs `wait(E); wait(M); insert; signal(M); signal(F)`. Semaphore operations are atomic. Which statements are correct?

A. If the consumer acquires M first, the system can deadlock.
B. Moving the consumer's wait(F) before wait(M) removes this specific empty-buffer deadlock.
C. Increasing the initial value of E while keeping F=0 always prevents the deadlock.
D. The proposed consumer may hold M while waiting for an item that the producer needs M to insert.

### Q61. [2 Marks] [NAT]

A real function f is twice continuously differentiable on [0,2], satisfies f(0)=f(2)=0, and has f″(x)≥2 for all x in [0,2]. What is the greatest possible value of f(1)?

**Answer format:** Integer.

### Q62. [2 Marks] [MCQ]

An HTTP client sends a conditional GET containing `If-None-Match: "v7"` for a cached representation. The server's current representation has the same entity tag and is otherwise eligible for the conditional request. Compare a 304 response with a 200 response carrying the entire unchanged representation. Which statement is correct?

A. A 304 necessarily eliminates the request-response round trip.
B. A 304 supplies a new full representation body that must replace the cached body.
C. A 304 can save representation-body transfer while still requiring a network round trip.
D. A 304 proves that all caches on the Internet contain the same body.

### Q63. [2 Marks] [NAT]

An eight-input Boolean function is the parity of all eight inputs. Only two-input XOR gates are available. Every gate has unit delay and unlimited fanout; wire delay is zero. Among circuits with the minimum possible number of XOR gates, what is the minimum worst-case input-to-output delay?

**Answer format:** Integer gate delays.

### Q64. [2 Marks] [MCQ]

Consider the schedule `w1(x), w2(x), w1(x), w2(y), r3(y), w3(z)`, followed by commits of all three transactions. The subscripts identify transactions; writes are blind writes of distinct values. There are no other reads or writes. For view equivalence, preserve every read-from relationship and the identity of the final writer of each item. Which pair correctly states whether the schedule is conflict serializable and the number of serial transaction orders view equivalent to it?

A. Not conflict serializable; 2 orders
B. Conflict serializable; 2 orders
C. Not conflict serializable; 0 orders
D. Conflict serializable; 1 order

### Q65. [2 Marks] [NAT]

A two-level page table uses 4 KiB pages and four-byte page-table entries. Each leaf page table occupies one page and describes 4 MiB of virtual space. The root occupies one page. A process maps exactly virtual pages 0,1023,1024,2048,3071; all other pages are unmapped. Leaf tables are allocated only where needed; data pages are not counted. What is the total memory in KiB occupied by its root and leaf page tables?

**Answer format:** Integer KiB.

---

## ANSWER KEY — MOCK TEST 005

For NAT questions, integer and exact-decimal entries are exact. Rounded entries are accepted at the displayed precision; the explicitly stated ranges below allow half a unit in the last displayed place.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 36 |
| 3 | MSQ | 1 | A, C |
| 4 | MCQ | 1 | B |
| 5 | MCQ | 1 | D |
| 6 | NAT | 2 | 3.125 (range 3.1245–3.1255) |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 8 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 2.333 (range 2.3325–2.3335) |
| 11 | MSQ | 1 | A, C |
| 12 | MCQ | 1 | C |
| 13 | NAT | 1 | 3 |
| 14 | MCQ | 1 | A |
| 15 | NAT | 1 | 86 |
| 16 | NAT | 1 | 1 |
| 17 | NAT | 1 | -0.0833 (range -0.08335–-0.08325) |
| 18 | NAT | 1 | 65534 |
| 19 | NAT | 1 | 5 |
| 20 | MCQ | 1 | C |
| 21 | NAT | 1 | 2 |
| 22 | MSQ | 1 | A, B |
| 23 | MSQ | 1 | A, C |
| 24 | MCQ | 1 | D |
| 25 | MSQ | 1 | A, C |
| 26 | MCQ | 1 | B |
| 27 | NAT | 1 | 2 |
| 28 | NAT | 1 | 1.718 (range 1.7175–1.7185) |
| 29 | NAT | 1 | 3 |
| 30 | MCQ | 1 | C |
| 31 | NAT | 1 | 2 |
| 32 | MCQ | 1 | C |
| 33 | NAT | 1 | 1 |
| 34 | MSQ | 1 | A, B |
| 35 | MCQ | 1 | B |
| 36 | NAT | 2 | 5.375 |
| 37 | MSQ | 2 | A, C, D |
| 38 | NAT | 2 | 51 |
| 39 | MCQ | 2 | B |
| 40 | NAT | 2 | 4 |
| 41 | MSQ | 2 | A, B, D |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 2 | A, C |
| 44 | NAT | 2 | 1 |
| 45 | MCQ | 2 | B |
| 46 | NAT | 2 | 256 |
| 47 | MCQ | 2 | B |
| 48 | NAT | 2 | 24 |
| 49 | NAT | 2 | 0.5 |
| 50 | MCQ | 2 | C |
| 51 | NAT | 2 | 405 |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 3 |
| 54 | MSQ | 2 | A, C |
| 55 | MCQ | 2 | B |
| 56 | NAT | 2 | 7 |
| 57 | MCQ | 2 | B |
| 58 | NAT | 2 | 0.8 |
| 59 | MSQ | 2 | A, B, D |
| 60 | MSQ | 2 | A, B, D |
| 61 | NAT | 2 | -1 |
| 62 | MCQ | 2 | C |
| 63 | NAT | 2 | 3 |
| 64 | MCQ | 2 | A |
| 65 | NAT | 2 | 16 |
