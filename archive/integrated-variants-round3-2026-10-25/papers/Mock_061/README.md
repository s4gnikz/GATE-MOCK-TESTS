# GATE CS 2027 — Full-Length Mock Test 061

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

Arrange these sentences into a coherent account. “This discrepancy” refers to the difference between the two measurements, and “the repair” refers to replacing the defective sensor.

P: A replacement sensor brought the readings into agreement.  
Q: Two instruments measuring the same temperature initially gave different readings.  
R: After the repair, both instruments remained stable during a second trial.  
S: This discrepancy led the technician to identify a defective sensor.

A. Q,S,P,R
B. S,Q,R,P
C. Q,P,R,S
D. P,R,Q,S

### Q2. [1 Mark] [NAT]

Household A has three boys. Household B has one boy and one girl. Choose a household with equal probability, then choose one of its children uniformly. Given that the selected child is a boy, what is the probability that household A was chosen?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The witness gave an equivocal reply: it could reasonably be understood as either agreement or refusal.” In this sentence, “equivocal” most nearly means:

A. deliberately brief  
B. supported by independent evidence  
C. open to conflicting interpretations  
D. expressing definite agreement

### Q4. [1 Mark] [NAT]

A culture grows exponentially at a constant rate. Its population becomes eight times its initial value in 12 hours. Starting from the same initial population, after how many hours will it become 32 times its initial value?

**Answer format:** Numeric value; integer.

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A device failed on three occasions when its battery level was below 5%, but no observations at other battery levels were collected. Which proposed next step would best test whether low battery level predicts failure?

A. Declare that every failure has already been explained.  
B. Collect comparable observations across both low and higher battery levels.  
C. Exclude every future observation above 5%.  
D. Infer that a full battery guarantees success without testing it.

### Q6. [2 Marks] [NAT]

A cube has face labels equal to the original outward normal directions: +x,−x,+y,−y,+z,−z. First rotate the cube90 degrees about the positive x axis, then90 degrees about the positive y axis, each by the right-hand rule about fixed world axes. Encode the face finally pointing upward(+z) as follows: +x=1,−x=2,+y=3,−y=4,+z=5,−z=6. What code results?

**Answer format:** Integer code.

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Three tasks A,B,C take 4,3,2 hours. A and B may run simultaneously on separate workers, but C requires both to have finished and uses one worker. Exactly two workers are available and tasks cannot be split. What is the minimum completion time for all tasks?

A. 5 hours  
B. 6 hours  
C. 7 hours  
D. 9 hours

### Q8. [2 Marks] [NAT]

A shortest lattice path from (0,0) to (4,3) uses only unit steps right or up. It must visit (1,1) and must not visit (3,2). How many such paths exist?

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

Arrange the sentences into a coherent paragraph.

P. To distinguish these explanations, the researchers repeated the trial with freshly calibrated instruments.
Q. The repeated trial again found the increase, weakening the calibration explanation.
R. The first trial showed a temperature increase, but the team was unsure whether it was real or caused by instrument drift.
S. They therefore concluded that further investigation of the physical cause was warranted.

A. P–R–Q–S
B. R–Q–P–S
C. R–P–Q–S
D. S–R–P–Q

### Q10. [2 Marks] [NAT]

A shop marks an item 25% above cost and then offers a 12% discount on the marked price. It also pays a transaction fee equal to 2% of the discounted selling price. What is its net profit percentage on cost?

**Answer format:** Exact finite decimal percentage, without the percent sign.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

The three-input majority function is F=xy+xz+yz. A two-to-one multiplexer selects D0 when x=0 and D1 when x=1. Which pair (D0,D1) realizes F?

A. (y OR z, y AND z)
B. (y AND z, y OR z)
C. (y XOR z, y AND z)
D. (NOT y, z)

### Q12. [1 Mark] [NAT]

On the real numbers other than−1, define x*y=x+y+xy. This operation forms a group with identity0. What is the inverse of3 under this operation?

**Answer format:** Exact decimal.

### Q13. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An established TCP connection carries five bytes. The sender issues successful send calls containing three bytes and then two bytes, in that order. No connection closure or error occurs. The receiver uses blocking recv calls with a buffer capacity of five bytes. Which receive patterns are possible, considering TCP byte-stream semantics?

**Candidates**

**I.** One recv returns all five bytes.

**II.** Two recv calls return one byte and then four bytes.

**III.** A recv returns zero solely because no bytes have arrived yet.

**IV.** The receiver obtains the two-byte send's bytes before the three-byte send's bytes.

A. I and IV  
B. I and II  
C. II and III  
D. II and IV

### Q14. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A JK flip-flop obeys Q′=J(NOT Q)+(NOT K)Q. Which settings force the stated behaviour for both possible current values of Q?

A. J=0,K=0 holds Q unchanged.  
B. J=1,K=1 toggles Q.  
C. J=1,K=0 forces Q′=0.  
D. J=0,K=1 forces Q′=0.

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

SQL table T(x) contains 2,2,3,NULL. What pair is returned by `SELECT COUNT(*), COUNT(x) FROM T`?

A. (4,3)  
B. (3,3)  
C. (4,2)  
D. (2,2)

### Q16. [1 Mark] [MSQ]

A nondeterministic PDA accepts by final state only after consuming the entire input. In a conversion to empty-stack acceptance, a fresh protected bottom marker is placed below the original stack, and from an original final state the machine may enter a new mode that uses only epsilon transitions to pop all remaining stack symbols, including that marker. Empty-stack acceptance also requires all input consumed. Which statements are correct?

A. The drain mode can successfully finish an accepting computation after the entire input has been consumed in an original final state.
B. Entering drain mode with unread input automatically accepts that input as well.
C. The new bottom marker must be treated as an ordinary original-stack symbol by every old transition, without restriction.
D. The requirement to consume all input prevents a drained stack reached too early from accepting a remaining suffix.

### Q17. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Delete a perfect matching from the complete bipartite graph K3,3. What is the size of a minimum vertex cover of the remaining graph?

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A paging system uses 4 KiB pages. A process requires 9,000 bytes of contiguous virtual storage starting at a page boundary. How many bytes of internal fragmentation are present in its allocated final page if all required pages are allocated?

**Required precision:** Integer bytes; 1 KiB=1024 bytes.

A. 6576  
B. 3288  
C. 1644  
D. 3289

### Q19. [1 Mark] [NAT]

How many binary strings of length4 contain exactly one occurrence of the substring00? Occurrences may overlap; for example,0001 contains two occurrences.

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

A process has three resident writable pages and forks using copy-on-write, initially sharing all three frames with its child. The parent writes page0 twice, then the child writes page1 once. No page is otherwise allocated or evicted. What is the peak number of physical frames holding these pages across both processes?

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A sequence satisfies T(0)=0 and T(n)=T(n−1)+2n−1 for n≥1. Find T(20).

**Required precision:** Integer.

A. 800  
B. 200  
C. 401  
D. 400

### Q22. [1 Mark] [NAT]

A postfix translation emits each operand when visited and emits an operator after both children. How many operator symbols appear in the postfix form of(a+b)*(c−d/e)?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A file's logical blocks0,1,2 map to disk blocks40,41,90. A system reads logical blocks0–2 in order. Adjacent disk block numbers can be transferred as one contiguous disk extent. What is the minimum number of extents that contain precisely these requested blocks?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a standard B+ tree in which all data entries are stored at leaves, which statements hold?

**Candidates**

**I.** Internal separator keys can appear again at the leaf level.

**II.** All leaves are at the same depth.

**III.** Every successful lookup must stop at an internal separator without reaching any leaf.

**IV.** The root must always have exactly the same minimum occupancy as a nonroot internal node.

A. II and III  
B. I and II  
C. II and IV  
D. III and IV

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An insertion-sort implementation shifts a preceding element only when it is strictly greater than the key being inserted. Records have a sorting key and a distinct label. Which statements are correct?

**Candidates**

**I.** Equal-key records retain their initial relative order.

**II.** Replacing the strict comparison by “greater than or equal” still guarantees stability.

**III.** On an already sorted array, no record is shifted by the inner loop.

**IV.** On every input, the number of shifts equals the number of adjacent equal-key pairs.

A. I and II  
B. I and IV  
C. II and III  
D. I and III

### Q26. [1 Mark] [NAT]

An eight-slot hash table probes i² modulo8 for i=0,1,2,... when inserting a particular key. All slots reached by this sequence are occupied. What is the largest possible number of empty slots elsewhere in the table despite this insertion being unable to reach them?

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Transaction T writes x, then transaction U reads that new value of x. T subsequently aborts. Which requirement alone directly forces U to abort too, even if U wrote no data?

A. Cascading recovery after a dirty read.  
B. The existence of a read–read conflict.  
C. Every read-only transaction must abort.  
D. Any two transactions accessing one item must be serialized by aborting both.

### Q28. [1 Mark] [NAT]

What integer is printed by this C code? All operations are within the array.

```c
int a[] = {2,4,6};
int *p = a;
int x = *p++;
int y = ++*p;
printf("%d", x + y + a[1]);
```

**Answer format:** Integer.

### Q29. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A byte-addressed processor has a 16-bit address bus. A 4 KiB memory chip is selected exactly when address bits A15..A12 equal 1010; A11..A0 address bytes within the chip. What is the largest decimal byte address mapped to the chip?

**Required precision:** Exact integer.

A. 90110  
B. 22528  
C. 45056  
D. 45055

### Q30. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A memory system has a 2 ns cache lookup time and a 5% miss rate. A miss adds 60 ns after the cache lookup, with no overlap. What is the average memory access time?

**Required precision:** Integer nanoseconds.

A. 10  
B. 5  
C. 3  
D. 6

### Q31. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Boolean function F(x,y,z)=(x OR y) AND(NOT x OR z). Which statements hold?

**Candidates**

**I.** If x=0, then F=y.

**II.** If x=1, then F=z.

**III.** F always equals y AND z.

**IV.** F always equals x XOR y XOR z.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An HTTP cache has a stale response with an entity tag. It validates the response using If-None-Match and receives304 Not Modified. Which action matches the response's meaning?

A. Replace the representation body by the digits304.  
B. Treat the resource as permanently deleted.  
C. Reuse the cached representation body subject to the updated cache metadata.  
D. Assume the server transmitted a complete replacement body.

### Q33. [1 Mark] [MCQ]

Let R be a binary relation on a nonempty domain. Which formula is the logical negation of

`forall x exists y [R(x,y) AND forall z (R(x,z) -> z=y)]`?

All variables in the options are bound as displayed.

A. exists x forall y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
B. exists x exists y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
C. forall x forall y [NOT R(x,y) AND exists z (R(x,z) AND z!=y)]  
D. exists x forall y [NOT R(x,y) OR forall z (R(x,z) AND z!=y)]

### Q34. [1 Mark] [NAT]

Procedure F(n) returns1 when n=0 and otherwise returns F(n−1)+F(n−1), making both calls without memoization. How many base-case invocations occur in F(5)?

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In an activation record, which link is normally used to restore the caller's activation when a procedure returns, regardless of lexical nesting?

A. The dynamic link.  
B. The static link in every case.  
C. A pointer to the global symbol table.  
D. A pointer to the first heap object.

### Q36. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n=2^k with k≥1, determine the tight asymptotic running time of this code. Every execution of work() costs one unit.

```text
i = n
while i >= 1:
    j = i
    while j <= n:
        work()
        j = 2*j
    i = i/2
```

A. Θ(log n)  
B. Θ(n)  
C. Θ((log n)²)  
D. Θ(n log n)

### Q37. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An array of length18 is rotated left by8 positions using an in-place cycle algorithm. A move maps each original index i to (i−8) modulo18. The algorithm saves one value in a temporary variable at the start of each disjoint index cycle and then completes that cycle before beginning another. How many times does it need to start a new cycle?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q38. [2 Marks] [NAT]

Singly linked nodes initially form A: 1→2→3→4→null and B: 9→3→4→null, sharing the actual nodes 3 and 4. The A list is reversed in place by changing its nodes' next pointers; B's head pointer is unchanged. What is the sum of node labels encountered from B's head after the reversal?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

A stack stores data and a separate stack of minima. On push(x), it pushes x on the minima stack only when that stack is empty or x is strictly smaller than its top. On pop, it removes the minima top whenever the popped data value equals it. Which statements are correct?

A. The sequence push(3),push(1),push(1),pop makes the reported minimum incorrect.
B. The algorithm is correct for arbitrary duplicate values without modification.
C. Pushing onto the minima stack also when x equals its top repairs this duplicate-minimum problem.
D. Removing the equality check from pop, so that the minima stack is never popped, repairs all cases.

### Q40. [2 Marks] [MSQ]

Host H sends an IPv4 packet through two routers to host J. Each link uses Ethernet, and there is no NAT, tunneling, or fragmentation. Which statements hold for normal forwarding?

A. The source and destination Ethernet addresses can change at each routed hop.
B. The source and destination IPv4 addresses change at every routed hop.
C. The IPv4 TTL decreases at each router that forwards the packet.
D. An Ethernet destination address on the first link must be J's Ethernet address even when J is on another subnet.

### Q41. [2 Marks] [MSQ]

A single-threaded process has a pipe with buffered data. It forks, after which both processes retain their inherited read and write descriptors. Neither writes more data. Which statements hold for blocking reads with a positive requested byte count?

A. After the buffered data is drained, the child can receive end-of-file only after all write descriptors referring to the pipe have been closed.
B. Closing only the child's write descriptor necessarily makes the next empty-pipe read return end-of-file while the parent's write descriptor remains open.
C. Closing unused write descriptors in both processes is needed if their intended protocol relies on detecting end-of-file.
D. A read from an empty pipe always returns zero immediately, even with an open writer.

### Q42. [2 Marks] [MSQ]

Let L be context-free and R regular over the same alphabet. Which languages are guaranteed context-free?

A. L∩R
B. L minus R
C. R minus L
D. L∪R

### Q43. [2 Marks] [NAT]

For what real value of k does the following system have infinitely many solutions?

```text
x + y + z = 2
2x + 3y + 4z = 5
3x + 4y + 5z = k
```

**Answer format:** Exact number.

### Q44. [2 Marks] [NAT]

A 10,000-bit payload is split into k equal packets, each with a 100-bit header, and sent through two equal-rate links via a store-and-forward router. Both links have rate R, propagation is negligible, links can work concurrently, and packets are transmitted back-to-back. k is a positive integer dividing 10,000. What k minimizes completion time of the final packet?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

In an expression DAG, equal leaves and identical operator nodes with identical ordered children are shared. Commutativity is not used. For expression(a+b)*(a+b)+(b+a), how many binary-operator nodes are present?

**Answer format:** Integer.

### Q46. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A cache has one data line and a separate one-line victim cache, both initially empty. A hit in the victim cache swaps its line with the main-cache line and does not access memory. On a miss in both, memory supplies the requested block to the main cache; its old valid block replaces the victim-cache line. Blocks are clean. For the access sequence A,B,A,C,B, how many memory block reads occur?

**Required precision:** Exact integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q47. [2 Marks] [NAT]

A process has three threads. One thread forks under a model in which the parent retains all threads and the child initially has only the calling thread. After the fork, each process creates two additional threads; none exit. How many threads exist in total across the two processes?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A four-variable Boolean function F(A,B,C,D) is 1 on minterms {0,1,2,3,8,9,10,11,12,13,14,15} and 0 elsewhere. A is the most significant minterm bit. A two-level sum-of-products implementation must cover all 1-minterms and no 0-minterms. What is the minimum total number of literals in a valid SOP?

**Required precision:** Exact integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q49. [2 Marks] [MSQ]

For L={0^n1^n : n≥0}, choose0^p1^p in a pumping-lemma argument, where p is a proposed regular pumping length. Which statements are correct?

A. Every legal pumped part lies entirely in the0 block.
B. Pumping that nonempty part down changes the number of0s while leaving the number of1s unchanged.
C. One must know the exact pumped-part length before choosing the original string.
D. The resulting contradiction disproves regularity.

### Q50. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A B+ tree root has two leaf children, containing[2,5] and[8,11]. Leaves hold at most 3 keys. Inserting into a full leaf first forms four sorted keys, then splits them into two leaves with two keys each. The first key of the new right leaf is copied to the parent. Internal nodes can have at most 3 children. Insert 6, then7. How many keys are in the root afterward?

**Required precision:** Exact integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q51. [2 Marks] [NAT]

For x≠0, f(x)=(exp(x)−1−x)/x². Set f(0) to the value making f continuous at0. What is f'(0)?

**Answer format:** Decimal rounded to four places.

### Q52. [2 Marks] [MSQ]

A program over mathematical integers executes while(x!=0){x=2*x+1;} and then returns0. No value of x is observed afterward. An optimizer removes the loop because x is unused at the return. Which statements are correct?

A. For initial x=0, both versions return0.
B. For initial x=1, the rewrite changes a nonterminating execution into a terminating one.
C. Absence of a later use of x is sufficient to justify this rewrite for every input.
D. Preserving termination behaviour matters for this transformation.

### Q53. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A cache has 64-byte lines and is initially empty. A packed row-major 16×16 array of four-byte elements begins on a line boundary. A loop reads every element exactly once in column-major order (all rows of column 0, then all rows of column 1, and so on). The cache is fully associative with eight lines and LRU replacement; no other memory accesses occur. How many cache misses occur?

**Required precision:** Integer.

A. 512  
B. 128  
C. 256  
D. 257

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An in-order five-stage pipeline has stages IF,ID,EX,MEM,WB. Every stage takes one cycle except EX for a multiplication, which occupies EX for three consecutive cycles. While EX is occupied, an instruction in ID and all following instructions stall. Each instruction uses MEM and WB for one cycle even if it has no memory operation. There are no data dependencies, branches, or memory stalls, and no separate multiplier. Six instructions execute, with multiplications at positions2 and5 and ordinary instructions elsewhere. Starting with instruction1 in IF in cycle1, in which cycle does instruction6 finish WB?

**Required precision:** Integer.

A. 14  
B. 28  
C. 7  
D. 15

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A recognizer for L1 and a recognizer for L2 may loop on nonmembers. Which proposed procedures recognize the stated languages for every such pair of recognizers?

**Candidates**

**I.** For L1∪L2, interleave one step of each recognizer and accept when either accepts.

**II.** For L1∪L2, run the first recognizer to completion before starting the second, accepting if either accepts.

**III.** For L1∩L2, run the first until it accepts, then the second until it accepts, and then accept.

**IV.** For the complement of L1, accept if its recognizer has not accepted after one million steps.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II

### Q56. [2 Marks] [NAT]

A ternary relationship R(A,B,C) uses domains of sizes 2,3,4 respectively. Constraints require that each pair (A,B) determines at most one C and each pair (A,C) determines at most one B. What is the maximum possible number of relationship tuples?

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

Eight nonpreemptive activities have the following half-open time intervals; an activity may begin exactly when another finishes.

| Activity | Interval |
|---|---|
| A | [0,3) |
| B | [1,2) |
| C | [2,4) |
| D | [3,5) |
| E | [4,6) |
| F | [5,7) |
| G | [6,8) |
| H | [7,9) |

Let m be the maximum number of mutually nonoverlapping activities that can be selected, and let r be the number of distinct activity subsets attaining this maximum. What is (m,r)?

A. (3,4)  
B. (4,4)  
C. (4,5)  
D. (5,1)

### Q58. [2 Marks] [NAT]

Independent X,Y are uniform on [0,1]. Find E[X | Y>X²].

**Answer format:** Exact finite decimal.

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A Boolean cover must cover columns {1,2,3}. Available implicants are P covering {1,2} at cost 3, Q covering {2,3} at cost 2, R covering {1} at cost 1, and S covering {3} at cost 1. Costs add, and any subset of implicants may be chosen. What is the minimum total cover cost?

**Required precision:** Integer.

A. 6  
B. 3  
C. 2  
D. 4

### Q60. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A four-bit carry-lookahead adder computes p_i=a_i XOR b_i and g_i=a_i AND b_i. XOR delay is 2 units; AND and OR delay is 1 unit independent of fan-in. All inputs and c0 arrive at time 0. Each carry is implemented directly as its expanded sum of products, using one AND level for each product and one OR level; single g terms need no additional AND. Sum s_i=p_i XOR c_i. What is the latest output-arrival time among s0,s1,s2,s3,c4?

**Required precision:** Integer time units.

A. 12  
B. 3  
C. 7  
D. 6

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A CRC uses generator G(x)=x³+x+1 over GF(2). In a fixed 15-bit transmitted word, exactly two distinct bit positions are inverted. How many unordered pairs of error positions produce an error polynomial divisible by G(x), and thus go undetected? Positions are numbered 0 through 14 by powers of x.

**Required precision:** Integer.

A. 9  
B. 18  
C. 5  
D. 10

### Q62. [2 Marks] [NAT]

How many functions f:{1,2,3,4,5}→{1,2,3,4,5} satisfy f(f(x))=x for every x and have exactly one fixed point?

**Answer format:** Integer.

### Q63. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A 0/1 knapsack has capacity 7. Four items have (weight,value) pairs (2,6),(3,8),(4,9),(5,12), and each item can be taken at most once. What is the optimal value?

**Required precision:** Integer.

A. 36  
B. 18  
C. 9  
D. 19

### Q64. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Processes P and Q communicate through a finite-capacity pipe. P writes until the pipe is full; Q still has an open read end but never reads. Assume blocking writes and no signals or failures. Which statements are correct?

**Candidates**

**I.** P may block on a further write.

**II.** Keeping a read end open guarantees that Q consumes bytes.

**III.** Closing all read ends changes the situation from merely having a full pipe.

**IV.** A finite buffer guarantees completion for an arbitrarily large write workload even if Q never reads.

A. I and II  
B. I and IV  
C. II and III  
D. I and III

### Q65. [2 Marks] [NAT]

Use set relational algebra. C(Student)={u,v,w}, R(Student,Course)={(u,x),(u,y),(v,x)}, and Required(Course) is empty. A query is defined as

```text
C − project_Student((C × Required) − R)
```

How many student tuples does the query return, including students with no tuples in R?

**Answer format:** Exact integer.

---

## ANSWER KEY — MOCK TEST 061

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 0.6667 (accepted range 0.66665–0.66675) |
| 3 | MSQ | 1 | A, B, D |
| 4 | NAT | 1 | 20 (exact) |
| 5 | MSQ | 1 | A, C, D |
| 6 | NAT | 2 | 2 |
| 7 | MSQ | 2 | A, C, D |
| 8 | NAT | 2 | 8 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 7.8 |
| 11 | MCQ | 1 | B |
| 12 | NAT | 1 | -0.75 |
| 13 | MCQ | 1 | B |
| 14 | MCQ | 1 | C |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 1 | A, D |
| 17 | MCQ | 1 | A |
| 18 | MCQ | 1 | B |
| 19 | NAT | 1 | 5 |
| 20 | NAT | 1 | 5 |
| 21 | MCQ | 1 | D |
| 22 | NAT | 1 | 4 |
| 23 | NAT | 1 | 2 |
| 24 | MCQ | 1 | B |
| 25 | MCQ | 1 | D |
| 26 | NAT | 1 | 5 |
| 27 | MSQ | 1 | B, C, D |
| 28 | NAT | 1 | 12 |
| 29 | MCQ | 1 | D |
| 30 | MCQ | 1 | B |
| 31 | MCQ | 1 | D |
| 32 | MSQ | 1 | A, B, D |
| 33 | MCQ | 1 | A |
| 34 | NAT | 1 | 32 |
| 35 | MSQ | 1 | B, C, D |
| 36 | MSQ | 2 | A, B, D |
| 37 | MCQ | 2 | C |
| 38 | NAT | 2 | 15 |
| 39 | MSQ | 2 | A, C |
| 40 | MSQ | 2 | A, C |
| 41 | MSQ | 2 | A, C |
| 42 | MSQ | 2 | A, B, D |
| 43 | NAT | 2 | 7 |
| 44 | NAT | 2 | 10 |
| 45 | NAT | 2 | 4 |
| 46 | MCQ | 2 | B |
| 47 | NAT | 2 | 8 |
| 48 | MCQ | 2 | A |
| 49 | MSQ | 2 | A, B, D |
| 50 | MCQ | 2 | A |
| 51 | NAT | 2 | 0.1667 (accepted range 0.16665–0.16675) |
| 52 | MSQ | 2 | A, B, D |
| 53 | MCQ | 2 | C |
| 54 | MCQ | 2 | A |
| 55 | MCQ | 2 | A |
| 56 | NAT | 2 | 6 |
| 57 | MCQ | 2 | C |
| 58 | NAT | 2 | 0.375 |
| 59 | MCQ | 2 | B |
| 60 | MCQ | 2 | D |
| 61 | MCQ | 2 | A |
| 62 | NAT | 2 | 15 |
| 63 | MCQ | 2 | B |
| 64 | MCQ | 2 | D |
| 65 | NAT | 2 | 3 |
