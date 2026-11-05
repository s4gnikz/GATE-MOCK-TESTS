# GATE CS 2027 — Full-Length Mock Test 022

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; other questions carry two marks. An MCQ has exactly one correct option; an incorrect MCQ loses one-third of its marks. An MSQ requires all correct options, without partial credit or negative marking. NATs have no negative marking. Unattempted questions score zero. General Aptitude carries15 marks, Engineering Mathematics13 and core CS72. Numerical answers are exact unless a precision is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Exactly one of three boxes contains a coin. Their labels state: A: “The coin is not in B”; B: “The coin is in this box”; C: “The coin is not in this box.” Exactly one label is true. Where is the coin?

A. Box A
B. Box B
C. Box C
D. The conditions have no solution.

### Q2. [1 Mark] [NAT]

A point is rotated180 degrees about(1,0), then180 degrees about(0,2). Starting at(3,4), what is the squared distance between its initial and final positions?

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

A study reports that among applicants who passed a competitive screening, experience and examination score were negatively associated. The screening favoured applicants with either strong experience or a high score. Which conclusion is justified by this description alone?

A. Experience causes lower examination scores in all applicants.
B. Restricting attention to screened applicants may create an association absent in the full applicant pool.
C. The screening must have ignored experience.
D. No applicant can have both strong experience and a high score.

### Q4. [1 Mark] [NAT]

Four distinct people sit around a circular table. Rotations are considered identical, but reflections are different. Two specified people must sit opposite each other. How many seating arrangements are possible?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

A college's pass rates in both departments increased from one year to the next, but its overall pass rate decreased. Which explanation is possible?

A. The departmental statements and overall statement are mathematically incompatible.
B. The fraction of candidates in the department with the lower pass rate increased sufficiently.
C. The number of departments necessarily increased.
D. Every candidate must have changed departments.

### Q6. [2 Marks] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left along x=4, then the top half down along y=4. Through all layers cut out the rectangle[1,3]×[0,1] of the folded sheet. Unfold the sheet. What is the total area removed from the original sheet?

**Answer format:** Integer square units.

### Q7. [2 Marks] [NAT]

Four paragraphs describe events on the same day. P describes a noon alarm, Q a10:00 repair, R a14:00 report and S a09:00 inspection. They currently appear in order P,Q,R,S. An editor must put them in chronological order and may exchange only two adjacent paragraphs in one operation. What is the minimum number of exchanges required?

**Answer format:** Integer.
### Q8. [2 Marks] [NAT]

Three cards labelled1,2,3 are shuffled uniformly. Cards are revealed until card3 appears, including card3. What is the expected sum of the labels revealed?

**Answer format:** Exact number.

### Q9. [2 Marks] [MCQ]

“The agreement is provisional, not irrevocable; either side may withdraw before the inspection, but neither may withdraw afterward.” Which statement follows?

A. The agreement never binds either side.
B. Withdrawal is permitted after inspection if both sides remain provisional.
C. The right to withdraw exists before inspection and ends afterward.
D. Inspection automatically cancels the agreement.

### Q10. [2 Marks] [NAT]

A population triples at the end of every complete day. Another population doubles at the end of every complete day and initially has eight times as many members as the first. What is the first integer day at whose end the first population is larger?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

For three Boolean variables a,b,c, the on-set is {000,001} and the don't-care set is {010,011}; every other input is in the off-set. Among prime implicants that cover at least one on-set input, how many literals does the largest such cube contain?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

A simple undirected graph has six vertices, every vertex has degree3, and the graph is bipartite. Which statements must hold?

A. Each bipartition class has three vertices.
B. The graph is connected.
C. The graph is isomorphic to K3,3.
D. The graph has a triangle.

### Q13. [1 Mark] [NAT]

A complete DFA has states0,1,2. Reading a sends0→1,1→2,2→2. Reading b leaves every state unchanged. A reset word sends all three possible starting states to the same state. What is the length of a shortest reset word?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

A directed weighted graph has edges s→a(1), a→a(−1), s→t(5), and no others. Distances refer to walks, which may repeat vertices. Which statements are correct?

A. There is a finite shortest-walk distance from s to t, equal to5.
B. Every vertex reachable from s has a finite shortest-walk distance.
C. A negative cycle reachable from s need not make the s-to-t distance unbounded below.
D. The negative self-loop can be inserted into a walk from s to t.

### Q15. [1 Mark] [NAT]

A nondecreasing array is[1,2,2,2,4,7], with indices0–5. A binary search for the first index with value at least2 uses a half-open search interval[l,r), initially[0,6), and updates r=mid when A[mid]≥2, otherwise l=mid+1, where mid=floor((l+r)/2). How many array-element comparisons occur before l=r?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A B+ tree has height3, meaning a root-to-leaf search reads three nodes including the root and leaf. Internal nodes are not cached. A range query starts in one leaf and continues through two successive leaves using leaf links. No leaf is revisited. How many node reads are needed, including the initial search?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

How many binary strings of length4 contain exactly one occurrence of the substring00? Occurrences may overlap; for example,0001 contains two occurrences.

**Answer format:** Integer.
### Q18. [1 Mark] [MSQ]

A database permits uncommitted updates to reach disk and uses an undo log. Before overwriting an on-disk data item, its old value is forced into the log. Which statements are correct?

A. The log-before-data rule supplies information needed to undo an uncommitted on-disk update.
B. Writing the old value to the log only after overwriting the disk item is equally safe against a crash between those writes.
C. A transaction's abort may require restoring disk data, not merely clearing a memory buffer.
D. The stated rule by itself proves that every committed update is already on disk.

### Q19. [1 Mark] [MCQ]

A NAT keeps an expiring UDP mapping from an internal endpoint to a public endpoint. After it expires, the same public endpoint is assigned to a different internal endpoint. A delayed incoming datagram addressed to the reused public endpoint then arrives. Assume mapping lookup uses only the destination public endpoint. Which statement is correct?

A. The datagram necessarily reaches the original internal endpoint.
B. The NAT can deliver it to the newly mapped endpoint because the datagram carries no mapping-generation identifier used by this lookup.
C. UDP sequence numbers universally prevent this.
D. The mapping can never expire while datagrams are delayed.

### Q20. [1 Mark] [NAT]

For grammar S→S | a, how many distinct finite parse trees generate a and contain at most three applications of S→S?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A TCP sender has congestion window6000 bytes, advertised receive window4500 bytes and3000 unacknowledged bytes. It has unlimited data ready, and no other sending restriction applies. How many additional bytes may it send without a new acknowledgment or window update?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A process incurs three page faults in sequence. Each fault reads one page from disk; the first and third evict dirty pages, while the second evicts a clean page. No writes are merged or deferred. How many page-sized disk transfers occur in total?

**Answer format:** Integer.

### Q23. [1 Mark] [MCQ]

A lexer recognizes unsigned integer tokens, the operator '-', and identifiers. It tokenizes x--12 without treating '--' as a separate operator. The parser alone distinguishes unary and binary minus. Which token sequence is produced?

A. identifier(x), minus, integer(−12)
B. identifier(x), minus, minus, integer(12)
C. identifier(x−−12)
D. identifier(x), decrement, integer(12)

### Q24. [1 Mark] [NAT]

A memory has eight banks. Word address a maps to bank a modulo8. A program repeatedly accesses addresses3,9,15,21,... with stride6. How many distinct banks are visited before the bank sequence repeats?

**Answer format:** Integer.

### Q25. [1 Mark] [MSQ]

Grammar S→aA | aB, A→b, B→c is rewritten as S→aX, X→A | B, A→b, B→c. Which statements are correct?

A. Both grammars generate exactly {ab,ac}.
B. The rewritten grammar can choose between X→A and X→B using one lookahead token.
C. The original grammar's two S alternatives have disjoint FIRST sets.
D. Left factoring necessarily removes ambiguity from every ambiguous grammar.

### Q26. [1 Mark] [NAT]

A file's inode initially has two hard links and one open file descriptor referring to it. Both hard links are removed. There are no other references, and reclamation occurs only when link count and open-reference count are both zero. How many further reference-removing operations are needed before the inode can be reclaimed?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

Linear probing in a hash table stores keys whose home slot is4 in slots4,5,6. Slot7 is empty. The key in slot5 is deleted. Which deletion action preserves ordinary probing searches for the key in slot6, if searches stop at a never-used empty slot?

A. Mark slot5 as never-used empty without moving keys.
B. Mark slot5 with a tombstone that searches pass through.
C. Clear slot6 as well.
D. Change only the deleted key's hash function.

### Q28. [1 Mark] [MSQ]

T1 holds an exclusive lock on x and requests y. T2 holds an exclusive lock on y and requests x. No locks are released until commit or abort. Which statements are correct?

A. Both transactions can remain blocked indefinitely without intervention.
B. Aborting either transaction and releasing all its locks can allow the other to proceed.
C. Two-phase locking makes this wait cycle impossible.
D. Both transactions must commit simultaneously to resolve it.

### Q29. [1 Mark] [NAT]

Let A(x)=(1+x²)/(1−x), interpreted as a formal power series. What is the coefficient of x³ in A(x)²?

**Answer format:** Integer.
### Q30. [1 Mark] [NAT]

In C, assume unsigned int has exactly16 value bits and arithmetic on it is modulo65536. What value is printed?

```c
unsigned int x = 65535u;
unsigned int y = x + 2u;
printf("%u", y);
```

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

A cache lookup takes2 ns. A miss adds60 ns after that lookup. A stream contains100 accesses; exactly10 miss, and no overlap is allowed. An optimization removes five misses but adds1 ns to every lookup. What is the net reduction in total time, in ns?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

A3-to-8 decoder has active-high outputs and an active-high enable. Two such decoders form a4-to-16 decoder, sharing the lower three address bits. One is enabled by the highest address bit and the other by its complement. For each valid stable input, how many of the sixteen outputs are high?

**Answer format:** Integer.

### Q33. [1 Mark] [MSQ]

Over a nonempty domain, consider propositions F=(for every x, P(x) OR Q(x)) and G=((for every x, P(x)) OR (for every x, Q(x))). Which statements are correct?

A. G implies F.
B. F implies G in every interpretation.
C. A two-element domain can make F true and G false.
D. F and G are equivalent when the domain has one element.

### Q34. [1 Mark] [NAT]

A3×3 matrix A has determinant5. Matrix B is obtained by interchanging A's first and third rows and then multiplying its second column by−2. What is det(B)?

**Answer format:** Exact number.

### Q35. [1 Mark] [NAT]

The procedure below uses a global integer g, initially0, and call-by-value n.

```text
F(n):
    if n == 0: return
    g = g + n
    F(n-1)
    g = g - 1
```

What is g after F(4) returns?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

An ER model has entity Building with key building_id and weak entity Room with partial key room_no. Each Room belongs to exactly one Building; room_no is unique within a building but may repeat across buildings. Which statements are correct for the relational mapping?

A. The pair(building_id,room_no) can identify Room rows.
B. room_no alone is necessarily a candidate key of Room.
C. A non-null foreign key from Room.building_id to Building implements the required owner reference, together with the appropriate Room key.
D. Removing building_id from Room loses information needed to distinguish equally numbered rooms in different buildings.

### Q37. [2 Marks] [MCQ]

What is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = 1
    while j <= i:
        for k = 1 to j:
            work()
        j = 2*j
```

A. Θ(n log n)
B. Θ(n²)
C. Θ(n² log n)
D. Θ(log² n)

### Q38. [2 Marks] [NAT]

A translation for binary digit strings synthesizes attributes len and val. A single bit b has len=1,val=b; concatenating strings X,Y gives len=X.len+Y.len and val=X.val·2^(Y.len)+Y.val. The parsed representation of101.101 treats the parts on either side of the point as separate strings and returns left.val+right.val/2^(right.len). What value is returned?

**Answer format:** Exact decimal.

### Q39. [2 Marks] [MSQ]

Relations R(A,B)={(1,x),(1,y),(2,x)} and S(A,B)={(1,x)} use set semantics. Compare E1=projection_A(R−S) and E2=projection_A(R)−projection_A(S). Which statements are correct?

A. E1={1,2}.
B. E2={2}.
C. Projection always distributes over set difference.
D. The surviving tuple(1,y) explains why1 belongs to E1 but not E2.

### Q40. [2 Marks] [MCQ]

A0/1 knapsack has capacity10 and items(weight,value)=(6,12),(5,9),(5,9), each available once. A heuristic scans items in decreasing value/weight order and takes an item whenever it fits. Which statement is correct?

A. The heuristic obtains12, while the optimum is18.
B. The heuristic obtains18, while the optimum is12.
C. Both obtain21 by splitting an item.
D. The heuristic cannot choose any item.

### Q41. [2 Marks] [NAT]

A cache starts empty, has two sets with two ways each, and uses LRU within each set. Block b maps to set b modulo2. Compare reference sequences0,2,4,0,2,4 and0,3,6,0,3,6. Each reference accesses one block, and the cache is reset between sequences. How many more misses occur in the first sequence than in the second?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

An interrupt handler increments a counter for every delivered interrupt. A device sets one pending bit whenever an event occurs; further events while that bit is1 do not accumulate. The handler clears the bit once on entry. Which statements are correct?

A. The counter necessarily equals the number of device events.
B. Two events arriving before the handler clears the bit may cause only one counter increment.
C. Replacing the pending bit with an adequately sized event counter can preserve event multiplicity if updates and reads are synchronized correctly.
D. Faster handler execution alone logically guarantees exact event counts for every possible event timing.

### Q43. [2 Marks] [MSQ]

For x≠0 define g(x)=sin(1/x). Which statements are correct?

A. There exists a sequence of positive x approaching0 on which g(x)=1.
B. There exists a sequence of positive x approaching0 on which g(x)=−1.
C. The limit of xg(x) as x approaches0 is0.
D. Assigning g(0)=0 makes g continuous at0.

### Q44. [2 Marks] [NAT]

A server's TCP application uses a protocol consisting of a two-byte unsigned big-endian payload length followed by that many payload bytes. The input stream begins with byte values0,3,65,66,67,0,2,68,69. The application's first read returns the first four bytes; its second returns all remaining bytes. After processing both reads, how many complete protocol messages can it extract?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A synchronous circuit has two D flip-flops with state(a,b), initialized to(0,1). Its next state is(a XOR b,a), using old values simultaneously. An output pulse occurs on an edge exactly when the old state is(1,0). How many output pulses occur during the first eight clock edges?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

X is uniform on {−1,0,1}, and Y=X². Which statements are correct?

A. Cov(X,Y)=0.
B. X and Y are independent.
C. E[Y]=2/3.
D. Knowing Y=0 determines X exactly.

### Q47. [2 Marks] [NAT]

A nonnegative fixed-point value x=11/16 is first rounded to two fractional binary bits, then rounded again to one fractional binary bit. Each rounding uses nearest, ties to even, with enough integer bits. Compare this with rounding x directly to one fractional binary bit. What is the two-stage result minus the direct result?

**Answer format:** Exact decimal.

### Q48. [2 Marks] [NAT]

A DNS cache is initially empty. A successful lookup at time t stores an answer with TTL10 seconds and negligible lookup latency. It is usable for times s with t≤s<t+10; cache hits do not refresh TTL. Requests arrive at times0,4,9,10,19,20 seconds. Every miss is resolved immediately and cached under the same rule. How many upstream lookups occur?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

Matrices A,B,C have dimensions10×2,2×20,20×3. Scalar multiplication count for multiplying an r×s matrix by an s×t matrix is rst. How many scalar multiplications are saved by choosing the cheaper parenthesization of ABC instead of the more expensive one?

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

A proposed PDA for L={a^n b^n : n≥0} pushes for every a and pops for every b, rejects an attempted pop from empty, and accepts at end exactly when the stack is empty. It has no state recording whether b's have begun, so it allows pushing after popping. Which statements are correct?

A. It accepts abab, which is outside L.
B. Adding a phase distinction that forbids a after the first b can repair the order constraint.
C. Its empty-stack condition alone guarantees all a's precede all b's.
D. It rejects aabb.

### Q51. [2 Marks] [NAT]

On A={1,2,3,4}, let τ interchange1 and2 and fix3 and4. How many functions f:A→A satisfy f(τ(x))=τ(f(x)) for every x?

**Answer format:** Integer.
### Q52. [2 Marks] [MSQ]

A link layer detects corrupted frames using a checksum but, by assumption, may silently discard any frame and performs no retransmission. An application requires delivery of its complete message. Which statements are correct?

A. Link error detection alone guarantees the application's delivery requirement.
B. An end-to-end acknowledgment and retransmission mechanism can address losses beyond a single link, subject to the network eventually allowing communication.
C. A valid link checksum proves the entire application message has arrived.
D. Detection of corruption and recovery from loss are different functions.

### Q53. [2 Marks] [NAT]

A process opens the same regular file twice in two separate successful open calls, obtaining descriptors p and q. No append mode is used. It reads4 bytes through p, seeks q to absolute offset7, then reads2 bytes through p. All reads succeed fully. What is the sum of the file offsets associated with p and q afterward?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

Unary relations R and S are finite. Compare query F={x : R(x) AND NOT S(x)} with query G={x : NOT S(x)} over an unrestricted infinite domain. Which statements are correct?

A. F is contained in the active domain of R.
B. G can return infinitely many values.
C. The occurrence of NOT makes F necessarily unsafe.
D. Positive range restriction by R is relevant to F's domain independence.

### Q55. [2 Marks] [MSQ]

A contiguous row-major array A has3 rows and5 columns of four-byte elements, without padding. A transpose view B has5 rows and3 columns and maps B[i,j] to A[j,i], without copying data. Which statements are correct?

A. Increasing i by1 at fixed j advances the element address by4 bytes.
B. Increasing j by1 at fixed i advances the element address by20 bytes.
C. B is contiguous in its own row-major traversal order.
D. Writing B[2,1] changes the same stored element as A[1,2].
### Q56. [2 Marks] [MSQ]

A procedure returns a nested function that references a local variable of the procedure. The language permits calling that function after the procedure returns. Which statements are correct?

A. The referenced variable's storage must remain valid for the later call.
B. A raw pointer into an ordinary reclaimed stack frame always suffices.
C. A closure can carry access to a separately retained environment.
D. Lexical scope alone implies that every activation record may be discarded immediately on return without preserving anything.

### Q57. [2 Marks] [MSQ]

Let R be regular and C be context-free over the same alphabet. Which statements hold for every such pair?

A. C∩R is context-free.
B. C−R is context-free.
C. R−C is necessarily context-free.
D. C∪R is context-free.

### Q58. [2 Marks] [NAT]

In an expression DAG, equal leaves and identical operator nodes with identical ordered children are shared. Commutativity is not used. For expression(a+b)*(a+b)+(b+a), how many binary-operator nodes are present?

**Answer format:** Integer.

### Q59. [2 Marks] [MCQ]

A language L satisfies the regular pumping lemma's conclusion for some pumping length. What can be concluded from this fact alone?

A. L is regular, since the condition is sufficient.
B. L is context-free but not regular.
C. It does not by itself prove regularity; the lemma supplies a necessary condition.
D. L must be finite.

### Q60. [2 Marks] [NAT]

In a singly linked structure, head reaches a path of length3 edges before first entering a cycle of length4. Floyd's algorithm starts slow and fast at head and, in each iteration, advances slow by one edge and fast by two, then compares them. How many iterations occur before the first equality?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

A five-stage scalar pipeline uses IF,ID,EX,MEM,WB, one cycle per stage, and has full forwarding except that a load's result becomes available only at the end of MEM. The sequence is load r1,[a]; add r2,r1,r3; add r4,r2,r5. With separate instruction/data memories and no other stalls, how many cycles are required from the first IF through the last WB?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A binary floating-point system has precision p=3 significant bits, minimum normal exponent−2, and gradual underflow. Normal positive values have the form1.bb×2^e, with e≥−2. Subnormal values use the same spacing as the smallest normal binade. Under rounding to nearest, ties to even, what value represents3/32?

**Answer format:** Exact decimal.
### Q63. [2 Marks] [MSQ]

A process has two threads sharing ordinary process resources. One thread changes a global variable and opens a file. Which statements are correct under the conventional process/thread model?

A. The other thread can access the same global variable, subject to synchronization requirements.
B. The threads necessarily have separate virtual address spaces.
C. The open descriptor belongs to a process-wide descriptor table shared by the threads.
D. Each thread normally has its own execution stack and register context.

### Q64. [2 Marks] [NAT]

A real2×2 matrix A has eigenvalues2 and3. What is det(A²−5A+7I)?

**Answer format:** Exact number.

### Q65. [2 Marks] [MSQ]

A bounded buffer has capacity2 and is initially empty. A semaphore empty starts at2, full at0, and mutex at1. A consumer mistakenly executes wait(mutex), then wait(full), and retains mutex while blocked. A producer executes wait(empty), then wait(mutex) before inserting. Which statements are correct if the consumer runs first?

A. The consumer can block while holding mutex.
B. The producer can then block on mutex while unable to insert the item that would release the consumer.
C. Increasing the buffer capacity alone fixes this ordering bug for an initially empty buffer.
D. Having the consumer wait(full) before wait(mutex) avoids this particular hold-and-wait cycle.


---

## ANSWER KEY — MOCK TEST 022

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 20 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 2 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 8 |
| 7 | NAT | 2 | 4 |
| 8 | NAT | 2 | 4.5 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 6 |
| 11 | NAT | 1 | 1 |
| 12 | MSQ | 1 | A, B, C |
| 13 | NAT | 1 | 2 |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 3 |
| 16 | NAT | 1 | 5 |
| 17 | NAT | 1 | 5 |
| 18 | MSQ | 1 | A, C |
| 19 | MCQ | 1 | B |
| 20 | NAT | 1 | 4 |
| 21 | NAT | 1 | 1500 |
| 22 | NAT | 1 | 5 |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 4 |
| 25 | MSQ | 1 | A, B |
| 26 | NAT | 1 | 1 |
| 27 | MCQ | 1 | B |
| 28 | MSQ | 1 | A, B |
| 29 | NAT | 1 | 8 |
| 30 | NAT | 1 | 1 |
| 31 | NAT | 1 | 200 |
| 32 | NAT | 1 | 1 |
| 33 | MSQ | 1 | A, C, D |
| 34 | NAT | 1 | 10 |
| 35 | NAT | 1 | 6 |
| 36 | MSQ | 2 | A, C, D |
| 37 | MCQ | 2 | B |
| 38 | NAT | 2 | 5.625 |
| 39 | MSQ | 2 | A, B, D |
| 40 | MCQ | 2 | A |
| 41 | NAT | 2 | 3 |
| 42 | MSQ | 2 | B, C |
| 43 | MSQ | 2 | A, B, C |
| 44 | NAT | 2 | 2 |
| 45 | NAT | 2 | 3 |
| 46 | MSQ | 2 | A, C, D |
| 47 | NAT | 2 | 0.5 |
| 48 | NAT | 2 | 3 |
| 49 | NAT | 2 | 820 |
| 50 | MSQ | 2 | A, B |
| 51 | NAT | 2 | 16 |
| 52 | MSQ | 2 | B, D |
| 53 | NAT | 2 | 13 |
| 54 | MSQ | 2 | A, B, D |
| 55 | MSQ | 2 | A, B, D |
| 56 | MSQ | 2 | A, C |
| 57 | MSQ | 2 | A, B, D |
| 58 | NAT | 2 | 4 |
| 59 | MCQ | 2 | C |
| 60 | NAT | 2 | 4 |
| 61 | NAT | 2 | 8 |
| 62 | NAT | 2 | 0.125 |
| 63 | MSQ | 2 | A, C, D |
| 64 | NAT | 2 | 1 |
| 65 | MSQ | 2 | A, B, D |



