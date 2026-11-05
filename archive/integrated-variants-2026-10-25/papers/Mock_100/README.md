# GATE CS 2027 — Full-Length Mock Test 100

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

A sequence begins with a1=1,a2=2 and obeys a(n)=a(n−1)+2a(n−2) for n≥3. Find a6.

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A rectangle has perimeter 40 cm and area 96 cm². Its longer side is increased by 1 cm and its shorter side decreased by 1 cm. By how many square centimetres does its area decrease?

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

Choose the grammatically correct completion in formal English: “Neither the two applicants nor their supervisor ___ available when the committee ___ its decision yesterday.”

A. were; announce
B. was; announced
C. were; announcing
D. was; announce

### Q4. [1 Mark] [NAT]

In a company, 60% of employees work remotely. Of the remote employees, 25% work part-time. Of the remaining employees, 10% work part-time. What percentage of all employees work part-time?

**Answer format:** Integer percentage, without the percent sign.

### Q5. [1 Mark] [NAT]

Exactly two of A, B, C and D must be on duty. If A is on duty, B must be on duty. In addition, C is on duty if and only if D is not on duty. How many different pairs can be on duty?

**Answer format:** Numeric value; integer.

### Q6. [2 Marks] [NAT]

A point is reflected across the vertical line x=1, and the reflected point is then rotated90 degrees counterclockwise about the origin. The final point is(−3,−2). What was the original point's distance from the origin?

**Answer format:** Exact number.

### Q7. [2 Marks] [MSQ]

A switch is either ON or OFF. A says, “The switch is ON.” B says, “A's statement is false.” C says, “The switch is OFF.” Exactly two of the three statements are true. Which conclusions follow?

A. The switch is OFF.
B. A and B are both truthful.
C. B and C are truthful.
D. The information is inconsistent.

### Q8. [2 Marks] [NAT]

How many distinct arrangements of the multiset of letters A,A,B,B,C contain no adjacent A's?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

A delivery service has two depots. Their on-time delivery percentages are unchanged between two months: depot A is90% on time and depot B is60% on time. In month1, A handles twice as many deliveries as B. In month2, the service-wide on-time rate is75%. Relative to its month1 share, by what percentage has A's share of all deliveries decreased?

**Answer format:** Percentage decrease as a number, without the percent symbol.

### Q10. [2 Marks] [NAT]

A square sheet occupies 0≤x≤8, 0≤y≤8. Fold the right half onto the left along x=4, then the top half onto the bottom along y=4. Punch one tiny circular hole centred at (4,1), and another centred at (2,2), through every layer. The radii are equal and less than 0.1; the first punch straddles the vertical folded edge. After unfolding completely, how many distinct circular holes are present? Count a hole centred on a former fold line once.

**Answer format:** Exact integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A nondeterministic PDA accepts by final state only after consuming the entire input. In a conversion to empty-stack acceptance, a fresh protected bottom marker is placed below the original stack, and from an original final state the machine may enter a new mode that uses only epsilon transitions to pop all remaining stack symbols, including that marker. Empty-stack acceptance also requires all input consumed. Which statements are correct?

A. The drain mode can successfully finish an accepting computation after the entire input has been consumed in an original final state.
B. Entering drain mode with unread input automatically accepts that input as well.
C. The new bottom marker must be treated as an ordinary original-stack symbol by every old transition, without restriction.
D. The requirement to consume all input prevents a drained stack reached too early from accepting a remaining suffix.

### Q12. [1 Mark] [NAT]

A B+ tree internal node contains six separator keys. Under the usual k-keys/k+1-children rule, how many child pointers does it contain?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A dataset of four values has mean 5 and population variance 4. Append two more observations, both equal to the old mean. What is the new population variance?

**Answer format:** Decimal rounded to four places.

### Q14. [1 Mark] [NAT]

A syntax-directed definition for a list uses L→L1,d with L.count=L1.count+1, and L→d with L.count=1. How many applications of the recursive production occur in a parse of d,d,d,d,d?

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

A process incurs three page faults in sequence. Each fault reads one page from disk; the first and third evict dirty pages, while the second evicts a clean page. No writes are merged or deferred. How many page-sized disk transfers occur in total?

**Answer format:** Integer.

### Q16. [1 Mark] [MCQ]

How many times is work() called asymptotically, for positive integer n?

```text
for i = 1 to n:
    j = i
    while j <= n:
        work()
        j = j + i
```

A. Θ(n)  
B. Θ(n²)  
C. Θ(log n)  
D. Θ(n log n)

### Q17. [1 Mark] [MSQ]

A cover-minimization procedure has two feasible covers: C1 uses two rows with total cost8; C2 uses three rows with total cost6. Each is assumed optimal for the count/cost pair shown, and no other cover improves either objective. Which statements are correct?

A. Minimizing row count first and total cost second selects C1.
B. Minimizing total cost first and row count second selects C2.
C. The two objectives necessarily choose the same cover.
D. Reporting only “minimum cover” without specifying the objective can be ambiguous here.

### Q18. [1 Mark] [MCQ]

A full adder receives inputs x,y and carry-in c. Its sum output is x XOR y XOR c. If x=y=1, what are its sum and carry-out as functions of c?

A. (c,1)
B. (NOT c,1)
C. (c,c)
D. (0,c)

### Q19. [1 Mark] [MSQ]

L is a language over {a,b}, and its complement is taken with respect to {a,b}*. Which statements necessarily hold?

A. If both L and its complement are finite, then {a,b}* is finite.
B. If L is regular, its complement is context-free.
C. If L is context-free, its complement is regular.
D. If L is finite, its complement is regular.

### Q20. [1 Mark] [NAT]

For Boolean inputs x,y let F(x,y)=xy and define G=F(x,y) XOR F(NOT x,y) XOR F(x,NOT y) XOR F(NOT x,NOT y). On how many of the four input assignments is G=1?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

On the real numbers other than−1, define x*y=x+y+xy. This operation forms a group with identity0. What is the inverse of3 under this operation?

**Answer format:** Exact decimal.

### Q22. [1 Mark] [NAT]

A C array `int a[3][5]` is stored in row-major order, with sizeof(int)=4 bytes. What is the byte offset of a[2][3] from the start of the array?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A synchronous two-bit machine updates Q0′=NOT Q0 and Q1′=Q1 XOR Q0, using the old state for both expressions. Starting at Q1Q0=10, what unsigned integer does its state represent after five clock edges?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Remove a perfect matching from the complete bipartite graph K3,3. How many spanning trees does the remaining graph have?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

For the unary regular language {a^(3k):k≥0}, what is the smallest positive pumping length satisfying the regular pumping lemma, including |xy|≤p and |y|>0?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

How many three-element subsets of {1,2,3,4,5,6,7} contain4 and contain no pair of consecutive integers?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A microinstruction independently selects at most one of three signals in group A, at most one of five signals in group B, and any subset of two further independent signals. Each group needs an explicit “none” encoding. Encode each group in its own minimum-width binary field and the further signals as individual bits. How many control bits are required?

**Answer format:** Integer.

### Q28. [1 Mark] [MSQ]

In a standard B+ tree in which all data entries are stored at leaves, which statements hold?

A. Internal separator keys can appear again at the leaf level.
B. All leaves are at the same depth.
C. Every successful lookup must stop at an internal separator without reaching any leaf.
D. The root must always have exactly the same minimum occupancy as a nonroot internal node.

### Q29. [1 Mark] [MCQ]

A change-making algorithm repeatedly takes the largest coin not exceeding the remaining amount. Coin denominations are1,4,6 with unlimited supplies. For amount8, which statement is correct?

A. Greedy uses two coins and is optimal.
B. Greedy uses three coins, while the optimum uses two.
C. Greedy uses four coins, while the optimum uses three.
D. No exact representation of8 exists.

### Q30. [1 Mark] [NAT]

A sequence satisfies T(0)=0 and T(n)=T(n−1)+2n−1 for n≥1. Find T(20).

**Answer format:** Integer.

### Q31. [1 Mark] [MCQ]

Initially head points to node A in the singly linked list A→B→C→NULL. Consider these assignments, evaluated in order:

```text
p = head.next
head.next = p.next
p.next = head
head = p
```

Which list is reachable from head afterward?

A. A→C→B→NULL
B. B→A→C→NULL
C. B→C→A→NULL
D. A→B→C→NULL

### Q32. [1 Mark] [MCQ]

A language has lexical nesting. Procedure Outer defines local x and nested procedure Inner, whose body references x. Inner is called by an unrelated procedure Caller while Outer remains active. Which link is needed to find the lexically enclosing activation containing x?

A. A dynamic link to Caller alone
B. A static link to Outer's activation
C. A link to whichever activation was created most recently
D. A link to the global symbol table alone

### Q33. [1 Mark] [NAT]

A 32-bit-wide memory module is constructed from chips each organized as 1024 words × 8 bits. How many chips are needed to obtain 1024 words × 32 bits, with all chips sharing address inputs?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

A transport-layer port number is primarily used to distinguish what?

A. Application endpoints on a host.
B. Individual bits within one Ethernet frame.
C. Physical pins on a memory chip.
D. Cache-line offsets inside a processor.

### Q35. [1 Mark] [NAT]

Two store-and-forward links in series each transmit at1000 bits/s. Propagation and processing delays are zero. A1000-bit message is split into two equal packets with no headers. Transmission starts at time0. At what time, in seconds, does the last bit reach the destination?

**Answer format:** Exact decimal.

### Q36. [2 Marks] [NAT]

Four processes have resource demands: P holds A and requests B; Q holds B and requests C; R holds C and requests A; S holds D and requests B. Each resource has one instance, requests block, and no process releases its held resource before receiving its request. How many processes lie on a directed cycle in the wait-for graph?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

A CRC uses generator G(x)=x³+x+1 over GF(2). An error is undetected exactly when its nonzero error polynomial is divisible by G. Which statements are correct?

A. Error x⁷+1 is undetected.  
B. Error x⁶+1 is undetected.  
C. Every single-bit error is detected.  
D. Every nonzero burst error of length at most three bits is detected.

### Q38. [2 Marks] [MSQ]

A weak entity Room is identified by the pair(BuildingID,RoomNumber). RoomNumber is unique only within a building. Which statements are correct?

A. Rooms in different buildings may share a RoomNumber.
B. RoomNumber alone necessarily identifies a room globally.
C. The owner's identifier contributes to the weak entity's identification.
D. Moving a room record to another building can cause an identifier collision if that building already has the same RoomNumber.

### Q39. [2 Marks] [NAT]

On the fixed domain {1,2,3}, how many binary relations R satisfy both (∀x ∃y R(x,y)) and NOT(∃y ∀x R(x,y))? Relations are distinguished by their sets of ordered pairs.

**Answer format:** Exact integer.

### Q40. [2 Marks] [MSQ]

A schedule consists of w1(x),w2(x),w1(x), followed by commits after all writes. There are no reads. The first and last writes belong to T1 and the middle write to T2. All writes assign fixed constants independently of prior values. Which statements are correct?

A. Its conflict graph is acyclic.
B. It is view-equivalent to the serial order T2,T1.
C. It is conflict-serializable.
D. Its final writer of x is T1.

### Q41. [2 Marks] [MSQ]

For an arbitrary Turing machine M, define L_M={x : M accepts x within at most |x| transition steps}. Which statements are correct?

A. L_M is decidable for every M.
B. Deciding L_M requires deciding whether M eventually halts on x.
C. A decider can simulate exactly the bounded number of allowed steps and reject if no acceptance has occurred.
D. L_M must be empty whenever M fails to halt on some other input.

### Q42. [2 Marks] [NAT]

A three-address code generator translates x=(a+b)*(a+b)+(a+b) and performs local common-subexpression elimination. All operands are unchanged mathematical integers. Each binary operation requires one assignment, and assigning the final expression to x needs no separate copy. What is the minimum number of binary-operation assignments in the resulting code?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

Let A be the real 4x4 matrix

```text
A = [0 1 0 0]
    [0 0 1 0]
    [0 0 0 1]
    [1 0 0 0].
```

How many real matrices X simultaneously satisfy X=X^T, AX=XA, X^2=X, and X*(1,1,1,1)^T=0?

**Answer format:** Numeric value; integer.

### Q44. [2 Marks] [NAT]

A path graph has vertex weights 4,7,5,6,3 in order. Select a set of vertices with no two adjacent, maximizing the total weight. How many different vertex sets attain the optimum? Vertices are distinguished by their positions, even if weights were equal.

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

Four jobs have processing times and deadlines (p,d): A=(2,4), B=(3,6), C=(1,3), D=(2,7). All are available at time 0 on one nonpreemptive machine. There are no idle times or setup costs. Lateness is completion time minus deadline, and maximum lateness is the largest lateness among jobs. What is the minimum achievable maximum lateness?

**Answer format:** Integer time units.

### Q46. [2 Marks] [NAT]

A processor issues four stores at cycles0,1,2,3 unless stalled. A single-entry write buffer accepts a store instantly when empty. Each accepted store occupies the buffer for three cycles: one accepted at cycle t completes and frees the entry at cycle t+3, before any issue at that cycle. While the entry is occupied, the next store stalls, and later stores cannot bypass it. At what cycle is the fourth store accepted?

**Answer format:** Exact integer.

### Q47. [2 Marks] [NAT]

A byte-addressed memory contains 64 KiB and is built from chips storing 8K words of four bits each. Chips are arranged so one addressed byte is transferred at once. How many chips are needed in total?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

A program over mathematical integers executes while(x!=0){x=2*x+1;} and then returns0. No value of x is observed afterward. An optimizer removes the loop because x is unused at the return. Which statements are correct?

A. For initial x=0, both versions return0.
B. For initial x=1, the rewrite changes a nonterminating execution into a terminating one.
C. Absence of a later use of x is sufficient to justify this rewrite for every input.
D. Preserving termination behaviour matters for this transformation.

### Q49. [2 Marks] [NAT]

Two signed fixed-point numbers are stored in 8-bit two's-complement form with four fractional bits. Their raw hexadecimal encodings are E7 and 39. Multiply their exact represented values, then round the result to the nearest representable value in the same format (ties to even). The result is in range. What is the unsigned decimal interpretation, from 0 to 255, of the resulting 8-bit encoding?

**Answer format:** Numeric value; integer.

### Q50. [2 Marks] [NAT]

An undirected graph has edges sa,sb,ac,bc,cd,ad. BFS from s records distances and counts the number of shortest paths to each vertex. What is the number of shortest s-to-d paths?

**Answer format:** Exact integer.

### Q51. [2 Marks] [NAT]

A system defines the working set immediately after a reference as the distinct pages in that reference and the previous three references, or all references so far if fewer than four exist. For the reference string 1,2,1,3,4,2,4,5, what is the sum of the working-set sizes immediately after references 4 through 8?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

Define f(x)=ax+b for x<0, f(0)=1, and f(x)=e^(2x) for x>0. Find a+b if f is differentiable at zero.

**Answer format:** Integer.

### Q53. [2 Marks] [MSQ]

DFAs D1,D2 over the same alphabet have n and m states. Their complete product automaton tracks ordered state pairs. Which accepting-pair choices recognize the specified language?

A. Both component states accepting: L(D1)∩L(D2).
B. Exactly one component state accepting: the symmetric difference of the languages.
C. At least one component state accepting: the concatenation L(D1)L(D2).
D. First component accepting and second not accepting: L(D1)−L(D2).

### Q54. [2 Marks] [MSQ]

Transactions obey basic two-phase locking: a growing phase acquires locks, and after the first unlock no more locks may be acquired. Exclusive locks conflict with every other transaction's lock on that item; shared locks conflict with exclusive locks. Locks need not be held until commit. Which statements are correct?

A. Every resulting complete schedule is conflict serializable.
B. Cascading aborts are impossible.
C. Deadlock is possible.
D. Holding all exclusive locks until commit is a stronger restriction that prevents another transaction from reading an uncommitted written value.

### Q55. [2 Marks] [NAT]

In grammar S→ABA, A→a | ε, B→b | ε, eliminate epsilon productions while preserving ε in the language by allowing S→ε. Obtain S alternatives by deleting any subset of nullable occurrences from ABA, retain distinct resulting right-hand sides only, and retain S→ε once. How many distinct productions have left-hand side S after this step?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

A toy normalized binary floating-point system has four significant bits, including the leading 1, and exponents large enough to avoid overflow and underflow. Each addition is rounded to nearest, ties to even. Let a=16, b=1, c=−16. What is the value of (a⊕b)⊕c, where ⊕ denotes a rounded addition?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

A queue is implemented with an input stack and an output stack. Enqueue pushes onto the input stack. Dequeue pops the output stack; if it is empty, all items from the input stack are first moved to it, one pop and one push per item. Count only individual stack pushes and pops. Starting empty, perform enqueue(A), enqueue(B), dequeue, enqueue(C), enqueue(D), dequeue, dequeue. How many stack operations are performed in total?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

CPU instructions each take one bus-available cycle. Beginning at cycle 1, a DMA device steals every fourth cycle (4,8,12,...) until it has completed 64 one-cycle transfers. The CPU must execute 100 instructions and cannot progress during stolen cycles. At the end of which cycle does its 100th instruction finish?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A full binary tree, in which every node has zero or two children, has 19 nodes. Exactly four internal nodes have two leaf children each. How many leaves have a sibling that is an internal node?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

Distinct keys are inserted into an unbalanced BST. Which statements are correct?

A. Inserting sorted ascending keys can produce height n−1 for n keys, counting edges.
B. The inorder traversal is sorted regardless of insertion order.
C. Every insertion order produces the same tree shape.
D. A sorted inorder traversal proves that search always takes logarithmic time.

### Q61. [2 Marks] [NAT]

A positive binary floating-point format has two exponent bits and two stored fraction bits. Exponent fields 01 and 10 represent normalized values (1.f)×2^(E−1), where E is the unsigned exponent-field value. Field 00 represents subnormals (0.f)×2⁰; field 11 is reserved. What is the ratio of the largest finite positive value to the smallest positive value?

**Answer format:** Integer.

### Q62. [2 Marks] [MSQ]

Random variables X∈{1,2} and Y∈{0,1} have joint probabilities P(X=x,Y=y)=c(x+y), for a normalizing constant c. Which statements are correct?

A. c=1/8.
B. X and Y are independent.
C. P(Y=1)=5/8.
D. E[X|Y=0]=5/3.

### Q63. [2 Marks] [NAT]

For relation R(A,B,C,D), F={AB→C, C→D, D→A}. How many candidate keys does R have?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

Two Ethernet stations independently choose backoff counters uniformly from{0,1,2,3} after the same collision. Under the simplified model that only equal counters cause another collision, what is the probability that one station selects a counter exactly one larger than the other?

**Answer format:** Exact decimal.

### Q65. [2 Marks] [MSQ]

In a compiler's constant lattice, a join keeps a constant only if all reachable incoming values agree. A block has incoming x=5 from one reachable predecessor and x=7 from an unreachable predecessor. Which statements are correct if reachability information is used?

A. The unreachable predecessor need not force x to be nonconstant.
B. x may be propagated as5 at the block's entry.
C. Treating every syntactic predecessor as reachable can lose this optimization.
D. Reachability information never affects constant propagation.

---

## ANSWER KEY — MOCK TEST 100

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 32 |
| 2 | NAT | 1 | 5 (exact) |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 19 |
| 5 | NAT | 1 | 2 (exact) |
| 6 | NAT | 2 | 5 |
| 7 | MSQ | 2 | A, C |
| 8 | NAT | 2 | 18 |
| 9 | NAT | 2 | 25 |
| 10 | NAT | 2 | 6 |
| 11 | MSQ | 1 | A, D |
| 12 | NAT | 1 | 7 |
| 13 | NAT | 1 | 2.6667 (accepted range 2.66665–2.66675) |
| 14 | NAT | 1 | 4 |
| 15 | NAT | 1 | 5 |
| 16 | MCQ | 1 | D |
| 17 | MSQ | 1 | A, B, D |
| 18 | MCQ | 1 | A |
| 19 | MSQ | 1 | A, B, D |
| 20 | NAT | 1 | 4 |
| 21 | NAT | 1 | -0.75 |
| 22 | NAT | 1 | 52 |
| 23 | NAT | 1 | 3 |
| 24 | NAT | 1 | 6 |
| 25 | NAT | 1 | 3 |
| 26 | NAT | 1 | 4 |
| 27 | NAT | 1 | 7 |
| 28 | MSQ | 1 | A, B |
| 29 | MCQ | 1 | B |
| 30 | NAT | 1 | 400 |
| 31 | MCQ | 1 | B |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 4 |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 1.5 |
| 36 | NAT | 2 | 3 |
| 37 | MSQ | 2 | A, C, D |
| 38 | MSQ | 2 | A, C, D |
| 39 | NAT | 2 | 174 |
| 40 | MSQ | 2 | B, D |
| 41 | MSQ | 2 | A, C |
| 42 | NAT | 2 | 3 |
| 43 | NAT | 2 | 4 (exact) |
| 44 | NAT | 2 | 1 |
| 45 | NAT | 2 | 1 |
| 46 | NAT | 2 | 9 |
| 47 | NAT | 2 | 16 |
| 48 | MSQ | 2 | A, B, D |
| 49 | NAT | 2 | 167 (exact) |
| 50 | NAT | 2 | 1 |
| 51 | NAT | 2 | 17 |
| 52 | NAT | 2 | 3 |
| 53 | MSQ | 2 | A, B, D |
| 54 | MSQ | 2 | A, C, D |
| 55 | NAT | 2 | 7 |
| 56 | NAT | 2 | 0 |
| 57 | NAT | 2 | 15 |
| 58 | NAT | 2 | 133 |
| 59 | NAT | 2 | 2 |
| 60 | MSQ | 2 | A, B |
| 61 | NAT | 2 | 14 |
| 62 | MSQ | 2 | A, C, D |
| 63 | NAT | 2 | 3 |
| 64 | NAT | 2 | 0.375 |
| 65 | MSQ | 2 | A, B, C |
