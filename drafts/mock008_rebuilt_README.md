# GATE CS 2027 — Full-Length Mock Test 008

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all others carry two marks. MCQs have one correct option; MSQs have multiple correct options and require the complete correct set, with no partial credit. An incorrect MCQ loses one-third of its marks. Incorrect MSQ/NAT answers and unattempted questions receive zero. Follow the stated NAT precision. General Aptitude contributes 15 marks, Engineering Mathematics 13, and core CS 72. Unless specified otherwise, arithmetic is exact and all stated operations complete successfully.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“The new procedure reduced measurement variability but did not change the mean measurement.” Which conclusion is supported?

A. Every new measurement equals the old mean.
B. New measurements are less dispersed under the reported variability measure.
C. The mean measurement became zero.
D. The old procedure must have been biased.

### Q2. [1 Mark] [NAT]

A number leaves remainder 2 when divided by 5 and remainder 3 when divided by 7. What is the smallest positive such number?

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

The word “qualified” in “The reviewer offered qualified support for the proposal” most nearly means:

A. Entirely unconditional
B. Subject to reservations or conditions
C. Expressed by an untrained person
D. Legally prohibited

### Q4. [1 Mark] [NAT]

A rectangular sheet is folded once along its vertical midline, making two layers, and then once along the horizontal midline of the folded rectangle, making four layers. A small circular hole is punched strictly inside the four-layer region, away from all fold lines and boundaries. How many separate holes appear after complete unfolding?

**Answer format:** Integer.

### Q5. [1 Mark] [MSQ]

Every sensor that passed calibration was installed. Some installed sensors were not tested. Which statements follow necessarily?

A. Every sensor not installed failed to pass calibration.
B. Every installed sensor passed calibration.
C. At least one installed sensor was not tested.
D. No untested sensor passed calibration.

### Q6. [2 Marks] [NAT]

A candidate answers 40 one-mark MCQs. Of these, 30 are correct and 10 incorrect; each incorrect answer loses 1/3 mark. The candidate also answers 20 two-mark MCQs. What is the minimum number of correct answers among those 20 needed for a total score of at least 50? Every remaining answer among the 20 is incorrect and loses 2/3 mark.

**Answer format:** Integer.

### Q7. [2 Marks] [MCQ]

A square's side is increased by 10%. A circle's radius is increased by 10%. Which pair gives the percentage increases in their areas?

A. 10%,10%
B. 20%,20%
C. 21%,21%
D. 21%,10%

### Q8. [2 Marks] [NAT]

An urn contains three red and three blue balls. Two balls are drawn without replacement. If they have different colours, a prize of 6 units is paid; otherwise nothing is paid. What is the expected prize?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MCQ]

Three tasks A,B,C take 4,3,2 hours. A and B may run simultaneously on separate workers, but C requires both to have finished and uses one worker. Exactly two workers are available and tasks cannot be split. What is the minimum completion time for all tasks?

A. 5 hours
B. 6 hours
C. 7 hours
D. 9 hours

### Q10. [2 Marks] [NAT]

Eight people are arranged uniformly at random in a circle. Rotations are treated as the same arrangement. What is the probability that two specified people sit adjacent? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A sequential detector emits a pulse when the latest three input bits are 101, allowing overlapping matches. It reads 10101 from left to right, starting with no previous bits. How many pulses are emitted?

A. 1
B. 2
C. 3
D. 5

### Q12. [1 Mark] [MSQ]

An eight-bit pattern is interpreted either as sign-magnitude or as two's complement. Which statements are correct?

A. 10000000 denotes zero in sign-magnitude.
B. 10000000 denotes −128 in two's complement.
C. Both representations assign the same value to every pattern with leading bit 1.
D. Both assign the same value to every pattern with leading bit 0.

### Q13. [1 Mark] [NAT]

How many permutations f of {1,2,3,4} satisfy f(f(x))=x for every x and have exactly two fixed points?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

Let A have rows (1,1),(1,1). Find trace(A⁵).

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

In C, assuming the proper standard header and successful allocation, which statement about `int *p=malloc(3*sizeof *p);` is correct before any initialization of the allocated int objects?

A. All three int values are guaranteed to be zero.
B. The allocated storage persists until it is freed, even if the local pointer variable leaves scope.
C. sizeof *p evaluates an indeterminate pointed-to int value.
D. The allocation contains exactly three bytes on every implementation.

### Q16. [1 Mark] [NAT]

A binary search repeatedly compares the target with a midpoint key, returning on equality and otherwise searching the appropriate remaining half. Midpoint is floor((low+high)/2). On the sorted keys 1 through 15, how many key comparisons find target 14?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

A language L is accepted by a DFA. Which operations always produce another regular language?

A. Reverse every word of L.
B. Take the complement of L over the same alphabet.
C. Intersect L with an arbitrary context-free language.
D. Concatenate L with itself.

### Q18. [1 Mark] [MCQ]

The grammar S→aSb | ε is used by a predictive parser. On valid input aabb, what is the maximum number of unconsumed b terminals simultaneously present on its stack, excluding input and the end marker?

A. 1
B. 2
C. 3
D. 4

### Q19. [1 Mark] [NAT]

A process has four virtual pages mapped to physical frames [7,2,7,9], respectively. Each physical frame occupies 4 KiB. How many KiB of distinct physical-frame storage do these mappings reference?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

A tree has eight vertices of degree 3, five vertices of degree 2, and all remaining vertices of degree 1. How many leaves does it have?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

Evaluate the limit as n tends to infinity of Σ(k=1 to n) n/(n²+k²). Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q22. [1 Mark] [MCQ]

SQL table T(x) contains 2,2,3,NULL. What pair is returned by `SELECT COUNT(*), COUNT(x) FROM T`?

A. (4,3)
B. (3,3)
C. (4,2)
D. (2,2)

### Q23. [1 Mark] [NAT]

An application sends 2400 bytes using three UDP datagrams, each with 800 application bytes. Each datagram adds an 8-byte UDP header and a 20-byte IPv4 header. No fragmentation occurs. How many total IPv4 bytes are transmitted?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

A full adder receives inputs x,y and carry-in c. Its sum output is x XOR y XOR c. If x=y=1, what are its sum and carry-out as functions of c?

A. (c,1)
B. (NOT c,1)
C. (c,c)
D. (0,c)

### Q25. [1 Mark] [NAT]

A machine fetches a 32-bit instruction using a 16-bit-wide memory interface. Each memory transfer takes one cycle and provides two adjacent bytes. The instruction is aligned to a two-byte boundary, and no overlapping or caching occurs. How many cycles are required to fetch it?

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

For a binary tree, preorder and inorder traversals are both A,B,C,D with distinct labels. Which statements are correct?

A. The root is A.
B. Every node except D has only a right child.
C. Every node except D has only a left child.
D. The postorder is D,C,B,A.

### Q27. [1 Mark] [NAT]

X is uniform on [−1,1], and Y=X². Find Var(Y), rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q28. [1 Mark] [MCQ]

An algorithm outputs every unordered pair of distinct elements from an n-element input, with one constant-time operation per emitted pair. What is the tight asymptotic lower bound arising from output size alone?

A. Ω(log n)
B. Ω(n)
C. Ω(n log n)
D. Ω(n²)

### Q29. [1 Mark] [NAT]

A DFA has exactly one accepting state, which is its initial state. Every input symbol moves it to a rejecting sink that loops on every symbol. Over a two-symbol alphabet, how many words does it accept?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

In a three-address representation, evaluate `a+b*c` with normal multiplication precedence, without algebraic reordering. Which sequence is suitable?

A. t1=a+b; t2=t1*c
B. t1=b*c; t2=a+t1
C. t1=a*c; t2=t1+b
D. t1=a+b; t2=b*c

### Q31. [1 Mark] [MSQ]

A process blocks on an empty pipe while another process can eventually write to it. Which statements are correct under ordinary blocking I/O semantics?

A. The blocked process need not consume CPU time by busy-waiting.
B. Blocking on the pipe necessarily means the whole system is deadlocked.
C. A successful write may make the reader runnable.
D. The reader must be executing continuously for the writer to write.

### Q32. [1 Mark] [NAT]

Relations R(A)={1,2,3} and S(B)={x,y} use set semantics. How many tuples remain in their Cartesian product after removing every tuple whose A component equals 2?

**Answer format:** Integer.

### Q33. [1 Mark] [MCQ]

Two machines are on the same ordinary Ethernet broadcast domain. A host broadcasts an ARP request for its default gateway's IPv4 address. What is it principally trying to learn?

A. The gateway's Ethernet address on that LAN.
B. The remote web server's TCP sequence number.
C. The gateway's complete routing table.
D. The DNS name of every host on the LAN.

### Q34. [1 Mark] [NAT]

A Boolean function of five variables is independent of its fifth variable and is 1 on exactly six assignments of the first four variables. On how many full five-variable assignments is it 1?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

A direct-mapped cache has four lines. Block b maps to line b mod 4. Which pair of distinct blocks can coexist in this cache?

A. 1 and 5
B. 2 and 6
C. 3 and 7
D. 4 and 5

### Q36. [2 Marks] [NAT]

Starting from an empty queue, execute enqueue 1, enqueue 2, dequeue, enqueue 3, enqueue 4, dequeue, enqueue 5. Transfer the remaining queue elements to an initially empty stack by repeatedly dequeuing and pushing. Then pop the entire stack and interpret the emitted digits as a decimal integer. What integer is obtained?

**Answer format:** Integer.

### Q37. [2 Marks] [MCQ]

A comparison sorting algorithm sorts n distinct keys. Its decision tree has binary comparison outcomes. Which is a valid worst-case lower-bound argument?

A. There are n possible outputs, so height is at least log₂n.
B. There are n! possible input orders requiring different sorting permutations, so height is at least ceil(log₂(n!)).
C. Every sorting algorithm must use exactly n² comparisons.
D. Each comparison places one key permanently, so n comparisons always suffice.

### Q38. [2 Marks] [MSQ]

Define L={aⁱbʲ:i,j≥0 and i≠j}. Which statements are correct?

A. L is context-free.
B. L is regular.
C. The complement of L within a*b* is {aⁿbⁿ:n≥0}.
D. ε belongs to L.

### Q39. [2 Marks] [NAT]

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

### Q40. [2 Marks] [NAT]

A system has three page frames and initially no resident pages. It uses optimal replacement with knowledge of the future. For references 1,2,3,4,1,2,5,1,2,3,4,5, how many page faults occur?

**Answer format:** Integer.

### Q41. [2 Marks] [MCQ]

R(A,B,C,D) has FDs A→B, B→C, C→D. Which decomposition is both lossless and dependency preserving?

A. AB, BC, CD
B. AB, CD
C. AC, BD
D. AD, BC

### Q42. [2 Marks] [NAT]

An IPv4 packet with 4000 payload bytes and a 20-byte header crosses a link with MTU 1500. It is fragmented using the fewest fragments and the largest possible payload in each nonfinal fragment. What is the fragment-offset field of the final fragment? Offsets are in eight-byte units.

**Answer format:** Integer.

### Q43. [2 Marks] [MSQ]

An n-bit ripple-carry adder has a carry dependency from each bit to the next. Each stage's carry propagation takes one time unit; inputs are available at time zero. Ignore sum-output delays. Which statements are correct?

A. The final carry may require n time units.
B. All carries necessarily settle within one time unit because the stages are physically parallel.
C. Grouping carry logic using additional gates can reduce carry depth compared with a ripple chain.
D. Increasing n never changes worst-case carry delay.

### Q44. [2 Marks] [NAT]

A tournament on four labelled vertices has exactly one directed edge between each pair. How many of the 2⁶ tournaments are strongly connected?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A 2 GHz processor executes 10⁹ instructions with average CPI 1.2. A compiler transformation reduces instruction count by 20% but increases average CPI to 1.4. What is the execution-time reduction in milliseconds at the same clock frequency?

**Answer format:** Integer.

### Q46. [2 Marks] [MCQ]

Build a max-heap in place from the one-indexed array [1,2,3,4,5,6,7] using bottom-up heap construction: process indices 3,2,1, and at each index repeatedly swap the current element with its larger child while heap order is violated. Count only swaps of two array elements. How many swaps are performed in total?

A. 2
B. 4
C. 3
D. 5

### Q47. [2 Marks] [NAT]

In an undirected graph with vertices s,a,b,t, edges have weights sa=1,sb=1,ab=0,at=1,bt=1. A path must be simple, so it cannot repeat vertices. How many shortest s-to-t paths exist?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

For L={aⁿbⁿ:n≥0}, choose w=aᵖbᵖ in a regular-language pumping-lemma proof, where p≥1. Which statements hold for every decomposition w=xyz with |xy|≤p and |y|>0?

A. y contains only a symbols.
B. Pumping y twice preserves equal numbers of a and b.
C. Pumping y zero times yields a word outside L.
D. The proof may choose a decomposition that violates |xy|≤p.

### Q49. [2 Marks] [MCQ]

A basic block ends with `x=a+b; y=x*c; x=0; return y;`, using exact scalar arithmetic and no externally observable intermediate assignments. Which first assignment is dead solely because x is overwritten later?

A. x=a+b is dead.
B. y=x*c is dead.
C. Neither of these assignments is dead: y uses the first x value and return uses y.
D. Both are dead.

### Q50. [2 Marks] [MSQ]

Two processes use a shared counting semaphore initialized to 0. P executes `signal(s); signal(s);`, while Q executes `wait(s); wait(s); print();`. There are no other accesses. Which statements are correct?

A. If both processes are eventually scheduled and semaphore operations are correct, Q can eventually print.
B. The two signals collapse into a single remembered event.
C. Q may block on its first wait depending on scheduling.
D. Q must print before P executes its second signal.

### Q51. [2 Marks] [NAT]

Independent trials produce symbols A,B,C with probabilities 1/2,1/3,1/6. Starting with none seen, what is the expected number of trials until all three symbols have appeared?

**Answer format:** Exact finite decimal.

### Q52. [2 Marks] [NAT]

For relation R(A,B,C,D), F={AB→C, C→D, D→A}. How many candidate keys does R have?

**Answer format:** Integer.

### Q53. [2 Marks] [MCQ]

A TCP receiver advertises zero window because its buffer is full. The network has no loss. Which statement is correct?

A. The sender should interpret this as proof that a router dropped a packet.
B. Receiver flow control currently prevents ordinary new data from exceeding that advertised allowance.
C. The receiver has permanently closed the TCP connection.
D. The sender's congestion window must become exactly zero immediately.

### Q54. [2 Marks] [NAT]

How many Boolean functions of three labelled variables depend essentially on all three variables? A variable is essential if changing only that variable changes the function value for at least one assignment of the other variables.

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A data-only L1 cache holds two blocks; a unified L2 holds three. Both are fully associative with LRU replacement and initially empty. L2 is inclusive: evicting a block invalidates any L1 copy. A data L1 miss accesses L2 and updates its LRU order; an L1 hit does not access L2. Instruction accesses bypass L1 and access/update only L2. Every L2 miss fetches one block from memory. Accesses are data A, data B, data A, instruction C, instruction D, data A. All block labels are distinct. How many memory block fetches occur?

**Answer format:** Integer memory block fetches.

### Q56. [2 Marks] [MSQ]

Let p point to the first element of an array of five ints. Which pointer expressions are permitted to be formed in C? No dereference is performed.

A. p+4
B. p+5
C. p+6
D. (p+5)-2

### Q57. [2 Marks] [NAT]

Jobs have unit processing time and pairs (deadline,profit): A=(1,20), B=(2,15), C=(2,30), D=(3,10). At most one job is executed in each integer slot, and a job in slot k meets deadline d when k≤d. All jobs are available initially. What is the maximum total profit from jobs completed by their deadlines?

**Answer format:** Integer.

### Q58. [2 Marks] [MCQ]

A language L is both recognizable and co-recognizable. Given recognizers for L and its complement, how can a decider be constructed?

A. Run the recognizer for L forever and reject if it has not accepted after any fixed universal timeout.
B. Dovetail the two recognizers and decide according to which accepts first.
C. Reject all strings because nontermination is possible.
D. Reverse the transitions of the recognizer for L.

### Q59. [2 Marks] [NAT]

For the grammar S→ABc, A→a | ε, B→AD | b, D→d | ε, with start S, how many distinct terminal symbols belong to FOLLOW(A)? The end marker is not a terminal symbol.

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

Two identical CPUs schedule four nonpreemptive jobs, all arriving at time 0. Jobs A and B, with bursts 4 and 3, can run only on CPU 0. Job D, with burst 2, can run only on CPU 1. Job C, with burst 2, can run on either CPU. There is no I/O or switching overhead and jobs cannot migrate once started. What is the minimum possible sum of all four ready-queue waiting times?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

A schedule is `r1(x), w1(x), r2(x), c1, c2`, where T2 reads the value written by T1. Which statements are correct?

A. It is recoverable.
B. It is cascadeless.
C. T2 could require cascading rollback if T1 aborted before its displayed commit instead.
D. T2 commits before T1 in the displayed schedule.

### Q62. [2 Marks] [NAT]

A protocol numbers bytes modulo 2ⁿ and sends continuously at 1 MiB/s (1 MiB=2²⁰ bytes). It requires strictly more than 12 seconds before any sequence number is reused. Its sender window must hold at least one second of traffic and must be strictly smaller than half the sequence space. What is the smallest integer n satisfying both requirements?

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

A synchronous counter cycles through exactly five distinct states and then repeats. Which statements are correct?

A. At least three binary storage bits are needed.
B. Exactly five flip-flops are necessary for every encoding.
C. A three-bit encoding has at least three unused binary patterns.
D. Every unused pattern necessarily recovers to the valid cycle without any next-state design constraint.

### Q64. [2 Marks] [MSQ]

A and B are real 4×4 matrices, each of rank 3. Which statements are correct?

A. rank(AB) is at least 2.
B. rank(AB) can be 3.
C. rank(AB) can be 1.
D. rank(AB) can be 2.

### Q65. [2 Marks] [NAT]

For f(x)=x ln x on x>0, draw its tangent at x=a, where a>e⁻¹. That tangent and the two coordinate axes enclose a triangle. What is the smallest possible triangle area? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

## ANSWER KEY — MOCK TEST 008

Integer and exact-decimal answers are exact; ranges for rounded values are shown explicitly.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 17 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 4 |
| 5 | MSQ | 1 | A, C |
| 6 | NAT | 2 | 14 |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 3.6 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 0.2857 (range 0.28565–0.28575) |
| 11 | MCQ | 1 | B |
| 12 | MSQ | 1 | A, B, D |
| 13 | NAT | 1 | 6 |
| 14 | NAT | 1 | 32 |
| 15 | MCQ | 1 | B |
| 16 | NAT | 1 | 3 |
| 17 | MSQ | 1 | A, B, D |
| 18 | MCQ | 1 | B |
| 19 | NAT | 1 | 12 |
| 20 | NAT | 1 | 10 |
| 21 | NAT | 1 | 0.7854 (range 0.78535–0.78545) |
| 22 | MCQ | 1 | A |
| 23 | NAT | 1 | 2484 |
| 24 | MCQ | 1 | A |
| 25 | NAT | 1 | 2 |
| 26 | MSQ | 1 | A, B, D |
| 27 | NAT | 1 | 0.0889 (range 0.08885–0.08895) |
| 28 | MCQ | 1 | D |
| 29 | NAT | 1 | 1 |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | A, C |
| 32 | NAT | 1 | 4 |
| 33 | MCQ | 1 | A |
| 34 | NAT | 1 | 12 |
| 35 | MCQ | 1 | D |
| 36 | NAT | 2 | 543 |
| 37 | MCQ | 2 | B |
| 38 | MSQ | 2 | A, C |
| 39 | NAT | 2 | 3 |
| 40 | NAT | 2 | 7 |
| 41 | MCQ | 2 | A |
| 42 | NAT | 2 | 370 |
| 43 | MSQ | 2 | A, C |
| 44 | NAT | 2 | 24 |
| 45 | NAT | 2 | 40 |
| 46 | MCQ | 2 | B |
| 47 | NAT | 2 | 4 |
| 48 | MSQ | 2 | A, C |
| 49 | MCQ | 2 | C |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 7.3 |
| 52 | NAT | 2 | 3 |
| 53 | MCQ | 2 | B |
| 54 | NAT | 2 | 218 |
| 55 | NAT | 2 | 5 |
| 56 | MSQ | 2 | A, B, D |
| 57 | NAT | 2 | 60 |
| 58 | MCQ | 2 | B |
| 59 | NAT | 2 | 4 |
| 60 | NAT | 2 | 5 |
| 61 | MSQ | 2 | A, C |
| 62 | NAT | 2 | 24 |
| 63 | MSQ | 2 | A, C |
| 64 | MSQ | 2 | A, B, D |
| 65 | NAT | 2 | 0.3679 (range 0.36785–0.36795) |




