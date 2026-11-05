# GATE CS 2027 — Full-Length Mock Test 084

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

### Q1. [1 Mark] [MSQ]

Three nonempty groups have mean scores 40,60,80. Their sizes are positive integers but otherwise unspecified. Which statements must hold for the combined mean μ?

A. 40<μ<80.
B. μ=60.
C. μ can equal 60 for some group sizes.
D. μ is always at least 60.

### Q2. [1 Mark] [MCQ]

A circular track has two concentric lane centre-lines of radii r and r+1 metres. Two runners move at equal constant speeds toward a finish on a fixed radial line. The inner runner starts on that line and runs one complete lap. The outer runner starts ahead of that line and runs the remainder of the circuit. Both start simultaneously. By how many metres along the outer lane must its start be advanced from the finish line so that the runners finish simultaneously?

A. π
B. 2π
C. πr
D. 2πr

### Q3. [1 Mark] [MCQ]

“Not every submitted report contains a diagram.” Which statement is logically equivalent?

A. No submitted report contains a diagram.
B. At least one submitted report contains no diagram.
C. Every submitted report contains no diagram.
D. At least one report containing a diagram was not submitted.

### Q4. [1 Mark] [NAT]

A mixture contains milk and water in the ratio3:2 by volume. Ten litres are removed after thorough mixing and replaced by ten litres of pure water. The final ratio is1:1, and total volume is unchanged. What was the initial total volume, in litres?

**Answer format:** Exact number.

### Q5. [1 Mark] [MCQ]

Exactly one of three boxes contains a coin. Their labels state: A: “The coin is not in B”; B: “The coin is in this box”; C: “The coin is not in this box.” Exactly one label is true. Where is the coin?

A. Box A
B. Box B
C. Box C
D. The conditions have no solution.

### Q6. [2 Marks] [MCQ]

A plane transformation T maps (x,y) to (1−y,x). Starting at (1,0), apply T exactly 2027 times. What is the final point?

A. (1,1)
B. (0,1)
C. (0,0)
D. (1,0)

### Q7. [2 Marks] [MCQ]

A library reports: “After online reservations began, the fraction of issued books returned late fell. However, the number of late returns increased because the number of issued books rose substantially. The figures do not identify what would have happened without online reservations.” Which interpretation is justified?

A. Online reservations caused every borrower to return books sooner.
B. A lower late-return fraction is incompatible with more late returns.
C. The number of timely returns must have fallen.
D. A larger borrowing volume can coexist with a lower late-return fraction and more late returns, without establishing a causal effect.

### Q8. [2 Marks] [NAT]

Four distinct couples sit around a circular table in eight equally spaced seats. Each person's partner must sit directly opposite. Arrangements differing only by rotation are identical; mirror images are distinct. How many arrangements are possible?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

A service runs in two regions. In region X, 80% of requests succeed; in region Y, 95% succeed. Initially each region receives 100 requests. Later the number in X doubles while Y still receives 100; each regional success rate stays unchanged. By how many percentage points does the combined success rate decrease?

**Answer format:** Exact decimal, without the % sign.

### Q10. [2 Marks] [NAT]

A square sheet occupies0≤x≤4,0≤y≤4. Fold its left half onto its right half along x=2. Cut out, through both layers, the triangle with vertices(2,0),(3,0),(2,1). After unfolding, what is the perimeter of the remaining sheet? The cut boundaries are included in the perimeter.

**Answer format:** Decimal rounded to four places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A syntax-directed translation emits each operand when recognized and emits a binary operator after translating both operands. Multiplication binds more tightly than addition. What does it emit for a+b*c?

A. ab+c*
B. +a*bc
C. abc*+
D. abc+*

### Q12. [1 Mark] [MCQ]

In a lexically scoped language, procedures Q and R are both immediately nested inside P. P declares x; Q and R do not declare x. During the calls P→Q→R, R accesses P's x. Static links point to the most recent activation of the immediately enclosing lexical procedure; dynamic links point to the caller. From R's activation, how many static links and dynamic links, respectively, lead to P's activation?

A. (2,1)  
B. (1,1)  
C. (2,2)  
D. (1,2)

### Q13. [1 Mark] [NAT]

A four-bit ring counter circulates a single 1 through its flip-flops, starting at 1000. How many clock edges are needed to return to 1000 for the first time?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

A foreign key Child.parent_id references Parent.id. It uses ON DELETE SET NULL, and Child.parent_id is also declared NOT NULL. A parent with a referencing child is deleted. Assume constraints are enforced immediately and no other action modifies the child. Which statements are correct?

A. The referential action would require setting the child's foreign key to NULL.
B. The deletion can violate the child's NOT NULL constraint and be rejected.
C. SET NULL silently overrides every NOT NULL constraint.
D. The child row must necessarily be deleted instead.

### Q15. [1 Mark] [MSQ]

An IPv4 fragment has offset field 100, 400 payload bytes, and MF=1. A downstream link permits only 200 payload bytes per fragment; 200 is divisible by eight. The router splits this fragment into two. Which statements are correct?

A. Their offset fields are 100 and 125.
B. Both resulting fragments have MF=1.
C. Both retain the original datagram's identification value.
D. Their offsets must restart from zero because they were produced by a different router.

### Q16. [1 Mark] [NAT]

Procedure F(n) returns1 when n=0 and otherwise returns F(n−1)+F(n−1), making both calls without memoization. How many base-case invocations occur in F(5)?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

Two threads always acquire mutexes X and Y in the order X then Y, and release both after finite computation. No other resources or waits exist. Which statement is correct?

A. A cycle of these two threads each holding one of X,Y and waiting for the other is possible.
B. The common acquisition order excludes a circular wait involving these mutexes.
C. The order guarantees equal waiting times.
D. Deadlock freedom implies that neither thread can ever wait.

### Q18. [1 Mark] [NAT]

Five observations have mean 10 and population variance 8. Remove one observation; the remaining four have mean 11. What is their population variance?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A byte-addressed machine has 32-bit addresses and a direct-mapped cache with 4 KiB of data capacity and 32-byte lines. Each line stores a tag, a valid bit, and a dirty bit. No other metadata are counted. How many metadata bits are stored in total?

**Answer format:** Integer bits.

### Q20. [1 Mark] [MCQ]

Two control-unit designs implement the same instruction-set behaviour. One stores sequences of control words in a control memory; the other generates signals through fixed combinational/sequential logic. Which statement is correct?

A. The first is microprogrammed; changing its control words may change instruction sequencing without redesigning all control logic.
B. The first cannot contain any sequencing logic.
C. The second must fetch a microinstruction from control memory every cycle.
D. Both designs must expose the same internal control-word format to application programs.

### Q21. [1 Mark] [MCQ]

An open-addressed hash table of size 10 uses probes h(k,i)=(h₁(k)+4i) mod 10. A key has h₁(k)=1. Which statement is correct?

A. Its probe sequence visits all ten slots before repeating.
B. It visits exactly five slots, so insertion can fail while some slots remain empty.
C. It visits only slot 1.
D. Its sequence depends on the values stored in occupied slots.

### Q22. [1 Mark] [MSQ]

R(A,B,C) has functional dependencies A→B and B→C, and no others except their consequences. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless.  
B. The decomposition preserves the given dependencies.  
C. The original R is in BCNF.  
D. Both component schemas are in BCNF.

### Q23. [1 Mark] [NAT]

In the multiplicative group of units modulo 10, what is the order of the element 3?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Three processes have (arrival time, CPU burst length) A=(0,7), B=(2,4), C=(4,1), in time units. A single CPU uses preemptive shortest-remaining-time-first scheduling with zero switching overhead. No process performs I/O. Waiting time is completion time minus arrival time minus burst length. What is the average waiting time?

**Answer format:** Numeric value; integer.

### Q25. [1 Mark] [MCQ]

A machine enumerates all binary strings and runs an effective test that halts and accepts exactly on strings belonging to a decidable language L. It prints the accepted strings, one at a time. If L is finite, which statement follows?

A. The enumeration must automatically know when its last output has been printed.
B. Enumeration can continue forever after its last output without contradicting correctness.
C. L becomes undecidable because enumeration is infinite.
D. The empty language cannot be enumerated.

### Q26. [1 Mark] [NAT]

An integer array initially contains [1,2,3,4,5,6]. A memmove-style operation copies its first four elements into positions 2 through 5, using zero-based positions and preserving the original source values even where source and destination overlap. What value is at position 5 afterward?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A connected simple undirected graph has seven vertices and seven edges. Its unique cycle has length4. How many edges of the graph are bridges?

**Answer format:** Exact integer.

### Q28. [1 Mark] [NAT]

Two unsigned8-bit fixed-point values have four fractional bits and raw integer encodings24 and40. Their exact product is to be represented with four fractional bits. What raw integer encoding represents that product?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

Let f(n)=n log₂n and g(n)=n^(3/2), for integers n≥2. Which statements are true?

A. f is O(g).
B. g is O(f).
C. f is o(g).
D. f and g are Θ-equivalent.

### Q30. [1 Mark] [NAT]

A DFA tracks the input length modulo2 and the number of a symbols modulo2 over alphabet{a,b}. It starts with both parities even. How many of the four parity-pair states are reachable?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

A singly linked list is A→B→C→D→NULL. Pointer p initially refers to A and pointer q initially refers to C. Execute these assignments in order:

```text
p.next = q.next;
q.next = p;
```

How many distinct nodes are reachable by following next pointers starting from q, counting q itself?

**Answer format:** Exact integer.

### Q32. [1 Mark] [MCQ]

A disk scheduler always chooses a pending request closest to the current head, breaking ties by lower cylinder number. New requests can arrive indefinitely. A request far from the current head is pending. Which statement is correct without an arrival-rate bound?

A. The pending request must be served after at most the current queue length requests.  
B. An unending stream of nearer requests can postpone it indefinitely.  
C. Shortest seek distance guarantees fairness.  
D. Tie-breaking alone prevents starvation.

### Q33. [1 Mark] [NAT]

How many triples of nonnegative integers(x,y,z) satisfy x+y+z=8, x≤2, and y odd?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

Two IPv4 ranges are10.0.0.0/25 and10.0.0.64/26. How many distinct addresses belong to their union?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

How many permutations f of {1,2,3,4} satisfy f(f(x))=x for every x and have exactly two fixed points?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

A byte-addressed processor has address lines A15 through A0. A memory board uses four 4K×8 RAM chips to provide one contiguous 16 KiB region starting at address 0x8000. Each selected chip supplies one byte. Chip address pins use A11 through A0; a decoder chooses one chip. Assume the decoder is enabled exactly for addresses in the intended region. Which statements are correct?

A. A13 and A12 can select the chip, while A15=1 and A14=0 enable the board.  
B. Address 0xB123 selects chip index 3 (indices 0–3 in increasing address order) at local offset 0x123.  
C. If the board enable checks only A15=1 and ignores A14, each physical byte is mapped at two processor addresses.  
D. Connecting chip address pins to A12 through A1, while otherwise retaining the stated decoder, still gives one-to-one addressing of the 16 KiB region.

### Q37. [2 Marks] [NAT]

An initially free64-KiB region is managed by a binary buddy allocator. Each request is rounded up to the smallest power-of-two KiB block that fits it. Splitting always allocates the lowest-address available suitable descendant; free buddies coalesce immediately. Requests A=9KiB, B=9KiB, C=17KiB are allocated in that order. A is then freed. What is the size, in KiB, of the largest request that can now be satisfied without freeing B or C?

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

R is a binary relation on a finite nonempty domain. Use the following properties:

- E: for every x there exists y such that R(x,y).
- T: R is transitive.
- I: R is irreflexive.
- S: R is symmetric.
- F: for each x, at most one y satisfies R(x,y).

Which listed combinations admit a model on some finite nonempty domain? Properties not listed in an option impose no condition.

A. E, T, I  
B. E, S, I, F  
C. E, T, I, F  
D. E, T, S

### Q39. [2 Marks] [MSQ]

A binary floating-point format has finite precision. Ignore overflow and underflow, and assume its precision is at least four significant bits. Which real values can be represented exactly?

A. 3/8
B. 1/10
C. 7/4
D. 1/3

### Q40. [2 Marks] [NAT]

An unspanned fixed-record file uses 1000-byte blocks. Records are 120 bytes, and each block reserves a 40-byte header. How many blocks are needed for 81 records, with no compression and no record crossing a block boundary?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A process references pages A,B,C,A,D,B. There are three initially empty frames. A page fault loads the requested page, and the optimal offline replacement policy evicts the page whose next use is farthest in the future, treating no future use as infinity. How many fewer page faults does this policy incur than FIFO on this trace?

**Answer format:** Exact integer.

### Q42. [2 Marks] [MSQ]

For Boolean inputs x,y,z, a circuit outputs F=(x AND y) OR ((NOT x) AND z). Which statements hold?

A. Flipping x leaves F unchanged exactly when y=z.
B. F equals (x OR z) AND ((NOT x) OR y).
C. F is independent of z whenever y=1.
D. When y=NOT z, F XOR z equals x.

### Q43. [2 Marks] [NAT]

A NAT allocates one public source port per distinct internal (IP address, UDP source port) pair, reusing that mapping for all remote destinations. It never expires a mapping during this experiment. Client A uses source port 4000 to contact three different servers; client B uses source port 4000 to contact two servers; client A additionally uses source port 4001 to contact one server. A and B have different internal IP addresses. How many mappings exist afterward?

**Answer format:** Exact integer.

### Q44. [2 Marks] [NAT]

For a real parameter t, consider

```text
x + y + z = 1
x + t*y + z = 2
x + y + t*z = 2
```

For every t for which a unique solution exists, let s(t)=x+y+z of that solution. How many real values of t make the system inconsistent?

**Answer format:** Exact integer.

### Q45. [2 Marks] [MSQ]

For grammar S→SS | a | ε, which statements are true?

A. Its language is a*.
B. The word a has infinitely many distinct parse trees.
C. Every generated word has exactly one parse tree.
D. The grammar is LL(1) as written.

### Q46. [2 Marks] [NAT]

A TCP receiver's cumulative ACK is1000 and its advertised receive window is1200 bytes. A sender has already transmitted bytes1000 through1799 inclusive, none cumulatively acknowledged yet. Its congestion window is1500 bytes. Assume no window changes, losses, retransmissions or extra data already in flight. How many additional consecutive bytes may it send immediately under both limits?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

A PDA recognizing balanced parentheses pushes on '(' and pops on ')', rejecting a pop from an empty stack; it accepts only with empty stack after all input. A proposed modification accepts immediately whenever the stack first becomes empty after consuming at least one symbol, even if input remains. Which input demonstrates that the modification accepts a string rejected by the original?

A. (())
B. ()()
C. ())
D. ((

### Q48. [2 Marks] [NAT]

For x≠0, f(x)=(exp(x)−1−x)/x². Set f(0) to the value making f continuous at0. What is f'(0)?

**Answer format:** Decimal rounded to four places.

### Q49. [2 Marks] [NAT]

A stack stores integers using the following minimum-encoding scheme. The first push stores the value and sets m to it. To push x<m, store 2x−m and set m=x; otherwise store x. When popping a stored value y<m, return the old m and then set m=2m−y; otherwise return y and leave m unchanged. Arithmetic has unlimited precision. Starting empty, execute push(7), push(3), push(5), push(−2), pop(), pop(), push(1), pop(), pop(). What is the sum of the four returned values?

**Answer format:** Integer.

### Q50. [2 Marks] [MCQ]

A stack log uses symbol a for a push and b for a pop. A valid log starts with an empty stack, never pops an empty stack, and ends with an empty stack. Let L contain exactly the valid logs in which neither aaa nor bbb occurs as a substring; the empty log belongs to L. Which statement about L is correct?

A. L is regular because no run has more than two identical operations.  
B. L is not regular, but a deterministic pushdown automaton can recognize it.  
C. L is context-free, but no deterministic pushdown automaton can recognize it.  
D. L is not context-free because the run restriction and the stack restriction must both be checked.

### Q51. [2 Marks] [NAT]

Short-circuit intermediate code evaluates P AND (Q OR R) from left to right, skipping operands whose values cannot affect the result. P,Q,R are independent Boolean inputs, each true with probability 1/2. What is the expected number of input predicates evaluated?

**Answer format:** Decimal rounded to two places.

### Q52. [2 Marks] [NAT]

An initially empty B+ tree has leaves holding at most three keys and internal nodes holding at most three separator keys (four children). Insert keys 1 through 12 in increasing order. An overflowing leaf with four keys splits into two leaves of two keys. An overflowing internal node with five children splits into a left node of two children and a right node of three children; one separating key is promoted. A root split creates a new root. Count all leaves and internal nodes, including the root. How many nodes exist after all insertions?

**Answer format:** Integer.

### Q53. [2 Marks] [MCQ]

An ordinary file has two hard links and is open through one file descriptor. Both directory entries are unlinked, but the descriptor remains open. Under a file system that preserves unlinked files while open, which event permits reclaiming the file's storage, assuming no new references arise?

A. Removing only the first hard link.
B. Closing the final open descriptor after both links have been removed.
C. Reading the first byte through the descriptor.
D. Merely changing the current directory.

### Q54. [2 Marks] [MCQ]

A0/1 knapsack has capacity10 and items(weight,value)=(6,12),(5,9),(5,9), each available once. A heuristic scans items in decreasing value/weight order and takes an item whenever it fits. Which statement is correct?

A. The heuristic obtains12, while the optimum is18.
B. The heuristic obtains18, while the optimum is12.
C. Both obtain21 by splitting an item.
D. The heuristic cannot choose any item.

### Q55. [2 Marks] [MCQ]

A TCP server has a listening socket and accepts two connections, producing descriptors c1 and c2. It then closes only the listening socket. No shutdown is applied to c1 or c2. Which statement is correct?

A. Both accepted connections necessarily close immediately.
B. c1 and c2 remain usable; closing the listener does not itself close those connected sockets.
C. c1 becomes a new listening socket automatically.
D. The two clients must now share one TCP byte stream.

### Q56. [2 Marks] [NAT]

A recursive procedure on a list segment performs a postorder traversal: it first visits the left half, then the right half, then emits one marker. A segment of size 1 emits a marker and returns. For a segment of size n>1, the halves have sizes floor(n/2) and ceil(n/2). Starting with n=13, how many markers have been emitted immediately before the root invocation emits its marker?

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

A dead assignment is `x = read_device();`, and x is not subsequently used. The function read_device has an observable device effect. Which optimization is generally valid?

A. Delete both the call and assignment solely because x is dead.
B. Preserve the call's effect, although storing its unused return value in x may be eliminated.
C. Replace the call by an arbitrary constant and preserve all behaviour.
D. Execute the call twice to compensate for removing the store.

### Q58. [2 Marks] [MSQ]

R(A,B,C) has exactly the dependencies implied by A→B and BC→A. Decompose it into R1(A,B) and R2(A,C). Which statements are correct?

A. The decomposition is lossless under the stated dependencies.
B. Both components are in BCNF under their projected dependencies.
C. Enforcing only the projected dependencies on the components need not enforce BC→A on their join.
D. A is a candidate key of the original R.

### Q59. [2 Marks] [NAT]

Five jobs in fixed order have (cost,value) pairs (4,9),(2,7),(3,8),(3,10),(2,6). Select exactly two jobs, with no two adjacent in the order, and total cost at most seven. What is the maximum total value?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

The following code uses unbounded integers. The input y is arbitrary.

```text
if y > 0:
    x = 2
else:
    x = 2
if x == 2:
    z = 7
else:
    z = y
```

Which statements are correct about the values and constant-propagation opportunities?

A. z is always7.
B. y must equal2 after the first conditional.
C. A flow-sensitive constant-propagation analysis can establish x=2 at the join and remove the unreachable second else branch.
D. The two different predecessor blocks force x to be nonconstant at their join even when both assign2.

### Q61. [2 Marks] [MCQ]

For powers of two n≥4, a recurrence is T(n)=3T(n/2)+n²/log₂n, with positive constant base costs for n≤2. What is its asymptotic order?

A. Θ(n²)
B. Θ(n²/log n)
C. Θ(n^(log₂3) log n)
D. Θ(n² log log n)

### Q62. [2 Marks] [NAT]

Insert keys20,10,30,25,40,22,27 into an initially empty ordinary BST. Perform a single left rotation at root20: its right child30 becomes the root,20 becomes30's left child, and30's former left subtree becomes20's right subtree. How many keys have the same depth before and after the rotation, counting the root's depth as0?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

Independent fair-coin tosses continue until the first head. Let N be the number of tosses, including the head. Given that N is odd, what is E[N]? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q64. [2 Marks] [NAT]

A cache miss adds 40 cycles to a base execution of one cycle per instruction. An optimization reduces misses per instruction from 0.04 to 0.01 but increases the instruction count by 20%. Clock period is unchanged and no penalties overlap. What is the ratio of old execution time to new execution time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q65. [2 Marks] [MSQ]

A Karnaugh-map group fixes variable a=1 and c=0 while leaving b and d free. Which statements are correct?

A. The group represents product a(NOT c).
B. It covers four minterms.
C. Its product must include b and d because they vary.
D. It can legally include specified zero cells in an exact SOP implementation without don't-cares.

---

## ANSWER KEY — MOCK TEST 084

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C |
| 2 | MCQ | 1 | B |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 60 |
| 5 | MCQ | 1 | C |
| 6 | MCQ | 2 | C |
| 7 | MCQ | 2 | D |
| 8 | NAT | 2 | 48 |
| 9 | NAT | 2 | 2.5 |
| 10 | NAT | 2 | 16.8284 (accepted range 16.82835–16.82845) |
| 11 | MCQ | 1 | C |
| 12 | MCQ | 1 | D |
| 13 | NAT | 1 | 4 |
| 14 | MSQ | 1 | A, B |
| 15 | MSQ | 1 | A, B, C |
| 16 | NAT | 1 | 32 |
| 17 | MCQ | 1 | B |
| 18 | NAT | 1 | 5 (exact) |
| 19 | NAT | 1 | 2816 |
| 20 | MCQ | 1 | A |
| 21 | MCQ | 1 | B |
| 22 | MSQ | 1 | A, B, D |
| 23 | NAT | 1 | 4 |
| 24 | NAT | 1 | 2 (exact) |
| 25 | MCQ | 1 | B |
| 26 | NAT | 1 | 4 |
| 27 | NAT | 1 | 3 |
| 28 | NAT | 1 | 60 |
| 29 | MSQ | 1 | A, C |
| 30 | NAT | 1 | 4 |
| 31 | NAT | 1 | 3 |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 11 |
| 34 | NAT | 1 | 128 |
| 35 | NAT | 1 | 6 |
| 36 | MSQ | 2 | A, B, C |
| 37 | NAT | 2 | 16 |
| 38 | MSQ | 2 | B, D |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 11 |
| 41 | NAT | 2 | 0 |
| 42 | MSQ | 2 | A, B, D |
| 43 | NAT | 2 | 3 |
| 44 | NAT | 2 | 1 |
| 45 | MSQ | 2 | A, B |
| 46 | NAT | 2 | 400 |
| 47 | MCQ | 2 | C |
| 48 | NAT | 2 | 0.1667 (accepted range 0.16665–0.16675) |
| 49 | NAT | 2 | 7 |
| 50 | MCQ | 2 | B |
| 51 | NAT | 2 | 1.75 (two decimals) |
| 52 | NAT | 2 | 9 |
| 53 | MCQ | 2 | B |
| 54 | MCQ | 2 | A |
| 55 | MCQ | 2 | B |
| 56 | NAT | 2 | 24 |
| 57 | MCQ | 2 | B |
| 58 | MSQ | 2 | A, B, C |
| 59 | NAT | 2 | 19 |
| 60 | MSQ | 2 | A, C |
| 61 | MCQ | 2 | B |
| 62 | NAT | 2 | 3 |
| 63 | NAT | 2 | 1.6667 (accepted range 1.66665–1.66675) |
| 64 | NAT | 2 | 1.5476 (range 1.54755–1.54765) |
| 65 | MSQ | 2 | A, B |
