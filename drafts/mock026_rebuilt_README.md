# GATE CS 2027 — Full-Length Mock Test 026

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the other questions carry two. Each MCQ has exactly one correct option and loses one-third of its marks for an incorrect response. MSQs require all correct options with no partial credit. MSQs and NATs have no negative marking. Unattempted questions score zero. GA contributes15 marks, Engineering Mathematics13 and core CS72. Numerical values are exact unless rounding is requested.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“The two estimates are commensurate because both measure annual cost in the same currency; this does not mean they are equal.” Which meaning of “commensurate” fits this explanation?

A. Comparable on a common basis.
B. Necessarily identical in magnitude.
C. Deliberately misleading.
D. Measured without units.

### Q2. [1 Mark] [NAT]

How many integers n with1≤n≤100 satisfy floor(log2 n)=floor(log3 n)? Here floor rounds downward to an integer.

**Answer format:** Integer.
### Q3. [1 Mark] [MCQ]

A rule returns the median of an odd-length list of real numbers. To the list, append one number strictly smaller than every original entry and one strictly larger than every original entry. What follows about the returned median?

A. It is unchanged.
B. It strictly increases.
C. It becomes the average of the two appended numbers.
D. It cannot be related to the original median without knowing every entry.
### Q4. [1 Mark] [NAT]

A2×2×2 array of unit cubes has all eight cubes present. Two cubes sharing one full face are removed. What is the total exposed surface area of the remaining solid, including newly exposed faces?

**Answer format:** Integer square units.

### Q5. [1 Mark] [NAT]

A sequence satisfies a1=1 and a(n+1)=a(n)+n(n+1) for n≥1. What is a5?

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

The diagonals of a trapezium ABCD intersect at O, with AB parallel to CD. The areas of triangles AOB and COD are 4 and 9 square units respectively. What is the area of the entire trapezium?

**Answer format:** Integer square units.
### Q7. [2 Marks] [MCQ]

A policy says, “Unless a submission is anonymous, it must include the author's name.” Which submission violates this rule?

A. An anonymous submission without a name.
B. A nonanonymous submission with a name.
C. A nonanonymous submission without a name.
D. An anonymous submission with a name.

### Q8. [2 Marks] [NAT]

A retailer marks an item25% above cost and gives a discount of d% on the marked price. The final profit is5% of cost. What is d?

**Answer format:** Exact percentage number.

### Q9. [2 Marks] [MSQ]

Exactly one of propositions p,q,r is true. Additionally, p implies q. Which statements must hold?

A. p is false.
B. Exactly one of q,r is true.
C. q is necessarily true.
D. q and r cannot both be false.

### Q10. [2 Marks] [NAT]

A square has vertices(0,0),(2,0),(2,2),(0,2). It is rotated90 degrees anticlockwise about(1,1) and then translated by(3,−1). What is the sum of the x-coordinates of its four resulting vertices?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A2×2 real matrix A has trace5 and determinant6. What is det(A−I)?

**Answer format:** Exact number.

### Q12. [1 Mark] [MSQ]

Let f(x)=|x| for real x. Which statements are correct at x=0?

A. f is continuous.
B. Its left derivative is−1 and its right derivative is1.
C. Its derivative exists and equals0 because f has a minimum there.
D. Every continuous function is differentiable there.

### Q13. [1 Mark] [NAT]

An inode has a link count of3. One pathname is renamed within the same file system without replacing an existing destination, and another pathname is then unlinked. Assume no other directory changes. What is the inode's final hard-link count?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A postfix translation emits each operand when visited and emits an operator after both children. How many operator symbols appear in the postfix form of(a+b)*(c−d/e)?

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

X takes values−2 and2 with equal probability. Let Y=X². What is Var(Y)?

**Answer format:** Exact number.


### Q16. [1 Mark] [NAT]

Two IPv4 ranges are10.0.0.0/25 and10.0.0.64/26. How many distinct addresses belong to their union?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A successful read system call requests10 bytes but returns4, having copied four bytes and advanced the regular file's offset by four. The caller then successfully reads the remaining six bytes. If the initial offset was20 and no seeks occur, what is the final offset?

**Answer format:** Integer.

### Q18. [1 Mark] [MSQ]

A cover-minimization procedure has two feasible covers: C1 uses two rows with total cost8; C2 uses three rows with total cost6. Each is assumed optimal for the count/cost pair shown, and no other cover improves either objective. Which statements are correct?

A. Minimizing row count first and total cost second selects C1.
B. Minimizing total cost first and row count second selects C2.
C. The two objectives necessarily choose the same cover.
D. Reporting only “minimum cover” without specifying the objective can be ambiguous here.

### Q19. [1 Mark] [MSQ]

Functions f:A→B and g:B→C have injective composition g∘f. Which statements necessarily follow?

A. f is injective.
B. g is injective on all of B.
C. g is injective when restricted to f(A).
D. f is surjective onto B.

### Q20. [1 Mark] [NAT]

Choose a uniformly from{0,1,2,3,4}, and define hash h_a(x)=ax modulo5 on keys{0,1,2,3,4}. For distinct keys x,y, what is P(h_a(x)=h_a(y))?

**Answer format:** Exact decimal.

### Q21. [1 Mark] [NAT]

A procedure F(n) returns immediately for n≤1 and otherwise calls F(floor(n/2)) once. Including the initial invocation and the base invocation, how many calls occur for n=19?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

In a C implementation, sizeof(int)=4 and sizeof(int*)=8. A caller declares int b[10]. In a function declared void f(int a[10]), what is sizeof(b) in the caller minus sizeof(a) inside f, in bytes?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

T2 reads a value written by T1 before either commits. T3 is independent of both. Ignoring all other constraints, how many of the six possible orders of the three commit events satisfy recoverability for this read dependency?

**Answer format:** Integer.

### Q24. [1 Mark] [MSQ]

Initially x=y=1 and a database invariant requires x+y≥1. Two concurrent transactions read the same initial snapshot. T1, seeing y=1, writes x=0; T2, seeing x=1, writes y=0. A scheme rejects only concurrent writes to the same item, so both commit. Which statements are correct?

A. Their writes target different items.
B. The final state violates the invariant.
C. The execution is equivalent to a serial execution of these conditional transactions.
D. Avoiding direct write-write conflicts alone is insufficient for this invariant.

### Q25. [1 Mark] [MCQ]

A language passes a scalar argument by value. A callee assigns a new scalar value to its parameter but does not access the caller's storage through any pointer or reference. Which statement is correct?

A. The assignment necessarily changes the caller's variable.
B. The assignment changes the callee's parameter value without thereby changing the caller's scalar variable.
C. Pass-by-value means the parameter cannot be assigned.
D. Pass-by-value requires the caller and callee to share one parameter storage cell.

### Q26. [1 Mark] [NAT]

A NAT can allocate public ports4000 through4007 inclusive on each of two public IPv4 addresses. Each simultaneous mapping consumes a distinct(public address,public port) pair, and no reuse is allowed. How many simultaneous mappings can it support?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A doubly linked list has consecutive nodes A,B,C. Deleting B without a sentinel requires setting A.next=C and C.prev=A. How many pointer fields in the surviving nodes must change?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

An instruction has a12-bit signed displacement encoded in two's complement and scaled by four bytes. What is the most negative byte displacement it can encode?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

An unsigned w-bit subtraction is implemented as A+(bitwise NOT B)+1, with the final carry-out retained. Which statements are correct?

A. The low w bits equal(A−B) modulo2^w.
B. Carry-out1 indicates no unsigned borrow under this convention.
C. Carry-out1 necessarily indicates signed overflow.
D. The low result bits alone always reveal whether unsigned borrowing occurred.

### Q30. [1 Mark] [NAT]

For n=16, how many times does work() execute?

```text
i = n
while i > 0:
    for j = 1 to i:
        work()
    i = floor(i/2)
```

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

A PDA can make epsilon transitions that do not consume input. Which statements are correct?

A. An epsilon transition may still change the state and stack.
B. Every epsilon transition must leave the stack unchanged.
C. A computation can contain several epsilon transitions between consecutive consumed symbols.
D. An epsilon transition consumes a special extra input character not in the input string.

### Q32. [1 Mark] [NAT]

In an ER model, each employee belongs to exactly one department, and each department may have any number of employees. There are12 employees and four departments. How many employee-department relationship instances exist?

**Answer format:** Integer.

### Q33. [1 Mark] [MSQ]

L is a finite language over a finite alphabet. Which statements necessarily hold?

A. L is regular.
B. L is context-free.
C. L contains the empty string.
D. Some DFA recognizes L.

### Q34. [1 Mark] [NAT]

A2×2 real matrix has eigenvalues3 and−1. What is trace(A²)?

**Answer format:** Exact number.

### Q35. [1 Mark] [NAT]

A two-input XOR gate's inputs are tied to the same Boolean signal x. Its output feeds one input of a two-input OR gate whose other input is y. How many of the four assignments to(x,y) make the circuit output1?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

Relations R(A,B)={(1,x),(1,y),(2,x),(3,z)} and S(B,C)={(x,p),(x,q),(y,p)} use set semantics. How many tuples remain after naturally joining R with S and then projecting onto(A,C)?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

Let s=aabbb and L=a*b*. Consider decompositions s=xyz satisfying |xy|≤3 and |y|>0. How many such decompositions have xy^i z in L for every integer i≥0? Different choices of the lengths of x and y count separately.

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

A multithreaded process has threads T1,T2. T2 holds a user-space mutex when T1 duplicates the process using a model in which the child contains only the calling thread but inherits a copy of the mutex's locked state. In the child, no automatic repair occurs and no surviving thread can release T2's lock. Which statements are correct?

A. The child's copied mutex may remain permanently locked.
B. The child's copy of T2 necessarily continues and releases it.
C. Waiting on that mutex in the child can block indefinitely under this model.
D. The parent's later unlock necessarily changes the child's private copied mutex state.

### Q39. [2 Marks] [NAT]

A synchronous three-bit register has next state(a,b,c)→(b,c,NOT a). It starts at000. Its output is1 exactly when the current state has two1 bits. Count output1 states among the first twelve states observed, including the initial state as observation1.

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

An algorithm receives a Turing machine M and a nonnegative integer k written in binary. It asks whether M, started on blank input, halts within k steps. Which statements are correct?

A. This bounded question is decidable by direct simulation.
B. A potentially enormous value of k makes the problem undecidable.
C. The same simulation strategy decides eventual halting without any bound by choosing one universally sufficient finite k.
D. Binary encoding can make the simulation duration much larger than the length of k's representation.

### Q41. [2 Marks] [NAT]

A DFA over{a,b} has three states0,1,2, start0 and sole accepting state2. On a, transitions are0→1,1→2,2→2. On b, transitions are0→0,1→0,2→2. How many strings of length4 are accepted?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

For a finite relation R(x,y), consider the formula R(x,y) AND NOT exists z(R(x,z) AND z≠y), with x,y free. Which statements are correct?

A. It selects tuples whose x value has exactly one distinct associated y value in R.
B. It rejects every tuple whenever R contains two different x values.
C. The existential variable z ranges over possible competing y values for the same x.
D. It can return an(x,y) pair not in R.

### Q43. [2 Marks] [NAT]

A differentiable function f on[0,2] has f(0)=f(2)=0 and is twice differentiable on(0,2), with f''(x)>0 throughout. How many zeros of f' exist in(0,2)?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

Three jobs have deadlines and profits(d,p): A=(1,20), B=(2,15), C=(2,10). Every job takes one unit of time, only one runs at a time, time slots finish at1 and2, and a profit is earned only if the job finishes by its deadline. What is the maximum total profit?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A microsequencer stores a subroutine return address in one link register, with no stack or other saved copy. Main calls micro-subroutine U, which calls V before returning. V returns via the link register, then U also returns through it. How many distinct return addresses must be simultaneously preserved at the moment V is entered for both returns to work correctly?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

An array has values[4,−1,2,−7,5,−2,3]. A nonempty contiguous subarray may have at most one element deleted from it, but at least one element must remain. What is the maximum sum achievable?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A memory device has address inputs A0–A9 and one active-high chip-select. A system connects only A0–A8 to varying address bits and permanently ties A9 to0. What fraction of the device's addressable locations can be selected through this wiring?

**Answer format:** Exact decimal.

### Q48. [2 Marks] [NAT]

A sender has transmitted bytes100 through699 inclusive. It receives a cumulative TCP ACK with acknowledgment number400 and a selective acknowledgment block[500,700). Ignoring retransmission policy, how many transmitted bytes remain neither cumulatively acknowledged nor covered by that SACK block?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

A three-address intermediate representation has one binary operation per assignment. To compute a*b+a*c+d*b+d*c, a compiler may reassociate and factor over mathematical integers and reuse intermediates. What is the minimum number of binary additions/multiplications needed if it uses the factorization(a+d)*(b+c)?

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

A synchronous message-passing send completes only when a matching receive occurs. Process P first sends to Q and then receives from Q; process Q first sends to P and then receives from P. Neither channel buffers a message. Which statements are correct?

A. Both processes can block on their first operation.
B. The program is guaranteed to finish because each process eventually has a receive in its source code.
C. Changing Q to receive first and then send removes this particular cyclic wait.
D. Adding a mutex around both sequences necessarily fixes the protocol.

### Q51. [2 Marks] [MSQ]

A TCP peer performs an orderly shutdown of its sending direction after transmitting some bytes. The receiver drains all those bytes. Assume no errors. Which statements are correct?

A. A subsequent receive can return zero to indicate end-of-stream in that direction.
B. The receiver must treat zero as one received byte whose value is0.
C. A half-close does not by itself prevent the other direction from carrying data.
D. TCP requires both applications to terminate immediately when one direction closes.

### Q52. [2 Marks] [NAT]

A stack stores integers using the following minimum-encoding scheme. The first push stores the value and sets m to it. To push x<m, store 2x−m and set m=x; otherwise store x. When popping a stored value y<m, return the old m and then set m=2m−y; otherwise return y and leave m unchanged. Arithmetic has unlimited precision. Starting empty, execute push(7), push(3), push(5), push(−2), pop(), pop(), push(1), pop(), pop(). What is the sum of the four returned values?

**Answer format:** Integer.
### Q53. [2 Marks] [MSQ]

A rooted ordered full binary tree has exactly four leaves. Every internal node has a left and a right child, and the root has depth 0. Which lists can be the depths of its leaves in left-to-right order?

A. (1,2,3,3)
B. (2,1,3,3)
C. (2,2,2,2)
D. (3,3,1,2)
### Q54. [2 Marks] [NAT]

A fair coin chooses one of two bags. Bag A contains two red and one blue ball; bag B contains one red and two blue balls. Two draws are made without replacement from the chosen bag. Given that the second draw is red, what is the probability that the first draw was blue? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q55. [2 Marks] [NAT]

Four memory banks are selected by word address modulo 4. Each request occupies its bank for 3 cycles; a bank accepting a request at cycle t is available again at t+3. The controller issues at most one request per cycle, in the listed order, and stalls if the next request's bank is busy. Initially all banks are idle. For word addresses 0,4,1,5,2,6,3,7, with the first issue at cycle 0, at what cycle does the last request finish?

**Answer format:** Integer cycle number.
### Q56. [2 Marks] [MSQ]

An optimizer replaces a conditional assignment by unconditional arithmetic. In the original program, an expression on an untaken branch is not evaluated and may divide by zero if evaluated. Which statements are correct?

A. Preserving the selected numerical result alone is enough to justify evaluating both branches.
B. Introducing a previously avoided invalid division can change program behavior.
C. A proof that both branch expressions are safe and side-effect-free is relevant to such a rewrite.
D. Branch removal never changes which expressions are evaluated.

### Q57. [2 Marks] [NAT]

A signed fixed-point representation stores an eight-bit two's-complement integer scaled by1/16. What is the width of its representable real interval, defined as largest value minus smallest value?

**Answer format:** Exact decimal.

### Q58. [2 Marks] [NAT]

Table A(k) contains1,1,2 and table B(k) contains1,1,3, with no NULLs. Under SQL bag semantics, how many rows does SELECT A.k FROM A JOIN B ON A.k=B.k return?

**Answer format:** Integer.

### Q59. [2 Marks] [MSQ]

Distinct keys are inserted into an unbalanced BST. Which statements are correct?

A. Inserting sorted ascending keys can produce height n−1 for n keys, counting edges.
B. The inorder traversal is sorted regardless of insertion order.
C. Every insertion order produces the same tree shape.
D. A sorted inorder traversal proves that search always takes logarithmic time.

### Q60. [2 Marks] [MSQ]

At a control-flow join, a compiler's scalar constant analysis knows x is either1 or2, and y is respectively2 or1 on the same paths. It tracks each variable independently as constant or nonconstant, with no relational information. Which statements are correct?

A. Semantically, x+y is3 on every path.
B. Independent per-variable joins may lose the fact needed to infer that sum directly.
C. x is individually constant at the join.
D. A relational analysis can preserve information that this independent analysis loses.

### Q61. [2 Marks] [NAT]

A poset has elements a,b,c,d with a<b, a<c, b<d and c<d, and no other comparabilities except those forced by transitivity and reflexivity. How many linear extensions does it have?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A divide-and-conquer algorithm splits a problem of size16 into two equal children until singleton leaves. Each internal node allocates a temporary buffer equal to its subproblem size, frees it before returning, and retains its own buffer while processing its two children sequentially. Leaf nodes allocate no buffer. What is the maximum simultaneous buffer allocation, in units?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A binary floating-point format has four significant bits including the leading 1, and supports all exponents needed here. Rounding is to nearest with ties to an even least significant significand bit. Among the real inputs x=k/16 for integer k from 60 through 68 inclusive, how many round to the floating-point value 4?

**Answer format:** Integer.
### Q64. [2 Marks] [MSQ]

A DNS record is cached with a positive TTL. The authoritative server changes the record before that TTL expires. Assume ordinary caching without an explicit invalidation mechanism. Which statements are correct?

A. A resolver can continue returning the cached old record until expiry.
B. Every cache is immediately informed of the authoritative change by the TTL field itself.
C. Reducing the authoritative record's TTL afterward does not retroactively shorten a previously cached expiry under this model.
D. TTL is a guarantee that the authoritative value cannot change during that interval.

### Q65. [2 Marks] [NAT]

For an integer t in {0,1,2,3,4,5}, let A(t)=[[t,1,0],[1,1,1],[0,1,2]]. How many choices of t make A(t) nonsingular but prevent a factorization A(t)=LU with unit lower-triangular L and upper-triangular U, without row permutations?

**Answer format:** Integer.



---

## ANSWER KEY — MOCK TEST 026

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 2 |
| 3 | MCQ | 1 | A |
| 4 | NAT | 1 | 22 |
| 5 | NAT | 1 | 41 |
| 6 | NAT | 2 | 25 |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 16 |
| 9 | MSQ | 2 | A, B, D |
| 10 | NAT | 2 | 16 |
| 11 | NAT | 1 | 2 |
| 12 | MSQ | 1 | A, B |
| 13 | NAT | 1 | 2 |
| 14 | NAT | 1 | 4 |
| 15 | NAT | 1 | 0 |
| 16 | NAT | 1 | 128 |
| 17 | NAT | 1 | 30 |
| 18 | MSQ | 1 | A, B, D |
| 19 | MSQ | 1 | A, C |
| 20 | NAT | 1 | 0.2 |
| 21 | NAT | 1 | 5 |
| 22 | NAT | 1 | 32 |
| 23 | NAT | 1 | 3 |
| 24 | MSQ | 1 | A, B, D |
| 25 | MCQ | 1 | B |
| 26 | NAT | 1 | 16 |
| 27 | NAT | 1 | 2 |
| 28 | NAT | 1 | -8192 |
| 29 | MSQ | 1 | A, B |
| 30 | NAT | 1 | 31 |
| 31 | MSQ | 1 | A, C |
| 32 | NAT | 1 | 12 |
| 33 | MSQ | 1 | A, B, D |
| 34 | NAT | 1 | 10 |
| 35 | NAT | 1 | 2 |
| 36 | NAT | 2 | 4 |
| 37 | NAT | 2 | 4 |
| 38 | MSQ | 2 | A, C |
| 39 | NAT | 2 | 4 |
| 40 | MSQ | 2 | A, D |
| 41 | NAT | 2 | 8 |
| 42 | MSQ | 2 | A, C |
| 43 | NAT | 2 | 1 |
| 44 | NAT | 2 | 35 |
| 45 | NAT | 2 | 2 |
| 46 | NAT | 2 | 11 |
| 47 | NAT | 2 | 0.5 |
| 48 | NAT | 2 | 100 |
| 49 | NAT | 2 | 3 |
| 50 | MSQ | 2 | A, C |
| 51 | MSQ | 2 | A, C |
| 52 | NAT | 2 | 7 |
| 53 | MSQ | 2 | A, C |
| 54 | NAT | 2 | 0.6667 (accepted range 0.66665–0.66675) |
| 55 | NAT | 2 | 18 |
| 56 | MSQ | 2 | B, C |
| 57 | NAT | 2 | 15.9375 |
| 58 | NAT | 2 | 4 |
| 59 | MSQ | 2 | A, B |
| 60 | MSQ | 2 | A, B, D |
| 61 | NAT | 2 | 2 |
| 62 | NAT | 2 | 30 |
| 63 | NAT | 2 | 7 |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 2 |
