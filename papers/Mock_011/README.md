# GATE CS 2027 — Full-Length Mock Test 011

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the other questions carry two marks each. Choose exactly one option for MCQ and all correct options for MSQ. MSQs award no partial credit. Incorrect MCQs lose one-third of their marks; incorrect MSQ/NAT responses and unattempted questions score zero. GA, Engineering Mathematics and core CS contribute 15,13,72 marks respectively. NAT precision is specified individually. Use the assumptions given in each question; arithmetic is exact unless rounding is requested.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“A library extended its opening hours. Evening attendance increased, but total daily attendance remained unchanged.” Which interpretation is consistent with both observations?

A. Some visits shifted from earlier hours to the evening.
B. Total daily attendance necessarily increased.
C. Earlier attendance necessarily increased too.
D. The library must have measured attendance incorrectly.

### Q2. [1 Mark] [NAT]

Three of seven seats in a row are to be marked reserved. No two reserved seats may be adjacent. How many different sets of reserved seats are possible?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A shop sells 40 items at a 25% profit on their individual cost and 60 items at a 10% loss. Every item has the same cost price. What is the overall profit percentage on the total cost?

**Answer format:** Integer percentage, without the percent sign.

### Q4. [1 Mark] [MCQ]

A square paper is folded once along its vertical midline. A small circular hole is punched through both layers away from the fold and away from the edges. After unfolding, which statement must hold about the two holes?

A. They are images of each other under reflection in the fold line.
B. They necessarily lie on the fold line.
C. Their distance apart equals the side of the original square.
D. Their positions are related by a 90-degree rotation about the centre for every punch location.

### Q5. [1 Mark] [MCQ]

Choose the order that gives the clearest causal sequence.

P. The alarm then sounded as designed.
Q. The technician first disconnected the sensor's power supply.
R. This demonstrated that the system detected the simulated failure.
S. The disconnection removed the sensor's normal signal.

A. Q–S–P–R
B. P–Q–R–S
C. S–R–Q–P
D. Q–R–S–P

### Q6. [2 Marks] [NAT]

A three-question quiz has four options per question and exactly one correct option each. A student independently guesses uniformly on every question. Each correct answer scores 3 and each wrong answer scores −1. Given that the student's total score is positive, what is the probability that exactly two answers were correct? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q7. [2 Marks] [MCQ]

“The evaluator called the design economical, not because it was cheap to manufacture, but because each component served several purposes.” Which interpretation best preserves the stated distinction?

A. The evaluator praised efficient use of components without asserting low manufacturing cost.
B. The evaluator established that manufacturing was inexpensive.
C. The design uses no components.
D. Multifunctional components necessarily increase manufacturing cost.

### Q8. [2 Marks] [NAT]

A population starts at 800, increases by 25% in the first year, decreases by 20% in the second, and increases by 10% in the third. What constant annual percentage growth rate over the same three years gives the same final population? Round to two decimal places.

**Answer format:** Number to 2 decimal places, without the percent sign.

### Q9. [2 Marks] [MCQ]

Town A introduced a road-safety campaign and its accident count fell by 20%. During the same period a similar town without the campaign also had a 20% fall. Which conclusion is most defensible from these facts alone?

A. The campaign certainly caused all of A's reduction.
B. The campaign certainly had no effect whatsoever.
C. A common external change could explain both reductions; these counts alone do not isolate the campaign's effect.
D. Accident counts in different towns must always move together.

### Q10. [2 Marks] [NAT]

A rectangular solid has side lengths 4,3,2 units. Its exterior is painted, then it is cut into unit cubes along integer coordinate planes. How many unit cubes have paint on exactly two faces?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A depth-first search of an undirected simple graph records parent pointers. Which statements hold?

A. Every edge joining an ancestor to a descendant can be represented as a tree edge or a back edge.
B. A non-tree edge necessarily joins vertices in unrelated DFS subtrees.
C. An edge to the parent should not by itself be treated as evidence of a cycle.
D. DFS discovery order must equal breadth-first discovery order.

### Q12. [1 Mark] [MCQ]

Two threads in the same ordinary process have different stack pointers but access the same heap object without synchronization. Which statement is correct?

A. Distinct stacks imply their heap writes cannot race.
B. Shared address-space access permits a data race despite separate stacks.
C. Sharing the heap requires the threads to share the same stack pointer.
D. Each thread automatically receives a private copy of every heap allocation.

### Q13. [1 Mark] [NAT]

Evaluate ∫ from −1 to 1 of (x cos x + x²) dx. Angles are in radians. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q14. [1 Mark] [MCQ]

What is the smallest single CIDR block containing both 10.0.4.0/24 and 10.0.5.0/24, without covering any additional /24 block? Use canonical network-address notation with all host bits zero.

A. 10.0.4.0/23
B. 10.0.4.0/22
C. 10.0.5.0/23
D. 10.0.0.0/21

### Q15. [1 Mark] [NAT]

Insert 8,3,10,1,6,4,7 into an initially empty ordinary binary search tree, with no rebalancing. Delete key 3 by replacing it with its inorder successor and then removing that successor's old node. What is the key of the left child of node 6 after deletion?

**Answer format:** Enter -1 if the child is absent; otherwise enter its key.

### Q16. [1 Mark] [MCQ]

Which conclusion is logically justified by the regular-language pumping lemma alone?

A. If a language violates the lemma's pumping property, it is not regular.
B. If a language satisfies the pumping property, it must be regular.
C. Every infinite language is nonregular.
D. Every regular language has exactly one pumping length.

### Q17. [1 Mark] [NAT]

Five observations are 2,4,x,8,11, and their arithmetic mean is 6. What is their median?

**Answer format:** Integer.

### Q18. [1 Mark] [MSQ]

Processes communicate through a bounded message queue. A send blocks when the queue is full, and a receive blocks when it is empty. Which statements are correct?

A. A blocked sender can become eligible to proceed after a receive removes an item.
B. Bounded buffering alone guarantees absence of deadlock in every application using the queue.
C. Blocking communication can synchronize processes without busy waiting by the blocked process.
D. The queue can hold arbitrarily many unreceived messages.

### Q19. [1 Mark] [NAT]

A byte-addressed 64 KiB memory is built from 16 KiB × 8-bit chips. Address lines not connected to a chip's internal address pins select the chip through a decoder. How many address bits are used for chip selection?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

M is a finite monoid with identity e. Every element a has a right inverse b satisfying ab=e. Which statements necessarily hold?

A. Every element has a two-sided inverse.
B. M is a group.
C. M must be commutative.
D. The right inverse of an element can be chosen arbitrarily from M.

### Q21. [1 Mark] [MCQ]

In ordinary constant propagation, one predecessor of block B assigns x=4 and another assigns x=7. Both paths are feasible. No assignment to x occurs at B before its first use. What can be concluded at entry to B?

A. x is the constant 4.
B. x is the constant 7.
C. x is not a single known constant at this merge.
D. x is uninitialized on both paths.

### Q22. [1 Mark] [NAT]

A port-address translator has one public IPv4 address and may allocate any source port from 40000 through 40099 inclusive. It must assign distinct translated source ports to simultaneous TCP connections that all contact the same external address and port. What is the maximum number of such connections it can distinguish using this pool?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A memory system has a 2 ns cache lookup time and a 5% miss rate. A miss adds 60 ns after the cache lookup, with no overlap. What is the average memory access time?

**Answer format:** Integer nanoseconds.

### Q24. [1 Mark] [MCQ]

A combinational block receives two bits a,b and must output 1 exactly when the two-bit unsigned value is prime. Which output function is correct?

A. a
B. b
C. a XOR b
D. a AND b

### Q25. [1 Mark] [MSQ]

A compiler removes an assignment to scalar x as dead code. The right-hand side has no side effects, exceptions, or observable traps. Which conditions support removal?

A. On every outgoing path, x is redefined before its current value is read, or execution ends without reading it.
B. x is read on at least one outgoing path before redefinition.
C. x is not live immediately after the assignment.
D. x has a short variable name.

### Q26. [1 Mark] [MCQ]

Consider `p=a*b; a=read_input(); q=a*b;`. Scalars do not alias, but read_input may return any value. Why is replacing the final a*b by p generally invalid?

A. Multiplication is never eligible for common-subexpression elimination.
B. Operand a may have changed since p was computed.
C. b must have changed.
D. p must be uninitialized.

### Q27. [1 Mark] [NAT]

A physically addressed direct-mapped cache holds 4 KiB of data in 64-byte lines. Physical addresses are 24 bits and memory is byte-addressed. How many bits are in each cache tag?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

A machine enumerates all binary strings and runs an effective test that halts and accepts exactly on strings belonging to a decidable language L. It prints the accepted strings, one at a time. If L is finite, which statement follows?

A. The enumeration must automatically know when its last output has been printed.
B. Enumeration can continue forever after its last output without contradicting correctness.
C. L becomes undecidable because enumeration is infinite.
D. The empty language cannot be enumerated.

### Q29. [1 Mark] [NAT]

An undirected graph is formed from a triangle on a,b,c by adding edges cd and de, with new vertices d,e. How many articulation vertices does it have?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

A binary min-heap stored from index 1 is [2,5,3,9,7,8]. Insert 1 by placing it at the next free index and repeatedly exchanging it with its parent while smaller. How many exchanges occur?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

An undirected connected graph has a unique minimum-weight edge e crossing a particular nontrivial cut. Which statements hold?

A. Every MST contains e.
B. No MST can contain any other edge crossing that cut.
C. Adding e to an MST that omitted it would allow a strictly lighter crossing edge exchange, contradicting minimality.
D. e must be a bridge in the original graph.

### Q32. [1 Mark] [NAT]

Under set semantics R(A)={1,2,3}, S(A)={2,4}, and T(A)={1,4}. How many tuples are in (R−S)∪(S∩T)?

**Answer format:** Integer.

### Q33. [1 Mark] [MCQ]

A positive-edge-triggered D flip-flop has asynchronous active-low reset. Its clock remains low while reset is asserted. What happens to Q?

A. Q resets without waiting for a rising clock edge.
B. Q can change only at the next rising edge, even under reset.
C. Q must toggle repeatedly while reset remains asserted.
D. Q becomes equal to the complement of D.

### Q34. [1 Mark] [MCQ]

Which tuple-calculus expression describes employees e who work in every department listed in relation Department? Works(e,d) records an assignment.

A. Employee(e) ∧ ∀d(Department(d) → Works(e,d))
B. Employee(e) ∧ ∃d(Department(d) ∧ Works(e,d))
C. Employee(e) ∧ ∀d(Department(d) ∧ Works(e,d))
D. Employee(e) ∧ ¬∃d Works(e,d)

### Q35. [1 Mark] [NAT]

Among permutations π of {1,2,3,4,5}, how many satisfy π(1)≠1 and π(2)≠2? No restriction is placed on the other positions.

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

Table A(id) contains rows 1,2,3. Table B(id,v) contains (1,5),(1,NULL),(2,NULL). Evaluate the query under ordinary SQL bag and NULL semantics:

```sql
SELECT COUNT(B.v)
FROM A LEFT JOIN B ON A.id = B.id;
```

What integer does it return?

**Answer format:** Integer.

### Q37. [2 Marks] [MCQ]

Two threads execute the following operations on atomic Boolean flags, initially false, under sequential consistency:

```text
Thread 0: flag0 = true; while (flag1) {} ; critical_section; flag0 = false;
Thread 1: flag1 = true; while (flag0) {} ; critical_section; flag1 = false;
```

Which assessment is correct?

A. Mutual exclusion can fail because both flags may be false at the start.
B. Mutual exclusion holds, but both threads can wait forever after setting their flags.
C. Both mutual exclusion and progress are guaranteed.
D. The algorithm implements strict alternation using a turn variable.

### Q38. [2 Marks] [NAT]

A lexer recognizes keywords `if`, identifiers matching `[a-z]+`, and single-character operators `<` and `=`. It uses maximal munch, breaking equal-length keyword/identifier ties in favour of the keyword. For input `ifx<if==x`, how many tokens are identifiers? There are no multi-character operators in this language.

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

A directed acyclic graph has edges s→a of weight 4, s→b of weight 2, a→b of weight −3, a→t of weight 4, b→t of weight 2. How many distinct s-to-t paths have total weight at most 4?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

An undirected simple graph with n vertices and m edges is represented either by a Boolean adjacency matrix or adjacency lists. Lists are unsorted and store each undirected edge twice. Which worst-case bounds hold?

A. The matrix uses Θ(n²) entries even for an empty graph.
B. Enumerating all neighbours of v from the matrix takes Θ(deg(v)) time for every v without extra indexing.
C. Enumerating all neighbours of v from its list takes Θ(1+deg(v)) time, including access to an empty list.
D. The lists require Θ(n+m) storage, including vertex headers.

### Q41. [2 Marks] [NAT]

Run stable insertion sort in increasing order on [4,1,3,1,2]. In each iteration, shift only elements strictly larger than the key one position right. Count only these rightward shifts, not the final placement of the key. How many shifts occur?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

An ordered sequence consists of steps of size 1 or 3 whose sum is 8. How many such sequences contain an even number of size-3 steps, including zero?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A TCP sender has cwnd=10 MSS and advertised receive window rwnd=8 MSS. There are already 6 MSS of unacknowledged data. One arriving cumulative acknowledgment acknowledges 2 MSS and advertises rwnd=5 MSS. Assume cwnd stays 10 MSS and no other acknowledgments arrive. What is the maximum additional data, in MSS units, that the sender may transmit immediately after processing this acknowledgment?

**Answer format:** Integer.

### Q44. [2 Marks] [MCQ]

A partial DFA over {a,b} has states q0,q1,q2, start state q0, and accepting set {q2}. Its only transitions are q0 on a to q1, q1 on a to q2, and q2 on a to q2. Undefined transitions reject. What is the minimum number of states in a complete DFA recognizing the complement of its language over {a,b}*?

A. 4
B. 3
C. 5
D. 6

### Q45. [2 Marks] [MSQ]

Two processes P,Q use single-instance resources A,B. P acquires A then requests B; Q acquires B then requests A. Resources cannot be preempted. Which modifications prevent deadlock in every execution of these two processes?

A. Require both to acquire A before acquiring B.
B. Require a process to acquire both resources atomically or acquire neither.
C. Merely increase each process's CPU priority after it blocks.
D. Allow each process to hold its first resource indefinitely while repeatedly requesting the second.

### Q46. [2 Marks] [NAT]

A device transfers 12,000 bytes in one second. With interrupt-driven I/O, each byte causes an interrupt costing 80 CPU cycles. With DMA, one completion interrupt occurs per 1,000-byte block at a cost of 120 CPU cycles, plus 30 setup cycles per block; ignore all other CPU work and bus stalls. How many CPU cycles are saved by DMA during that second?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

Grammar S→aSbS | bSaS | ε generates equal numbers of a and b. How many distinct strings of length four does it generate? Count strings, not parse trees.

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

Relation Child(cid,pid) has primary key cid and a foreign key pid referencing Parent(pid), whose primary key is pid. Child.pid is nullable and referential integrity uses ordinary SQL semantics without additional restrictions. Which statements are correct?

A. Two Child rows with different cid values may reference the same parent.
B. A non-NULL Child.pid must match a Parent.pid.
C. Every parent must be referenced by at least one child.
D. Child.pid must be unique because it is a foreign key.

### Q49. [2 Marks] [MCQ]

For grammar S→L=R | R, L→*R | id, R→L, consider an LR(0) item set containing S→L·=R and R→L·. In SLR parsing, FOLLOW(R) contains '='. What conflict occurs in the SLR table for lookahead '='?

A. No conflict, because completed items are ignored on '='.
B. Shift–reduce conflict between shifting '=' and reducing R→L.
C. Reduce–reduce conflict between two completed productions shown here.
D. Accept–reduce conflict because every completed item accepts the input.

### Q50. [2 Marks] [MSQ]

The domain is a nonempty set and R is a binary relation. Which implications are valid for every interpretation?

A. (∃y∀x R(x,y)) → (∀x∃y R(x,y))
B. (∀x∃y R(x,y)) → (∃y∀x R(x,y))
C. (∀x∀y R(x,y)) → (∃y∀x R(x,y))
D. (∃x∃y R(x,y)) → (∀x∃y R(x,y))

### Q51. [2 Marks] [NAT]

Relation R(A,B,C,D) has functional dependencies A→B, B→A, AC→D. How many candidate keys does R have?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

Two unsigned eight-bit fixed-point operands each have four fractional bits. Their encoded integers are 24 and 20. Their exact product is rescaled to the same format by dividing the integer product by 16 and rounding to nearest, with ties to even. What encoded integer is stored? No overflow occurs.

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, one cycle each. ALU results can be forwarded from EX/MEM or MEM/WB to EX, but load data becomes available only after MEM. A dependent instruction immediately following a load must stall one cycle. No other stalls occur. For the sequence below, how many total cycles elapse from the first IF through the last WB, starting empty?

```text
load r1, [r0]
add  r2, r1, r3
sub  r4, r2, r5
load r6, [r4]
add  r7, r6, r2
```

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A size-7 hash table uses linear probing with h(k)=k mod 7 and wraparound. Insert 10,17,24,11 in that order into an empty table. Delete 17 by leaving a tombstone. A subsequent unsuccessful search for 31 stops at the first slot that has never been occupied, but passes tombstones. How many slots does this search inspect, including the terminating slot?

**Answer format:** Integer.

### Q55. [2 Marks] [MCQ]

A TCP server has a listening socket and accepts two connections, producing descriptors c1 and c2. It then closes only the listening socket. No shutdown is applied to c1 or c2. Which statement is correct?

A. Both accepted connections necessarily close immediately.
B. c1 and c2 remain usable; closing the listener does not itself close those connected sockets.
C. c1 becomes a new listening socket automatically.
D. The two clients must now share one TCP byte stream.

### Q56. [2 Marks] [NAT]

A toy normalized binary floating-point system has four significant bits, including the leading 1, and exponents large enough to avoid overflow and underflow. Each addition is rounded to nearest, ties to even. Let a=16, b=1, c=−16. What is the value of (a⊕b)⊕c, where ⊕ denotes a rounded addition?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

A compiler translates references to a contiguous three-dimensional array with index ranges −1..1, 2..5, and 0..2, all inclusive. Elements occupy four bytes. Storage is row-major, so the final index varies fastest. The base address denotes element A[−1][2][0]. What byte offset from the base does the compiler generate for A[0][4][1]?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

Three jobs arrive at times 0,1,2 with CPU bursts 7,4,1 respectively. A preemptive shortest-remaining-time scheduler breaks equal remaining-time ties by earlier arrival. Context switches cost zero. What is the total waiting time of the three jobs?

**Answer format:** Integer time units.

### Q59. [2 Marks] [NAT]

A 16-bit instruction set uses variable-length opcodes but fixed-length instructions. There are 8 registers. Type A uses two three-bit register fields and has 32 opcodes. Type B uses one three-bit register field. Opcode prefixes are allocated so no Type B instruction is confused with Type A. All bit patterns not allocated to Type A may be used for Type B, and each Type B opcode must allow all eight registers. What is the maximum number of Type B opcodes?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

What does this conforming C program print?

```c
#include <stdio.h>
void change(int **q, int *r) {
    **q += 2;
    *q = r;
    **q += 3;
}
int main(void) {
    int a = 4, b = 7;
    int *p = &a;
    change(&p, &b);
    printf("%d\n", a + b + *p);
    return 0;
}
```

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

For how many integer values t in {−2,−1,0,1,2} is the following linear system consistent?

```text
x + t*y + z = 1
t*x + y + t*z = 0
x + t*y + z = 1
```

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A browser retrieves one HTML page and then its four images using HTTP without pipelining. Initially no TCP connection exists. Opening a connection costs one RTT, and each complete HTTP request-response costs one RTT; transmission and DNS time are negligible. At most two persistent connections to the server may exist. The browser opens its first connection to fetch the HTML. It may open the second only after receiving the HTML. All images become known then, and requests on different connections can run concurrently. What is the minimum total number of RTTs from starting the first connection until all images have arrived?

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

For a nondeterministic pushdown automaton, compare acceptance by final state and by empty stack, always requiring all input to be consumed. Which statements are correct?

A. Every language accepted by final state has an empty-stack NPDA recognizing the same language.
B. The same NPDA with its transitions unchanged always recognizes the same language under either convention.
C. Every empty-stack NPDA language can also be recognized by a final-state NPDA.
D. Both conventions characterize context-free languages when suitable machine conversions are allowed.

### Q64. [2 Marks] [NAT]

A recursive procedure enumerates subsets of positions 1 through 5 with no two adjacent positions selected. At each position, it always makes a recursive call excluding that position. It also makes a call including it if the previous position was not selected. After position 5 it outputs once and returns. The initial call handles position 1 with no previous position selected. How many nonleaf calls occur, counting separate calls even when their remaining-position arguments coincide?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Define f(x)=ax+b for x<0, f(0)=1, and f(x)=e^(2x) for x>0. Find a+b if f is differentiable at zero.

**Answer format:** Integer.

## ANSWER KEY — MOCK TEST 011

NAT answers are exact except where an accepted rounded range is supplied.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 10 |
| 3 | NAT | 1 | 4 |
| 4 | MCQ | 1 | A |
| 5 | MCQ | 1 | A |
| 6 | NAT | 2 | 0.2432 (range 0.24315–0.24325) |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 3.23 (range 3.225–3.235) |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 12 |
| 11 | MSQ | 1 | A, C |
| 12 | MCQ | 1 | B |
| 13 | NAT | 1 | 0.6667 (range 0.66665–0.66675) |
| 14 | MCQ | 1 | A |
| 15 | NAT | 1 | -1 |
| 16 | MCQ | 1 | A |
| 17 | NAT | 1 | 5 |
| 18 | MSQ | 1 | A, C |
| 19 | NAT | 1 | 2 |
| 20 | MSQ | 1 | A, B |
| 21 | MCQ | 1 | C |
| 22 | NAT | 1 | 100 |
| 23 | NAT | 1 | 5 |
| 24 | MCQ | 1 | A |
| 25 | MSQ | 1 | A, C |
| 26 | MCQ | 1 | B |
| 27 | NAT | 1 | 12 |
| 28 | MCQ | 1 | B |
| 29 | NAT | 1 | 2 |
| 30 | NAT | 1 | 2 |
| 31 | MSQ | 1 | A, C |
| 32 | NAT | 1 | 3 |
| 33 | MCQ | 1 | A |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 78 |
| 36 | NAT | 2 | 1 |
| 37 | MCQ | 2 | B |
| 38 | NAT | 2 | 2 |
| 39 | NAT | 2 | 2 |
| 40 | MSQ | 2 | A, C, D |
| 41 | NAT | 2 | 6 |
| 42 | NAT | 2 | 7 |
| 43 | NAT | 2 | 1 |
| 44 | MCQ | 2 | A |
| 45 | MSQ | 2 | A, B |
| 46 | NAT | 2 | 958200 |
| 47 | NAT | 2 | 6 |
| 48 | MSQ | 2 | A, B |
| 49 | MCQ | 2 | B |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 2 |
| 52 | NAT | 2 | 30 |
| 53 | NAT | 2 | 11 |
| 54 | NAT | 2 | 5 |
| 55 | MCQ | 2 | B |
| 56 | NAT | 2 | 0 |
| 57 | NAT | 2 | 76 |
| 58 | NAT | 2 | 6 |
| 59 | NAT | 2 | 7936 |
| 60 | NAT | 2 | 26 |
| 61 | NAT | 2 | 3 |
| 62 | NAT | 2 | 5 |
| 63 | MSQ | 2 | A, C, D |
| 64 | NAT | 2 | 19 |
| 65 | NAT | 2 | 3 |



