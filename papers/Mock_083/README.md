# GATE CS 2027 — Full-Length Mock Test 083

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

A report states: “Giving buses priority reduced average passenger delay on the studied corridor, although average car travel time increased. The study did not measure adjacent roads.” Which conclusion is supported?

A. Every traveller's journey became faster.
B. Adjacent roads necessarily became less congested.
C. The reported average passenger benefit can coexist with an increase in average car travel time.
D. Bus priority always reduces delay on every corridor.

### Q2. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Five distinct books are arranged on a shelf. Two specified books must have exactly one book between them. How many arrangements satisfy this condition?

**Required precision:** Integer.

A. 72  
B. 18  
C. 37  
D. 36

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The new procedure reduced measurement variability but did not change the mean measurement.” Which conclusion is supported?

A. Every new measurement equals the old mean.  
B. New measurements are less dispersed under the reported variability measure.  
C. The mean measurement became zero.  
D. The old procedure must have been biased.

### Q4. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A point initially at (2,0) is reflected first across the line y=x and then across the line x=1. What are its final coordinates?

A. (2,2)  
B. (0,0)  
C. (0,2)  
D. (2,−2)

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange these sentences into the most coherent chronological paragraph, using the references “that inspection” and “second inspection” consistently.

P. This second inspection found no leak.  
Q. The crew replaced the cracked valve and inspected the pipe again.  
R. A pressure drop first prompted an inspection.  
S. That inspection identified a crack in the valve.

A. R,Q,S,P  
B. S,R,Q,P  
C. R,S,Q,P  
D. Q,P,R,S

### Q6. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A fair coin selects one of two bags. Bag I contains 4 red and 2 blue balls; Bag II contains 2 red and 3 blue balls. Two balls are then drawn uniformly without replacement from the selected bag. Given that the two balls have the same colour, what is the probability that both are red?

**Candidate answers**
I. 1/2
II. 15/26
III. 7/13
IV. 3/5

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The agreement is provisional, not irrevocable; either side may withdraw before the inspection, but neither may withdraw afterward.” Which statement follows?

A. The agreement never binds either side.  
B. Withdrawal is permitted after inspection if both sides remain provisional.  
C. The right to withdraw exists before inspection and ends afterward.  
D. Inspection automatically cancels the agreement.

### Q8. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

How many distinct positive integers N≤72 can be written as N=2^a·3^b with nonnegative integers a,b and are divisible by6?

**Required precision:** Integer.

A. 16  
B. 4  
C. 8  
D. 9

### Q9. [2 Marks] [MCQ]

A three-letter code is formed by reversing the word, then advancing the first letter by one, the second by two and the third by three positions in the cyclic English alphabet. The same procedure is applied twice to CAT. What is the final code?

A. UCE
B. ECV
C. FEX
D. DBU

### Q10. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Four unit cubes occupy grid positions (0,0,0), (1,0,0), (1,1,0), and (1,1,1). A position (i,j,k) denotes the cube [i,i+1]×[j,j+1]×[k,k+1]. What is the total exposed surface area of their union, in square units? Shared full faces are internal; contact along an edge does not hide any face area.

**Required precision:** Exact integer.

A. 36  
B. 18  
C. 9  
D. 19

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A schedule has operations r1(x),r2(x),w1(x),w2(x), followed by commits. How many directed edges are in its precedence graph, counting each ordered pair of distinct transactions at most once?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q12. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An inode has one direct pointer and one pointer to a single-indirect block. Blocks contain 1024 bytes and pointers contain 4 bytes. A previously empty file is extended by writing one byte at byte offset 3072, with offsets starting at zero. The file system supports holes and allocates only necessary data and indirect blocks. Excluding the inode, how many blocks are newly allocated?

**Required precision:** Exact integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q13. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A byte-addressed system maps four 4 KiB×8 memory chips consecutively to addresses 0x8000–0xBFFF. Chips are numbered 0 through 3 in increasing base-address order. Which pair gives the chip number and the offset within that chip for address 0x9ABC?

**Candidate answers**
I. (0,0x9ABC)
II. (2,0xABC)
III. (1,0x1ABC)
IV. (1,0xABC)

A. I: valid; II: invalid; III: invalid; IV: valid  
B. I: invalid; II: invalid; III: valid; IV: valid  
C. I: valid; II: valid; III: valid; IV: invalid  
D. I: invalid; II: invalid; III: invalid; IV: valid

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Evaluate the limit as x→0 of (eˣ−1−x)/x².

**Required precision:** Exact finite decimal.

A. 0.3  
B. 0.8  
C. 0.1  
D. 0.5

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Over {a,b}, consider the regular expression a*(ba*)*. How many different words of length four belong to its language?

**Required precision:** Exact integer.

A. 32  
B. 8  
C. 17  
D. 16

### Q16. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A network-layer packet is carried through two links with different link-layer protocols. No tunnelling or address translation is used. Which statements are correct?

**Candidates**

**I.** The outgoing link can use a different frame format from the incoming link.

**II.** A router must preserve the incoming link-layer checksum unchanged in the outgoing frame.

**III.** Link-specific headers may be removed and replaced while forwarding the packet.

**IV.** Changing link-layer protocol necessarily changes the application's message content.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q17. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Consider ordinary integer variables with no overflow or side effects:

```text
x = a * 0
y = x + b
x = 7
return y
```

Which replacement computes the same returned value for all inputs?

**Candidate answers**
I. return 7+b
II. return a+b
III. return b
IV. return 0

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q18. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In ordinary constant propagation, one predecessor of block B assigns x=4 and another assigns x=7. Both paths are feasible. No assignment to x occurs at B before its first use. What can be concluded at entry to B?

**Candidate answers**
I. x is the constant 4.
II. x is the constant 7.
III. x is not a single known constant at this merge.
IV. x is uninitialized on both paths.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q19. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

X takes values−2 and2 with equal probability. Let Y=X². What is Var(Y)?

**Required precision:** Exact number.

A. 0  
B. 1  
C. 2  
D. 3

### Q20. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

The only use of scalar x after this fragment is return x. Variables are ordinary integers and expressions have no side effects.

```text
x = a + b
x = c + d
return x
```

Which statements are correct?

**Candidate answers**
I. The first assignment's computed value is dead.
II. The first assignment can be removed under the stated assumptions.
III. Both assigned values are simultaneously live before return.
IV. The second assignment is dead because x was previously assigned.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: invalid  
D. I: invalid; II: invalid; III: valid; IV: valid

### Q21. [1 Mark] [MSQ]

Functions f:A→B and g:B→A satisfy g composed with f=identity on A. No finiteness assumption is made. Which statements necessarily hold?

A. f is injective.
B. f is surjective onto B.
C. g is surjective onto A.
D. f composed with g=identity on B.

### Q22. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A real 6×6 matrix A satisfies A²=0. What is the largest possible rank of A?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An ordinary IPv4 subnet is 192.168.1.96/27, with its all-zero and all-one host fields reserved for network and broadcast addresses. Which is the highest assignable host address?

A. 192.168.1.127  
B. 192.168.1.126  
C. 192.168.1.128  
D. 192.168.1.125

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean variables x,y,z, let F=(x AND y) OR ((NOT x) AND z). When y=z, which expression always equals F?

A. x  
B. NOT y  
C. x XOR y  
D. y

### Q25. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A function f is continuous on [0,2], differentiable on (0,2), and satisfies f(0)=f(2)=1. Which conclusions must hold?

**Candidate answers**
I. Some c∈(0,2) satisfies f′(c)=0.
II. f is constant on [0,2].
III. f attains both a maximum and a minimum on [0,2].
IV. f′(1)=0 necessarily.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q26. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A parent opens an ordinary file and then forks. Neither process closes or duplicates the inherited descriptor. Which property is shared through the inherited open file description?

**Candidate answers**
I. The processes' program counters.
II. The file offset associated with those descriptors.
III. Every local variable in their stacks.
IV. Their process identifiers.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q27. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A binary search tree stores distinct keys. A node x has both a left and a right child. Its inorder successor s is used when deleting x. Which statements about s in the tree before deletion are correct?

**Candidate answers**
I. s is in the right subtree of x.
II. s must be a leaf.
III. s has no left child.
IV. s may have a right child.

A. I: invalid; II: invalid; III: valid; IV: valid  
B. I: valid; II: invalid; III: invalid; IV: valid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q28. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

The grammar has start symbol S and productions S→aSbb | T and T→bTa | epsilon. How many distinct terminal strings of length6 does it generate?

**Required precision:** Exact integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q29. [1 Mark] [MSQ]

For a binary tree, preorder and inorder traversals are both A,B,C,D with distinct labels. Which statements are correct?

A. The root is A.
B. Every node except D has only a right child.
C. Every node except D has only a left child.
D. The postorder is D,C,B,A.

### Q30. [1 Mark] [NAT]

A process writes a2048-byte buffer using a system call that may complete partially. The first call returns768 and the second, correctly adjusted call returns512. Both returns indicate successfully written bytes. How many buffer bytes remain to be written, assuming no other output occurs?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Two1000-bit packets traverse a store-and-forward router. The incoming link transmits1000 bits/ms; the outgoing link transmits500 bits/ms. Both packets are ready at the source at time0, propagation is negligible, and the router starts forwarding a packet only after receiving it completely. At what time, in milliseconds, does the last bit of the second packet leave the router?

**Required precision:** Exact number.

A. 5  
B. 10  
C. 3  
D. 6

### Q32. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A directed graph has adjacency lists s:[a,b], a:[c,d], b:[d], c:[], d:[e], e:[]. BFS starts at s, scans each list in the displayed order and marks a vertex when enqueuing it. At the instant d is first enqueued, how many vertices are already in the queue immediately before that enqueue?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q33. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A process blocks on an empty pipe while another process can eventually write to it. Which statements are correct under ordinary blocking I/O semantics?

**Candidate answers**
I. The blocked process need not consume CPU time by busy-waiting.
II. Blocking on the pipe necessarily means the whole system is deadlocked.
III. A successful write may make the reader runnable.
IV. The reader must be executing continuously for the writer to write.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q34. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

In an ER model, Department is a strong entity with key dept_id. Project is weak and identified by its owning Department and partial key project_code. Task is weak and identified by its owning Project and partial key task_no. Project codes may repeat across departments; task numbers may repeat across projects. No surrogate keys or additional uniqueness constraints are introduced. How many attributes are needed in the minimal primary key of the mapped Task relation?

A. 3  
B. 6  
C. 2  
D. 4

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A two-level AND–OR circuit implements f=ab+(NOT a)c. Assume b=c=1 and only a changes from0 to1. Gate delays are arbitrary positive values; a and NOT a need not change simultaneously. Which extra product term can be ORed into the output without changing f's Boolean function and eliminates the possible static-1 hazard for this transition?

A. (NOT b)(NOT c)  
B. a(NOT c)  
C. bc  
D. (NOT a)(NOT b)

### Q36. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A binary code consists of all length4 bit strings having even parity. A codeword is transmitted through a channel where each bit independently flips with probability1/4. What is the probability that at least one bit changes but the received string is another valid codeword?

**Required precision:** Exact decimal.

A. 0.78515625  
B. 0.10742188  
C. 0.21484375  
D. 0.60742188

### Q37. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A hidden source is chosen once: source I with probability 1/3, source II with probability 2/3. Conditional on that source, trials are independent; success probability is 1/4 for I and 1/2 for II. Given exactly two successes in the first three trials, what is the probability of success on the fourth trial?

**Candidate answers**
I. 1/2
II. 35/76
III. 3/19
IV. 7/16

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q38. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A PDA has one control state and initial stack containing one X. Reading a replaces a top X by XX; reading b pops one X. There are no epsilon moves and no transition when the stack is empty. It accepts when the whole input is consumed and the stack is empty. How many words of length5 over{a,b} are accepted?

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A DMA device writes a memory buffer while a CPU has an old cached copy. Assume the cache is not coherent with the device and no synchronization action is taken. Which statements are correct?

**Candidates**

**I.** The CPU can read stale data from its cache after DMA completes.

**II.** DMA completion alone under these assumptions guarantees the cached copy was updated.

**III.** A suitable cache-invalidation protocol can be necessary before CPU consumption.

**IV.** Physical memory sharing necessarily implies hardware cache coherence.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q40. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A machine has a 1 ns clock, ideal CPI=1, and no overlapping stalls. Conditional branches are 20% of instructions. A static predictor predicts not taken; 60% of branches are taken, and each misprediction costs three additional cycles. A new predictor mispredicts 10% of all branches but requires a 1.1 ns clock; all other CPI contributions stay unchanged. Approximately what is the new processor's speedup over the old one on the same instruction stream?

**Candidate answers**
I. 0.857
II. 1.166
III. 1.283
IV. 1.360

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A binary search tree contains ordered keys a<b<c. Successful search probabilities are 0.2,0.5,0.3, respectively, with no unsuccessful searches. Each comparison with a node costs one unit, including the successful comparison. What is the minimum expected search cost over all BST shapes?

**Required precision:** Exact finite decimal.

A. 3.0  
B. 0.8  
C. 2.5  
D. 1.5

### Q42. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An instruction computes an address by first adding a signed displacement to a base register, then reading a32-bit pointer from that address, then using the pointer as the final operand address. Base=1000, displacement=12, and memory word at1012 contains2040. The operand is a four-byte integer. How many data-memory reads are needed to obtain the operand, excluding instruction fetch and assuming no cache hits?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q43. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Use set relational algebra. C(Student)={u,v,w}, R(Student,Course)={(u,x),(u,y),(v,x)}, and Required(Course) is empty. A query is defined as

```text
C − project_Student((C × Required) − R)
```

How many student tuples does the query return, including students with no tuples in R?

**Required precision:** Exact integer.

A. 6  
B. 3  
C. 2  
D. 4

### Q44. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A directed graph has edges s→a(1),s→b(4),b→a(−5),a→t(1),b→t(10). An implementation runs Dijkstra's algorithm and terminates as soon as t is extracted as minimum, despite the negative edge. What is its reported distance minus the actual shortest s-to-t distance?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q45. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process has two threads sharing ordinary process resources. One thread changes a global variable and opens a file. Which statements are correct under the conventional process/thread model?

A. The other thread can access the same global variable, subject to synchronization requirements.  
B. The threads necessarily have separate virtual address spaces.  
C. The open descriptor belongs to a process-wide descriptor table shared by the threads.  
D. Each thread normally has its own execution stack and register context.

### Q46. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A binary min-heap contains distinct keys. Decreasing the key at an arbitrary nonroot index may violate heap order with which nodes first?

**Candidate answers**
I. Its parent; upward restoration may be needed.
II. Only its children; downward restoration is always required.
III. Every node necessarily becomes invalid.
IV. No heap-order violation can result from decreasing a key.

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q47. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An undirected graph on A,B,C,D has edges AB=1, AC=2, BC=2, BD=3, CD=3, AD=4. Which statements are correct?

A. Every minimum spanning tree contains AB.  
B. Exactly four minimum spanning trees exist.  
C. The smallest spanning-tree weight strictly greater than the minimum is 8.  
D. Raising AD's weight from 4 to 100 leaves the set of minimum spanning trees unchanged.

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider languages over {0,1}. Which statements are true?

**Candidates**

**I.** {wwᴿ : w∈{0,1}*} is context-free.

**II.** {ww : w∈{0,1}*} is context-free.

**III.** Restricting {ww : w∈{0,1}*} to the unary alphabet {0} gives a regular language.

**IV.** Every context-free language is closed under intersection with every other context-free language.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q49. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A message queue has capacity3. It starts empty. Process P executes send(A),send(B),send(C),send(D) in order, and process Q has not yet run. Each send blocks if the queue is full; a successful send appends one item. How many of P's sends have completed when it first blocks?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q50. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An undirected graph has vertices1 through5 and edges12,23,31,34,45. A signed vertex-edge incidence matrix assigns an arbitrary orientation to every edge, placing−1 at its tail and+1 at its head. What is the dimension of the null space of this matrix over the real numbers?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q51. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In this code, p points to a valid integer object, f may modify that object, and integer arithmetic does not overflow:

```text
u = *p + 2
call f()
v = *p + 2
```

Which statements are correct?

**Candidate answers**
I. Identical text proves v may be replaced by u.
II. A proof that f cannot modify the pointed-to object can make that reuse valid.
III. If f changes the object, the two evaluations may differ.
IV. A function call is never relevant to memory-expression availability.

A. I: valid; II: valid; III: valid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: invalid; IV: valid

### Q52. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Relation R(x,y) contains(1,1),(1,2),(2,2),(3,1). Evaluate the domain-restricted tuple-calculus condition R(x,y) AND NOT EXISTS z(R(y,z) AND z≠x). How many tuples of R satisfy it?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q53. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

In the divisibility poset of positive divisors of 72, how many elements x satisfy gcd(x,12)=6 and lcm(x,12)=72?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q54. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A table has rows (department,salary): (A,10),(A,10),(A,20),(B,20),(B,NULL). Consider:

```sql
SELECT department
FROM T
GROUP BY department
HAVING COUNT(DISTINCT salary) = 2
   AND SUM(salary) > 30;
```

Which result is returned under standard SQL aggregate rules?

**Candidate answers**
I. No rows
II. A only
III. B only
IV. A and B

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A one-slot producer–consumer buffer uses semaphores empty=1 and full=0. The producer incorrectly performs wait(empty), signal(full), then writes the item. The consumer performs wait(full), reads the item, signal(empty). Assume semaphore operations are atomic and scheduling may switch between any two operations. Which statements are correct?

**Candidates**

**I.** The consumer can read before the producer writes the new item.

**II.** Atomic semaphore operations alone eliminate this ordering error.

**III.** Moving the producer's signal(full) after the write repairs this particular publication error.

**IV.** The consumer's wait(full) forces all future producer writes to occur before its read.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV

### Q56. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes the keyword if, identifiers consisting of a letter followed by letters or digits, double-quoted string literals, and C-style /*...*/ comments. It uses longest match and gives a keyword priority over an identifier in an equal-length tie. Whitespace and comments are discarded. How many keyword tokens and total tokens, respectively, result from this input?

```text
"if" if /*if*/ if2
```

A. (3,4)  
B. (2,3)  
C. (1,4)  
D. (1,3)

### Q57. [2 Marks] [NAT]

For A with rows (2,1,1),(4,3,3),(8,7,9), compute a Doolittle factorization A=LU without row swaps, where L has diagonal entries 1. What is L₃₂?

**Answer format:** Integer.

### Q58. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

The grammar E→E+E | E*E | id has no precedence or associativity rules. For the token string id+id*id+id, how many distinct parse trees have a '+' production at the root?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q59. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A four-port Ethernet switch initially has dynamic entries A→1, B→2, C→3 and no entry for D. It learns or updates the source port before forwarding each frame, floods an unknown destination to every port except ingress, and has no entry expiry during this sequence. Four frames arrive in order: (ingress 3, source A, destination B), (ingress 2, source B, destination A), (ingress 3, source C, destination D), (ingress 4, source D, destination C). Which lists their respective egress-port sets?

**Candidate answers**
I. {2}; {3}; {1,2,4}; {3}
II. {2}; {1}; {1,2,4}; {3}
III. {2}; {3}; {1,2,3,4}; {3}
IV. {2}; {3}; {4}; {1,2,3}

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q60. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An ε-NFA has initial state p, final state r, ε-transitions p→q and q→p, and an a-transition q→r. There are no other transitions. Which statement is correct?

**Candidate answers**
I. The language is infinite because there is an ε-cycle.
II. The language is {a}, although there are infinitely many finite accepting runs on a.
III. The empty string is accepted because p and q form a cycle.
IV. No string is accepted because the ε-cycle prevents progress.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q61. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Evaluate ∫₀¹ max(x²,1−x) dx, rounded to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.3183  
B. 0.3409  
C. 0.8409  
D. 0.6817

### Q62. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A distance-vector router X has neighbours Y and Z with link costs2 and5. Their advertised distances to destination D are respectively7 and0, so X initially routes through Z. The X–Z link fails; X receives no new advertisement from Y before recomputing. Y's advertised7 was itself based on routing through X before the failure. Using the stored advertisements exactly as stated, what distance does X now advertise to D? No split horizon or poison reverse is used.

**Required precision:** Integer.

A. 18  
B. 9  
C. 5  
D. 10

### Q63. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A six-bit unsigned register x initially holds 45. One operation rotates its bits left by two positions within the six-bit word, then XORs the result with binary 001111. What decimal value results after two such operations?

**Required precision:** Integer.

A. 40  
B. 80  
C. 20  
D. 41

### Q64. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What does the following conforming C program print? All arithmetic fits in int.

```c
#include <stdio.h>
static void change(int **p, int *q) {
    int *t = *p;
    *p = q;
    *t += **p;
    **p += 1;
}
int main(void) {
    int a[3] = {2,5,9};
    int *p = a;
    change(&p, a+1);
    change(&p, a);
    printf("%d %d %d\n", a[0], a[1], (int)(p-a));
    return 0;
}
```

A. 7 13 0  
B. 8 13 0  
C. 8 6 1  
D. The program has undefined behaviour due to pointer aliasing.

### Q65. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-input Boolean function F(a,b,c,d) equals 1 exactly when at least three inputs are 1. It is implemented using a 4-to-1 multiplexer whose select bits are b (more significant) and c (less significant). Data inputs I0, I1, I2, I3 correspond respectively to bc = 00, 01, 10, 11. Which tuple of data-input functions implements F? Here juxtaposition means AND and + means OR.

A. (0, ad, ad, a+d)  
B. (0, a+d, a+d, ad)  
C. (ad, ad, ad, 1)  
D. (0, 0, 0, a+d)

## ANSWER KEY — MOCK TEST 083

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MSQ | 1 | A, B, C |
| 3 | MSQ | 1 | A, C, D |
| 4 | MSQ | 1 | B, C, D |
| 5 | MSQ | 1 | A, B, D |
| 6 | MCQ | 2 | B |
| 7 | MSQ | 2 | A, B, D |
| 8 | MCQ | 2 | C |
| 9 | MCQ | 2 | C |
| 10 | MSQ | 2 | A, C, D |
| 11 | MSQ | 1 | B, C, D |
| 12 | MCQ | 1 | C |
| 13 | MCQ | 1 | D |
| 14 | MCQ | 1 | D |
| 15 | MCQ | 1 | D |
| 16 | MCQ | 1 | A |
| 17 | MCQ | 1 | A |
| 18 | MCQ | 1 | D |
| 19 | MCQ | 1 | A |
| 20 | MCQ | 1 | C |
| 21 | MSQ | 1 | A, C |
| 22 | MSQ | 1 | A, B, C |
| 23 | MSQ | 1 | A, C, D |
| 24 | MSQ | 1 | A, B, C |
| 25 | MCQ | 1 | A |
| 26 | MCQ | 1 | D |
| 27 | MCQ | 1 | C |
| 28 | MSQ | 1 | B, C, D |
| 29 | MSQ | 1 | A, B, D |
| 30 | NAT | 1 | 768 |
| 31 | MCQ | 1 | A |
| 32 | MCQ | 1 | B |
| 33 | MCQ | 1 | B |
| 34 | MCQ | 1 | A |
| 35 | MSQ | 1 | A, B, D |
| 36 | MSQ | 2 | A, B, D |
| 37 | MCQ | 2 | A |
| 38 | MSQ | 2 | A, B, C |
| 39 | MCQ | 2 | C |
| 40 | MCQ | 2 | B |
| 41 | MSQ | 2 | A, B, C |
| 42 | MCQ | 2 | C |
| 43 | MSQ | 2 | A, C, D |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 2 | B |
| 46 | MCQ | 2 | C |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | B |
| 49 | MCQ | 2 | D |
| 50 | MCQ | 2 | A |
| 51 | MCQ | 2 | B |
| 52 | MCQ | 2 | D |
| 53 | MCQ | 2 | C |
| 54 | MCQ | 2 | A |
| 55 | MCQ | 2 | B |
| 56 | MSQ | 2 | A, B, C |
| 57 | NAT | 2 | 3 |
| 58 | MSQ | 2 | A, B, C |
| 59 | MCQ | 2 | B |
| 60 | MCQ | 2 | B |
| 61 | MSQ | 2 | A, B, C |
| 62 | MCQ | 2 | B |
| 63 | MSQ | 2 | B, C, D |
| 64 | MSQ | 2 | A, C, D |
| 65 | MSQ | 2 | B, C, D |
