# GATE CS — Additional Practice Set 015

**Questions:** 50  
**Maximum marks:** 73

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What does this C program print? Assume a conforming C implementation.

```c
#include <stdio.h>
int main(void) {
    int a[2][3] = {{2,4,6},{1,3,5}};
    int (*p)[3] = a;
    int *q = p[1];
    p[0][2] += q[1];
    int *r = p[0] + 1;
    *r++ = q[0];
    q[2] = *r;
    printf("%d\n", a[0][1] + a[1][2]);
    return 0;
}
```

A. 7  
B. 10  
C. 13  
D. The program has undefined behaviour.  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Table T(k,v) contains exactly these rows; NULL denotes the SQL null value, and duplicates are retained:
```text
(1,10), (1,NULL), (1,10), (2,NULL), (2,NULL), (3,5)
```
What rows, in any order, does the following standard SQL query return?
```sql
SELECT k, COUNT(*) AS n, COUNT(v) AS c
FROM T
GROUP BY k
HAVING COUNT(v) < COUNT(*) AND SUM(v) >= 10;
```

A. (1,3,2) only  
B. (1,3,2) and (2,2,0)  
C. (1,2,1) only  
D. No rows  

### Q3. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A binary floating-point system retains three significant binary digits, including the leading 1. Exponents are unbounded, and every result is rounded to nearest, ties to even. Which statements are correct?

**Candidates**

**I.** The exact value 1.125 rounds to 1.0.

**II.** Consecutive representable numbers in [2,4) are separated by 0.25.

**III.** Adding represented values 1.75 and 0.25 yields exactly 2.0.

**IV.** Every integer from 0 through 9 is represented exactly.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed multigraph has vertices 1,2,3 and the following adjacency matrix, where entry Mij is the number of distinct edges from i to j:

```text
M = [0 2 1]
    [1 0 1]
    [0 1 1].
```

Count the closed walks of length four that never traverse the same directed edge twice. Vertices may repeat, and opposite-direction edges are distinct. The two parallel edges from 1 to 2 are distinguishable. Count ordered edge sequences together with their starting vertex; cyclic rotations are counted separately whenever the resulting ordered sequences differ.

How many such walks exist?

A. 7  
B. 12  
C. 16  
D. 24  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Integer division discards the fractional part. What sequence is printed by visit(4)?

```text
visit(n):
    if n == 0: return
    visit(n / 2)
    print(n)
    visit((n - 1) / 2)
```

A. 1,2,1,4  
B. 1,2,4,1  
C. 4,2,1,1  
D. 1,2,3,4  

### Q6. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Parent(a,b) has the single row (1,2), with composite primary key (a,b). Child(a,b,qty) has a composite foreign key referencing Parent with MATCH SIMPLE, and CHECK(qty>0). All Child columns allow NULL. MATCH SIMPLE skips the referential check when either foreign-key component is NULL; a CHECK rejects only FALSE, not UNKNOWN. Starting with an empty Child table, which individual insertions succeed?

**Candidates**

**I.** (1,NULL,5)

**II.** (NULL,9,−1)

**III.** (9,9,NULL)

**IV.** (1,2,NULL)

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q7. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Routers A,B,D initially have link costs AD=1, BD=4, AB=1 and correct shortest-path routes to D. AD then changes to 10. A recomputes using the new complete link-state graph, while B temporarily retains its old table. What can happen to a packet for D forwarded by A during this interval?

A. It must follow A→D because A has a direct link.  
B. It can loop A→B→A until a table changes or the packet expires.  
C. It must follow A→B→D because B's direct link is unchanged.  
D. A correctly computed individual table makes transient loops impossible.  

### Q8. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A synchronous three-bit counter has transitions 0→1→2→3→4→5→0, and both unused states 6 and 7 transition to 0. Bits are q2q1q0 in binary. Which statements are correct?

A. From every initial bit pattern, the counter eventually enters the six-state cycle.  
B. An unused state remains unchanged until an external reset.  
C. On the steady cycle, q2 is 1 for one third of the clock intervals.  
D. On the steady cycle, q0 alternates at every clock edge.  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For the grammar S→aSb | bSa | ε, which description is exact?

A. All strings with equally many a and b symbols.  
B. All even-length palindromes over {a,b}.  
C. All strings whose second half is the symbolwise complement of the reverse of the first half.  
D. All strings of the form aⁿbⁿ only.  

### Q10. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four runners finish without ties. A finishes before B; C finishes after B; D finishes before C. Which runner can finish neither first nor last?

A. A  
B. B  
C. C  
D. D  

### Q11. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An undirected graph on A,B,C,D has edges AB=1, AC=2, BC=2, BD=3, CD=3, AD=4. Which statements are correct?

A. Every minimum spanning tree contains AB.  
B. Exactly four minimum spanning trees exist.  
C. The smallest spanning-tree weight strictly greater than the minimum is 8.  
D. Raising AD's weight from 4 to 100 leaves the set of minimum spanning trees unchanged.  

### Q12. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A binary min-heap stores seven distinct keys in indices 1–7, with children 2i and 2i+1. Which positions can contain the second-smallest key in some valid heap?

**Candidates**

**I.** 2

**II.** 3

**III.** 4

**IV.** 7

A. II and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q13. [1 Mark] [MCQ]

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

### Q14. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For L={aⁿbⁿ:n≥0}, choose w=aᵖbᵖ in a regular-language pumping-lemma proof, where p≥1. Which statements hold for every decomposition w=xyz with |xy|≤p and |y|>0?

A. y contains only a symbols.  
B. Pumping y twice preserves equal numbers of a and b.  
C. Pumping y zero times yields a word outside L.  
D. The proof may choose a decomposition that violates |xy|≤p.  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process is blocked solely waiting for a disk read. The read completes successfully while another process runs on the CPU. What is the usual immediate process-state transition for the waiting process?

A. Blocked to ready.  
B. Blocked to terminated.  
C. Blocked directly to running in every case.  
D. Ready to blocked.  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange the sentences into a coherent paragraph.

P. To distinguish these explanations, the researchers repeated the trial with freshly calibrated instruments.
Q. The repeated trial again found the increase, weakening the calibration explanation.
R. The first trial showed a temperature increase, but the team was unsure whether it was real or caused by instrument drift.
S. They therefore concluded that further investigation of the physical cause was warranted.

A. P–R–Q–S  
B. R–Q–P–S  
C. R–P–Q–S  
D. S–R–P–Q  

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“A library extended its opening hours. Evening attendance increased, but total daily attendance remained unchanged.” Which interpretation is consistent with both observations?

A. Some visits shifted from earlier hours to the evening.  
B. Total daily attendance necessarily increased.  
C. Earlier attendance necessarily increased too.  
D. The library must have measured attendance incorrectly.  

### Q18. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A partial DFA over {a,b} has states q0,q1,q2, start state q0, and accepting set {q2}. Its only transitions are q0 on a to q1, q1 on a to q2, and q2 on a to q2. Undefined transitions reject. What is the minimum number of states in a complete DFA recognizing the complement of its language over {a,b}*?

A. 4  
B. 3  
C. 5  
D. 6  

### Q19. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A function f is continuous on [0,2], differentiable on (0,2), and satisfies f(0)=f(2)=1. Which conclusions must hold?

**Candidates**

**I.** Some c∈(0,2) satisfies f′(c)=0.

**II.** f is constant on [0,2].

**III.** f attains both a maximum and a minimum on [0,2].

**IV.** f′(1)=0 necessarily.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In `t=a+b; c=d+e; u=a+b;`, variables a,b,c,d,e,t,u are distinct nonaliased scalars and arithmetic is exact. Which replacement is valid?

A. Replace the final a+b by t.  
B. Replace the final a+b by c for all inputs.  
C. Replace d+e by t for all inputs.  
D. Delete the first assignment and leave u=t with no definition of t.  

### Q21. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A recursive function has a local scalar variable x whose address is never returned or retained beyond its activation. Different recursive calls require separate x values until they return. Which allocation strategy directly supports this requirement?

A. A single global x shared by every activation with no saving.  
B. One x slot in each activation record on the runtime stack.  
C. No storage because recursion forbids locals.  
D. One immutable constant substituted for x in every call regardless of assignments.  

### Q22. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A variable x is live after statement `x = y+z`. Which statement describes the liveness transfer across this assignment, ignoring other live variables?

A. Old x must remain live before the statement solely because new x is live after it.  
B. Old x is killed by the assignment, while y and z are used and become live before it.  
C. y and z are killed because they appear on the right-hand side.  
D. The statement cannot define x because x is already live.  

### Q23. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A producer sends messages through an operating-system queue and a consumer receives them. Which statements distinguish message passing from directly accessing an ordinary shared variable?

**Candidates**

**I.** Communication uses send/receive operations on messages.

**II.** A messaging interface can transfer data between distinct address spaces.

**III.** Message passing necessarily makes every application free of race conditions.

**IV.** All message passing must use busy waiting.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A system's measured cache hit rate rises after an optimization, but its clock period also increases. Which conclusion is justified without further data?

A. Total execution time necessarily decreases.  
B. Hit rate alone is insufficient to establish an execution-time improvement.  
C. The instruction count must become zero.  
D. A higher hit rate necessarily implies a shorter clock period.  

### Q25. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A programming language permits arbitrarily nested comments, with tokens OPEN and CLOSE marking comment boundaries. Why is a fixed finite-state lexer, with no extra stack or counter, insufficient to recognize exactly the balanced comment sequences of unbounded depth?

A. It would need to distinguish arbitrarily many outstanding OPEN counts.  
B. Every finite input requires infinitely many processing steps.  
C. The two-token alphabet is infinite.  
D. All non-nested comments are also nonregular by definition.  

### Q26. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let F(x,y,z)=xy+yz+zx using Boolean AND and OR. Define its Boolean difference with respect to x as F(0,y,z) XOR F(1,y,z). Which statements are correct?

**Candidates**

**I.** The difference equals y+z.

**II.** The difference equals y XOR z.

**III.** The difference is independent of x.

**IV.** The difference equals yz.

A. I and III  
B. II and III  
C. I and IV  
D. II and IV  

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For the following straight-line code, which variables are live immediately after the second statement? Use ordinary syntactic liveness on this code as written, before dead-code elimination; there are no implicit uses at return.

```text
x = a+b
y = x*c
x = d
return y
```

**Candidates**

**I.** x

**II.** d

**III.** c

**IV.** y

A. I and IV  
B. II and III  
C. II and IV  
D. III and IV  

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four events are A, data collection; B, instrument calibration; C, result certification; D, publication. The only constraints are A before C, B before C and C before D. Which lists exactly the possible chronological orders?

A. ABCD only  
B. ABCD and BACD  
C. ACBD and BCAD  
D. All 24 permutations  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A disk uses SSTF. Its head starts at track 0 with requests pending at tracks 1 and 100. Each time it services track 1 a fresh request for track 0 arrives immediately, and each time it services track 0 a fresh request for track 1 arrives immediately. No other requests arrive; service takes zero time and movement is positive time. Which statements are true?

**Candidates**

**I.** The track-100 request can remain unserved forever under this arrival pattern.

**II.** SSTF guarantees a finite waiting bound solely because it selects the nearest request.

**III.** A fixed finite request set with no new arrivals can reproduce this infinite starvation while each service removes one request.

**IV.** The continued supply of nearby requests is essential to this particular starvation construction.

A. I and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A connected TCP socket receives application writes of lengths3 and5 bytes from its peer. The receiver calls recv with a buffer of8 bytes. Assume no errors and no end-of-stream, but allow arbitrary legal timing. Which statement is correct?

A. The first recv must return exactly3 bytes.  
B. The first recv must return exactly8 bytes.  
C. A successful positive return may contain bytes spanning both writes.  
D. The receiver can infer write boundaries from TCP's byte stream alone.  

### Q31. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For0/1 knapsack, an implementation uses one array dp[c], initially zero. For each item of positive weight w and value v, it updates dp[c]=max(dp[c],dp[c−w]+v). Which statements are correct?

A. Scanning c downward from capacity to w prevents reuse of the current item.  
B. Scanning upward can allow the same item to be used repeatedly.  
C. Either direction always computes the0/1 optimum.  
D. With a single item of weight2 and value3 and capacity4, an upward scan gives dp[4]=6.  

### Q32. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A simple undirected graph has six vertices, every vertex has degree3, and the graph is bipartite. Which statements must hold?

A. Each bipartition class has three vertices.  
B. The graph is connected.  
C. The graph is isomorphic to K3,3.  
D. The graph has a triangle.  

### Q33. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language L satisfies the regular pumping lemma's conclusion for some pumping length. What can be concluded from this fact alone?

A. L is regular, since the condition is sufficient.  
B. L is context-free but not regular.  
C. It does not by itself prove regularity; the lemma supplies a necessary condition.  
D. L must be finite.  

### Q34. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In this code, p points to a valid integer object, f may modify that object, and integer arithmetic does not overflow:

```text
u = *p + 2
call f()
v = *p + 2
```

Which statements are correct?

**Candidates**

**I.** Identical text proves v may be replaced by u.

**II.** A proof that f cannot modify the pointed-to object can make that reuse valid.

**III.** If f changes the object, the two evaluations may differ.

**IV.** A function call is never relevant to memory-expression availability.

A. III and IV  
B. II and III  
C. I and II  
D. I and III  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under strict two-phase locking, exclusive locks are retained until commit or abort. Which statements are correct?

**Candidates**

**I.** Another transaction cannot read an item modified under an unreleased exclusive lock.

**II.** Retaining exclusive locks prevents cascading aborts caused by reading those uncommitted writes.

**III.** The rule alone makes deadlock impossible.

**IV.** A transaction may release an exclusive lock immediately after its write under this strict rule.

A. I and III  
B. I and IV  
C. I and II  
D. II and III  

### Q36. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A programming language specifies that every evaluation of a volatile memory read is observable, even if the returned values happen to be equal. For two successive expressions x=read_volatile(p) and y=read_volatile(p), which statements are correct?

**Candidates**

**I.** Equal returned values alone justify replacing the second read by y=x.

**II.** Such replacement removes an observable operation.

**III.** Ordinary expression-value equality is insufficient for this optimization.

**IV.** Volatile reads are guaranteed never to return equal values.

A. I and III  
B. I and IV  
C. II and IV  
D. II and III  

### Q37. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A cover-minimization procedure has two feasible covers: C1 uses two rows with total cost8; C2 uses three rows with total cost6. Each is assumed optimal for the count/cost pair shown, and no other cover improves either objective. Which statements are correct?

A. Minimizing row count first and total cost second selects C1.  
B. Minimizing total cost first and row count second selects C2.  
C. The two objectives necessarily choose the same cover.  
D. Reporting only “minimum cover” without specifying the objective can be ambiguous here.  

### Q38. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

At entry to a block, x and y have defined values. The block is:

```text
x = y + 1
z = x + y
return z
```

No other use follows. Which statements are correct under standard liveness analysis?

**Candidates**

**I.** The incoming value of x is live at block entry.

**II.** The incoming value of y is live at block entry.

**III.** Immediately after the first assignment, both x and y are live.

**IV.** Immediately after the second assignment, y is live.

A. II and IV  
B. II and III  
C. III and IV  
D. I and II  

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A school introduces an optional tutoring programme. Students who chose it scored higher on average than those who did not. No information is available about their earlier scores or reasons for enrolling. Which statements follow from this description?

**Candidates**

**I.** Participation and the observed scores are associated in this sample.

**II.** The comparison alone does not isolate the causal effect of tutoring.

**III.** Tutoring necessarily caused every participant's score to increase.

**IV.** The participants and nonparticipants necessarily had identical prior achievement.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Processes P and Q communicate through a finite-capacity pipe. P writes until the pipe is full; Q still has an open read end but never reads. Assume blocking writes and no signals or failures. Which statements are correct?

**Candidates**

**I.** P may block on a further write.

**II.** Keeping a read end open guarantees that Q consumes bytes.

**III.** Closing all read ends changes the situation from merely having a full pipe.

**IV.** A finite buffer guarantees completion for an arbitrarily large write workload even if Q never reads.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q41. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n a positive perfect square, determine the tight asymptotic number of loop iterations as n grows. Arithmetic and floor-square-root evaluation each take constant time.

```text
i = 1
while i < n:
    i = i + floor(sqrt(i))
```

A. Θ(log n)  
B. Θ(n)  
C. Θ(n log n)  
D. Θ(sqrt(n))  

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

G is a finite group of odd order, with identity e. An element x satisfies x^4=e and x^6=e. Which statements must hold?

**Candidates**

**I.** x=e.

**II.** x has order2.

**III.** x²=e.

**IV.** x has order3.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DNS configuration contains only the alias records alpha→beta and beta→alpha for the names being resolved, with neither leading to an address record. Which conclusion is appropriate?

A. The resolver can infer an address from either name's spelling.  
B. Following these aliases cycles and cannot produce an address from these records alone.  
C. Two aliases necessarily cancel, yielding the client's own address.  
D. The resolver must return whichever address it used for its previous unrelated query.  

### Q44. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A narrative says: “The team archived the original readings before recalibrating the instrument. It then repeated the measurements. Only after this repetition did it compare the two sets of readings.” Which event necessarily happened immediately before the comparison among the three later events mentioned?

A. Archiving the original readings  
B. Repeating the measurements  
C. Recalibrating the instrument  
D. Discarding the original readings  

### Q45. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic PDA has a designated set of final states. Acceptance by final state requires all input to be consumed, and the stack may remain nonempty. Which assertions are valid?

**Candidates**

**I.** Every language accepted by such a machine is context-free.

**II.** Every context-free language can be accepted by some deterministic PDA.

**III.** A nondeterministic PDA can accept the same language using empty-stack acceptance instead.

**IV.** Simply declaring all states final always preserves the accepted language.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Host H sends an IPv4 packet through two routers to host J. Each link uses Ethernet, and there is no NAT, tunneling, or fragmentation. Which statements hold for normal forwarding?

**Candidates**

**I.** The source and destination Ethernet addresses can change at each routed hop.

**II.** The source and destination IPv4 addresses change at every routed hop.

**III.** The IPv4 TTL decreases at each router that forwards the packet.

**IV.** An Ethernet destination address on the first link must be J's Ethernet address even when J is on another subnet.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV  

### Q47. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={a^(n²):n≥0}. For an assumed pumping length p≥1, choose z=a^(p²) and consider any valid regular-pumping decomposition z=uvw with1≤|v|≤p. Which argument correctly shows that pumping v twice leaves L?

A. The new length p²+|v| lies strictly between p² and(p+1)².  
B. The new length must be a prime number.  
C. The new length is always(p+1)².  
D. The new length is smaller than p².  

### Q48. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Procedure outer contains local variable x and returns an inner function that later reads x. The language permits that returned function to be called after outer returns. Which statements hold for a correct implementation?

**Candidates**

**I.** The lifetime of captured x must extend beyond outer's return when the returned function still needs it.

**II.** A pointer into an already reclaimed stack frame always suffices to implement the returned function.

**III.** An environment stored outside the reclaimed stack frame can preserve x.

**IV.** The inner function must read a new unrelated variable named x from its caller's frame.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes the keyword `in`, identifiers matching [a-z]+, and the single-character token '.'. It uses longest match, giving the keyword priority over an identifier only when their matched lengths tie. What token-type sequence is produced on input `in.inner`?

A. keyword, '.', identifier.  
B. identifier, '.', keyword, identifier.  
C. keyword, '.', keyword, identifier.  
D. identifier, '.', identifier.  

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A parent creates a pipe and forks one child. Both processes initially inherit both ends. The child reads until EOF. The parent writes a finite message, closes its own write descriptor, and waits for the child; the child has forgotten to close its inherited write descriptor. No other processes hold the pipe. Which statements are correct?

**Candidates**

**I.** After draining the message, the child can block waiting for EOF.

**II.** The parent's close alone guarantees EOF at the child.

**III.** Closing the child's inherited write end before its read loop permits EOF once the parent's write end closes and buffered bytes are drained.

**IV.** The parent waiting for the child automatically closes the child's descriptors.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

---

## ANSWER KEY — SET 015

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C, D |
| 2 | MSQ | 2 | B, C, D |
| 3 | MCQ | 1 | C |
| 4 | MSQ | 2 | A, C, D |
| 5 | MSQ | 1 | A, C, D |
| 6 | MCQ | 2 | B |
| 7 | MSQ | 1 | A, C, D |
| 8 | MCQ | 2 | B |
| 9 | MSQ | 1 | A, B, D |
| 10 | MSQ | 1 | A, C, D |
| 11 | MCQ | 2 | C |
| 12 | MCQ | 1 | D |
| 13 | MCQ | 1 | A |
| 14 | MSQ | 2 | B, D |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 2 | A, B, D |
| 17 | MSQ | 1 | B, C, D |
| 18 | MSQ | 2 | B, C, D |
| 19 | MCQ | 1 | C |
| 20 | MSQ | 1 | B, C, D |
| 21 | MSQ | 2 | A, C, D |
| 22 | MSQ | 2 | A, C, D |
| 23 | MCQ | 1 | C |
| 24 | MSQ | 1 | A, C, D |
| 25 | MSQ | 2 | B, C, D |
| 26 | MCQ | 2 | B |
| 27 | MCQ | 1 | C |
| 28 | MSQ | 1 | A, C, D |
| 29 | MCQ | 2 | A |
| 30 | MSQ | 1 | A, B, D |
| 31 | MCQ | 1 | C |
| 32 | MCQ | 1 | D |
| 33 | MSQ | 2 | A, B, D |
| 34 | MCQ | 2 | B |
| 35 | MCQ | 1 | C |
| 36 | MCQ | 1 | D |
| 37 | MCQ | 1 | C |
| 38 | MCQ | 1 | B |
| 39 | MCQ | 2 | C |
| 40 | MCQ | 2 | D |
| 41 | MSQ | 2 | A, B, C |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 1 | A, C, D |
| 44 | MSQ | 1 | A, C, D |
| 45 | MCQ | 2 | A |
| 46 | MCQ | 2 | B |
| 47 | MSQ | 2 | B, C, D |
| 48 | MCQ | 1 | D |
| 49 | MSQ | 1 | B, C, D |
| 50 | MCQ | 2 | B |
