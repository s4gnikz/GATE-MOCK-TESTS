# GATE CS 2027 — Full-Length Mock Test 074

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

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Exactly one of three boxes A,B,C contains a prize. Their labels say, respectively, “The prize is in B,” “The prize is in C,” and “The prize is not in C.” Exactly one label is true. Which statements follow?

**Candidates**

**I.** The prize may be in A.

**II.** The prize must be in C.

**III.** The prize cannot be in B.

**IV.** The label on A must be true.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q2. [1 Mark] [NAT]

How many digits are in the ordinary binary representation, without leading zeroes, of the positive integer8^5/4^2?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A mixture contains milk and water in the ratio3:2 by volume. Ten litres are removed after thorough mixing and replaced by ten litres of pure water. The final ratio is1:1, and total volume is unchanged. What was the initial total volume, in litres?

**Answer format:** Exact number.

### Q4. [1 Mark] [NAT]

A sequence satisfies a1=1 and a(n+1)=a(n)+n(n+1) for n≥1. What is a5?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A report describes four events: obtaining permission(P), collecting samples(C), calibrating the instrument(K), and measuring the samples(M). Permission was obtained before collection; both collection and calibration occurred before measurement. No other ordering information is given, and no events were simultaneous. How many chronological orders are consistent with the report?

**Answer format:** Integer.

### Q6. [2 Marks] [MSQ]

A notice states: “Only applicants who submitted both forms were interviewed. Every interviewed applicant received a decision.” Assume both statements are true. Which conclusions necessarily follow?

A. No applicant who failed to submit both forms was interviewed.
B. An applicant who received no decision was not interviewed.
C. Every applicant who submitted both forms was interviewed.
D. Every applicant who received a decision was interviewed.

### Q7. [2 Marks] [MSQ]

Which sentences use standard subject–verb agreement?

A. Each of the reports has a separate appendix.
B. The reports, each with a separate appendix, have been submitted.
C. Each of the reports have a separate appendix.
D. The reports, each with a separate appendix, has been submitted.

### Q8. [2 Marks] [NAT]

A cube on a horizontal grid has top face1, bottom6, north-facing face2, south-facing5, east-facing3 and west-facing4. It rolls one square north, then east, then south, then west, without slipping or turning about the vertical axis between rolls. A north roll puts the former north-facing face on the bottom; analogous conventions apply to the other directions. What number is on top afterward?

**Answer format:** Integer face label.

### Q9. [2 Marks] [NAT]

A 3×3×3 cube of unit cubes is painted on all six outer faces. All eight corner unit cubes are then removed. Of the exposed unit-square faces of the remaining solid, what fraction are painted? Include newly exposed faces and round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q10. [2 Marks] [NAT]

A firm reports revenue and cost as follows: year1 revenue120, cost90; year2 revenue150, cost120, in the same units. Profit margin is profit divided by revenue. By how many percentage points did the margin decrease from year1 to year2?

**Answer format:** Exact number of percentage points.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Starting with [1,2,3,4,5,6], perform a stable partition that puts all even values before all odd values while preserving order within each group. Only swaps of adjacent elements are permitted. What is the minimum number of swaps?

**Answer format:** Integer.

### Q12. [1 Mark] [MCQ]

A mutex is held while a thread updates two fields that jointly maintain an invariant. Why can protecting only the first field's assignment be insufficient?

A. Another thread may observe the intermediate inconsistent pair before the second assignment.
B. A mutex can protect only constant variables.
C. Two fields always update atomically without synchronization.
D. Locking necessarily prevents either assignment from executing.

### Q13. [1 Mark] [NAT]

A protocol numbers frames modulo 16. The receiver currently expects 14 and accepts only the next in-order frame, discarding every other arrival. Frames arrive with sequence numbers 15,14,0,15,0,1, in that order. What sequence number does it expect at the end?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A real3×3 matrix has rank2. A consistent linear system Ax=b therefore has a solution set that is an affine space of what dimension?

**Answer format:** Integer.

### Q15. [1 Mark] [MSQ]

For real x, define f(x)=x when x is rational and f(x)=−x when x is irrational. Which statements are true?

A. f is continuous at zero.
B. f is not differentiable at zero.
C. f is continuous at one.
D. f′(0)=0.

### Q16. [1 Mark] [MSQ]

For powers of two n, a recursive algorithm has three recursive calls on size n/2, nonrecursive work Θ(n²), and constant work at n=1. Which statements are true?

A. Its total work is Θ(n²).
B. Its total work is Θ(n² log n).
C. Its recursion tree has n^(log₂3) leaves.
D. Its recursion tree has n internal levels before reaching size one.

### Q17. [1 Mark] [NAT]

A stack-machine translation evaluates postfix expression a b + c d − * using PUSH for operands and binary operators that pop two values and push one result. What is the maximum operand-stack depth, starting empty?

**Answer format:** Exact integer.

### Q18. [1 Mark] [MCQ]

A queue is implemented with two stacks. Enqueue pushes onto stack I. Dequeue pops stack O if nonempty; otherwise it moves all of I to O by repeated pops and pushes, then pops O. Which statement is correct for a sequence starting with both stacks empty?

A. Each element can move from I to O at most once before removal.
B. Every dequeue performs a constant number of stack operations in the worst case.
C. Moving I to O reverses FIFO order incorrectly.
D. Every enqueue must first empty O.

### Q19. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic pushdown automaton recognizes balanced parentheses by pushing on '(' and popping on ')', rejecting a pop from an empty stack. Acceptance requires the stack to be empty at end of input. Which statements are correct?

**Candidates**

**I.** The empty string is accepted.

**II.** Equal total counts of '(' and ')' guarantee acceptance.

**III.** Every prefix of an accepted string has at least as many '(' as ')'.

**IV.** The string '())(' is accepted.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q20. [1 Mark] [NAT]

Independent random variables X and Y each have variance 4. Find Var(2X−3Y+7).

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be regular and F finite over the same alphabet. Which languages are necessarily regular?

A. L∪F  
B. L−F  
C. F−L  
D. Every language containing L as a subset.

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For one program, processor P executes N instructions at CPI=1.5 and 3 GHz. Processor Q executes 0.8N instructions at CPI=2 and 4 GHz. Ignore all other delays. What is Q's speedup over P?

A. 0.8  
B. 1.0  
C. 1.25  
D. 1.5

### Q23. [1 Mark] [MCQ]

Equivalence relations R and S on {1,2,3,4,5,6} have partitions {{1,2},{3,4},{5,6}} and {{1},{2,3},{4,5},{6}}, respectively. Let T be the smallest equivalence relation containing R∪S. How many ordered pairs are in R∩S and T, respectively?

A. 6 and 36
B. 0 and 30
C. 12 and 36
D. 6 and 18

### Q24. [1 Mark] [MCQ]

P holds a single-instance resource R and waits for S. Q holds the single instance of S but is running and will release it without requesting another resource. No other processes or requests exist. Which statement is justified?

A. P and Q are already deadlocked because P waits.
B. A circular wait exists through R and S.
C. Q must be waiting for R implicitly.
D. The stated resource situation does not form a deadlock.

### Q25. [1 Mark] [NAT]

Table T(x) contains 2,2,NULL,5. What is the result of `SELECT COUNT(DISTINCT x) FROM T`?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

A tree has ten vertices. What is the sum of its vertex degrees?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A CPU can mask ordinary maskable interrupts while executing a short critical section. Which statements are correct?

**Candidates**

**I.** Masking prevents delivery of those maskable interrupts during the masked interval.

**II.** Masking interrupts on one CPU automatically stops every other CPU from accessing shared memory.

**III.** Excessively long masked intervals can increase interrupt response latency.

**IV.** Masking converts every ordinary load/store into a multi-CPU atomic read-modify-write operation.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q28. [1 Mark] [MSQ]

All operands below are unsigned n-bit integers, and operations wrap modulo2^n. Evaluating operands has no side effects. Which rewrites preserve both definedness and value for every input? Division by zero is undefined.

A. x*(y+z) to x*y+x*z
B. x/x to1, including when x=0
C. x*0 to0
D. x−y to y−x for every n≥2

### Q29. [1 Mark] [MSQ]

A combinational block has Boolean inputs a,b,c and outputs s=a XOR b XOR c and k=ab OR ac OR bc. Which statements hold?

A. The numerical sum a+b+c equals s+2k.
B. k is 1 exactly when all three inputs are 1.
C. Complementing all three inputs complements s and complements k.
D. Distinct input triples always produce distinct output pairs (s,k).

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A synchronous two-bit machine updates (q1,q0) to (q0,q1 XOR q0) on each clock edge. Its reset state is 01. Which statements are correct?

**Candidates**

**I.** The reset trajectory has period 3.

**II.** State 00 is reached after three edges from reset.

**III.** State 10 is reached after two edges from reset.

**IV.** q1 and q0 are complements throughout the reset trajectory.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q31. [1 Mark] [MSQ]

An SQL integer column x has CHECK(x>0) but no NOT NULL constraint. A CHECK passes when its condition is TRUE or UNKNOWN. Which statements are correct?

A. A row with x=NULL can satisfy this CHECK.
B. Every non-NULL value satisfying this CHECK is positive.
C. The CHECK alone excludes NULL values.
D. Adding NOT NULL would impose no additional restriction.

### Q32. [1 Mark] [MCQ]

A compiler uses a non-relational constant-propagation analysis: it tracks each variable separately and joins different constants to “not constant.” Both branches below are feasible.

```text
if p then { x=2; y=7; }
else      { x=7; y=2; }
z=x+y;
```

At the assignment to z, which description is correct?

A. The analysis proves x=2 and z=9.
B. The analysis proves y=7 and z=9.
C. The stated analysis cannot prove z constant, although z is always 9.
D. z can equal 4 or 14 during execution.

### Q33. [1 Mark] [NAT]

A five-stage IF–ID–EX–MEM–WB pipeline issues one instruction per cycle. Full forwarding is present, but an immediately following user of a load incurs one stall cycle. All other hazards below are resolved by forwarding. How many cycles, starting with the first IF, complete all three instructions through WB?

```text
LOAD R1,[R0]
ADD  R2,R1,R1
ADD  R3,R2,R1
```

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A real3×3 matrix A has rank1 and trace5. What is trace(A²)?

**Answer format:** Exact number.

### Q35. [1 Mark] [MCQ]

A client asks DNS for an AAAA record. Which result type is being requested?

A. An IPv6 address associated with the name.
B. An Ethernet hardware address.
C. A TCP acknowledgment number.
D. The text of an HTTP response body.

### Q36. [2 Marks] [NAT]

Relation R(A,B,C,D) has functional dependencies A→B, B→A, AC→D. How many candidate keys does R have?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A slotted page has 4096 bytes, a fixed 32-byte header and twelve existing four-byte slot entries. Existing records occupy 3900 bytes in total. Compaction may collect all free bytes, but existing records and slots remain. Inserting one new record needs one new four-byte slot entry. What is the largest new record size in bytes that can fit after compaction?

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

A completed depth-first search of a directed graph assigns discovery/finish times u:(2,9), v:(4,7), and w:(10,13), using one global clock. Which statements are correct?

A. v is a descendant of u in the DFS forest.
B. If edge v→u exists, it is a back edge.
C. If edge u→v exists, it must be a tree edge rather than a forward edge.
D. An edge v→w could be present with these timestamps in that completed DFS.

### Q39. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A receiver expects byte 1000. Segments containing bytes 1100–1199,1200–1299,1300–1399 arrive before the segment containing 1000–1099. It immediately sends a cumulative ACK for each arrival and buffers out-of-order bytes. No bytes are lost. What ACK numbers are sent for these four arrivals in order?

A. 1200,1300,1400,1100  
B. 1000,1000,1000,1400  
C. 1100,1200,1300,1400  
D. 1000,1100,1200,1300

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A schedule is `r1(x), w1(x), r2(x), c1, c2`, where T2 reads the value written by T1. Which statements are correct?

**Candidates**

**I.** It is recoverable.

**II.** It is cascadeless.

**III.** T2 could require cascading rollback if T1 aborted before its displayed commit instead.

**IV.** T2 commits before T1 in the displayed schedule.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

### Q41. [2 Marks] [NAT]

Round-robin scheduling uses quantum two and zero context-switch cost. Jobs P,Q,R arrive at times 0,1,2 with CPU bursts 5,3,1 respectively. Arrivals exactly at a quantum boundary join the ready queue before the just-preempted job. What is the sum of their waiting times?

**Answer format:** Integer.

### Q42. [2 Marks] [MCQ]

Let L={a^(n^2) : n is a nonnegative integer}. A proof assumes that L is regular, takes a pumping length p>=1, and chooses w=a^(p^2). Which continuation correctly contradicts the regular-language pumping lemma?

A. In every permitted decomposition w=xyz, y must have length p; pumping twice gives a length outside L.  
B. In every permitted decomposition w=xyz, 1<=|y|<=p; pumping twice gives a length strictly between p^2 and (p+1)^2.  
C. It suffices to choose one permitted decomposition with |y|=1 and show that pumping it twice leaves L.  
D. Pumping down always gives the immediately preceding square length (p-1)^2, which contradicts regularity.

### Q43. [2 Marks] [NAT]

A disk has cylinders0 through199, and the head starts at50 moving toward larger numbers. Pending requests are at60,70,20, with no future arrivals. LOOK reverses at the largest pending request; SCAN proceeds to199 before reversing. Both stop immediately after serving the last request. How much more total head movement does SCAN make than LOOK?

**Answer format:** Integer cylinders.

### Q44. [2 Marks] [MCQ]

A variable x is live after statement `x = y+z`. Which statement describes the liveness transfer across this assignment, ignoring other live variables?

A. Old x must remain live before the statement solely because new x is live after it.
B. Old x is killed by the assignment, while y and z are used and become live before it.
C. y and z are killed because they appear on the right-hand side.
D. The statement cannot define x because x is already live.

### Q45. [2 Marks] [NAT]

For a Turing machine M over binary input strings, consider these four sets of valid machine encodings:

1. M accepts the string 01.
2. Every string accepted by M is equal to 01.
3. M halts on every binary input string.
4. There exists a binary input string on which M eventually enters a designated state q (the state q is part of the machine description and is distinct from its initial state).

A set is recognizable if some Turing machine accepts exactly its members and may fail to halt on nonmembers. How many of the four sets are recognizable?

**Answer format:** Numeric value; integer.

### Q46. [2 Marks] [NAT]

How many insertion orders of the distinct keys 1–7 produce an ordinary unbalanced BST whose root is 4, whose left subtree has root 2 and leaves 1,3, and whose right subtree has root 6 and leaves 5,7? There is no rebalancing.

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A simple undirected graph has vertices A,B,C,D,E,F. Each edge of triangle ABC and each edge of triangle DEF has weight 1. Edges AD, BE and CF have weight 2, and edge AE has weight 3. There are no other edges. Two spanning trees are distinct when their edge sets differ. Which statements are correct?

A. The minimum spanning-tree weight is 6.  
B. There are exactly 27 minimum spanning trees.  
C. There are exactly 45 spanning trees of weight 7.  
D. Every spanning tree of weight 7 uses exactly two weight-2 edges.

### Q48. [2 Marks] [NAT]

For real a, define f_a(x)=x^4-2a*x^2+4x on the whole real line. What is the smallest integer a for which f_a has two distinct strict local minima?

**Answer format:** Numeric value; integer.

### Q49. [2 Marks] [NAT]

A min-heap contains the array[1,3,2,8,7,4,5]. Replace its root by 9, then restore heap order by repeatedly swapping the current key with its smaller child while that child is smaller. How many swaps occur?

**Answer format:** Exact integer.

### Q50. [2 Marks] [NAT]

A B+ tree leaf can hold at most four keys and must hold at least two unless it is the root. The root currently has three leaf children with keys [2,4], [6,8], and [10,12,14]. Delete key6. Prefer borrowing from the right sibling if it has more than its minimum; otherwise borrow from the left if possible; otherwise merge with the right. How many leaf children does the root have afterward?

**Answer format:** Exact integer.

### Q51. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A partial DFA over {a,b} has states q0,q1,q2, start state q0, and accepting set {q2}. Its only transitions are q0 on a to q1, q1 on a to q2, and q2 on a to q2. Undefined transitions reject. What is the minimum number of states in a complete DFA recognizing the complement of its language over {a,b}*?

A. 4  
B. 3  
C. 5  
D. 6

### Q52. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed graph permits parallel edges. Its adjacency-list representation stores one entry per edge, while its Boolean adjacency matrix stores only whether at least one edge exists for each ordered vertex pair. Which statements hold?

A. The Boolean matrix alone may not determine the number of edges.  
B. Summing entries in a Boolean matrix row always gives the outdegree when parallel edges count separately.  
C. Reachability is unchanged if parallel edges are collapsed to one edge.  
D. Two different edge multisets can have the same Boolean adjacency matrix.

### Q53. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A singly linked list must be reversed in place. The code maintains pointers prev,cur,next and uses three assignments per iteration after saving next=cur.next. Which order preserves access to the remaining unreversed suffix?

A. cur=cur.next; cur.next=prev; prev=cur  
B. cur.next=prev; prev=cur; cur=next  
C. prev=cur; cur=next; cur.next=prev  
D. cur.next=next; prev=next; cur=prev

### Q54. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A contiguous memory region occupies addresses [0,240), where [u,v) has size v−u. Initially its free regions are [0,60), [100,180), and [200,240). Process X occupies [60,100), and process Y occupies [180,200). Compare first-fit and best-fit, each starting from this initial state.

First allocate A of size 50, then B of size 35. Next free X and A, leaving B and Y allocated. Every allocation takes space from the lowest-address end of its selected hole. First-fit searches from address 0 on each request; best-fit selects the smallest sufficient hole. Adjacent free regions are immediately coalesced, with no metadata overhead or compaction.

What are the largest single requests that can now be satisfied under (first-fit, best-fit), respectively?

A. (100,180)  
B. (100,100)  
C. (180,180)  
D. (180,100)

### Q55. [2 Marks] [NAT]

For f(x)=x ln x on x>0, draw its tangent at x=a, where a>e⁻¹. That tangent and the two coordinate axes enclose a triangle. What is the smallest possible triangle area? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q56. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Evaluate (7+3)+(−5) using four-bit signed two's-complement integers, rounding neither operand. In implementation S, each addition saturates at −8 or 7 if needed. In implementation W, each addition wraps modulo 16. What are the final signed results (S,W)?

A. (5,5)  
B. (2,5)  
C. (2,−11)  
D. (7,−6)

### Q57. [2 Marks] [NAT]

A poset has elements a,b,c,d with a<b, a<c, b<d and c<d, and no other comparabilities except those forced by transitivity and reflexivity. How many linear extensions does it have?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A lexer uses maximal munch. Its tokens are ID=[a-z]+, EQ='=', and EQEQ='=='. Keyword 'if' takes precedence over ID only when both match the same longest lexeme. Whitespace is ignored. How many tokens result from this input?

```text
ifif===if = iff
```

**Answer format:** Exact integer.

### Q59. [2 Marks] [NAT]

A message of6000 data bytes crosses three equal-rate store-and-forward links in sequence. Each link sends1000 bytes per millisecond. There is no propagation or processing delay. Packets have an extra100-byte header and may be pipelined across links. Splitting the message into six equal data packets instead of three equal data packets changes the time until the entire message reaches the destination. How many milliseconds are saved?

**Answer format:** Exact number.

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An HTTP client sends a conditional GET containing `If-None-Match: "v7"` for a cached representation. The server's current representation has the same entity tag and is otherwise eligible for the conditional request. Compare a 304 response with a 200 response carrying the entire unchanged representation. Which statement is correct?

A. A 304 necessarily eliminates the request-response round trip.  
B. A 304 supplies a new full representation body that must replace the cached body.  
C. A 304 can save representation-body transfer while still requiring a network round trip.  
D. A 304 proves that all caches on the Internet contain the same body.

### Q61. [2 Marks] [MCQ]

A microprogram must start one memory read at the address in MAR, wait until READY=1, copy the returned data into MDR, and increment register R exactly once. All microinstruction operations execute once on every cycle in which that microinstruction is visited. A START pulse begins a transaction; issuing START again before completion begins an unwanted second transaction. READY remains 0 until the transaction completes and then remains 1 until the routine exits. Which routine meets the requirements for every finite memory latency? A branch tests READY at the end of its cycle.

A. U: START; R=R+1; if READY=0 goto U else goto V. V: MDR=DATA; exit.  
B. U: START; goto V. V: if READY=0 goto V else goto W. W: MDR=DATA; R=R+1; exit.  
C. U: START; goto V. V: R=R+1; if READY=0 goto V else goto W. W: MDR=DATA; exit.  
D. U: START; MDR=DATA; R=R+1; exit.

### Q62. [2 Marks] [MCQ]

A directed graph has edges s→a of weight 1, a→b of weight 0, b→a of weight 0, and b→t of weight 2. Walks may revisit vertices. Which statement is correct?

A. The shortest s-to-t walk weight is unbounded below.
B. The shortest weight is 3 and only one shortest walk exists.
C. The shortest weight is 3 and infinitely many shortest walks exist.
D. No walk from s to t exists.

### Q63. [2 Marks] [MSQ]

Consider A=[[0,1],[1,1]]. An unpivoted factorization A=LU is sought with L unit lower triangular and U upper triangular. Which statements are correct?

A. Such an LU factorization exists because det(A) is nonzero.
B. Interchanging the rows allows a unit-lower/upper factorization.
C. A is invertible even though the stated unpivoted factorization is impossible.
D. The obstruction proves that the linear system Ax=b has no solution for some real b.

### Q64. [2 Marks] [MCQ]

An eight-bit two's-complement fixed-point format has four fractional bits. Multiply the values encoded by 0xE6 and 0x1C using an exact intermediate result, then round once to the nearest representable value, breaking a tie toward an even least significant retained bit. No overflow occurs. What is the final encoded byte?

A. 0xD3  
B. 0xD2  
C. 0x2E  
D. 0xD4

### Q65. [2 Marks] [NAT]

A binary floating-point system has precision p=3 significant bits, minimum normal exponent−2, and gradual underflow. Normal positive values have the form1.bb×2^e, with e≥−2. Subnormal values use the same spacing as the smallest normal binade. Under rounding to nearest, ties to even, what value represents3/32?

**Answer format:** Exact decimal.

---

## ANSWER KEY — MOCK TEST 074

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 12 |
| 3 | NAT | 1 | 60 |
| 4 | NAT | 1 | 41 |
| 5 | NAT | 1 | 3 |
| 6 | MSQ | 2 | A, B |
| 7 | MSQ | 2 | A, B |
| 8 | NAT | 2 | 5 |
| 9 | NAT | 2 | 0.5556 (range 0.55555–0.55565) |
| 10 | NAT | 2 | 5 |
| 11 | NAT | 1 | 6 |
| 12 | MCQ | 1 | A |
| 13 | NAT | 1 | 2 |
| 14 | NAT | 1 | 1 |
| 15 | MSQ | 1 | A, B |
| 16 | MSQ | 1 | A, C |
| 17 | NAT | 1 | 3 |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | A |
| 20 | NAT | 1 | 52 |
| 21 | MCQ | 1 | D |
| 22 | MSQ | 1 | A, B, D |
| 23 | MCQ | 1 | A |
| 24 | MCQ | 1 | D |
| 25 | NAT | 1 | 2 |
| 26 | NAT | 1 | 18 |
| 27 | MCQ | 1 | B |
| 28 | MSQ | 1 | A, C |
| 29 | MSQ | 1 | A, C |
| 30 | MCQ | 1 | D |
| 31 | MSQ | 1 | A, B |
| 32 | MCQ | 1 | C |
| 33 | NAT | 1 | 8 (exact) |
| 34 | NAT | 1 | 25 |
| 35 | MCQ | 1 | A |
| 36 | NAT | 2 | 2 |
| 37 | NAT | 2 | 112 |
| 38 | MSQ | 2 | A, B |
| 39 | MSQ | 2 | A, C, D |
| 40 | MCQ | 2 | D |
| 41 | NAT | 2 | 10 |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 258 |
| 44 | MCQ | 2 | B |
| 45 | NAT | 2 | 2 (exact) |
| 46 | NAT | 2 | 80 |
| 47 | MCQ | 2 | D |
| 48 | NAT | 2 | 2 (exact) |
| 49 | NAT | 2 | 2 |
| 50 | NAT | 2 | 3 |
| 51 | MSQ | 2 | B, C, D |
| 52 | MCQ | 2 | B |
| 53 | MSQ | 2 | A, C, D |
| 54 | MSQ | 2 | B, C, D |
| 55 | NAT | 2 | 0.3679 (range 0.36785–0.36795) |
| 56 | MSQ | 2 | A, C, D |
| 57 | NAT | 2 | 2 |
| 58 | NAT | 2 | 6 |
| 59 | NAT | 2 | 1.7 |
| 60 | MSQ | 2 | A, B, D |
| 61 | MCQ | 2 | B |
| 62 | MCQ | 2 | C |
| 63 | MSQ | 2 | B, C |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 0.125 |
