# GATE CS 2027 — Full-Length Mock Test 080

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

Choose the word that best completes the sentence: “The committee accepted the proposal, ___ its concern about the short implementation period.”

A. because
B. notwithstanding
C. therefore
D. consequently

### Q2. [1 Mark] [MCQ]

A square paper is folded once along its vertical midline. A small circular hole is punched through both layers away from the fold and away from the edges. After unfolding, which statement must hold about the two holes?

A. They are images of each other under reflection in the fold line.
B. They necessarily lie on the fold line.
C. Their distance apart equals the side of the original square.
D. Their positions are related by a 90-degree rotation about the centre for every punch location.

### Q3. [1 Mark] [MCQ]

A narrative contains: “Mira mailed the parcel after weighing it. She obtained the address before mailing it, but the text does not specify whether she obtained the address before or after weighing.” Which order is inconsistent with this account?

A. Obtain address, weigh, mail.
B. Weigh, obtain address, mail.
C. Weigh, mail, obtain address.
D. Both A and B are possible.

### Q4. [1 Mark] [NAT]

Cards labelled1,2,3 are placed in uniformly random order. Given that the first card's number is smaller than the second card's number, what is the probability that the second card's number is smaller than the third card's number?

**Answer format:** Decimal rounded to four places.

### Q5. [1 Mark] [MCQ]

“The panel vacillated between the two proposals, repeatedly reversing its tentative preference.” Which word best replaces vacillated without changing the meaning?

A. Wavered
B. Collaborated
C. Converged
D. Disappeared

### Q6. [2 Marks] [MSQ]

For which of the following real values of x is the equation log_x(16)=log_2(x) defined and true?

A. 4  
B. 1/4  
C. −4  
D. 1

### Q7. [2 Marks] [MCQ]

A square's side is increased by 10%. A circle's radius is increased by 10%. Which pair gives the percentage increases in their areas?

A. 10%,10%
B. 20%,20%
C. 21%,21%
D. 21%,10%

### Q8. [2 Marks] [NAT]

A shop buys equal numbers of two items at Rs. 60 and Rs. 100 per item. It sells every cheaper item at a 25% profit and every costlier item at a 10% loss, with no other costs. What is the overall profit percentage? Round to three decimal places.

**Answer format:** Percentage to 3 decimal places.

### Q9. [2 Marks] [MCQ]

In a group of 20 workers the mean daily output is 30 units. After removing the five workers with the lowest outputs, the mean of the remaining workers is 34. A second group of five workers, each producing 28 units, joins those remaining workers. What is the difference between the new 20-worker mean and the mean of the five removed workers?

A. 12.5 units
B. 14.5 units
C. 16 units
D. 18 units

### Q10. [2 Marks] [NAT]

Two circular disks of equal radius r>0 have centres separated by distance r. Let P be the perimeter of their union, excluding arcs lying inside the other disk. What is P/(πr)?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Two independent fair coins are tossed. Their colours are red and blue, so they are distinguishable. A report states that the red coin is heads. What is the conditional probability that exactly one coin is heads?

**Answer format:** Exact decimal.

### Q12. [1 Mark] [NAT]

A scheduler uses shortest remaining processing time, with zero switching cost. Job A arrives at 0 with burst7, B at 2 with burst2, and C at 3 with burst1. A tie retains the currently running job. At what time does A complete?

**Answer format:** Exact integer.

### Q13. [1 Mark] [MSQ]

An optimizer considers reusing a+b across a function call. Arithmetic is exact. Which conditions are sufficient for this reuse to preserve the expression value?

A. a and b are unchanged local scalars whose addresses have never escaped, and the called function has no access to them.  
B. a and b are mutable globals, and the function's effects are unknown.  
C. The function is proven not to modify either operand, directly or indirectly.  
D. The expression text is identical before and after the call, regardless of side effects.

### Q14. [1 Mark] [MCQ]

A binary tree has distinct labels, preorder A,B,D,E,C,F and inorder D,B,E,A,C,F. What is its postorder?

A. D,E,B,F,C,A
B. D,B,E,F,C,A
C. E,D,B,C,F,A
D. D,E,F,B,C,A

### Q15. [1 Mark] [NAT]

An eight-bit two's-complement fixed-point value has three fractional bits and raw bit pattern11110100. What real value does it represent?

**Answer format:** Exact decimal.

### Q16. [1 Mark] [MSQ]

Order the set{1,2,3,4,12} by divisibility. Which statements are correct?

A. This poset is a lattice.
B. This lattice is distributive.
C. The join of2 and3 is12.
D. The meet of4 and3 is1.

### Q17. [1 Mark] [MCQ]

A disk scheduler uses LOOK, moving toward increasing cylinder numbers. The head is at 40; pending requests are 10,30,55,70. No further requests arrive. Which service order follows?

A. 55,70,30,10
B. 30,10,55,70
C. 55,30,70,10
D. 70,55,30,10

### Q18. [1 Mark] [MSQ]

An address-and-port translator lets two internal clients connect simultaneously to the same external server and server port, using one public IPv4 address. Assume its mapping distinguishes connections using the public source port. Which statements are correct?

A. The two active mappings need different public source ports.
B. Both internal clients must have identical private source addresses.
C. Return traffic can be demultiplexed using the stored mappings.
D. The translator must change the external server's application data to identify the clients.

### Q19. [1 Mark] [MSQ]

Two established TCP connections terminate at the same server IPv4 address and local port. Which statements are correct?

A. They may be distinguished by different remote IPv4 addresses or remote ports.
B. The shared local port alone forces the two connections to be the same connection.
C. The connection-identifying four-tuple includes both endpoint addresses and both endpoint ports.
D. Every established server-side connection must use a different local port.

### Q20. [1 Mark] [MCQ]

In C, assuming the proper standard header and successful allocation, which statement about `int *p=malloc(3*sizeof *p);` is correct before any initialization of the allocated int objects?

A. All three int values are guaranteed to be zero.
B. The allocated storage persists until it is freed, even if the local pointer variable leaves scope.
C. sizeof *p evaluates an indeterminate pointed-to int value.
D. The allocation contains exactly three bytes on every implementation.

### Q21. [1 Mark] [MCQ]

In C, `int a[3]={5,6,7}; int *p=a+3;` is executed. Which subsequent operation is valid by the one-past-the-end pointer rule?

A. Evaluate *p.
B. Evaluate *(p-1).
C. Form p+1 and dereference it.
D. Write p[0]=8.

### Q22. [1 Mark] [MCQ]

A PDA for balanced parentheses pushes on '(' and pops on ')'. Which extra condition is needed besides having an empty stack at the end, assuming a separate bottom marker?

A. No prefix may attempt to pop below the bottom marker.
B. The input must have odd length.
C. Every '(' must be immediately followed by ')'.
D. The stack may contain only two items throughout the input.

### Q23. [1 Mark] [NAT]

Gaussian elimination without row exchanges factors A=LU, where L has unit diagonal. For

```text
A = [ 2  1  0
      4  3  1
      2  2  3 ]
```

what is the entry U33 after both elimination stages?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MCQ]

A system's measured cache hit rate rises after an optimization, but its clock period also increases. Which conclusion is justified without further data?

A. Total execution time necessarily decreases.
B. Hit rate alone is insufficient to establish an execution-time improvement.
C. The instruction count must become zero.
D. A higher hit rate necessarily implies a shorter clock period.

### Q25. [1 Mark] [NAT]

Evaluate the integral from 0 to 1 of max(x,1-2x) with respect to x. Round the result to three decimal places.

**Answer format:** Numeric value; 3 decimal places.

### Q26. [1 Mark] [MCQ]

A four-line direct-mapped cache starts empty and uses block number modulo four as its line index. Which reference sequence has exactly one hit?

A. 0,4,0,4
B. 0,1,0,4
C. 0,1,2,3
D. 0,0,0,0

### Q27. [1 Mark] [NAT]

A binary floating-point format has three significant bits including the leading one, sufficient exponent range, and round-to-nearest with ties-to-even. Starting from the exactly represented value 1, add the exact real number 0.125 twice, rounding after each addition. What is the exact real sum minus the final stored value?

**Answer format:** Exact finite decimal.

### Q28. [1 Mark] [MSQ]

A SQL table declares id as PRIMARY KEY and parent_id as a nullable foreign key referencing id in the same table. There are no other constraints. Which statements hold?

A. A row may have parent_id=NULL.
B. The declarations alone prevent a row from referencing itself.
C. The declarations alone prevent a cycle involving two rows.
D. Every non-NULL parent_id must match an existing id when the foreign-key constraint is checked.

### Q29. [1 Mark] [NAT]

A graph has edges AB=1, BC=2, AC=2, AD=3 and CD=3, with no others. By how much does the minimum spanning-tree weight increase if edge AB is deleted?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

On R(A,B,C,D), the functional dependencies are A→B, B→C and AC→D. How many attributes are in the closure of A under these dependencies?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

An unordered file has 1,000 fixed-size records, 25 records per disk block, and no index. A successful equality search scans blocks in a fixed order and stops on the block containing the target record. Each record is equally likely to be the target. What is the expected number of block reads?

**Answer format:** Exact finite decimal.

### Q32. [1 Mark] [MCQ]

Which operation is guaranteed to preserve context-freeness for two context-free languages L1,L2?

A. Union
B. Intersection in every case
C. Complement in every case
D. Set difference in every case

### Q33. [1 Mark] [NAT]

A lexer recognizes identifiers matching a letter followed by zero or more letters or digits, integer literals matching one or more digits, and the operators '=', '==', '>'. It uses longest match and skips spaces. How many tokens does it emit for the input below?

```text
a1===23> b
```

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

An unweighted directed graph has exactly the edges s→a, s→b, a→c, a→d, b→d, c→t, d→t. Which pair gives the shortest s-to-t path length in edges and the number of distinct shortest s-to-t paths?

A. (3,3)
B. (3,2)
C. (4,3)
D. (3,4)

### Q35. [1 Mark] [MCQ]

A data set has five real observations with median 10 and mean 12. A sixth observation equal to 100 is appended. Which quantity is determined uniquely from this information?

A. The new median.
B. The new mean.
C. The new range.
D. The new population variance.

### Q36. [2 Marks] [MSQ]

An interrupt handler increments a counter for every delivered interrupt. A device sets one pending bit whenever an event occurs; further events while that bit is1 do not accumulate. The handler clears the bit once on entry. Which statements are correct?

A. The counter necessarily equals the number of device events.
B. Two events arriving before the handler clears the bit may cause only one counter increment.
C. Replacing the pending bit with an adequately sized event counter can preserve event multiplicity if updates and reads are synchronized correctly.
D. Faster handler execution alone logically guarantees exact event counts for every possible event timing.

### Q37. [2 Marks] [MCQ]

A datagram socket has queued datagrams of lengths 12 and 5 bytes, in that order. Each receive uses an 8-byte buffer. The specified API returns at most one datagram per receive and discards excess bytes of a truncated datagram. What byte counts do the next two receives return?

A. 8 and 8
B. 8 and 5
C. 12 and 5
D. 8 and 4

### Q38. [2 Marks] [MCQ]

Thirteen distinct keys occupy positions 1 through 13. A tournament finds the minimum as follows: in each round, compare consecutive surviving keys in their current order, keep the smaller from each pair, and give the final unpaired key a bye when the number of survivors is odd. Survivors retain their order. After finding the minimum, find the second-smallest by scanning only the keys that lost directly to the minimum, using one fewer comparisons than the number of these keys. Over all possible initial key orders, what are the (minimum, maximum) possible total numbers of comparisons for both stages together?

A. (12,15)  
B. (13,15)  
C. (14,16)  
D. (15,15)

### Q39. [2 Marks] [NAT]

Six independent multiplication operations feed six additions into a running accumulator, in multiplication order. A multiply takes three cycles; an add takes one cycle, and an add may begin when its multiply and the previous accumulator add have finished. Different functional units overlap. Multiplications start as early as the multiplier permits, beginning at time zero. Compare a pipelined multiplier accepting a new operation every cycle with an unpipelined multiplier accepting one every three cycles. How many cycles earlier does the sixth addition finish in the pipelined design?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

Free memory holes, in address order, have sizes200,500,300 bytes. Process requests250 bytes and then200 bytes; each allocation consumes space from the beginning of its chosen hole, without overhead. Compare first-fit with best-fit, starting separately from the original holes. What is the largest remaining hole under best-fit minus that under first-fit?

**Answer format:** Integer bytes.

### Q41. [2 Marks] [NAT]

An initially empty B+ tree has a single root leaf. Each leaf holds at most three keys. Inserting a fourth key splits a leaf into two leaves of two keys each, promoting the first key of the right leaf to the parent; the key remains in the leaf. Insert1,2,3,4,5,6 in order. The internal root can hold at least three separators. How many leaf nodes exist afterward?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Consider the grammar

```text
S → a A | a B
A → b
B → c
```

The start symbol is S and the terminals are a,b,c. Which statements hold?

A. The grammar as written has an LL(1) conflict in S's row.
B. The language cannot be generated by any LL(1) grammar.
C. Left factoring S into S→aX, X→b|c yields an LL(1) grammar for the same language.
D. The grammar is ambiguous because both S productions begin with a.

### Q43. [2 Marks] [MSQ]

Let L={a^n : n is a perfect square}, including ε. For a hypothetical regular pumping length p≥1, choose s=a^(p²). A legal pumped part has length k with1≤k≤p. Which statements are correct?

A. Pumping once more gives length p²+k, strictly between p² and(p+1)².
B. For every legal decomposition, pumping twice leaves the language.
C. The proof depends on choosing the pumped part to have exactly p symbols.
D. The pumping lemma therefore proves L regular.

### Q44. [2 Marks] [NAT]

A memoized function F(n) has base F(0)=0,F(1)=1. For n≥2 it calls F(n−1), then F(n−2), sums the results, and stores the result. The cache is initially empty, and base cases are cached too. On a cache hit, the function returns immediately. During evaluation of F(6), how many function invocations occur, including cache hits and the initial call?

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

A TCP sender learns that the path MTU is 1280 bytes and wishes to send full-sized IPv4 packets without fragmentation. IPv4 and TCP each use a 20-byte header, with no options or other encapsulation. The application has 3000 bytes ready. What is the payload size, in bytes, of the final packet when earlier packets use the maximum permitted payload?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A TCP segment contains 1000 data bytes and a 20-byte TCP header. It is carried in an IPv4 datagram with a 20-byte header and no options. A router fragments this datagram for a link whose IP MTU is 600 bytes, using the minimum number of fragments and the largest permitted first-fragment payload. Each link frame adds a 14-byte header and a four-byte trailer. Ignore padding, preambles and gaps. How many bytes are transmitted on this link for all fragments, including these headers and trailers?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

Under multiplication modulo15, consider the group of invertible residues. How many group elements x satisfy x²=1 modulo15?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

For four Boolean inputs a,b,c,d, let F=(a XOR b) AND (b XOR c) AND (c XOR d). How many input assignments make F=1?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

Processes P and Q each reference two private pages. The interleaved reference sequence is P1,Q1,P2,Q2,P1,Q1,P2,Q2. Compare three initially empty frames managed by global FIFO with local FIFO allocating two frames exclusively to P and one exclusively to Q. How many more page faults occur under the global allocation?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

For F(a,b,c,d)=(a XOR b)(c XOR d), what is the minimum total number of literal occurrences in a two-level sum-of-products expression without don't-care inputs? Count each occurrence in each product separately.

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

An algorithm receives a Turing machine M and a nonnegative integer k written in binary. It asks whether M, started on blank input, halts within k steps. Which statements are correct?

A. This bounded question is decidable by direct simulation.
B. A potentially enormous value of k makes the problem undecidable.
C. The same simulation strategy decides eventual halting without any bound by choosing one universally sufficient finite k.
D. Binary encoding can make the simulation duration much larger than the length of k's representation.

### Q52. [2 Marks] [MCQ]

A comparison sorting algorithm sorts n distinct keys. Its decision tree has binary comparison outcomes. Which is a valid worst-case lower-bound argument?

A. There are n possible outputs, so height is at least log₂n.
B. There are n! possible input orders requiring different sorting permutations, so height is at least ceil(log₂(n!)).
C. Every sorting algorithm must use exactly n² comparisons.
D. Each comparison places one key permanently, so n comparisons always suffice.

### Q53. [2 Marks] [MSQ]

Two transactions both hold shared locks on x and each requests an upgrade to an exclusive lock before releasing its shared lock. No other transaction holds a lock. Which statements are correct?

A. Both upgrade requests can block, creating a deadlock.
B. The two-phase-locking rule by itself prevents this deadlock.
C. Each exclusive upgrade conflicts with the other transaction's shared lock.
D. The original pair of shared locks already conflicted with each other.

### Q54. [2 Marks] [MCQ]

A 5×5 matrix is stored in row-major order in a one-dimensional C array: row r, column c is a[5*r+c], for 0≤r,c<5. Consider this complete program. All arithmetic fits in int.
```c
#include <stdio.h>
static void swap(int *p, int *q) {
    int t = *p; *p = *q; *q = t;
}
int main(void) {
    int a[25];
    for (int i = 0; i < 25; ++i) a[i] = i;
    for (int k = 0; k < 2027; ++k) {
        for (int r = 0; r < 5; ++r)
            for (int c = r + 1; c < 5; ++c)
                swap(&a[5*r+c], &a[5*c+r]);
        for (int r = 0; r < 5; ++r)
            for (int c = 0; c < 2; ++c)
                swap(&a[5*r+c], &a[5*r+4-c]);
    }
    printf("%d %d", a[7], a[17]);
    return 0;
}
```
What is printed?

A. 13 11  
B. 11 13  
C. 7 17  
D. 17 7

### Q55. [2 Marks] [NAT]

A bipartite graph has left vertices a,b,c,d and right vertices1,2,3,4. Vertices a,b are adjacent only to1, while c,d are adjacent only to2. How many unordered pairs of currently absent edges, when added together, make a perfect matching possible?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

Independent coin tosses alternate between two coins: odd-numbered tosses have P(H)=1/2 and even-numbered tosses have P(H)=1/4. Tossing starts at toss 1 and stops immediately when two consecutive heads first occur. What is the expected number of tosses? Round to three decimal places.

**Answer format:** Number to 3 decimal places.

### Q57. [2 Marks] [MCQ]

A double-hashing table has 12 slots. Probing from h1 uses (h1+jh2) mod 12 for j=0,1,2,…. The second hash is chosen uniformly from {1,2,…,11}. What is the probability that the probe sequence visits every slot before repeating, regardless of h1?

A. 1/3  
B. 4/11  
C. 6/11  
D. 1

### Q58. [2 Marks] [NAT]

A strip of length6 is tiled with unit tiles and length-two tiles. Two length-two tiles may not be adjacent. Tiles of the same length are indistinguishable. How many different left-to-right tilings exist?

**Answer format:** Integer.

### Q59. [2 Marks] [MSQ]

A Boolean cover-selection chart contains candidate rows P and Q. P covers{u,v} at cost3; Q covers{u,v,w} at cost2. The objective is minimum total cost, and selecting a row has no effect except covering its columns. Which statements are correct?

A. An optimal cover can always be chosen without P.
B. Replacing P by Q in a cover cannot uncover a column and cannot increase cost.
C. P must be retained merely because some of its columns also appear in Q.
D. The same dominance conclusion follows if Q instead costs5, solely from its greater coverage.

### Q60. [2 Marks] [MSQ]

Consider the following algorithm, with n≥2 and a constant-time body that allocates no storage:

```text
for i = 1 to n:
    for j = i to n step i:
        body()
```

Which statements are correct?

A. The body executes exactly Σ(i=1..n) floor(n/i) times.
B. The running time is Θ(n log n).
C. The algorithm needs Θ(n) auxiliary words merely to execute these loops.
D. The body executes Θ(n²) times.

### Q61. [2 Marks] [NAT]

A precedence graph for a transaction schedule has exactly three vertices T1,T2,T3 and the single edge T1→T3. How many serial orders are conflict-equivalent to the schedule?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

In a singly linked structure, head reaches a path of length3 edges before first entering a cycle of length4. Floyd's algorithm starts slow and fast at head and, in each iteration, advances slow by one edge and fast by two, then compares them. How many iterations occur before the first equality?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

Over alphabet {a,b}, consider the language of strings with an even number of a's whose last symbol is b. The empty string is not in the language. What is the minimum number of states in a complete DFA recognizing it?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A 16-bit instruction set uses variable-length opcodes but fixed-length instructions. There are 8 registers. Type A uses two three-bit register fields and has 32 opcodes. Type B uses one three-bit register field. Opcode prefixes are allocated so no Type B instruction is confused with Type A. All bit patterns not allocated to Type A may be used for Type B, and each Type B opcode must allow all eight registers. What is the maximum number of Type B opcodes?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Under lexical scope, an outer procedure activation P1 has local x=10 and creates a nested procedure Q1 that refers to P1.x. A later separate activation P2 has local x=20 and calls Q1, passing no x parameter. Environments are retained correctly for nested procedures. What value of x does Q1 read?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 080

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MCQ | 1 | A |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 5 | MCQ | 1 | A |
| 6 | MSQ | 2 | A, B |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 3.125 (range 3.1245–3.1255) |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 2.6667 (accepted range 2.66665–2.66675) |
| 11 | NAT | 1 | 0.5 |
| 12 | NAT | 1 | 10 |
| 13 | MSQ | 1 | A, C |
| 14 | MCQ | 1 | A |
| 15 | NAT | 1 | -1.5 |
| 16 | MSQ | 1 | A, C, D |
| 17 | MCQ | 1 | A |
| 18 | MSQ | 1 | A, C |
| 19 | MSQ | 1 | A, C |
| 20 | MCQ | 1 | B |
| 21 | MCQ | 1 | B |
| 22 | MCQ | 1 | A |
| 23 | NAT | 1 | 2 |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 0.667 (exact) |
| 26 | MCQ | 1 | B |
| 27 | NAT | 1 | 0.25 |
| 28 | MSQ | 1 | A, D |
| 29 | NAT | 1 | 1 (exact) |
| 30 | NAT | 1 | 4 |
| 31 | NAT | 1 | 20.5 |
| 32 | MCQ | 1 | A |
| 33 | NAT | 1 | 6 |
| 34 | MCQ | 1 | A |
| 35 | MCQ | 1 | B |
| 36 | MSQ | 2 | B, C |
| 37 | MCQ | 2 | B |
| 38 | MCQ | 2 | B |
| 39 | NAT | 2 | 10 |
| 40 | NAT | 2 | 200 |
| 41 | NAT | 2 | 3 |
| 42 | MSQ | 2 | A, C |
| 43 | MSQ | 2 | A, B |
| 44 | NAT | 2 | 11 |
| 45 | NAT | 2 | 520 |
| 46 | NAT | 2 | 1096 (exact) |
| 47 | NAT | 2 | 4 |
| 48 | NAT | 2 | 2 |
| 49 | NAT | 2 | 2 |
| 50 | NAT | 2 | 16 |
| 51 | MSQ | 2 | A, D |
| 52 | MCQ | 2 | B |
| 53 | MSQ | 2 | A, C |
| 54 | MCQ | 2 | A |
| 55 | NAT | 2 | 8 |
| 56 | NAT | 2 | 11.273 (range 11.2725–11.2735) |
| 57 | MCQ | 2 | B |
| 58 | NAT | 2 | 9 |
| 59 | MSQ | 2 | A, B |
| 60 | MSQ | 2 | A, B |
| 61 | NAT | 2 | 3 |
| 62 | NAT | 2 | 4 |
| 63 | NAT | 2 | 3 |
| 64 | NAT | 2 | 7936 |
| 65 | NAT | 2 | 10 |
