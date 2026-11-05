# GATE CS 2027 — Full-Length Mock Test 085

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

A narrative says: “The team archived the original readings before recalibrating the instrument. It then repeated the measurements. Only after this repetition did it compare the two sets of readings.” Which event necessarily happened immediately before the comparison among the three later events mentioned?

A. Archiving the original readings
B. Repeating the measurements
C. Recalibrating the instrument
D. Discarding the original readings

### Q2. [1 Mark] [NAT]

A bag contains one red and three blue balls. They are drawn without replacement until the red ball appears. What is the expected total number of draws, including the red ball?

**Answer format:** Exact decimal.

### Q3. [1 Mark] [MCQ]

“The proposed change is reversible: the previous configuration can be restored.” Which meaning of reversible applies?

A. Impossible to undo.
B. Capable of being undone.
C. Required to happen twice.
D. Unrelated to the previous configuration.

### Q4. [1 Mark] [NAT]

How many integers x with1≤x≤1000 satisfy floor(log2 x)=floor(log3 x)? Here floor denotes the greatest integer not exceeding its argument.

**Answer format:** Exact integer.

### Q5. [1 Mark] [MSQ]

An engineer tests a device at every integer temperature from 0°C through 100°C. It operates correctly in all tests. No rule governing its behaviour between tested temperatures is known. Which statements are justified solely by these observations?

A. The device operates correctly at 37°C under the tested conditions.
B. The device must operate correctly at 37.5°C.
C. The observations are compatible with a device that fails at 37.5°C.
D. The device must operate correctly at every integer temperature above 100°C.

### Q6. [2 Marks] [NAT]

Unit cubes are stacked in four columns on a2×2 base. A column may have height0,1,or2. The maximum heights seen in the two rows are respectively2 and1; the maximum heights seen in the two columns are respectively2 and1. Rows and columns have fixed labels. How many different height arrays satisfy these four maxima?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A sequence satisfies a1=2 and a(n+1)=2a(n)+1 for n≥1. What is the sum of its first four terms?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

A rectangular garden is 40 m by 30 m. A path of uniform width runs just inside all four boundaries, leaving a rectangular planted region. If the path occupies 264 m², find its width, which is less than 15 m.

**Answer format:** Integer metres.

### Q9. [2 Marks] [MCQ]

Five presentations P,Q,R,S,T occupy five consecutive slots, one per slot. Q occurs immediately after P. R occurs before P, and S occurs after Q. How many schedules satisfy these restrictions?

A. 2
B. 4
C. 6
D. 8

### Q10. [2 Marks] [NAT]

A retailer marks an item25% above cost and gives a discount of d% on the marked price. The final profit is5% of cost. What is d?

**Answer format:** Exact percentage number.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A BFS from s runs on an undirected graph with edges sa, sb, ac, ad, be, and ce. Vertices are marked when enqueued. Which discovery order is impossible, regardless of adjacency-list ordering?

A. s,a,b,c,d,e
B. s,b,a,e,c,d
C. s,a,b,c,e,d
D. s,a,b,d,c,e

### Q12. [1 Mark] [MSQ]

Under strict two-phase locking, exclusive locks are retained until commit or abort. Which statements are correct?

A. Another transaction cannot read an item modified under an unreleased exclusive lock.
B. Retaining exclusive locks prevents cascading aborts caused by reading those uncommitted writes.
C. The rule alone makes deadlock impossible.
D. A transaction may release an exclusive lock immediately after its write under this strict rule.

### Q13. [1 Mark] [NAT]

An HTTP client first opens a new TCP connection and obtains a base HTML document. It then opens exactly three new TCP connections in parallel for six images, requesting one image per connection at a time and reusing each connection for its second image. There is no pipelining. Each TCP handshake takes one RTT, and each request-response takes one RTT. RTT is 40 ms for every connection. Ignore DNS, transmission time, TLS and processing. What is the minimum time from starting the HTML connection until all images arrive, in milliseconds?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A min-heap stores distinct keys in a one-based array of length15. A particular key's array index is known to be6. Ignoring its own position, how many other array positions are guaranteed to contain larger keys solely because of the heap-order property?

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

On set{1,2,3,4}, define xRy exactly when floor(x/2)=floor(y/2). How many ordered pairs belong to R?

**Answer format:** Integer.

### Q16. [1 Mark] [MSQ]

A compiler removes an assignment to scalar x as dead code. The right-hand side has no side effects, exceptions, or observable traps. Which conditions support removal?

A. On every outgoing path, x is redefined before its current value is read, or execution ends without reading it.
B. x is read on at least one outgoing path before redefinition.
C. x is not live immediately after the assignment.
D. x has a short variable name.

### Q17. [1 Mark] [NAT]

A real matrix has rows (0,−2),(1,3). Find the trace of its inverse.

**Answer format:** Exact finite decimal.

### Q18. [1 Mark] [MSQ]

A programming language specifies that every evaluation of a volatile memory read is observable, even if the returned values happen to be equal. For two successive expressions x=read_volatile(p) and y=read_volatile(p), which statements are correct?

A. Equal returned values alone justify replacing the second read by y=x.
B. Such replacement removes an observable operation.
C. Ordinary expression-value equality is insufficient for this optimization.
D. Volatile reads are guaranteed never to return equal values.

### Q19. [1 Mark] [NAT]

A differentiable function f on[0,2] has f(0)=1 and f(2)=7, and f'(x)≤3 everywhere on(0,2). What is f(1)?

**Answer format:** Exact integer.

### Q20. [1 Mark] [NAT]

Starting with one process, the following code executes. Every fork succeeds, returns 0 only in its new child, and returns a positive child identifier in its parent. Every process reaches the final line once. How many processes execute work()?

```c
int p = fork();
if (p == 0) fork();
fork();
work();
```

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A tabular minimization pattern `1-0--` has five bit positions. How many minterms does it represent?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A directed graph on vertices 0–3 is stored in CSR form with row pointers [0,2,2,5,6] and column indices [1,3,0,2,3,1]. Outgoing neighbours of vertex i occupy indices row[i] through row[i+1]−1. What is the minimum number of directed edges that must be added to make the graph strongly connected?

**Answer format:** Integer.

### Q23. [1 Mark] [MSQ]

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

### Q24. [1 Mark] [NAT]

A cache stores64 data bytes in four-byte blocks and is four-way set associative. How many sets does it contain?

**Answer format:** Integer.

### Q25. [1 Mark] [MCQ]

A 4-to-1 multiplexer has select bits A,B, with A more significant. Its data inputs for select values 00,01,10,11 are C, NOT C, 1,0 respectively. Minterms are numbered using A,B,C with A most significant. Which set is the output's on-set?

A. {0,3,4,5}  
B. {1,2,4,5}  
C. {1,2,6,7}  
D. {0,1,2,5}

### Q26. [1 Mark] [MCQ]

Consider L={aⁿbᵐ:n,m≥0 and n≠m}. For an arbitrary positive proposed regular pumping length p, choose w=aᵖb^(p+p!). Every valid split w=xyz with |xy|≤p and |y|>0 has y=aᵏ for some 1≤k≤p. Which pumping exponent i makes xy^i z have equal a and b counts and therefore leave L?

A. i=p!
B. i=1+p!/k
C. i=1−p!/k
D. i=k+1

### Q27. [1 Mark] [MCQ]

Recognizers M and N recognize L and its complement respectively. How can they be used to decide L on input w?

A. Run M to completion before starting N.
B. Accept whenever either machine accepts.
C. Interleave their steps; accept if M accepts and reject if N accepts.
D. Reject immediately unless M accepts in its first step.

### Q28. [1 Mark] [NAT]

A connected undirected graph has four vertices and every edge has weight 7. How much does any minimum spanning tree weigh?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

An ER relationship between three distinct entities in set A and four distinct entities in set B is many-to-many, with total participation on both sides. Relationship instances are sets of distinct pairs from A×B. How many different relationship instances have exactly four pairs?

**Answer format:** Exact integer.

### Q30. [1 Mark] [MSQ]

Use set semantics. R(A,B)={(1,x),(1,y),(2,x)} and S(B)={(x),(y)}. Define

`E = projection_A(R) - projection_A((projection_A(R) x S) - R)`

where x is Cartesian product and - is set difference. Which statements are correct? Each proposed change is applied independently to the original relations.

A. For the original relations, E={(1)}.  
B. If S is empty, E={(1),(2)}.  
C. If (2,y) is added to R, E remains {(1)}.  
D. If (z) is added to S, E is empty.

### Q31. [1 Mark] [NAT]

P(B)=0.5, P(A|B)=0.6 and P(A|not B)=0.2. Find P(B|A).

**Answer format:** Exact finite decimal.

### Q32. [1 Mark] [NAT]

A virtually indexed, physically tagged cache has 32 KiB data capacity and 64-byte lines. Pages are 4 KiB. To keep every set-index bit within the page offset, what is the minimum power-of-two associativity? Ignore all metadata and use conventional contiguous offset/index fields.

**Answer format:** Integer number of ways.

### Q33. [1 Mark] [NAT]

Let A={1,2} and B={1,2,3,4,5}. Consider the set of all X satisfying A⊆X⊆B, ordered by inclusion. How many ordered pairs (X,Y) satisfy X∩Y=A and X∪Y=B?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

A directed weighted graph has edges s→a(1), a→a(−1), s→t(5), and no others. Distances refer to walks, which may repeat vertices. Which statements are correct?

A. There is a finite shortest-walk distance from s to t, equal to5.
B. Every vertex reachable from s has a finite shortest-walk distance.
C. A negative cycle reachable from s need not make the s-to-t distance unbounded below.
D. The negative self-loop can be inserted into a walk from s to t.

### Q35. [1 Mark] [MCQ]

A router forwards an IPv4 datagram from one Ethernet link to another. Assume no tunnelling or network address translation. Which pair of fields is necessarily replaced with values appropriate to the outgoing link?

A. Source and destination IPv4 addresses
B. Source and destination TCP port numbers
C. Ethernet source and destination MAC addresses
D. Application sequence numbers

### Q36. [2 Marks] [NAT]

For a binary input string, prepend zeroes if needed to obtain at least three bits. Accept exactly when the last three bits of this padded string have even parity; thus the empty string is accepted. What is the minimum number of states of a complete DFA recognizing this language?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A comparison-based search probes a sorted array of15 distinct keys by repeatedly choosing the middle of the remaining interval. What is the maximum number of key comparisons for a successful search?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

Two processes communicate over two initially empty FIFO channels of capacity one message each. Sending blocks when the destination channel is full; receiving blocks when it is empty. P executes send(a),send(b),receive(x), while Q executes send(c),receive(y),receive(z). P's sends go to Q and Q's send goes to P. Both run fairly, and local computation takes no time. How many messages can remain queued when both processes finish?

**Answer format:** Exact integer.

### Q39. [2 Marks] [MSQ]

A synchronous machine has two different states that produce the same output now. Which statements are correct about state minimization?

A. Equal current outputs alone guarantee equivalence.
B. A future input sequence yielding different output sequences distinguishes the states.
C. Equivalent states must have equivalent successors for every input under the usual deterministic Moore-machine definition.
D. Different state encodings alone guarantee distinguishability by external observations.

### Q40. [2 Marks] [MSQ]

For a finite relation R(x,y), consider the formula R(x,y) AND NOT exists z(R(x,z) AND z≠y), with x,y free. Which statements are correct?

A. It selects tuples whose x value has exactly one distinct associated y value in R.
B. It rejects every tuple whenever R contains two different x values.
C. The existential variable z ranges over possible competing y values for the same x.
D. It can return an(x,y) pair not in R.

### Q41. [2 Marks] [NAT]

For the grammar S→ABc, A→a | ε, B→AD | b, D→d | ε, with start S, how many distinct terminal symbols belong to FOLLOW(A)? The end marker is not a terminal symbol.

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

An input describes a Turing machine M over {0,1}, with the promise that M halts on every input string. Algorithms below need only behave correctly on machines satisfying the promise. Which statements are correct?

A. Nonemptiness of L(M) is semidecidable by testing strings and eventually accepting whenever an accepted string exists.
B. Emptiness of L(M) is decidable solely because every individual simulation halts.
C. Equivalence of L(M) to the empty language is decidable under this promise.
D. Whether M accepts at least one string of length at most ten is decidable.

### Q43. [2 Marks] [NAT]

A 0/1 knapsack has capacity 8 and five distinct items with (weight,value): A=(2,3), B=(2,3), C=(3,4), D=(3,4), E=(4,5). Each may be selected at most once. How many distinct subsets attain the maximum possible value without exceeding capacity? Subsets differing only by A versus B or C versus D still count as distinct.

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

Routers have converged exact shortest distances d(v) to destination t. Each router v≠t selects a next hop u satisfying d(v)=w(v,u)+d(u). All relevant distances are finite. Which statements are correct?

A. If all link costs are strictly positive, the selected next-hop graph cannot contain a directed cycle.
B. If zero-cost links are allowed, independent tie choices can create a forwarding cycle despite correct distances.
C. Correct distances alone prevent forwarding cycles for every set of nonnegative link costs.
D. With positive costs, distance strictly decreases at every selected hop.

### Q45. [2 Marks] [NAT]

An initially empty five-stage IF-ID-EX-MEM-WB pipeline issues at most one instruction per cycle. Without stalls, N retired instructions take N+4 cycles. Full forwarding leaves exactly one stall cycle for an immediately dependent load-use pair. A taken branch incurs exactly two additional cycles, with no other penalties. A path retires, in order, a load, an ALU instruction using that load, a taken branch depending on that ALU result, and a target ALU instruction. ALU-to-branch forwarding avoids any additional data stall. How many cycles elapse through the final instruction's WB?

**Answer format:** Exact integer.

### Q46. [2 Marks] [MSQ]

For grammar S→aSb | T and T→cT | ε, which statements are true?

A. Every generated word has equally many a and b symbols.
B. Every generated word has all c symbols between its a and b blocks.
C. The grammar generates abcc.
D. The grammar generates aacbb.

### Q47. [2 Marks] [MCQ]

A system has two resource types A and B. It uses the Banker's safety test. Current allocation and maximum claims are:

| Process | Allocation (A,B) | Maximum (A,B) |
|---|---|---|
| P0 | (1,0) | (2,2) |
| P1 | (0,1) | (1,2) |
| P2 | (1,1) | (3,1) |

The available vector is (1,1). P0 requests (0,1). The request is within its remaining claim and the available resources. Which conclusion is correct?

A. Grant it: P0,P1,P2 is a safe sequence afterward.  
B. Grant it: P2,P1,P0 is a safe sequence afterward.  
C. Defer it: the present state is safe, but the tentative grant is unsafe.  
D. Defer it: the present state is already unsafe.

### Q48. [2 Marks] [NAT]

Five distinguishable bins each hold at most two identical tokens. In how many ways can exactly five tokens be distributed among the bins?

**Answer format:** Integer.

### Q49. [2 Marks] [MSQ]

Over GF(2), a CRC generator is g(x)=x³+x+1. The transmitted codeword suffers error polynomial e(x)=x^k g(x), for some k≥0 that fits within the transmitted frame. Which statements are correct?

A. The CRC remainder of the error polynomial is zero.
B. This nonzero error can escape detection.
C. Multiplication by x^k guarantees detection of every nonzero polynomial.
D. The error polynomial must be a single-bit error.

### Q50. [2 Marks] [MCQ]

A lexer has the token rules `a`, `b`, `d`, and `ab*c`, where `b*` means zero or more b symbols. It uses longest match. An implementation reads forward until no token rule can still match, then returns to the most recent accepting position to emit that token. Consider the inputs `ab^n d`, with no spaces and arbitrary integer n>=1. Before returning the first token, how much lookahead beyond the most recent accepting position can this implementation require?

A. At most one character, independently of n.  
B. At most two characters, independently of n.  
C. An amount unbounded as n grows.  
D. Zero, because the rule `a` can be emitted immediately upon reading a.

### Q51. [2 Marks] [MSQ]

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

### Q52. [2 Marks] [NAT]

In an idealized CSMA/CD network, the farthest stations have a one-way propagation time of12 microseconds. A100-Mbit/s transmitter must still be transmitting at the latest possible collision-detection instant. Ignoring all encoding overhead and assuming a collision can occur just before a distant station first senses the transmission, what is the minimum frame length in bytes?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

Keys 40,20,60,10,30,50,70,25,35 are inserted in that order into an initially empty ordinary BST. Delete 20 by replacing its key with its inorder predecessor and physically removing that predecessor's original node. Then delete 40 by replacing its key with its inorder successor and physically removing that successor's original node. What is the key at the lowest common ancestor of 25 and 70 in the resulting tree?

**Answer format:** Integer key.

### Q54. [2 Marks] [NAT]

A continuously differentiable function f on[0,2] satisfies f(2)=4 and the integral of f(x) over[0,2] equals3. What is the integral of x f'(x) over[0,2]?

**Answer format:** Exact number.

### Q55. [2 Marks] [NAT]

A stack machine stores four-byte integers. PUSH first subtracts4 from SP, then writes at the new SP. POP reads at SP, then adds4 to SP. Initially SP=100. Execute PUSH7, PUSH9, POP into R, then store R at address SP+4, then POP into S. What is R+S? The stack is ordinary writable memory and all addresses are valid.

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

An8-bit two's-complement ALU computes the expression (x+y)−y, wrapping after each operation. For x=100 and y=60, count how many of the two operations signal signed overflow. The overflow flag is recomputed separately for each operation.

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

Relation Child(cid,pid) has primary key cid and a foreign key pid referencing Parent(pid), whose primary key is pid. Child.pid is nullable and referential integrity uses ordinary SQL semantics without additional restrictions. Which statements are correct?

A. Two Child rows with different cid values may reference the same parent.
B. A non-NULL Child.pid must match a Parent.pid.
C. Every parent must be referenced by at least one child.
D. Child.pid must be unique because it is a foreign key.

### Q58. [2 Marks] [MSQ]

For grammar S→AB, A→aA | ε, B→bBc | ε, with start symbol S and end marker $, which statements are correct?

A. The grammar is LL(1).
B. c belongs to FOLLOW(A).
C. FOLLOW(B)={c,$}.
D. The production A→ε must be selected on lookahead a in an LL(1) table.

### Q59. [2 Marks] [NAT]

A syntax-directed translation uses the grammar E→E−T | T and T→digit. The semantic rules are E→E1−T: E.val=E1.val−T.val; E→T: E.val=T.val; T→digit: T.val=the digit's value. For the input9−4−2, a second implementation incorrectly rewrites the grammar to right recursion E→T−E | T and uses ordinary subtraction of the child values. What is the correct implementation's value minus the second implementation's value?

**Answer format:** Integer, possibly negative.

### Q60. [2 Marks] [NAT]

Six observations are3,3,3,7,7,7. Replace exactly one observation by any real number, keeping the other five fixed. The median of six observations is the average of the third and fourth values in sorted order. What is the largest possible increase in the median?

**Answer format:** Exact number.

### Q61. [2 Marks] [NAT]

Procedure F(n), for n≥0, returns immediately when n≤1. Otherwise it calls F(n−1), then F(n−2), with no memoization. Count only calls with n=0. How many such calls occur during F(6)?

**Answer format:** Integer.

### Q62. [2 Marks] [MSQ]

A toy floating-point format has four significant binary bits and round-to-nearest, ties-to-even. It supports all exponents needed below. Which real values round to exactly1.5?

A. 1.4375
B. 1.49
C. 1.5625
D. 1.625

### Q63. [2 Marks] [MCQ]

Over alphabet {a,b}, let L={a,ab}. A pushdown automaton starts with one bottom-of-stack symbol. For empty-stack acceptance, a string is accepted only if all input has been consumed and the stack is empty; no transition is possible once the stack is empty. No right-end marker is supplied. Standard determinism forbids a choice between an epsilon transition and an input-consuming transition for the same state and stack top. Which machine model cannot recognize L?

A. A deterministic finite automaton.  
B. A nondeterministic pushdown automaton accepting by empty stack.  
C. A deterministic pushdown automaton accepting by final state.  
D. A deterministic pushdown automaton accepting by empty stack.

### Q64. [2 Marks] [NAT]

How many subgroups of the permutation group S3 are abelian? Include the trivial subgroup and count distinct subgroups, not isomorphism types.

**Answer format:** Integer.

### Q65. [2 Marks] [MCQ]

What is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = 1
    while j <= i:
        for k = 1 to j:
            work()
        j = 2*j
```

A. Θ(n log n)
B. Θ(n²)
C. Θ(n² log n)
D. Θ(log² n)

---

## ANSWER KEY — MOCK TEST 085

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 2.5 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 2 |
| 5 | MSQ | 1 | A, C |
| 6 | NAT | 2 | 5 |
| 7 | NAT | 2 | 41 |
| 8 | NAT | 2 | 2 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 16 |
| 11 | MCQ | 1 | C |
| 12 | MSQ | 1 | A, B |
| 13 | NAT | 1 | 200 (exact) |
| 14 | NAT | 1 | 2 |
| 15 | NAT | 1 | 6 |
| 16 | MSQ | 1 | A, C |
| 17 | NAT | 1 | 1.5 |
| 18 | MSQ | 1 | B, C |
| 19 | NAT | 1 | 4 |
| 20 | NAT | 1 | 6 (exact) |
| 21 | NAT | 1 | 8 |
| 22 | NAT | 1 | 1 (exact) |
| 23 | MSQ | 1 | B, C, D |
| 24 | NAT | 1 | 4 |
| 25 | MCQ | 1 | B |
| 26 | MCQ | 1 | B |
| 27 | MCQ | 1 | C |
| 28 | NAT | 1 | 21 |
| 29 | NAT | 1 | 36 |
| 30 | MSQ | 1 | A, B, D |
| 31 | NAT | 1 | 0.75 |
| 32 | NAT | 1 | 8 |
| 33 | NAT | 1 | 8 |
| 34 | MSQ | 1 | A, C |
| 35 | MCQ | 1 | C |
| 36 | NAT | 2 | 8 |
| 37 | NAT | 2 | 4 |
| 38 | NAT | 2 | 0 |
| 39 | MSQ | 2 | B, C |
| 40 | MSQ | 2 | A, C |
| 41 | NAT | 2 | 4 |
| 42 | MSQ | 2 | A, D |
| 43 | NAT | 2 | 3 |
| 44 | MSQ | 2 | A, B, D |
| 45 | NAT | 2 | 11 |
| 46 | MSQ | 2 | A, B, D |
| 47 | MCQ | 2 | C |
| 48 | NAT | 2 | 51 |
| 49 | MSQ | 2 | A, B |
| 50 | MCQ | 2 | C |
| 51 | MSQ | 2 | A, B |
| 52 | NAT | 2 | 300 |
| 53 | NAT | 2 | 50 |
| 54 | NAT | 2 | 5 |
| 55 | NAT | 2 | 16 |
| 56 | NAT | 2 | 2 |
| 57 | MSQ | 2 | A, B |
| 58 | MSQ | 2 | A, C |
| 59 | NAT | 2 | -4 |
| 60 | NAT | 2 | 2 |
| 61 | NAT | 2 | 5 |
| 62 | MSQ | 2 | A, B, C |
| 63 | MCQ | 2 | D |
| 64 | NAT | 2 | 5 |
| 65 | MCQ | 2 | B |
