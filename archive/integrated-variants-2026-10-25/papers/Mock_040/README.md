# GATE CS 2027 — Full-Length Mock Test 040

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

“The new procedure reduced measurement variability but did not change the mean measurement.” Which conclusion is supported?

A. Every new measurement equals the old mean.
B. New measurements are less dispersed under the reported variability measure.
C. The mean measurement became zero.
D. The old procedure must have been biased.

### Q2. [1 Mark] [MCQ]

A square paper is folded once along its vertical midline. A small circular hole is punched through both layers away from the fold and away from the edges. After unfolding, which statement must hold about the two holes?

A. They are images of each other under reflection in the fold line.
B. They necessarily lie on the fold line.
C. Their distance apart equals the side of the original square.
D. Their positions are related by a 90-degree rotation about the centre for every punch location.

### Q3. [1 Mark] [MCQ]

Arrange these steps into a logically coherent experimental sequence: P, record the result; Q, formulate a hypothesis; R, design a test of that hypothesis; S, conduct that test.

A. Q–R–S–P
B. R–Q–P–S
C. P–S–R–Q
D. Q–P–R–S

### Q4. [1 Mark] [NAT]

A fair six-sided die is rolled twice independently. What is the probability that the second result exceeds the first? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q5. [1 Mark] [MCQ]

“The grant was contingent on the laboratory obtaining approval.” Which phrase best replaces “contingent on” without changing the meaning?

A. unrelated to
B. dependent on
C. completed before
D. guaranteed despite

### Q6. [2 Marks] [MSQ]

For which of the following real values of x is the equation log_x(16)=log_2(x) defined and true?

A. 4  
B. 1/4  
C. −4  
D. 1

### Q7. [2 Marks] [MSQ]

A proposed rule maps every integer n to n²+n+1. Observations for inputs1,2,3 give outputs3,7,13. Which statements are correct?

A. The proposed rule agrees with all three observations.
B. These observations uniquely establish the rule for every integer input.
C. Adding (n−1)(n−2)(n−3) to the proposed rule gives another rule agreeing with the observations.
D. The proposed rule predicts21 at input4.

### Q8. [2 Marks] [NAT]

Unit cubes are stacked in four columns on a2×2 base. Heights are nonnegative integers. Maximum heights in the first and second rows are3 and1; maximum heights in the first and second columns are2 and3. What is the minimum total number of cubes consistent with these four maxima?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

The three-digit strings000 through111 containing only binary digits are listed in increasing binary numerical order, with leading zeros retained. Between each consecutive pair, count how many digit positions change. What is the sum of these counts over all seven transitions?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

The diagonals of a trapezium ABCD intersect at O, with AB parallel to CD. The areas of triangles AOB and COD are 4 and 9 square units respectively. What is the area of the entire trapezium?

**Answer format:** Integer square units.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A processor issues instructions out of order but commits their architectural results in program order using a reorder buffer. Which mechanism chiefly prevents a younger completed instruction from exposing its architectural result before an older faulting instruction is resolved?

A. In-order commit from the reorder buffer.
B. Issuing every ready instruction as soon as possible.
C. Increasing the number of execution units.
D. Predicting every branch as taken.

### Q12. [1 Mark] [NAT]

A three-input majority gate outputs one exactly when at least two inputs are one. Its input is currently 011. Among the three possible single-input-bit flips, how many change the gate's output?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A process writes a2048-byte buffer using a system call that may complete partially. The first call returns768 and the second, correctly adjusted call returns512. Both returns indicate successfully written bytes. How many buffer bytes remain to be written, assuming no other output occurs?

**Answer format:** Exact integer.

### Q14. [1 Mark] [MCQ]

An open-addressed hash table uses linear probing and tombstones for deletion. During insertion of key k, the first tombstone is encountered before an occupied slot containing k. Duplicate keys are forbidden. What must a correct insertion do?

A. Immediately place a second copy of k in the tombstone.
B. Treat the tombstone as proof that k is absent.
C. Stop searching at every tombstone as if it were never occupied.
D. Continue searching beyond the tombstone to detect the existing key before deciding to insert.

### Q15. [1 Mark] [MCQ]

A transport-layer port number is primarily used to distinguish what?

A. Application endpoints on a host.
B. Individual bits within one Ethernet frame.
C. Physical pins on a memory chip.
D. Cache-line offsets inside a processor.

### Q16. [1 Mark] [MCQ]

a0=0, a1=1 and a_n=3a_(n−1)−2a_(n−2) for n≥2. Which formal generating function equals Σ_(n≥0) a_n x^n?

A. 1/(1−3x+2x²)  
B. x/(1−3x−2x²)  
C. (1−x)/(1−2x)  
D. x/((1−x)(1−2x))

### Q17. [1 Mark] [MSQ]

Over a nonempty domain, consider propositions F=(for every x, P(x) OR Q(x)) and G=((for every x, P(x)) OR (for every x, Q(x))). Which statements are correct?

A. G implies F.
B. F implies G in every interpretation.
C. A two-element domain can make F true and G false.
D. F and G are equivalent when the domain has one element.

### Q18. [1 Mark] [NAT]

An instruction uses base-plus-scaled-index addressing: effective address=base+4×index+displacement. The index register contains−3, base contains100 and displacement is20. A32-bit word is loaded from that effective address. What is the byte address of its last byte?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A syntax-directed translator for expressions uses E→E+T with E.val=Eleft.val+T.val, E→T with E.val=T.val, T→digit with T.val=digit.value, and T→(E) with T.val=2×E.val. What value is assigned to the complete expression (2+3)+(4)?

**Answer format:** Exact integer.

### Q20. [1 Mark] [MCQ]

A timestamp protocol handles a write by transaction timestamp t as follows: abort if t<readTS(x); otherwise ignore the write if t<writeTS(x); otherwise perform it. Initially readTS(x)=5 and writeTS(x)=9. Two separate attempts are considered from this same initial state, with t=7 and t=4. What are their respective outcomes?


A. Perform, ignore
B. Abort, ignore
C. Ignore, abort
D. Perform, abort

### Q21. [1 Mark] [MSQ]

A dynamic array starts with capacity one. Appending to a full array allocates a new array of twice the capacity and copies all existing elements; other appends take constant time. Which statements hold over n appends starting empty?

A. The total copying work is O(n).
B. The total copying work is necessarily Θ(n log n).
C. A single append can take Θ(n) time when the current number of elements is proportional to n.
D. Every individual append has worst-case constant time.

### Q22. [1 Mark] [MSQ]

A ternary ER relationship Assignment(Employee,Project,Role) records who fills each role on each project. Every (Project,Role) pair has at most one assigned employee. An employee may fill several roles on the same project, and may work on several projects. There are no other key constraints. Which statements hold?

A. (Project,Role) is a candidate key of Assignment.
B. (Employee,Project) is necessarily a candidate key.
C. Two assignments with the same project and role but different employees violate the constraint.
D. Replacing the relationship by Employee–Project alone preserves all assignment information.

### Q23. [1 Mark] [MCQ]

What does this conforming C program print? Array indices are valid and all arithmetic is representable.

```c
#include <stdio.h>
void f(int a[], int n) {
    int *p = a;
    a = a + 1;
    a[n-2] = p[0] + a[0];
}
int main(void) {
    int x[] = {4,7,9};
    f(x,3);
    printf("%d %d\n", x[0],x[2]);
    return 0;
}
```

A. 7 11
B. 4 11
C. 4 9
D. 11 9

### Q24. [1 Mark] [NAT]

A coin system has denominations1,3,4 and unlimited coins. For amount6, how many more coins does repeatedly taking the largest affordable denomination use than an optimal solution?

**Answer format:** Integer.

### Q25. [1 Mark] [MSQ]

A deterministic pushdown automaton recognizes balanced parentheses by pushing on '(' and popping on ')', rejecting a pop from an empty stack. Acceptance requires the stack to be empty at end of input. Which statements are correct?

A. The empty string is accepted.
B. Equal total counts of '(' and ')' guarantee acceptance.
C. Every prefix of an accepted string has at least as many '(' as ')'.
D. The string '())(' is accepted.

### Q26. [1 Mark] [MCQ]

A doubly linked list has adjacent non-sentinel nodes P,X,N. Removing X while preserving the list requires which neighbour updates?

A. P.next=N and N.prev=P.
B. P.prev=N and N.next=P.
C. P.next=X and N.prev=X.
D. P.next=P and N.prev=N.

### Q27. [1 Mark] [MCQ]

SQL table L(id) contains 1,2 and table R(id,v) contains (1,0),(1,5). What rows are returned by the following query, using ordinary SQL bag semantics?

```sql
SELECT L.id, R.v
FROM L LEFT JOIN R ON L.id=R.id AND R.v>0;
```

A. (1,5) only
B. (1,0),(1,5),(2,NULL)
C. (1,5),(2,NULL)
D. (1,NULL),(2,NULL)

### Q28. [1 Mark] [NAT]

A 3×4 matrix has rows (1,2,0,1),(0,1,1,0),(1,3,1,1). What is the dimension of its nullspace over the real numbers?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

For x≠0, let f(x)=(sin(3x)−3x)/x³, with angles in radians. What value should be assigned to f(0) to make f continuous at zero?

**Answer format:** Exact finite decimal.

### Q30. [1 Mark] [NAT]

Two D flip-flops store bits q1,q0. On every clock edge, q1 becomes the old q0 and q0 becomes NOT(old q1 XOR old q0). Starting at 00, what is the least positive number of edges after which the state is 00 again?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MCQ]

Which language is regular?

A. {aⁿbⁿ : n≥0}
B. {aᵖ : p is prime}
C. {aⁿbᵐ : n,m≥0 and n is even}
D. {ww : w∈{0,1}*}

### Q32. [1 Mark] [NAT]

X has a Poisson distribution with parameter lambda>0. It is known that P(X=0)=P(X=1). What is E[X^2]?

**Answer format:** Numeric value; integer.

### Q33. [1 Mark] [NAT]

A link sends packets of1000 payload bits plus a100-bit header at1100 bits per millisecond. Packets are continuously available and there are no other delays or losses. What payload throughput, in bits per millisecond, is achieved?

**Answer format:** Exact number.

### Q34. [1 Mark] [MSQ]

Procedure P makes a call as its final action, passing the address of a local variable x to callee Q. Q dereferences that address during the call. Which statements about optimizing this call are correct?

A. P's frame may always be discarded and overwritten before Q reads x, solely because the call is in tail position.
B. Any transformation must preserve the addressed object's value and valid storage for Q's use.
C. Q cannot observe x because callees never receive pointers to caller variables.
D. Tail position alone is insufficient to justify overwriting all storage in P's frame.

### Q35. [1 Mark] [MSQ]

Two threads each execute the following two-iteration loop on shared x, initially 0. Each read and write is atomic, the computation uses a private register r, and execution is a sequentially consistent interleaving preserving each thread's order.

```text
repeat twice:
    r = x
    x = r + 1
```

Which values of x are possible after both threads finish?

A. 1  
B. 2  
C. 3  
D. 4

### Q36. [2 Marks] [NAT]

A compiler translates a short-circuit Boolean expression (p AND q) OR r into a decision graph. Each predicate occurrence is evaluated at most once on any execution, in source short-circuit order. How many different subsets of {p,q,r} can be evaluated during an execution, as their truth values vary?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

Each reference first spends 1 ns searching a TLB. A TLB miss, occurring on 10% of references, adds a 200 ns page-table walk before the data-cache lookup. Every data-cache lookup takes 2 ns; a data-cache miss, occurring on 5% of references, adds 50 ns. These delays do not overlap, and there are no page faults. What is the mean reference time in ns?

**Answer format:** Exact finite decimal.

### Q38. [2 Marks] [NAT]

A microinstruction independently selects one of nine source choices, one of five ALU choices, and any subset of eight destination registers, including the empty subset. A format with separate fixed-width binary source and ALU fields plus an eight-bit destination mask is compared with an unrestricted single binary field encoding all legal combinations. How many bits does the separate-field format require in excess of the minimum single-field width?

**Answer format:** Integer.

### Q39. [2 Marks] [MCQ]

An eight-bit two's-complement fixed-point format has four fractional bits. Multiply the values encoded by 0xE6 and 0x1C using an exact intermediate result, then round once to the nearest representable value, breaking a tie toward an even least significant retained bit. No overflow occurs. What is the final encoded byte?

A. 0xD3  
B. 0xD2  
C. 0x2E  
D. 0xD4

### Q40. [2 Marks] [NAT]

Relation R(x,y) contains(1,1),(1,2),(2,2),(3,1). Evaluate the domain-restricted tuple-calculus condition R(x,y) AND NOT EXISTS z(R(y,z) AND z≠x). How many tuples of R satisfy it?

**Answer format:** Integer.

### Q41. [2 Marks] [MSQ]

Let u=(1,1,0)ᵀ, v=(1,0,1)ᵀ, P=uuᵀ/(uᵀu), and Q=vvᵀ/(vᵀv). Which statements are correct?

A. PQ has rank one.
B. trace(PQ)=1/4.
C. PQ is symmetric.
D. The eigenvalues of PQ, counting multiplicity, are 1/4,0,0.

### Q42. [2 Marks] [MSQ]

In a binary floating-point format with round-to-nearest, ties-to-even and finite precision, which statements are correct?

A. Addition is necessarily associative for all finite inputs whose computations stay finite.
B. Adding a sufficiently small positive number to a sufficiently large positive number can leave the stored result unchanged.
C. Cancellation of nearby numbers can reveal error already present in their approximations.
D. Every integer of arbitrary size is represented exactly.

### Q43. [2 Marks] [MSQ]

A proposed proof claims that the regular language a*b* is not regular: “For pumping length p choose a^p b^p. Select a decomposition whose pumped part contains both a and b. Pumping twice destroys the required order.” Which objections correctly identify flaws?

A. A nonregularity proof must defeat every legal decomposition, not just one selected decomposition.
B. Any legal decomposition with prefix-plus-pumped-part length at most p has its pumped part entirely among the a's.
C. The pumping lemma permits an empty pumped part, so the proof must use one.
D. Choosing a string of length2p is forbidden by the pumping lemma.

### Q44. [2 Marks] [NAT]

Let A=[[0,1],[−2,3]] and let v=(x,y)ᵀ satisfy x+y=6. The sequence A^n v must remain bounded as n tends to infinity. What is x?

**Answer format:** Exact number.

### Q45. [2 Marks] [MSQ]

D(id) contains 1 and 2. E(eid,did,active) contains (10,1,0) and (11,1,1); all columns are non-NULL. Consider this SQL query:

```sql
SELECT D.id, COUNT(*) AS n, COUNT(E.eid) AS m
FROM D LEFT JOIN E
  ON D.id = E.did AND E.active = 1
GROUP BY D.id;
```

Which statements are correct?

A. The row for id=1 has n=1 and m=1.
B. The row for id=2 has n=1 and m=0.
C. Moving E.active=1 from ON to WHERE necessarily preserves the result.
D. The row for id=2 has n=0 and m=0.

### Q46. [2 Marks] [MCQ]

An HTTP client sends a conditional GET containing `If-None-Match: "v7"` for a cached representation. The server's current representation has the same entity tag and is otherwise eligible for the conditional request. Compare a 304 response with a 200 response carrying the entire unchanged representation. Which statement is correct?

A. A 304 necessarily eliminates the request-response round trip.
B. A 304 supplies a new full representation body that must replace the cached body.
C. A 304 can save representation-body transfer while still requiring a network round trip.
D. A 304 proves that all caches on the Internet contain the same body.

### Q47. [2 Marks] [MSQ]

A synchronous message-passing send completes only when a matching receive occurs. Process P first sends to Q and then receives from Q; process Q first sends to P and then receives from P. Neither channel buffers a message. Which statements are correct?

A. Both processes can block on their first operation.
B. The program is guaranteed to finish because each process eventually has a receive in its source code.
C. Changing Q to receive first and then send removes this particular cyclic wait.
D. Adding a mutex around both sequences necessarily fixes the protocol.

### Q48. [2 Marks] [NAT]

A queue is implemented with an input stack and an output stack. Enqueue pushes onto the input stack. Dequeue pops the output stack; if it is empty, all items from the input stack are first moved to it, one pop and one push per item. Count only individual stack pushes and pops. Starting empty, perform enqueue(A), enqueue(B), dequeue, enqueue(C), enqueue(D), dequeue, dequeue. How many stack operations are performed in total?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

A 0/1 knapsack has capacity6. Items A,B,C have (weight,value) pairs (3,5),(4,7),(2,4). Each item can be selected at most once. A faulty implementation updates its one-dimensional DP array in increasing capacity order for each item, allowing an item to be reused. By how much can its final dp[6] exceed the true optimum, starting with all entries zero and processing items A,B,C in that order?

**Answer format:** Exact integer.

### Q50. [2 Marks] [MSQ]

A byte-addressed processor has address lines A15 through A0. A memory board uses four 4K×8 RAM chips to provide one contiguous 16 KiB region starting at address 0x8000. Each selected chip supplies one byte. Chip address pins use A11 through A0; a decoder chooses one chip. Assume the decoder is enabled exactly for addresses in the intended region. Which statements are correct?

A. A13 and A12 can select the chip, while A15=1 and A14=0 enable the board.  
B. Address 0xB123 selects chip index 3 (indices 0–3 in increasing address order) at local offset 0x123.  
C. If the board enable checks only A15=1 and ignores A14, each physical byte is mapped at two processor addresses.  
D. Connecting chip address pins to A12 through A1, while otherwise retaining the stated decoder, still gives one-to-one addressing of the 16 KiB region.

### Q51. [2 Marks] [MSQ]

A machine M is described together with a finite input x and a nonnegative integer bound k. Which questions are decidable uniformly from this data?

A. Does M accept x within k steps?
B. Does M halt on x within k steps?
C. Does M eventually halt on x with no bound?
D. Does the simulation visit the same full configuration twice within its first k steps?

### Q52. [2 Marks] [MSQ]

A and B are real 4×4 matrices, each of rank 3. Which statements are correct?

A. rank(AB) is at least 2.
B. rank(AB) can be 3.
C. rank(AB) can be 1.
D. rank(AB) can be 2.

### Q53. [2 Marks] [NAT]

Integers x range over all four-bit signed values −8 through 7. Evaluate `y=(2*x)/2` by first multiplying with four-bit two's-complement wraparound, then dividing the resulting signed value by two using exact division on even integers. For how many x values is y=x?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

For Boolean inputs x,y,z, consider F=(x OR y) AND ((NOT x) OR z). Which statements are correct?

A. F=(x AND z) OR ((NOT x) AND y).
B. The product term yz can be added to the expression in A without changing F.
C. F is always equal to y AND z.
D. When y=z, F equals that common value.

### Q55. [2 Marks] [MCQ]

A partial DFA over {a,b} has states q0,q1,q2, start state q0, and accepting set {q2}. Its only transitions are q0 on a to q1, q1 on a to q2, and q2 on a to q2. Undefined transitions reject. What is the minimum number of states in a complete DFA recognizing the complement of its language over {a,b}*?

A. 4
B. 3
C. 5
D. 6

### Q56. [2 Marks] [MCQ]

A binary tree has distinct labels. Its preorder is A,B,D,E,C,F and its inorder is D,B,E,A,C,F. Which postorder is correct?

A. D,E,B,F,C,A
B. D,B,E,F,C,A
C. E,D,B,C,F,A
D. D,E,F,B,C,A

### Q57. [2 Marks] [NAT]

A comparison algorithm recursively divides an array of n=32 elements into equal halves. At every non-leaf call it first solves both halves and then compares every element in the left half with every element in the right half, once per pair. A one-element call makes no comparisons. How many comparisons occur in total?

**Answer format:** Exact integer.

### Q58. [2 Marks] [NAT]

In an idealized CSMA/CD network, the farthest stations have a one-way propagation time of12 microseconds. A100-Mbit/s transmitter must still be transmitting at the latest possible collision-detection instant. Ignoring all encoding overhead and assuming a collision can occur just before a distant station first senses the transmission, what is the minimum frame length in bytes?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A recursive DFS starts at s in a directed graph with edges s→a,s→b,a→c,b→c,c→d. Each adjacency list is processed in alphabetical order. A vertex is marked immediately upon its first visit. How many edges lead to vertices already marked at the moment that edge is examined?

**Answer format:** Integer.

### Q60. [2 Marks] [MCQ]

A hidden source is chosen once: source I with probability 1/3, source II with probability 2/3. Conditional on that source, trials are independent; success probability is 1/4 for I and 1/2 for II. Given exactly two successes in the first three trials, what is the probability of success on the fourth trial?

A. 1/2  
B. 35/76  
C. 3/19  
D. 7/16

### Q61. [2 Marks] [MCQ]

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

### Q62. [2 Marks] [MSQ]

Resource A has two instances and B has one. P holds one A and requests B; Q holds B and requests one A; R holds the other A and requests nothing more. A process that receives its request completes and releases its resources; R can complete immediately. Which statements are correct?

A. The system can finish all processes in order R,Q,P.
B. The cycle involving P and Q proves deadlock even with R able to release an A instance.
C. A cycle in the resource-allocation graph is not sufficient here to establish deadlock.
D. Releasing R's A can enable Q, whose completion can then enable P.

### Q63. [2 Marks] [MSQ]

In a finite directed network, every link has strictly positive cost and every router can reach destination d. Each router u other than d selects any outgoing neighbour v satisfying dist(u,d)=cost(u,v)+dist(v,d), using exact shortest-path distances. Different routers may break equal-cost ties independently. Which statements are correct?

A. The selected next-hop graph can contain a directed cycle because tie-breaking is independent.
B. Distance to d strictly decreases at each selected hop.
C. Every packet following these next hops eventually reaches d.
D. Allowing zero-cost links would leave the strict-decrease argument unchanged.

### Q64. [2 Marks] [MSQ]

A loop begins with x=0 and repeatedly executes `x=x+1` while an input-dependent condition holds. A simple forward constant-propagation analysis joins facts from the initial edge and loop back edge at the header. Which statements are correct?

A. x need not be a single known constant at the loop header after the fixed point is reached.
B. Treating x as zero on every header visit is sound merely because its initializer is zero.
C. Different iterations can reach the header with different x values.
D. Constant propagation alone necessarily computes the exact iteration count for every input condition.

### Q65. [2 Marks] [MCQ]

Two initially empty tables P(id,qid) and Q(id,pid) have non-NULL foreign keys P.qid→Q.id and Q.pid→P.id. A transaction inserts P(1,1) and Q(1,1). What difference can deferred checking make, assuming both foreign keys permit checking at commit?

A. It allows both rows to be inserted and the final mutually referencing state to satisfy the constraints, whereas immediate checking would reject whichever insert occurs first.
B. It permits either foreign key to remain broken permanently after commit.
C. It removes the requirement that referenced keys exist at commit.
D. It forces both tables to remain empty.

---

## ANSWER KEY — MOCK TEST 040

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MCQ | 1 | A |
| 3 | MCQ | 1 | A |
| 4 | NAT | 1 | 0.4167 (range 0.41665–0.41675) |
| 5 | MCQ | 1 | B |
| 6 | MSQ | 2 | A, B |
| 7 | MSQ | 2 | A, C, D |
| 8 | NAT | 2 | 6 |
| 9 | NAT | 2 | 11 |
| 10 | NAT | 2 | 25 |
| 11 | MCQ | 1 | A |
| 12 | NAT | 1 | 2 |
| 13 | NAT | 1 | 768 |
| 14 | MCQ | 1 | D |
| 15 | MCQ | 1 | A |
| 16 | MCQ | 1 | D |
| 17 | MSQ | 1 | A, C, D |
| 18 | NAT | 1 | 111 |
| 19 | NAT | 1 | 18 |
| 20 | MCQ | 1 | C |
| 21 | MSQ | 1 | A, C |
| 22 | MSQ | 1 | A, C |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 1 |
| 25 | MSQ | 1 | A, C |
| 26 | MCQ | 1 | A |
| 27 | MCQ | 1 | C |
| 28 | NAT | 1 | 2 |
| 29 | NAT | 1 | -4.5 |
| 30 | NAT | 1 | 3 |
| 31 | MCQ | 1 | C |
| 32 | NAT | 1 | 2 (exact) |
| 33 | NAT | 1 | 1000 |
| 34 | MSQ | 1 | B, D |
| 35 | MSQ | 1 | B, C, D |
| 36 | NAT | 2 | 3 |
| 37 | NAT | 2 | 25.5 |
| 38 | NAT | 2 | 1 |
| 39 | MCQ | 2 | B |
| 40 | NAT | 2 | 1 |
| 41 | MSQ | 2 | A, B, D |
| 42 | MSQ | 2 | B, C |
| 43 | MSQ | 2 | A, B |
| 44 | NAT | 2 | 3 |
| 45 | MSQ | 2 | A, B |
| 46 | MCQ | 2 | C |
| 47 | MSQ | 2 | A, C |
| 48 | NAT | 2 | 15 |
| 49 | NAT | 2 | 1 |
| 50 | MSQ | 2 | A, B, C |
| 51 | MSQ | 2 | A, B, D |
| 52 | MSQ | 2 | A, B, D |
| 53 | NAT | 2 | 8 |
| 54 | MSQ | 2 | A, B, D |
| 55 | MCQ | 2 | A |
| 56 | MCQ | 2 | A |
| 57 | NAT | 2 | 496 |
| 58 | NAT | 2 | 300 |
| 59 | NAT | 2 | 1 |
| 60 | MCQ | 2 | B |
| 61 | MCQ | 2 | B |
| 62 | MSQ | 2 | A, C, D |
| 63 | MSQ | 2 | B, C |
| 64 | MSQ | 2 | A, C |
| 65 | MCQ | 2 | A |
