# GATE CS — Additional Practice Set 013

**Questions:** 50  
**Maximum marks:** 74

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An IPv4 packet carrying a TCP segment crosses one router between two Ethernet LANs. The router performs ordinary forwarding, with no NAT, fragmentation or tunnelling. Its incoming TTL is greater than 1. Which statements are correct about the outgoing packet/frame?

**Candidates**

**I.** The destination IPv4 address is unchanged.

**II.** The destination Ethernet address must be unchanged.

**III.** The IPv4 TTL is one less than on arrival.

**IV.** The TCP destination port is replaced by the router's port number.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q2. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A component is faulty with probability 1/4. Each test is positive with probability 4/5 for a faulty component and 1/10 for a sound component. Repeated results are conditionally independent given the component's status. Testing stops at the first negative result or after three tests, whichever occurs first. N is the number of tests performed. Which statements are correct?

A. E[N]=577/400.  
B. P(faulty | N=3)=512/515.  
C. Given that exactly two positive results were observed before a negative result, the probability of a faulty component is 128/155.  
D. Given that the first result was positive and the stopping result was negative, the probability of a faulty component is 32/65.  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The following basic block uses exact mathematical integers and ordinary scalar variables, with no aliases or externally visible intermediate states. All three final variable values must be preserved. Which replacement is equivalent for every initial value of b and c?
```text
a = b + c
b = a - c
c = a - b
```

A. a = b + c  
B. a = b + c; b = c  
C. a = b + c; c = a  
D. a = b + c; b = a; c = 0  

### Q4. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Over alphabet {a,b,c}, define

```text
L = { a^i b^j c^k : i,j,k >= 0 and (i=j or j=k) }
R = { a^i b^j c^k : i,j,k >= 0 and j<=2 }
S = { a^n b^m c^n : n,m >= 0 }.
```

All exponents are integers, and L minus R denotes set difference. Which statements are correct?

**Candidates**

**I.** L intersect R is regular.

**II.** L minus R is regular.

**III.** L minus R is context-free.

**IV.** L intersect S is context-free.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A byte-addressed system maps four 4 KiB×8 memory chips consecutively to addresses 0x8000–0xBFFF. Chips are numbered 0 through 3 in increasing base-address order. Which pair gives the chip number and the offset within that chip for address 0x9ABC?

A. (0,0x9ABC)  
B. (2,0xABC)  
C. (1,0x1ABC)  
D. (1,0xABC)  

### Q6. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The block below uses exact integer arithmetic, ordinary scalars and no aliases. An optimizer may share identical expressions, treating multiplication as commutative, and remove unnecessary copies. It must preserve all returned values. It may not use distributivity or introduce operations other than the displayed additions and multiplications. What are the minimum numbers of multiplications and additions, respectively?

```text
a = x * y
b = y * x
c = a + z
d = b + z
x = x + 1
e = x * y
f = e + z
return (c,d,f)
```

A. (1,2)  
B. (2,2)  
C. (2,3)  
D. (3,3)  

### Q7. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C) has functional dependencies A→B and B→C, and no others except their consequences. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless.  
B. The decomposition preserves the given dependencies.  
C. The original R is in BCNF.  
D. Both component schemas are in BCNF.  

### Q8. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

On a Unix-style file system, an ordinary file has two hard-link names and an open descriptor. Both names are unlinked, but the descriptor remains open and has suitable access permission. No other references exist. Which statements are correct?

**Candidates**

**I.** Reading the file's data through the open descriptor remains possible.

**II.** The file's data blocks must be freed immediately after the second unlink.

**III.** Opening either removed pathname fails unless a new directory entry is created there.

**IV.** The inode's hard-link count remains 1 because an open descriptor is a hard link.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q9. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For relation R(A,B,C), the functional dependencies are exactly those implied by AB→C and C→A. Which attribute sets are candidate keys?

**Candidates**

**I.** AB

**II.** AC

**III.** BC

**IV.** C

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the schedule `w1(x), w2(x), w1(x), w2(y), r3(y), w3(z)`, followed by commits of all three transactions. The subscripts identify transactions; writes are blind writes of distinct values. There are no other reads or writes. For view equivalence, preserve every read-from relationship and the identity of the final writer of each item. Which pair correctly states whether the schedule is conflict serializable and the number of serial transaction orders view equivalent to it?

A. Not conflict serializable; 2 orders  
B. Conflict serializable; 2 orders  
C. Not conflict serializable; 0 orders  
D. Conflict serializable; 1 order  

### Q11. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Five variables a,b,c,d,e have an interference graph that is exactly the cycle a–b–c–d–e–a. Two variables connected by an edge cannot share a register; there are no preassigned registers, spills, or other constraints. Which pair gives the size of the largest clique and the minimum number of registers?

A. (2,2)  
B. (2,3)  
C. (3,3)  
D. (3,5)  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A scheduler assigns smaller numeric priority to more urgent jobs. Every waiting job's priority decreases by one per time unit, while a running job's priority is unchanged. Which problem is this aging rule principally intended to mitigate?

A. Deadlock caused by inconsistent mutex acquisition order.  
B. Starvation of low-priority jobs under repeated arrivals of more urgent work.  
C. Internal fragmentation in a page.  
D. Loss of a dirty cache line during DMA.  

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The new procedure reduced measurement variability but did not change the mean measurement.” Which conclusion is supported?

A. Every new measurement equals the old mean.  
B. New measurements are less dispersed under the reported variability measure.  
C. The mean measurement became zero.  
D. The old procedure must have been biased.  

### Q14. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An n-bit ripple-carry adder has a carry dependency from each bit to the next. Each stage's carry propagation takes one time unit; inputs are available at time zero. Ignore sum-output delays. Which statements are correct?

**Candidates**

**I.** The final carry may require n time units.

**II.** All carries necessarily settle within one time unit because the stages are physically parallel.

**III.** Grouping carry logic using additional gates can reduce carry depth compared with a ripple chain.

**IV.** Increasing n never changes worst-case carry delay.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q15. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic machine on each fixed input has only finitely many possible configurations, and its full transition relation can be simulated effectively. Which statements are correct?

**Candidates**

**I.** Repeating an identical nonhalting configuration proves that the subsequent computation loops.

**II.** Simulating until it halts, without checking repeats, necessarily terminates.

**III.** Recording visited configurations permits deciding whether this computation eventually accepts.

**IV.** Finiteness alone makes every computation halt.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The panel's endorsement was qualified: it supported the proposal provided that the drainage plan was revised.” Here, “qualified” most nearly means:

A. Issued by technically trained people.  
B. Unreserved.  
C. Subject to a condition.  
D. Withdrawn completely.  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An algorithm splits a size-n problem, where n is a power of two, into two half-size subproblems and then merges in Θ(n/log₂n) time for n≥4. Its running time satisfies T(n)=2T(n/2)+Θ(n/log₂n), with constant base cases at n≤2. What is the tight bound?

A. Θ(n)  
B. Θ(n log log n)  
C. Θ(n log n)  
D. Θ(n²)  

### Q18. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two control-unit designs implement the same instruction-set behaviour. One stores sequences of control words in a control memory; the other generates signals through fixed combinational/sequential logic. Which statement is correct?

A. The first is microprogrammed; changing its control words may change instruction sequencing without redesigning all control logic.  
B. The first cannot contain any sequencing logic.  
C. The second must fetch a microinstruction from control memory every cycle.  
D. Both designs must expose the same internal control-word format to application programs.  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-line direct-mapped cache starts empty and uses block number modulo four as its line index. Which reference sequence has exactly one hit?

A. 0,4,0,4  
B. 0,1,0,4  
C. 0,1,2,3  
D. 0,0,0,0  

### Q21. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP receiver calls a blocking `recv` requesting up to 100 bytes. The peer has sent 40 bytes, which are available, but has not closed the connection. Assuming the API allows a positive short return, which application behaviour is correct?

A. Treat a return of 40 as necessarily indicating end-of-file.  
B. Accumulate received bytes according to the application's framing rule rather than assuming each receive corresponds to one send or fills the requested count.  
C. Assume every return of fewer than 100 bytes is a network corruption.  
D. Assume TCP inserts an application-message boundary after each send.  

### Q22. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A loop begins with x=0 and repeatedly executes `x=x+1` while an input-dependent condition holds. A simple forward constant-propagation analysis joins facts from the initial edge and loop back edge at the header. Which statements are correct?

**Candidates**

**I.** x need not be a single known constant at the loop header after the fixed point is reached.

**II.** Treating x as zero on every header visit is sound merely because its initializer is zero.

**III.** Different iterations can reach the header with different x values.

**IV.** Constant propagation alone necessarily computes the exact iteration count for every input condition.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For a PDA accepting by empty stack with all input consumed, why must the input-consumption condition be checked explicitly?

A. Emptying the stack while unread input remains is not by itself acceptance under this convention.  
B. A stack can never be empty.  
C. Input is always consumed in one transition.  
D. Empty-stack acceptance requires a finite input alphabet of exactly one symbol.  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The proposed change is reversible: the previous configuration can be restored.” Which meaning of reversible applies?

A. Impossible to undo.  
B. Capable of being undone.  
C. Required to happen twice.  
D. Unrelated to the previous configuration.  

### Q25. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A nondeterministic PDA can make epsilon moves and may have infinite branches. Which statements about searching its computation tree are true?

**Candidates**

**I.** Breadth-first search will eventually find an accepting computation if one exists with finitely many transitions, assuming finite branching.

**II.** Naive depth-first search that never backtracks from an infinite branch always finds every accepting computation.

**III.** An epsilon loop can trap such a depth-first search despite another accepting branch.

**IV.** Breadth-first search necessarily halts and rejects every nonmember of every context-free language without any further algorithmic construction.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q26. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider a resource-allocation graph for processes waiting for reusable resources; a resource type may have multiple instances. Which statements hold in the standard model?

**Candidates**

**I.** A deadlock implies a directed cycle.

**II.** An acyclic graph rules out deadlock.

**III.** Every directed cycle proves deadlock even with multiple instances per resource type.

**IV.** A cycle-free graph proves every process has already finished.

A. I and IV  
B. I and II  
C. II and III  
D. II and IV  

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sequence can be the preorder traversal of a BST with distinct keys and the ordinary strict ordering property?

A. 40,20,10,30,60,50,70  
B. 40,20,50,10,60,30,70  
C. 40,60,50,20,10,30,70  
D. 40,20,30,10,60,50,70  

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A report states: “The survey's volunteers reported shorter commutes than the city average. Because participation was voluntary, the survey alone cannot establish that the same pattern holds among all residents.” Which conclusion best respects this qualification?

A. Every resident has a shorter-than-average commute.  
B. Voluntary participation guarantees a representative sample.  
C. The volunteers' result is an observation whose generalization requires further evidence.  
D. Every volunteer's response must be false.  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Exact integer variable x starts at zero. A loop executes `x=1-x` an arbitrary finite number of times, possibly zero. After the loop, y=x*(x−1) is evaluated. Which statements are true?

**Candidates**

**I.** x is necessarily zero after the loop.

**II.** x is always either zero or one after the loop.

**III.** y is always zero and may be replaced by that constant.

**IV.** y can equal one if the iteration count is odd.

A. II and III  
B. III and IV  
C. I and II  
D. I and III  

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Transaction T writes x, then transaction U reads that new value of x. T subsequently aborts. Which requirement alone directly forces U to abort too, even if U wrote no data?

A. Cascading recovery after a dirty read.  
B. The existence of a read–read conflict.  
C. Every read-only transaction must abort.  
D. Any two transactions accessing one item must be serialized by aborting both.  

### Q31. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two processes share a memory segment containing a counter initialized to0. Each performs one ordinary non-atomic read-increment-write operation. Which statements are correct without synchronization?

**Candidates**

**I.** A final value of1 is possible.

**II.** A final value of2 is possible.

**III.** Shared memory automatically makes each read-increment-write atomic.

**IV.** A final value of3 is possible from these two operations alone.

A. I and IV  
B. II and III  
C. I and II  
D. II and IV  

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A college's pass rates in both departments increased from one year to the next, but its overall pass rate decreased. Which explanation is possible?

A. The departmental statements and overall statement are mathematically incompatible.  
B. The fraction of candidates in the department with the lower pass rate increased sufficiently.  
C. The number of departments necessarily increased.  
D. Every candidate must have changed departments.  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A contiguous row-major array A has3 rows and5 columns of four-byte elements, without padding. A transpose view B has5 rows and3 columns and maps B[i,j] to A[j,i], without copying data. Which statements are correct?

A. Increasing i by1 at fixed j advances the element address by4 bytes.  
B. Increasing j by1 at fixed i advances the element address by20 bytes.  
C. B is contiguous in its own row-major traversal order.  
D. Writing B[2,1] changes the same stored element as A[1,2].  

### Q34. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary search tree stores distinct keys. An algorithm claims that checking only “each left child is smaller than its parent and each right child is larger” is sufficient to validate the whole BST. Which statements are correct?

A. The local condition is necessary.  
B. The local condition is sufficient.  
C. A tree with root10, left child5 and5's right child12 is a counterexample to sufficiency.  
D. Propagating ancestor-imposed lower and upper bounds can detect the counterexample.  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For Boolean variables x,y, which expressions equal x XOR y for every assignment?

**Candidates**

**I.** (x OR y) AND NOT(x AND y).

**II.** (x AND NOT y) OR (NOT x AND y).

**III.** x OR y.

**IV.** NOT(x XOR y).

A. I and III  
B. I and IV  
C. I and II  
D. II and III  

### Q36. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Over alphabet{a,b}, let R=a*b* and L={a^n b^n:n≥0}. Which statements are correct?

**Candidates**

**I.** L is a subset of R.

**II.** Every subset of a regular language is regular.

**III.** R is regular but L is not.

**IV.** The inclusion L⊆R proves that L is finite.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q37. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Exactly one of propositions p,q,r is true. Additionally, p implies q. Which statements must hold?

A. p is false.  
B. Exactly one of q,r is true.  
C. q is necessarily true.  
D. q and r cannot both be false.  

### Q38. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proposed rule maps every integer n to n²+n+1. Observations for inputs1,2,3 give outputs3,7,13. Which statements are correct?

A. The proposed rule agrees with all three observations.  
B. These observations uniquely establish the rule for every integer input.  
C. Adding (n−1)(n−2)(n−3) to the proposed rule gives another rule agreeing with the observations.  
D. The proposed rule predicts21 at input4.  

### Q39. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n=2^k with k≥1, determine the tight asymptotic running time of this code. Every execution of work() costs one unit.

```text
i = n
while i >= 1:
    j = i
    while j <= n:
        work()
        j = 2*j
    i = i/2
```

A. Θ(log n)  
B. Θ(n)  
C. Θ((log n)²)  
D. Θ(n log n)  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process opens a file once, duplicates that descriptor, and then forks. Assume ordinary shared-open-file-description semantics, no later opens, and sequential rather than concurrent reads. Which statements are correct?

**Candidates**

**I.** Parent and child descriptor references can share one file offset.

**II.** Duplicating a descriptor necessarily creates an independent offset.

**III.** A read through one of the shared references can change the offset seen by the others.

**IV.** Closing one reference necessarily closes every remaining reference immediately.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q41. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Someone argues that a language is regular because one selected word has one decomposition that pumps for every exponent. Which statements are correct?

**Candidates**

**I.** This establishes the pumping lemma's required property for every sufficiently long word.

**II.** The argument omits a uniform pumping length and quantification over words.

**III.** Even satisfying the regular pumping lemma's condition would not by itself prove regularity.

**IV.** Showing one decomposition fails is sufficient to establish nonregularity.

A. II and III  
B. I and III  
C. I and IV  
D. II and IV  

### Q42. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A weak entity Room is identified by the pair(BuildingID,RoomNumber). RoomNumber is unique only within a building. Which statements are correct?

A. Rooms in different buildings may share a RoomNumber.  
B. RoomNumber alone necessarily identifies a room globally.  
C. The owner's identifier contributes to the weak entity's identification.  
D. Moving a room record to another building can cause an identifier collision if that building already has the same RoomNumber.  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A dynamic array doubles capacity when an append encounters a full array and halves capacity immediately when a removal leaves size exactly half the current capacity. Each resize copies all retained elements. Starting with size and capacity both n, repeatedly append one element and then remove it, for k repetitions. Ignore unrelated work. What is the total copying cost?

A. Θ(k)  
B. Θ(n+k)  
C. Θ(kn)  
D. Θ(log n)  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Grammar S→aSa | bSb | a | b is over{a,b}. Which statements are correct?

**Candidates**

**I.** Every generated string is an odd-length palindrome.

**II.** The grammar generates ε.

**III.** Reversing a generated string always gives a generated string.

**IV.** The language is closed under concatenation.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q45. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean inputs x,y,z, a circuit outputs F=(x AND y) OR ((NOT x) AND z). Which statements hold?

A. Flipping x leaves F unchanged exactly when y=z.  
B. F equals (x OR z) AND ((NOT x) OR y).  
C. F is independent of z whenever y=1.  
D. When y=NOT z, F XOR z equals x.  

### Q46. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A browser already knows a server's IP address and establishes a new TCP connection to request an HTTP resource. The server responds with a redirection to a different hostname. Which statements hold?

**Candidates**

**I.** The initial request need not perform a new DNS query if its address is already usable.

**II.** The redirect guarantees that the original server's IP address is valid for the new hostname.

**III.** Following the redirect may require resolving the new hostname.

**IV.** An HTTP redirect changes the destination address of the already transmitted request.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV  

### Q47. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A microprogrammed controller has a control-store address register, a microinstruction register, and combinational next-address logic. A fetched microinstruction specifies both datapath controls and a conditional next address. Which statements hold?

**Candidates**

**I.** A datapath status flag can influence selection of the next microinstruction.

**II.** The control store must be writable during every machine instruction.

**III.** Several compatible datapath control signals can be asserted by the same microinstruction.

**IV.** Every machine instruction necessarily executes the same number of microinstructions.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q48. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A connected TCP socket receives the peer's orderly write shutdown after all previously transmitted bytes have arrived. The local application has read all those bytes. No reset or error occurs. Which statements hold?

**Candidates**

**I.** A subsequent positive-length receive can return0 to indicate end of stream.

**II.** The local application must interpret that0 return as a received zero-valued data byte.

**III.** The local endpoint may still send data if its own write direction remains open and the peer continues receiving.

**IV.** TCP necessarily delivers a separate application record for the shutdown.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q49. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under set relational algebra, R(A,B) contains (1,x),(1,y),(2,x), and S(B) contains x,y. Let D=R÷S and P=π_A(R). Which statements hold?

**Candidates**

**I.** D contains exactly the tuple A=1.

**II.** D=P.

**III.** Adding (2,y) to R makes D=P.

**IV.** Removing y from S makes D empty.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q50. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The available closed intervals are [0,4], [3,8], [7,10], [0,6], [6,9], [8,10]. Starting at 0, a greedy covering algorithm repeatedly chooses, among intervals beginning at or before the current covered endpoint, an interval extending that endpoint farthest. It stops when [0,10] is covered. Which sequence does it select?

A. [0,4], [3,8], [8,10]  
B. [0,6], [6,9], [8,10]  
C. [0,6], [7,10]  
D. [0,4], [7,10]  

---

## ANSWER KEY — SET 013

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | MCQ | 2 | B |
| 3 | MSQ | 1 | B, C, D |
| 4 | MCQ | 2 | D |
| 5 | MSQ | 1 | A, B, C |
| 6 | MSQ | 2 | A, B, D |
| 7 | MCQ | 1 | C |
| 8 | MCQ | 2 | D |
| 9 | MCQ | 1 | A |
| 10 | MSQ | 2 | B, C, D |
| 11 | MSQ | 2 | A, C, D |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 1 | A, C, D |
| 14 | MCQ | 2 | B |
| 15 | MCQ | 1 | C |
| 16 | MSQ | 1 | A, B, D |
| 17 | MSQ | 2 | A, C, D |
| 18 | MSQ | 2 | A, C, D |
| 19 | MSQ | 1 | B, C, D |
| 20 | MSQ | 1 | A, C, D |
| 21 | MSQ | 2 | A, C, D |
| 22 | MCQ | 2 | B |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 1 | A, C, D |
| 25 | MCQ | 2 | A |
| 26 | MCQ | 1 | B |
| 27 | MSQ | 1 | B, C, D |
| 28 | MSQ | 1 | A, B, D |
| 29 | MCQ | 2 | A |
| 30 | MSQ | 1 | B, C, D |
| 31 | MCQ | 1 | C |
| 32 | MSQ | 1 | A, C, D |
| 33 | MCQ | 2 | C |
| 34 | MCQ | 2 | B |
| 35 | MCQ | 1 | C |
| 36 | MCQ | 1 | D |
| 37 | MCQ | 2 | C |
| 38 | MCQ | 2 | B |
| 39 | MSQ | 2 | A, B, D |
| 40 | MCQ | 2 | D |
| 41 | MCQ | 2 | A |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 1 | A, B, D |
| 44 | MCQ | 2 | D |
| 45 | MCQ | 2 | C |
| 46 | MCQ | 1 | B |
| 47 | MCQ | 1 | C |
| 48 | MCQ | 1 | D |
| 49 | MCQ | 1 | A |
| 50 | MSQ | 2 | A, C, D |
