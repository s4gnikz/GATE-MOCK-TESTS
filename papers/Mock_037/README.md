# GATE CS 2027 — Full-Length Mock Test 037

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

Arrange the sentences into the most coherent account. No other comparison, restoration or verification is implied.

P. The comparison showed that the missing entries were present in the backup.
Q. The librarian noticed gaps in the catalogue and compared it with a backup.
R. A final check then confirmed that the restored catalogue contained every entry.
S. Using that evidence, she restored the missing entries from the backup.

A. Q, P, S, R  
B. P, Q, S, R  
C. Q, S, P, R  
D. Q, P, R, S

### Q2. [1 Mark] [NAT]

Household A has three boys. Household B has one boy and one girl. Choose a household with equal probability, then choose one of its children uniformly. Given that the selected child is a boy, what is the probability that household A was chosen?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

### Q3. [1 Mark] [MCQ]

“The panel gave the proposal a qualified endorsement: it supported the idea, provided that the budget and access arrangements were revised.” What does “qualified” mean here?

A. Issued by a person holding a professional certificate.
B. Limited by stated conditions.
C. Completely withdrawn.
D. Expressed without reservation.

### Q4. [1 Mark] [NAT]

For real x>0 with x≠1, solve log_x(16)=log_2(x). What is the sum of all valid solutions x?

**Answer format:** Exact decimal.

### Q5. [1 Mark] [MSQ]

An engineer tests a device at every integer temperature from 0°C through 100°C. It operates correctly in all tests. No rule governing its behaviour between tested temperatures is known. Which statements are justified solely by these observations?

A. The device operates correctly at 37°C under the tested conditions.
B. The device must operate correctly at 37.5°C.
C. The observations are compatible with a device that fails at 37.5°C.
D. The device must operate correctly at every integer temperature above 100°C.

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Unit cubes form four vertical columns on a 2×2 grid, with no gaps within a column. All four columns are nonempty. Let h(i,j) be the positive integer height in row i, column j. Orthographic views establish

```text
max(h(1,1),h(1,2)) = 3
max(h(2,1),h(2,2)) = 2
max(h(1,1),h(2,1)) = 3
max(h(1,2),h(2,2)) = 2
```

Which total numbers of cubes are possible?

A. 7  
B. 8  
C. 9  
D. 10

### Q7. [2 Marks] [NAT]

A ten-entry sequence was intended to contain the first ten positive odd integers in order. Exactly one entry was replaced by a different integer. The recorded entries b1,…,b10 satisfy Σ b(i)=106 and Σ i·b(i)=757. What was the intended value of the altered entry?

**Answer format:** Exact integer.

### Q8. [2 Marks] [NAT]

Two circular disks of equal radius r>0 have centres separated by distance r. Let P be the perimeter of their union, excluding arcs lying inside the other disk. What is P/(πr)?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

### Q9. [2 Marks] [MSQ]

Which sentences use standard subject–verb agreement?

A. Each of the reports has a separate appendix.
B. The reports, each with a separate appendix, have been submitted.
C. Each of the reports have a separate appendix.
D. The reports, each with a separate appendix, has been submitted.

### Q10. [2 Marks] [NAT]

Every item in a batch costs a retailer ₹80, and the listed selling price is ₹100. The retailer sells three-fifths of the batch at the listed price, then sells all remaining items at one discounted price. The overall profit is 12.5% of the batch's total cost. What percentage discount from the listed price was used for the remaining items? Ignore taxes and other costs.

**Answer format:** Exact integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An SQL integer column x has CHECK(x>0) but no NOT NULL constraint. A CHECK passes when its condition is TRUE or UNKNOWN. Which statements are correct?

**Candidates**

**I.** A row with x=NULL can satisfy this CHECK.

**II.** Every non-NULL value satisfying this CHECK is positive.

**III.** The CHECK alone excludes NULL values.

**IV.** Adding NOT NULL would impose no additional restriction.

A. I and II  
B. II and IV  
C. III and IV  
D. I and III

### Q12. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In a three-address representation, evaluate `a+b*c` with normal multiplication precedence, without algebraic reordering. Which sequence is suitable?

**Candidate answers**
I. t1=a+b; t2=t1*c
II. t1=b*c; t2=a+t1
III. t1=a*c; t2=t1+b
IV. t1=a+b; t2=b*c

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A stack initially empty receives items1,2,3,4 in that order. Pops may be interleaved with pushes. Which proposed output sequence is impossible?

A. 2,1,4,3  
B. 3,2,1,4  
C. 3,1,2,4  
D. 4,3,2,1

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

For L={ε,a³}∪{aⁿ:n≥5}, find the smallest positive regular pumping length p. The requirement is: every w∈L with |w|≥p has a decomposition w=xyz with |xy|≤p, |y|>0, and xyⁱz∈L for every integer i≥0.

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 4-to-1 multiplexer has select bits A,B, with A more significant. Its data inputs for select values 00,01,10,11 are C, NOT C, 1,0 respectively. Minterms are numbered using A,B,C with A most significant. Which set is the output's on-set?

A. {0,3,4,5}  
B. {1,2,4,5}  
C. {1,2,6,7}  
D. {0,1,2,5}

### Q16. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A0/1 knapsack of capacity4 has just one item, of weight2 and value3. An implementation initializes dp[0..4] to0 and processes this item as follows:

```text
for w = 2 to 4, in increasing order:
    dp[w] = max(dp[w], dp[w-2] + 3)
```

Which statements are correct?

**Candidates**

**I.** The loop returns the correct0/1 optimum at dp[4].

**II.** It sets dp[4] to6 by effectively reusing the item.

**III.** Iterating w from4 down to2 instead avoids this reuse.

**IV.** Every dp[w-2] read in this loop is necessarily from before processing the item.

A. I and II  
B. II and III  
C. I and III  
D. I and IV

### Q17. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A synchronous two-bit machine updates (q1,q0) to (q0,q1 XOR q0) on each clock edge. Its reset state is 01. Which statements are correct?

**Candidate answers**
I. The reset trajectory has period 3.
II. State 00 is reached after three edges from reset.
III. State 10 is reached after two edges from reset.
IV. q1 and q0 are complements throughout the reset trajectory.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Equivalence relations R and S on {1,2,3,4,5,6} have partitions {{1,2},{3,4},{5,6}} and {{1},{2,3},{4,5},{6}}, respectively. Let T be the smallest equivalence relation containing R∪S. How many ordered pairs are in R∩S and T, respectively?

A. 6 and 36  
B. 0 and 30  
C. 12 and 36  
D. 6 and 18

### Q19. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A byte-addressed machine executes a 4-byte load instruction beginning at address 100. Its indirect PC-relative mode first sign-extends an 8-bit displacement, multiplies that signed displacement by 4, and adds it to the address immediately after the instruction. The 32-bit word at this intermediate address is the effective address of the operand. The displacement bits are 11111010. Memory words M[80]=120 and M[120]=7 are given. What is the effective address of the operand? All addresses are decimal; the machine uses two's-complement displacements.

A. 240  
B. 60  
C. 121  
D. 120

### Q20. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An8-bit ALU computes subtraction X−Y as X+(bitwise NOT Y)+1, retaining the low8 bits. Let X=10000000 and Y=00000001. Which combination is correct? Carry-out refers to the ninth bit of this addition, and signed overflow refers to two's-complement interpretation.

**Candidate answers**
I. Result01111111; carry-out0; signed overflow0.
II. Result01111111; carry-out1; signed overflow1.
III. Result10000001; carry-out1; signed overflow0.
IV. Result01111111; carry-out0; signed overflow1.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

On R(A,B,C,D), the functional dependencies are A→B, B→C and AC→D. How many attributes are in the closure of A under these dependencies?

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q22. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A frame appends one even-parity bit to its data. The receiver checks even parity over the entire received frame. Which corruption patterns are always detected?

**Candidate answers**
I. Exactly one flipped bit anywhere in the frame.
II. Exactly two flipped data bits.
III. Exactly three flipped bits anywhere in the frame.
IV. Any nonempty set of flipped bits.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A five-stage pipeline uses one single-ported memory for both IF instruction fetch and MEM data access. A load instruction is in MEM while a younger instruction needs IF during the same cycle. Even with complete data forwarding, what remains?

A. A structural conflict for the memory port.  
B. A mandatory arithmetic overflow.  
C. A control hazard caused by every load.  
D. No possible conflict because forwarding duplicates the memory port.

### Q24. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A2×2 real matrix has eigenvalues3 and−1. What is trace(A²)?

**Required precision:** Exact number.

A. 20  
B. 10  
C. 5  
D. 11

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A function f is continuous on[0,2] and twice differentiable on(0,2), with f(0)=0,f(1)=2,f(2)=0. Which statement must hold?

A. f''(x)<0 at every x in(0,2).  
B. f''(x)<0 at some x in(0,2).  
C. f''(1)=−4.  
D. f'(1)=0.

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Events A and B are independent, with P(A)=0.4 and P(B)=0.5. Find P(A | A∪B). Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.4286  
B. 0.2857  
C. 0.5714  
D. 0.7857

### Q27. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A compiler lowers `if (p) x=a; else x=b; use(x);` to a control-flow graph. What must both branch arms do before the common use(x) block?

**Candidate answers**
I. Define x along their respective paths.
II. Execute both assignments unconditionally in source order.
III. Eliminate the branch condition regardless of its value.
IV. Assign the same constant to x in every case.

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A rooted binary tree has eight leaves and three nodes with exactly one child. Every other non-leaf has exactly two children. How many vertices does the tree have in total?

**Required precision:** Integer.

A. 36  
B. 9  
C. 18  
D. 19

### Q29. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Recognizers M and N recognize L and its complement respectively. How can they be used to decide L on input w?

**Candidate answers**
I. Run M to completion before starting N.
II. Accept whenever either machine accepts.
III. Interleave their steps; accept if M accepts and reject if N accepts.
IV. Reject immediately unless M accepts in its first step.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q30. [1 Mark] [MCQ]

A system has one instance each of resources R and S. P holds R and waits for S. Q holds S and waits for R. Resources cannot be preempted, and neither process releases its held resource until its request is satisfied. Which single policy change directly breaks a necessary deadlock condition for this execution?

A. Raise both process priorities equally.
B. Allow a waiting process's held resource to be forcibly reclaimed.
C. Add another ready process that requests neither resource.
D. Increase the CPU clock frequency.

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Three processes have (arrival time, CPU burst length) A=(0,7), B=(2,4), C=(4,1), in time units. A single CPU uses preemptive shortest-remaining-time-first scheduling with zero switching overhead. No process performs I/O. Waiting time is completion time minus arrival time minus burst length. What is the average waiting time?

**Required precision:** Numeric value; integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q32. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A compiler considers replacing x/x by1 for a signed integer x. Division by zero is invalid; all other values here are representable. Which statements are correct?

**Candidate answers**
I. The rewrite preserves the defined result whenever x is known to be nonzero.
II. The rewrite preserves every possible runtime error when x may be zero.
III. A dominating condition that establishes x!=0, with no intervening modification, can justify the rewrite on that path.
IV. Textual repetition of x alone proves the rewrite safe for every input.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q33. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A parent opens an ordinary file and then forks. Neither process closes or duplicates the inherited descriptor. Which property is shared through the inherited open file description?

A. The processes' program counters.  
B. The file offset associated with those descriptors.  
C. Every local variable in their stacks.  
D. Their process identifiers.

### Q34. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Which word belongs to (ab|ba)* but not to (ab)*?

**Candidate answers**
I. abab
II. baab
III. aabb
IV. aaa

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q35. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For f(x)=ln x on [1,e], the mean value theorem gives a point c in (1,e) satisfying f′(c)=(f(e)−f(1))/(e−1). What is c, rounded to three decimal places?

**Required precision:** Number to 3 decimal places.

A. 3.436  
B. 0.859  
C. 2.718  
D. 1.718

### Q36. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Choose a signed two's-complement fixed-point format with a total of w bits and f fractional bits. It must represent every real input in [−15,15] by round-to-nearest without overflow, and its worst-case absolute rounding error must be at most 0.01. What is the smallest possible w?

**Required precision:** Integer bits.

A. 22  
B. 11  
C. 6  
D. 12

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A BST has root 40, with left child 20 and right child 60. Node 60 has left child 50; node 50 has left child 45; node 45 has right child 47. All unspecified child links are null. Delete key 40 by copying its inorder successor's key into the root and then removing the successor's original node, reconnecting that node's child if necessary. In the resulting tree, what are respectively the parent key of node 47 and the inorder successor key of 47?

A. (45,50)  
B. (50,50)  
C. (50,60)  
D. (45,60)

### Q38. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A sorted file occupies100 pages, each with100 records. A sparse index has one entry per data page, with20 entries fitting per index page. The index is searched in memory after all its pages are fetched once. A query then fetches one qualifying data page. With an empty buffer and no other reads, how many page reads occur?

**Required precision:** Integer.

A. 6  
B. 12  
C. 3  
D. 7

### Q39. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For A with rows (2,1,1),(4,3,3),(8,7,9), compute a Doolittle factorization A=LU without row swaps, where L has diagonal entries 1. What is L₃₂?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q40. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={aⁱbʲcᵏ : i,j,k≥0 and i=j or j=k}. Which statement is correct?

A. L is not context-free because it contains aⁿbⁿcⁿ.  
B. L is regular because the condition uses “or.”  
C. L is context-free, but its intersection with {aⁿbⁿcⁿ:n≥0} is not context-free.  
D. L is finite.

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A min-heap contains the array[1,3,2,8,7,4,5]. Replace its root by 9, then restore heap order by repeatedly swapping the current key with its smaller child while that child is smaller. How many swaps occur?

**Required precision:** Exact integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q42. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A disk's cylinders are 0 through 199. The head is at 80 and is moving upward. Pending requests are 20,90,150. Under SCAN, the head continues to cylinder 199 before reversing, even after serving 150. Stop measuring when the final pending request is served. What total distance is travelled?

**Required precision:** Integer cylinders.

A. 596  
B. 149  
C. 299  
D. 298

### Q43. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A binary floating-point format has finite precision. Ignore overflow and underflow, and assume its precision is at least four significant bits. Which real values can be represented exactly?

**Candidate answers**
I. 3/8
II. 1/10
III. 7/4
IV. 1/3

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q44. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

For 0≤t≤1, define I(t)=∫₀¹|x−t| dx. Which statements are correct?

**Candidate answers**
I. The minimum of I(t) is 1/4, attained only at t=1/2.
II. I(t)+I(1−t)≥1/2 for all t in [0,1].
III. ∫₀¹I(t) dt=1/2.
IV. The set of t in [0,1] satisfying I(t)≤5/16 is an interval of length 1/2.

A. I: invalid; II: valid; III: invalid; IV: valid  
B. I: valid; II: valid; III: valid; IV: valid  
C. I: valid; II: valid; III: invalid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q45. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In a compiler's constant lattice, a join keeps a constant only if all reachable incoming values agree. A block has incoming x=5 from one reachable predecessor and x=7 from an unreachable predecessor. Which statements are correct if reachability information is used?

**Candidate answers**
I. The unreachable predecessor need not force x to be nonconstant.
II. x may be propagated as5 at the block's entry.
III. Treating every syntactic predecessor as reachable can lose this optimization.
IV. Reachability information never affects constant propagation.

A. I: invalid; II: valid; III: valid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: invalid  
D. I: invalid; II: invalid; III: invalid; IV: valid

### Q46. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For observations0,0,4,10, first choose x to minimize the sum of absolute deviations from x. Among all such minimizers, choose x to minimize the sum of squared deviations. What value is selected?

**Required precision:** Exact decimal.

A. 7.0  
B. 1.8  
C. 3.5  
D. 4.5

### Q47. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A B+ tree has all leaves exactly two edges below the root. The root and each nonroot internal node have between two and four children. Each leaf stores between two and four data keys; internal separator copies are not data keys. Which pair gives the minimum and maximum possible data-key counts?

A. (4,16)  
B. (8,64)  
C. (8,32)  
D. (16,64)

### Q48. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A microprogram must start one memory read at the address in MAR, wait until READY=1, copy the returned data into MDR, and increment register R exactly once. All microinstruction operations execute once on every cycle in which that microinstruction is visited. A START pulse begins a transaction; issuing START again before completion begins an unwanted second transaction. READY remains 0 until the transaction completes and then remains 1 until the routine exits. Which routine meets the requirements for every finite memory latency? A branch tests READY at the end of its cycle.

A. U: START; R=R+1; if READY=0 goto U else goto V. V: MDR=DATA; exit.  
B. U: START; goto V. V: if READY=0 goto V else goto W. W: MDR=DATA; R=R+1; exit.  
C. U: START; goto V. V: R=R+1; if READY=0 goto V else goto W. W: MDR=DATA; exit.  
D. U: START; MDR=DATA; R=R+1; exit.

### Q49. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A contiguous memory region occupies addresses [0,240), where [u,v) has size v−u. Initially its free regions are [0,60), [100,180), and [200,240). Process X occupies [60,100), and process Y occupies [180,200). Compare first-fit and best-fit, each starting from this initial state.

First allocate A of size 50, then B of size 35. Next free X and A, leaving B and Y allocated. Every allocation takes space from the lowest-address end of its selected hole. First-fit searches from address 0 on each request; best-fit selects the smallest sufficient hole. Adjacent free regions are immediately coalesced, with no metadata overhead or compaction.

What are the largest single requests that can now be satisfied under (first-fit, best-fit), respectively?

**Candidate answers**
I. (100,180)
II. (100,100)
III. (180,180)
IV. (180,100)

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q50. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Let G be the multiplicative group of nonzero residues modulo 17. How many elements x in G satisfy x^4=1 but x²≠1? You may use that G is cyclic.

**Required precision:** Exact integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q51. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A byte-addressed machine has a16-bit address bus and a2KiB memory chip. The chip uses A10..A0 internally. Its select signal tests only A15=1 and A14=0; bits A13,A12,A11 are ignored. How many different processor addresses refer to any one fixed byte in this chip?

**Required precision:** Exact integer.

A. 16  
B. 4  
C. 9  
D. 8

### Q52. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A DFS of a directed graph has discovery/finish intervals u:[2,11] and v:[4,7]. Edge u→v exists but is not a tree edge. How is it classified under standard DFS edge categories?

**Candidate answers**
I. Back edge.
II. Forward edge.
III. Cross edge.
IV. Impossible because intervals may never nest.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q53. [2 Marks] [MCQ]

A PDA recognizing balanced parentheses pushes on '(' and pops on ')', rejecting a pop from an empty stack; it accepts only with empty stack after all input. A proposed modification accepts immediately whenever the stack first becomes empty after consuming at least one symbol, even if input remains. Which input demonstrates that the modification accepts a string rejected by the original?

A. (())
B. ()()
C. ())
D. ((

### Q54. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A circuit is a two-to-one multiplexer with output F=(NOT s)a+sb. Its select line is tied to its own data input a, so s=a. Which statements are correct?

**Candidate answers**
I. The resulting function is ab.
II. When a=0, changing b changes F.
III. The function can be implemented with one two-input NAND followed by one inverter.
IV. The resulting function is a OR b.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q55. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In a connected undirected weighted graph, an edge e is the unique heaviest edge of a cycle. Which statements are correct?

**Candidate answers**
I. e belongs to every MST.
II. e belongs to no MST.
III. Deleting e leaves the graph connected.
IV. The conclusion in B remains valid with “unique heaviest” replaced by merely “one of the heaviest”.

A. I: valid; II: valid; III: valid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: valid  
D. I: invalid; II: valid; III: valid; IV: invalid

### Q56. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Relations R(A,B) and S(B,C) each contain 100 tuples. B is a key of S, and every R.B value references an existing S.B value. No additional constraints are given. Under set semantics, how many tuples must R⋈S contain?

**Candidate answers**
I. 0
II. 100
III. 10,000
IV. It cannot be determined even under these constraints.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q57. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A DNS cache is initially empty. A successful lookup at time t stores an answer with TTL10 seconds and negligible lookup latency. It is usable for times s with t≤s<t+10; cache hits do not refresh TTL. Requests arrive at times0,4,9,10,19,20 seconds. Every miss is resolved immediately and cached under the same rule. How many upstream lookups occur?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q58. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A recovery system uses immediate updates with write-ahead logging, undo of uncommitted transactions and redo of committed transactions. Since the last checkpoint, the log records T1 changing X from 5 to 8, T2 changing Y from 4 to 9, and T1 committing. A crash occurs before T2 commits. Disk may contain either old or new values of each item. After recovery, what must (X,Y) be?

A. (5,4)  
B. (8,9)  
C. (8,4)  
D. (5,9)

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A tunnel adds an outer IPv4 header of20 bytes to each entire inner IPv4 packet. The path MTU for outer packets is1500 bytes. Outer fragmentation is prohibited. The inner packet has an IPv4 header of20 bytes and a TCP header of20 bytes, with no options. What is the largest TCP data payload, in bytes, that fits in one tunneled packet?

**Required precision:** Integer.

A. 2880  
B. 720  
C. 1440  
D. 1441

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed graph has edges s→a of weight 1, a→b of weight 0, b→a of weight 0, and b→t of weight 2. Walks may revisit vertices. Which statement is correct?

A. The shortest s-to-t walk weight is unbounded below.  
B. The shortest weight is 3 and only one shortest walk exists.  
C. The shortest weight is 3 and infinitely many shortest walks exist.  
D. No walk from s to t exists.

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A process has four virtual pages numbered 0–3, initially absent from memory, and two frames. It accesses pages 0,1,0,2,1,3,1,2 in that order. Under optimal offline page replacement, what is the minimum possible number of page faults?

**Required precision:** Integer.

A. 10  
B. 3  
C. 6  
D. 5

### Q62. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A stack log uses symbol a for a push and b for a pop. A valid log starts with an empty stack, never pops an empty stack, and ends with an empty stack. Let L contain exactly the valid logs in which neither aaa nor bbb occurs as a substring; the empty log belongs to L. Which statement about L is correct?

A. L is regular because no run has more than two identical operations.  
B. L is not regular, but a deterministic pushdown automaton can recognize it.  
C. L is context-free, but no deterministic pushdown automaton can recognize it.  
D. L is not context-free because the run restriction and the stack restriction must both be checked.

### Q63. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In the code below, execution starts at line1 and exits after line6. Only z is observed on exit. Expressions have no side effects.

```text
1: x = 1
2: if flag goto 5
3: y = x + 1
4: goto 6
5: y = 4
6: z = y
```

Which statements are correct about ordinary may-liveness analysis?

**Candidate answers**
I. x is live immediately after line2.
II. x is live immediately before line5.
III. y is live immediately before line6.
IV. Line1 is dead because one path does not use x.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q64. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A cache miss adds 40 cycles to a base execution of one cycle per instruction. An optimization reduces misses per instruction from 0.04 to 0.01 but increases the instruction count by 20%. Clock period is unchanged and no penalties overlap. What is the ratio of old execution time to new execution time? Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 1.5476  
B. 3.0952  
C. 0.7738  
D. 2.5476

### Q65. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A singly linked list must be reversed in place. The code maintains pointers prev,cur,next and uses three assignments per iteration after saving next=cur.next. Which order preserves access to the remaining unreversed suffix?

**Candidate answers**
I. cur=cur.next; cur.next=prev; prev=cur
II. cur.next=prev; prev=cur; cur=next
III. prev=cur; cur=next; cur.next=prev
IV. cur.next=next; prev=next; cur=prev

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

## ANSWER KEY — MOCK TEST 037

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | NAT | 1 | 0.6667 (accepted range 0.66665–0.66675) |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 4.25 |
| 5 | MSQ | 1 | A, C |
| 6 | MCQ | 2 | D |
| 7 | NAT | 2 | 13 |
| 8 | NAT | 2 | 2.6667 (accepted range 2.66665–2.66675) |
| 9 | MSQ | 2 | A, B |
| 10 | NAT | 2 | 25 |
| 11 | MCQ | 1 | A |
| 12 | MCQ | 1 | A |
| 13 | MSQ | 1 | A, B, D |
| 14 | MCQ | 1 | D |
| 15 | MSQ | 1 | A, C, D |
| 16 | MCQ | 1 | B |
| 17 | MCQ | 1 | A |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 1 | A, B, C |
| 20 | MCQ | 1 | C |
| 21 | MCQ | 1 | B |
| 22 | MCQ | 1 | C |
| 23 | MSQ | 1 | B, C, D |
| 24 | MCQ | 1 | B |
| 25 | MSQ | 1 | A, C, D |
| 26 | MCQ | 1 | C |
| 27 | MCQ | 1 | C |
| 28 | MCQ | 1 | C |
| 29 | MCQ | 1 | D |
| 30 | MCQ | 1 | B |
| 31 | MCQ | 1 | D |
| 32 | MCQ | 1 | C |
| 33 | MSQ | 1 | A, C, D |
| 34 | MCQ | 1 | C |
| 35 | MSQ | 1 | A, B, C |
| 36 | MCQ | 2 | B |
| 37 | MSQ | 2 | A, C, D |
| 38 | MCQ | 2 | A |
| 39 | MSQ | 2 | A, B, C |
| 40 | MSQ | 2 | A, B, D |
| 41 | MSQ | 2 | A, C, D |
| 42 | MSQ | 2 | A, B, C |
| 43 | MCQ | 2 | D |
| 44 | MCQ | 2 | C |
| 45 | MCQ | 2 | B |
| 46 | MSQ | 2 | A, B, D |
| 47 | MSQ | 2 | A, C, D |
| 48 | MSQ | 2 | A, C, D |
| 49 | MCQ | 2 | B |
| 50 | MSQ | 2 | A, B, C |
| 51 | MCQ | 2 | D |
| 52 | MCQ | 2 | B |
| 53 | MCQ | 2 | C |
| 54 | MCQ | 2 | C |
| 55 | MCQ | 2 | D |
| 56 | MCQ | 2 | B |
| 57 | MSQ | 2 | A, B, C |
| 58 | MSQ | 2 | A, B, D |
| 59 | MCQ | 2 | C |
| 60 | MSQ | 2 | A, B, D |
| 61 | MCQ | 2 | D |
| 62 | MSQ | 2 | A, C, D |
| 63 | MCQ | 2 | D |
| 64 | MCQ | 2 | A |
| 65 | MCQ | 2 | D |
