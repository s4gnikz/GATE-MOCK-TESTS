# GATE CS 2027 — Full-Length Mock Test 028

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

The examination lasts180 minutes. Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes15 marks, Engineering Mathematics13 and core Computer Science72.

An MCQ has exactly one correct option. An MSQ has multiple correct options and earns marks only when all and only those options are selected. An incorrect one-mark MCQ incurs a penalty of1/3 mark; an incorrect two-mark MCQ incurs2/3 mark. MSQ and NAT questions have no negative marking. Unattempted questions receive zero. No partial credit applies. For NAT questions, use the requested precision; integers and exact decimals require exact values. Mathematical arithmetic is exact unless a machine representation is specified. The answer key is placed after Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

A sequence begins a1=1,a2=2 and satisfies a(n+2)=a(n+1)+a(n). How many of its first twelve terms are odd?

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

The midpoints of the four sides of a12-by-8 rectangle are joined consecutively to form a quadrilateral. What is its area?

**Answer format:** Integer square units.

### Q3. [1 Mark] [MCQ]

Choose the grammatically appropriate completion: “Neither the editor nor the authors ___ willing to omit the evidence.”

A. is
B. are
C. has
D. was

### Q4. [1 Mark] [NAT]

A uniform mixture of two grains has average cost50 currency units per kilogram. Five kilograms are removed and replaced by five kilograms of grain costing40 per kilogram. The resulting average is45 per kilogram. What was the mixture's original mass?

**Answer format:** Exact number of kilograms.

### Q5. [1 Mark] [NAT]

An integer x is in {1,2,3,4}. Exactly two of these statements are true: x≤2; x is even; x=3. What is x?

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

A point is reflected across the vertical line x=1, and the reflected point is then rotated90 degrees counterclockwise about the origin. The final point is(−3,−2). What was the original point's distance from the origin?

**Answer format:** Exact number.

### Q7. [2 Marks] [MSQ]

A school introduces an optional tutoring programme. Students who chose it scored higher on average than those who did not. No information is available about their earlier scores or reasons for enrolling. Which statements follow from this description?

A. Participation and the observed scores are associated in this sample.
B. The comparison alone does not isolate the causal effect of tutoring.
C. Tutoring necessarily caused every participant's score to increase.
D. The participants and nonparticipants necessarily had identical prior achievement.

### Q8. [2 Marks] [NAT]

Six distinct people form three specified pairs. They sit around a circular table, and no person's specified partner may occupy an adjacent seat. Rotations count as the same seating; reflections count as different. How many seatings are possible?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

An organizer may buy any nonnegative integer number of two advertising packages. Each A package costs40 and brings exactly10 registrations. Each B package costs60 and brings exactly12 registrations. With a budget of300, what is the maximum number of registrations obtainable?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

A square sheet occupies0≤x≤4,0≤y≤4. Fold its left half onto its right half along x=2. Cut out, through both layers, the triangle with vertices(2,0),(3,0),(2,1). After unfolding, what is the perimeter of the remaining sheet? The cut boundaries are included in the perimeter.

**Answer format:** Decimal rounded to four places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Over alphabet{a,b}, how many strings of length3 belong to the language described by the regular expression(a|ba)*?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

A singly linked list has a noncyclic prefix of three nodes followed by a cycle of four nodes. A slow pointer and a fast pointer both start at the head. In each iteration slow advances one link and fast advances two. Equality is tested only after these advances. After how many iterations do they first point to the same node?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A router has routes192.0.2.0/24→A,192.0.2.128/25→B and192.0.2.160/27→C, using longest-prefix match. How many addresses in192.0.2.0/24 are forwarded to B?

**Answer format:** Integer address count; include all addresses in the ranges.

### Q14. [1 Mark] [MCQ]

A language has lexical nesting. Procedure Outer defines local x and nested procedure Inner, whose body references x. Inner is called by an unrelated procedure Caller while Outer remains active. Which link is needed to find the lexically enclosing activation containing x?

A. A dynamic link to Caller alone
B. A static link to Outer's activation
C. A link to whichever activation was created most recently
D. A link to the global symbol table alone

### Q15. [1 Mark] [MSQ]

Two virtual pages of one process intentionally map to the same physical frame. Both mappings are writable and there is no copy-on-write mechanism. Which statements are correct?

A. A write through one mapping can be read through the other at the corresponding offset.
B. The virtual page numbers must be equal.
C. The mappings can have different virtual addresses while sharing storage.
D. Each write necessarily allocates a fresh physical frame.

### Q16. [1 Mark] [NAT]

Grammar S→SS | a generates strings of a's. Count ordered parse trees, not derivation orders. How many parse trees generate aaaa?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A file's logical blocks0,1,2 map to disk blocks40,41,90. A system reads logical blocks0–2 in order. Adjacent disk block numbers can be transferred as one contiguous disk extent. What is the minimum number of extents that contain precisely these requested blocks?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

A fair coin is tossed twice. X is the number of heads, and Y is1 if the tosses differ and0 otherwise. What is Cov(X,Y)?

**Answer format:** Exact number.

### Q19. [1 Mark] [MSQ]

A compiler lowers the condition (p!=0) AND ((*p)>0) using short-circuit evaluation. The pointer p may be null. Which statements are correct?

A. The dereference may be skipped when p is null.
B. Evaluating both operands before combining their Boolean values always preserves behaviour.
C. A control-flow edge can bypass the dereference after a false first test.
D. The second comparison must be evaluated before the first comparison.

### Q20. [1 Mark] [NAT]

A coin system has denominations1,3,4 and unlimited coins. For amount6, how many more coins does repeatedly taking the largest affordable denomination use than an optimal solution?

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

T1 writes x. Before T1 commits, T2 reads that written value and then commits. T1 later aborts. Which statements are correct?

A. T2 performed a dirty read.
B. This schedule is recoverable.
C. T2 committed based on a value later rolled back.
D. The schedule is strict.

### Q22. [1 Mark] [NAT]

A horizontal microinstruction has five independent one-bit control signals and an eight-bit next-address field. A redesigned encoding replaces the five control bits by a three-bit code selecting one of six permitted control combinations, retaining the next-address field unchanged. How many bits per microinstruction are saved?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A signed fixed-point format stores a six-bit two's-complement integer divided by8. What real value results if the stored code011111 is incremented by1 with six-bit wraparound?

**Answer format:** Exact number.

### Q24. [1 Mark] [NAT]

On set{1,2,3,4}, define xRy exactly when floor(x/2)=floor(y/2). How many ordered pairs belong to R?

**Answer format:** Integer.

### Q25. [1 Mark] [MSQ]

A finite binary floating-point format rounds to nearest and has a largest finite positive value M. Which statements are correct, assuming real input values may exceed the representable range?

A. Every real number in[−M,M] is exactly representable.
B. Distinct real values can round to the same finite floating-point number.
C. Having sufficient exponent range alone does not guarantee exact representation of every fraction.
D. Every arithmetic result with magnitude below M must be represented exactly.

### Q26. [1 Mark] [NAT]

A Boolean circuit computes F=(x XOR y) XOR (y XOR z). How many assignments to(x,y,z) make F differ from x XOR z?

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

A nondeterministic pushdown automaton accepts if at least one computation branch consumes the whole input and reaches a designated final state. Which statements are correct?

A. A rejecting branch prevents acceptance even if another branch accepts.
B. An infinite branch need not prevent acceptance by a different finite branch.
C. Reaching a final state before consuming all input is sufficient under the stated rule.
D. Acceptance uses an existential condition over branches.

### Q28. [1 Mark] [NAT]

A real3×3 matrix A has rank1 and trace5. What is trace(A²)?

**Answer format:** Exact number.

### Q29. [1 Mark] [NAT]

A schedule has operations r1(x),r2(x),w1(x),w2(x), followed by commits. How many directed edges are in its precedence graph, counting each ordered pair of distinct transactions at most once?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

A function f is continuous on[0,2] and twice differentiable on(0,2), with f(0)=0,f(1)=2,f(2)=0. Which statement must hold?

A. f''(x)<0 at every x in(0,2).
B. f''(x)<0 at some x in(0,2).
C. f''(1)=−4.
D. f'(1)=0.
### Q31. [1 Mark] [MSQ]

A0/1 knapsack of capacity4 has just one item, of weight2 and value3. An implementation initializes dp[0..4] to0 and processes this item as follows:

```text
for w = 2 to 4, in increasing order:
    dp[w] = max(dp[w], dp[w-2] + 3)
```

Which statements are correct?

A. The loop returns the correct0/1 optimum at dp[4].
B. It sets dp[4] to6 by effectively reusing the item.
C. Iterating w from4 down to2 instead avoids this reuse.
D. Every dp[w-2] read in this loop is necessarily from before processing the item.
### Q32. [1 Mark] [NAT]

Events A and B satisfy P(A)=0.4, P(B)=0.5 and P(A∪B)=0.7. What is P(A|B)?

**Answer format:** Exact decimal.

### Q33. [1 Mark] [NAT]

A memory system must contain1024 words of16 bits each. Available chips each contain256 words of8 bits. How many chips are required, assuming ordinary depth and width expansion without redundancy?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

Distinct values1,2,3,4,5 arrive in that order at a single stack. Each value is pushed exactly once and popped exactly once; pushes and pops may be interleaved. How many distinct full output permutations can have4 as their first popped value?

**Answer format:** Integer.
### Q35. [1 Mark] [MSQ]

An address-and-port translator lets two internal clients connect simultaneously to the same external server and server port, using one public IPv4 address. Assume its mapping distinguishes connections using the public source port. Which statements are correct?

A. The two active mappings need different public source ports.
B. Both internal clients must have identical private source addresses.
C. Return traffic can be demultiplexed using the stored mappings.
D. The translator must change the external server's application data to identify the clients.

### Q36. [2 Marks] [NAT]

A sender estimates round-trip time using S←(3/4)S+(1/4)R and then D←(1/2)D+(1/2)|R−S_old|, where S_old is the estimate before that sample's update. Its timeout is S+4D. Initially S=100ms and D=10ms. Two successive unambiguous samples are140ms and100ms. What timeout results after both updates?

**Answer format:** Exact milliseconds.

### Q37. [2 Marks] [MSQ]

L is a nonregular language over alphabetΣ. Which statements must hold?

A. Its complement Σ*\L is nonregular.
B. L union (Σ*\L) is regular.
C. Intersecting L with any infinite regular language always gives a nonregular language.
D. Removing finitely many strings from L leaves a nonregular language.

### Q38. [2 Marks] [NAT]

A ternary relationship T(Student,Course,Tutor) has tuples(0,0,0),(0,1,1),(1,0,1),(1,1,0). A designer replaces it by the three binary relationship projections onto(Student,Course),(Student,Tutor),(Course,Tutor). How many additional ternary tuples appear when those projections are naturally joined, beyond the four original tuples?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

An application must receive exactly five bytes from a TCP stream into buf[0..4]. There are no errors or end-of-stream events. Consider this pseudocode, where recv returns a positive number of bytes actually written:

```text
n = 0
while n < 5:
    k = recv(socket, buf, 5-n)
    n = n + k
```

The sender's five bytes are A,B,C,D,E in that order. The two recv calls return2 and3 respectively. Which statements are correct?

A. The second call overwrites the buffer's first three positions.
B. The loop necessarily leaves A,B,C,D,E in consecutive buffer positions.
C. Passing buf+n as the destination before each call repairs the placement error.
D. TCP's ordered delivery guarantees that the application cannot overwrite previously received bytes.

### Q40. [2 Marks] [MSQ]

A poset has elements a,b,c,d with a<c,b<c,c<d, and only the comparisons forced by these and reflexivity. Let J be the family of its downward-closed subsets, ordered by inclusion. Which statements are correct?

A. J has six elements, including the empty subset.
B. Join in J is set union.
C. Meet in J is set intersection.
D. J fails distributivity because a and b are incomparable.

### Q41. [2 Marks] [NAT]

Let A be the4×4 tridiagonal matrix with diagonal entries2, immediate subdiagonal and superdiagonal entries−1, and all other entries0. In its LU factorization without pivoting, with L unit lower triangular, what is U's last diagonal entry?

**Answer format:** Exact decimal.

### Q42. [2 Marks] [MSQ]

Consider proving that L={a^(n²) : n≥0} is not regular using pumping length p≥1 and word a^(p²). Which statements are correct?

A. Every permitted pumping substring y has length d satisfying1≤d≤p.
B. Pumping y twice gives length p²+d, strictly between consecutive squares p² and(p+1)².
C. Choosing y of length0 is permitted and defeats the proof.
D. The word's length is too small to invoke the lemma for any p≥1.

### Q43. [2 Marks] [NAT]

The Boolean function F(a,b,c)=ab+(NOT a)c is implemented as a two-level AND–OR circuit. Gate delays are arbitrary positive values. The implementation must be free of static-1 hazards for every single-input transition; redundant product terms may be added, but only uncomplemented or complemented input literals may feed the AND gates. What is the minimum total number of literal occurrences in such a hazard-free sum-of-products implementation?

**Answer format:** Integer.
### Q44. [2 Marks] [MSQ]

Assume mathematical integer arithmetic and a Boolean flag whose value is not known at compile time. Compare these blocks:

```text
Original:
    x = 0
    if flag: x = 1
    y = x + 1

Proposed:
    x = 0
    y = 1
    if flag: x = 1
```

Both x and y are observable at exit. Which statements are correct?

A. The transformation preserves both outputs when flag is false.
B. The transformation preserves both outputs when flag is true.
C. Treating x=0 as an invariant across the conditional is unsound here.
D. Making y unobservable at exit would make these particular blocks equivalent on their remaining observable output x.

### Q45. [2 Marks] [NAT]

A processor services eight independent cache misses. Each miss takes100 cycles from issue to completion. It can issue at most one miss per cycle and have at most four outstanding misses. A slot freed by a completion can be reused in that same cycle. All misses are ready initially and are issued as early as permitted, starting in cycle0. In what cycle does the last miss complete?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A rooted tree has the parent array for vertices1 through7 given by[0,1,1,2,2,4,3], where0 marks the root. An operation cuts the subtree rooted at2 and reattaches its root as a child of7. How much does the sum of depths of all seven vertices increase, with the root's depth defined as0?

**Answer format:** Integer.

### Q47. [2 Marks] [MSQ]

A prime-implicant chart has required columns u,v,w and rows P={u,v}, Q={v,w}, R={u,w}. Every row has equal cost. Which statements are correct?

A. Every row is essential because it covers two columns.
B. No single row covers all required columns.
C. There are exactly three distinct minimum-cardinality covers.
D. Deleting any one row leaves at least one valid cover.

### Q48. [2 Marks] [NAT]

A continuous function f on[0,1] satisfies f(x)+f(1−x)=x(1−x) for all x in[0,1]. What is the integral of f from0 to1?

**Answer format:** Decimal rounded to four places.

### Q49. [2 Marks] [MSQ]

Under set semantics, R(A,B) and S(A,B) have the same schema. Which statements hold for every instance?

A. πA(R−S)=πA(R)−πA(S).
B. πA(R−S) contains πA(R)−πA(S).
C. πA(R∩S) is contained in πA(R)∩πA(S).
D. πA(R∩S)=πA(R)∩πA(S).

### Q50. [2 Marks] [NAT]

A two-way set-associative cache has two sets and one block per way. Block b maps to set b modulo2, and each set uses LRU replacement. Starting empty, access blocks0,2,1,0,4,2,1. How many misses occur?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

Six observations are3,3,3,7,7,7. Replace exactly one observation by any real number, keeping the other five fixed. The median of six observations is the average of the third and fourth values in sorted order. What is the largest possible increase in the median?

**Answer format:** Exact number.

### Q52. [2 Marks] [MSQ]

A Turing machine M is promised to halt on every input. A proposed procedure enumerates input strings and simulates M on each until it finds an accepted input. Which statements are correct?

A. If L(M) is nonempty, this sequential procedure eventually finds an accepted input.
B. If L(M) is empty, the procedure eventually proves emptiness just by reaching a sufficiently long rejected input.
C. Totality of M makes each individual simulation finish.
D. The promise supplies a finite maximum length beyond which no new accepted input can occur.

### Q53. [2 Marks] [NAT]

A four-to-one multiplexer selects data input D(2s1+s0), where s1,s0 are the select bits. To implement F(a,b,c)=1 exactly when precisely one of a,b,c is1, choose s1=a,s0=b. Each data input may be0,1,c,or NOT c. How many of the four required data inputs equal NOT c?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

Insert keys20,10,30,25,40,22,27 into an initially empty ordinary BST. Perform a single left rotation at root20: its right child30 becomes the root,20 becomes30's left child, and30's former left subtree becomes20's right subtree. How many keys have the same depth before and after the rotation, counting the root's depth as0?

**Answer format:** Integer.
### Q55. [2 Marks] [NAT]

A divide-and-conquer procedure on an array of length8 splits each nonsingleton interval into equal halves and recurses on both. At each internal node it merges the halves into a new buffer, writing every element exactly once; singleton leaves perform no writes. How many element writes occur across all merge buffers?

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

A binary min-heap contains distinct keys. Its array uses one-based indexing. Which statements must hold for every heap of at least seven elements?

A. The second-smallest key is at index2 or3.
B. The third-smallest key is necessarily at index4 or5.
C. The parent of a node always has a smaller key than that node.
D. The array is globally sorted in increasing order.

### Q57. [2 Marks] [MSQ]

A directed graph has edges a→b,b→c,c→a,c→d,d→e,e→d,e→f. Which statements are correct?

A. c and d are in the same strongly connected component.
B. Adding the edge f→b makes the entire graph strongly connected.
C. Reversing every edge preserves the partition into strongly connected components.
D. In the original graph, f can reach a.
### Q58. [2 Marks] [MSQ]

A process opens a file once, duplicates that descriptor, and then forks. Assume ordinary shared-open-file-description semantics, no later opens, and sequential rather than concurrent reads. Which statements are correct?

A. Parent and child descriptor references can share one file offset.
B. Duplicating a descriptor necessarily creates an independent offset.
C. A read through one of the shared references can change the offset seen by the others.
D. Closing one reference necessarily closes every remaining reference immediately.

### Q59. [2 Marks] [NAT]

A process starts with integer x=1. It forks once, creating independent address spaces. Both parent and child then execute x=x+1. Only the parent forks a second time. Every existing process then prints its own x once and exits. Assuming all forks succeed and output buffering does not duplicate earlier output, what is the sum of the printed integers?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

A control-flow graph contains a loop entered with x=0. Its body is x=x+1, and it may execute any nonnegative number of times. A sound scalar constant-propagation analysis represents each variable as either a particular integer constant or nonconstant at a program point. Which statements are correct?

A. At the loop header, x may soundly be reported as the constant0 for all executions.
B. Merging the entry path and back edge prevents x from remaining a single known constant at the header.
C. At loop exit, x is always1.
D. A more expressive analysis could retain a range fact such as x≥0.

### Q61. [2 Marks] [NAT]

Relation R(x,y) contains(1,1),(1,2),(2,2),(3,1). Evaluate the domain-restricted tuple-calculus condition R(x,y) AND NOT EXISTS z(R(y,z) AND z≠x). How many tuples of R satisfy it?

**Answer format:** Integer.

### Q62. [2 Marks] [MSQ]

Processes P and Q communicate through a finite-capacity pipe. P writes until the pipe is full; Q still has an open read end but never reads. Assume blocking writes and no signals or failures. Which statements are correct?

A. P may block on a further write.
B. Keeping a read end open guarantees that Q consumes bytes.
C. Closing all read ends changes the situation from merely having a full pipe.
D. A finite buffer guarantees completion for an arbitrarily large write workload even if Q never reads.

### Q63. [2 Marks] [NAT]

A device generates one completion every20 microseconds. An interrupt handler costs3 microseconds of CPU time per interrupt. Coalescing groups four consecutive completions into one interrupt, without changing handler cost. In a steady-state interval of400 microseconds containing exactly20 completions, how many microseconds of CPU time are saved compared with one interrupt per completion?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

An undirected connected graph may have equal edge weights. For one edge e, there is a cut for which e is the unique lightest crossing edge. Which statements must hold?

A. Every minimum spanning tree contains e.
B. e is the unique lightest edge in the entire graph.
C. If a spanning tree omits e, adding e creates a cycle containing another edge crossing that cut.
D. The graph has a unique minimum spanning tree.

### Q65. [2 Marks] [NAT]

For this straight-line block, return is the only observable use after the last assignment. Count named scalar variables only, not constants or temporary arithmetic results.

```text
a = input()
b = input()
c = a + b
a = c + 1
d = b + a
return d
```

What is the maximum number of simultaneously live named variables immediately after any assignment in this block?

**Answer format:** Integer.



---

## ANSWER KEY — MOCK TEST 028

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 8 |
| 2 | NAT | 1 | 48 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 10 |
| 5 | NAT | 1 | 2 |
| 6 | NAT | 2 | 5 |
| 7 | MSQ | 2 | A, B |
| 8 | NAT | 2 | 32 |
| 9 | NAT | 2 | 72 |
| 10 | NAT | 2 | 16.8284 (accepted range 16.82835–16.82845) |
| 11 | NAT | 1 | 3 |
| 12 | NAT | 1 | 4 |
| 13 | NAT | 1 | 96 |
| 14 | MCQ | 1 | B |
| 15 | MSQ | 1 | A, C |
| 16 | NAT | 1 | 5 |
| 17 | NAT | 1 | 2 |
| 18 | NAT | 1 | 0 |
| 19 | MSQ | 1 | A, C |
| 20 | NAT | 1 | 1 |
| 21 | MSQ | 1 | A, C |
| 22 | NAT | 1 | 2 |
| 23 | NAT | 1 | -4 |
| 24 | NAT | 1 | 6 |
| 25 | MSQ | 1 | B, C |
| 26 | NAT | 1 | 0 |
| 27 | MSQ | 1 | B, D |
| 28 | NAT | 1 | 25 |
| 29 | NAT | 1 | 2 |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | B, C |
| 32 | NAT | 1 | 0.4 |
| 33 | NAT | 1 | 8 |
| 34 | NAT | 1 | 4 |
| 35 | MSQ | 1 | A, C |
| 36 | NAT | 2 | 177.5 |
| 37 | MSQ | 2 | A, B, D |
| 38 | NAT | 2 | 4 |
| 39 | MSQ | 2 | A, C |
| 40 | MSQ | 2 | A, B, C |
| 41 | NAT | 2 | 1.25 |
| 42 | MSQ | 2 | A, B |
| 43 | NAT | 2 | 6 |
| 44 | MSQ | 2 | A, C, D |
| 45 | NAT | 2 | 203 |
| 46 | NAT | 2 | 8 |
| 47 | MSQ | 2 | B, C, D |
| 48 | NAT | 2 | 0.0833 (accepted range 0.08325–0.08335) |
| 49 | MSQ | 2 | B, C |
| 50 | NAT | 2 | 5 |
| 51 | NAT | 2 | 2 |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 2 |
| 54 | NAT | 2 | 3 |
| 55 | NAT | 2 | 24 |
| 56 | MSQ | 2 | A, C |
| 57 | MSQ | 2 | B, C |
| 58 | MSQ | 2 | A, C |
| 59 | NAT | 2 | 6 |
| 60 | MSQ | 2 | B, D |
| 61 | NAT | 2 | 1 |
| 62 | MSQ | 2 | A, C |
| 63 | NAT | 2 | 45 |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 2 |
