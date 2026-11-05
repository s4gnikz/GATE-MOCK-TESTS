# GATE CS 2027 — Full-Length Mock Test 093

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

Which sequence correctly orders an evidence-based correction: P, test the revised version; Q, identify the error; R, revise the faulty step; S, compare the original result with the requirement?

A. P–R–Q–S
B. S–Q–R–P
C. R–S–P–Q
D. Q–P–S–R

### Q2. [1 Mark] [NAT]

A bag contains two red and two blue balls. Two balls are drawn without replacement. The first ball's colour is not revealed. A truthful observer reports only that at least one of the drawn balls is red. What is the probability that both are red? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q3. [1 Mark] [MCQ]

“The witness gave an equivocal reply: it could reasonably be understood as either agreement or refusal.” In this sentence, “equivocal” most nearly means:

A. deliberately brief
B. supported by independent evidence
C. open to conflicting interpretations
D. expressing definite agreement

### Q4. [1 Mark] [NAT]

Find the positive real x satisfying 3^(x+1)=27×9^(x−2).

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

Which sentence unambiguously states that the researchers, rather than the samples, were exhausted when they repeated the experiment?

A. Exhausted, the experiment was repeated on the samples by the researchers.
B. The exhausted researchers repeated the experiment on the samples.
C. The researchers repeated the experiment on the exhausted samples.
D. Repeated by the researchers, the exhausted experiment used the samples.

### Q6. [2 Marks] [NAT]

A solid cube is assembled from 27 unit cubes in a 3×3×3 arrangement. Remove the central unit cube of each of its six faces, leaving all other unit cubes in place. Count every face of a remaining unit cube that is adjacent to empty space, including space within the resulting openings. What is the total exposed area in square units?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

Evaluate the sum from n=1 to8 of1/[n(n+2)].

**Answer format:** Decimal rounded to four places.

### Q8. [2 Marks] [NAT]

An open cylindrical container has a horizontal base area100 square centimetres and initially contains water to depth5 cm. A solid cube of side4 cm is placed flat on the bottom without spilling water. Assuming the cube becomes fully submerged, what is the final water depth?

**Answer format:** Exact decimal in centimetres.

### Q9. [2 Marks] [MCQ]

Choose the revision that is grammatically correct and preserves both intended meanings: Mira did not leave earlier, so she missed the train; Mira, not the meeting, reached the office late.

Original: “If Mira had left earlier, she will catch the train. Having reached the office late, the meeting had already begun.”

A. If Mira left earlier, she will catch the train. Having reached the office late, the meeting began.  
B. If Mira had left earlier, she would have caught the train. When Mira reached the office late, the meeting had already begun.  
C. If Mira had left earlier, she would catch the train. Having reached the office late, the meeting had begun.  
D. If Mira would have left earlier, she caught the train. When the meeting reached the office late, Mira had begun.

### Q10. [2 Marks] [NAT]

A100-kg salt solution contains10% salt by mass. Exactly20kg of water evaporates, with no salt lost. Then10kg of the remaining uniform solution is removed and replaced by10kg of pure water. What is the final salt percentage by mass?

**Answer format:** Exact percentage without the percent sign.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Under multiplication modulo 10, consider the set {2,4,6,8}. It forms a group with identity 6. What is the order of the element 2 in this group, namely the least positive k for which 2^k is the group identity?

**Answer format:** Exact integer.

### Q12. [1 Mark] [MCQ]

A language has lexically nested procedures. Procedure P contains Q and R; Q calls R. In a stack activation record for R, which relationship is correct under the usual static-link and dynamic-link model?

A. Both links point to Q's activation record.
B. The static link identifies P's activation; the dynamic link identifies Q's activation.
C. The static link identifies Q's activation; the dynamic link identifies P's activation.
D. Both links identify P's activation regardless of the caller.

### Q13. [1 Mark] [MCQ]

An out-of-order processor retires instructions in program order. Stores may execute speculatively but do not modify architecturally visible memory until retirement. Why is this restriction useful for precise exceptions?

A. It ensures a younger store cannot become visible before an older faulting instruction is handled.
B. It makes every load take one cycle.
C. It eliminates all data dependencies.
D. It guarantees that speculative branches are always predicted correctly.

### Q14. [1 Mark] [MCQ]

Three-address code evaluates `(a+b)*(a+b)` with exact scalar arithmetic and unchanged operands. Which sequence computes it using only two arithmetic operations?

A. t=a+b; r=t*t
B. t=a*b; r=t+t
C. t=a+a; r=t*b
D. t=a+b; r=t+b

### Q15. [1 Mark] [MCQ]

For n≥2, consider the following pseudocode, with constant-time integer operations:

```text
j=1;
for i=1 to n:
    while j<=i:
        j=2*j;
```

What is the tight asymptotic running time?

A. Theta(log n)
B. Theta(n log n)
C. Theta(n)
D. Theta(n²)

### Q16. [1 Mark] [MCQ]

A process forks, then its child successfully executes a new program using exec. Which statement is correct under ordinary process semantics?

A. exec necessarily creates another process with a new process identifier.
B. The child keeps its process identity while its program image is replaced.
C. The parent's program image is replaced by the child's exec.
D. The child resumes at the instruction after the successful exec call in its old program.

### Q17. [1 Mark] [NAT]

A scalar five-stage pipeline issues one instruction each cycle when unobstructed. A taken branch incurs two lost issue cycles; an untaken branch incurs none. An execution contains100 instructions, including20 branches, of which12 are taken. Ignore pipeline filling and draining and assume no other stalls. How many issue cycles are needed?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

Under set semantics R(A)={1,2,3}, S(A)={2,4}, and T(A)={1,4}. How many tuples are in (R−S)∪(S∩T)?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

In a C implementation, sizeof(int)=4 and sizeof(int*)=8. A caller declares int b[10]. In a function declared void f(int a[10]), what is sizeof(b) in the caller minus sizeof(a) inside f, in bytes?

**Answer format:** Integer.

### Q20. [1 Mark] [MCQ]

A three-variable Karnaugh map represents F=1 exactly when an even number of inputs are1. There are no don't-care entries. Which statement about a two-level SOP using only uncomplemented or complemented input literals is correct?

A. One four-cell group covers all1-cells.
B. Two two-cell groups cover all1-cells.
C. Four singleton groups are required.
D. No SOP can represent this function.

### Q21. [1 Mark] [MSQ]

A bipartite graph has left vertices a,b,c and right vertices1,2,3. Its edges are a–1,a–2,b–2,c–2,c–3. Which statements are correct?

A. The graph has exactly one perfect matching.
B. Removing edge a–2 destroys every perfect matching.
C. Edge b–2 belongs to every perfect matching.
D. Adding edge b–1 creates a second perfect matching.

### Q22. [1 Mark] [MCQ]

A sorted array is [1,2,2,2,4,4,7]. A lower-bound search returns the first index whose key is at least x, while an upper-bound search returns the first index whose key is greater than x. Both return 7 if no such index exists, and indexing starts at zero. What pair is returned for x=4?

A. (3,5)
B. (4,5)
C. (4,6)
D. (5,6)

### Q23. [1 Mark] [NAT]

A process with three private writable pages forks using copy-on-write. Initially all three physical pages are shared between parent and child. The parent writes page 0, the child writes page 1, and the parent writes page 0 again. Neither process exits. A first write to a shared page makes one physical copy; a write to an exclusively owned page makes none. How many physical pages now hold these processes' three logical pages each?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

How many binary strings of length4 contain exactly one occurrence of the substring00? Occurrences may overlap; for example,0001 contains two occurrences.

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

How many proper vertex colorings of a labelled five-cycle exist using three available labelled colors? Adjacent vertices must differ; not every color need be used.

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

A port-address translator has one public IPv4 address and may allocate any source port from 40000 through 40099 inclusive. It must assign distinct translated source ports to simultaneous TCP connections that all contact the same external address and port. What is the maximum number of such connections it can distinguish using this pool?

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

Let L1={aⁿbⁿ:n≥0} and L2={aⁿb^(2n):n≥0}. Which statements are true?

A. L1∪L2 is context-free.
B. L1∩L2={ε}.
C. Every intersection of two context-free languages is context-free.
D. L1L2 is context-free.

### Q28. [1 Mark] [NAT]

A three-variable Boolean function F(A,B,C), with A as the most significant index bit, is 1 exactly at minterms 0,1,2,5,6,7 and has no don't-cares. How many distinct minimum-product-term sum-of-products covers can be formed using only prime implicants? Ignore the order of terms.

**Answer format:** Numeric value; integer.

### Q29. [1 Mark] [NAT]

An instruction uses base-plus-scaled-index addressing: effective address=base+4×index+displacement. The index register contains−3, base contains100 and displacement is20. A32-bit word is loaded from that effective address. What is the byte address of its last byte?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

A finite language contains no word longer than20 symbols. Why can21 serve as a pumping length in the necessary pumping condition for regular languages?

A. Every word in the language has a nonempty substring of length21.
B. Every word of length21 must be in the language.
C. There are no language words of length at least21 to which the pumping requirement applies.
D. Pumping lengths may be chosen only for infinite languages.

### Q31. [1 Mark] [NAT]

A singly linked list has a noncyclic prefix of three nodes followed by a cycle of four nodes. A slow pointer and a fast pointer both start at the head. In each iteration slow advances one link and fast advances two. Equality is tested only after these advances. After how many iterations do they first point to the same node?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

A TCP sender has congestion window6000 bytes, advertised receive window4500 bytes and3000 unacknowledged bytes. It has unlimited data ready, and no other sending restriction applies. How many additional bytes may it send without a new acknowledgment or window update?

**Answer format:** Integer.

### Q33. [1 Mark] [MCQ]

Two blocking message queues A and B each have capacity one and are initially empty. Process P sends two messages to A before receiving from B. Process Q sends two messages to B before receiving from A. Both processes are eventually scheduled, and neither removes messages in any other way. What happens?

A. Both processes necessarily complete because the queues start empty.
B. Only P can block; Q cannot.
C. Both eventually block on their second send, with neither able to reach its receive.
D. Sending to a full queue automatically deletes the older message.

### Q34. [1 Mark] [MCQ]

A stack initially empty receives items1,2,3,4 in that order. Pops may be interleaved with pushes. Which proposed output sequence is impossible?

A. 2,1,4,3
B. 3,2,1,4
C. 3,1,2,4
D. 4,3,2,1

### Q35. [1 Mark] [NAT]

Let A have rows (1,1),(1,1). Find trace(A⁵).

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

For what real value of k does the following system have infinitely many solutions?

```text
x + y + z = 2
2x + 3y + 4z = 5
3x + 4y + 5z = k
```

**Answer format:** Exact number.

### Q37. [2 Marks] [MSQ]

Let HALT={(M,w): M eventually halts on w}. Assume a computable many-one reduction from HALT to a language L. Which conclusions follow?

A. L cannot be decidable.
B. L must be recursively enumerable.
C. A decider for L would yield a decider for HALT.
D. The existence of this reduction alone guarantees a computable many-one reduction from L to HALT.

### Q38. [2 Marks] [MSQ]

In first-order notation, consider the query {x : R(x) AND (exists x S(x))}, where the inner quantifier binds only its own occurrence of x and shadows the outer name within its parentheses. R and S are finite unary relations. Which statements are correct?

A. Renaming the bound inner variable to y leaves the query unchanged.
B. The query always returns R intersect S.
C. If S is nonempty, the query returns all of R.
D. If S is empty, the query returns the empty relation.

### Q39. [2 Marks] [NAT]

The complete undirected graph on labelled vertices A,B,C,D has one edge between every pair. How many spanning trees contain edge AB but do not contain edge AC?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

A basic block is `t=a+b; a=a+1; u=a+b; v=t;`. Arithmetic is exact, and scalar variables have no aliases. Which transformations preserve the final values of a,t,u,v for all initial a,b?

A. Replace `v=t` by `v=a+b-1` after the other statements.
B. Replace `u=a+b` by `u=t`.
C. Replace `u=a+b` by `u=t+1`.
D. Delete `t=a+b` while leaving `v=t` unchanged and without introducing another definition of t.

### Q41. [2 Marks] [MSQ]

A TCP peer performs an orderly shutdown of its sending direction after transmitting some bytes. The receiver drains all those bytes. Assume no errors. Which statements are correct?

A. A subsequent receive can return zero to indicate end-of-stream in that direction.
B. The receiver must treat zero as one received byte whose value is0.
C. A half-close does not by itself prevent the other direction from carrying data.
D. TCP requires both applications to terminate immediately when one direction closes.

### Q42. [2 Marks] [MSQ]

Consider the following control-flow graph. Variables are ordinary scalars without aliases, both branches are feasible, and only the returned value is observable. A variable is live at a point if some path from that point reads its current value before redefining it.

```text
B1: x = a+b
    y = x*c
    if p goto B2 else B3
B2: z = y+1
    goto B4
B3: x = a-b
    z = x+c
    goto B4
B4: return z
```

At the point immediately after `y=x*c` and before the conditional, which statements are correct?

A. y is live.
B. c is dead.
C. x is dead.
D. a is live.

### Q43. [2 Marks] [NAT]

A rooted tree has 15 vertices. Every internal vertex has exactly three children. How many leaves does it have?

**Answer format:** Enter -1 if no such tree exists; otherwise enter the number of leaves.

### Q44. [2 Marks] [NAT]

Insert keys8,4,12,2,6,10,14,5 into an initially empty BST without rotations. Delete8 by replacing its key with its inorder successor and deleting that successor's original node. What is the edge distance from the new root to key5 afterward?

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

SQL uses bag semantics and ordinary three-valued logic. T(k) has rows 1,1,NULL and U(k) has rows 1,NULL. How many rows does this query return?

```sql
SELECT T.k, U.k
FROM T LEFT JOIN U ON T.k = U.k
WHERE U.k IS NULL;
```

**Answer format:** Exact integer.

### Q46. [2 Marks] [NAT]

Four matrices A,B,C,D have dimensions 5×10, 10×2, 2×8 and 8×3. Using ordinary matrix multiplication with pqr scalar multiplications for a p×q by q×r product, what is the minimum scalar multiplication count over all parenthesizations of ABCD?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

An algorithm splits a size-n problem, where n is a power of two, into two half-size subproblems and then merges in Θ(n/log₂n) time for n≥4. Its running time satisfies T(n)=2T(n/2)+Θ(n/log₂n), with constant base cases at n≤2. What is the tight bound?

A. Θ(n)
B. Θ(n log log n)
C. Θ(n log n)
D. Θ(n²)

### Q48. [2 Marks] [NAT]

In a four-bit adder, each propagate signal P_i=A_i XOR B_i is available at time 2, each generate G_i=A_i AND B_i at time 1, and input carry C0 at time 0. AND and OR gates each add one unit delay, with unlimited fan-in. A ripple implementation uses C_(i+1)=G_i OR (P_i AND C_i). A lookahead implementation directly forms C4 as the OR of its five standard product terms. How many delay units earlier is C4 available with lookahead than with ripple? Use the latest-input timing bound for every gate.

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

A directed graph has edges a→b,b→a,b→c,c→d,d→c,d→e and isolated vertex f. How many strongly connected components have no outgoing edge to a different component?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

Three independent draws select uniformly from three colours, with replacement. Let D be the number of distinct colours observed. What is Var(D)?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

### Q51. [2 Marks] [MSQ]

Exact integer variable x starts at zero. A loop executes `x=1-x` an arbitrary finite number of times, possibly zero. After the loop, y=x*(x−1) is evaluated. Which statements are true?

A. x is necessarily zero after the loop.
B. x is always either zero or one after the loop.
C. y is always zero and may be replaced by that constant.
D. y can equal one if the iteration count is odd.

### Q52. [2 Marks] [NAT]

Over {0,1}, a language contains exactly strings whose third symbol from the right is 1. Strings shorter than three symbols are rejected. How many states are required by a minimal complete DFA?

**Answer format:** Integer.

### Q53. [2 Marks] [MCQ]

A file contains bytes abcdef. fd1 opens it read-only; fd2=dup(fd1); fd3 opens the same pathname independently. All operations succeed. Read two bytes from fd1, one from fd2, and one from fd3. Then seek fd2 to absolute offset 1 and read two bytes from fd1. Which bytes does this final read return?

A. de  
B. ab  
C. bc  
D. cd

### Q54. [2 Marks] [MSQ]

Resource A has two instances and B has one. P holds one A and requests B; Q holds B and requests one A; R holds the other A and requests nothing more. A process that receives its request completes and releases its resources; R can complete immediately. Which statements are correct?

A. The system can finish all processes in order R,Q,P.
B. The cycle involving P and Q proves deadlock even with R able to release an A instance.
C. A cycle in the resource-allocation graph is not sufficient here to establish deadlock.
D. Releasing R's A can enable Q, whose completion can then enable P.

### Q55. [2 Marks] [NAT]

A microinstruction independently selects one of nine source choices, one of five ALU choices, and any subset of eight destination registers, including the empty subset. A format with separate fixed-width binary source and ALU fields plus an eight-bit destination mask is compared with an unrestricted single binary field encoding all legal combinations. How many bits does the separate-field format require in excess of the minimum single-field width?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

A binary min-heap contains seven distinct keys in a one-based array. How many positions could contain the maximum key, considering all valid heaps of that size?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

How many functions f:{1,2,3,4,5}→{1,2,3,4,5} satisfy f(f(x))=x for every x and have exactly one fixed point?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

A single CPU uses round-robin scheduling with quantum 2 and zero switching overhead. Processes A,B,C have (arrival,burst) values (0,5),(1,4),(2,2). At a quantum boundary, new arrivals join the ready queue before the preempted running process is requeued. A process whose burst finishes is not requeued. What is the mean waiting time?

**Answer format:** Decimal rounded to two places.

### Q59. [2 Marks] [MSQ]

Grammar S→aSa | bSb | a | b is over{a,b}. Which statements are correct?

A. Every generated string is an odd-length palindrome.
B. The grammar generates ε.
C. Reversing a generated string always gives a generated string.
D. The language is closed under concatenation.

### Q60. [2 Marks] [MSQ]

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

### Q61. [2 Marks] [NAT]

Evaluate a binary expression tree using two rules: evaluate both children recursively, retain the first child's result while evaluating the second, then combine the results in one register and release the other. Leaves require one register. Child evaluation order may be chosen independently at each node, and no spilling or recomputation is allowed. The expression is `(a+b)*((c+d)+(e+f))`, with all leaves distinct. What is the minimum number of registers needed?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A four-to-one multiplexer selects data input D(2s1+s0), where s1,s0 are the select bits. To implement F(a,b,c)=1 exactly when precisely one of a,b,c is1, choose s1=a,s0=b. Each data input may be0,1,c,or NOT c. How many of the four required data inputs equal NOT c?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A synchronous four-bit register has next-state rule(a,b,c,d)→(b,c,d,a XOR b), evaluated from the old state. Starting from0001, what is the smallest positive number of clock edges after which the register returns to0001?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

Assume ordinary TCP, UDP and IPv4 layering, without application-specific boundary reconstruction. Which statements are correct?

A. TCP does not preserve individual application write boundaries as receive-message boundaries.
B. A UDP datagram can never be fragmented at the IPv4 layer.
C. IPv4 fragmentation may be hidden from the receiving UDP application by IP reassembly.
D. A link-layer frame's header must remain unchanged across all routers on a path.

### Q65. [2 Marks] [NAT]

Define sat(x)=min(7,max(−8,x)). All additions below apply this signed four-bit saturation after each addition. For a=7,b=3,c=−3, calculate sat(sat(a+b)+c)−sat(a+sat(b+c)).

**Answer format:** Exact signed integer.

---

## ANSWER KEY — MOCK TEST 093

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 0.2000 (accepted range 0.19995–0.20005) |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 2 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 78 (exact) |
| 7 | NAT | 2 | 0.6444 (accepted range 0.64435–0.64445) |
| 8 | NAT | 2 | 5.64 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 10.9375 |
| 11 | NAT | 1 | 4 |
| 12 | MCQ | 1 | B |
| 13 | MCQ | 1 | A |
| 14 | MCQ | 1 | A |
| 15 | MCQ | 1 | C |
| 16 | MCQ | 1 | B |
| 17 | NAT | 1 | 124 |
| 18 | NAT | 1 | 3 |
| 19 | NAT | 1 | 32 |
| 20 | MCQ | 1 | C |
| 21 | MSQ | 1 | A, C, D |
| 22 | MCQ | 1 | C |
| 23 | NAT | 1 | 5 |
| 24 | NAT | 1 | 5 |
| 25 | NAT | 1 | 30 |
| 26 | NAT | 1 | 100 |
| 27 | MSQ | 1 | A, B, D |
| 28 | NAT | 1 | 2 (exact) |
| 29 | NAT | 1 | 111 |
| 30 | MCQ | 1 | C |
| 31 | NAT | 1 | 4 |
| 32 | NAT | 1 | 1500 |
| 33 | MCQ | 1 | C |
| 34 | MCQ | 1 | C |
| 35 | NAT | 1 | 32 |
| 36 | NAT | 2 | 7 |
| 37 | MSQ | 2 | A, C |
| 38 | MSQ | 2 | A, C, D |
| 39 | NAT | 2 | 5 |
| 40 | MSQ | 2 | A, C |
| 41 | MSQ | 2 | A, C |
| 42 | MSQ | 2 | A, C, D |
| 43 | NAT | 2 | -1 |
| 44 | NAT | 2 | 3 |
| 45 | NAT | 2 | 1 |
| 46 | NAT | 2 | 178 |
| 47 | MCQ | 2 | B |
| 48 | NAT | 2 | 6 |
| 49 | NAT | 2 | 2 |
| 50 | NAT | 2 | 0.3210 (accepted range 0.32095–0.32105) |
| 51 | MSQ | 2 | B, C |
| 52 | NAT | 2 | 8 (exact) |
| 53 | MCQ | 2 | C |
| 54 | MSQ | 2 | A, C, D |
| 55 | NAT | 2 | 1 |
| 56 | NAT | 2 | 4 |
| 57 | NAT | 2 | 15 |
| 58 | NAT | 2 | 4.33 (two decimals) |
| 59 | MSQ | 2 | A, C |
| 60 | MSQ | 2 | A, B, D |
| 61 | NAT | 2 | 3 |
| 62 | NAT | 2 | 2 |
| 63 | NAT | 2 | 15 |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | -3 |
