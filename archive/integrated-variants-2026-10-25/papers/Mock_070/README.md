# GATE CS 2027 — Full-Length Mock Test 070

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

### Q1. [1 Mark] [MSQ]

Among employees, every auditor is a reviewer, and no reviewer is an intern. At least one auditor exists. Which statements must follow?

A. At least one reviewer is not an intern.
B. Every non-intern is an auditor.
C. No auditor is an intern.
D. At least one intern exists.

### Q2. [1 Mark] [NAT]

A planar figure consists of the three labelled points A=(0,0), B=(2,0), C=(0,1). It is reflected in the line y=x and then translated by(1,−1). What is the x-coordinate of the image of C minus the y-coordinate of the image of B?

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

“A train service reduced the average delay but increased the maximum delay.” Which statement follows from these two statistics alone?

A. Every passenger experienced a shorter delay.
B. At least one statistic improved while the worst observed delay became larger.
C. The statistics are mathematically inconsistent.
D. The median delay necessarily increased.

### Q4. [1 Mark] [NAT]

Four distinct people sit around a circular table. Rotations are considered identical, but reflections are different. Two specified people must sit opposite each other. How many seating arrangements are possible?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A factory reports that20% of the items produced on Monday were rejected. On Tuesday it produced twice as many items, and10% were rejected. What percentage of the two days' rejected items came from Monday?

**Answer format:** Exact percentage, without the percent sign.

### Q6. [2 Marks] [NAT]

A rectangular paper strip extends from x=0 to x=12. It is folded at x=6 so the right half lies on the left. A cut through all layers removes the closed interval 1≤x≤2 from the folded strip, across its full width. After unfolding, how many connected pieces of paper remain? Ignore zero-width boundaries.

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

Four paragraphs describe events on the same day. P describes a noon alarm, Q a10:00 repair, R a14:00 report and S a09:00 inspection. They currently appear in order P,Q,R,S. An editor must put them in chronological order and may exchange only two adjacent paragraphs in one operation. What is the minimum number of exchanges required?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

A bag contains two red and two blue balls. Draw two without replacement. If their colors match, record 1; otherwise record 0. Repeat the entire experiment independently after restoring the bag. What is the probability that the two recorded values differ?

**Answer format:** Decimal rounded to four places.

### Q9. [2 Marks] [NAT]

Six teams play a single round-robin tournament, every pair playing once. A win earns three points and a loss zero; a draw gives each team one point. The sum of all teams' final points is 41. How many matches were drawn?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

How many distinct positive integers N≤72 can be written as N=2^a·3^b with nonnegative integers a,b and are divisible by6?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Functions F,G are defined on integers by F(n)=1 for n≤0, otherwise F(n)=1+G(n−2); and G(n)=1 for n≤0, otherwise G(n)=1+F(n−1). What is F(7)?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

An integer array initially contains [1,2,3,4,5,6]. A memmove-style operation copies its first four elements into positions 2 through 5, using zero-based positions and preserving the original source values even where source and destination overlap. What value is at position 5 afterward?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A protocol numbers frames modulo 16. The receiver currently expects 14 and accepts only the next in-order frame, discarding every other arrival. Frames arrive with sequence numbers 15,14,0,15,0,1, in that order. What sequence number does it expect at the end?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A byte-addressed machine fetches a four-byte branch instruction at address1000. Its eight-bit displacement field contains11111100. The processor sign-extends this field, multiplies it by4, and adds the result to the address immediately after the instruction. What is the target byte address?

**Answer format:** Exact integer.

### Q15. [1 Mark] [MCQ]

A language has lexical nesting. Procedure Outer defines local x and nested procedure Inner, whose body references x. Inner is called by an unrelated procedure Caller while Outer remains active. Which link is needed to find the lexically enclosing activation containing x?

A. A dynamic link to Caller alone
B. A static link to Outer's activation
C. A link to whichever activation was created most recently
D. A link to the global symbol table alone

### Q16. [1 Mark] [MSQ]

Two threads execute atomic fetch-and-add(counter,1), each exactly once, with counter initially0. Each operation returns the value before its increment. Which statements must hold after both finish?

A. The final counter is2.
B. Both operations return0.
C. The two returned values are0 and1 in some order.
D. The thread that starts first must receive0, even if it is delayed before executing its atomic operation.

### Q17. [1 Mark] [NAT]

An undirected graph is formed from a triangle on a,b,c by adding edges cd and de, with new vertices d,e. How many articulation vertices does it have?

**Answer format:** Integer.

### Q18. [1 Mark] [MSQ]

An unsigned w-bit subtraction is implemented as A+(bitwise NOT B)+1, with the final carry-out retained. Which statements are correct?

A. The low w bits equal(A−B) modulo2^w.
B. Carry-out1 indicates no unsigned borrow under this convention.
C. Carry-out1 necessarily indicates signed overflow.
D. The low result bits alone always reveal whether unsigned borrowing occurred.

### Q19. [1 Mark] [NAT]

SQL table A(k) contains1,2,NULL; B(k) contains2,NULL. Compare the counts returned by these predicates on rows of A: NOT EXISTS(SELECT 1 FROM B WHERE B.k=A.k), and A.k NOT IN(SELECT k FROM B). Using ordinary SQL three-valued logic, what is the first count minus the second?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

A depth-first search starts at vertex a in an undirected graph with edges ab,ac,bd,cd,ce. Neighbours are examined alphabetically. How many tree edges lie on the DFS-tree path from a to e?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

How many onto functions map a three-element labelled set to a two-element labelled set?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

For the grammar S→AB, A→aA | ε, B→aB | ε, how many distinct parse trees generate the terminal string aaa?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A sequence satisfies a0=0 and an=2a(n−1)+2^n for n≥1. What is a5?

**Answer format:** Integer.

### Q24. [1 Mark] [MSQ]

A table has PRIMARY KEY(id) and a foreign key parent_id referencing id in the same table. parent_id is nullable and no further constraint is specified. Which statements are correct?

A. A row may have parent_id=NULL.
B. The foreign key alone prevents cycles of length two.
C. A row whose parent_id equals its own existing id can satisfy these constraints.
D. Every non-null parent_id must reference an existing key when the constraint is checked.

### Q25. [1 Mark] [MCQ]

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

### Q26. [1 Mark] [NAT]

There are three identical reusable resources. Each of two processes may need at most two simultaneously; each holds any allocated resources until it finishes. If each currently holds one and requests one more, how many processes can finish first without preempting resources?

**Answer format:** Number of possible choices for the first finishing process.

### Q27. [1 Mark] [MSQ]

For propositions p and q, which formulas are logically equivalent to NOT(p implies q)?

A. p AND NOT q.
B. NOT p OR q.
C. p AND (p XOR q).
D. NOT p AND q.

### Q28. [1 Mark] [MCQ]

In `t=a+b; c=d+e; u=a+b;`, variables a,b,c,d,e,t,u are distinct nonaliased scalars and arithmetic is exact. Which replacement is valid?

A. Replace the final a+b by t.
B. Replace the final a+b by c for all inputs.
C. Replace d+e by t for all inputs.
D. Delete the first assignment and leave u=t with no definition of t.

### Q29. [1 Mark] [NAT]

Starting with one process, the following code executes. Every fork succeeds, returns 0 only in its new child, and returns a positive child identifier in its parent. Every process reaches the final line once. How many processes execute work()?

```c
int p = fork();
if (p == 0) fork();
fork();
work();
```

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

Two positive-edge-triggered flip-flops have state (A,B) and next-state equations A'=A XOR B and B'=NOT A. Starting at (0,0), how many distinct states occur before the first repeated state?

**Answer format:** Exact integer.

### Q31. [1 Mark] [NAT]

Over {a,b}, consider the regular expression a*(ba*)*. How many different words of length four belong to its language?

**Answer format:** Exact integer.

### Q32. [1 Mark] [NAT]

A nondecreasing array is[1,2,2,2,4,7], with indices0–5. A binary search for the first index with value at least2 uses a half-open search interval[l,r), initially[0,6), and updates r=mid when A[mid]≥2, otherwise l=mid+1, where mid=floor((l+r)/2). How many array-element comparisons occur before l=r?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

X is binomial with four trials and success probability p, where 0<p<1. Given P(X=0)=P(X=2), find E[X], rounded to three decimal places.

**Answer format:** Number to 3 decimal places.

### Q34. [1 Mark] [NAT]

A control store has256 words. Each word contains eight independent control bits and a binary address field naming any word. No other fields exist. How many bits does the entire control store contain?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

Two Ethernet stations independently select a uniformly random integer backoff from {0,1,…,7}. What is the probability that exactly one selects zero?

**Answer format:** Decimal rounded to five places.

### Q36. [2 Marks] [NAT]

A disk head starts at track 50 moving upward at one track per ms on tracks 0–99. It uses SCAN: it continues to physical endpoint 99 before reversing, even if no pending request lies farther upward. At time zero requests exist at tracks 60 and 20. A new request for track 70 arrives at time 30 ms, after the head has passed track 70. Service takes zero time; direction does not change for the new arrival. How many ms does the new request wait from arrival to service?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Let p point to the first element of an array of five ints. Which pointer expressions are permitted to be formed in C? No dereference is performed.

A. p+4
B. p+5
C. p+6
D. (p+5)-2

### Q38. [2 Marks] [NAT]

A linked list has a noncyclic prefix of length 3 followed by a cycle of length 5. Floyd's algorithm starts slow and fast at the head. In phase one, each iteration advances slow by one link and fast by two, then tests equality; it stops at the first equality. In phase two, one pointer is reset to the head, and both move one link at a time until equal. Count every individual next-link traversal in both phases, excluding the reset. What is the total?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

In a tabular Boolean minimization, a dash in a four-bit cube denotes a free variable. The ON-set is {0,1,2,3,8,9}, the don't-care set is {10}, and all remaining minterms are OFF. Which operations are valid? A combined cube must contain no OFF minterm.

A. Combine 000- and 001- to obtain 00--.
B. Combine 00-- and 100- to obtain -0--.
C. Combine 00-0 and 10-0 to obtain -0-0.
D. Combine -00- and -010 to obtain -0--.

### Q40. [2 Marks] [NAT]

Fixed partitions have sizes8,12,20 KiB. Processes of sizes7,10,18 KiB are assigned to them respectively. What is total internal fragmentation, in KiB?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A block contains a 3×4 array of data bits. Separate parity bits check every row and every column. Exactly four distinct data bits flip, and no parity bit changes. How many four-position error patterns go undetected by all row and column parity checks?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A byte-addressed memory uses four banks, selected by the low two address bits. Each bank stores one byte at each local row; the remaining address bits select that row. A four-byte word beginning at byte address6 is read. How many distinct local row numbers are accessed across its four bytes?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A processor's execution time is40% memory-stall time and60% other time on a fixed workload. A proposed change halves only the memory-stall component but increases the other component by10%. What is the new execution time as a percentage of the original time?

**Answer format:** Exact percentage number, without the percent symbol.

### Q44. [2 Marks] [NAT]

A path starts at the top-left cell and ends at the bottom-right cell of the cost grid below, moving only one cell right or down. Its cost is the sum of visited cell costs, including both endpoints. Once during the path, it may replace one visited cell's cost by0. What is the minimum possible path cost?

```text
 0   5   1
 2  -4   3
 9   2   0
```

**Answer format:** Exact signed integer.

### Q45. [2 Marks] [NAT]

Nonpreemptive shortest-job-first scheduling handles jobs J1,J2,J3 with arrival times 0,1,2 and CPU bursts 5,2,1. Context switching costs zero. What is their mean turnaround time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q46. [2 Marks] [NAT]

Grammar S→aSbS | bSaS | ε generates equal numbers of a and b. How many distinct strings of length four does it generate? Count strings, not parse trees.

**Answer format:** Integer.

### Q47. [2 Marks] [MSQ]

An optimizer replaces a conditional assignment by unconditional arithmetic. In the original program, an expression on an untaken branch is not evaluated and may divide by zero if evaluated. Which statements are correct?

A. Preserving the selected numerical result alone is enough to justify evaluating both branches.
B. Introducing a previously avoided invalid division can change program behavior.
C. A proof that both branch expressions are safe and side-effect-free is relevant to such a rewrite.
D. Branch removal never changes which expressions are evaluated.

### Q48. [2 Marks] [MSQ]

Let L={w#wᴿ : w∈{0,1}*}, where # is a separator and wᴿ denotes reversal. Which statements are correct?

A. A deterministic pushdown automaton can recognize L by switching from pushing to matching at #.
B. L is regular because the separator locates its midpoint.
C. Removing # from every word of L produces a context-free language.
D. A finite automaton can always store the entire prefix w because each individual input is finite.

### Q49. [2 Marks] [NAT]

A clustered file packs ten fixed-length records per data block. A range scan starts at zero-based slot 7 of one block and returns the next 23 records, including that starting record. Finding the first record requires reading three separate index blocks; all blocks are initially uncached, index blocks are distinct from data blocks, and following data blocks incurs no extra index reads. How many distinct blocks must be read?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

A comparison tournament finds the largest of seven distinct keys using six comparisons. The eventual winner received one initial bye and participated in exactly two comparisons. Using only the recorded results plus further key comparisons, what is the minimum total number of comparisons, including the original six, sufficient to identify both the largest and second-largest keys in the worst case under this condition?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

How many insertion orders of the distinct keys 1–7 produce an ordinary unbalanced BST whose root is 4, whose left subtree has root 2 and leaves 1,3, and whose right subtree has root 6 and leaves 5,7? There is no rebalancing.

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A write-back, write-allocate cache has initially empty lines, with16 bytes per block. A processor writes one byte at each of addresses0,1,16,17. The cache has enough space for both blocks and evicts neither during these stores. It is then flushed, writing every dirty block once. Ignoring metadata and counting full-block transfers, how many bytes move between cache and memory in total?

**Answer format:** Exact integer.

### Q53. [2 Marks] [NAT]

A file contains1000 fixed-size records of80 bytes in4000-byte data blocks, with no headers and no spanning. A sparse index has one16-byte entry per data block and is stored in4000-byte index blocks. No blocks are cached. A successful lookup first reads the required index block, then the selected data block. What is the total number of block reads for that lookup?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

The complete undirected graph on labelled vertices A,B,C,D has one edge between every pair. How many spanning trees contain edge AB but do not contain edge AC?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A slotted switch has two inputs and two outputs O1,O2. Initially input I1 holds packets [A destined for O1, B destined for O2] in that order, and I2 holds [C destined for O1]. No packets arrive later. A packet occupies one whole slot; each input and each output serves at most one packet per slot. O1 is unavailable in slots 1 and 2 and available thereafter; O2 is always available. Ties for O1 favour I1. Compare strict FIFO input queues (only a head packet is eligible) with separate queues per output at each input (B can bypass A). By how many slots does FIFO delay B's departure relative to the separate-queue design?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

Six positions around a circle are filled with two red, two blue and two green beads. Beads of the same colour are indistinguishable. Adjacent positions, including the last and first, must have different colours. Arrangements related by rotation are identified; reflections are counted separately unless a rotation already identifies them. How many arrangements are there?

**Answer format:** Numeric value; integer.

### Q57. [2 Marks] [MSQ]

A constant-propagation pass treats integer comparisons exactly and removes unreachable branches. Integer arithmetic is unbounded. Consider:

```text
x=0;
if x==0 { y=4; } else { y=input(); }
z=y*y;
```

Which statements hold?

A. The call input() is unreachable.
B. z can be replaced by16 after proving the branch condition.
C. It is necessary to execute input() to determine whether z is constant.
D. y is nonconstant solely because one syntactic assignment uses input().

### Q58. [2 Marks] [MSQ]

Relations R(x) and S(x) are finite subsets of an infinite domain D. In the following tuple-calculus formulas, x is the only free variable and quantifiers range over D. Which formulas necessarily define finite result sets for every finite R,S?

A. R(x) AND NOT S(x)
B. NOT R(x) AND NOT S(x)
C. EXISTS y (R(y) AND x=y)
D. FOR ALL y (S(y) IMPLIES x=y)

### Q59. [2 Marks] [NAT]

A full binary tree, in which every node has zero or two children, has 19 nodes. Exactly four internal nodes have two leaf children each. How many leaves have a sibling that is an internal node?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

Let L be a language that is not context-free. Which statements are true?

A. Its reversal Lᴿ cannot be context-free.
B. Every homomorphic image of L must be non-context-free.
C. Intersecting L with any regular language must remain non-context-free.
D. A homomorphism erasing every symbol can map L to a regular language.

### Q61. [2 Marks] [MCQ]

A NAT maps internal TCP endpoint 192.168.1.8:5000 to public endpoint 203.0.113.2:42000 for a connection to 198.51.100.9:443. It translates an outgoing IPv4 packet with no options and no fragmentation. Which checksum fields must be updated because of these substitutions?

A. Only the IPv4 header checksum.
B. Only the TCP checksum.
C. Neither checksum, because payload bytes are unchanged.
D. Both the IPv4 header checksum and the TCP checksum.

### Q62. [2 Marks] [NAT]

A four-variable Boolean function, indexed by ABCD with A most significant, is 1 exactly when the Hamming weight of ABCD is 2. There are no don't-cares. What is the minimum number of product terms in a two-level sum-of-products expression for the function? Complemented literals are allowed.

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

Let A(a) have rows (1,a,0), (0,1,a), (a,0,1), where a is real. Consider A(a)x=(1,1,1)ᵀ. Which statements are true?

A. A(a) is singular for every real a.
B. det(A(a))=1+a³.
C. At a=−1, the displayed system has infinitely many solutions.
D. At a=−1, A(a) has rank two.

### Q64. [2 Marks] [MSQ]

An n-bit ripple-carry adder adds unsigned A and B with carry-in0. Its most significant sum bit is s, carry into that bit is c and carry out is d. The input sign bits, when interpreted as two's complement, are a and b. Which expressions detect signed overflow for every input?

A. c XOR d.
B. d alone.
C. ((NOT a) AND (NOT b) AND s) OR (a AND b AND (NOT s)).
D. a XOR b.

### Q65. [2 Marks] [NAT]

Let u,v be real column vectors of length four satisfying vᵀu=−1, and A=I+uvᵀ. Find det(A+2I).

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 070

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C |
| 2 | NAT | 1 | 1 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 2 |
| 5 | NAT | 1 | 50 |
| 6 | NAT | 2 | 3 |
| 7 | NAT | 2 | 4 |
| 8 | NAT | 2 | 0.4444 (accepted range 0.44435–0.44445) |
| 9 | NAT | 2 | 4 |
| 10 | NAT | 2 | 8 |
| 11 | NAT | 1 | 6 |
| 12 | NAT | 1 | 4 |
| 13 | NAT | 1 | 2 |
| 14 | NAT | 1 | 988 |
| 15 | MCQ | 1 | B |
| 16 | MSQ | 1 | A, C |
| 17 | NAT | 1 | 2 |
| 18 | MSQ | 1 | A, B |
| 19 | NAT | 1 | 2 |
| 20 | NAT | 1 | 4 |
| 21 | NAT | 1 | 6 |
| 22 | NAT | 1 | 4 |
| 23 | NAT | 1 | 160 |
| 24 | MSQ | 1 | A, C, D |
| 25 | MCQ | 1 | B |
| 26 | NAT | 1 | 2 |
| 27 | MSQ | 1 | A, C |
| 28 | MCQ | 1 | A |
| 29 | NAT | 1 | 6 (exact) |
| 30 | NAT | 1 | 3 |
| 31 | NAT | 1 | 16 |
| 32 | NAT | 1 | 3 |
| 33 | NAT | 1 | 1.160 (range 1.1595–1.1605) |
| 34 | NAT | 1 | 4096 |
| 35 | NAT | 1 | 0.21875 (five decimals) |
| 36 | NAT | 2 | 48 |
| 37 | MSQ | 2 | A, B, D |
| 38 | NAT | 2 | 21 |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 5 |
| 41 | NAT | 2 | 18 |
| 42 | NAT | 2 | 2 |
| 43 | NAT | 2 | 86 |
| 44 | NAT | 2 | -2 |
| 45 | NAT | 2 | 5.3333 (range 5.33325–5.33335) |
| 46 | NAT | 2 | 6 |
| 47 | MSQ | 2 | B, C |
| 48 | MSQ | 2 | A, C |
| 49 | NAT | 2 | 6 |
| 50 | NAT | 2 | 7 |
| 51 | NAT | 2 | 80 |
| 52 | NAT | 2 | 64 |
| 53 | NAT | 2 | 2 |
| 54 | NAT | 2 | 5 |
| 55 | NAT | 2 | 3 |
| 56 | NAT | 2 | 5 (exact) |
| 57 | MSQ | 2 | A, B |
| 58 | MSQ | 2 | A, C |
| 59 | NAT | 2 | 2 |
| 60 | MSQ | 2 | A, D |
| 61 | MCQ | 2 | D |
| 62 | NAT | 2 | 6 |
| 63 | MSQ | 2 | B, D |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 54 |
