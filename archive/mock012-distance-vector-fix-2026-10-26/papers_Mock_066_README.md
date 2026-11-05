# GATE CS 2027 — Full-Length Mock Test 066

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

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The two estimates are commensurate because both measure annual cost in the same currency; this does not mean they are equal.” Which meaning of “commensurate” fits this explanation?

A. Comparable on a common basis.  
B. Necessarily identical in magnitude.  
C. Deliberately misleading.  
D. Measured without units.

### Q2. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For positive numbers x and y, log2(x)+log2(y)=7 and log2(x/y)=3. What is x?

**Required precision:** Exact number.

A. 64  
B. 16  
C. 32  
D. 33

### Q3. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An inspector accepts or rejects cards using one of the four candidate rules below. Each card has one colour, one shape, and is either filled or hollow. Observations are:

| Colour | Shape | Appearance | Decision |
|---|---|---|---|
| Red | Circle | Filled | Reject |
| Red | Circle | Hollow | Accept |
| Red | Square | Filled | Accept |
| Blue | Circle | Filled | Reject |
| Blue | Circle | Hollow | Reject |

Which candidate rule agrees with every observation?

**Candidate answers**
I. Accept if the card is red and is either circular or filled, including when both hold.
II. Accept if the card is red and exactly one of “circular” and “filled” holds.
III. Accept if exactly one of “circular” and “filled” holds, regardless of colour.
IV. Accept if the card is red or circular, including when both hold.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A 2×5 rectangular board is tiled completely with identical 1×2 dominoes, with no overlaps. Exactly three dominoes are vertical, each covering an entire height-two column. How many distinct tilings satisfy this condition? Board positions are fixed; mirror images count separately when different.

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q5. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Let a(n) be the largest exponent k such that2^k divides n!. What is a(16)−a(15)?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q6. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An open cylindrical container has a horizontal base area100 square centimetres and initially contains water to depth5 cm. A solid cube of side4 cm is placed flat on the bottom without spilling water. Assuming the cube becomes fully submerged, what is the final water depth?

**Required precision:** Exact decimal in centimetres.

A. 11.28  
B. 2.82  
C. 6.64  
D. 5.64

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A policy says, “Unless a submission is anonymous, it must include the author's name.” Which submission violates this rule?

A. An anonymous submission without a name.  
B. A nonanonymous submission with a name.  
C. A nonanonymous submission without a name.  
D. An anonymous submission with a name.

### Q8. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A container initially holds10 litres of a mixture that is30% salt solution by volume, with the remaining volume water. Remove2 litres of the well-mixed contents and replace them with2 litres of pure water. Then remove5 litres of the newly mixed contents and replace them with5 litres of a60% salt solution. Assuming volumes add, what percentage of the final mixture is salt solution?

**Required precision:** Exact decimal percentage, without the % sign.

A. 42  
B. 84  
C. 21  
D. 43

### Q9. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Five distinct presentations A,B,C,D,E occupy five consecutive slots. A must precede B, B must precede C, and D must precede E. There are no other constraints. How many valid schedules exist?

**Required precision:** Integer.

A. 20  
B. 10  
C. 5  
D. 11

### Q10. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two distinct numbers are selected uniformly as an unordered pair from {1,2,3,4,5,6}. Given that their product is even, what is the probability that their sum is even?

**Required precision:** Exact finite decimal.

A. 0.75  
B. 0.13  
C. 0.63  
D. 0.25

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For real t let

```text
A(t) = [1  2  1]
       [2  t  3]
       [1  3  1].
```

Use Doolittle elimination, with unit diagonal in L and no row exchanges unless an option explicitly permits one. Which statements are correct?

**Candidates**

**I.** det(A(t))=-1 for every real t.

**II.** An unpivoted factorization A=LU with unit lower-triangular L exists for every real t.

**III.** At t=4, exchanging rows 2 and 3 after eliminating column 1 allows elimination to finish without a zero pivot.

**IV.** At t=5, the final diagonal entry U33 is 1.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II

### Q12. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be a context-free language over {a,b}. Define h(a)=01 and h(b)=epsilon. Let R be a regular language over {0,1}. Which languages must be context-free?

A. h(L)  
B. h(L) intersect R  
C. The complement of L over {a,b}*  
D. L intersect {a}*

### Q13. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed weighted graph has edges s→a(1), a→a(−1), s→t(5), and no others. Distances refer to walks, which may repeat vertices. Which statements are correct?

**Candidates**

**I.** There is a finite shortest-walk distance from s to t, equal to5.

**II.** Every vertex reachable from s has a finite shortest-walk distance.

**III.** A negative cycle reachable from s need not make the s-to-t distance unbounded below.

**IV.** The negative self-loop can be inserted into a walk from s to t.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An undirected simple graph with six vertices is stored in adjacency lists, with each undirected edge recorded at both endpoints. There are14 neighbour entries. Three vertices have degrees1,2,3. What is the sum of the degrees of the other three vertices?

**Required precision:** Integer.

A. 16  
B. 4  
C. 9  
D. 8

### Q15. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two1000-bit packets traverse a store-and-forward router. The incoming link transmits1000 bits/ms; the outgoing link transmits500 bits/ms. Both packets are ready at the source at time0, propagation is negligible, and the router starts forwarding a packet only after receiving it completely. At what time, in milliseconds, does the last bit of the second packet leave the router?

**Required precision:** Exact number.

A. 10  
B. 3  
C. 6  
D. 5

### Q16. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A process's page table marks page 5 as valid but not resident. The process reads page 5 with sufficient access permission. How many page faults are generated by this single memory access, assuming fault handling loads the page successfully and no other fault occurs?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q17. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An integrable real function on [0,1] satisfies f(x)+f(1−x)=x²+(1−x)² for every x in that interval. Evaluate ∫₀¹ f(x) dx, rounded to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.6667  
B. 0.1667  
C. 0.2500  
D. 0.3333

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process blocks on an empty pipe while another process can eventually write to it. Which statements are correct under ordinary blocking I/O semantics?

**Candidates**

**I.** The blocked process need not consume CPU time by busy-waiting.

**II.** Blocking on the pipe necessarily means the whole system is deadlocked.

**III.** A successful write may make the reader runnable.

**IV.** The reader must be executing continuously for the writer to write.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q19. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Five observations are 2,4,x,8,11, and their arithmetic mean is 6. What is their median?

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q20. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A foreign key Child.parent_id references Parent.id. It uses ON DELETE SET NULL, and Child.parent_id is also declared NOT NULL. A parent with a referencing child is deleted. Assume constraints are enforced immediately and no other action modifies the child. Which statements are correct?

**Candidate answers**
I. The referential action would require setting the child's foreign key to NULL.
II. The deletion can violate the child's NOT NULL constraint and be rejected.
III. SET NULL silently overrides every NOT NULL constraint.
IV. The child row must necessarily be deleted instead.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: valid; II: valid; III: valid; IV: invalid  
D. I: invalid; II: invalid; III: valid; IV: valid

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

In C, `int x=3; int *p=&x; *p=*p+4;` is executed. What is the value of x afterwards?

**Required precision:** Integer.

A. 14  
B. 4  
C. 7  
D. 8

### Q22. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Insertion sort is run on keys `[3a, 1, 3b, 2, 3c]`, where 3a, 3b and 3c have equal numeric key 3 and the suffixes only identify records. The usual inner loop shifts a preceding record while its key is strictly greater than the key being inserted. A modified version shifts while it is greater than or equal. Count only shifts of preceding records one position to the right, not final placements of the inserted record. How many additional shifts does the modified version perform?

A. 6  
B. 3  
C. 2  
D. 4

### Q23. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

How many group homomorphisms exist from the additive group Z12 to the additive group Z18?

**Required precision:** Integer.

A. 6  
B. 12  
C. 3  
D. 7

### Q24. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A binary floating-point format has three significant bits including the leading one, sufficient exponent range, and round-to-nearest with ties-to-even. Starting from the exactly represented value 1, add the exact real number 0.125 twice, rounding after each addition. What is the exact real sum minus the final stored value?

**Required precision:** Exact finite decimal.

A. 0.25  
B. 0.75  
C. 0.13  
D. 0.63

### Q25. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Two threads use a mutex to protect a counter. The counter is initialized once before either starts. Each thread locks, reads, increments, writes and unlocks exactly once. Which statements are correct under ordinary correct mutex semantics?

**Candidate answers**
I. The two increment regions cannot overlap.
II. The final value is the initial value plus2.
III. The mutex by itself specifies which thread increments first.
IV. Removing the lock but retaining the unlock preserves the synchronization guarantee.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: valid; IV: valid  
D. I: valid; II: valid; III: invalid; IV: invalid

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Four NAND gates are connected as t=NAND(a,b), u=NAND(a,t), v=NAND(b,t), y=NAND(u,v). Out of the four possible input assignments to a,b, on how many does y differ from OR(a,b)?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two identical resource instances exist. P holds one and Q holds the other; each waits for one additional instance and neither releases before obtaining it. There are no other processes. Which statements are correct?

**Candidates**

**I.** Both processes are blocked indefinitely under these rules.

**II.** Having multiple instances makes deadlock impossible.

**III.** Releasing one held instance could permit one process to finish, if that change were allowed.

**IV.** Each process already holds enough instances to satisfy its outstanding request without any release.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A DMA controller transfers a block of64 bytes using eight-byte bus transactions. After every two DMA transactions it relinquishes the bus, except that it finishes immediately after its last transaction. How many relinquishments occur before transfer completion?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q29. [1 Mark] [NAT]

A machine fetches a 32-bit instruction using a 16-bit-wide memory interface. Each memory transfer takes one cycle and provides two adjacent bytes. The instruction is aligned to a two-byte boundary, and no overlapping or caching occurs. How many cycles are required to fetch it?

**Answer format:** Integer.

### Q30. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

SQL table T(g,x) has rows (A,NULL),(A,NULL),(B,1),(B,NULL),(C,1),(C,1). How many groups are returned by this query under standard SQL NULL semantics?

```sql
SELECT g FROM T
GROUP BY g
HAVING COUNT(DISTINCT x)=1 AND COUNT(*)>COUNT(x);
```

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Take two vertex-disjoint triangles and add one edge joining a vertex of one triangle to a vertex of the other. What is the minimum number of edges whose removal makes the resulting graph bipartite?

**Required precision:** Exact integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

To use the pumping lemma for context-free languages to prove non-context-freeness, a proof must handle which choice of decomposition w=uvxyz?

A. Only the lexicographically first decomposition.  
B. Every decomposition satisfying |vxy|≤p and |vy|>0, after choosing a suitable w with |w|≥p.  
C. Only decompositions with v=y=ε.  
D. No decomposition, because choosing a long word is sufficient.

### Q33. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A recursive routine visits a binary tree as follows. A null pointer returns immediately; a non-null call invokes the routine on both children, even when a child pointer is null. If the tree has 12 non-null vertices, how many calls receive a null pointer?

**Required precision:** Exact integer.

A. 26  
B. 7  
C. 14  
D. 13

### Q34. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexical analyzer distinguishes an identifier token from a symbol-table entry. Which statement is correct?

A. Every occurrence of the same identifier spelling must create a permanently distinct name entry regardless of scope or implementation.  
B. Token recognition and name binding are different tasks; returning an identifier token does not alone determine which declaration it denotes.  
C. Recognizing a token proves that the entire program is type-correct.  
D. Whitespace must always be emitted as an identifier token.

### Q35. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

For the grammar below, construct the standard LL(1) predictive parsing table using FIRST and FOLLOW sets. A conflicting entry means a single table cell containing two or more distinct productions. Count conflicting cells, not pairs of productions. The start symbol is S and the end marker is $.

```text
S -> A a | b
A -> a A | B
B -> b B | epsilon
```

How many table cells conflict?

A. 4  
B. 1  
C. 2  
D. 3

### Q36. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A transaction reads row x twice. Another transaction commits a change to x between the reads. Which statements are correct?

**Candidates**

**I.** If the first transaction observes different committed values, this is a nonrepeatable read.

**II.** Such an observation necessarily means the first read saw uncommitted data.

**III.** Holding an appropriate shared lock on x throughout both reads prevents an intervening conflicting exclusive write lock under ordinary locking rules.

**IV.** A nonrepeatable read necessarily involves inserting a new row rather than updating x.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q37. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An array of eight distinct values is reordered in place by exchanging entries whose indices are reversals of each other's three-bit binary representation. Indices range0–7. Each unequal pair is exchanged once, and equal-index pairs are untouched. How many swaps occur?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q38. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

In a singly linked structure, head reaches a path of length3 edges before first entering a cycle of length4. Floyd's algorithm starts slow and fast at head and, in each iteration, advances slow by one edge and fast by two, then compares them. How many iterations occur before the first equality?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q39. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A single CPU uses round-robin scheduling with quantum 2 and zero switching overhead. Processes A,B,C have (arrival,burst) values (0,5),(1,4),(2,2). At a quantum boundary, new arrivals join the ready queue before the preempted running process is requeued. A process whose burst finishes is not requeued. What is the mean waiting time?

**Required precision:** Decimal rounded to two places.

A. 8.66  
B. 4.33  
C. 2.17  
D. 5.33

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relations Candidate(x)={a,b}, Required(y)=empty, and Completed(x,y)=empty use set semantics. The desired query returns candidates who have completed every required item. Which statements are correct?

**Candidates**

**I.** The result is empty because Completed is empty.

**II.** The result is {a,b} by vacuous truth.

**III.** For each candidate, testing that no required item lacks a matching Completed tuple implements the desired condition.

**IV.** Replacing the outer Candidate relation by the x-projection of Completed preserves the result for this instance.

A. II and III  
B. I and III  
C. I and IV  
D. II and IV

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Independent coin tosses alternate between two coins: odd-numbered tosses have P(H)=1/2 and even-numbered tosses have P(H)=1/4. Tossing starts at toss 1 and stops immediately when two consecutive heads first occur. What is the expected number of tosses? Round to three decimal places.

**Required precision:** Number to 3 decimal places.

A. 22.546  
B. 5.637  
C. 11.273  
D. 12.273

### Q42. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An ordered sequence consists of steps of size 1 or 3 whose sum is 8. How many such sequences contain an even number of size-3 steps, including zero?

**Required precision:** Integer.

A. 14  
B. 7  
C. 4  
D. 8

### Q43. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A translator scans a binary string left to right, maintaining attributes v and p, initially 0 and 1. On reading bit b, it simultaneously sets v_new=v+b*p and p_new=2*p. What final v results from input 10110?

**Required precision:** Integer.

A. 26  
B. 13  
C. 7  
D. 14

### Q44. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An eight-bit signed two's-complement fixed-point word has four fractional bits and represents −1.375. Convert it to a format with two fractional bits by an arithmetic right shift of its signed raw integer by two positions, defined to round toward negative infinity. Compare the represented result with conversion obtained by dividing the raw integer by four and truncating toward zero. What is the absolute difference of the two represented real values?

**Required precision:** Exact finite decimal.

A. 0.25  
B. 0.75  
C. 0.13  
D. 0.63

### Q45. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A toy binary floating-point system has precision 3 significant bits, unbounded exponents, and rounding to nearest with ties to even. Every addition is rounded immediately. Let a=8, b=1, c=1. What is the numerical value of (a+(b+c))−((a+b)+c), where the final subtraction is evaluated exactly on the two already rounded results?

**Required precision:** Exact integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q46. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Routers A,B,C form a triangle with all three link costs 1. A also has a cost-1 link to destination D. Initially their distances to D are (1,2,2). The A–D link fails. They then run synchronous distance-vector rounds without split horizon or poison reverse. In each round every router computes its new distance using neighbours' distances from the preceding round; A cannot use its failed direct link. The first round uses the stated initial distances. What is the sum of A,B,C's distances after the second round?

**Required precision:** Integer.

A. 18  
B. 5  
C. 9  
D. 10

### Q47. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A chained hash table has three buckets containing respectively 1,2,3 distinct keys. All six keys are equally likely targets of a successful search, and each chain is searched from its head. What is the expected number of key comparisons? Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 3.3334  
B. 0.8334  
C. 2.6667  
D. 1.6667

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Procedure P lexically contains Q and S; Q lexically contains R. During execution P calls S, S calls Q, and Q calls R. There is no recursion. Each frame has a static link to its lexical parent's active frame and a dynamic link to its caller. Starting at R's frame, how many more dynamic-link traversals than static-link traversals are needed to reach P's frame?

**Required precision:** Exact integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q49. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The domain is a nonempty set and R is a binary relation. Which implications are valid for every interpretation?

**Candidates**

**I.** (∃y∀x R(x,y)) → (∀x∃y R(x,y))

**II.** (∀x∃y R(x,y)) → (∃y∀x R(x,y))

**III.** (∀x∀y R(x,y)) → (∃y∀x R(x,y))

**IV.** (∃x∃y R(x,y)) → (∀x∃y R(x,y))

A. II and IV  
B. I and III  
C. III and IV  
D. I and II

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A Turing machine M is promised to halt on every input. A proposed procedure enumerates input strings and simulates M on each until it finds an accepted input. Which statements are correct?

**Candidates**

**I.** If L(M) is nonempty, this sequential procedure eventually finds an accepted input.

**II.** If L(M) is empty, the procedure eventually proves emptiness just by reaching a sufficiently long rejected input.

**III.** Totality of M makes each individual simulation finish.

**IV.** The promise supplies a finite maximum length beyond which no new accepted input can occur.

A. I and II  
B. I and IV  
C. II and III  
D. I and III

### Q51. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A disk head moves at one cylinder per time unit, initially at0. It begins serving a request at100 nonpreemptively. At time10, a new request at20 arrives. Once the first request completes, it serves the new request directly. At what time does the request at20 complete?

**Required precision:** Integer.

A. 360  
B. 90  
C. 181  
D. 180

### Q52. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Relation R(A,B,C,D) has dependencies A→B, B→A and C→D, with no additional independent dependencies. Which statements are true?

**Candidate answers**
I. AC and BC are exactly its candidate keys.
II. R is already in BCNF.
III. Decomposition into AB, CD and AC is lossless and preserves all the given dependencies.
IV. Decomposition into AB and CD alone is guaranteed lossless.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q53. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Evaluate `(P && Q) || R` by left-to-right short-circuit rules, where P,Q,R are Boolean comparisons with no side effects. Among the eight possible assignments of truth values to P,Q,R, how many cause exactly two of the three comparisons to be evaluated?

**Required precision:** Integer.

A. 6  
B. 12  
C. 3  
D. 7

### Q54. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An IPv4 receiver reassembles fragments using the tuple(source address,destination address,protocol,identification). Two fragments have the same identification value but different source addresses. Which statements are correct under this rule?

**Candidate answers**
I. They belong to different reassembly contexts.
II. Equal identification values alone are sufficient to combine them.
III. The fragment offset determines placement within a context rather than replacing the context key.
IV. Arrival order alone uniquely identifies which datagram each fragment belongs to.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q55. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A segmented memory uses separate base and limit values for each segment. A byte access of length L at offset o is valid iff o≥0 and o+L≤limit. Segment2 has base1000 and limit100. A four-byte word is requested at offset98. How many bytes from the requested word can the processor access before trapping if the whole access is checked atomically before any memory read?

**Required precision:** Exact integer.

A. 0  
B. 1  
C. 2  
D. 3

### Q56. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For regular expressions over {a,b}, which identities hold as language equalities, with ε denoting the empty word?

**Candidates**

**I.** (a*)*=a*

**II.** (a|b)*=a*b*

**III.** εa=a

**IV.** (ab)*=a*b*

A. II and IV  
B. III and IV  
C. I and III  
D. I and II

### Q57. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let M have rows (2,1,0),(1,1,1),(0,1,2). For arbitrary b=(b1,b2,b3)ᵀ, consider Mx=b over the real numbers. Which statements are correct?

A. M has rank 2.  
B. The null space is spanned by (1,−2,1)ᵀ.  
C. Mx=b is consistent exactly when b1−2b2+b3=0.  
D. Every consistent system Mx=b has a unique solution.

### Q58. [2 Marks] [NAT]

Independent unbiased bits a,b,c are supplied to two Boolean circuits. One computes F=(a OR b) AND (a OR c). The other computes G=(a AND b) OR (a AND c). What is the probability that their outputs differ?

**Answer format:** Exact decimal.

### Q59. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A grammar has S→ABA, A→a | ε, B→b | ε. When eliminating epsilon productions, form S's nonempty right-hand sides by independently retaining or omitting nullable occurrences in ABA, then remove duplicate right-hand sides. How many distinct nonempty right-hand sides result for S?

**Required precision:** Integer.

A. 12  
B. 3  
C. 7  
D. 6

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

External merge sort handles a file of 17 disk blocks using three buffer blocks. Initial run generation sorts up to three blocks at a time. Each later merge pass uses two input buffers and one output buffer. Every pass, including initial generation and the final merge, reads and writes all 17 blocks; no pass is fused or streamed away. How many total block transfers occur?

**Required precision:** Integer reads plus writes.

A. 272  
B. 136  
C. 68  
D. 137

### Q62. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Three jobs have deadlines and profits(d,p): A=(1,20), B=(2,15), C=(2,10). Every job takes one unit of time, only one runs at a time, time slots finish at1 and2, and a profit is earned only if the job finishes by its deadline. What is the maximum total profit?

**Required precision:** Integer.

A. 70  
B. 18  
C. 36  
D. 35

### Q63. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Six independent multiplication operations feed six additions into a running accumulator, in multiplication order. A multiply takes three cycles; an add takes one cycle, and an add may begin when its multiply and the previous accumulator add have finished. Different functional units overlap. Multiplications start as early as the multiplier permits, beginning at time zero. Compare a pipelined multiplier accepting a new operation every cycle with an unpipelined multiplier accepting one every three cycles. How many cycles earlier does the sixth addition finish in the pipelined design?

**Required precision:** Integer.

A. 20  
B. 10  
C. 5  
D. 11

### Q64. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An instruction uses base-plus-scaled-index addressing: address=base+4×index+signed displacement. The base register holds 1000, the index holds 7, and the eight-bit displacement field is 11111000₂. What byte address is computed?

**Required precision:** Integer.

A. 1020  
B. 2040  
C. 510  
D. 1021

### Q65. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A queue is implemented using two stacks. Enqueue pushes onto input stack I. Dequeue pops from output stack O; if O is empty, it first transfers every element of I to O, one pop and one push per transferred element. Starting empty, execute enqueue(a), enqueue(b), dequeue, enqueue(c), dequeue, dequeue. How many primitive stack pushes and pops are performed in total?

**Required precision:** Exact integer.

A. 24  
B. 6  
C. 12  
D. 13

## ANSWER KEY — MOCK TEST 066

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | MSQ | 1 | A, B, D |
| 3 | MCQ | 1 | A |
| 4 | MCQ | 1 | B |
| 5 | MSQ | 1 | B, C, D |
| 6 | MSQ | 2 | A, B, C |
| 7 | MSQ | 2 | A, B, D |
| 8 | MSQ | 2 | B, C, D |
| 9 | MCQ | 2 | B |
| 10 | MSQ | 2 | A, B, C |
| 11 | MCQ | 1 | A |
| 12 | MCQ | 1 | C |
| 13 | MCQ | 1 | B |
| 14 | MCQ | 1 | D |
| 15 | MSQ | 1 | A, B, C |
| 16 | MCQ | 1 | D |
| 17 | MSQ | 1 | A, B, C |
| 18 | MCQ | 1 | B |
| 19 | MSQ | 1 | A, B, D |
| 20 | MCQ | 1 | A |
| 21 | MCQ | 1 | C |
| 22 | MCQ | 1 | B |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 1 | B, C, D |
| 25 | MCQ | 1 | D |
| 26 | MCQ | 1 | A |
| 27 | MCQ | 1 | A |
| 28 | MCQ | 1 | D |
| 29 | NAT | 1 | 2 |
| 30 | MSQ | 1 | B, C, D |
| 31 | MCQ | 1 | C |
| 32 | MSQ | 1 | A, C, D |
| 33 | MSQ | 1 | A, B, C |
| 34 | MSQ | 1 | A, C, D |
| 35 | MCQ | 1 | C |
| 36 | MCQ | 2 | D |
| 37 | MSQ | 2 | B, C, D |
| 38 | MSQ | 2 | A, B, C |
| 39 | MSQ | 2 | A, C, D |
| 40 | MCQ | 2 | A |
| 41 | MSQ | 2 | A, B, D |
| 42 | MSQ | 2 | A, C, D |
| 43 | MCQ | 2 | B |
| 44 | MCQ | 2 | A |
| 45 | MSQ | 2 | A, B, D |
| 46 | MSQ | 2 | A, B, D |
| 47 | MSQ | 2 | A, B, C |
| 48 | MCQ | 2 | D |
| 49 | MCQ | 2 | B |
| 50 | MCQ | 2 | D |
| 51 | MCQ | 2 | D |
| 52 | MCQ | 2 | D |
| 53 | MSQ | 2 | B, C, D |
| 54 | MCQ | 2 | C |
| 55 | MSQ | 2 | B, C, D |
| 56 | MCQ | 2 | C |
| 57 | MCQ | 2 | D |
| 58 | NAT | 2 | 0.25 |
| 59 | MSQ | 2 | A, B, C |
| 60 | MSQ | 2 | A, C, D |
| 61 | MCQ | 2 | B |
| 62 | MCQ | 2 | D |
| 63 | MSQ | 2 | A, C, D |
| 64 | MSQ | 2 | B, C, D |
| 65 | MCQ | 2 | C |
