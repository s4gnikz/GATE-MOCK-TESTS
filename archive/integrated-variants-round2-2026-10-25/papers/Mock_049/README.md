# GATE CS 2027 — Full-Length Mock Test 049

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

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sentence unambiguously states that Meera checked the figures before submitting the report?

A. Before submitting the report, the figures were checked by Meera.  
B. Before Meera submitted the report, she checked the figures.  
C. The figures submitted the report after Meera checked them.  
D. Having been submitted, Meera checked the report's figures.

### Q2. [1 Mark] [NAT]

Two tanks initially contain equal volumes of liquid. Tank A contains20% salt and tank B contains40% salt, measured by mass; both liquids have the same density, and mixing preserves total mass. One-quarter of A's original liquid is poured into B and mixed. Then the same mass of the resulting mixture is returned to A. What is A's final salt percentage?

**Answer format:** Percentage as a number, without the percent symbol.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rule says, “A consignment will be released only if it is inspected, unless it is exempt.” Which situation necessarily violates the rule?

A. An exempt consignment is released without inspection.  
B. A nonexempt consignment is inspected but not released.  
C. A nonexempt consignment is released without inspection.  
D. An exempt consignment is inspected before release.

### Q4. [1 Mark] [MCQ]

A planar figure is reflected across the x-axis and then across the line y=x. Which coordinate rule describes the combined transformation?

A. (x,y)→(−y,x)
B. (x,y)→(y,−x)
C. (x,y)→(−x,−y)
D. (x,y)→(x,−y)

### Q5. [1 Mark] [MCQ]

A report states: “Every village whose water supply was tested met the safety standard. Some villages could not be reached during the survey.” Which conclusion is justified by these statements alone?

A. Every village met the safety standard.
B. At least one untested village failed the standard.
C. No tested village failed the standard.
D. The untested villages had safer water than the tested villages.

### Q6. [2 Marks] [NAT]

Three distinct integers are chosen uniformly from {1,…,8}. What is the expected value of the smallest chosen integer?

**Answer format:** Exact finite decimal.

### Q7. [2 Marks] [NAT]

An organizer may buy any nonnegative integer number of two advertising packages. Each A package costs40 and brings exactly10 registrations. Each B package costs60 and brings exactly12 registrations. With a budget of300, what is the maximum number of registrations obtainable?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

A square sheet occupies 0≤x≤8, 0≤y≤8. Fold the right half onto the left along x=4, then the top half onto the bottom along y=4. Punch one tiny circular hole centred at (4,1), and another centred at (2,2), through every layer. The radii are equal and less than 0.1; the first punch straddles the vertical folded edge. After unfolding completely, how many distinct circular holes are present? Count a hole centred on a former fold line once.

**Answer format:** Exact integer.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A survey includes 120 people. Seventy read newspaper A, sixty read newspaper B, and twenty read neither. Among those who read at least one, what fraction read exactly one?

A. 3/10  
B. 7/10  
C. 3/4  
D. 5/6

### Q10. [2 Marks] [NAT]

A three-question quiz has four options per question and exactly one correct option each. A student independently guesses uniformly on every question. Each correct answer scores 3 and each wrong answer scores −1. Given that the student's total score is positive, what is the probability that exactly two answers were correct? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A DFA has states0,1,2,3, start state0 and only accepting state0. On symbol a it moves from state i to(i+1) mod4; on symbol b it moves to(i+2) mod4. How many length-three strings over {a,b} are accepted?

**Answer format:** Exact integer.

### Q12. [1 Mark] [NAT]

A cache contains exactly one four-word line, initially invalid. It uses write-back and write-allocate. A word-store miss fetches the entire target line before updating the word; evicting a dirty line writes the entire line to memory. The accesses are store to block 0, store to block 1, load from block 0. Each access is to one word, blocks 0 and 1 differ, and there is no final cache flush. How many complete cache-line transfers between memory and cache occur, counting reads and write-backs?

**Answer format:** Integer.

### Q13. [1 Mark] [MCQ]

A language passes a scalar argument by value. A callee assigns a new scalar value to its parameter but does not access the caller's storage through any pointer or reference. Which statement is correct?

A. The assignment necessarily changes the caller's variable.
B. The assignment changes the callee's parameter value without thereby changing the caller's scalar variable.
C. Pass-by-value means the parameter cannot be assigned.
D. Pass-by-value requires the caller and callee to share one parameter storage cell.

### Q14. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

On a nonempty domain, P and Q are unary predicates. Which implications are valid for every interpretation?

**Candidates**

**I.** (∀x P(x)) OR (∀x Q(x)) implies ∀x(P(x) OR Q(x)).

**II.** ∀x(P(x) OR Q(x)) implies (∀x P(x)) OR (∀x Q(x)).

**III.** ∃x(P(x) AND Q(x)) implies (∃x P(x)) AND (∃x Q(x)).

**IV.** (∃x P(x)) AND (∃x Q(x)) implies ∃x(P(x) AND Q(x)).

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For positive integers n, let f(n)=n if n is even and f(n)=n² if n is odd. Which asymptotic statement holds?

A. f(n)=Theta(n).  
B. f(n)=Theta(n²).  
C. f(n)=Omega(n²).  
D. f(n)=O(n²) and f(n)=Omega(n), but neither A nor B holds.

### Q16. [1 Mark] [NAT]

A3×3 matrix A has determinant5. Matrix B is obtained by interchanging A's first and third rows and then multiplying its second column by−2. What is det(B)?

**Answer format:** Exact number.

### Q17. [1 Mark] [NAT]

The grammar has start symbol S and productions S→aSbb | T and T→bTa | epsilon. How many distinct terminal strings of length6 does it generate?

**Answer format:** Exact integer.

### Q18. [1 Mark] [MSQ]

Relation R(A,B,C,D) has dependencies A→B, AB→C, C→D, A→D. Which statements hold?

A. B is extraneous in the left side of AB→C.
B. A→D can be removed without changing the set of implied dependencies.
C. C→D can be removed without changing the set of implied dependencies.
D. A is a candidate key.

### Q19. [1 Mark] [MCQ]

A change-making algorithm repeatedly takes the largest coin not exceeding the remaining amount. Coin denominations are1,4,6 with unlimited supplies. For amount8, which statement is correct?

A. Greedy uses two coins and is optimal.
B. Greedy uses three coins, while the optimum uses two.
C. Greedy uses four coins, while the optimum uses three.
D. No exact representation of8 exists.

### Q20. [1 Mark] [NAT]

A singly linked structure has successor sequence 0→1→2→3→4→5→3→4→5→… . Floyd's algorithm starts both pointers at node 0. In each iteration the slow pointer advances once and the fast pointer advances twice, then equality is tested. At which node do they first meet?

**Answer format:** Integer node label.

### Q21. [1 Mark] [NAT]

A block contains four data bits followed by one even-parity bit. Exactly one of the five transmitted bits is flipped. How many different one-bit error patterns are undetected by the parity check?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

An unlimited supply of coins of denominations 1 and 3 is used to make amount 5. If order matters, how many sequences of coins have total value 5?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

An index lookup requires exactly three distinct index-page reads and returns matching record locations on data pages 4,4,7,9,7. Data and index pages are disjoint. Initially no page is cached; every page read remains cached throughout the query. How many page reads are required in total?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

For x≠0, define f(x)=(|x|−x)/x, and set f(0)=k. Which statement holds?

A. k=0 makes f continuous at 0.
B. k=−2 makes f differentiable at 0.
C. No real k makes f continuous at 0.
D. Every real k makes f continuous at 0.

### Q25. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An eight-bit pattern is interpreted either as sign-magnitude or as two's complement. Which statements are correct?

A. 10000000 denotes zero in sign-magnitude.  
B. 10000000 denotes −128 in two's complement.  
C. Both representations assign the same value to every pattern with leading bit 1.  
D. Both assign the same value to every pattern with leading bit 0.

### Q26. [1 Mark] [NAT]

Two independent fair dice give values X,Y. Find E[X | X+Y=7 and X>Y].

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A disk has cylinders 0 through 99. At time 0, its head is at cylinder 50, moving toward larger numbers, with requests pending at 70, 90 and 10. Seek speed is one cylinder per time unit; service and reversal take zero time. A new request for cylinder 95 arrives at time 45. LOOK continues in its current direction while any request is pending ahead, and otherwise reverses. New arrivals join the queue without causing an early reversal. What total head movement serves all four requests?

**Answer format:** Numeric value; integer.

### Q28. [1 Mark] [MSQ]

A segment has byte offsets 0 through 5999. It is paged using 4096-byte pages, with both required pages present. Segment bounds are checked independently of page presence. Which statements are correct?

A. Offset 5000 is valid and uses page 1 with offset 904.  
B. Offset 7000 is valid because page 1 is present.  
C. Offset 5999 is the last valid byte.  
D. Allocating the second page automatically enlarges the segment to 8192 bytes.

### Q29. [1 Mark] [NAT]

Three Ethernet stations independently select uniformly from {0,1,2,3} as their backoff counters for one contention attempt. What is the probability that exactly one station selects the smallest counter?

**Answer format:** Exact finite decimal.

### Q30. [1 Mark] [MCQ]

Three-address code evaluates `(a+b)*(a+b)` with exact scalar arithmetic and unchanged operands. Which sequence computes it using only two arithmetic operations?

A. t=a+b; r=t*t
B. t=a*b; r=t+t
C. t=a+a; r=t*b
D. t=a+b; r=t+b

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean variables x, y and z, let F=(x OR y) AND ((NOT x) OR z). Which expression is equivalent to F for every input?

A. (x AND z) OR ((NOT x) AND y)  
B. (x AND y) OR ((NOT x) AND z)  
C. y OR z  
D. x XOR y XOR z

### Q32. [1 Mark] [MCQ]

A queue is implemented with two stacks. Enqueue pushes onto stack I. Dequeue pops stack O if nonempty; otherwise it moves all of I to O by repeated pops and pushes, then pops O. Which statement is correct for a sequence starting with both stacks empty?

A. Each element can move from I to O at most once before removal.
B. Every dequeue performs a constant number of stack operations in the worst case.
C. Moving I to O reverses FIFO order incorrectly.
D. Every enqueue must first empty O.

### Q33. [1 Mark] [NAT]

A four-variable Boolean function is1 exactly when the two least significant input bits are equal; the two other bits are unrestricted. In a minimum sum-of-products representation without don't-cares, what is the total number of literal occurrences?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

Let g permute {1,2,3} cyclically: g(1)=2, g(2)=3, g(3)=1. How many functions f:{1,2,3}→{1,2,3} satisfy f(g(x))=g(f(x)) for every x?

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DMA device writes a buffer in main memory. The CPU has an old, clean copy of that buffer in a non-coherent write-back cache. The DMA completion interrupt has arrived. Which action is sufficient to make a subsequent CPU read obtain the DMA result, assuming no concurrent writes?

A. Write back the old clean cache line without invalidating it.  
B. Invalidate the cached buffer lines before reading.  
C. Disable interrupts after the completion interrupt.  
D. Read the buffer repeatedly until its value changes.

### Q36. [2 Marks] [NAT]

A recursive procedure on a sorted array of length64 splits every non-singleton interval into two equal halves. It processes both children, then compares the last element of the left half with the first element of the right half. If they are already in nondecreasing order, it skips merging entirely. Otherwise it would merge, but this never occurs on the given sorted input. How many key comparisons are performed in total, including only the stated boundary tests?

**Answer format:** Integer.

### Q37. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let A=[[2,1],[0,2]]. Which statements are correct?

**Candidates**

**I.** A has two linearly independent eigenvectors over the real numbers.

**II.** A⁵ has diagonal entries32 and32.

**III.** A⁵−32I has rank1.

**IV.** A⁵=32I.

A. II and III  
B. I and II  
C. I and III  
D. I and IV

### Q38. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A dead assignment is `x = read_device();`, and x is not subsequently used. The function read_device has an observable device effect. Which optimization is generally valid?

A. Delete both the call and assignment solely because x is dead.  
B. Preserve the call's effect, although storing its unused return value in x may be eliminated.  
C. Replace the call by an arbitrary constant and preserve all behaviour.  
D. Execute the call twice to compensate for removing the store.

### Q39. [2 Marks] [MSQ]

Two threads share ordinary Boolean flags f0=f1=false. Under sequential consistency, thread i sets fi=true, then busy-waits while the other flag is true, enters its critical section, and finally sets fi=false. Reads and writes of each flag are atomic. Which statements are correct?

A. Both threads can be stuck waiting forever even if both are scheduled fairly.
B. Both threads can be simultaneously in their critical sections.
C. Mutual exclusion holds.
D. Replacing the flags with volatile flags alone necessarily prevents the waiting failure.

### Q40. [2 Marks] [NAT]

A processor can issue one instruction per cycle. A loop has 100 instructions, including ten branches. Exactly three of the branches mispredict, each inserting four cycles with no issue. Each of eight cache misses adds five stall cycles, but two of those misses occur entirely during branch-stall intervals and add no extra cycles. All other penalties are disjoint. Ignoring pipeline fill/drain, how many cycles does the loop take?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

An undirected network has edges AB=2, AC=7, BC=1, BD=6, CD=2. Node A's link-state database is complete and correct. The edge BC fails and is removed. By how much does the shortest-path distance from A to D increase after recomputation?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A stack machine stores four-byte integers. PUSH first subtracts4 from SP, then writes at the new SP. POP reads at SP, then adds4 to SP. Initially SP=100. Execute PUSH7, PUSH9, POP into R, then store R at address SP+4, then POP into S. What is R+S? The stack is ordinary writable memory and all addresses are valid.

**Answer format:** Integer.

### Q43. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A function f is continuously differentiable on [0,1], with f(0)=0, f(1/2)=2 and f(1)=1. Which statements must hold?

A. f′ equals 4 somewhere in (0,1/2).  
B. f′ is positive throughout (0,1).  
C. f′ equals −2 somewhere in (1/2,1).  
D. f′ equals zero somewhere in (0,1).

### Q44. [2 Marks] [MSQ]

Consider the following code. Each call to more() returns an arbitrary Boolean value and does not change x. Consider only terminating executions. A conventional constant-propagation analysis tracks a single constant per variable or “not constant”; it joins distinct incoming constants as “not constant” and computes a fixed point over the loop.

```text
x = 1
while more():
    x = 2
y = x
```

Which statements are correct?

A. At the loop header, this analysis establishes x=1 at its fixed point.  
B. Immediately after the body assignment, this analysis establishes x=2.  
C. On every terminating execution, the final y is 2.  
D. Replacing the while loop with a do-while loop executing x=2 before its first call to more() removes final value y=1 from the possible outcomes.

### Q45. [2 Marks] [NAT]

A compiler represents a basic block as a DAG and merges identical pure expressions whose operand values are unchanged. Consider exact integers with distinct scalar variables and no aliases:

```text
t1 = a+b
t2 = a+b
a = t1+c
t3 = a+b
t4 = t2+c
```

How many distinct addition nodes are needed, including the value assigned to a?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A prime-implicant chart requires columns1,2,3,4,5. Rows A,B,C,D cover respectively{1,2},{2,3},{3,4,5},{1,4,5}, with literal costs2,2,3,3. Only these rows are available. How many distinct minimum-total-cost covers exist?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the following complete read/write schedule; commits occur afterwards and are omitted. Subscripts identify transactions. Repeated writes by one transaction are distinct operations. The read returns the value written by the latest preceding write.

```text
w1(x); w2(x); w3(y); w2(y); r4(x); w4(y); w1(x)
```

A view-equivalent serial schedule must preserve the transaction from which every read obtains its value, any reads of initial values, and the final writer of each item. A serial order includes all four transactions, preserving each transaction's internal operation order. Which statements are correct?

A. The displayed schedule is conflict-serializable.  
B. The displayed schedule is view-serializable.  
C. Exactly two transaction orders give view-equivalent serial schedules.  
D. If only the first operation w1(x) is deleted, the resulting schedule has exactly one conflict-equivalent serial transaction order.

### Q48. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A component is faulty with probability 1/4. Each test is positive with probability 4/5 for a faulty component and 1/10 for a sound component. Repeated results are conditionally independent given the component's status. Testing stops at the first negative result or after three tests, whichever occurs first. N is the number of tests performed. Which statements are correct?

A. E[N]=577/400.  
B. P(faulty | N=3)=512/515.  
C. Given that exactly two positive results were observed before a negative result, the probability of a faulty component is 128/155.  
D. Given that the first result was positive and the stopping result was negative, the probability of a faulty component is 32/65.

### Q49. [2 Marks] [MCQ]

A router uses longest-prefix matching with routes 10.0.0.0/8→A, 10.1.0.0/16→B, 10.1.128.0/17→C, and 10.1.192.0/18→D. Only the /17 route is withdrawn. Which next hops are then used for 10.1.160.1 and 10.1.200.1, respectively?

A. (A,A)  
B. (C,D)  
C. (B,B)  
D. (B,D)

### Q50. [2 Marks] [MSQ]

An 8-bit ALU performs subtraction x−y as x+(NOT y)+1 and retains only the low eight result bits. C is the carry out of bit 7; V indicates signed two's-complement overflow. For x=0x80 and y=0x01, which statements hold?

A. The retained result is 0x7F.
B. C=0, indicating an unsigned borrow.
C. V=1.
D. The signed mathematical result is representable in eight bits.

### Q51. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A proposed PDA for L={a^n b^n : n≥0} pushes for every a and pops for every b, rejects an attempted pop from empty, and accepts at end exactly when the stack is empty. It has no state recording whether b's have begun, so it allows pushing after popping. Which statements are correct?

**Candidates**

**I.** It accepts abab, which is outside L.

**II.** Adding a phase distinction that forbids a after the first b can repair the order constraint.

**III.** Its empty-stack condition alone guarantees all a's precede all b's.

**IV.** It rejects aabb.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q52. [2 Marks] [MCQ]

A binary tree is height-balanced if the heights of the two child subtrees at every node differ by at most one. An empty subtree has height −1 and a leaf height zero. Among such trees of height five, choose one with the minimum possible number of nodes. Which pair gives its number of nodes and its number of leaves?

A. (31,16)
B. (20,8)
C. (12,5)
D. (20,10)

### Q53. [2 Marks] [MCQ]

Transactions have timestamps T1=10,T2=20,T3=30, with lower meaning older. A wait-die lock manager lets an older requester wait for a younger holder but aborts a younger requester asking for an older holder's lock. T2 holds X, T3 requests X, then T1 requests X. What happens to these two requests, assuming T2 still holds X?

A. Both requesters wait.
B. T3 aborts and T1 waits.
C. T3 waits and T1 aborts.
D. Both requesters abort.

### Q54. [2 Marks] [NAT]

A sparse file uses 4096-byte blocks and four-byte pointers. Its inode has eight direct pointers, one single-indirect pointer and one double-indirect pointer. Logical block numbers start at zero. Starting with no allocated data or indirect blocks, one byte is written in logical block 1032, then one byte in logical block 2061. Only necessary data and pointer blocks are allocated; holes consume no blocks, and the existing inode is not counted. How many blocks have been allocated after both writes?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A variable x is live after statement `x = y+z`. Which statement describes the liveness transfer across this assignment, ignoring other live variables?

A. Old x must remain live before the statement solely because new x is live after it.  
B. Old x is killed by the assignment, while y and z are used and become live before it.  
C. y and z are killed because they appear on the right-hand side.  
D. The statement cannot define x because x is already live.

### Q56. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 4-to-1 multiplexer has select bits s1,s0 and data inputs D0=0,D1=x,D2=x′,D3=1. For which select settings is its output independent of x?

A. Only 00.  
B. Only 11.  
C. 00 and 11.  
D. 01 and 10.

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C,D) has FDs A→B, B→C, C→D. Which decomposition is both lossless and dependency preserving?

A. AB, BC, CD  
B. AB, CD  
C. AC, BD  
D. AD, BC

### Q58. [2 Marks] [MSQ]

A directed graph has edges a→b,b→c,c→a,c→d,d→e,e→d,e→f. Which statements are correct?

A. c and d are in the same strongly connected component.
B. Adding the edge f→b makes the entire graph strongly connected.
C. Reversing every edge preserves the partition into strongly connected components.
D. In the original graph, f can reach a.

### Q59. [2 Marks] [MSQ]

Let h be a homomorphism that maps each symbol of a finite alphabet to a finite string, possibly ε. Which statements are correct?

A. The image under h of a regular language is regular.
B. The image under h of a context-free language is context-free.
C. A nonregular language must remain nonregular under every such h.
D. Erasing every symbol maps every nonempty language to{ε}.

### Q60. [2 Marks] [MCQ]

In a binary tree with distinct keys, each node has a parent pointer. Given a pointer to x, an algorithm finds the next node in preorder traversal: if x has a left child, return it; otherwise, if x has a right child, return it; otherwise ascend. During ascent, when the current node is a left child and its parent has a right child, return that right child; if the root is passed, return NULL. What is the total time for starting at the root and repeatedly applying this algorithm until NULL, for a tree of n nodes?

A. Θ(log n) for every tree
B. Θ(n)
C. Θ(n log n) for every tree
D. Θ(n²) for a path-shaped tree

### Q61. [2 Marks] [MCQ]

Let L={a^(n²):n≥0}. For an assumed pumping length p≥1, choose z=a^(p²) and consider any valid regular-pumping decomposition z=uvw with1≤|v|≤p. Which argument correctly shows that pumping v twice leaves L?

A. The new length p²+|v| lies strictly between p² and(p+1)².
B. The new length must be a prime number.
C. The new length is always(p+1)².
D. The new length is smaller than p².

### Q62. [2 Marks] [NAT]

A synchronous three-bit register has next state(a,b,c)→(b,c,NOT a). It starts at000. Its output is1 exactly when the current state has two1 bits. Count output1 states among the first twelve states observed, including the initial state as observation1.

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A poset consists of pairs (i,j), where i∈{1,2} and j∈{1,2,3}, with (i,j)≤(k,l) iff i≤k and j≤l. How many downward-closed subsets does it have, including the empty set? A subset is downward-closed when containing an element implies containing every smaller element.

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A connected weighted graph has exactly five edges forming a five-vertex cycle with successive edge weights 2,7,3,6,4. What is the additional cost of a minimum-weight spanning tree constrained to include the weight-7 edge, compared with an unconstrained MST?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A process has descriptor3 for an open file. It calls dup(3), obtaining descriptor4. It then sets the close-on-exec flag on descriptor3 only and successfully executes a new program. No other descriptor refers to this open-file description. How many descriptors in the new program refer to it?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 049

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C, D |
| 2 | NAT | 1 | 24 |
| 3 | MSQ | 1 | A, B, D |
| 4 | MCQ | 1 | A |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 2.25 |
| 7 | NAT | 2 | 72 |
| 8 | NAT | 2 | 6 |
| 9 | MSQ | 2 | A, C, D |
| 10 | NAT | 2 | 0.2432 (range 0.24315–0.24325) |
| 11 | NAT | 1 | 3 |
| 12 | NAT | 1 | 5 |
| 13 | MCQ | 1 | B |
| 14 | MCQ | 1 | C |
| 15 | MSQ | 1 | A, B, C |
| 16 | NAT | 1 | 10 |
| 17 | NAT | 1 | 2 |
| 18 | MSQ | 1 | A, B, D |
| 19 | MCQ | 1 | B |
| 20 | NAT | 1 | 3 |
| 21 | NAT | 1 | 0 |
| 22 | NAT | 1 | 4 |
| 23 | NAT | 1 | 6 (exact) |
| 24 | MCQ | 1 | C |
| 25 | MCQ | 1 | C |
| 26 | NAT | 1 | 5 |
| 27 | NAT | 1 | 205 (exact) |
| 28 | MSQ | 1 | A, C |
| 29 | NAT | 1 | 0.65625 |
| 30 | MCQ | 1 | A |
| 31 | MSQ | 1 | B, C, D |
| 32 | MCQ | 1 | A |
| 33 | NAT | 1 | 4 |
| 34 | NAT | 1 | 3 (exact) |
| 35 | MSQ | 1 | A, C, D |
| 36 | NAT | 2 | 63 |
| 37 | MCQ | 2 | A |
| 38 | MSQ | 2 | A, C, D |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 142 |
| 41 | NAT | 2 | 3 |
| 42 | NAT | 2 | 16 |
| 43 | MCQ | 2 | B |
| 44 | MSQ | 2 | B, D |
| 45 | NAT | 2 | 3 |
| 46 | NAT | 2 | 2 |
| 47 | MCQ | 2 | A |
| 48 | MCQ | 2 | B |
| 49 | MCQ | 2 | D |
| 50 | MSQ | 2 | A, C |
| 51 | MCQ | 2 | C |
| 52 | MCQ | 2 | B |
| 53 | MCQ | 2 | B |
| 54 | NAT | 2 | 5 |
| 55 | MSQ | 2 | A, C, D |
| 56 | MSQ | 2 | A, B, D |
| 57 | MSQ | 2 | B, C, D |
| 58 | MSQ | 2 | B, C |
| 59 | MSQ | 2 | A, B, D |
| 60 | MCQ | 2 | B |
| 61 | MCQ | 2 | A |
| 62 | NAT | 2 | 4 |
| 63 | NAT | 2 | 10 |
| 64 | NAT | 2 | 1 |
| 65 | NAT | 2 | 1 |
