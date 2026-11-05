# GATE CS — Additional Practice Set 011

**Questions:** 50  
**Maximum marks:** 73

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 4-bit adder-subtractor computes A+(B XOR ssss)+s and keeps the low four result bits. Its carry-out is C and its two's-complement signed overflow flag is V. For A=0111, B=1010 and s=1, which triple (result,C,V) is correct?

A. (1101,1,0)  
B. (1101,0,0)  
C. (0011,1,1)  
D. (1101,0,1)  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A singly linked list initially consists of six distinct nodes with values 1,2,3,4,5,6 in that order, followed by NULL. The following pointer operations are executed. Node fields are modified in place; no nodes are allocated or freed.
```text
p = head
q = NULL
while p != NULL and p.next != NULL:
    r = p.next
    p.next = r.next
    r.next = q
    q = r
    p = p.next
```
Which pair gives the lists reached from (head, q) after termination?

A. (1→3→5, 2→4→6)  
B. (1→3→5, 6→4→2)  
C. (1→5, 6→4→3→2)  
D. (1→2→3, 6→5→4)  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A depth-first search of a directed graph records discovery and finish times. Vertex u has interval [2,9] and vertex v has interval [4,7]. The graph contains an edge v→u. Which conclusion is necessarily correct?

A. The edge v→u is a tree edge.  
B. The graph contains a directed cycle.  
C. The edge v→u must be a cross edge.  
D. The graph must be acyclic because the intervals are nested.  

### Q4. [2 Marks] [MCQ]

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

### Q5. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For which of the following real values of x is the equation log_x(16)=log_2(x) defined and true?

**Candidates**

**I.** 4

**II.** 1/4

**III.** −4

**IV.** 1

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the positive divisors of 60, ordered by divisibility. The least and greatest elements are 1 and 60. A complement of d is a divisor e with meet(d,e)=1 and join(d,e)=60. Which statements are correct?

A. This partially ordered set is a lattice.  
B. Every element has a complement.  
C. Exactly eight elements have complements.  
D. The lattice is distributive.  

### Q7. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Start with complete bipartite graph K3,4, with sides {a,b,c} and {1,2,3,4}. Remove edges {a,1},{b,2},{c,3}. Which statements are correct?

**Candidates**

**I.** Its maximum matching has size 3.

**II.** Every vertex cover has at least 4 vertices.

**III.** Its chromatic number is 2.

**IV.** It has a matching covering all seven vertices.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q8. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let M have rows (2,1,0),(1,1,1),(0,1,2). For arbitrary b=(b1,b2,b3)ᵀ, consider Mx=b over the real numbers. Which statements are correct?

A. M has rank 2.  
B. The null space is spanned by (1,−2,1)ᵀ.  
C. Mx=b is consistent exactly when b1−2b2+b3=0.  
D. Every consistent system Mx=b has a unique solution.  

### Q9. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two threads acquire initially free nonrecursive mutexes A and B. Thread P acquires A then B; thread Q acquires B then A. Each releases both only after acquiring both. Which statements are correct?

**Candidates**

**I.** A deadlock is possible.

**II.** Every interleaving deadlocks.

**III.** Changing Q to acquire A then B eliminates deadlock in this two-thread, two-mutex program.

**IV.** Releasing a mutex immediately after acquiring it preserves the original protection of a critical section that requires both mutexes together.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q10. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two processes share a bounded queue initially empty, a mutex M initially 1, a counting semaphore E initially equal to the positive capacity, and a counting semaphore F initially 0. A proposed consumer performs `wait(M); wait(F); remove; signal(E); signal(M)`. A producer performs `wait(E); wait(M); insert; signal(M); signal(F)`. Semaphore operations are atomic. Which statements are correct?

A. If the consumer acquires M first, the system can deadlock.  
B. Moving the consumer's wait(F) before wait(M) removes this specific empty-buffer deadlock.  
C. Increasing the initial value of E while keeping F=0 always prevents the deadlock.  
D. The proposed consumer may hold M while waiting for an item that the producer needs M to insert.  

### Q11. [2 Marks] [MCQ]

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

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

SQL table L(id) contains 1,2 and table R(id,v) contains (1,0),(1,5). What rows are returned by the following query, using ordinary SQL bag semantics?

```sql
SELECT L.id, R.v
FROM L LEFT JOIN R ON L.id=R.id AND R.v>0;
```

A. (1,5) only  
B. (1,0),(1,5),(2,NULL)  
C. (1,5),(2,NULL)  
D. (1,NULL),(2,NULL)  

### Q13. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A recognizer for L1 and a recognizer for L2 may loop on nonmembers. Which proposed procedures recognize the stated languages for every such pair of recognizers?

**Candidates**

**I.** For L1∪L2, interleave one step of each recognizer and accept when either accepts.

**II.** For L1∪L2, run the first recognizer to completion before starting the second, accepting if either accepts.

**III.** For L1∩L2, run the first until it accepts, then the second until it accepts, and then accept.

**IV.** For the complement of L1, accept if its recognizer has not accepted after one million steps.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q14. [2 Marks] [MCQ]

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

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An ordinary IPv4 subnet is 192.168.1.96/27, with its all-zero and all-one host fields reserved for network and broadcast addresses. Which is the highest assignable host address?

A. 192.168.1.127  
B. 192.168.1.126  
C. 192.168.1.128  
D. 192.168.1.125  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler performs copy propagation on `x=y; z=x+1; y=5; w=x+1;`, with exact ordinary scalar variables and no aliases. Which replacement of both uses of x is valid for every initial y?

A. Replace both by the current y without any saved value.  
B. Replace only the use in z by y; the later use needs the old value represented by x or another saved copy.  
C. Replace both by 5.  
D. Replace neither use under any circumstances.  

### Q17. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L={w#wᴿ : w∈{0,1}*}, where # is a separator and wᴿ denotes reversal. Which statements are correct?

**Candidates**

**I.** A deterministic pushdown automaton can recognize L by switching from pushing to matching at #.

**II.** L is regular because the separator locates its midpoint.

**III.** Removing # from every word of L produces a context-free language.

**IV.** A finite automaton can always store the entire prefix w because each individual input is finite.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A positive-edge-triggered D flip-flop has asynchronous active-low reset. Its clock remains low while reset is asserted. What happens to Q?

A. Q resets without waiting for a rising clock edge.  
B. Q can change only at the next rising edge, even under reset.  
C. Q must toggle repeatedly while reset remains asserted.  
D. Q becomes equal to the complement of D.  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which language is regular?

A. {aⁿbⁿ : n≥0}  
B. {aᵖ : p is prime}  
C. {aⁿbᵐ : n,m≥0 and n is even}  
D. {ww : w∈{0,1}*}  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A device failed on three occasions when its battery level was below 5%, but no observations at other battery levels were collected. Which proposed next step would best test whether low battery level predicts failure?

A. Declare that every failure has already been explained.  
B. Collect comparable observations across both low and higher battery levels.  
C. Exclude every future observation above 5%.  
D. Infer that a full battery guarantees success without testing it.  

### Q21. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C) has dependencies AB→C and C→B. Which statement is correct?

A. Its only candidate key is AB and it is in BCNF.  
B. Its candidate keys are AB and AC; it is in 3NF but not BCNF.  
C. Every attribute is a candidate key by itself.  
D. It fails 3NF because B is not prime.  

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A committed transaction's update is lost after a crash despite the system acknowledging its commit. Which ACID property is directly violated?

A. Durability  
B. Atomicity necessarily, even if every update of that transaction was lost together  
C. Isolation only  
D. No property, because crashes are excluded from ACID concerns  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Grammar S→aS | Sb | ε generates which language?

A. a*b*  
B. {aⁿbⁿ:n≥0}  
C. (ab)* only  
D. All strings over {a,b}  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A point initially at (2,0) is reflected first across the line y=x and then across the line x=1. What are its final coordinates?

A. (2,2)  
B. (0,0)  
C. (0,2)  
D. (2,−2)  

### Q25. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider `p=A[i]; A[j]=7; q=A[i];` with valid indices, no other changes, and exact ordinary array storage. Which statements are correct?

**Candidates**

**I.** If i≠j is proved, the final load may be replaced by p.

**II.** With no relation known between i,j, the final load may always be replaced by p.

**III.** If i=j is proved, the final load's value is 7.

**IV.** The store can never affect any later load from A.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q26. [1 Mark] [MCQ]

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

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For powers of two n, a recursive algorithm has three recursive calls on size n/2, nonrecursive work Θ(n²), and constant work at n=1. Which statements are true?

**Candidates**

**I.** Its total work is Θ(n²).

**II.** Its total work is Θ(n² log n).

**III.** Its recursion tree has n^(log₂3) leaves.

**IV.** Its recursion tree has n internal levels before reaching size one.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q28. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Choose a,b independently and uniformly from {0,1,2,3,4}, and define h(x)=(ax+b) mod 5 on the same domain. For two distinct fixed keys x,y, which statements are true?

**Candidates**

**I.** For each ordered pair (r,s) of output values, exactly one pair (a,b) gives h(x)=r,h(y)=s.

**II.** Every function in this family is a permutation of the domain.

**III.** The probability h(x)=h(y) is 1/5.

**IV.** After conditioning on a≠0, h(x) and h(y) remain independent uniform variables.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For resource types A,B, three processes have allocations P:(0,1), Q:(1,0), R:(1,1) and remaining maximum needs P:(1,0), Q:(0,2), R:(1,1). Available resources are initially (0,0). Apply the standard safety test: a process whose remaining need is available may finish and release its allocation. Which statements are true?

**Candidates**

**I.** The initial state is unsafe.

**II.** Adding one available unit of B makes the state safe.

**III.** Adding one available unit of A makes the state safe.

**IV.** An unsafe maximum-claim state alone proves that the processes are already deadlocked on actual requests.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider this basic block; on exit only z is live. Variables have ordinary scalar values, and evaluating expressions has no side effects.

```text
1: x = a + b
2: y = x + c
3: x = d + e
4: z = y + x
```

Which statements are correct?

**Candidates**

**I.** Immediately before line3, the old value of x is live.

**II.** Immediately before line3, y is live.

**III.** Both assignments to x contribute to the final z.

**IV.** Line1 can be removed merely because line3 also assigns x.

A. I and II  
B. II and III  
C. I and III  
D. I and IV  

### Q31. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

On {1,2,3}, equivalence relation R has classes {1,2},{3}; equivalence relation S has classes {1},{2,3}. Which statements are correct?

**Candidates**

**I.** R∪S is transitive.

**II.** R∩S is the identity relation.

**III.** The smallest equivalence relation containing R∪S has one class.

**IV.** R∪S contains the ordered pair(1,3).

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Exactly one of three boxes contains a coin. Their labels state: A: “The coin is not in B”; B: “The coin is in this box”; C: “The coin is not in this box.” Exactly one label is true. Where is the coin?

A. Box A  
B. Box B  
C. Box C  
D. The conditions have no solution.  

### Q33. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A link layer detects corrupted frames using a checksum but, by assumption, may silently discard any frame and performs no retransmission. An application requires delivery of its complete message. Which statements are correct?

**Candidates**

**I.** Link error detection alone guarantees the application's delivery requirement.

**II.** An end-to-end acknowledgment and retransmission mechanism can address losses beyond a single link, subject to the network eventually allowing communication.

**III.** A valid link checksum proves the entire application message has arrived.

**IV.** Detection of corruption and recovery from loss are different functions.

A. II and IV  
B. II and III  
C. III and IV  
D. I and II  

### Q34. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a tabular Boolean-minimization procedure, two product cubes may be combined only if their don't-care positions are identical and they differ in exactly one remaining bit. Here '-' denotes a don't-care position. Which pairs can be combined under that rule?

**Candidates**

**I.** 0-01 and0-11.

**II.** 00-1 and0-01.

**III.** -100 and-101.

**IV.** 0101 and1010.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A symbolic link stores a pathname rather than increasing its target file's hard-link count. Which statements are correct?

**Candidates**

**I.** Deleting the target's only pathname can leave a dangling symbolic link.

**II.** A symbolic link necessarily prevents the target inode from being reclaimed forever.

**III.** A symbolic link can name a target on another file system under ordinary pathname resolution.

**IV.** Every symbolic link is indistinguishable from a hard link in inode reference counting.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q36. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The only use of scalar x after this fragment is return x. Variables are ordinary integers and expressions have no side effects.

```text
x = a + b
x = c + d
return x
```

Which statements are correct?

**Candidates**

**I.** The first assignment's computed value is dead.

**II.** The first assignment can be removed under the stated assumptions.

**III.** Both assigned values are simultaneously live before return.

**IV.** The second assignment is dead because x was previously assigned.

A. I and IV  
B. II and III  
C. II and IV  
D. I and II  

### Q37. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rule returns the median of an odd-length list of real numbers. To the list, append one number strictly smaller than every original entry and one strictly larger than every original entry. What follows about the returned median?

A. It is unchanged.  
B. It strictly increases.  
C. It becomes the average of the two appended numbers.  
D. It cannot be related to the original median without knowing every entry.  

### Q38. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange the sentences into a coherent paragraph.

P: This second reading was lower than the first.
Q: To check the surprising result, she repeated the measurement.
R: Mira measured the room's temperature using a newly calibrated sensor.
S: She therefore decided to investigate the conditions before reporting either value.

A. R,Q,P,S  
B. Q,R,S,P  
C. P,S,R,Q  
D. R,P,Q,S  

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A proposed proof that {a^n b^n : n≥0} is not regular takes pumping length p and word a^p b^p. Which statements correctly describe the regular-language pumping lemma argument?

**Candidates**

**I.** Every permitted decomposition with |xy|≤p and |y|>0 has y consisting only of a's.

**II.** Choosing the one convenient decomposition x=ε,y=a is sufficient by itself.

**III.** For every permitted decomposition, pumping y zero times produces a word outside the language.

**IV.** The pumping length may be chosen after seeing an arbitrary decomposition of an arbitrarily short word.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A Turing machine M is promised to halt on every input. A proposed procedure enumerates input strings and simulates M on each until it finds an accepted input. Which statements are correct?

**Candidates**

**I.** If L(M) is nonempty, this sequential procedure eventually finds an accepted input.

**II.** If L(M) is empty, the procedure eventually proves emptiness just by reaching a sufficiently long rejected input.

**III.** Totality of M makes each individual simulation finish.

**IV.** The promise supplies a finite maximum length beyond which no new accepted input can occur.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q41. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean inputs x,y,z, consider F=(x OR y) AND ((NOT x) OR z). Which statements are correct?

A. F=(x AND z) OR ((NOT x) AND y).  
B. The product term yz can be added to the expression in A without changing F.  
C. F is always equal to y AND z.  
D. When y=z, F equals that common value.  

### Q42. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In an ordinary BST with distinct keys, a node v has both children and its inorder successor s has a right child. Which statements are correct?

**Candidates**

**I.** s has no left child.

**II.** s must be v's immediate right child.

**III.** Removing s from its old position can reconnect its right child to s's former parent.

**IV.** s can have two children.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q43. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider formulas P:∀x∃y(x≠y) and Q:∃y∀x(x≠y), with equality interpreted normally over a nonempty domain. Which statements are correct?

**Candidates**

**I.** P is true on every domain with at least two elements.

**II.** Q is true on every domain with at least two elements.

**III.** Q is false on every nonempty domain, finite or infinite.

**IV.** P implies Q on every nonempty domain.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II  

### Q44. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A program over mathematical integers executes while(x!=0){x=2*x+1;} and then returns0. No value of x is observed afterward. An optimizer removes the loop because x is unused at the return. Which statements are correct?

A. For initial x=0, both versions return0.  
B. For initial x=1, the rewrite changes a nonterminating execution into a terminating one.  
C. Absence of a later use of x is sufficient to justify this rewrite for every input.  
D. Preserving termination behaviour matters for this transformation.  

### Q45. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary max-heap contains distinct keys 1 through 7 in an array indexed 1 through 7. The key 6 is at index 3. Which statement characterizes all possible positions of key 5?

A. It must be at index 2.  
B. It can be at any of indices 2,4,5,6,7.  
C. It can be at indices 2,6,7, and no others.  
D. It can be at index 1 or 2 only.  

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A system has one instance each of resources R and S. P holds R and waits for S. Q holds S and waits for R. Resources cannot be preempted, and neither process releases its held resource until its request is satisfied. Which single policy change directly breaks a necessary deadlock condition for this execution?

A. Raise both process priorities equally.  
B. Allow a waiting process's held resource to be forcibly reclaimed.  
C. Add another ready process that requests neither resource.  
D. Increase the CPU clock frequency.  

### Q47. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A link-state router retains, for each origin, only the advertisement with the highest sequence number. Sequence numbers do not wrap in this scenario. For origin X, it receives advertisements (sequence,link cost)=(41,5),(43,9),(42,2),(43,9). Which link cost from X remains in its database?

A. 2  
B. 5  
C. 9  
D. 25  

### Q48. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Grammar G has start symbol S and productions S→aSb | aS | epsilon. Which strings are generated?

**Candidates**

**I.** aab

**II.** abb

**III.** aaabb

**IV.** ba

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q49. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a directed simple graph on n labelled vertices, an adjacency matrix M stores M[u,v]=1 exactly when u→v exists. There are no self-loops. Which statements are correct?

**Candidates**

**I.** A diagonal entry of M² counts directed walks of length two returning to that vertex.

**II.** The sum of all entries of M always equals twice the number of directed edges.

**III.** Transposing M reverses every edge.

**IV.** A zero diagonal of M implies a zero diagonal of M².

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For real t consider

```text
x1 + x2 + x3 = 1
x1 + 2x2 + 3x3 = 2
2x1 + 3x2 + 4x3 = t
```

Which statements are correct?

A. The system is consistent exactly when t=3.  
B. When t=3, there are infinitely many solutions.  
C. Every solution satisfies x1=x3.  
D. When t=3, the coefficient matrix is invertible.  

---

## ANSWER KEY — SET 011

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, B, C |
| 2 | MSQ | 2 | A, C, D |
| 3 | MSQ | 1 | A, C, D |
| 4 | MCQ | 2 | A |
| 5 | MCQ | 2 | A |
| 6 | MCQ | 2 | B |
| 7 | MCQ | 1 | C |
| 8 | MCQ | 2 | D |
| 9 | MCQ | 1 | A |
| 10 | MCQ | 2 | C |
| 11 | MCQ | 2 | C |
| 12 | MSQ | 1 | A, B, D |
| 13 | MCQ | 2 | A |
| 14 | MCQ | 2 | B |
| 15 | MSQ | 1 | A, C, D |
| 16 | MSQ | 2 | A, C, D |
| 17 | MCQ | 2 | A |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 1 | A, B, D |
| 20 | MSQ | 1 | A, C, D |
| 21 | MSQ | 2 | A, C, D |
| 22 | MSQ | 1 | B, C, D |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 1 | B, C, D |
| 25 | MCQ | 2 | A |
| 26 | MCQ | 1 | B |
| 27 | MCQ | 1 | C |
| 28 | MCQ | 2 | D |
| 29 | MCQ | 2 | A |
| 30 | MCQ | 1 | B |
| 31 | MCQ | 1 | C |
| 32 | MSQ | 1 | A, B, D |
| 33 | MCQ | 2 | A |
| 34 | MCQ | 2 | B |
| 35 | MCQ | 1 | C |
| 36 | MCQ | 1 | D |
| 37 | MSQ | 1 | B, C, D |
| 38 | MSQ | 1 | B, C, D |
| 39 | MCQ | 2 | C |
| 40 | MCQ | 2 | D |
| 41 | MCQ | 2 | C |
| 42 | MCQ | 1 | B |
| 43 | MCQ | 1 | C |
| 44 | MCQ | 2 | C |
| 45 | MSQ | 2 | A, B, D |
| 46 | MSQ | 1 | A, C, D |
| 47 | MSQ | 1 | A, B, D |
| 48 | MCQ | 1 | D |
| 49 | MCQ | 1 | A |
| 50 | MCQ | 2 | D |
