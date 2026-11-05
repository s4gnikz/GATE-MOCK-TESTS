# GATE CS 2027 — Full-Length Mock Test 092

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

### Q1. [1 Mark] [NAT]

A sequence starts with 3. To obtain successive terms, alternately multiply by 2 and subtract 1, starting with multiplication. What is its seventh term?

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A rectangle has perimeter 30 and diagonal length √125. What is its area?

**Answer format:** Integer square units.

### Q3. [1 Mark] [MCQ]

Select the pair completing the sentence with correct subject–verb agreement: “One of the proposals that ___ discussed yesterday ___ now been withdrawn.”

A. was, have
B. were, have
C. was, has
D. were, has

### Q4. [1 Mark] [NAT]

Six equally efficient workers can complete a job in eight days. They work for two days, after which two workers leave. How many additional days do the remaining workers need? Work is divisible and each worker's daily rate is constant.

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four switches P,Q,R,S are either ON or OFF. Exactly two are ON. Whenever P is ON, Q is ON. Whenever R is OFF, S is ON. Which statements must hold?

A. P is OFF.  
B. At least one of R and S is ON.  
C. Q is ON.  
D. If Q is OFF, both R and S are ON.

### Q6. [2 Marks] [NAT]

Two distinct numbers are selected uniformly as an unordered pair from {1,2,3,4,5,6}. Given that their product is even, what is the probability that their sum is even?

**Answer format:** Exact finite decimal.

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A voluntary online survey asks users of a study app whether it improved their examination scores. Eighty percent of respondents say yes. No earlier scores or comparison group are recorded. Which statement is best supported?

A. The app caused an improvement for 80% of all students.  
B. Eighty percent of respondents reported improvement, but population effects and causation are not established.  
C. Voluntary participation proves that respondents are representative.  
D. The app cannot have helped any student because there was no control group.

### Q8. [2 Marks] [NAT]

Six distinct students A,B,C,D,E,F are partitioned into two unlabelled groups of three. One leader is chosen in each group. A and B must be in different groups, C must lead the group containing C, and B must not be a leader. How many different group-and-leader assignments are possible? Swapping the names or display order of the two groups does not create a new assignment.

**Answer format:** Exact integer.

### Q9. [2 Marks] [NAT]

Last year, centre A passed 90 of 100 candidates and centre B passed 1 of 10. This year, A passed 19 of 20 and B passed 16 of 80. By how many percentage points did the combined pass percentage fall, despite both centres improving individually? Round to two decimal places.

**Answer format:** Number to 2 decimal places.

### Q10. [2 Marks] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left across x=4 and the top half down across y=4. From the folded stack, remove the triangle with vertices(4,4),(3,4),(4,3), cutting through all layers. After unfolding, a single hole is formed at the centre. What is the square of that hole's perimeter?

**Answer format:** Integer square units.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A BST has root20, left child10, right child30, and node10 has right child15. A right rotation is performed at20. How many nodes are visited by a successful ordinary search for30 after the rotation, including root and target?

**Answer format:** Integer.

### Q12. [1 Mark] [MCQ]

A binary CRC generator polynomial has nonzero constant term and contains the factor x+1. Which error pattern is guaranteed to be detected, irrespective of its positions within a sufficiently long codeword?

A. Every error with exactly four flipped bits.
B. Every error with an odd number of flipped bits.
C. Every error with any even number of flipped bits.
D. Every nonzero error pattern.

### Q13. [1 Mark] [MCQ]

A three-bit reflected Gray code g2g1g0 encodes binary b2b1b0 by g2=b2, g1=b2 XOR b1, g0=b1 XOR b0. The present Gray word is 101. What Gray word encodes the next larger binary integer, without wraparound?

A. 110
B. 111
C. 100
D. 001

### Q14. [1 Mark] [NAT]

A random variable X takes values 0,1,2 with probabilities1/4,1/2,1/4. Define Y=1 if X=1, and Y=0 otherwise. What is the covariance Cov(X,Y)?

**Answer format:** Exact integer.

### Q15. [1 Mark] [MSQ]

On {1,2,3}, equivalence relation R has classes {1,2},{3}; equivalence relation S has classes {1},{2,3}. Which statements are correct?

A. R∪S is transitive.
B. R∩S is the identity relation.
C. The smallest equivalence relation containing R∪S has one class.
D. R∪S contains the ordered pair(1,3).

### Q16. [1 Mark] [NAT]

A four-bit ripple-carry adder adds binary operands1011 and0110 with carry-in0. Let c1,c2,c3,c4 be the carry out of bit positions0,1,2,3 respectively, where bit0 is least significant. What unsigned integer is represented by c4c3c2c1?

**Answer format:** Exact integer.

### Q17. [1 Mark] [MSQ]

Consider this program with exact integers and an arbitrary Boolean input flag. A conventional nonrelational constant-propagation analysis tracks, for each variable separately, either a single constant or 'not constant'; at a join, distinct incoming constants become 'not constant'.
```text
if flag:
    x = 2; y = 3
else:
    x = 3; y = 2
z = x + y
```
Which statements are correct?

A. Every execution assigns5 to z.  
B. The stated analysis finds x constant at the join.  
C. The stated analysis necessarily infers z=5 directly from the joined abstract values of x and y.  
D. Moving the assignment z=x+y into the end of each branch allows the stated analysis to find z=5 after the join.

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For the following straight-line code, which variables are live immediately after the second statement? Use ordinary syntactic liveness on this code as written, before dead-code elimination; there are no implicit uses at return.

```text
x = a+b
y = x*c
x = d
return y
```

**Candidates**

**I.** x

**II.** d

**III.** c

**IV.** y

A. I and IV  
B. II and III  
C. II and IV  
D. III and IV

### Q19. [1 Mark] [NAT]

A control ROM is addressed by a two-bit operation code, a three-bit microstep index and two condition bits. Every address combination has a word containing 20 control bits and a seven-bit next address. How many bits does the ROM contain, including unused address combinations?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

Two Ethernet stations collide and independently choose their backoff values uniformly from {0,1,2,3}. Conditional on their values being different, what is the probability that the smaller value is zero?

**Answer format:** Exact decimal.

### Q21. [1 Mark] [NAT]

An ER relationship assigns each of 17 employees to exactly one department, and each department must have at least three assigned employees. Departments with no assigned employees are forbidden. What is the largest possible number of departments?

**Answer format:** Integer.

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which conclusion is logically justified by the regular-language pumping lemma alone?

A. If a language violates the lemma's pumping property, it is not regular.  
B. If a language satisfies the pumping property, it must be regular.  
C. Every infinite language is nonregular.  
D. Every regular language has exactly one pumping length.

### Q23. [1 Mark] [MSQ]

A deterministic Turing machine on a fixed input is forbidden to visit more than100 tape cells. Its finite state set and tape alphabet are known. Which statements are correct?

A. Whether it halts can be decided by simulating until halting or a repeated complete configuration.
B. Every such machine must halt.
C. Only finitely many complete configurations are possible on that input.
D. This establishes decidability of unrestricted Turing-machine halting.

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A memory allocator has two nonadjacent free holes of 40 bytes each, but no free hole of 60 bytes. A request needs a contiguous 60-byte block. What explains failure despite 80 free bytes in total?

A. External fragmentation.  
B. Internal fragmentation inside the requested block before it is allocated.  
C. A necessary arithmetic overflow.  
D. The existence of exactly two CPU cores.

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected connected graph has a unique minimum-weight edge e crossing a particular nontrivial cut. Which statements hold?

**Candidates**

**I.** Every MST contains e.

**II.** No MST can contain any other edge crossing that cut.

**III.** Adding e to an MST that omitted it would allow a strictly lighter crossing edge exchange, contradicting minimality.

**IV.** e must be a bridge in the original graph.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q26. [1 Mark] [NAT]

A memory has eight banks. Word address a maps to bank a modulo8. A program repeatedly accesses addresses3,9,15,21,... with stride6. How many distinct banks are visited before the bank sequence repeats?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

Let A=uvᵀ, where u=(1,2,−1)ᵀ and v=(2,0,3)ᵀ. What is the sum of the squares of A's three eigenvalues, counted with algebraic multiplicity?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

SQL table T(g,x) has rows (A,NULL),(A,NULL),(B,1),(B,NULL),(C,1),(C,1). How many groups are returned by this query under standard SQL NULL semantics?

```sql
SELECT g FROM T
GROUP BY g
HAVING COUNT(DISTINCT x)=1 AND COUNT(*)>COUNT(x);
```

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

Two balls are drawn without replacement from a bag containing two red and two blue balls. Let X and Y be the indicators that the first and second drawn balls, respectively, are red. Find Cov(X,Y), rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Events A,B have P(A)=0.8 and P(B)=0.7. Which additional specifications are individually consistent with these two probabilities?

**Candidates**

**I.** P(A∩B)=0.4

**II.** P(A∩B)=0.6

**III.** P(A|B)=0.5

**IV.** P(A∪B)=1

A. I and IV  
B. II and III  
C. III and IV  
D. II and IV

### Q31. [1 Mark] [MCQ]

In `t=a+b; c=d+e; u=a+b;`, variables a,b,c,d,e,t,u are distinct nonaliased scalars and arithmetic is exact. Which replacement is valid?

A. Replace the final a+b by t.
B. Replace the final a+b by c for all inputs.
C. Replace d+e by t for all inputs.
D. Delete the first assignment and leave u=t with no definition of t.

### Q32. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A TLB tags each translation by an address-space identifier (ASID) and a virtual page number. Processes P and Q have different ASIDs but may use the same virtual addresses. Which statements are correct?

**Candidates**

**I.** A translation for P need not be discarded merely because the CPU switches to Q.

**II.** The ASID alone identifies a physical page without the virtual page number.

**III.** Reusing P's ASID for an unrelated address space may require invalidating stale translations carrying that ASID.

**IV.** ASIDs eliminate the need to update a translation after its page-table mapping changes.

A. I and II  
B. I and IV  
C. II and III  
D. I and III

### Q33. [1 Mark] [NAT]

An unsigned fixed-point format uses six bits with a scale factor of 1/8: the stored unsigned integer k represents k/8. Addition wraps modulo 64 in the stored integer. What numerical value is stored after adding the encodings of 5.75 and 3.5?

**Answer format:** Exact decimal.

### Q34. [1 Mark] [NAT]

A fixed-length file uses unspanned records of 90 bytes and blocks of 512 bytes, with no headers. It currently contains 12 records packed into the fewest possible blocks. How many additional records can be inserted without allocating another block, if records may be rearranged within the allocated blocks?

**Answer format:** Exact integer.

### Q35. [1 Mark] [NAT]

A min-heap with distinct keys1 through7 is stored in an array indexed1 through7. The key7 is known to be at index2. How many such heaps exist?

**Answer format:** Exact integer.

### Q36. [2 Marks] [NAT]

A B+ tree has a root with two internal children. Each of those children has exactly three leaf children. Every leaf contains exactly four data entries. Internal separator copies are not data entries. How many data entries does the tree contain?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A directed graph has edges s→a(1), a→b(1), b→t(1), s→b(5), a→t(8), and s→t(10), with weights in parentheses. A route is allowed to use at most two edges. By how much does the cheapest permitted route exceed the unrestricted shortest-path distance from s to t?

**Answer format:** Exact integer.

### Q38. [2 Marks] [NAT]

A directed graph with four vertices has adjacency matrix A, where A[i,j] is the number of directed edges i→j. Its only edges are1→2,1→3,2→4,3→4,4→1, one of each. What is entry(1,1) of A³?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

An undirected network has edges AB=2, AC=7, BC=1, BD=6, CD=2. Node A's link-state database is complete and correct. The edge BC fails and is removed. By how much does the shortest-path distance from A to D increase after recomputation?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A processor services eight independent cache misses. Each miss takes100 cycles from issue to completion. It can issue at most one miss per cycle and have at most four outstanding misses. A slot freed by a completion can be reused in that same cycle. All misses are ready initially and are issued as early as permitted, starting in cycle0. In what cycle does the last miss complete?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A compiler represents a basic block as a DAG and merges identical pure expressions whose operand values are unchanged. Consider exact integers with distinct scalar variables and no aliases:

```text
t1 = a+b
t2 = a+b
a = t1+c
t3 = a+b
t4 = t2+c
```

How many distinct addition nodes are needed, including the value assigned to a?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

In a binary floating-point format with round-to-nearest, ties-to-even and finite precision, which statements are correct?

A. Addition is necessarily associative for all finite inputs whose computations stay finite.
B. Adding a sufficiently small positive number to a sufficiently large positive number can leave the stored result unchanged.
C. Cancellation of nearby numbers can reveal error already present in their approximations.
D. Every integer of arbitrary size is represented exactly.

### Q43. [2 Marks] [NAT]

A direct-mapped cache has four lines and one word per line. Word address w maps to line w mod4. Starting empty, it accesses words0,4,1,5,0,4,1,5. A fully associative cache of four lines, using LRU and starting empty, sees the same trace. How many misses in the direct-mapped cache are eliminated by the fully associative cache?

**Answer format:** Exact integer.

### Q44. [2 Marks] [MSQ]

Consider the positive divisors of 60, ordered by divisibility. The least and greatest elements are 1 and 60. A complement of d is a divisor e with meet(d,e)=1 and join(d,e)=60. Which statements are correct?

A. This partially ordered set is a lattice.  
B. Every element has a complement.  
C. Exactly eight elements have complements.  
D. The lattice is distributive.

### Q45. [2 Marks] [NAT]

A routing table contains only the following entries, plus a default route. For destinations in 10.0.0.0/24, how many addresses select interface A under longest-prefix matching?

```text
10.0.0.0/24     A
10.0.0.64/26    B
10.0.0.96/27    A
10.0.0.112/28   C
```

Count all addresses, without excluding network or broadcast addresses.

**Answer format:** Exact integer.

### Q46. [2 Marks] [NAT]

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

### Q47. [2 Marks] [NAT]

A paged process uses virtual addresses of16 bits with1024-byte pages. A valid page-table entry maps virtual page5 to physical frame12. What physical byte address corresponds to virtual byte address5500?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

A lexer recognizes identifiers `[a-z]+`, integers `[0-9]+`, the keyword `if`, and the single-character token `+`. It uses longest match; an exact tie between an identifier and the keyword is resolved in favour of the keyword. There is no rule requiring whitespace between tokens. How many tokens does it produce for `ifx12if+007`?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

Construct the usual predictive parsing table for grammar S→AB, A→aA | ε, B→bB | a, with start symbol S and end marker $. Count cells that contain more than one production; count a conflicting cell once regardless of how many productions it contains. How many such cells are there?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

A DFA over{a,b} has three states0,1,2, start0 and sole accepting state2. On a, transitions are0→1,1→2,2→2. On b, transitions are0→0,1→0,2→2. How many strings of length4 are accepted?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

The grammar S→(S)S | epsilon generates balanced parenthesis strings. How many distinct strings with four opening and four closing parentheses have maximum nesting depth exactly 2?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A DMA controller transfers a block of400 bytes over a shared bus. Each burst transfers20 bytes and holds the bus for5 cycles. Between consecutive bursts it releases the bus for3 cycles, during which the CPU may use it. The first burst begins at cycle0, and no gap follows the last burst. How many cycles elapse before DMA completes?

**Answer format:** Exact integer.

### Q53. [2 Marks] [NAT]

Matrix A has rows (0,1,1),(2,1,0),(4,3,2). Swap its first two rows to obtain PA, then compute PA=LU with unit diagonal L and no further row swaps. What is L₃₂?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A recursion on an input interval of length n returns immediately for n≤1. Otherwise it recursively processes the first floor(n/2) entries and then the remaining entries. For n=10, how many calls split their input into two parts of unequal lengths? Count separate calls, even when their input lengths are equal to one another.

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A pushdown machine starts with an empty stack. Reading a pushes one X. Reading b nondeterministically pops either one X or two X symbols; a move requiring unavailable symbols is disallowed. There are no other choices or epsilon moves. It accepts exactly when the entire input is consumed and the stack is empty. How many accepting computations exist on the input shown below? Spaces separate blocks for readability and are not input symbols.

```text
aa b a b aaaa bbb
```

Computations are distinct if their choices of one-symbol versus two-symbol pops differ.

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two transactions each increment the same data item x by reading it and later writing the incremented value. Both initially hold compatible shared locks on x and then request an upgrade to an exclusive lock without releasing their shared locks. A transaction retains every lock until commit. Which statement is correct?

A. The upgrades can deadlock even though retaining locks until commit prevents another transaction from reading an uncommitted write.  
B. The second upgrade must succeed because shared locks are compatible.  
C. Releasing each shared lock before requesting its exclusive lock always preserves two-phase locking.  
D. If both transactions instead request an exclusive lock before reading x and hold it until commit, a lost update remains possible in a completed execution.

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

After a successful fork, both processes execute `counter++`, where counter was an ordinary private global integer equal to 5 before fork. There is no shared-memory mapping. After both increments, what are their counter values?

A. Each process has value 6 in its own address space.  
B. Both necessarily observe a shared value 7.  
C. The child must have value 1.  
D. The parent must retain value 5.

### Q58. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Records have fields (department,score,id). A stable sorting routine is available. The desired order is department ascending, then score descending, preserving original order for records tied on both fields. Which procedures always achieve that order?

**Candidates**

**I.** Stable sort by score descending, then stable sort by department ascending.

**II.** Stable sort by department ascending, then stable sort by score descending.

**III.** One stable sort using the lexicographic key (department,negative score).

**IV.** First reverse the entire input, then use procedure A.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV

### Q59. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially X=Y=0. Transactions perform r1(X), r2(Y), w1(Y=1), w2(X=1), and then both commit. Each read sees the initial value. Which statement is correct?

A. The schedule is conflict serializable in order T1,T2.  
B. The schedule is conflict serializable in order T2,T1.  
C. The precedence graph has a cycle, and neither serial order reproduces both reads.  
D. No conflict exists because the writes target different items.

### Q60. [2 Marks] [NAT]

An expression node has synthesized attribute p, the parity of its integer value. Leaves provide their value modulo2. Addition combines child parities using XOR; multiplication combines them using AND. For expression (u+v)*(v+w)+u*w, how many of the eight assignments of parities to u,v,w make the root parity1?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

A real 3×3 matrix A satisfies A³=0 and A²≠0. Which statements must hold?

A. rank(A)=2.
B. rank(A²)=1.
C. A has an eigenvalue equal to 1.
D. (I−A)⁻¹=I+A+A².

### Q62. [2 Marks] [NAT]

An IPv4 packet with 4000 payload bytes and a 20-byte header crosses a link with MTU 1500. It is fragmented using the fewest fragments and the largest possible payload in each nonfinal fragment. What is the fragment-offset field of the final fragment? Offsets are in eight-byte units.

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A circuit is a two-to-one multiplexer with output F=(NOT s)a+sb. Its select line is tied to its own data input a, so s=a. Which statements are correct?

A. The resulting function is ab.  
B. When a=0, changing b changes F.  
C. The function can be implemented with one two-input NAND followed by one inverter.  
D. The resulting function is a OR b.

### Q64. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An initially empty hash table has slots 0 through 6. All inserted keys have primary hash 0. For each insertion, quadratic probing visits slots i² mod 7 for i=0,1,…,6, in that order, and reports failure if all these visits find occupied slots. There are no deletions. Which statements hold?

**Candidates**

**I.** The first four keys can all be inserted.

**II.** The fifth insertion succeeds because three slots are still empty.

**III.** No insertion ever examines slot 3.

**IV.** Replacing this probe rule by i mod 7 would have the same failure point.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q65. [2 Marks] [NAT]

Two disjoint groups each contain the same number of observations. Their means are2 and8, and their population variances are1 and9 respectively. What is the population variance of all observations combined?

**Answer format:** Exact number.

---

## ANSWER KEY — MOCK TEST 092

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 17 |
| 2 | NAT | 1 | 50 |
| 3 | MCQ | 1 | D |
| 4 | NAT | 1 | 9 |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 0.25 |
| 7 | MSQ | 2 | A, C, D |
| 8 | NAT | 2 | 15 |
| 9 | NAT | 2 | 47.73 (range 47.725–47.735) |
| 10 | NAT | 2 | 32 |
| 11 | NAT | 1 | 3 |
| 12 | MCQ | 1 | B |
| 13 | MCQ | 1 | C |
| 14 | NAT | 1 | 0 |
| 15 | MSQ | 1 | B, C |
| 16 | NAT | 1 | 14 |
| 17 | MSQ | 1 | A, D |
| 18 | MCQ | 1 | C |
| 19 | NAT | 1 | 3456 |
| 20 | NAT | 1 | 0.5 |
| 21 | NAT | 1 | 5 |
| 22 | MSQ | 1 | B, C, D |
| 23 | MSQ | 1 | A, C |
| 24 | MSQ | 1 | B, C, D |
| 25 | MCQ | 1 | D |
| 26 | NAT | 1 | 4 |
| 27 | NAT | 1 | 1 |
| 28 | NAT | 1 | 1 |
| 29 | NAT | 1 | -0.0833 (range -0.08335–-0.08325) |
| 30 | MCQ | 1 | D |
| 31 | MCQ | 1 | A |
| 32 | MCQ | 1 | D |
| 33 | NAT | 1 | 1.25 |
| 34 | NAT | 1 | 3 |
| 35 | NAT | 1 | 0 |
| 36 | NAT | 2 | 24 |
| 37 | NAT | 2 | 3 |
| 38 | NAT | 2 | 2 |
| 39 | NAT | 2 | 3 |
| 40 | NAT | 2 | 203 |
| 41 | NAT | 2 | 3 |
| 42 | MSQ | 2 | B, C |
| 43 | NAT | 2 | 4 |
| 44 | MSQ | 2 | A, C, D |
| 45 | NAT | 2 | 208 |
| 46 | NAT | 2 | 26 |
| 47 | NAT | 2 | 12668 |
| 48 | NAT | 2 | 5 |
| 49 | NAT | 2 | 1 |
| 50 | NAT | 2 | 8 |
| 51 | NAT | 2 | 7 (exact) |
| 52 | NAT | 2 | 157 |
| 53 | NAT | 2 | 1 |
| 54 | NAT | 2 | 4 |
| 55 | NAT | 2 | 9 (exact) |
| 56 | MSQ | 2 | B, C, D |
| 57 | MSQ | 2 | B, C, D |
| 58 | MCQ | 2 | A |
| 59 | MSQ | 2 | A, B, D |
| 60 | NAT | 2 | 2 |
| 61 | MSQ | 2 | A, B, D |
| 62 | NAT | 2 | 370 |
| 63 | MSQ | 2 | B, D |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 14 |
