# GATE CS — Additional Practice Set 007

**Questions:** 50  
**Maximum marks:** 75

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A fair coin selects one of two bags. Bag I contains 4 red and 2 blue balls; Bag II contains 2 red and 3 blue balls. Two balls are then drawn uniformly without replacement from the selected bag. Given that the two balls have the same colour, what is the probability that both are red?

A. 1/2  
B. 15/26  
C. 7/13  
D. 3/5  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Three processes P, Q and R use two initially empty pipes X and Y. Initially P owns X's write end and Y's read end; Q owns X's read end and Y's write end; R owns an additional copy of X's write end. No other descriptors for these pipes exist. A read-until-EOF operation returns only after all data has been consumed and every write descriptor for that pipe is closed. Pipe capacities exceed all data written here. All processes are eventually scheduled; there are no errors or signals.

- P writes one byte to X, closes its X writer, then reads Y until EOF, then terminates.
- Q reads X until EOF, then writes one byte to Y, closes its Y writer and terminates.
- R waits for P to terminate, then closes its X writer and terminates.

Which single change, with all other operations unchanged, is sufficient to ensure that all three processes terminate?

A. Increase the capacity of X.  
B. Have P wait for R to terminate immediately before P reads Y.  
C. Move R's close of the X writer to immediately before R waits for P.  
D. Have Q close its Y writer only after P terminates.  

### Q3. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Five distinct talks A,B,C,D,E are scheduled in positions 1 through 5. C is last. A occurs before C. Exactly one talk lies between B and D. E is neither first nor last. Which statements are true over schedules satisfying all these conditions?

A. A can be fourth.  
B. A must occur before E.  
C. E can be third.  
D. B and D must both occupy odd-numbered positions.  

### Q4. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two private hosts, 10.0.0.1 and 10.0.0.2, each initiate a TCP connection from local port 5000 to 203.0.113.8 port 443. A NAT gateway uses the single public IPv4 address 198.51.100.6 and assigns public source port 41001 to the connection from 10.0.0.1 and public source port 41002 to the connection from 10.0.0.2. Packets are unfragmented. Which statements are correct for this port-translating NAT?

A. A reply arriving at public port 41002 can be mapped back to 10.0.0.2 port 5000.  
B. The remote server sees both connections as originating from the respective private IPv4 addresses.  
C. Translating the source IPv4 address of an outgoing packet requires updating its IPv4 header checksum.  
D. Translating the source IPv4 address and TCP source port requires updating the TCP checksum because both affect its checksum calculation.  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A square sheet occupies 0≤x≤8, 0≤y≤8. Fold the right half onto the left along x=4, then fold the upper half onto the lower along y=4. A point hole is punched at (1,3) in the folded sheet through all layers. After unfolding, what is the greatest distance between two holes?

A. 6  
B. 2√10  
C. 8  
D. 4√5  

### Q6. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A parent creates a pipe and forks two children, both inheriting both pipe ends. The parent closes its write end and reads. Child I writes a finite message and closes both ends. Child II closes its read end but keeps its write end open indefinitely without writing. After consuming Child I's entire message, what happens to the parent's next blocking read, assuming no signals or errors?

A. It immediately returns end-of-file because Child I finished.  
B. It blocks because a write end remains open.  
C. It returns the last byte repeatedly.  
D. It necessarily raises a broken-pipe error.  

### Q7. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A dataset contains 1 twice, 3 three times and 7 once. Two additional observations, both equal to x, are added. The resulting mean is 4. Which statements are correct about the resulting eight observations?

A. x=7.  
B. The median is 3.  
C. There is a unique mode, 7.  
D. The range is 6.  

### Q8. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Starting with three empty page frames, process the reference string 1,2,3,1,4,2,5. Which statements are correct?

A. FIFO incurs five page faults.  
B. LRU incurs six page faults.  
C. This example proves FIFO never faults more often than LRU on any reference string.  
D. Increasing the frame count cannot increase LRU's faults for a fixed reference string starting empty.  

### Q9. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Over {0,1}, let L be denoted by the regular expression (0|11)*. Which statements are correct?

**Candidates**

**I.** Every maximal contiguous run of 1s in a string in L has even length.

**II.** Every binary string with an even total number of 1s belongs to L.

**III.** 110011 belongs to L.

**IV.** 101 belongs to L.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q10. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L be recognized by a Turing machine that may loop on nonmembers. A second machine enumerates all strings, simulates the recognizer on them by dovetailing, and prints a string when its simulation accepts. Which statements are correct?

**Candidates**

**I.** Every member of L is eventually printed.

**II.** The enumerator must halt when L is finite.

**III.** If L is empty, the enumerator may run forever without printing anything.

**IV.** Waiting for a fixed input to appear in this enumeration decides membership in L for every recognizable L.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q11. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A JK flip-flop obeys Q′=J(NOT Q)+(NOT K)Q. Which settings force the stated behaviour for both possible current values of Q?

A. J=0,K=0 holds Q unchanged.  
B. J=1,K=1 toggles Q.  
C. J=1,K=0 forces Q′=0.  
D. J=0,K=1 forces Q′=0.  

### Q12. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A switch is either ON or OFF. A says, “The switch is ON.” B says, “A's statement is false.” C says, “The switch is OFF.” Exactly two of the three statements are true. Which conclusions follow?

A. The switch is OFF.  
B. A and B are both truthful.  
C. B and C are truthful.  
D. The information is inconsistent.  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler may reuse the caller's activation record for a tail call when no work remains after the callee returns and no live local address must survive. Which recursive return expression is eligible under exact integers and ordinary call-by-value semantics, assuming the recursive call otherwise meets these conditions?

A. `return 1 + f(n-1);`  
B. `return f(n-1) * n;`  
C. `return f(n-1, acc*n);`  
D. `return g(f(n-1));`  

### Q14. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process blocks on an empty pipe while another process can eventually write to it. Which statements are correct under ordinary blocking I/O semantics?

**Candidates**

**I.** The blocked process need not consume CPU time by busy-waiting.

**II.** Blocking on the pipe necessarily means the whole system is deadlocked.

**III.** A successful write may make the reader runnable.

**IV.** The reader must be executing continuously for the writer to write.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, `char s[]="a\0bc";` is declared. What are sizeof(s) and strlen(s), respectively? The proper standard header is included.

A. (4,4)  
B. (5,1)  
C. (5,4)  
D. (4,1)  

### Q16. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A transaction reads row x twice. Another transaction commits a change to x between the reads. Which statements are correct?

**Candidates**

**I.** If the first transaction observes different committed values, this is a nonrepeatable read.

**II.** Such an observation necessarily means the first read saw uncommitted data.

**III.** Holding an appropriate shared lock on x throughout both reads prevents an intervening conflicting exclusive write lock under ordinary locking rules.

**IV.** A nonrepeatable read necessarily involves inserting a new row rather than updating x.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially X=Y=0. Transactions perform r1(X), r2(Y), w1(Y=1), w2(X=1), and then both commit. Each read sees the initial value. Which statement is correct?

A. The schedule is conflict serializable in order T1,T2.  
B. The schedule is conflict serializable in order T2,T1.  
C. The precedence graph has a cycle, and neither serial order reproduces both reads.  
D. No conflict exists because the writes target different items.  

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A combinational block receives two bits a,b and must output 1 exactly when the two-bit unsigned value is prime. Which output function is correct?

A. a  
B. b  
C. a XOR b  
D. a AND b  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, let `int a[4]={2,4,6,8}; int *p=a+1;`. Which expression evaluates to 6 without undefined behaviour?

A. *p++  
B. *(p+1)  
C. *p+1  
D. *(p-1)  

### Q20. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 4-to-1 multiplexer has select bits s1,s0 and data inputs D0=0,D1=x,D2=x′,D3=1. For which select settings is its output independent of x?

A. Only 00.  
B. Only 11.  
C. 00 and 11.  
D. 01 and 10.  

### Q21. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proof for L={aⁿbⁿcⁿ:n≥0} chooses aᵖbᵖcᵖ in the context-free pumping lemma. Why does |vxy|≤p help show every valid decomposition fails for some pumping exponent?

A. It forces v and y both to be empty.  
B. It prevents the pumpable region from spanning all three blocks, so pumping changes some counts without changing all three equally, or disrupts the block order.  
C. It forces the entire word to have length at most p.  
D. It proves the language finite.  

### Q22. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a standard B+ tree in which all data entries are stored at leaves, which statements hold?

**Candidates**

**I.** Internal separator keys can appear again at the leaf level.

**II.** All leaves are at the same depth.

**III.** Every successful lookup must stop at an internal separator without reaching any leaf.

**IV.** The root must always have exactly the same minimum occupancy as a nonroot internal node.

A. II and III  
B. I and II  
C. II and IV  
D. III and IV  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two consecutive instructions write the same register, and the younger instruction completes first in an out-of-order execution system. Which hazard must be handled to preserve the correct final register value?

A. Write-after-write.  
B. Read-after-read.  
C. A mandatory memory-address alignment fault.  
D. A control hazard caused by all register writes.  

### Q24. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A strict-priority preemptive scheduler always chooses a ready higher-priority job before a lower-priority one. A low-priority job is ready continuously. Which statements are true?

**Candidates**

**I.** An unending supply of higher-priority work can starve it.

**II.** Increasing its priority over time through an appropriate aging policy can address this starvation risk.

**III.** Its ready state alone guarantees it executes within one time quantum under the stated strict-priority policy.

**IV.** Preemption by itself guarantees bounded waiting for every priority level.

A. III and IV  
B. I and III  
C. I and IV  
D. I and II  

### Q25. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For grammar S→SS | a | ε, which statements are true?

**Candidates**

**I.** Its language is a*.

**II.** The word a has infinitely many distinct parse trees.

**III.** Every generated word has exactly one parse tree.

**IV.** The grammar is LL(1) as written.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

On domain {0,1}, let R(x,y) mean x=y. Which pair gives the truth values of ∀x∃y R(x,y) and ∃y∀x R(x,y), in that order?

A. False, false  
B. True, false  
C. False, true  
D. True, true  

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The panel vacillated between the two proposals, repeatedly reversing its tentative preference.” Which word best replaces vacillated without changing the meaning?

A. Wavered  
B. Collaborated  
C. Converged  
D. Disappeared  

### Q28. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed graph has edges s→a of weight 2, s→b of weight 5, b→a of weight −4, a→t of weight 3 and b→t of weight 1. A standard Dijkstra implementation finalizes vertices in increasing tentative-distance order, breaks the a/b/t ties by choosing t before b, never reopens a finalized vertex, and stops when t is finalized. Which statements are true?

**Candidates**

**I.** The true shortest s-to-t distance is 5.

**II.** The true shortest s-to-t distance is 4.

**III.** This graph contains a negative directed cycle.

**IV.** The specified implementation returns 5.

A. II and III  
B. III and IV  
C. I and II  
D. II and IV  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Suppose a hypothetical oracle correctly answers whether any supplied ordinary Turing machine halts on any supplied input. Fix an ordinary recognizer M of a language L. Which tasks become possible using this oracle?

**Candidates**

**I.** Decide whether any given word belongs to L by first querying whether M halts and, when it does, simulating its outcome.

**II.** Conclude that M must already halt on every word without querying the oracle.

**III.** Enumerate the complement of L by testing words one by one with the resulting oracle-assisted decision procedure.

**IV.** Replace all oracle calls by one universal fixed finite simulation-time bound for ordinary machines.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A bipartite graph has left vertices a,b,c and right vertices1,2,3. Its edges are a–1,a–2,b–2,c–2,c–3. Which statements are correct?

A. The graph has exactly one perfect matching.  
B. Removing edge a–2 destroys every perfect matching.  
C. Edge b–2 belongs to every perfect matching.  
D. Adding edge b–1 creates a second perfect matching.  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The committee's endorsement was qualified: it supported the proposal only if its cost was independently audited.” In this sentence, “qualified” most nearly means:

A. Awarded a professional certificate.  
B. Expressed subject to a reservation or condition.  
C. Withdrawn without explanation.  
D. Unconditionally enthusiastic.  

### Q32. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For variables a,b,c,d, f=1 exactly when a XOR b=1, independently of c,d. A conventional sum-of-products Karnaugh-map minimization uses cubes that do not cover a zero. Which statements are correct?

A. f has a two-product implementation (NOT a)b+a(NOT b).  
B. One product term is sufficient because eight of the sixteen inputs produce1.  
C. Each of the two displayed products covers four minterms.  
D. A valid product covering both(a,b)=(0,1) and(1,0) can omit both a and b without covering zeros.  

### Q33. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An interrupt handler increments a counter for every delivered interrupt. A device sets one pending bit whenever an event occurs; further events while that bit is1 do not accumulate. The handler clears the bit once on entry. Which statements are correct?

**Candidates**

**I.** The counter necessarily equals the number of device events.

**II.** Two events arriving before the handler clears the bit may cause only one counter increment.

**III.** Replacing the pending bit with an adequately sized event counter can preserve event multiplicity if updates and reads are synchronized correctly.

**IV.** Faster handler execution alone logically guarantees exact event counts for every possible event timing.

A. II and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q34. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In the subset lattice of {a,b,c}, ordered by inclusion, which statements are correct?

A. The meet of{a,b} and{b,c} is{b}.  
B. Their join is{a,b,c}.  
C. They are comparable.  
D. The empty set is a lower bound of every pair of elements.  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A NAT rewrites an outgoing IPv4 packet's source address and TCP source port. Assume ordinary checksums are used and no checksum offload is involved. Which statements are correct?

**Candidates**

**I.** The IPv4 header checksum must reflect the address change.

**II.** The TCP checksum may need updating because it covers the TCP header and an IP pseudo-header.

**III.** The TCP checksum covers only application payload, so ports are irrelevant.

**IV.** Changing an IPv4 address never affects transport-layer checksum calculation.

A. I and III  
B. I and IV  
C. I and II  
D. II and III  

### Q36. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A writer intends to compare the cost of repairing a machine with the cost of replacing that machine, not with the machine itself. Which sentence makes the comparison explicit and parallel?

A. Repairing the machine costs less than the replacement machine.  
B. The cost of repairing the machine is lower than that of replacing it.  
C. Repairing costs less than the machine is replaced.  
D. The machine is cheaper than repairing it costs less.  

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A Karnaugh-map group fixes variable a=1 and c=0 while leaving b and d free. Which statements are correct?

A. The group represents product a(NOT c).  
B. It covers four minterms.  
C. Its product must include b and d because they vary.  
D. It can legally include specified zero cells in an exact SOP implementation without don't-cares.  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An optimizer replaces a conditional assignment by unconditional arithmetic. In the original program, an expression on an untaken branch is not evaluated and may divide by zero if evaluated. Which statements are correct?

**Candidates**

**I.** Preserving the selected numerical result alone is enough to justify evaluating both branches.

**II.** Introducing a previously avoided invalid division can change program behavior.

**III.** A proof that both branch expressions are safe and side-effect-free is relevant to such a rewrite.

**IV.** Branch removal never changes which expressions are evaluated.

A. II and IV  
B. II and III  
C. III and IV  
D. I and II  

### Q39. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let u,v be nonzero real column vectors of length3 satisfying vᵀu=1, and let A=I−uvᵀ. Which statements are correct?

A. A is invertible.  
B. The nullspace of A is precisely the span of u.  
C. Ax=b is solvable exactly when vᵀb=0.  
D. A²=A.  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider proving that L={a^(n²) : n≥0} is not regular using pumping length p≥1 and word a^(p²). Which statements are correct?

**Candidates**

**I.** Every permitted pumping substring y has length d satisfying1≤d≤p.

**II.** Pumping y twice gives length p²+d, strictly between consecutive squares p² and(p+1)².

**III.** Choosing y of length0 is permitted and defeats the proof.

**IV.** The word's length is too small to invoke the lemma for any p≥1.

A. I and III  
B. I and IV  
C. II and III  
D. I and II  

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two identical resource instances exist. P holds one and Q holds the other; each waits for one additional instance and neither releases before obtaining it. There are no other processes. Which statements are correct?

**Candidates**

**I.** Both processes are blocked indefinitely under these rules.

**II.** Having multiple instances makes deadlock impossible.

**III.** Releasing one held instance could permit one process to finish, if that change were allowed.

**IV.** Each process already holds enough instances to satisfy its outstanding request without any release.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q42. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A four-variable function, with bit order A,B,C,D from most to least significant, is1 exactly at minterms0,2,8,10. Which statements are correct?

**Candidates**

**I.** These four minterms form a single valid four-cell Karnaugh-map group.

**II.** A must be fixed to one value throughout that group.

**III.** C must be fixed to one value throughout that group.

**IV.** The group is represented by (NOT B) AND (NOT D).

A. II and III  
B. I and IV  
C. II and IV  
D. III and IV  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A finite language contains no word longer than20 symbols. Why can21 serve as a pumping length in the necessary pumping condition for regular languages?

A. Every word in the language has a nonempty substring of length21.  
B. Every word of length21 must be in the language.  
C. There are no language words of length at least21 to which the pumping requirement applies.  
D. Pumping lengths may be chosen only for infinite languages.  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An inclusive two-level cache requires every block in L1 also to be present in L2. An exclusive design instead requires blocks resident in L1 to be absent from L2. Ignore other cache levels. Which statements are correct?

**Candidates**

**I.** Evicting an L2 block in the inclusive design may require invalidating its L1 copy.

**II.** An inclusive L1 miss can never be an L2 hit.

**III.** The exclusive design permits the same block to remain simultaneously in both levels by definition.

**IV.** Replication in the inclusive design can reduce the number of distinct resident blocks compared with equal-capacity exclusive levels.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q45. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A distance-vector router X has links of costs 2 and 5 to neighbors Y and Z. Before processing updates, their advertised distances to D are 4 and 1, respectively. Only Y then advertises distance 9. Using the latest advertisement from each neighbor and no other route to D, what should X advertise?

A. 4  
B. 6  
C. 11  
D. 14  

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language has lexically nested procedures. Procedure P contains Q and R; Q calls R. In a stack activation record for R, which relationship is correct under the usual static-link and dynamic-link model?

A. Both links point to Q's activation record.  
B. The static link identifies P's activation; the dynamic link identifies Q's activation.  
C. The static link identifies Q's activation; the dynamic link identifies P's activation.  
D. Both links identify P's activation regardless of the caller.  

### Q47. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A recursive depth-first search on a directed graph colors undiscovered vertices white, vertices on its active recursion stack gray, and finished vertices black. A currently explored edge is u→v. Which statements hold?

**Candidates**

**I.** If v is gray, the graph contains a directed cycle.

**II.** If v is black, u→v necessarily belongs to a directed cycle.

**III.** If no edge to a gray vertex is encountered during a full DFS forest, the graph is acyclic.

**IV.** If v is white, v must be an ancestor of u in the current DFS tree.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q48. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A table T(id,code) declares id as its primary key and code as NOT NULL, but code is not declared UNIQUE. Initially it contains(1,'X'),(2,'Y'). Which individual insertions, each considered independently on this original table, satisfy both stated constraints?

**Candidates**

**I.** (3,'X')

**II.** (2,'Z')

**III.** (4,NULL)

**IV.** (4,'Z')

A. II and IV  
B. III and IV  
C. I and II  
D. I and IV  

### Q49. [1 Mark] [MCQ]

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

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In tuple relational calculus, R(x) is a unary relation containing {1,2}. Consider the expression {x | NOT R(x)}, with x ranging over the entire interpretation domain. Which statements hold?

A. Over domain {1,2,3}, its result is {3}.  
B. Over domain {1,2,3,4}, its result is still {3}.  
C. Its result depends on values outside R, so it is not domain-independent.  
D. Replacing the formula by R(x) AND NOT R(x) yields a domain-independent empty result.  

---

## ANSWER KEY — SET 007

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 2 | A, C, D |
| 2 | MSQ | 2 | A, B, D |
| 3 | MSQ | 2 | B, D |
| 4 | MCQ | 2 | B |
| 5 | MSQ | 1 | A, C, D |
| 6 | MSQ | 1 | A, C, D |
| 7 | MCQ | 2 | C |
| 8 | MCQ | 2 | C |
| 9 | MCQ | 1 | A |
| 10 | MCQ | 2 | B |
| 11 | MCQ | 1 | C |
| 12 | MSQ | 2 | B, D |
| 13 | MSQ | 2 | A, B, D |
| 14 | MCQ | 1 | B |
| 15 | MSQ | 1 | A, C, D |
| 16 | MCQ | 2 | D |
| 17 | MSQ | 2 | A, B, D |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 1 | A, C, D |
| 20 | MSQ | 2 | A, B, D |
| 21 | MSQ | 2 | A, C, D |
| 22 | MCQ | 1 | B |
| 23 | MSQ | 1 | B, C, D |
| 24 | MCQ | 2 | D |
| 25 | MCQ | 2 | A |
| 26 | MSQ | 1 | A, C, D |
| 27 | MSQ | 1 | B, C, D |
| 28 | MCQ | 2 | D |
| 29 | MCQ | 2 | A |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | A, C, D |
| 32 | MSQ | 2 | B, D |
| 33 | MCQ | 2 | A |
| 34 | MCQ | 1 | C |
| 35 | MCQ | 1 | C |
| 36 | MSQ | 1 | A, C, D |
| 37 | MSQ | 2 | C, D |
| 38 | MCQ | 2 | B |
| 39 | MCQ | 2 | A |
| 40 | MCQ | 2 | D |
| 41 | MCQ | 1 | A |
| 42 | MCQ | 1 | B |
| 43 | MSQ | 1 | A, B, D |
| 44 | MCQ | 2 | D |
| 45 | MSQ | 1 | A, C, D |
| 46 | MSQ | 1 | A, C, D |
| 47 | MCQ | 1 | C |
| 48 | MCQ | 1 | D |
| 49 | MCQ | 1 | A |
| 50 | MCQ | 2 | B |
