# GATE CS 2027 — Full-Length Mock Test 072

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

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Every signed form is archived. No archived form is editable. At least one editable form exists. Which conclusions necessarily follow?

**Candidates**

**I.** No signed form is editable.

**II.** Every unsigned form is editable.

**III.** At least one unsigned form exists.

**IV.** At least one signed form exists.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV

### Q2. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A paper strip has coordinate 0≤x≤8. Fold its part x>5 leftwards across x=5. Then fold every layer lying at x<3 rightwards across x=3. Punch through all layers at the resulting position x=4 and fully unfold. What is the mean of the original x-coordinates of all distinct punctures?

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q3. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four events occur once each: filing F, inspection I, approval A, and publication P. Filing precedes both inspection and approval. Publication follows both inspection and approval. No order between inspection and approval is specified. Which conclusions necessarily follow?

A. Filing is the first of these four events.  
B. Inspection immediately precedes approval.  
C. Publication is the last of these four events.  
D. Exactly two orders of these four events satisfy the conditions.

### Q4. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A bag contains one red and three blue balls. They are drawn without replacement until the red ball appears. What is the expected total number of draws, including the red ball?

**Required precision:** Exact decimal.

A. 5.0  
B. 1.3  
C. 3.5  
D. 2.5

### Q5. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Every sensor that passed calibration was installed. Some installed sensors were not tested. Which statements follow necessarily?

**Candidates**

**I.** Every sensor not installed failed to pass calibration.

**II.** Every installed sensor passed calibration.

**III.** At least one installed sensor was not tested.

**IV.** No untested sensor passed calibration.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II

### Q6. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A triangle has vertices A=(0,8),B=(−6,0),C=(6,0). Its orthocentre H is the intersection of its altitude lines. What is the y-coordinate of H?

**Required precision:** Exact decimal.

A. 9.0  
B. 2.3  
C. 5.5  
D. 4.5

### Q7. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a finite list of integers, operation R reverses the list, and operation N negates every entry without changing the order. A student claims that applying R then N always gives the same list as applying N then R. Which statements hold?

**Candidates**

**I.** Checking the claim on one list of length three proves it for lists of every length.

**II.** The claim holds because each final position contains the negative of the same original entry under either order.

**III.** Applying the combined operation twice restores every original list.

**IV.** The claim implies that reversing a list always leaves it unchanged.

A. II and IV  
B. III and IV  
C. I and II  
D. II and III

### Q8. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An urn contains three red and three blue balls. Two balls are drawn without replacement. If they have different colours, a prize of 6 units is paid; otherwise nothing is paid. What is the expected prize?

**Required precision:** Exact finite decimal.

A. 7.2  
B. 1.8  
C. 3.6  
D. 4.6

### Q9. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A sequence starts a1=0. For each positive integer n, define a(n+1)=a(n)+n when n is odd and a(n+1)=a(n)−n when n is even. What is a101?

**Required precision:** Integer, including a minus sign if needed.

A. -100  
B. -50  
C. -25  
D. -49

### Q10. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two axis-aligned squares each have side4. One occupies [0,4]×[0,4]. The other occupies [t,t+4]×[t,t+4], where0≤t≤4. Their union has area28. What is t?

**Required precision:** Exact number.

A. 2  
B. 4  
C. 1  
D. 3

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A C array `int a[3][5]` is stored in row-major order, with sizeof(int)=4 bytes. What is the byte offset of a[2][3] from the start of the array?

**Required precision:** Integer.

A. 104  
B. 26  
C. 53  
D. 52

### Q12. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A DFA tracks the input length modulo2 and the number of a symbols modulo2 over alphabet{a,b}. It starts with both parities even. How many of the four parity-pair states are reachable?

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q13. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially x=y=1 and a database invariant requires x+y≥1. Two concurrent transactions read the same initial snapshot. T1, seeing y=1, writes x=0; T2, seeing x=1, writes y=0. A scheme rejects only concurrent writes to the same item, so both commit. Which statements are correct?

A. Their writes target different items.  
B. The final state violates the invariant.  
C. The execution is equivalent to a serial execution of these conditional transactions.  
D. Avoiding direct write-write conflicts alone is insufficient for this invariant.

### Q14. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

T1 writes x. Before T1 commits, T2 reads that written value and then commits. T1 later aborts. Which statements are correct?

**Candidate answers**
I. T2 performed a dirty read.
II. This schedule is recoverable.
III. T2 committed based on a value later rolled back.
IV. The schedule is strict.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q15. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A grammar has start symbol S and productions S→AB, A→a, B→bB, C→c. A nonterminal is productive if it derives some finite terminal string. How many nonterminals are both reachable from S and productive?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q16. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A Karnaugh-map group contains eight minterms of a four-variable function and forms a valid Boolean cube. How many literals remain in its product term?

**Required precision:** Integer.

A. 2  
B. 1  
C. 0  
D. 3

### Q17. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An unweighted directed graph has edges s→a,s→b,a→c,b→d,d→c. A BFS begins at s and marks vertices when enqueued. Which statements are correct regardless of the order of s's adjacency list?

**Candidates**

**I.** c is assigned distance2.

**II.** c may be assigned distance3 if b is examined first.

**III.** d is assigned distance2.

**IV.** Every vertex's BFS parent is necessarily unique in every directed graph.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

### Q18. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A collision-detection link transmits at 100 Mbit/s. The worst-case one-way propagation time between stations, including repeater delays, is 2.4 microseconds. Ignore all other timing constraints. What is the minimum frame size in bytes required for a sender still to be transmitting when a worst-case collision notification returns?

**Required precision:** Integer bytes; use 1 Mbit=10⁶ bits.

A. 60  
B. 120  
C. 30  
D. 61

### Q19. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A directory contains three hard links to the same ordinary file. One link is removed. How many directory hard links to that file remain, assuming no other changes?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q20. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A procedure F(n) returns immediately for n≤1 and otherwise calls F(floor(n/2)) once. Including the initial invocation and the base invocation, how many calls occur for n=19?

**Required precision:** Integer.

A. 10  
B. 3  
C. 6  
D. 5

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A random variable X has mean 10 and variance 4. For Z=3X−2, find E[Z²].

**Required precision:** Integer.

A. 1640  
B. 410  
C. 820  
D. 821

### Q22. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A relation R on {1,2,3,4} is defined by xRy iff x and y have the same parity. How many ordered pairs belong to R composed with R?

**Required precision:** Exact integer.

A. 16  
B. 4  
C. 8  
D. 9

### Q23. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A lexer recognizes unsigned integer tokens, the operator '-', and identifiers. It tokenizes x--12 without treating '--' as a separate operator. The parser alone distinguishes unary and binary minus. Which token sequence is produced?

**Candidate answers**
I. identifier(x), minus, integer(−12)
II. identifier(x), minus, minus, integer(12)
III. identifier(x−−12)
IV. identifier(x), decrement, integer(12)

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q24. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two Ethernet stations collide and independently choose their backoff values uniformly from {0,1,2,3}. Conditional on their values being different, what is the probability that the smaller value is zero?

**Required precision:** Exact decimal.

A. 0.3  
B. 0.8  
C. 0.1  
D. 0.5

### Q25. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Four identical256×8-bit RAM chips provide a1024×8-bit byte-addressable memory. Address bits A0–A7 connect to every chip's address pins. A decoder selects a chip using A8,A9. How many chips are selected during one valid byte read, and how many distinct byte addresses can be read? Enter the product of these two numbers.

**Required precision:** Integer.

A. 2048  
B. 512  
C. 1025  
D. 1024

### Q26. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A connected weighted undirected graph has a vertex v incident to exactly one edge e. Edge weights may be negative or equal. Which statements necessarily hold?

**Candidates**

**I.** Every spanning tree contains e.

**II.** Every minimum spanning tree contains e.

**III.** e must be the minimum-weight edge in the entire graph.

**IV.** Removing e leaves a connected graph.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q27. [1 Mark] [NAT]

In a simplified slotted contention scheme, two stations independently choose one of four slots uniformly and transmit once in that slot. A collision occurs if they choose the same slot. Given that station A chose a slot later than slot1, what is the collision probability?

**Answer format:** Exact decimal.

### Q28. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

In the multiplicative group of units modulo 10, what is the order of the element 3?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q29. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For real x, define f(x)=x when x is rational and f(x)=−x when x is irrational. Which statements are true?

**Candidates**

**I.** f is continuous at zero.

**II.** f is not differentiable at zero.

**III.** f is continuous at one.

**IV.** f′(0)=0.

A. I and IV  
B. I and II  
C. II and III  
D. II and IV

### Q30. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An eight-bit two's-complement fixed-point representation uses four fractional bits. What real number does bit pattern 11101000 represent?

**Required precision:** Exact finite decimal.

A. -3.0  
B. -0.8  
C. -0.5  
D. -1.5

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes the keyword `in`, identifiers matching [a-z]+, and the single-character token '.'. It uses longest match, giving the keyword priority over an identifier only when their matched lengths tie. What token-type sequence is produced on input `in.inner`?

A. keyword, '.', identifier.  
B. identifier, '.', keyword, identifier.  
C. keyword, '.', keyword, identifier.  
D. identifier, '.', identifier.

### Q32. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed graph has edges s→a of weight 2, s→b of weight 5, and b→a of weight −4. There are no other edges. Which statements are correct?

**Candidates**

**I.** The shortest s-to-a path has weight 1.

**II.** The graph has a negative-weight cycle.

**III.** A Dijkstra implementation that permanently settles a before b can output a wrong distance for a.

**IV.** Every shortest path uses the fewest possible edges.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q33. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Independent random variables X and Y each have variance 4. Find Var(2X−3Y+7).

**Required precision:** Integer.

A. 104  
B. 26  
C. 52  
D. 53

### Q34. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A processor uses byte addressing and little-endian 32-bit words. Bytes at addresses 100 through 103 are hexadecimal 12,34,56,78. It loads the 32-bit word at 100, shifts that unsigned value right by 16 bits, and stores the low 16 bits at addresses 102–103 in little-endian order. What decimal value is then in byte 102?

**Required precision:** Integer.

A. 172  
B. 43  
C. 86  
D. 87

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

On a UNIX-like file system, path p refers to regular file F. Process R has already opened F for reading. Process W creates a different regular file G and atomically renames G over p. No process modifies F or G afterward. Assume rename succeeds and no symbolic links are involved. Which statements hold?

**Candidates**

**I.** R's existing descriptor still refers to F.

**II.** A later successful open of p refers to G.

**III.** The rename necessarily changes the inode referred to by R's existing descriptor.

**IV.** F's storage must be reclaimed before the rename can return, even while R retains its descriptor.

A. II and III  
B. II and IV  
C. I and II  
D. III and IV

### Q36. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A size-7 hash table uses linear probing with h(k)=k mod 7 and wraparound. Insert 10,17,24,11 in that order into an empty table. Delete 17 by leaving a tombstone. A subsequent unsuccessful search for 31 stops at the first slot that has never been occupied, but passes tombstones. How many slots does this search inspect, including the terminating slot?

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q37. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A direct-mapped cache has four sets and two-word blocks. A four-row matrix stores four data words per row, followed by p padding words per row. The matrix starts at word address0, and each row must begin at an even word address. What is the smallest nonnegative p making the first data words of the four rows map to four different cache sets?

**Required precision:** Integer words.

A. 4  
B. 2  
C. 1  
D. 3

### Q38. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A routing table contains prefix203.0.113.0/24 via X and more-specific prefix203.0.113.128/25 via Y. No other route matches. Which statements are correct under longest-prefix matching?

**Candidate answers**
I. Address203.0.113.200 uses Y.
II. Address203.0.113.100 uses X.
III. Installing the /24 after the /25 necessarily makes it override the /25.
IV. Removing the /25 makes203.0.113.200 use X.

A. I: invalid; II: valid; III: invalid; IV: valid  
B. I: valid; II: valid; III: valid; IV: valid  
C. I: invalid; II: invalid; III: valid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q39. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Four matrices A,B,C,D have dimensions 5×10, 10×2, 2×8 and 8×3. Using ordinary matrix multiplication with pqr scalar multiplications for a p×q by q×r product, what is the minimum scalar multiplication count over all parenthesizations of ABCD?

**Required precision:** Integer.

A. 178  
B. 356  
C. 89  
D. 179

### Q40. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A message of 1200 bytes traverses two store-and-forward links in series, each operating at 8000 bits/s. It is divided into k equal-payload packets, each with a 75-byte header, where k is a positive divisor of1200. Links can operate simultaneously on different packets. Ignore propagation and processing delays. What value of k minimizes the time at which the complete message arrives?

**Required precision:** Exact integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A rooted tree has the parent array for vertices1 through7 given by[0,1,1,2,2,4,3], where0 marks the root. An operation cuts the subtree rooted at2 and reattaches its root as a child of7. How much does the sum of depths of all seven vertices increase, with the root's depth defined as0?

**Required precision:** Integer.

A. 16  
B. 8  
C. 4  
D. 9

### Q42. [2 Marks] [NAT]

Insert keys20,10,30,25,40,22,27 into an initially empty ordinary BST. Perform a single left rotation at root20: its right child30 becomes the root,20 becomes30's left child, and30's former left subtree becomes20's right subtree. How many keys have the same depth before and after the rotation, counting the root's depth as0?

**Answer format:** Integer.

### Q43. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Represent exactly the address set10.1.0.0/24 excluding10.1.0.64/26 as a union of CIDR prefixes, without including any excluded address. What is the minimum number of prefixes needed?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q44. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider replacing x*2 by x+x in an integer intermediate representation. Which statements are correct?

A. For unbounded mathematical integers the two expressions are equal.  
B. For arithmetic modulo2^w the two results are equal for every w-bit x.  
C. This equivalence alone proves that replacing any signed C expression involving multiplication can ignore its language's overflow rules.  
D. The replacement's profitability can depend on the target machine, even when semantic equivalence holds.

### Q45. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A fractional knapsack has capacity5 and two available items, each of weight4 and value8. Any real fraction between0 and1 of each item may be selected. Which statements are correct?

**Candidates**

**I.** Selecting weight2.5 from each item is optimal.

**II.** Every optimal solution must have at most one partially selected item.

**III.** An optimal solution with one whole item and one partially selected item exists.

**IV.** The optimal allocation is unique.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q46. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

How many ordered compositions of 8 use only parts 1 and 2 and never place two parts of size 2 consecutively? For example, 2,1,2 is allowed for total 5, while 1,2,2 is not.

**Required precision:** Integer.

A. 38  
B. 10  
C. 20  
D. 19

### Q47. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Procedure P is lexically nested inside Main. Procedures Q and R are both lexically nested inside P. During execution, Main calls P, P calls Q, and Q calls R. Each activation has a static link to its immediate lexical parent's activation and a dynamic link to its caller. From R's activation, how many static links must be followed to access a local variable of Main?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q48. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A binary floating-point system has three significant bits, including the leading1, and sufficient exponent range. It rounds each operation to nearest, with ties to an even significand low bit. Compute the absolute difference between fl(fl(8+1)−8) and fl(8+fl(1−8)). Here fl means rounding one operation in that format.

**Required precision:** Exact number.

A. 2  
B. 0  
C. 3  
D. 1

### Q49. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Five CPU-bound processes are permanently ready in round-robin order. A quantum lasts q positive integer milliseconds, and each intervening context switch costs one millisecond. At time zero the first process starts without an initial switch. Require useful CPU time to be at least 80% of steady-state elapsed time, and require the fifth process to begin its first quantum no later than time 20. What value of q satisfies both requirements?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q50. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A Boolean cover-selection chart contains candidate rows P and Q. P covers{u,v} at cost3; Q covers{u,v,w} at cost2. The objective is minimum total cost, and selecting a row has no effect except covering its columns. Which statements are correct?

**Candidate answers**
I. An optimal cover can always be chosen without P.
II. Replacing P by Q in a cover cannot uncover a column and cannot increase cost.
III. P must be retained merely because some of its columns also appear in Q.
IV. The same dominance conclusion follows if Q instead costs5, solely from its greater coverage.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: valid; IV: valid  
D. I: valid; II: valid; III: invalid; IV: invalid

### Q51. [2 Marks] [NAT]

A rooted tree has root r with children a,b,c. Vertex a has two leaf children, b has one leaf child, and c is a leaf. How many different preorder sequences of vertex labels are possible if the order of children at every vertex may be chosen independently? All seven vertex labels are distinct.

**Answer format:** Exact integer.

### Q52. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

On the interval[−2,2], how many distinct x values attain the global maximum of |x³−3x|?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q53. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Define L={aⁱbʲ:i,j≥0 and i≠j}. Which statements are correct?

**Candidates**

**I.** L is context-free.

**II.** L is regular.

**III.** The complement of L within a*b* is {aⁿbⁿ:n≥0}.

**IV.** ε belongs to L.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Six employees participate in a directed Mentors relationship. Self-mentoring is forbidden. Each employee may mentor at most two others and must be mentored by at least one other employee. A pair (u,v) means u mentors v. What is the maximum possible number of distinct pairs?

**Required precision:** Integer.

A. 24  
B. 12  
C. 6  
D. 13

### Q55. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An initially free64-KiB region is managed by a binary buddy allocator. Each request is rounded up to the smallest power-of-two KiB block that fits it. Splitting always allocates the lowest-address available suitable descendant; free buddies coalesce immediately. Requests A=9KiB, B=9KiB, C=17KiB are allocated in that order. A is then freed. What is the size, in KiB, of the largest request that can now be satisfied without freeing B or C?

**Required precision:** Integer.

A. 32  
B. 8  
C. 16  
D. 17

### Q56. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A combinational circuit implements unsigned comparison A>B for two-bit inputs A=a1a0 and B=b1b0. Among the16 possible input pairs, for how many does the low-bit comparison a0>b0 disagree with the full comparison A>B?

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q57. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

One process executes the following pseudocode. Every fork succeeds and duplicates the current process; no process exits early.

```text
fork()
if fork() returns 0:
    fork()
```

Including the original process, how many processes exist after all forks complete?

**Required precision:** Integer.

A. 12  
B. 6  
C. 3  
D. 7

### Q58. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Let L={a^n : n is a perfect square}, including ε. For a hypothetical regular pumping length p≥1, choose s=a^(p²). A legal pumped part has length k with1≤k≤p. Which statements are correct?

**Candidate answers**
I. Pumping once more gives length p²+k, strictly between p² and(p+1)².
II. For every legal decomposition, pumping twice leaves the language.
III. The proof depends on choosing the pumped part to have exactly p symbols.
IV. The pumping lemma therefore proves L regular.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: valid; II: valid; III: valid; IV: invalid  
D. I: invalid; II: invalid; III: valid; IV: valid

### Q59. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={ww : w in {a,b}*}. Which statements are correct?

A. Every word in L has even length.  
B. Every even-length palindrome belongs to L.  
C. L contains words that are not palindromes.  
D. L is closed under reversal.

### Q60. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An ideal single-issue pipeline executes100 instructions in104 cycles, including filling and draining. Of these instructions,20 are conditional branches. A prediction scheme mispredicts exactly25% of those branches; every misprediction introduces3 extra cycles. No other stalls occur. What is the resulting CPI, using total execution cycles divided by100?

**Required precision:** Exact decimal.

A. 2.38  
B. 0.60  
C. 2.19  
D. 1.19

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A fair coin chooses one of two bags. Bag A contains two red and one blue ball; bag B contains one red and two blue balls. Two draws are made without replacement from the chosen bag. Given that the second draw is red, what is the probability that the first draw was blue? Round to four decimal places.

**Required precision:** Decimal rounded to four places.

A. 0.6667  
B. 0.3333  
C. 0.3334  
D. 0.8334

### Q62. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L1={a^n b^n c^m : n,m≥0} and L2={a^m b^n c^n : n,m≥0}. Which statements are correct?

A. Both L1 and L2 are context-free.  
B. Their intersection is {a^n b^n c^n : n≥0}.  
C. Their intersection must be context-free because each language is context-free.  
D. Their union is context-free.

### Q63. [2 Marks] [NAT]

Under set semantics, R(A,B)={(1,x),(1,y),(2,x),(3,x),(3,y)} and S(B)={x,y}. How many tuples are in relational division R÷S?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

In an expression language, evaluating an operand may have side effects; && and || evaluate left to right and short-circuit. Values are Boolean. Which rewrites preserve both returned value and operand side effects in every execution?

A. false && f() → false
B. f() && false → false
C. true || f() → true
D. f() || true → true

### Q65. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A poset has elements a,b,c,d with a<c,b<c,c<d, and only the comparisons forced by these and reflexivity. Let J be the family of its downward-closed subsets, ordered by inclusion. Which statements are correct?

**Candidate answers**
I. J has six elements, including the empty subset.
II. Join in J is set union.
III. Meet in J is set intersection.
IV. J fails distributivity because a and b are incomparable.

A. I: invalid; II: valid; III: valid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: invalid  
D. I: invalid; II: invalid; III: invalid; IV: valid

## ANSWER KEY — MOCK TEST 072

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | MCQ | 1 | C |
| 3 | MCQ | 1 | B |
| 4 | MSQ | 1 | A, B, C |
| 5 | MCQ | 1 | A |
| 6 | MSQ | 2 | A, B, C |
| 7 | MCQ | 2 | D |
| 8 | MSQ | 2 | A, B, D |
| 9 | MSQ | 2 | A, C, D |
| 10 | MSQ | 2 | B, C, D |
| 11 | MCQ | 1 | D |
| 12 | MSQ | 1 | A, C, D |
| 13 | MCQ | 1 | C |
| 14 | MCQ | 1 | D |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 1 | A, C, D |
| 17 | MCQ | 1 | D |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 1 | B, C, D |
| 20 | MCQ | 1 | D |
| 21 | MCQ | 1 | C |
| 22 | MCQ | 1 | C |
| 23 | MCQ | 1 | D |
| 24 | MSQ | 1 | A, B, C |
| 25 | MCQ | 1 | D |
| 26 | MCQ | 1 | C |
| 27 | NAT | 1 | 0.25 |
| 28 | MSQ | 1 | B, C, D |
| 29 | MCQ | 1 | B |
| 30 | MCQ | 1 | D |
| 31 | MSQ | 1 | B, C, D |
| 32 | MCQ | 1 | C |
| 33 | MCQ | 1 | C |
| 34 | MCQ | 1 | C |
| 35 | MCQ | 1 | C |
| 36 | MCQ | 2 | C |
| 37 | MCQ | 2 | B |
| 38 | MCQ | 2 | D |
| 39 | MCQ | 2 | A |
| 40 | MSQ | 2 | B, C, D |
| 41 | MSQ | 2 | A, C, D |
| 42 | NAT | 2 | 3 |
| 43 | MCQ | 2 | C |
| 44 | MCQ | 2 | C |
| 45 | MCQ | 2 | B |
| 46 | MSQ | 2 | A, B, C |
| 47 | MSQ | 2 | A, C, D |
| 48 | MSQ | 2 | A, B, C |
| 49 | MCQ | 2 | D |
| 50 | MCQ | 2 | D |
| 51 | NAT | 2 | 12 |
| 52 | MSQ | 2 | B, C, D |
| 53 | MCQ | 2 | B |
| 54 | MCQ | 2 | B |
| 55 | MSQ | 2 | A, B, D |
| 56 | MCQ | 2 | B |
| 57 | MCQ | 2 | B |
| 58 | MCQ | 2 | B |
| 59 | MCQ | 2 | B |
| 60 | MCQ | 2 | D |
| 61 | MCQ | 2 | A |
| 62 | MCQ | 2 | C |
| 63 | NAT | 2 | 2 |
| 64 | MSQ | 2 | A, C |
| 65 | MCQ | 2 | B |
