# GATE CS 2027 — Full-Length Mock Test 030

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. The180-minute examination allocates15 marks to General Aptitude,13 to Engineering Mathematics, and72 to core Computer Science.

MCQs have exactly one correct choice. MSQs have multiple correct choices and receive credit only for selecting all and only those choices. An incorrect one-mark MCQ loses1/3 mark; an incorrect two-mark MCQ loses2/3 mark. MSQ and NAT questions have no negative marking. Unattempted questions receive zero; no partial credit applies. NAT answers must use the stated precision. The answer key follows Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MSQ]

Every approved design is either tested or exempt, but never both. No exempt design uses material M. Design D is approved and uses material M. Which conclusions follow?

A. D is tested.
B. D is exempt.
C. D is not exempt.
D. Every tested design uses material M.

### Q2. [1 Mark] [NAT]

An ordered triangle has vertices A=(0,0),B=(4,0),C=(0,3). Reflect all its vertices across the y-axis, rotate them90 degrees counterclockwise about the origin, then translate them by(7,−2). What is the signed area of the resulting ordered triangle, with counterclockwise orientation positive?

**Answer format:** Exact signed number.

### Q3. [1 Mark] [MCQ]

A notice says: “Applications received after Friday will be considered only if places remain.” Which conclusion is justified?


A. Every late application will be accepted if a place remains.
B. Applications submitted before Friday are considered only if places remain.
C. Every application received by Friday will be accepted.
D. No late application can be considered when all places have been filled.

### Q4. [1 Mark] [NAT]

How many distinct arrangements of the multiset A,A,B,B,C,C contain no two identical letters next to each other?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A school has two classes. In the first,18 of30 students passed an examination. Across both classes,42 of60 students passed. What percentage of the second class passed?

**Answer format:** Exact percentage without the percent sign.

### Q6. [2 Marks] [NAT]

A rectangular sheet spans0≤x≤8 and0≤y≤2. Fold the left half onto the right along x=4. Then fold the part of that packet with6≤x≤8 onto4≤x≤6 along x=6. Cut straight through all layers along x=5 for the full height of the folded packet. After unfolding and separating along the cuts, how many connected pieces remain? Creases alone do not separate pieces.

**Answer format:** Integer.

### Q7. [2 Marks] [MSQ]

An investigation records: “The alarm sounded before the operator entered. The operator entered before the inspection began. The inspection began before the leak was found.” A later summary adds statements below. Which are compatible with the original record, without assuming any unstated duration or cause?

A. The leak was found before the alarm sounded.
B. The alarm sounded before the inspection began.
C. The leak already existed before the operator entered.
D. The operator entered after the leak was found.

### Q8. [2 Marks] [NAT]

Three counters are drawn independently with replacement from a box containing one counter of each of four colours. What is the expected number of distinct colours observed?

**Answer format:** Exact decimal.

### Q9. [2 Marks] [MCQ]

“The new measurement corroborates the earlier report, although it does not establish the proposed explanation.” Which paraphrase preserves both claims?


A. The measurement supports the report but does not by itself prove the explanation.
B. The measurement contradicts the report and disproves its explanation.
C. The measurement proves the report and every explanation consistent with it.
D. The measurement merely repeats the wording of the report without supplying evidence.

### Q10. [2 Marks] [NAT]

How many distinct positive integers N≤72 can be written as N=2^a·3^b with nonnegative integers a,b and are divisible by6?

**Answer format:** Integer.
## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A deterministic Turing machine on a fixed input is forbidden to visit more than100 tape cells. Its finite state set and tape alphabet are known. Which statements are correct?

A. Whether it halts can be decided by simulating until halting or a repeated complete configuration.
B. Every such machine must halt.
C. Only finitely many complete configurations are possible on that input.
D. This establishes decidability of unrestricted Turing-machine halting.

### Q12. [1 Mark] [NAT]

A process has three resident writable pages and forks using copy-on-write, initially sharing all three frames with its child. The parent writes page0 twice, then the child writes page1 once. No page is otherwise allocated or evicted. What is the peak number of physical frames holding these pages across both processes?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A real3×3 matrix A satisfies A²=A and has rank2. What is det(A+2I)?

**Answer format:** Exact number.

### Q14. [1 Mark] [MSQ]

All operands below are unsigned n-bit integers, and operations wrap modulo2^n. Evaluating operands has no side effects. Which rewrites preserve both definedness and value for every input? Division by zero is undefined.

A. x*(y+z) to x*y+x*z
B. x/x to1, including when x=0
C. x*0 to0
D. x−y to y−x for every n≥2

### Q15. [1 Mark] [NAT]

For x≥0, let f(x)=x² exp(−x). What is its global maximum value?

**Answer format:** Decimal rounded to four places.

### Q16. [1 Mark] [MSQ]

Events A,B have P(A)=0.8 and P(B)=0.7. Which additional specifications are individually consistent with these two probabilities?

A. P(A∩B)=0.4
B. P(A∩B)=0.6
C. P(A|B)=0.5
D. P(A∪B)=1

### Q17. [1 Mark] [NAT]

A recovery system redoes committed updates and undoes uncommitted updates using durable before-and-after log records. Initially x=5,y=7. T1 logs x:5→8 and commits, but its updated data page has not been flushed. T2 logs y:7→9 and its data page is flushed, but T2 has not committed when a crash occurs. All mentioned log records and T1's commit record are durable. What is x+y after recovery?

**Answer format:** Integer.
### Q18. [1 Mark] [MSQ]

Order the set{1,2,3,4,12} by divisibility. Which statements are correct?

A. This poset is a lattice.
B. This lattice is distributive.
C. The join of2 and3 is12.
D. The meet of4 and3 is1.

### Q19. [1 Mark] [MCQ]

A timestamp protocol handles a write by transaction timestamp t as follows: abort if t<readTS(x); otherwise ignore the write if t<writeTS(x); otherwise perform it. Initially readTS(x)=5 and writeTS(x)=9. Two separate attempts are considered from this same initial state, with t=7 and t=4. What are their respective outcomes?


A. Perform, ignore
B. Abort, ignore
C. Ignore, abort
D. Perform, abort

### Q20. [1 Mark] [MSQ]

A four-variable function, with bit order A,B,C,D from most to least significant, is1 exactly at minterms0,2,8,10. Which statements are correct?

A. These four minterms form a single valid four-cell Karnaugh-map group.
B. A must be fixed to one value throughout that group.
C. C must be fixed to one value throughout that group.
D. The group is represented by (NOT B) AND (NOT D).
### Q21. [1 Mark] [MSQ]

An invertible matrix A has factorization A=LU, with L unit lower triangular and U upper triangular. To solve Aᵀx=b, which statements are correct?

A. Aᵀ=UᵀLᵀ.
B. Solving Lᵀy=b and then Uᵀx=y always gives the desired x.
C. One can first solve Uᵀy=b, then Lᵀx=y.
D. Lᵀ is unit upper triangular.

### Q22. [1 Mark] [NAT]

A file occupies eight data blocks. Its only directory link is removed while one process still has the file open. Assume blocks are reclaimed only when both link count and open-reference count become zero. How many of its data blocks are reclaimed by this unlink operation itself?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A sliding-window minimum algorithm maintains a deque of indices. Before inserting each new index i, it removes expired indices from the front, then removes indices from the back while their values are at least the new value, then appends i. The window length is3. Starting empty, process values[4,2,3,1] from left to right. How many removals from the back occur in total?

**Answer format:** Integer.
### Q24. [1 Mark] [NAT]

A process opens the same file twice, obtaining independent open file descriptions at offset0, with descriptors a and b. It reads3 bytes through a, then executes dup2(a,b), replacing b's reference by a duplicate of a. It next reads2 bytes through b. All reads return the requested counts. What offset is now observed through a?

**Answer format:** Integer bytes.

### Q25. [1 Mark] [NAT]

An undirected tree has edges1–2,1–3,2–4,2–5,3–6. Root the tree at vertex4. What is the label of the lowest common ancestor of vertices5 and6?

**Answer format:** Integer vertex label.

### Q26. [1 Mark] [MSQ]

A Boolean minimization problem specifies ON, OFF and don't-care minterms. Which statements are correct?

A. A valid implicant may cover don't-care minterms as well as ON minterms.
B. Every don't-care minterm must be covered by the final expression.
C. No selected implicant may cover an OFF minterm.
D. A cube containing only don't-care minterms must appear in every minimum cover.

### Q27. [1 Mark] [NAT]

A scalar constant-propagation analysis sees three incoming paths to a join. Two set x=4; the third is provably unreachable and would set x=9. If unreachable paths are excluded, what constant value can be assigned to x at the join?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A dynamic program counts ordered sequences of steps of sizes1 or2 whose sum is4, but forbids two consecutive size1 steps. How many sequences are counted?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

A router runs link-state routing. Assume all routers have received the same complete link-state database and use the same positive link costs. Which statements are correct?

A. Routers can independently compute shortest paths from that database.
B. Each router needs only its neighbours' currently advertised distances, with no topology information.
C. Different source routers may obtain different shortest-path trees from the same database.
D. Identical topology information forces every router to choose the same next hop for a fixed destination.

### Q30. [1 Mark] [NAT]

A cache stores64 data bytes in four-byte blocks and is four-way set associative. How many sets does it contain?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

An IPv4 fragment has fragment offset75 and carries240 bytes of payload. What is the offset, in bytes from the original datagram payload's beginning, of its final payload byte? Offset fields are in eight-byte units.

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

In an ordinary BST with distinct keys, a node v has both children and its inorder successor s has a right child. Which statements are correct?

A. s has no left child.
B. s must be v's immediate right child.
C. Removing s from its old position can reconnect its right child to s's former parent.
D. s can have two children.

### Q33. [1 Mark] [NAT]

A peripheral produces one byte every10 microseconds. The CPU polls every25 microseconds, reading and clearing all available bytes instantly. Initially the buffer is empty and a poll occurs at time0; arrivals start at time10. What minimum buffer capacity in bytes avoids overflow indefinitely? If an arrival and poll coincide, the arrival occurs first.

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A DFA tracks the input length modulo2 and the number of a symbols modulo2 over alphabet{a,b}. It starts with both parities even. How many of the four parity-pair states are reachable?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A recursive algorithm on an input of size16 calls itself on sizes n/2 and n/4 whenever n≥4, and stops immediately for n<4. How many leaf calls occur?

**Answer format:** Integer.


### Q36. [2 Marks] [MSQ]

Define MUX(s,u,v) to return u when s=0 and v when s=1. A circuit computes T=MUX(s,a,b), then F=MUX(T,s,NOT s). Which statements are correct?

A. F=(NOT s AND a) OR (s AND NOT b).
B. If a=b, toggling s toggles F.
C. If a and b differ, F is independent of s.
D. F always equals s XOR a XOR b.

### Q37. [2 Marks] [NAT]

A synchronous four-bit register has next-state rule(a,b,c,d)→(b,c,d,a XOR b), evaluated from the old state. Starting from0001, what is the smallest positive number of clock edges after which the register returns to0001?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

A pipeline has four stages whose combinational delays are2,3,10,4ns. Each stage adds1ns register overhead to the clock-period requirement. A redesign splits the10ns stage into two5ns stages with the same overhead per stage. There are100 independent instructions, no stalls, and initially empty pipelines. How many nanoseconds does the redesign save from first launch to the last instruction's completion?

**Answer format:** Integer nanoseconds.

### Q39. [2 Marks] [NAT]

Evaluate the integral from0 to2 of |x²−1| with respect to x.

**Answer format:** Exact number.

### Q40. [2 Marks] [MSQ]

A weak entity Room is identified by the pair(BuildingID,RoomNumber). RoomNumber is unique only within a building. Which statements are correct?

A. Rooms in different buildings may share a RoomNumber.
B. RoomNumber alone necessarily identifies a room globally.
C. The owner's identifier contributes to the weak entity's identification.
D. Moving a room record to another building can cause an identifier collision if that building already has the same RoomNumber.

### Q41. [2 Marks] [NAT]

In the following control flow, p is an unchanged input Boolean. All named values use mathematical integer semantics.

```text
Entry: a = 0; goto Loop
Loop:  b = a + 1
       if p goto Again else goto Exit
Again: a = b; goto Loop
Exit:  return a
```

Under standard backward may-liveness analysis, how many named variables are live immediately after b=a+1 and before the conditional test in Loop?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

A block computes t=a+b, then branches. Path P executes a=a+1, while path Q changes neither a nor b. At the join, u=a+b is computed. Arithmetic is over mathematical integers. Which statements are correct?

A. On path P, the join expression equals t+1.
B. Replacing u by t on both paths is valid.
C. The original t is overwritten by updating a.
D. Selecting t+1 for path P and t for path Q preserves u.

### Q43. [2 Marks] [MSQ]

A completed depth-first search of a directed graph assigns discovery/finish times u:(2,9), v:(4,7), and w:(10,13), using one global clock. Which statements are correct?

A. v is a descendant of u in the DFS forest.
B. If edge v→u exists, it is a back edge.
C. If edge u→v exists, it must be a tree edge rather than a forward edge.
D. An edge v→w could be present with these timestamps in that completed DFS.

### Q44. [2 Marks] [NAT]

A process has three threads. One thread forks under a model in which the parent retains all threads and the child initially has only the calling thread. After the fork, each process creates two additional threads; none exit. How many threads exist in total across the two processes?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A grammar has S→ABA, A→a | ε, B→b | ε. When eliminating epsilon productions, form S's nonempty right-hand sides by independently retaining or omitting nullable occurrences in ABA, then remove duplicate right-hand sides. How many distinct nonempty right-hand sides result for S?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A one-based min-heap array is[1,10,2,11,12,3,4]. Delete the node at index4 by replacing it with the last entry and removing the last slot. Restore the heap using the necessary upward or downward exchanges. What value ends at index2?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

An undirected graph has edges AB of weight x, BC of weight2, AC of weight5, AD of weight1, and CD of weight4. For how many integer choices x in {0,1,2,3,4,5,6} does the graph have more than one minimum spanning tree?

**Answer format:** Integer.
### Q48. [2 Marks] [NAT]

For observations0,0,4,10, first choose x to minimize the sum of absolute deviations from x. Among all such minimizers, choose x to minimize the sum of squared deviations. What value is selected?

**Answer format:** Exact decimal.

### Q49. [2 Marks] [MSQ]

G is a finite group of odd order, with identity e. An element x satisfies x^4=e and x^6=e. Which statements must hold?

A. x=e.
B. x has order2.
C. x²=e.
D. x has order3.

### Q50. [2 Marks] [MSQ]

A PDA recognizes L and a DFA recognizes R over the same alphabet. To recognize L∩R, one uses a product control state with the PDA's original stack. Which statements are correct?

A. Consuming one input symbol updates both components according to that symbol.
B. Every epsilon transition of the PDA must consume a symbol in the DFA.
C. One stack suffices for this construction.
D. A second unbounded stack is necessary to remember the DFA's state.

### Q51. [2 Marks] [NAT]

Relation E(src,dst) is{(a,b),(b,c),(c,a),(a,c)}. Let P contain all pairs(x,z) for which some y satisfies E(x,y) and E(y,z), using set semantics. How many pairs belong to P−E?

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

A lexer uses maximal munch with tokens HEX=0x[0-9A-F]+ and ID=[A-Z]+. No rule requires whitespace between tokens. On the input0x1G, which statements are correct?

A. The lexer can return HEX with lexeme0x1 followed by ID with lexemeG.
B. The entire input must be one valid HEX token because it starts with0x.
C. Successful tokenization alone does not prove that the token sequence is a valid expression in the parser's grammar.
D. G is a valid hexadecimal digit under the given HEX rule.

### Q53. [2 Marks] [NAT]

Represent exactly the address set10.1.0.0/24 excluding10.1.0.64/26 as a union of CIDR prefixes, without including any excluded address. What is the minimum number of prefixes needed?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

Define sat(x)=min(7,max(−8,x)). All additions below apply this signed four-bit saturation after each addition. For a=7,b=3,c=−3, calculate sat(sat(a+b)+c)−sat(a+sat(b+c)).

**Answer format:** Exact signed integer.

### Q55. [2 Marks] [NAT]

A bipartite graph has left vertices a,b,c,d and right vertices1,2,3,4. Vertices a,b are adjacent only to1, while c,d are adjacent only to2. How many unordered pairs of currently absent edges, when added together, make a perfect matching possible?

**Answer format:** Integer.
### Q56. [2 Marks] [NAT]

A stack machine stores four-byte integers. PUSH first subtracts4 from SP, then writes at the new SP. POP reads at SP, then adds4 to SP. Initially SP=100. Execute PUSH7, PUSH9, POP into R, then store R at address SP+4, then POP into S. What is R+S? The stack is ordinary writable memory and all addresses are valid.

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

A directed graph has edges s→a(1),s→b(4),b→a(−5),a→t(1),b→t(10). An implementation runs Dijkstra's algorithm and terminates as soon as t is extracted as minimum, despite the negative edge. What is its reported distance minus the actual shortest s-to-t distance?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

Two processes communicate using two separate FIFO channels, one in each direction. Each channel has a positive integer capacity measured in messages. Each process sends two messages to the other, then receives two. A send blocks only while its channel is full; a receive blocks only while its channel is empty. Under fair execution, what is the minimum sum of the two channel capacities that guarantees completion?

**Answer format:** Integer.

### Q59. [2 Marks] [MSQ]

L is context-free and R is regular. Which languages are necessarily context-free?

A. L∩R
B. L∪R
C. The complement of L
D. The concatenation LR

### Q60. [2 Marks] [NAT]

A directed graph on vertices0,1,2,3 is stored in CSR form with row offsets[0,2,3,5,5] and neighbour array[1,3,2,0,3]. Reverse every edge and build CSR again, retaining the same vertex order. What is the new row offset for vertex3?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

A one-slot producer–consumer buffer uses semaphores empty=1 and full=0. The producer incorrectly performs wait(empty), signal(full), then writes the item. The consumer performs wait(full), reads the item, signal(empty). Assume semaphore operations are atomic and scheduling may switch between any two operations. Which statements are correct?

A. The consumer can read before the producer writes the new item.
B. Atomic semaphore operations alone eliminate this ordering error.
C. Moving the producer's signal(full) after the write repairs this particular publication error.
D. The consumer's wait(full) forces all future producer writes to occur before its read.

### Q62. [2 Marks] [MSQ]

Relations R(x),S(x) are finite but the underlying value domain is infinite. Which formulas, with x free, always return a finite set of values?

A. R(x) AND NOT S(x)
B. NOT R(x)
C. R(x) OR S(x)
D. NOT R(x) AND NOT S(x)

### Q63. [2 Marks] [NAT]

A translator has one public IPv4 address and six available public source ports. It distinguishes mappings using the public source port together with the remote IP-and-port endpoint. It permits reuse of a public port for different remote endpoints, but not for the same remote endpoint. Connections target exactly two distinct remote endpoints. What is the maximum number of simultaneous mappings under this model?

**Answer format:** Integer.

### Q64. [2 Marks] [MCQ]

What pair is printed by this C program? The && operator short-circuits and sequences evaluation of its left operand before its right operand.

```c
#include <stdio.h>
int main(void) {
    int a[5] = {1,2,0,4,5};
    int i = 0, sum = 0;
    while (i < 5 && a[i++] > 0)
        sum += a[i];
    printf("%d %d\n", i, sum);
    return 0;
}
```

A. 2 3
B. 3 2
C. 2 2
D. 3 3

### Q65. [2 Marks] [NAT]

A TCP receiver's cumulative ACK is1000 and its advertised receive window is1200 bytes. A sender has already transmitted bytes1000 through1799 inclusive, none cumulatively acknowledged yet. Its congestion window is1500 bytes. Assume no window changes, losses, retransmissions or extra data already in flight. How many additional consecutive bytes may it send immediately under both limits?

**Answer format:** Integer.



---

## ANSWER KEY — MOCK TEST 030

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C |
| 2 | NAT | 1 | -6 |
| 3 | MCQ | 1 | D |
| 4 | NAT | 1 | 30 |
| 5 | NAT | 1 | 80 |
| 6 | NAT | 2 | 5 |
| 7 | MSQ | 2 | B, C |
| 8 | NAT | 2 | 2.3125 |
| 9 | MCQ | 2 | A |
| 10 | NAT | 2 | 8 |
| 11 | MSQ | 1 | A, C |
| 12 | NAT | 1 | 5 |
| 13 | NAT | 1 | 18 |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 0.5413 (accepted range 0.54125–0.54135) |
| 16 | MSQ | 1 | B, D |
| 17 | NAT | 1 | 15 |
| 18 | MSQ | 1 | A, C, D |
| 19 | MCQ | 1 | C |
| 20 | MSQ | 1 | A, D |
| 21 | MSQ | 1 | A, C, D |
| 22 | NAT | 1 | 0 |
| 23 | NAT | 1 | 3 |
| 24 | NAT | 1 | 5 |
| 25 | NAT | 1 | 2 |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 4 |
| 28 | NAT | 1 | 2 |
| 29 | MSQ | 1 | A, C |
| 30 | NAT | 1 | 4 |
| 31 | NAT | 1 | 839 |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 3 |
| 34 | NAT | 1 | 4 |
| 35 | NAT | 1 | 5 |
| 36 | MSQ | 2 | A, B, C |
| 37 | NAT | 2 | 15 |
| 38 | NAT | 2 | 509 |
| 39 | NAT | 2 | 2 |
| 40 | MSQ | 2 | A, C, D |
| 41 | NAT | 2 | 3 |
| 42 | MSQ | 2 | A, D |
| 43 | MSQ | 2 | A, B |
| 44 | NAT | 2 | 8 |
| 45 | NAT | 2 | 6 |
| 46 | NAT | 2 | 4 |
| 47 | NAT | 2 | 1 |
| 48 | NAT | 2 | 3.5 |
| 49 | MSQ | 2 | A, C |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 4 |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 2 |
| 54 | NAT | 2 | -3 |
| 55 | NAT | 2 | 8 |
| 56 | NAT | 2 | 16 |
| 57 | NAT | 2 | 2 |
| 58 | NAT | 2 | 3 |
| 59 | MSQ | 2 | A, B, D |
| 60 | NAT | 2 | 3 |
| 61 | MSQ | 2 | A, C |
| 62 | MSQ | 2 | A, C |
| 63 | NAT | 2 | 12 |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 400 |
