# GATE CS 2027 — Full-Length Mock Test 086

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

### Q1. [1 Mark] [NAT]

An integer x is in {1,2,3,4}. Exactly two of these statements are true: x≤2; x is even; x=3. What is x?

**Answer format:** Integer.

### Q2. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A planar figure is reflected across the x-axis and then across the line y=x. Which coordinate rule describes the combined transformation?

A. (x,y)→(−y,x)  
B. (x,y)→(y,−x)  
C. (x,y)→(−x,−y)  
D. (x,y)→(x,−y)

### Q3. [1 Mark] [MCQ]

A study reports that among applicants who passed a competitive screening, experience and examination score were negatively associated. The screening favoured applicants with either strong experience or a high score. Which conclusion is justified by this description alone?

A. Experience causes lower examination scores in all applicants.
B. Restricting attention to screened applicants may create an association absent in the full applicant pool.
C. The screening must have ignored experience.
D. No applicant can have both strong experience and a high score.

### Q4. [1 Mark] [NAT]

Six distinct people A,B,C,D,E,F sit around a circular table with six equally spaced seats. Arrangements differing only by rotation are identical; mirror images are distinct. A and B must sit opposite one another, and C and D must be adjacent. How many arrangements satisfy both restrictions?

**Answer format:** Exact integer.

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Twenty-five observations fall in intervals [0,10), [10,20), [20,30), [30,40), with respective frequencies 4,6,10,5. Which interval necessarily contains the median?

A. [0,10)  
B. [10,20)  
C. [20,30)  
D. [30,40)

### Q6. [2 Marks] [NAT]

A square sheet occupies 0 <= x <= 8 and 0 <= y <= 8. Fold its left half onto its right half along x=4. Next fold its bottom half onto its top half along y=4. Punch small point-like holes through all layers at (5,6) and (6,5) in the folded sheet. After fully unfolding, how many distinct holes lie on the line y=x+1? Ignore hole diameter and sheet thickness.

**Answer format:** Numeric value; integer.

### Q7. [2 Marks] [MCQ]

A survey includes 120 people. Seventy read newspaper A, sixty read newspaper B, and twenty read neither. Among those who read at least one, what fraction read exactly one?

A. 3/10
B. 7/10
C. 3/4
D. 5/6

### Q8. [2 Marks] [NAT]

A fair six-sided die is rolled twice independently. Given that the larger of the two results is4, what is the probability that their sum is even? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q9. [2 Marks] [MCQ]

A policy states: “Unless the permit is renewed before Monday, the pilot must stop on Monday. Renewal alone does not authorize expansion; an independent review is also required.” Assume the policy is followed and the pilot continues on Tuesday. Which conclusion is justified?

A. An independent review must already have authorized expansion.  
B. The permit was renewed before Monday, but authorization for expansion cannot be inferred.  
C. Continuing the pilot automatically authorizes expansion.  
D. The permit could have remained unrenewed because an independent review replaces renewal.

### Q10. [2 Marks] [NAT]

For positive real x, suppose log2(x)·log4(x)=8. What is the product of all positive solutions x?

**Answer format:** Exact number.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Which language is regular?

A. {aⁿbⁿ : n≥0}
B. {aᵖ : p is prime}
C. {aⁿbᵐ : n,m≥0 and n is even}
D. {ww : w∈{0,1}*}

### Q12. [1 Mark] [MCQ]

Records initially occur as (a,2),(b,1),(a,1),(b,2), where the first component is a letter key and the second a numeric key. First stably sort by the letter in ascending order, and then stably sort by the number in ascending order. What is the final sequence?

A. (a,1),(a,2),(b,1),(b,2)
B. (b,1),(a,1),(a,2),(b,2)
C. (a,1),(b,1),(a,2),(b,2)
D. (b,1),(a,1),(b,2),(a,2)

### Q13. [1 Mark] [MSQ]

A microprogrammed controller has a control-store address register, a microinstruction register, and combinational next-address logic. A fetched microinstruction specifies both datapath controls and a conditional next address. Which statements hold?

A. A datapath status flag can influence selection of the next microinstruction.
B. The control store must be writable during every machine instruction.
C. Several compatible datapath control signals can be asserted by the same microinstruction.
D. Every machine instruction necessarily executes the same number of microinstructions.

### Q14. [1 Mark] [NAT]

Take two vertex-disjoint triangles and add one edge joining a vertex of one triangle to a vertex of the other. What is the minimum number of edges whose removal makes the resulting graph bipartite?

**Answer format:** Exact integer.

### Q15. [1 Mark] [NAT]

How many subsets S of {1,2,3,4,5,6} satisfy the rule that, for each i in {1,2,3}, exactly one of i and i+3 belongs to S, and the sum of elements of S is even?

**Answer format:** Integer.

### Q16. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relation R(A,B,C,D) has dependencies A→B, AB→C, C→D, A→D. Which statements hold?

A. B is extraneous in the left side of AB→C.  
B. A→D can be removed without changing the set of implied dependencies.  
C. C→D can be removed without changing the set of implied dependencies.  
D. A is a candidate key.

### Q17. [1 Mark] [MCQ]

A proposed proof applies the regular-language pumping lemma to L={0ⁿ1ⁿ:n≥0}. After choosing w=0ᵖ1ᵖ, it picks the particular decomposition x=ε,y=0,z=0^(p−1)1ᵖ and shows that this decomposition fails when pumped. What must be repaired to make the argument valid?

A. The proof must show failure for every decomposition satisfying |xy|≤p and |y|>0.
B. The proof must show that L is finite.
C. Pumping down is forbidden; only pumping up is permitted.
D. The selected word must have length less than p.

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

L is a Turing-recognizable language, and the halting problem has a computable many-one reduction to L. Which statements must hold?

**Candidates**

**I.** L is undecidable.

**II.** L is not Turing-recognizable.

**III.** The complement of L is not Turing-recognizable.

**IV.** The reduction gives a total decision procedure for L.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q19. [1 Mark] [MCQ]

A language passes a scalar argument by value. A callee assigns a new scalar value to its parameter but does not access the caller's storage through any pointer or reference. Which statement is correct?

A. The assignment necessarily changes the caller's variable.
B. The assignment changes the callee's parameter value without thereby changing the caller's scalar variable.
C. Pass-by-value means the parameter cannot be assigned.
D. Pass-by-value requires the caller and callee to share one parameter storage cell.

### Q20. [1 Mark] [NAT]

A three-address-code representation allows each arithmetic instruction to contain exactly one binary operation and one assignment. Loads and copies are not needed; the operands a,b,c,d are already available. No algebraic reassociation is allowed. What is the minimum number of arithmetic instructions required to compute (a+b)*(c−d)+(a+b), reusing repeated subexpressions?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

What is the coefficient of x⁷ in the formal power series 1/((1−x)(1−x²))?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

Routers A,B,C use synchronous distance-vector updates for destination C. Link costs are A–B=1, B–C=1 and A–C=10. Initially routes are converged. Link B–C fails immediately before round 1. In every round each router recomputes its distance using its still-working links and the neighbours' distances from the end of the preceding round; C always advertises 0. No split horizon, poison reverse or triggered intermediate updates are used. What distance does A advertise after round 2?

**Answer format:** Numeric value; integer.

### Q23. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An IPv4 fragment has a 20-byte header and MF=1. Which total-length values can meet the eight-byte payload-alignment requirement? Ignore link MTU limits for this question.

A. 532  
B. 540  
C. 552  
D. 556

### Q24. [1 Mark] [NAT]

An array initially contains[1,2,3,4,5]. First copy its first four entries to positions1 through4, using zero-based indices and semantics as if the source were saved in a temporary array before writing. Then similarly copy positions2 through4 to positions0 through2. What is the sum of all five final entries?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

For Boolean variables a,b,c, how many assignments satisfy (a OR b) AND ((NOT a) OR c) while making b OR c false?

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

For propositions p and q, which formulas are logically equivalent to NOT(p implies q)?

A. p AND NOT q.
B. NOT p OR q.
C. p AND (p XOR q).
D. NOT p AND q.

### Q27. [1 Mark] [NAT]

A 3×3 matrix A has det(A)=−2. B is formed by interchanging A's first two rows, then multiplying the third column by 3. Find det(B).

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A routing table contains destination prefixes 0.0.0.0/0, 172.16.0.0/16, 172.16.32.0/20 and 172.16.40.0/24, each with a different next hop. For destination 172.16.41.7, what prefix length is selected by longest-prefix matching?

**Answer format:** Integer prefix length.

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A doubly linked list has adjacent non-sentinel nodes P,X,N. Removing X while preserving the list requires which neighbour updates?

A. P.next=N and N.prev=P.  
B. P.prev=N and N.next=P.  
C. P.next=X and N.prev=X.  
D. P.next=P and N.prev=N.

### Q30. [1 Mark] [MCQ]

A sequential detector emits a pulse when the latest three input bits are 101, allowing overlapping matches. It reads 10101 from left to right, starting with no previous bits. How many pulses are emitted?

A. 1
B. 2
C. 3
D. 5

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a four-variable Karnaugh map, why are columns labelled 00,01,11,10 rather than 00,01,10,11?

A. Every pair of horizontally adjacent columns, including wraparound, then differs in exactly one bit.  
B. Binary numbers must always be written in Gray-code order.  
C. The order changes the function's truth table values.  
D. Adjacent columns must differ in both bits.

### Q32. [1 Mark] [MSQ]

A condition variable wait atomically releases its associated mutex and blocks, and reacquires the mutex before returning. Wakeups do not guarantee the application's predicate is true. Which statements are correct?

A. The predicate should be rechecked after returning from wait.
B. A single if test before wait is sufficient for every execution.
C. Another thread can change the predicate before the awakened thread reacquires the mutex.
D. Returning from wait means the mutex remains released under this specification.

### Q33. [1 Mark] [NAT]

A disk has cylinders 0 through 99. At time 0, its head is at cylinder 50, moving toward larger numbers, with requests pending at 70, 90 and 10. Seek speed is one cylinder per time unit; service and reversal take zero time. A new request for cylinder 95 arrives at time 45. LOOK continues in its current direction while any request is pending ahead, and otherwise reverses. New arrivals join the queue without causing an early reversal. What total head movement serves all four requests?

**Answer format:** Numeric value; integer.

### Q34. [1 Mark] [NAT]

A byte-addressed 64 KiB memory is built from 16 KiB × 8-bit chips. Address lines not connected to a chip's internal address pins select the chip through a decoder. How many address bits are used for chip selection?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A directed acyclic graph on A,B,C,D has edges A→C, B→C, B→D and no others. How many topological orderings does it have?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

Inputs 1,2,3,4 enter a single stack in that order. Each input is pushed exactly once and each is popped exactly once; pops produce an output permutation. How many distinct output permutations are possible if the stack may never hold more than two items?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary tree has distinct labels. Its preorder is A,B,D,E,C,F and its inorder is D,B,E,A,C,F. Which postorder is correct?

A. D,E,B,F,C,A  
B. D,B,E,F,C,A  
C. E,D,B,C,F,A  
D. D,E,F,B,C,A

### Q38. [2 Marks] [MSQ]

Two private hosts, 10.0.0.1 and 10.0.0.2, each initiate a TCP connection from local port 5000 to 203.0.113.8 port 443. A NAT gateway uses the single public IPv4 address 198.51.100.6 and assigns public source port 41001 to the connection from 10.0.0.1 and public source port 41002 to the connection from 10.0.0.2. Packets are unfragmented. Which statements are correct for this port-translating NAT?

A. A reply arriving at public port 41002 can be mapped back to 10.0.0.2 port 5000.  
B. The remote server sees both connections as originating from the respective private IPv4 addresses.  
C. Translating the source IPv4 address of an outgoing packet requires updating its IPv4 header checksum.  
D. Translating the source IPv4 address and TCP source port requires updating the TCP checksum because both affect its checksum calculation.

### Q39. [2 Marks] [NAT]

Integers x range over all four-bit signed values −8 through 7. Evaluate `y=(2*x)/2` by first multiplying with four-bit two's-complement wraparound, then dividing the resulting signed value by two using exact division on even integers. For how many x values is y=x?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

Over alphabet {0,1}, accept a word exactly when it contains exactly one position at which two adjacent symbols are equal. Overlapping adjacent pairs count separately: 000 has two such positions. What is the number of states in the minimal complete DFA, including a rejecting sink?

**Answer format:** Integer.

### Q41. [2 Marks] [MSQ]

In a tabular Boolean minimization, a dash in a four-bit cube denotes a free variable. The ON-set is {0,1,2,3,8,9}, the don't-care set is {10}, and all remaining minterms are OFF. Which operations are valid? A combined cube must contain no OFF minterm.

A. Combine 000- and 001- to obtain 00--.
B. Combine 00-- and 100- to obtain -0--.
C. Combine 00-0 and 10-0 to obtain -0-0.
D. Combine -00- and -010 to obtain -0--.

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider the following code. Each call to more() returns an arbitrary Boolean value and does not change x. Consider only terminating executions. A conventional constant-propagation analysis tracks a single constant per variable or “not constant”; it joins distinct incoming constants as “not constant” and computes a fixed point over the loop.

```text
x = 1
while more():
    x = 2
y = x
```

Which statements are correct?

**Candidates**

**I.** At the loop header, this analysis establishes x=1 at its fixed point.

**II.** Immediately after the body assignment, this analysis establishes x=2.

**III.** On every terminating execution, the final y is 2.

**IV.** Replacing the while loop with a do-while loop executing x=2 before its first call to more() removes final value y=1 from the possible outcomes.

A. I and IV  
B. II and III  
C. II and IV  
D. III and IV

### Q43. [2 Marks] [MCQ]

A full binary recursion tree has n=2^k leaves at depth k, with the root at depth0. Every call at depth d allocates and initializes2^d buffer cells, retains them while processing its children sequentially in depth-first order, then frees them before returning. Leaves also allocate their stated buffers. What are the tight orders of total cell initializations and maximum simultaneously live buffer cells, respectively?


A. (Θ(n²),Θ(n))
B. (Θ(n log n),Θ(n))
C. (Θ(n²),Θ(n²))
D. (Θ(n log n),Θ(log n))

### Q44. [2 Marks] [NAT]

Processes P and Q arrive at time 0, with P initially ahead of Q. Round-robin scheduling uses a quantum of 2 time units and zero context-switch cost. P executes a CPU burst of 2, performs I/O for 3, then executes a CPU burst of 2 and terminates. Q has one CPU burst of 5. A process finishing I/O joins the tail of the ready queue without preempting the running process. A quantum-expired process also joins the tail. What is the sum of their waiting times in the ready queue? I/O time is not waiting time.

**Answer format:** Integer time units.

### Q45. [2 Marks] [MCQ]

A process's virtual address space contains a mapped region that is much larger than currently used physical memory. Pages are allocated on first write. Which statement is correct?

A. Every reserved virtual page necessarily already occupies a private physical frame.
B. Reserving address space and committing physical backing may occur at different times.
C. Virtual addresses must equal physical addresses in this arrangement.
D. The process cannot ever fault on a valid mapped virtual address.

### Q46. [2 Marks] [MSQ]

Let f(x)=min(x²,2−x²) on the interval [−2,2]. Which statements are correct?

A. The maximum value is 1, attained at both x=−1 and x=1.
B. The minimum value is −2.
C. f is differentiable at x=0.
D. f is differentiable at x=1.

### Q47. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A full-adder sum bit is implemented using a 4-to-1 mux with select bits a,b and remaining input c. Which data inputs (D0,D1,D2,D3) are correct?

A. (0,c,c,1)  
B. (c,c′,c′,c)  
C. (c′,c,c,c′)  
D. (0,0,1,1)

### Q48. [2 Marks] [NAT]

Independent X,Y are uniform on [0,1]. Find E[X | Y>X²].

**Answer format:** Exact finite decimal.

### Q49. [2 Marks] [MSQ]

A synchronous three-bit counter has transitions 0→1→2→3→4→5→0, and both unused states 6 and 7 transition to 0. Bits are q2q1q0 in binary. Which statements are correct?

A. From every initial bit pattern, the counter eventually enters the six-state cycle.  
B. An unused state remains unchanged until an external reset.  
C. On the steady cycle, q2 is 1 for one third of the clock intervals.  
D. On the steady cycle, q0 alternates at every clock edge.

### Q50. [2 Marks] [NAT]

For matrix-chain multiplication, four matrices have dimensions 5×10,10×3,3×12,12×5. Count scalar multiplications in the usual way: multiplying p×q by q×r costs pqr. What is the minimum scalar-multiplication cost for their product?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

A segmented memory uses separate base and limit values for each segment. A byte access of length L at offset o is valid iff o≥0 and o+L≤limit. Segment2 has base1000 and limit100. A four-byte word is requested at offset98. How many bytes from the requested word can the processor access before trapping if the whole access is checked atomically before any memory read?

**Answer format:** Exact integer.

### Q52. [2 Marks] [NAT]

A B+ tree has maximum three keys per leaf and maximum four children per internal node. Leaves hold data keys only. Insert into a leaf in sorted order; when it reaches four keys, split into two leaves with two keys each and copy the smallest key of the right leaf upward. Initially the root has separator30 and two leaves [10,20] and [30,40,50]. Insert35, then45, then15. No deletion occurs. How many separator keys are in the root at the end?

**Answer format:** Integer.

### Q53. [2 Marks] [MCQ]

A singly linked list is 1→2→3→4→5→NULL. Pointers p and q initially refer to nodes 2 and 4. Execute the following assignments in the displayed order, with t a temporary pointer:

```text
t = p.next
p.next = q.next
q.next = t
```

Starting at node 1 afterward, what happens when next links are followed?

A. The traversal is 1,2,5 and then NULL.
B. The traversal is 1,2,3,4,5 and then NULL.
C. The traversal is 1,2,4,3,5 and then NULL.
D. The traversal enters a cycle containing node 1.

### Q54. [2 Marks] [NAT]

Finite sets A and B have sizes3 and4. How many ordered pairs of functions f:A→B and g:B→A satisfy g(f(a))=a for every a in A?

**Answer format:** Integer.

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A schedule has operations in this order: w1(X), r2(X), w2(Y), c2, a1. Here ci commits transaction i and ai aborts it; no earlier versions of X are read. Which statements are correct?

**Candidates**

**I.** Transaction 2 reads an uncommitted value.

**II.** The schedule is recoverable.

**III.** A cascading-abort requirement arises, but transaction 2 has already committed.

**IV.** The schedule is strict.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q56. [2 Marks] [NAT]

In an idealized TCP congestion-avoidance model, cwnd starts at 4 MSS. Each complete loss-free RTT acknowledges the entire current window, then cwnd increases by exactly 1 MSS. The receiver window never limits transmission. How many MSS are transmitted over the first four RTTs? Count each round's transmitted data before its increase.

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two threads share ordinary Boolean flags f0=f1=false. Under sequential consistency, thread i sets fi=true, then busy-waits while the other flag is true, enters its critical section, and finally sets fi=false. Reads and writes of each flag are atomic. Which statements are correct?

**Candidates**

**I.** Both threads can be stuck waiting forever even if both are scheduled fairly.

**II.** Both threads can be simultaneously in their critical sections.

**III.** Mutual exclusion holds.

**IV.** Replacing the flags with volatile flags alone necessarily prevents the waiting failure.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q58. [2 Marks] [NAT]

In the following control flow, p is an unchanged input Boolean. All named values use mathematical integer semantics.

```text
Entry: a = 0; goto Loop
Loop:  b = a + 1
       if p goto Again else goto Exit
Again: a = b; goto Loop
Exit:  return a
```

Under standard backward may-liveness analysis, how many named variables are live immediately after b=a+1 and before the conditional test in Loop?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A write-back, write-allocate cache has initially empty lines, with16 bytes per block. A processor writes one byte at each of addresses0,1,16,17. The cache has enough space for both blocks and evicts neither during these stores. It is then flushed, writing every dirty block once. Ignoring metadata and counting full-block transfers, how many bytes move between cache and memory in total?

**Answer format:** Exact integer.

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP receiver calls a blocking `recv` requesting up to 100 bytes. The peer has sent 40 bytes, which are available, but has not closed the connection. Assuming the API allows a positive short return, which application behaviour is correct?

A. Treat a return of 40 as necessarily indicating end-of-file.  
B. Accumulate received bytes according to the application's framing rule rather than assuming each receive corresponds to one send or fills the requested count.  
C. Assume every return of fewer than 100 bytes is a network corruption.  
D. Assume TCP inserts an application-message boundary after each send.

### Q61. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Under basic timestamp ordering, x initially has read timestamp 0 and write timestamp 0. T10 with timestamp 10 successfully reads x. T5 with timestamp 5 then attempts to write x. Which action is required? Thomas's write rule, if considered, may ignore an obsolete write only when it does not violate the read-timestamp test.

A. Accept the write because x has never been written.  
B. Ignore the write under Thomas's rule without aborting T5.  
C. Reject the write and abort T5 because its timestamp is below x's read timestamp.  
D. Decrease x's read timestamp to 5 and accept.

### Q62. [2 Marks] [NAT]

A real2×2 matrix A has eigenvalues2 and3. What is det(A²−5A+7I)?

**Answer format:** Exact number.

### Q63. [2 Marks] [MSQ]

A nondeterministic PDA can make epsilon moves and may have infinite branches. Which statements about searching its computation tree are true?

A. Breadth-first search will eventually find an accepting computation if one exists with finitely many transitions, assuming finite branching.
B. Naive depth-first search that never backtracks from an infinite branch always finds every accepting computation.
C. An epsilon loop can trap such a depth-first search despite another accepting branch.
D. Breadth-first search necessarily halts and rejects every nonmember of every context-free language without any further algorithmic construction.

### Q64. [2 Marks] [NAT]

An initially empty sparse file has an inode with four direct block pointers and one single-indirect pointer. Blocks are1024 bytes and pointers are4 bytes. A write of one byte at file offset6144 allocates only the necessary data block and any necessary indirect block. Unwritten holes need no data blocks. Exclude the already existing inode. How many bytes of newly allocated blocks are needed?

**Answer format:** Integer.

### Q65. [2 Marks] [MSQ]

Define L={aⁱbʲ:i,j≥0 and i≠j}. Which statements are correct?

A. L is context-free.
B. L is regular.
C. The complement of L within a*b* is {aⁿbⁿ:n≥0}.
D. ε belongs to L.

---

## ANSWER KEY — MOCK TEST 086

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 2 |
| 2 | MSQ | 1 | B, C, D |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 8 |
| 5 | MSQ | 1 | A, B, D |
| 6 | NAT | 2 | 2 (exact) |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 0.4286 (accepted range 0.42855–0.42865) |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 1 |
| 11 | MCQ | 1 | C |
| 12 | MCQ | 1 | C |
| 13 | MSQ | 1 | A, C |
| 14 | NAT | 1 | 2 |
| 15 | NAT | 1 | 4 |
| 16 | MCQ | 1 | C |
| 17 | MCQ | 1 | A |
| 18 | MCQ | 1 | C |
| 19 | MCQ | 1 | B |
| 20 | NAT | 1 | 4 |
| 21 | NAT | 1 | 4 |
| 22 | NAT | 1 | 4 (exact) |
| 23 | MCQ | 1 | C |
| 24 | NAT | 1 | 16 |
| 25 | NAT | 1 | 0 |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 6 |
| 28 | NAT | 1 | 20 |
| 29 | MSQ | 1 | B, C, D |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | B, C, D |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 205 (exact) |
| 34 | NAT | 1 | 2 |
| 35 | NAT | 1 | 5 |
| 36 | NAT | 2 | 8 |
| 37 | MSQ | 2 | B, C, D |
| 38 | MSQ | 2 | A, C, D |
| 39 | NAT | 2 | 8 |
| 40 | NAT | 2 | 6 |
| 41 | MSQ | 2 | A, C |
| 42 | MCQ | 2 | C |
| 43 | MCQ | 2 | A |
| 44 | NAT | 2 | 5 |
| 45 | MCQ | 2 | B |
| 46 | MSQ | 2 | A, B, C |
| 47 | MSQ | 2 | A, C, D |
| 48 | NAT | 2 | 0.375 |
| 49 | MSQ | 2 | A, C, D |
| 50 | NAT | 2 | 405 |
| 51 | NAT | 2 | 0 |
| 52 | NAT | 2 | 2 |
| 53 | MCQ | 2 | A |
| 54 | NAT | 2 | 72 |
| 55 | MCQ | 2 | C |
| 56 | NAT | 2 | 22 |
| 57 | MCQ | 2 | C |
| 58 | NAT | 2 | 3 |
| 59 | NAT | 2 | 64 |
| 60 | MSQ | 2 | A, C, D |
| 61 | MSQ | 2 | A, B, D |
| 62 | NAT | 2 | 1 |
| 63 | MSQ | 2 | A, C |
| 64 | NAT | 2 | 2048 |
| 65 | MSQ | 2 | A, C |
