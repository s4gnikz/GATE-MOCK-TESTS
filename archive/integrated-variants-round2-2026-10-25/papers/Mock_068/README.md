# GATE CS 2027 — Full-Length Mock Test 068

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

A sequence starts with a1=1 and satisfies a(n+1)−a(n)=2n+1 for n≥1. For how many n in {1,...,10} is a(n+1)−a(n) greater than a(n)?

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A right triangle has perpendicular sides 6 cm and 8 cm. What is the altitude from its right-angle vertex to its hypotenuse?

**Answer format:** Exact finite decimal centimetres.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange these events into the only order consistent with their stated dependencies: P: restore a backup after locating the fault; Q: test the restored system; R: locate the fault using diagnostic logs; S: reopen access only after the test succeeds.

A. P,R,Q,S  
B. R,P,S,Q  
C. R,P,Q,S  
D. Q,R,P,S

### Q4. [1 Mark] [NAT]

A service receives orders of two kinds, X and Y. Initially, 40% of the orders are X. Exactly 25% of X orders and 10% of Y orders are cancelled; all remaining orders are completed. What percentage of completed orders are X? Round to two decimal places.

**Answer format:** Numeric value; 2 decimal places.

### Q5. [1 Mark] [MSQ]

Four switches P,Q,R,S are either ON or OFF. Exactly two are ON. Whenever P is ON, Q is ON. Whenever R is OFF, S is ON. Which statements must hold?

A. P is OFF.
B. At least one of R and S is ON.
C. Q is ON.
D. If Q is OFF, both R and S are ON.

### Q6. [2 Marks] [NAT]

A square has vertices(0,0),(2,0),(2,2),(0,2). It is rotated90 degrees anticlockwise about(1,1) and then translated by(3,−1). What is the sum of the x-coordinates of its four resulting vertices?

**Answer format:** Integer.

### Q7. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Read the passage: “The library extended evening hours and then recorded a rise in visits per week. During the same period, a nearby reading room closed. Visitor surveys were voluntary and were collected only during the new evening hours. Most respondents said that the extended hours were useful.” Which statements are justified?

**Candidates**

**I.** The observed increase by itself identifies the extended hours as the sole cause.

**II.** The reading-room closure is a possible alternative contributor to the increase.

**III.** The survey directly estimates the views of all local residents without selection concerns.

**IV.** The survey results are compatible with visitors outside the new hours having different views.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q8. [2 Marks] [NAT]

A committee of four is selected from five engineers and three designers. It must contain at least two engineers and at least one designer. How many committees are possible?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

A service runs in two regions. In region X, 80% of requests succeed; in region Y, 95% succeed. Initially each region receives 100 requests. Later the number in X doubles while Y still receives 100; each regional success rate stays unchanged. By how many percentage points does the combined success rate decrease?

**Answer format:** Exact decimal, without the % sign.

### Q10. [2 Marks] [NAT]

A square sheet occupies −4≤x≤4, −4≤y≤4. Fold the lower half over the upper half along y=0, then the left half over the right along x=0. Finally fold the part with x>y across y=x onto x≤y. Punch a small hole centred at (1,3) through all layers, away from all creases. How many distinct hole centres appear after fully unfolding?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Grammar S→aSbb | ε generates a word with 12 terminal symbols. How many a symbols does that word contain?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

A Boolean circuit computes F=(x XOR y) XOR (y XOR z). How many assignments to(x,y,z) make F differ from x XOR z?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

Choose a uniformly from{0,1,2,3,4}, and define hash h_a(x)=ax modulo5 on keys{0,1,2,3,4}. For distinct keys x,y, what is P(h_a(x)=h_a(y))?

**Answer format:** Exact decimal.

### Q14. [1 Mark] [NAT]

A DMA transfer copies4096 bytes in16-byte bursts. Every burst requires one bus-grant handshake, and no burst is partial. How many handshakes are required?

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

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

### Q16. [1 Mark] [NAT]

In C, assume unsigned int has exactly16 value bits and arithmetic on it is modulo65536. What value is printed?

```c
unsigned int x = 65535u;
unsigned int y = x + 2u;
printf("%u", y);
```

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A condition variable wait atomically releases its associated mutex and blocks, and reacquires the mutex before returning. Wakeups do not guarantee the application's predicate is true. Which statements are correct?

**Candidates**

**I.** The predicate should be rechecked after returning from wait.

**II.** A single if test before wait is sufficient for every execution.

**III.** Another thread can change the predicate before the awakened thread reacquires the mutex.

**IV.** Returning from wait means the mutex remains released under this specification.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q18. [1 Mark] [NAT]

For Boolean variables a,b,c, how many assignments satisfy (a OR b) AND ((NOT a) OR c) while making b OR c false?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

Table T has column x with rows1,1,2,NULL. What is the number of rows returned by this query under SQL bag semantics?

```sql
SELECT x FROM T
UNION ALL
SELECT x FROM T WHERE x <> 1;
```

**Answer format:** Integer.

### Q20. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A PDA's stack alphabet has only one ordinary symbol X plus a protected bottom marker. Which capabilities can it still support?

A. Counting an unbounded run of a symbols by pushing one X per a.  
B. Matching a later run of b symbols to that count by popping one X per b.  
C. Storing every arbitrary binary prefix exactly using only one X per input symbol and no other encoding or memory.  
D. Having infinitely many possible stack heights despite a finite stack alphabet.

### Q21. [1 Mark] [MCQ]

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

### Q22. [1 Mark] [NAT]

For the augmented grammar S'→S, S→CC, C→cC | d, let I0 be the LR(0) closure of S'→·S. How many items are in GOTO(I0,C), including closure items?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A single-issue, in-order pipeline can issue one instruction per cycle. Without a stall, an instruction immediately after its producer has issue-cycle separation 1. A load's dependent instruction requires separation at least 3; an ALU instruction's dependent instruction requires separation at least 1. Independent instructions have no restrictions. How many idle issue cycles are required for this fixed sequence?

```text
load r1,[a]
add  r2,r1,r3
add  r4,r5,r6
load r7,[b]
add  r8,r7,r2
```

**Answer format:** Exact integer.

### Q24. [1 Mark] [NAT]

A system has one resource type and three processes. Currently available instances=2. Allocations to P1,P2,P3 are1,2,2, and their maximum demands are3,4,6 respectively. A process may finish if its remaining need can be met, then releases its entire allocation. How many permutations of the three processes are safe completion orders?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

Let f(x)=x³+x on the real line, and let g be its inverse. Find g′(2).

**Answer format:** Exact finite decimal.

### Q26. [1 Mark] [NAT]

A recursive function on a string returns 0 for the empty string; otherwise it returns one plus the value on the suffix obtained by deleting the first character. An implementation makes no tail-call optimization. For an input of length 12, how many activations of this function are simultaneously present at the deepest point, including the base-case activation?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic Turing machine on a fixed input is forbidden to visit more than100 tape cells. Its finite state set and tape alphabet are known. Which statements are correct?

**Candidates**

**I.** Whether it halts can be decided by simulating until halting or a repeated complete configuration.

**II.** Every such machine must halt.

**III.** Only finitely many complete configurations are possible on that input.

**IV.** This establishes decidability of unrestricted Turing-machine halting.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III

### Q28. [1 Mark] [NAT]

Under multiplication modulo 12, the units form a group {1,5,7,11}. How many elements generate this entire group by repeated multiplication?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A syntax-directed definition for a list uses L→L1,d with L.count=L1.count+1, and L→d with L.count=1. How many applications of the recursive production occur in a parse of d,d,d,d,d?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A simple undirected graph has six vertices, every vertex has degree3, and the graph is bipartite. Which statements must hold?

A. Each bipartition class has three vertices.  
B. The graph is connected.  
C. The graph is isomorphic to K3,3.  
D. The graph has a triangle.

### Q31. [1 Mark] [NAT]

Among real triples satisfying x+y+z=6 and x−y=0, what is the minimum possible value of x²+y²+z²?

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

A connected undirected graph has distinct edge weights, and e is the unique heaviest edge on a cycle. Which statements are correct?

A. Every spanning tree contains e.
B. Deleting e leaves the graph connected.
C. No minimum spanning tree contains e.
D. e must be the heaviest edge of the entire graph.

### Q33. [1 Mark] [NAT]

Let A(x)=(1+x²)/(1−x), interpreted as a formal power series. What is the coefficient of x³ in A(x)²?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A resolver caches an authoritative negative DNS response for a name with an unexpired negative-cache TTL. The name is then created at the authoritative server. Assuming no forced refresh or invalidation, why may the resolver temporarily continue reporting that the name does not exist?

A. DNS names can never be created after the first query.  
B. TCP forbids any change to DNS records.  
C. The cached negative result may be reused until its TTL expires.  
D. Every negative DNS response has an infinite lifetime.

### Q35. [1 Mark] [NAT]

An IPv4 address set consists exactly of 192.0.2.32 through 192.0.2.95 inclusive. What is the smallest number of CIDR blocks whose union is exactly this set, with no extra addresses?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A TCP segment contains 1000 data bytes and a 20-byte TCP header. It is carried in an IPv4 datagram with a 20-byte header and no options. A router fragments this datagram for a link whose IP MTU is 600 bytes, using the minimum number of fragments and the largest permitted first-fragment payload. Each link frame adds a 14-byte header and a four-byte trailer. Ignore padding, preambles and gaps. How many bytes are transmitted on this link for all fragments, including these headers and trailers?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

For F(a,b,c,d)=(a XOR b)(c XOR d), what is the minimum total number of literal occurrences in a two-level sum-of-products expression without don't-care inputs? Count each occurrence in each product separately.

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Six simultaneous UDP flows use six distinct internal source IP/port pairs; three connect to remote endpoint X and three to a different endpoint Y. Each public IPv4 address provides four usable external ports. Under policy I, each internal source pair needs its own external port independent of remote endpoint. Under policy II, an external port may be reused for X and Y, and reverse lookup includes that remote endpoint. What are the minimum public-address counts under policies I and II respectively?

A. (1,1)  
B. (2,1)  
C. (2,2)  
D. (3,2)

### Q39. [2 Marks] [NAT]

In a tabular minimization procedure, the remaining cover-selection problem is the chart below. The column labels are abstract requirements, not binary minterm indices. Every column must be covered. Candidate rows have the stated costs; no other rows are available.

| Implicant | Covered columns | Literal cost |
|---|---|---:|
| P | 1,2 | 2 |
| Q | 2,3 | 2 |
| R | 3,4 | 2 |
| S | 1,4 | 3 |
| T | 1,2,3 | 4 |

Among covers using the minimum possible number of rows, what is the minimum total cost?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

A strict-priority preemptive scheduler always chooses a ready higher-priority job before a lower-priority one. A low-priority job is ready continuously. Which statements are true?

A. An unending supply of higher-priority work can starve it.
B. Increasing its priority over time through an appropriate aging policy can address this starvation risk.
C. Its ready state alone guarantees it executes within one time quantum under the stated strict-priority policy.
D. Preemption by itself guarantees bounded waiting for every priority level.

### Q41. [2 Marks] [NAT]

On a finite nonempty domain, R is symmetric and irreflexive. Every element is related to exactly two distinct elements. Also, for every x,y,z, R(x,y) AND R(y,z) implies NOT R(x,z). What is the smallest possible domain size?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A 16-bit instruction set uses variable-length opcodes but fixed-length instructions. There are 8 registers. Type A uses two three-bit register fields and has 32 opcodes. Type B uses one three-bit register field. Opcode prefixes are allocated so no Type B instruction is confused with Type A. All bit patterns not allocated to Type A may be used for Type B, and each Type B opcode must allow all eight registers. What is the maximum number of Type B opcodes?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A binary min-heap contains seven distinct keys in a one-based array. How many positions could contain the maximum key, considering all valid heaps of that size?

**Answer format:** Integer.

### Q44. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C) has dependencies A→B and B→C. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless with respect to the dependencies.  
B. The dependencies are preserved by enforcing them separately in R1 and R2.  
C. R itself is in BCNF under the given dependencies.  
D. Both decomposed relations are in BCNF under their projected dependencies.

### Q45. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A0/1 knapsack has capacity10 and items(weight,value)=(6,12),(5,9),(5,9), each available once. A heuristic scans items in decreasing value/weight order and takes an item whenever it fits. Which statement is correct?

A. The heuristic obtains12, while the optimum is18.  
B. The heuristic obtains18, while the optimum is12.  
C. Both obtain21 by splitting an item.  
D. The heuristic cannot choose any item.

### Q46. [2 Marks] [NAT]

A disk head starts at cylinder50 moving upward on cylinders0 through99. Requests70 and20 are pending. A request60 arrives exactly when the head reaches65. The head moves one cylinder per time unit and service takes zero time. Under LOOK it continues upward to the last pending request in that direction, then reverses; it does not reverse early for a new request behind it. What total distance is travelled before all three requests are served?

**Answer format:** Integer cylinders.

### Q47. [2 Marks] [NAT]

For Boolean inputs a,b,c, a circuit computes p=NAND(a,b), q=NAND(a,c), r=NAND(b,c), u=NAND(p,q), v=NAND(u,u), and F=NAND(v,r). Consider two otherwise identical faulty copies: in one, p is permanently0; in the other, p is permanently1. All other gates work normally. For how many of the eight input assignments do the two faulty copies produce different F outputs?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

Let A be the 3×3 upper-triangular matrix with rows (1,1,0),(0,1,1),(0,0,1). Find the entry in row 1, column 3 of A⁵+A⁻².

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

For grammar S→CC, C→cC | d, use canonical LR(0) item sets for the augmented grammar S′→S. How many distinct states contain a completed item C→d·? Count states, not transitions into them.

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

Short-circuit intermediate code evaluates P AND (Q OR R) from left to right, skipping operands whose values cannot affect the result. P,Q,R are independent Boolean inputs, each true with probability 1/2. What is the expected number of input predicates evaluated?

**Answer format:** Decimal rounded to two places.

### Q51. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler optimizes signed integer expressions. In this question, signed overflow traps, division by zero traps, and expressions have no side effects other than such traps. Which replacements preserve both value and whether a trap occurs for every integer x in the representable range?

**Candidates**

**I.** x−x → 0

**II.** x/x → 1

**III.** x*0 → 0

**IV.** (x+1)−1 → x

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q52. [2 Marks] [MSQ]

Consider proving that L={a^(n²) : n≥0} is not regular using pumping length p≥1 and word a^(p²). Which statements are correct?

A. Every permitted pumping substring y has length d satisfying1≤d≤p.
B. Pumping y twice gives length p²+d, strictly between consecutive squares p² and(p+1)².
C. Choosing y of length0 is permitted and defeats the proof.
D. The word's length is too small to invoke the lemma for any p≥1.

### Q53. [2 Marks] [NAT]

A slotted page has 4096 bytes, a fixed 32-byte header and twelve existing four-byte slot entries. Existing records occupy 3900 bytes in total. Compaction may collect all free bytes, but existing records and slots remain. Inserting one new record needs one new four-byte slot entry. What is the largest new record size in bytes that can fit after compaction?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

Languages A and B satisfy A≤mB: a total computable function f obeys x∈A iff f(x)∈B. Which implications necessarily hold?

A. If B is decidable, A is decidable.
B. If A is decidable, B is decidable.
C. If A is not recognizable, B is not recognizable.
D. If B is not recognizable, A is not recognizable.

### Q55. [2 Marks] [NAT]

An IPv4 datagram has a 20-byte header without options and 2000 bytes of payload. It traverses a link of MTU 1020 bytes, then a link of MTU 620 bytes. At each link, fragmentation uses the largest legal payload for each nonfinal fragment. Every resulting fragment traverses both links; no reassembly occurs between them. What is the sum of the fragment-offset field values in the four fragments leaving the second link? Offsets are measured in units of eight bytes relative to the original payload.

**Answer format:** Exact integer.

### Q56. [2 Marks] [NAT]

A singly linked structure has three nodes before its cycle entry and a cycle of five nodes. Floyd's algorithm starts slow and fast at the head, then repeatedly advances slow by one link and fast by two until they first coincide after advancing. It then resets slow to the head and advances both by one until they meet at the entry. Across both phases, how many individual next-link traversals are performed? Resetting a pointer is not counted as a traversal.

**Answer format:** Exact integer.

### Q57. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let f(0)=0 and f(x)=x²sin(1/x) for x≠0. Which statements are true?

A. f is continuous at zero.  
B. f is differentiable at zero with f′(0)=0.  
C. f′ is continuous at zero.  
D. f′ is bounded on some open interval containing zero.

### Q58. [2 Marks] [MCQ]

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

### Q59. [2 Marks] [NAT]

The values 1,2,3,4,5,6 arrive in that order. A single initially empty stack has capacity three. At each step the next unread input may be pushed if space is available, or the top may be popped to an output sequence. Each value must be pushed and popped exactly once. The output is required to begin with 3,2. How many distinct complete output sequences satisfy these conditions?

**Answer format:** Numeric value; integer.

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For L={aⁿbⁿ:n≥0}, choose w=aᵖbᵖ in a regular-language pumping-lemma proof, where p≥1. Which statements hold for every decomposition w=xyz with |xy|≤p and |y|>0?

A. y contains only a symbols.  
B. Pumping y twice preserves equal numbers of a and b.  
C. Pumping y zero times yields a word outside L.  
D. The proof may choose a decomposition that violates |xy|≤p.

### Q61. [2 Marks] [NAT]

Two four-bit two's-complement operands A,B independently range over all 16 bit patterns. How many of the 256 ordered operand pairs cause signed overflow when their sum is retained in four bits?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A process has virtual pages0–7. A page table maps pages0,1,4,5 to physical frames3,7,3,9; other pages are absent. The page size is1024 bytes. How many distinct physical byte addresses are represented by all valid virtual addresses in those four mapped pages?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A control word contains twelve independent Boolean control signals and three separately encoded groups of mutually exclusive signals of sizes 4,5,3. Each group must also represent “none active.” Signals from different groups and the twelve independent signals may coexist freely. What is the minimum control-word width under this field-by-field encoding?

**Answer format:** Integer bits.

### Q64. [2 Marks] [NAT]

Five jobs in fixed order have (cost,value) pairs (4,9),(2,7),(3,8),(3,10),(2,6). Select exactly two jobs, with no two adjacent in the order, and total cost at most seven. What is the maximum total value?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

How many binary strings of length eight contain no adjacent zeros and have an even number of ones?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 068

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 2 |
| 2 | NAT | 1 | 4.8 |
| 3 | MSQ | 1 | A, B, D |
| 4 | NAT | 1 | 35.71 (exact) |
| 5 | MSQ | 1 | A, B, D |
| 6 | NAT | 2 | 16 |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 60 |
| 9 | NAT | 2 | 2.5 |
| 10 | NAT | 2 | 8 |
| 11 | NAT | 1 | 4 |
| 12 | NAT | 1 | 0 |
| 13 | NAT | 1 | 0.2 |
| 14 | NAT | 1 | 256 |
| 15 | MCQ | 1 | A |
| 16 | NAT | 1 | 1 |
| 17 | MCQ | 1 | A |
| 18 | NAT | 1 | 0 |
| 19 | NAT | 1 | 5 |
| 20 | MCQ | 1 | C |
| 21 | MCQ | 1 | D |
| 22 | NAT | 1 | 3 |
| 23 | NAT | 1 | 4 |
| 24 | NAT | 1 | 3 |
| 25 | NAT | 1 | 0.25 |
| 26 | NAT | 1 | 13 |
| 27 | MCQ | 1 | D |
| 28 | NAT | 1 | 0 |
| 29 | NAT | 1 | 4 |
| 30 | MCQ | 1 | D |
| 31 | NAT | 1 | 12 |
| 32 | MSQ | 1 | B, C |
| 33 | NAT | 1 | 8 |
| 34 | MSQ | 1 | A, B, D |
| 35 | NAT | 1 | 2 |
| 36 | NAT | 2 | 1096 (exact) |
| 37 | NAT | 2 | 16 |
| 38 | MSQ | 2 | A, C, D |
| 39 | NAT | 2 | 4 |
| 40 | MSQ | 2 | A, B |
| 41 | NAT | 2 | 4 (exact) |
| 42 | NAT | 2 | 7936 |
| 43 | NAT | 2 | 4 |
| 44 | MCQ | 2 | C |
| 45 | MSQ | 2 | B, C, D |
| 46 | NAT | 2 | 70 |
| 47 | NAT | 2 | 5 |
| 48 | NAT | 2 | 13 |
| 49 | NAT | 2 | 1 |
| 50 | NAT | 2 | 1.75 (two decimals) |
| 51 | MCQ | 2 | D |
| 52 | MSQ | 2 | A, B |
| 53 | NAT | 2 | 112 |
| 54 | MSQ | 2 | A, C |
| 55 | NAT | 2 | 400 |
| 56 | NAT | 2 | 21 |
| 57 | MCQ | 2 | C |
| 58 | MCQ | 2 | A |
| 59 | NAT | 2 | 13 (exact) |
| 60 | MSQ | 2 | B, D |
| 61 | NAT | 2 | 64 |
| 62 | NAT | 2 | 3072 |
| 63 | NAT | 2 | 20 (exact) |
| 64 | NAT | 2 | 19 |
| 65 | NAT | 2 | 27 |
