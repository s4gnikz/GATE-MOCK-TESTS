# GATE CS 2027 — Full-Length Mock Test 015

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all remaining questions carry two marks each. MCQ has exactly one correct option. MSQ requires all correct options and awards no partial credit. Incorrect MCQs lose one-third of their marks. Incorrect MSQ/NAT answers and unattempted questions receive zero. GA contributes 15 marks, mathematics 13 and core CS 72. All assumptions needed for numerical questions are stated. Follow each NAT answer format; use exact arithmetic unless rounding is requested.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

A screening procedure flags an item whenever its measured value exceeds a threshold. Raising that threshold while leaving all measurements unchanged can have which effect on the set of flagged items?

A. It can only stay the same or become a subset of its former set.
B. It must strictly increase.
C. Every formerly unflagged item must become flagged.
D. It must become empty regardless of the measurements.

### Q2. [1 Mark] [NAT]

A 3×5 rectangular grid of unit squares is rotated 180 degrees about its centre. How many unit squares map onto themselves as sets?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A sequence begins with a1=1,a2=2 and obeys a(n)=a(n−1)+2a(n−2) for n≥3. Find a6.

**Answer format:** Integer.

### Q4. [1 Mark] [NAT]

A rectangle has perimeter 30 and diagonal length √125. What is its area?

**Answer format:** Integer square units.

### Q5. [1 Mark] [MCQ]

Which sentence has correct subject–verb agreement?

A. Each of the reports have an appendix.
B. The list of required documents are on the desk.
C. Neither of the two proposed routes is suitable.
D. The results of the experiment indicates a change.

### Q6. [2 Marks] [NAT]

A shop marks an item 25% above cost and then offers a 12% discount on the marked price. It also pays a transaction fee equal to 2% of the discounted selling price. What is its net profit percentage on cost?

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q7. [2 Marks] [MCQ]

A valid password must satisfy both rules: if it contains a digit, it must contain a symbol; if it contains a symbol, it must contain at least eight characters. Which case necessarily violates these rules?

A. A seven-character password containing a digit and a symbol.
B. An eight-character password containing neither digits nor symbols.
C. A nine-character password containing a symbol but no digit.
D. An eight-character password containing both a digit and a symbol.

### Q8. [2 Marks] [NAT]

A rectangular tile measures 2 by 3 units. An unlimited number of these tiles may be rotated by 90 degrees. What is the smallest positive side length of a square that can be tiled completely without cutting or overlap, if the square's side length must be an integer?

**Answer format:** Integer units.

### Q9. [2 Marks] [MCQ]

“A new policy reduced average processing time, but the study did not measure the number of incorrect decisions.” Which claim is justified by the study as described?

A. Processing became faster on average, while the effect on decision accuracy remains unmeasured.
B. Decision accuracy necessarily improved.
C. Every decision became faster and more accurate.
D. Incorrect decisions necessarily increased.

### Q10. [2 Marks] [NAT]

A committee of four is selected from five engineers and three designers. It must contain at least two engineers and at least one designer. How many committees are possible?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

In a three-variable Karnaugh map, minterms 000 and 100 are adjacent. What term results from combining just these two minterms, with variables a,b,c in that order?

A. b′c′
B. a′b′
C. ac′
D. a+b+c

### Q12. [1 Mark] [MSQ]

An IPv4 fragment has offset field 100, 400 payload bytes, and MF=1. A downstream link permits only 200 payload bytes per fragment; 200 is divisible by eight. The router splits this fragment into two. Which statements are correct?

A. Their offset fields are 100 and 125.
B. Both resulting fragments have MF=1.
C. Both retain the original datagram's identification value.
D. Their offsets must restart from zero because they were produced by a different router.

### Q13. [1 Mark] [MCQ]

Two consecutive instructions write the same register, and the younger instruction completes first in an out-of-order execution system. Which hazard must be handled to preserve the correct final register value?

A. Write-after-write.
B. Read-after-read.
C. A mandatory memory-address alignment fault.
D. A control hazard caused by all register writes.

### Q14. [1 Mark] [NAT]

How many onto functions map a three-element labelled set to a two-element labelled set?

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

What is the coefficient of x⁷ in the formal power series 1/((1−x)(1−x²))?

**Answer format:** Integer.

### Q16. [1 Mark] [MCQ]

A tuple-calculus query uses `Employee(e) AND EXISTS d (Department(d) AND Works(e,d))`. What does it require of each returned employee?

A. Assignment to at least one listed department.
B. Assignment to every department.
C. No assignments at all.
D. That every domain object be a department.

### Q17. [1 Mark] [NAT]

How many truth assignments to p,q,r satisfy (p→q)∧(q→r)∧(r→p)?

**Answer format:** Integer.

### Q18. [1 Mark] [MSQ]

A source-reachable directed graph has nonnegative edge weights, some equal to zero. Which statements about Dijkstra's algorithm are correct?

A. Zero-weight edges are permitted by its correctness argument.
B. Every source-reachable vertex must have a unique shortest path.
C. Different vertices can have the same final distance from the source.
D. A zero-weight cycle necessarily makes shortest distances undefined.

### Q19. [1 Mark] [NAT]

A 3×4 matrix has rows (1,2,0,1),(0,1,1,0),(1,3,1,1). What is the dimension of its nullspace over the real numbers?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

Evaluate the limit as x→0 of (eˣ−1−x)/x².

**Answer format:** Exact finite decimal.

### Q21. [1 Mark] [MCQ]

A lexer has tokens `>` and `>=` and uses longest match. How does it tokenize `>=>`?

A. `>=` followed by `>`.
B. `>` followed by `=>`, where `=>` is not a declared token.
C. One token `>=>` even though none is declared.
D. It must discard the final character.

### Q22. [1 Mark] [NAT]

A tabular minimization pattern `1-0--` has five bit positions. How many minterms does it represent?

**Answer format:** Integer.

### Q23. [1 Mark] [MCQ]

Grammar S→aS | Sb | ε generates which language?

A. a*b*
B. {aⁿbⁿ:n≥0}
C. (ab)* only
D. All strings over {a,b}

### Q24. [1 Mark] [NAT]

A directed graph with five vertices has eight edges and no self-loops. In an adjacency-list representation storing each directed edge once, how many edge entries are stored, excluding vertex headers?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

Table T(g,v) contains (A,2),(A,NULL),(B,5),(B,7). How many groups remain after `GROUP BY g HAVING COUNT(v)=2`?

**Answer format:** Integer.

### Q26. [1 Mark] [MCQ]

A half-adder adds bits x,y without a carry input. Which pair gives (sum,carry)?

A. (x XOR y, x AND y)
B. (x OR y, x XOR y)
C. (x AND y, x OR y)
D. (NOT x, NOT y)

### Q27. [1 Mark] [MCQ]

For a PDA accepting by empty stack with all input consumed, why must the input-consumption condition be checked explicitly?

A. Emptying the stack while unread input remains is not by itself acceptance under this convention.
B. A stack can never be empty.
C. Input is always consumed in one transition.
D. Empty-stack acceptance requires a finite input alphabet of exactly one symbol.

### Q28. [1 Mark] [NAT]

In C, `int x=3; int *p=&x; *p=*p+4;` is executed. What is the value of x afterwards?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

An instruction's unsigned immediate field has six bits. How many different nonnegative integers can it encode directly?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

Which address is inside subnet 192.0.2.128/26?

A. 192.0.2.127
B. 192.0.2.160
C. 192.0.2.192
D. 192.0.3.1

### Q31. [1 Mark] [MSQ]

A producer sends messages through an operating-system queue and a consumer receives them. Which statements distinguish message passing from directly accessing an ordinary shared variable?

A. Communication uses send/receive operations on messages.
B. A messaging interface can transfer data between distinct address spaces.
C. Message passing necessarily makes every application free of race conditions.
D. All message passing must use busy waiting.

### Q32. [1 Mark] [MCQ]

A mutex is held while a thread updates two fields that jointly maintain an invariant. Why can protecting only the first field's assignment be insufficient?

A. Another thread may observe the intermediate inconsistent pair before the second assignment.
B. A mutex can protect only constant variables.
C. Two fields always update atomically without synchronization.
D. Locking necessarily prevents either assignment from executing.

### Q33. [1 Mark] [NAT]

For grammar S→AB, A→a|ε, B→b|ε, how many distinct terminal strings are generated?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

In an S-attributed syntax-directed definition, which attribute kind is used?

A. Synthesized attributes only.
B. Inherited attributes only.
C. No attributes at all.
D. Attributes that can depend only on future input characters, never on children.

### Q35. [1 Mark] [NAT]

A stable sort by key is applied to records (2,A),(1,B),(2,C),(1,D). What is the one-based position of record (2,A) in the sorted output?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A translator uses one public IPv4 address and may reuse a public source port for connections to different external endpoint pairs, since the return mapping includes both external address and external port. It must use distinct public source ports for connections to the same external endpoint. There are three simultaneous connections to endpoint X, two to endpoint Y, and four to endpoint Z, with X,Y,Z distinct. What is the minimum size of the public source-port pool that suffices?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Resource A has two instances and B has one. P holds one A and requests B; Q holds B and requests one A; R holds the other A and requests nothing more. A process that receives its request completes and releases its resources; R can complete immediately. Which statements are correct?

A. The system can finish all processes in order R,Q,P.
B. The cycle involving P and Q proves deadlock even with R able to release an A instance.
C. A cycle in the resource-allocation graph is not sufficient here to establish deadlock.
D. Releasing R's A can enable Q, whose completion can then enable P.

### Q38. [2 Marks] [MCQ]

A TCP receiver initially expects byte 1000. Four 100-byte segments cover byte ranges 1000–1099,1100–1199,1200–1299,1300–1399. They arrive in the order third,first,fourth,second. The receiver buffers out-of-order data and sends a cumulative ACK after each arrival, stating the next missing byte. Which ACK sequence is correct?

A. 1300,1100,1400,1200
B. 1000,1100,1100,1400
C. 1000,1200,1300,1400
D. 1100,1200,1300,1400

### Q39. [2 Marks] [MCQ]

Two initially empty tables P(id,qid) and Q(id,pid) have non-NULL foreign keys P.qid→Q.id and Q.pid→P.id. A transaction inserts P(1,1) and Q(1,1). What difference can deferred checking make, assuming both foreign keys permit checking at commit?

A. It allows both rows to be inserted and the final mutually referencing state to satisfy the constraints, whereas immediate checking would reject whichever insert occurs first.
B. It permits either foreign key to remain broken permanently after commit.
C. It removes the requirement that referenced keys exist at commit.
D. It forces both tables to remain empty.

### Q40. [2 Marks] [NAT]

Under lexical scope, an outer procedure activation P1 has local x=10 and creates a nested procedure Q1 that refers to P1.x. A later separate activation P2 has local x=20 and calls Q1, passing no x parameter. Environments are retained correctly for nested procedures. What value of x does Q1 read?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

Independent X,Y are uniform on [0,1]. Find E[X | Y>X²].

**Answer format:** Exact finite decimal.

### Q42. [2 Marks] [NAT]

A synchronous three-bit register has next-state rule (a,b,c)→(b,c,a XOR c), using old bits simultaneously. Starting at 001, how many clock edges occur before the state first becomes 100?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

Two four-bit two's-complement operands A,B independently range over all 16 bit patterns. How many of the 256 ordered operand pairs cause signed overflow when their sum is retained in four bits?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

Procedure F(n), for n≥0, returns immediately when n≤1. Otherwise it calls F(n−1), then F(n−2), with no memoization. Count only calls with n=0. How many such calls occur during F(6)?

**Answer format:** Integer.

### Q45. [2 Marks] [MSQ]

A compiler translates `x != 0 && 10/x > 1` using left-to-right short-circuit evaluation over exact integers, with division by zero raising an observable exception. Which transformations preserve behaviour for every x?

A. Test x!=0 first and branch around the division when false.
B. Evaluate 10/x before testing x!=0 for all x.
C. Replace the conjunction by an evaluation that performs the division only on the x!=0 branch.
D. Replace the whole expression by true because 10 is positive.

### Q46. [2 Marks] [MCQ]

A dead assignment is `x = read_device();`, and x is not subsequently used. The function read_device has an observable device effect. Which optimization is generally valid?

A. Delete both the call and assignment solely because x is dead.
B. Preserve the call's effect, although storing its unused return value in x may be eliminated.
C. Replace the call by an arbitrary constant and preserve all behaviour.
D. Execute the call twice to compensate for removing the store.

### Q47. [2 Marks] [NAT]

How many equivalence relations on a labelled four-element set have exactly two equivalence classes?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

An array of length 12 is cyclically rotated left by 8 positions using a cycle-following algorithm. Each disjoint permutation cycle uses one temporary variable to save its first value and performs one write to each array location in that cycle. How many separate cycles does the algorithm process?

**Answer format:** Integer.

### Q49. [2 Marks] [MSQ]

Consider languages over {0,1}. Which statements are true?

A. {wwᴿ : w∈{0,1}*} is context-free.
B. {ww : w∈{0,1}*} is context-free.
C. Restricting {ww : w∈{0,1}*} to the unary alphabet {0} gives a regular language.
D. Every context-free language is closed under intersection with every other context-free language.

### Q50. [2 Marks] [MCQ]

A linear-probing table has occupied slots 2,3,4 holding keys whose home slots are respectively 2,2,4. Slot 5 has never been occupied. The key in slot 2 is deleted. Which repair preserves searches for the two remaining keys if no tombstones are allowed?

A. Leave slot 2 empty and do nothing else.
B. Move the key from slot 3 to slot 2 and leave slot 3 empty; keep the key whose home is 4 in slot 4.
C. Move the key from slot 4 to slot 2 and leave slot 3 unchanged.
D. Clear all three slots without reinserting either remaining key.

### Q51. [2 Marks] [MSQ]

R(A,B,C) has dependencies A→B and B→C. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless with respect to the dependencies.
B. The dependencies are preserved by enforcing them separately in R1 and R2.
C. R itself is in BCNF under the given dependencies.
D. Both decomposed relations are in BCNF under their projected dependencies.

### Q52. [2 Marks] [NAT]

A real symmetric 5×5 matrix A satisfies A³=A, rank(A)=4, and trace(A)=0. Find det(I+2A).

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

An open box is made by removing equal squares of side x from the corners of a 12×12 square sheet and folding the sides. For 0<x<6, what is the maximum box volume?

**Answer format:** Integer cubic units.

### Q54. [2 Marks] [MCQ]

For the finite language L={ε,a,a²,…,a⁷}, what is the smallest positive pumping length p satisfying the regular-language pumping lemma? The lemma imposes its decomposition requirement only on words of length at least p.

A. 8
B. 7
C. 1
D. No pumping length exists because the language is finite.

### Q55. [2 Marks] [NAT]

External merge sort handles a file of 17 disk blocks using three buffer blocks. Initial run generation sorts up to three blocks at a time. Each later merge pass uses two input buffers and one output buffer. Every pass, including initial generation and the final merge, reads and writes all 17 blocks; no pass is fused or streamed away. How many total block transfers occur?

**Answer format:** Integer reads plus writes.

### Q56. [2 Marks] [NAT]

A linked list has a noncyclic prefix of length 3 followed by a cycle of length 5. Floyd's algorithm starts slow and fast at the head. In phase one, each iteration advances slow by one link and fast by two, then tests equality; it stops at the first equality. In phase two, one pointer is reset to the head, and both move one link at a time until equal. Count every individual next-link traversal in both phases, excluding the reset. What is the total?

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

A datagram socket has queued datagrams of lengths 12 and 5 bytes, in that order. Each receive uses an 8-byte buffer. The specified API returns at most one datagram per receive and discards excess bytes of a truncated datagram. What byte counts do the next two receives return?

A. 8 and 8
B. 8 and 5
C. 12 and 5
D. 8 and 4

### Q58. [2 Marks] [MSQ]

A strict-priority preemptive scheduler always chooses a ready higher-priority job before a lower-priority one. A low-priority job is ready continuously. Which statements are true?

A. An unending supply of higher-priority work can starve it.
B. Increasing its priority over time through an appropriate aging policy can address this starvation risk.
C. Its ready state alone guarantees it executes within one time quantum under the stated strict-priority policy.
D. Preemption by itself guarantees bounded waiting for every priority level.

### Q59. [2 Marks] [MCQ]

An algorithm runs the following loops, with work() constant time:

```text
for i = 1 to n:
    for j = 1 to floor(n/i):
        for k = 1 to i:
            work()
```

What is its tight asymptotic running time?

A. Θ(n log n)
B. Θ(n²)
C. Θ(n³)
D. Θ(log n)

### Q60. [2 Marks] [MSQ]

A disk uses shortest-seek-time-first scheduling. New requests may arrive while earlier requests wait. Which statements are correct?

A. A sufficiently persistent stream of nearby requests can postpone a distant pending request indefinitely.
B. SSTF guarantees bounded waiting for every request without any restriction on arrivals.
C. If only finitely many requests exist and no new ones arrive, repeated service eventually serves all of them.
D. SSTF must visit the highest-numbered cylinder before every direction reversal.

### Q61. [2 Marks] [NAT]

A microinstruction includes 12 independent control bits, a next-address field for a 256-word control store, and a two-bit sequencing mode. There are no other fields or encoding restrictions. How many bits wide is each microinstruction?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

Four unit-time jobs have (deadline,profit): A(1,70), B(2,60), C(2,50), D(3,40). At most one job runs in each integer slot 1,2,3; a job earns its profit only if completed in a slot no later than its deadline. What maximum total profit is possible?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

The exact value −1.375 is rounded to a signed fixed-point format with two fractional bits and sufficient integer range. Rounding is to nearest, ties to an even encoded integer. What real value is stored?

**Answer format:** Exact finite decimal.

### Q64. [2 Marks] [NAT]

Memory has four interleaved banks. Consecutive word addresses use banks 0,1,2,3 cyclically. The controller issues at most one request per cycle; a bank next accepts a request no earlier than six cycles after its previous request. Eight consecutive word reads starting at address zero are issued in order as early as possible. All banks are initially idle and the first request issues at cycle 0. At which cycle does the eighth request issue?

**Answer format:** Integer.

### Q65. [2 Marks] [MSQ]

A binary floating-point format has finite precision. Ignore overflow and underflow, and assume its precision is at least four significant bits. Which real values can be represented exactly?

A. 3/8
B. 1/10
C. 7/4
D. 1/3

## ANSWER KEY — MOCK TEST 015

All NAT answers in this paper are exact.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 1 |
| 3 | NAT | 1 | 32 |
| 4 | NAT | 1 | 50 |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 7.8 |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 6 |
| 9 | MCQ | 2 | A |
| 10 | NAT | 2 | 60 |
| 11 | MCQ | 1 | A |
| 12 | MSQ | 1 | A, B, C |
| 13 | MCQ | 1 | A |
| 14 | NAT | 1 | 6 |
| 15 | NAT | 1 | 4 |
| 16 | MCQ | 1 | A |
| 17 | NAT | 1 | 2 |
| 18 | MSQ | 1 | A, C |
| 19 | NAT | 1 | 2 |
| 20 | NAT | 1 | 0.5 |
| 21 | MCQ | 1 | A |
| 22 | NAT | 1 | 8 |
| 23 | MCQ | 1 | A |
| 24 | NAT | 1 | 8 |
| 25 | NAT | 1 | 1 |
| 26 | MCQ | 1 | A |
| 27 | MCQ | 1 | A |
| 28 | NAT | 1 | 7 |
| 29 | NAT | 1 | 64 |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | A, B |
| 32 | MCQ | 1 | A |
| 33 | NAT | 1 | 4 |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 3 |
| 36 | NAT | 2 | 4 |
| 37 | MSQ | 2 | A, C, D |
| 38 | MCQ | 2 | B |
| 39 | MCQ | 2 | A |
| 40 | NAT | 2 | 10 |
| 41 | NAT | 2 | 0.375 |
| 42 | NAT | 2 | 6 |
| 43 | NAT | 2 | 64 |
| 44 | NAT | 2 | 5 |
| 45 | MSQ | 2 | A, C |
| 46 | MCQ | 2 | B |
| 47 | NAT | 2 | 7 |
| 48 | NAT | 2 | 4 |
| 49 | MSQ | 2 | A, C |
| 50 | MCQ | 2 | B |
| 51 | MSQ | 2 | A, B, D |
| 52 | NAT | 2 | 9 |
| 53 | NAT | 2 | 128 |
| 54 | MCQ | 2 | A |
| 55 | NAT | 2 | 136 |
| 56 | NAT | 2 | 21 |
| 57 | MCQ | 2 | B |
| 58 | MSQ | 2 | A, B |
| 59 | MCQ | 2 | B |
| 60 | MSQ | 2 | A, C |
| 61 | NAT | 2 | 22 |
| 62 | NAT | 2 | 170 |
| 63 | NAT | 2 | -1.5 |
| 64 | NAT | 2 | 9 |
| 65 | MSQ | 2 | A, C |

