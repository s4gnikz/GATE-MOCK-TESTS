# GATE CS 2027 — Full-Length Mock Test 058

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

“The panel's endorsement was qualified: it supported the proposal provided that the drainage plan was revised.” Here, “qualified” most nearly means:

A. Issued by technically trained people.  
B. Unreserved.  
C. Subject to a condition.  
D. Withdrawn completely.

### Q2. [1 Mark] [NAT]

How many integers n with1≤n≤100 satisfy floor(log2 n)=floor(log3 n)? Here floor rounds downward to an integer.

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A report states: “Every approved application was received before the deadline. Several applications received before the deadline were rejected.” Which inference is justified?

A. Receiving an application before the deadline guarantees approval.  
B. Every rejected application arrived after the deadline.  
C. No application was approved.  
D. Timely receipt was necessary but not sufficient for approval in this set of applications.

### Q4. [1 Mark] [NAT]

The central unit square is removed from a3×3 board of unit squares. How many tilings of the remaining eight squares by1×2 dominoes exist? Rotations and reflections of a tiling count as different if the occupied domino pairs differ.

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A numerical sequence begins a1=2 and a2=5. For every integer n>=3, its rule is a_n=2*a_(n-1)-a_(n-2)+n. What is a5-a4?

**Answer format:** Numeric value; integer.

### Q6. [2 Marks] [NAT]

Two filled, axis-aligned squares have coordinate ranges[0,4]×[0,4] and[1,5]×[2,6]. What is the perimeter of their union, counting only its outer boundary?

**Answer format:** Integer length units.

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that most clearly expresses both stated facts without a misplaced modifier: the researcher analyzed the samples, and the samples—not the researcher—had been stored overnight.

A. Stored overnight, the researcher analyzed the samples.  
B. The researcher analyzed the samples that had been stored overnight.  
C. Analyzing the researcher, the samples had been stored overnight.  
D. The researcher, which had been stored overnight, analyzed the samples.

### Q8. [2 Marks] [NAT]

A shop expects unit sales to fall by 20% from last month. This month every item will also be sold at a 10% discount on its new sticker price; last month all items sold at their old sticker price. All items have the same price within each month. What percentage increase in sticker price is required to keep sales revenue unchanged? Round to two decimal places.

**Answer format:** Number to 2 decimal places, without the percent sign.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Each of four people is either a truth-teller, whose statement below is true, or a liar, whose statement is false. A says “B is a liar.” B says “C is a liar.” C says “D is a liar.” D says “A and B are both truth-tellers.” Which pair consists exactly of the truth-tellers?

A. A,B  
B. A,C  
C. B,D  
D. C,D

### Q10. [2 Marks] [NAT]

A point is reflected across the vertical line x=1, and the reflected point is then rotated90 degrees counterclockwise about the origin. The final point is(−3,−2). What was the original point's distance from the origin?

**Answer format:** Exact number.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A byte-addressed 16-bit address bus interfaces an 8 KiB memory chip. Chip inputs A0 through A12 connect to the corresponding bus lines. The chip is selected exactly when A15=1 and A14=0; A13 is not decoded. How many distinct CPU byte addresses access the same physical byte of this chip?

**Answer format:** Exact integer.

### Q12. [1 Mark] [MCQ]

Let L={aⁿbⁿ:n≥0}. Which of the following is regular?

A. L
B. L∩a*b*
C. L∩a*b³
D. {a,b}* minus L

### Q13. [1 Mark] [MCQ]

Router A reaches destination D through neighbour B at total cost 5; A also has a direct link to D of cost 8. A currently selects B as next hop. With poisoned reverse, what distance to D does A advertise to B for this selected route?

A. 5
B. 8
C. Infinity
D. The cost of A's link to B only

### Q14. [1 Mark] [MCQ]

Records initially occur as (a,2),(b,1),(a,1),(b,2), where the first component is a letter key and the second a numeric key. First stably sort by the letter in ascending order, and then stably sort by the number in ascending order. What is the final sequence?

A. (a,1),(a,2),(b,1),(b,2)
B. (b,1),(a,1),(a,2),(b,2)
C. (a,1),(b,1),(a,2),(b,2)
D. (b,1),(a,1),(b,2),(a,2)

### Q15. [1 Mark] [NAT]

A is a 3×3 real matrix with determinant 2. Form B by interchanging its first two rows and then multiplying its third column by −3. What is det(2B)?

**Answer format:** Exact integer.

### Q16. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Input consists of a deterministic Turing machine M, a string w, and a nonnegative integer k in binary. Which tasks are decidable?

**Candidates**

**I.** Determine whether M accepts w within k transitions.

**II.** Determine whether M ever accepts w, with no time bound.

**III.** Determine whether M visits more than k distinct tape cells during its first k transitions.

**IV.** Determine whether M halts on every input.

A. I and III  
B. I and II  
C. I and IV  
D. II and III

### Q17. [1 Mark] [MCQ]

A JK flip-flop is initially 0. Across four successive active clock edges, its (J,K) inputs are (1,0),(1,1),(0,0),(0,1). What are the four successive output values?

A. 1,0,0,0
B. 1,1,1,0
C. 0,1,1,0
D. 1,0,1,0

### Q18. [1 Mark] [MSQ]

Every memory access first spends 1 ns at L1. An L1 miss spends an additional 9 ns at L2; an L2 miss spends another 90 ns at memory. The L1 hit probability is 0.8, and the L2 hit probability conditional on an L1 miss is 0.5. Which statements are correct?

A. The probability of an L1 miss followed by an L2 hit is 0.1.  
B. The probability of accessing main memory is 0.1.  
C. The average access time is 11.8 ns.  
D. Half of all original accesses are L2 hits.

### Q19. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An IPv4 fragment has offset field 100, 400 payload bytes, and MF=1. A downstream link permits only 200 payload bytes per fragment; 200 is divisible by eight. The router splits this fragment into two. Which statements are correct?

A. Their offset fields are 100 and 125.  
B. Both resulting fragments have MF=1.  
C. Both retain the original datagram's identification value.  
D. Their offsets must restart from zero because they were produced by a different router.

### Q20. [1 Mark] [NAT]

Starting with an empty stack, process tokens `5 2 - 3 *` as a postfix arithmetic expression, with binary operators popping the right operand first. What value remains?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A directed acyclic graph on A,B,C,D has edges A→C, B→C, B→D and no others. How many topological orderings does it have?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

Evaluate the limit as n tends to infinity of Σ(k=1 to n) n/(n²+k²). Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q23. [1 Mark] [NAT]

A nonnegative integer-valued random variable X satisfies P(X=0)=1/2, P(X=1)=1/4 and P(X=2)=1/4. What is Var(X)?

**Answer format:** Exact decimal.

### Q24. [1 Mark] [NAT]

During merge-based inversion counting, the sorted left half is[2,5,7] and the sorted right half is[1,5,6]. An inversion is a pair of positions i<j with value[i]>value[j], strictly. How many cross-half inversions are counted at this merge?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

An eight-bit two's-complement fixed-point value has three fractional bits and raw bit pattern11110100. What real value does it represent?

**Answer format:** Exact decimal.

### Q26. [1 Mark] [NAT]

An undirected tree has edges1–2,1–3,2–4,2–5,3–6. Root the tree at vertex4. What is the label of the lowest common ancestor of vertices5 and6?

**Answer format:** Integer vertex label.

### Q27. [1 Mark] [MCQ]

An out-of-order processor retires instructions in program order. Stores may execute speculatively but do not modify architecturally visible memory until retirement. Why is this restriction useful for precise exceptions?

A. It ensures a younger store cannot become visible before an older faulting instruction is handled.
B. It makes every load take one cycle.
C. It eliminates all data dependencies.
D. It guarantees that speculative branches are always predicted correctly.

### Q28. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For relation R(A,B,C), the functional dependencies are exactly those implied by AB→C and C→A. Which attribute sets are candidate keys?

**Candidates**

**I.** AB

**II.** AC

**III.** BC

**IV.** C

A. I and III  
B. III and IV  
C. I and II  
D. I and IV

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An LL(1) parser is built for S→A b, A→a A | ε. The stack top is A and lookahead is b. Which action is correct?

A. Consume b and retain A on the stack.  
B. Apply A→ε without consuming input.  
C. Apply A→aA.  
D. Report an error because b is not in FIRST(aA).

### Q30. [1 Mark] [NAT]

Table T(x) contains 2,2,NULL,5. What is the result of `SELECT COUNT(DISTINCT x) FROM T`?

**Answer format:** Integer.

### Q31. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two processes share a memory segment containing a counter initialized to0. Each performs one ordinary non-atomic read-increment-write operation. Which statements are correct without synchronization?

**Candidates**

**I.** A final value of1 is possible.

**II.** A final value of2 is possible.

**III.** Shared memory automatically makes each read-increment-write atomic.

**IV.** A final value of3 is possible from these two operations alone.

A. I and IV  
B. II and III  
C. I and II  
D. II and IV

### Q32. [1 Mark] [NAT]

Let R={(1,2),(2,3),(3,1)}. Its composition R∘R contains (x,z) when some y satisfies (x,y)∈R and (y,z)∈R. How many pairs belong to R∩(R∘R)?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

A real2×2 matrix A has trace5 and determinant6. What is trace(A²)?

**Answer format:** Exact integer.

### Q34. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A mutex is held while a thread updates two fields that jointly maintain an invariant. Why can protecting only the first field's assignment be insufficient?

A. Another thread may observe the intermediate inconsistent pair before the second assignment.  
B. A mutex can protect only constant variables.  
C. Two fields always update atomically without synchronization.  
D. Locking necessarily prevents either assignment from executing.

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

All operands below are unsigned n-bit integers, and operations wrap modulo2^n. Evaluating operands has no side effects. Which rewrites preserve both definedness and value for every input? Division by zero is undefined.

**Candidates**

**I.** x*(y+z) to x*y+x*z

**II.** x/x to1, including when x=0

**III.** x*0 to0

**IV.** x−y to y−x for every n≥2

A. II and III  
B. I and III  
C. II and IV  
D. III and IV

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The following schema uses immediate constraint checking after each SQL statement. The database initially contains Parent ids 1 and 2, and Child rows (10,1), (11,2), (12,NULL).
```sql
CREATE TABLE Parent (id INTEGER PRIMARY KEY);
CREATE TABLE Child (
    id INTEGER PRIMARY KEY,
    pid INTEGER,
    FOREIGN KEY (pid) REFERENCES Parent(id)
        ON DELETE SET NULL ON UPDATE CASCADE
);
```
Each proposed operation below is considered independently from this initial state. Which statements are correct?

A. Deleting Parent row id=1 succeeds and leaves Child row id=10 with pid=NULL.  
B. Updating Parent id=2 to id=3 succeeds and changes Child row id=11 to pid=3.  
C. Inserting Child row (13,NULL) violates the foreign-key constraint because no Parent id is NULL.  
D. Updating Parent id=1 to id=2 fails even though ON UPDATE CASCADE is specified.

### Q37. [2 Marks] [NAT]

A directed graph has edges a→b,b→a,b→c,c→d,d→c,d→e and isolated vertex f. How many strongly connected components have no outgoing edge to a different component?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

Over alphabet {a,b}, consider the language of strings with an even number of a's whose last symbol is b. The empty string is not in the language. What is the minimum number of states in a complete DFA recognizing it?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

A BST stores keys 1–15 in a perfectly balanced shape: root 8, recursively choosing the midpoint as each subtree root. Run this range-search procedure with lo=6, hi=10. Count non-null calls, including calls on nodes whose keys are not reported.

```text
search(node):
    if node is null: return
    if node.key > lo: search(node.left)
    if lo <= node.key <= hi: report(node.key)
    if node.key < hi: search(node.right)
```

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A toy normalized binary floating-point system has four significant bits, including the leading 1, and exponents large enough to avoid overflow and underflow. Each addition is rounded to nearest, ties to even. Let a=16, b=1, c=−16. What is the value of (a⊕b)⊕c, where ⊕ denotes a rounded addition?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

What is the maximum value of x²(1−x) for0≤x≤1? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q42. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A Banker's-algorithm system has two resource types. Current available resources are (1,1). Allocation and remaining need are:

| Process | Allocation | Remaining need |
|---|---|---|
| P0 | (1,0) | (1,2) |
| P1 | (0,1) | (2,0) |
| P2 | (1,1) | (1,1) |

Consider each request independently from the displayed state. Which statements are correct?

A. The current state has exactly two safe process-completion orders.  
B. Granting P0's request (1,0) would make the state unsafe.  
C. Granting P1's request (1,0) leaves a safe state.  
D. Granting P2's request (1,0) leaves a safe state.

### Q43. [2 Marks] [NAT]

An undirected graph consists of the four-cycle a–b–c–d–a and diagonal a–c. Every edge has weight one. How many distinct minimum spanning trees does it have?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

For Boolean variables x,y,z, define F=(x XOR y) AND (y XOR z). How many input triples make F=1?

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

A two-way set-associative cache has two sets and one block per way. Block b maps to set b modulo2, and each set uses LRU replacement. Starting empty, access blocks0,2,1,0,4,2,1. How many misses occur?

**Answer format:** Integer.

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler analyzes the loop below using a non-relational constant lattice, meeting different constants as “nonconstant.” It does not unroll the loop or track relationships between variables. Input n is an arbitrary nonnegative integer.

```text
x=0; y=0;
repeat n times:
    x=x+1;
    y=y+1;
z=x-y;
```

Which statements hold?

**Candidates**

**I.** Concrete execution always sets z=0.

**II.** The stated abstraction necessarily retains x=y at the loop exit.

**III.** Joining the entry values with the first-iteration values makes both x and y nonconstant.

**IV.** The program can set z=1 for some nonnegative n.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q47. [2 Marks] [NAT]

A prize is equally likely to be in boxes A,B,C. A contestant selects A. A knowledgeable host opens an unselected empty box: if the prize is in A, the host opens B with probability 1/4 and C with probability 3/4; if the prize is elsewhere, the host opens the only empty unselected box. Given that the host opens B, what is the probability that switching to C wins?

**Answer format:** Exact finite decimal.

### Q48. [2 Marks] [NAT]

Processor A has a 1 ns clock and base CPI 1. Loads constitute 30% of instructions, and 10% of loads incur a 20-cycle penalty in addition to base execution. Processor B halves the load-miss probability, retains base CPI 1 and the 20-cycle penalty, but may have a longer clock period. Penalties do not overlap and there are no other stalls. What is the largest clock period for B, in ns, for which its mean instruction time is no greater than A's? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q49. [2 Marks] [NAT]

A single CPU uses nonpreemptive shortest-job-first scheduling. At each completion it chooses the ready process with the smallest CPU burst. Processes are A(arrival0,burst5), B(1,2), C(2,1), D(6,1). Ties use earlier arrival. There is no context-switch overhead. What is the average waiting time of the four processes?

**Answer format:** Exact decimal in time units.

### Q50. [2 Marks] [MSQ]

Relation R(X,Y,Z) has functional dependencies XY→Z and Z→Y. It is decomposed into R1(X,Z) and R2(Z,Y), using their projected dependencies. Which statements are correct?

A. The decomposition is lossless.
B. The decomposition preserves XY→Z through the projected dependencies alone.
C. Both components are in BCNF.
D. Z is necessarily a key of the original R.

### Q51. [2 Marks] [NAT]

In grammar S→ABA, A→a | ε, B→b | ε, eliminate epsilon productions while preserving ε in the language by allowing S→ε. Obtain S alternatives by deleting any subset of nullable occurrences from ABA, retain distinct resulting right-hand sides only, and retain S→ε once. How many distinct productions have left-hand side S after this step?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A disk head starts at cylinder40. Pending requests are10,45,70, and no new requests arrive. Under shortest-seek-time-first, choose the nearest pending request, breaking ties toward the lower cylinder. What total distance is travelled to serve all requests?

**Answer format:** Integer cylinders.

### Q53. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In this code, p points to a valid integer object, f may modify that object, and integer arithmetic does not overflow:

```text
u = *p + 2
call f()
v = *p + 2
```

Which statements are correct?

**Candidates**

**I.** Identical text proves v may be replaced by u.

**II.** A proof that f cannot modify the pointed-to object can make that reuse valid.

**III.** If f changes the object, the two evaluations may differ.

**IV.** A function call is never relevant to memory-expression availability.

A. III and IV  
B. II and III  
C. I and II  
D. I and III

### Q54. [2 Marks] [NAT]

Initially its completion counter is zero and its timer is stopped. A device completes DMA requests at times 0,3,6,9,12,… microseconds. On the first completion after an interrupt, it starts a 10-microsecond timer and sets a completion counter to 1. Further completions increment the counter. It interrupts when either the counter reaches 8 or the timer expires, then clears the counter and stops the timer. Completions are instantaneous; none coincide with the first two timer expirations. How many interrupts occur at or before time 30 microseconds?

**Answer format:** Exact integer.

### Q55. [2 Marks] [NAT]

A routing table contains only the following entries, plus a default route. For destinations in 10.0.0.0/24, how many addresses select interface A under longest-prefix matching?

```text
10.0.0.0/24     A
10.0.0.64/26    B
10.0.0.96/27    A
10.0.0.112/28   C
```

Count all addresses, without excluding network or broadcast addresses.

**Answer format:** Exact integer.

### Q56. [2 Marks] [NAT]

A five-stage scalar pipeline uses IF,ID,EX,MEM,WB, one cycle per stage, and has full forwarding except that a load's result becomes available only at the end of MEM. The sequence is load r1,[a]; add r2,r1,r3; add r4,r2,r5. With separate instruction/data memories and no other stalls, how many cycles are required from the first IF through the last WB?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two private hosts each use UDP source port 5000. H1 sends to server endpoint S1 and to distinct server endpoint S2; H2 sends to S1. Compare NAT mapping policies: endpoint-dependent creates a separate mapping for each (private address,private port,destination address,destination port); endpoint-independent creates one for each (private address,private port). All mappings remain live. How many mappings are needed under the two policies, respectively?

A. (3,2)  
B. (2,3)  
C. (3,3)  
D. (2,2)

### Q58. [2 Marks] [NAT]

A directed graph has edges s→a(4),s→b(1),b→a(1),a→t(2),b→t(8). How many edges are in its unique shortest s-to-t path?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A heap file has100 data pages. A noncovering secondary index identifies8 qualifying records, whose record identifiers refer to pages7,7,19,44,44,44,80,80. The index lookup costs3 page reads. The buffer is initially empty but can retain all accessed pages. Ignoring output writes and counting each distinct fetched page once, how many page reads are needed to retrieve all qualifying records using this index?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A binary min-heap with fifteen distinct keys uses array indices 1–15. Across all valid assignments of those keys to a heap, how many different indices can contain the third-smallest key?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

The Boolean function F=AB+(NOT A)C is implemented directly as a two-level AND-OR circuit, with a separate inverter generating NOT A. Gate delays are positive and may differ. Only one primary input changes at a time, after the circuit has settled. Which statements are correct?

A. Adding the product term BC does not change the Boolean function.  
B. With B=C=1, a change of A can produce a temporary 0 at the output for some gate delays.  
C. Adding the product term ABC guarantees removal of this possible temporary 0 for every choice of positive gate delays.  
D. Adding the product term BC guarantees removal of this possible temporary 0 during changes of A with B=C=1.

### Q62. [2 Marks] [NAT]

Let D be the positive divisors of 30, ordered by divisibility. How many bijections f:D→D preserve the order in both directions, meaning x divides y if and only if f(x) divides f(y)?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A TCP sender has cwnd=10 MSS and advertised receive window rwnd=8 MSS. There are already 6 MSS of unacknowledged data. One arriving cumulative acknowledgment acknowledges 2 MSS and advertises rwnd=5 MSS. Assume cwnd stays 10 MSS and no other acknowledgments arrive. What is the maximum additional data, in MSS units, that the sender may transmit immediately after processing this acknowledgment?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

In an undirected graph with vertices s,a,b,t, edges have weights sa=1,sb=1,ab=0,at=1,bt=1. A path must be simple, so it cannot repeat vertices. How many shortest s-to-t paths exist?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Matrix A has rows (0,1,1),(2,1,0),(4,3,2). Swap its first two rows to obtain PA, then compute PA=LU with unit diagonal L and no further row swaps. What is L₃₂?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 058

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, B, D |
| 2 | NAT | 1 | 2 |
| 3 | MSQ | 1 | A, B, C |
| 4 | NAT | 1 | 2 |
| 5 | NAT | 1 | 15 (exact) |
| 6 | NAT | 2 | 22 |
| 7 | MSQ | 2 | A, C, D |
| 8 | NAT | 2 | 38.89 (range 38.885–38.895) |
| 9 | MSQ | 2 | A, C, D |
| 10 | NAT | 2 | 5 |
| 11 | NAT | 1 | 2 |
| 12 | MCQ | 1 | C |
| 13 | MCQ | 1 | C |
| 14 | MCQ | 1 | C |
| 15 | NAT | 1 | 48 |
| 16 | MCQ | 1 | A |
| 17 | MCQ | 1 | A |
| 18 | MSQ | 1 | A, B, C |
| 19 | MCQ | 1 | D |
| 20 | NAT | 1 | 9 |
| 21 | NAT | 1 | 5 |
| 22 | NAT | 1 | 0.7854 (range 0.78535–0.78545) |
| 23 | NAT | 1 | 0.6875 |
| 24 | NAT | 1 | 5 |
| 25 | NAT | 1 | -1.5 |
| 26 | NAT | 1 | 2 |
| 27 | MCQ | 1 | A |
| 28 | MCQ | 1 | A |
| 29 | MSQ | 1 | A, C, D |
| 30 | NAT | 1 | 2 |
| 31 | MCQ | 1 | C |
| 32 | NAT | 1 | 0 |
| 33 | NAT | 1 | 13 |
| 34 | MSQ | 1 | B, C, D |
| 35 | MCQ | 1 | B |
| 36 | MCQ | 2 | C |
| 37 | NAT | 2 | 2 |
| 38 | NAT | 2 | 3 |
| 39 | NAT | 2 | 7 |
| 40 | NAT | 2 | 0 |
| 41 | NAT | 2 | 0.1481 (accepted range 0.14805–0.14815) |
| 42 | MCQ | 2 | C |
| 43 | NAT | 2 | 8 |
| 44 | NAT | 2 | 2 |
| 45 | NAT | 2 | 5 |
| 46 | MCQ | 2 | C |
| 47 | NAT | 2 | 0.8 |
| 48 | NAT | 2 | 1.2308 (range 1.23075–1.23085) |
| 49 | NAT | 2 | 2.25 |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 7 |
| 52 | NAT | 2 | 90 |
| 53 | MCQ | 2 | B |
| 54 | NAT | 2 | 2 |
| 55 | NAT | 2 | 208 |
| 56 | NAT | 2 | 8 |
| 57 | MSQ | 2 | B, C, D |
| 58 | NAT | 2 | 3 |
| 59 | NAT | 2 | 7 |
| 60 | NAT | 2 | 6 |
| 61 | MSQ | 2 | A, B, D |
| 62 | NAT | 2 | 6 |
| 63 | NAT | 2 | 1 |
| 64 | NAT | 2 | 4 |
| 65 | NAT | 2 | 1 |
