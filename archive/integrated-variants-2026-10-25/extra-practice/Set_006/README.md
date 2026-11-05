# GATE CS — Additional Practice Set 006

**Questions:** 50  
**Maximum marks:** 76

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange the following sentences into a coherent chronological account. Treat the explicitly stated causal and time relations as binding.

P. Based on the successful repeat trial, the final report recommended a full rollout.
Q. Both gauges were calibrated before the first trial began.
R. During that first trial, the two readings diverged as temperature rose.
S. Replacing one gauge eliminated this divergence in a repeat trial.
T. After receiving the final report, the committee accepted its recommendation.

Which sequence is correct?

A. Q-R-P-S-T  
B. R-Q-S-P-T  
C. Q-R-S-P-T  
D. Q-S-R-T-P  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two positive-edge-triggered D flip-flops store bits (q1,q0). At every active clock edge both are updated simultaneously according to q1(next) = q0 XOR q1 and q0(next) = NOT q1. The initial state is (0,0). What is the state after 2027 active clock edges?

A. (0,0)  
B. (0,1)  
C. (1,1)  
D. (1,0)  

### Q3. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A tank contains 120 litres of a well-mixed milk-water mixture in the ratio 3:2. First, 30 litres are removed and replaced with water. After thorough mixing, 20 litres are removed and replaced with pure milk. What is the final ratio of milk to water? Volumes are additive.

A. 11:13  
B. 13:11  
C. 3:2  
D. 7:5  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router must advertise exactly all IPv4 addresses from 10.4.1.0 through 10.4.6.255, inclusive, using ordinary CIDR prefixes. No address outside this interval may be covered, and no exception routes are allowed. What is the smallest number of prefixes required?

A. 2  
B. 3  
C. 4  
D. 6  

### Q5. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The table gives successful applications divided by total applications for two programmes. Every application belongs to exactly one programme.

| Programme | Year 1 | Year 2 |
|---|---:|---:|
| P | 80/100 | 9/10 |
| Q | 20/100 | 27/90 |

Which statements follow from the table?

**Candidates**

**I.** Each programme's success percentage increased.

**II.** The combined success percentage increased.

**III.** Programme Q's share of all applications increased.

**IV.** The table proves that an individual applicant's chance of success increased because of a policy change.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q6. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

How many times is work() called asymptotically, for positive integer n?

```text
for i = 1 to n:
    j = i
    while j <= n:
        work()
        j = j + i
```

A. Θ(n)  
B. Θ(n²)  
C. Θ(log n)  
D. Θ(n log n)  

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A voluntary online survey asks users of a study app whether it improved their examination scores. Eighty percent of respondents say yes. No earlier scores or comparison group are recorded. Which statement is best supported?

A. The app caused an improvement for 80% of all students.  
B. Eighty percent of respondents reported improvement, but population effects and causation are not established.  
C. Voluntary participation proves that respondents are representative.  
D. The app cannot have helped any student because there was no control group.  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Under basic timestamp ordering, x initially has read timestamp 0 and write timestamp 0. T10 with timestamp 10 successfully reads x. T5 with timestamp 5 then attempts to write x. Which action is required? Thomas's write rule, if considered, may ignore an obsolete write only when it does not violate the read-timestamp test.

A. Accept the write because x has never been written.  
B. Ignore the write under Thomas's rule without aborting T5.  
C. Reject the write and abort T5 because its timestamp is below x's read timestamp.  
D. Decrease x's read timestamp to 5 and accept.  

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Five presentations P,Q,R,S,T occupy five consecutive slots, one per slot. Q occurs immediately after P. R occurs before P, and S occurs after Q. How many schedules satisfy these restrictions?

A. 2  
B. 4  
C. 6  
D. 8  

### Q10. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Use set semantics. R(A,B) contains (1,x),(2,x), and S(B,C) contains (x,p),(x,q). The natural join J=R⋈S is formed. Which statements are correct?

**Candidates**

**I.** J has four tuples.

**II.** A→C holds in J.

**III.** Projecting J onto (A,B) recovers R exactly.

**IV.** B is a candidate key of J.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q11. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A two-input gate outputs 1 exactly when its inputs differ. Its output is fed to a second identical gate together with a third input c. Which description of the final output is correct?

A. It is 1 exactly when one input, but not all three, is 1.  
B. It is 1 exactly when an odd number of the three inputs are 1.  
C. It is 1 exactly when at least two inputs are 1.  
D. It is 1 exactly when all inputs agree.  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange these events into the only order consistent with their stated dependencies: P: restore a backup after locating the fault; Q: test the restored system; R: locate the fault using diagnostic logs; S: reopen access only after the test succeeds.

A. P,R,Q,S  
B. R,P,S,Q  
C. R,P,Q,S  
D. Q,R,P,S  

### Q13. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed weighted graph contains s→a (1), a→b (−2), b→a (1), b→c (4), and s→t (5), with no other edges. Which statements are correct?

**Candidates**

**I.** There is no finite minimum weight among s-to-c walks.

**II.** The shortest s-to-t path has weight 5.

**III.** The negative cycle makes every vertex's distance from s equal to minus infinity.

**IV.** c can reach a negative cycle.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a three-address representation, evaluate `a+b*c` with normal multiplication precedence, without algebraic reordering. Which sequence is suitable?

A. t1=a+b; t2=t1*c  
B. t1=b*c; t2=a+t1  
C. t1=a*c; t2=t1+b  
D. t1=a+b; t2=b*c  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A synchronous three-bit binary counter has next-state equations q0′=NOT q0, q1′=q1 XOR q0, q2′=q2 XOR (q1 AND q0). Starting in 011, what is its state after five clock edges?

A. 111  
B. 000  
C. 001  
D. 101  

### Q16. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An input describes a Turing machine M over {0,1}, with the promise that M halts on every input string. Algorithms below need only behave correctly on machines satisfying the promise. Which statements are correct?

**Candidates**

**I.** Nonemptiness of L(M) is semidecidable by testing strings and eventually accepting whenever an accepted string exists.

**II.** Emptiness of L(M) is decidable solely because every individual simulation halts.

**III.** Equivalence of L(M) to the empty language is decidable under this promise.

**IV.** Whether M accepts at least one string of length at most ten is decidable.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q17. [2 Marks] [MCQ]

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

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In ordinary constant propagation, one predecessor of block B assigns x=4 and another assigns x=7. Both paths are feasible. No assignment to x occurs at B before its first use. What can be concluded at entry to B?

A. x is the constant 4.  
B. x is the constant 7.  
C. x is not a single known constant at this merge.  
D. x is uninitialized on both paths.  

### Q19. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An IP packet traverses two Ethernet links through an IP router, with no tunnelling. Which statements hold?

**Candidates**

**I.** The router normally constructs a new link-layer frame for the outgoing link.

**II.** The incoming Ethernet destination address must remain the outgoing Ethernet destination address.

**III.** End-to-end IP addressing and hop-local link-layer addressing serve different scopes.

**IV.** Ethernet framing removes the need for an IP destination address across routed networks.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q20. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar S→aSb | T and T→cT | ε, which statements are true?

A. Every generated word has equally many a and b symbols.  
B. Every generated word has all c symbols between its a and b blocks.  
C. The grammar generates abcc.  
D. The grammar generates aacbb.  

### Q21. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two internal TCP clients connect to the same external server through a translator sharing one public address. The translator assigns different public source ports. Which information is essential for routing a returning server segment to the correct internal connection?

A. Only the external server's destination port, ignoring the translated port.  
B. A translation mapping that includes the public-side connection endpoint information and its corresponding internal endpoint.  
C. Only the Ethernet broadcast address.  
D. Only the length of the TCP payload.  

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A doubly linked list has adjacent non-sentinel nodes P,X,N. Removing X while preserving the list requires which neighbour updates?

A. P.next=N and N.prev=P.  
B. P.prev=N and N.next=P.  
C. P.next=X and N.prev=X.  
D. P.next=P and N.prev=N.  

### Q23. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An IPv4 fragment has offset field 100, 400 payload bytes, and MF=1. A downstream link permits only 200 payload bytes per fragment; 200 is divisible by eight. The router splits this fragment into two. Which statements are correct?

A. Their offset fields are 100 and 125.  
B. Both resulting fragments have MF=1.  
C. Both retain the original datagram's identification value.  
D. Their offsets must restart from zero because they were produced by a different router.  

### Q24. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A datagram socket has queued datagrams of lengths 12 and 5 bytes, in that order. Each receive uses an 8-byte buffer. The specified API returns at most one datagram per receive and discards excess bytes of a truncated datagram. What byte counts do the next two receives return?

A. 8 and 8  
B. 8 and 5  
C. 12 and 5  
D. 8 and 4  

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which word belongs to (ab|ba)* but not to (ab)*?

A. abab  
B. baab  
C. aabb  
D. aaa  

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A byte-addressed 4 KiB window maps to a 2 KiB memory chip. Address bits A10–A0 reach the chip; A11 is ignored and the chip is selected throughout the window 0x000–0xFFF. Which other address accesses the same stored byte as 0x134?

A. 0x135  
B. 0x234  
C. 0x534  
D. 0x934  

### Q27. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a language with exact integer arithmetic, division by zero raises an observable exception. Consider `t=1/x; t=2; print(t);`, with x unchanged and print observable. Which statements are correct?

**Candidates**

**I.** The first assignment can always be removed because its stored value is dead.

**II.** Its stored value is dead, but its possible exception can prevent unconditional removal.

**III.** Both assignments can always be removed, leaving print(t) with t's old value.

**IV.** If x is proved nonzero, the whole fragment may be replaced by print(2).

A. II and IV  
B. I and IV  
C. II and III  
D. III and IV  

### Q28. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For grammar S→AB, A→aA | ε, B→bBc | ε, with start symbol S and end marker $, which statements are correct?

**Candidates**

**I.** The grammar is LL(1).

**II.** c belongs to FOLLOW(A).

**III.** FOLLOW(B)={c,$}.

**IV.** The production A→ε must be selected on lookahead a in an LL(1) table.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q29. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An interrupt source sets a single pending bit on each event; setting an already-set bit has no extra effect. Interrupts are masked until time 5. Events occur at times 1,2,3,6. On entering a handler the bit is cleared; each handler lasts two time units, and events during it can set the bit again. A pending interrupt is handled immediately when unmasked and no handler is running. Which pair gives the number of handler invocations and the final handler's completion time?

A. (4,13)  
B. (2,9)  
C. (1,7)  
D. (3,11)  

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process uses two distinct virtual pages v1 and v2 as aliases of the same physical frame. A simplified inverted page table stores exactly one pair(process ID, virtual page number) per physical frame. A lookup searches those stored pairs; no auxiliary alias information exists. Which statements are correct?

**Candidates**

**I.** The simplified table can simultaneously represent both aliases in its one entry for the frame.

**II.** The physical memory arrangement is possible even though the simplified representation cannot encode both aliases.

**III.** A mapping structure with a list of aliases per physical frame can address this representation problem.

**IV.** Aliasing requires the two virtual page numbers to be equal.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange these sentences into a coherent account. “This discrepancy” refers to the difference between the two measurements, and “the repair” refers to replacing the defective sensor.

P: A replacement sensor brought the readings into agreement.  
Q: Two instruments measuring the same temperature initially gave different readings.  
R: After the repair, both instruments remained stable during a second trial.  
S: This discrepancy led the technician to identify a defective sensor.

A. Q,S,P,R  
B. S,Q,R,P  
C. Q,P,R,S  
D. P,R,Q,S  

### Q32. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

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

**Candidates**

**I.** x is live immediately after line2.

**II.** x is live immediately before line5.

**III.** y is live immediately before line6.

**IV.** Line1 is dead because one path does not use x.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q33. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A0/1 knapsack has capacity10 and items(weight,value)=(6,12),(5,9),(5,9), each available once. A heuristic scans items in decreasing value/weight order and takes an item whenever it fits. Which statement is correct?

A. The heuristic obtains12, while the optimum is18.  
B. The heuristic obtains18, while the optimum is12.  
C. Both obtain21 by splitting an item.  
D. The heuristic cannot choose any item.  

### Q34. [1 Mark] [MCQ]

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

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

After fork, a parent and child initially share read-only physical pages under copy-on-write. Each has its own virtual mappings. Which statements are correct?

**Candidates**

**I.** The first write by one process may trigger a fault and a private copy.

**II.** Every page must be copied immediately at fork under this scheme.

**III.** A successful private copy can allow one process to modify its page without changing the other's contents.

**IV.** Sharing a physical page initially implies that later writes must always be visible to both processes.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q36. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A condition D has probability0.1. Two tests are independent conditional on whether D holds. Each test is positive with probability0.9 given D and0.2 given NOT D. Which statements are correct?

**Candidates**

**I.** The two positive-result indicators are independent without conditioning.

**II.** The probability both tests are positive is0.117.

**III.** Given both positive, P(D)=9/13.

**IV.** Given one positive, a second positive leaves P(D) unchanged.

A. I and III  
B. II and III  
C. I and IV  
D. II and IV  

### Q37. [2 Marks] [MCQ]

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

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A rooted ordered full binary tree has exactly four leaves. Every internal node has a left and a right child, and the root has depth 0. Which lists can be the depths of its leaves in left-to-right order?

**Candidates**

**I.** (1,2,3,3)

**II.** (2,1,3,3)

**III.** (2,2,2,2)

**IV.** (3,3,1,2)

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L={a^n b^n : n≥0}, and define K={w : there exists z in b* such that wz is in L}. Which statements are correct?

**Candidates**

**I.** aaab belongs to K.

**II.** abb belongs to K.

**III.** K is context-free.

**IV.** K is regular.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q40. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A poset has elements a,b,c,d with a<c,b<c,c<d, and only the comparisons forced by these and reflexivity. Let J be the family of its downward-closed subsets, ordered by inclusion. Which statements are correct?

A. J has six elements, including the empty subset.  
B. Join in J is set union.  
C. Meet in J is set intersection.  
D. J fails distributivity because a and b are incomparable.  

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An n-bit adder has carry-in0, carry into the sign bit c and final carry-out d. Which statements are correct for two's-complement addition?

**Candidates**

**I.** Signed overflow is indicated by c XOR d.

**II.** Final carry-out alone always indicates signed overflow.

**III.** Adding operands of opposite signs cannot cause signed overflow.

**IV.** A result with sign bit1 always indicates overflow.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q42. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A timestamp protocol handles a write by transaction timestamp t as follows: abort if t<readTS(x); otherwise ignore the write if t<writeTS(x); otherwise perform it. Initially readTS(x)=5 and writeTS(x)=9. Two separate attempts are considered from this same initial state, with t=7 and t=4. What are their respective outcomes?

A. Perform, ignore  
B. Abort, ignore  
C. Ignore, abort  
D. Perform, abort  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

SQL table T(x) has two rows, both x=NULL. Compare Q1=SELECT COUNT(*) FROM (SELECT DISTINCT x FROM T) AS U and Q2=SELECT COUNT(DISTINCT x) FROM T. What pair of scalar results (Q1,Q2) is returned?

A. (0,0)  
B. (2,0)  
C. (1,1)  
D. (1,0)  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let f:{a,b,c}→{0,1} satisfy f(a)=f(b)=0 and f(c)=1. Which statements are correct?

**Candidates**

**I.** Exactly two functions g:{0,1}→{a,b,c} satisfy f composed with g equal to the identity on{0,1}.

**II.** Some function g satisfies g composed with f equal to the identity on{a,b,c}.

**III.** Every g satisfying the identity in A is injective.

**IV.** f is injective.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q45. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Order the set {1,2,3,6} by divisibility. Which statements hold?

**Candidates**

**I.** Every pair has a greatest lower bound and a least upper bound in this set.

**II.** 2 and 3 have neither a common upper bound nor a common lower bound.

**III.** Every element has a complement with respect to bottom 1 and top 6.

**IV.** The order is a total order.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q46. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

L is a language over {a,b}, and its complement is taken with respect to {a,b}*. Which statements necessarily hold?

A. If both L and its complement are finite, then {a,b}* is finite.  
B. If L is regular, its complement is context-free.  
C. If L is context-free, its complement is regular.  
D. If L is finite, its complement is regular.  

### Q47. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A three-variable Karnaugh map represents F=1 exactly when an even number of inputs are1. There are no don't-care entries. Which statement about a two-level SOP using only uncomplemented or complemented input literals is correct?

A. One four-cell group covers all1-cells.  
B. Two two-cell groups cover all1-cells.  
C. Four singleton groups are required.  
D. No SOP can represent this function.  

### Q48. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Functions f:A→B and g:B→A satisfy g composed with f=identity on A. No finiteness assumption is made. Which statements necessarily hold?

**Candidates**

**I.** f is injective.

**II.** f is surjective onto B.

**III.** g is surjective onto A.

**IV.** f composed with g=identity on B.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that unambiguously states that the technician, rather than the instrument, was in a hurry.

A. Being in a hurry, the instrument was checked by the technician.  
B. The instrument was checked in a hurry that belonged to the technician.  
C. In a hurry, the technician checked the instrument.  
D. The technician checked the instrument that was in a hurry.  

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An NPDA chooses one of two branches at the start. Its first branch recognizes {a^i b^j c^k : i=j, i,j,k≥0}; its second recognizes {a^i b^j c^k : j=k, i,j,k≥0}. Acceptance requires consuming the entire input and acceptance by at least one branch. Which words does it accept?

A. aabbccc  
B. aabbbccc  
C. aaabcc  
D. abc  

---

## ANSWER KEY — SET 006

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 2 | A, B, D |
| 2 | MSQ | 2 | A, B, D |
| 3 | MSQ | 2 | A, C, D |
| 4 | MSQ | 2 | A, B, D |
| 5 | MCQ | 1 | C |
| 6 | MSQ | 1 | A, B, C |
| 7 | MSQ | 2 | A, C, D |
| 8 | MSQ | 2 | A, B, D |
| 9 | MSQ | 2 | A, C, D |
| 10 | MCQ | 2 | D |
| 11 | MSQ | 1 | A, C, D |
| 12 | MSQ | 1 | A, B, D |
| 13 | MCQ | 2 | C |
| 14 | MSQ | 1 | A, C, D |
| 15 | MSQ | 1 | A, C, D |
| 16 | MCQ | 2 | B |
| 17 | MCQ | 2 | C |
| 18 | MSQ | 1 | A, B, D |
| 19 | MCQ | 1 | A |
| 20 | MCQ | 2 | C |
| 21 | MSQ | 2 | A, C, D |
| 22 | MSQ | 1 | B, C, D |
| 23 | MCQ | 1 | D |
| 24 | MSQ | 2 | A, C, D |
| 25 | MSQ | 1 | A, C, D |
| 26 | MSQ | 1 | A, B, C |
| 27 | MCQ | 2 | A |
| 28 | MCQ | 2 | B |
| 29 | MSQ | 2 | A, C, D |
| 30 | MCQ | 1 | D |
| 31 | MSQ | 1 | B, C, D |
| 32 | MCQ | 2 | B |
| 33 | MSQ | 2 | B, C, D |
| 34 | MCQ | 1 | D |
| 35 | MCQ | 1 | A |
| 36 | MCQ | 2 | B |
| 37 | MCQ | 2 | C |
| 38 | MCQ | 2 | D |
| 39 | MCQ | 2 | A |
| 40 | MCQ | 2 | D |
| 41 | MCQ | 1 | C |
| 42 | MSQ | 1 | A, B, D |
| 43 | MSQ | 1 | A, B, C |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 1 | C |
| 46 | MCQ | 1 | C |
| 47 | MSQ | 1 | A, B, D |
| 48 | MCQ | 1 | B |
| 49 | MSQ | 1 | A, B, D |
| 50 | MCQ | 2 | C |
