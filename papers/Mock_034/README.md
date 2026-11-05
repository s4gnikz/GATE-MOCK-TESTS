# GATE CS 2027 — Full-Length Mock Test 034

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes15 marks, Engineering Mathematics13, and core Computer Science72. The duration is180 minutes.

MCQ has one correct choice; MSQ requires all and only correct choices. An incorrect MCQ loses one third of its marks. MSQ and NAT have no negative marking, and MSQ has no partial credit. Unattempted questions receive zero. Follow each NAT precision instruction. The answer key follows Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“The witness gave an equivocal reply: it could reasonably be understood as either agreement or refusal.” In this sentence, “equivocal” most nearly means:

A. deliberately brief
B. supported by independent evidence
C. open to conflicting interpretations
D. expressing definite agreement

### Q2. [1 Mark] [NAT]

How many integers x with1≤x≤1000 satisfy floor(log2 x)=floor(log3 x)? Here floor denotes the greatest integer not exceeding its argument.

**Answer format:** Exact integer.

### Q3. [1 Mark] [MSQ]

A rule is claimed for every positive integer n: if n leaves remainder1 upon division by3, then n² leaves remainder1 upon division by3. Which observations are logically valid?

A. Writing n=3k+1 and expanding its square proves the claim for all eligible n.
B. Checking n=1,4,7 proves the universal claim without any further argument.
C. A number with remainder2 can also have a square with remainder1.
D. The converse follows solely because the forward implication holds.

### Q4. [1 Mark] [NAT]

A solid cube is made from27 identical unit cubes arranged3×3×3. Remove the central unit cube from each of the six outer faces, and also remove the central unit cube of the solid. All seven removed cubes are distinct. How many exposed unit-square faces belong to the remaining solid, counting newly exposed internal surfaces?

**Answer format:** Exact integer.

### Q5. [1 Mark] [NAT]

A sequence satisfies a1=2 and a(n+1)=an+2n+1 for every n≥1. What is the smallest index n for which an exceeds100?

**Answer format:** Exact integer.

### Q6. [2 Marks] [NAT]

A rectangular garden is12 m by8 m. A path of constant width w runs along the inside of all four edges, leaving a smaller central rectangle. The path and the central rectangle have equal areas. What is w?

**Answer format:** Decimal rounded to three places, in metres.

### Q7. [2 Marks] [MCQ]

Choose the sentence that most clearly expresses both stated facts without a misplaced modifier: the researcher analyzed the samples, and the samples—not the researcher—had been stored overnight.

A. Stored overnight, the researcher analyzed the samples.
B. The researcher analyzed the samples that had been stored overnight.
C. Analyzing the researcher, the samples had been stored overnight.
D. The researcher, which had been stored overnight, analyzed the samples.

### Q8. [2 Marks] [NAT]

A container initially holds10 litres of a mixture that is30% salt solution by volume, with the remaining volume water. Remove2 litres of the well-mixed contents and replace them with2 litres of pure water. Then remove5 litres of the newly mixed contents and replace them with5 litres of a60% salt solution. Assuming volumes add, what percentage of the final mixture is salt solution?

**Answer format:** Exact decimal percentage, without the % sign.

### Q9. [2 Marks] [NAT]

Exactly one of four labeled boxes A,B,C,D contains a token. Their labels state:

- A: “The token is in B or C.”
- B: “The token is in A.”
- C: “The token is not in C.”
- D: “The token is in D.”

Exactly two labels are true. How many possible token locations are consistent with this information?

**Answer format:** Exact integer.

### Q10. [2 Marks] [NAT]

A point is transformed by T(x,y)=(y,−x), a clockwise quarter-turn about the origin, and by U(x,y)=(x+2,y). Starting from(1,1), compare two results: first T then U, and first U then T. What is the squared Euclidean distance between these two final points?

**Answer format:** Exact integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

On a UNIX-like file system, path p refers to regular file F. Process R has already opened F for reading. Process W creates a different regular file G and atomically renames G over p. No process modifies F or G afterward. Assume rename succeeds and no symbolic links are involved. Which statements hold?

A. R's existing descriptor still refers to F.
B. A later successful open of p refers to G.
C. The rename necessarily changes the inode referred to by R's existing descriptor.
D. F's storage must be reclaimed before the rename can return, even while R retains its descriptor.

### Q12. [1 Mark] [MSQ]

For real t, let A be the matrix below. An LU factorization here means A=LU without row exchanges, with L lower triangular with diagonal entries1 and U upper triangular. Which statements hold?

```text
A = [ t  1
      1  0 ]
```

A. A is invertible for every real t.
B. Such an LU factorization exists for t=0.
C. Such an LU factorization exists for every nonzero t.
D. For nonzero t, U22=−1/t.

### Q13. [1 Mark] [NAT]

An Ethernet learning switch has hosts A,B,C on distinct ports1,2,3. Its forwarding table is initially empty. It learns a source address before deciding how to forward that frame. In order, it receives unicast frames A→B, B→A, and C→A. There is no aging or other traffic. How many frame copies in total are transmitted by the switch over its output ports?

**Answer format:** Exact integer.

### Q14. [1 Mark] [NAT]

A binary search tree contains distinct keys1,3,4,5,7,8 and has postorder traversal1,4,3,8,7,5. Starting from an empty BST and using ordinary leaf insertion without rotations, how many different insertion orders generate this exact tree?

**Answer format:** Exact integer.

### Q15. [1 Mark] [NAT]

Evaluate the definite integral of x|x−1| over0≤x≤2.

**Answer format:** Exact integer.

### Q16. [1 Mark] [MCQ]

Two datasets each contain three real observations. Their medians are2 and9, respectively. Combine all six observations and define the new median as the average of the third and fourth ordered observations. Which assertion is necessarily true?

A. The combined median equals5.5.
B. The combined median lies in[2,9].
C. The combined mean lies in[2,9].
D. The combined median equals one of the original six observations.

### Q17. [1 Mark] [NAT]

A min-heap with distinct keys1 through7 is stored in an array indexed1 through7. The key7 is known to be at index2. How many such heaps exist?

**Answer format:** Exact integer.

### Q18. [1 Mark] [NAT]

The grammar has start symbol S and productions S→aSbb | T and T→bTa | epsilon. How many distinct terminal strings of length6 does it generate?

**Answer format:** Exact integer.

### Q19. [1 Mark] [MCQ]

A three-variable Karnaugh map represents F=1 exactly when an even number of inputs are1. There are no don't-care entries. Which statement about a two-level SOP using only uncomplemented or complemented input literals is correct?

A. One four-cell group covers all1-cells.
B. Two two-cell groups cover all1-cells.
C. Four singleton groups are required.
D. No SOP can represent this function.

### Q20. [1 Mark] [MSQ]

A recursive depth-first search on a directed graph colors undiscovered vertices white, vertices on its active recursion stack gray, and finished vertices black. A currently explored edge is u→v. Which statements hold?

A. If v is gray, the graph contains a directed cycle.
B. If v is black, u→v necessarily belongs to a directed cycle.
C. If no edge to a gray vertex is encountered during a full DFS forest, the graph is acyclic.
D. If v is white, v must be an ancestor of u in the current DFS tree.

### Q21. [1 Mark] [NAT]

A byte-addressed machine fetches a four-byte branch instruction at address1000. Its eight-bit displacement field contains11111100. The processor sign-extends this field, multiplies it by4, and adds the result to the address immediately after the instruction. What is the target byte address?

**Answer format:** Exact integer.

### Q22. [1 Mark] [MSQ]

Transaction T1 locks every existing row satisfying salary>100 and counts those rows twice. Between the counts, T2 inserts and commits a new row with salary150. The system uses only row locks on existing rows; no predicate or range locks are acquired. Which statements hold?

A. T1's locks need not prevent T2's insertion.
B. The second count can exceed the first despite locking all originally qualifying rows.
C. Locking existing rows necessarily locks every future row satisfying the same predicate.
D. A suitable predicate lock can prevent the insertion until T1 releases it.

### Q23. [1 Mark] [NAT]

All functions from the set {a,b,c} to itself form a monoid under composition. How many functions f in this monoid satisfy f composed with f=f and have an image containing exactly two elements?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MCQ]

A compiler considers common-subexpression elimination in this fragment. Arithmetic is exact, and a,b,c,d are distinct variables.

```text
if p { t=a+b; } else { t=c+d; }
u=a+b;
```

Which proposed justification for replacing u=a+b by u=t is valid?

A. The expression a+b appears earlier in the text, so the replacement is always valid.
B. The replacement is valid if c+d=a+b is proved on every execution taking the else branch.
C. The replacement is valid merely because neither a nor b changes in the fragment.
D. The replacement is valid merely because both branches assign t.

### Q25. [1 Mark] [NAT]

After tabular minimization, selecting prime implicants P,Q,R must satisfy the cover expression (P+Q)(Q+R)(P+R), where + means choosing at least one listed implicant and multiplication means satisfying all requirements. Each selected implicant has equal cost. How many distinct minimum-cardinality covers exist?

**Answer format:** Exact integer.

### Q26. [1 Mark] [MSQ]

In a connected undirected weighted graph, edge e joins u to v and has weight8. There is a u-to-v path avoiding e on which every edge has weight at most7. Which statements necessarily hold?

A. No minimum spanning tree contains e.
B. Removing e disconnects the graph.
C. If a spanning tree contains e, some cheaper spanning tree can be obtained by exchanging one edge.
D. Every edge of the alternative path must belong to every minimum spanning tree.

### Q27. [1 Mark] [NAT]

An ER relationship between three distinct entities in set A and four distinct entities in set B is many-to-many, with total participation on both sides. Relationship instances are sets of distinct pairs from A×B. How many different relationship instances have exactly four pairs?

**Answer format:** Exact integer.

### Q28. [1 Mark] [NAT]

A process writes a2048-byte buffer using a system call that may complete partially. The first call returns768 and the second, correctly adjusted call returns512. Both returns indicate successfully written bytes. How many buffer bytes remain to be written, assuming no other output occurs?

**Answer format:** Exact integer.

### Q29. [1 Mark] [MCQ]

A link-state router retains, for each origin, only the advertisement with the highest sequence number. Sequence numbers do not wrap in this scenario. For origin X, it receives advertisements (sequence,link cost)=(41,5),(43,9),(42,2),(43,9). Which link cost from X remains in its database?

A. 2
B. 5
C. 9
D. 25

### Q30. [1 Mark] [MSQ]

A nondeterministic PDA begins with one bottom symbol Z on its stack. It has exactly these moves: on input a with top Z, replace Z by XZ; on input b with top X, pop X; on empty input with top Z, pop Z. There are no moves with an empty stack. Acceptance requires the entire input to be consumed and the stack to be empty. Which strings are accepted?

A. epsilon
B. ab
C. aabb
D. abab

### Q31. [1 Mark] [NAT]

A four-bit ripple-carry adder adds binary operands1011 and0110 with carry-in0. Let c1,c2,c3,c4 be the carry out of bit positions0,1,2,3 respectively, where bit0 is least significant. What unsigned integer is represented by c4c3c2c1?

**Answer format:** Exact integer.

### Q32. [1 Mark] [MCQ]

A lexer has tokens IF='if', ID=[a-z][a-z0-9]*, and INT=[0-9]+. It applies maximal munch, with IF winning a tie against ID. Which tokenization is produced for the input if2if?

A. IF, INT, IF
B. ID
C. IF, ID
D. Lexical error because digits cannot occur in an identifier.

### Q33. [1 Mark] [NAT]

A connected simple undirected graph has seven vertices and seven edges. Its unique cycle has length4. How many edges of the graph are bridges?

**Answer format:** Exact integer.

### Q34. [1 Mark] [MSQ]

A microprogrammed controller has a control-store address register, a microinstruction register, and combinational next-address logic. A fetched microinstruction specifies both datapath controls and a conditional next address. Which statements hold?

A. A datapath status flag can influence selection of the next microinstruction.
B. The control store must be writable during every machine instruction.
C. Several compatible datapath control signals can be asserted by the same microinstruction.
D. Every machine instruction necessarily executes the same number of microinstructions.

### Q35. [1 Mark] [NAT]

Initially one single-threaded process executes the following pseudocode. Every fork succeeds; a child returns0 from fork, and the parent returns a positive value. No process exits early.

```text
x = fork();
if x == 0 {
    fork();
} else {
    fork();
    fork();
}
```

How many processes, including the original, reach the end?

**Answer format:** Exact integer.

### Q36. [2 Marks] [NAT]

A directed graph has edges s→a(1), a→b(1), b→t(1), s→b(5), a→t(8), and s→t(10), with weights in parentheses. A route is allowed to use at most two edges. By how much does the cheapest permitted route exceed the unrestricted shortest-path distance from s to t?

**Answer format:** Exact integer.

### Q37. [2 Marks] [MSQ]

Let L1={a^n b^n c^m:n,m≥0} and L2={a^m b^n c^n:n,m≥0}. Which statements hold?

A. L1 union L2 is context-free.
B. L1 intersect L2 is regular.
C. L1 intersect L2 equals {a^n b^n c^n:n≥0}.
D. L1 union L2 is regular.

### Q38. [2 Marks] [NAT]

An IPv4 receiver obtains three fragments of one original datagram. Their (fragment offset,payload length,MF) triples are(0,400,1),(75,200,1),(100,120,0). Offsets are in standard IPv4 units; all payload lengths are in bytes. No other fragments have arrived. How many original payload bytes are still missing?

**Answer format:** Exact integer.

### Q39. [2 Marks] [NAT]

A2-to-4 decoder has active-high outputs D0,D1,D2,D3, with exactly the output matching its two-bit input asserted. A combinational circuit computes F=D1 OR D2. Due to a fault, D1 is permanently stuck at1, while other decoder outputs behave normally. Over all four equally likely input combinations, what fraction of inputs produce an incorrect F?

**Answer format:** Exact decimal.

### Q40. [2 Marks] [MCQ]

Let L={a^(n²):n≥0}. For an assumed pumping length p≥1, choose z=a^(p²) and consider any valid regular-pumping decomposition z=uvw with1≤|v|≤p. Which argument correctly shows that pumping v twice leaves L?

A. The new length p²+|v| lies strictly between p² and(p+1)².
B. The new length must be a prime number.
C. The new length is always(p+1)².
D. The new length is smaller than p².

### Q41. [2 Marks] [NAT]

Two processes communicate over two initially empty FIFO channels of capacity one message each. Sending blocks when the destination channel is full; receiving blocks when it is empty. P executes send(a),send(b),receive(x), while Q executes send(c),receive(y),receive(z). P's sends go to Q and Q's send goes to P. Both run fairly, and local computation takes no time. How many messages can remain queued when both processes finish?

**Answer format:** Exact integer.

### Q42. [2 Marks] [NAT]

A byte-addressed machine has a16-bit address bus and a2KiB memory chip. The chip uses A10..A0 internally. Its select signal tests only A15=1 and A14=0; bits A13,A12,A11 are ignored. How many different processor addresses refer to any one fixed byte in this chip?

**Answer format:** Exact integer.

### Q43. [2 Marks] [NAT]

How many distinct permutations of the multiset {A,A,B,B,C,C} have neither the two A's adjacent nor the two B's adjacent? Adjacency of the C's is allowed.

**Answer format:** Exact integer.

### Q44. [2 Marks] [NAT]

Use set relational algebra. Relation E(X,Y) contains(a,b),(a,c),(b,c),(c,c). Form pairs(X,Z) for which some Y satisfies E(X,Y) and E(Y,Z), project away Y, then subtract E after renaming its second attribute to Z. How many tuples remain?

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

A processor issues four stores at cycles0,1,2,3 unless stalled. A single-entry write buffer accepts a store instantly when empty. Each accepted store occupies the buffer for three cycles: one accepted at cycle t completes and frees the entry at cycle t+3, before any issue at that cycle. While the entry is occupied, the next store stalls, and later stores cannot bypass it. At what cycle is the fourth store accepted?

**Answer format:** Exact integer.

### Q46. [2 Marks] [NAT]

Insertion sort on an array of distinct values shifts an earlier element right whenever it is greater than the current key. Count only these shifts, not key placements or failed comparisons. An initial array is formed by concatenating ascending blocks [4,5,6], [1,2,3], and [7,8]. How many shifts does insertion sort perform?

**Answer format:** Exact integer.

### Q47. [2 Marks] [MSQ]

A directed graph permits parallel edges. Its adjacency-list representation stores one entry per edge, while its Boolean adjacency matrix stores only whether at least one edge exists for each ordered vertex pair. Which statements hold?

A. The Boolean matrix alone may not determine the number of edges.
B. Summing entries in a Boolean matrix row always gives the outdegree when parallel edges count separately.
C. Reachability is unchanged if parallel edges are collapsed to one edge.
D. Two different edge multisets can have the same Boolean adjacency matrix.

### Q48. [2 Marks] [NAT]

A synchronous machine has one state bit q, initially0. For input bit x, it emits y=q XOR x and then updates q=x at the clock edge. On input sequence110101, how many emitted bits are1?

**Answer format:** Exact integer.

### Q49. [2 Marks] [MSQ]

A linear-probing hash table uses EMPTY for never-used slots and DELETED for tombstones. Searches stop at EMPTY, but continue past DELETED. Which claims hold?

A. Replacing a deleted occupied slot by EMPTY can make another existing key unreachable by search.
B. An insertion can remember the first DELETED slot, continue searching for an existing copy of its key, then reuse that slot if the key is absent.
C. A search can always stop at DELETED because it no longer contains a key.
D. Tombstones can increase the number of probes in an unsuccessful search.

### Q50. [2 Marks] [MCQ]

Over a finite candidate relation C(x) and a finite required relation S(y), query Q selects candidates satisfying FOR ALL y(S(y) IMPLIES R(x,y)). Query P instead requires FOR ALL y(S(y) AND R(x,y)), where the quantified domain is infinite and S is finite. Which statement holds when S is empty and C is nonempty?

A. Both queries return C.
B. Q returns C, while P returns no candidates.
C. Q returns no candidates, while P returns C.
D. Both queries return no candidates.

### Q51. [2 Marks] [MSQ]

Two Turing machines recognize languages L1,L2 over a finite alphabet, but may loop on nonmembers. Which assertions hold?

A. Nonemptiness of L1 intersect L2 can be recognized by dovetailing simulations on all strings.
B. Running both machines to completion on each string before considering the next always recognizes nonemptiness of their intersection.
C. If both accept some common string, a fair dovetailing search eventually finds one.
D. Failure to find a common accepted string after any finite amount of simulation proves their intersection empty.

### Q52. [2 Marks] [NAT]

SQL table T(g,v) contains(A,2),(A,NULL),(B,NULL),(B,NULL),(C,5). How many rows are returned by the following query?

```sql
SELECT g
FROM T
GROUP BY g
HAVING COUNT(*) > COUNT(v) AND SUM(v) > 1;
```

**Answer format:** Exact integer.

### Q53. [2 Marks] [NAT]

Two signed8-bit fixed-point values each have four fractional bits. Their exact product is computed using a signed16-bit intermediate with eight fractional bits. The operand encodings are00011000 and11110100. What signed integer is stored in the16-bit intermediate, before any rescaling?

**Answer format:** Exact integer, possibly negative.

### Q54. [2 Marks] [MSQ]

Consider these C declarations inside a function. No operation shown overflows.

```c
int a[3] = {2,4,6};
int *p = a + 3;
```

Which subsequent expressions have defined behavior?

A. p - a
B. *(p - 1)
C. *p
D. p == a + 3

### Q55. [2 Marks] [NAT]

For the grammar S→A b A c and A→a | epsilon, construct an LL(1) parsing table using standard FIRST and FOLLOW rules. How many table cells in A's row contain a production, counting each occupied terminal column once? Include the end-marker column if applicable.

**Answer format:** Exact integer.

### Q56. [2 Marks] [NAT]

Shared x initially equals0. Two threads each execute this sequence once, using the same binary semaphore mutex initially1:

```text
wait(mutex);
t = x;          // t is local to the thread
x = t + 1;
signal(mutex);
```

A third thread performs only wait(mutex); signal(mutex). All three threads finish successfully. How many distinct final values of x are possible?

**Answer format:** Exact integer.

### Q57. [2 Marks] [NAT]

A network advertises exactly the address range10.8.0.0 through10.8.5.255, inclusive, using nonoverlapping CIDR prefixes and no addresses outside this range. What is the minimum number of prefixes required?

**Answer format:** Exact integer.

### Q58. [2 Marks] [NAT]

A translation for binary strings uses S→S b | b, where b is a terminal0 or1. At S→b, set S.value=b and S.length=1. At S→Sleft b, set S.value=Sleft.value+b×2^(Sleft.length) and S.length=Sleft.length+1. What value is computed for terminal string10110?

**Answer format:** Exact integer.

### Q59. [2 Marks] [NAT]

A NAT maintains separate TCP and UDP port-allocation pools, each containing the same100 public port numbers on one public IP. Within each protocol a public port may serve only one live internal endpoint; ports are not shared within a protocol even for different remote peers. There are90 live TCP mappings and95 live UDP mappings. How many further mappings can be admitted if new arrivals contain at least100 TCP requests and at least100 UDP requests and no mapping expires?

**Answer format:** Exact integer.

### Q60. [2 Marks] [MCQ]

There are two instances of resource type R and one instance of S. P holds one R and requests S. Q holds S and requests one R. The other R is free. Requests can be granted using any available instance, and a process can finish and release its resources after its pending request is granted. Which statement is correct?

A. P and Q are necessarily deadlocked because their resource-type graph contains a cycle.
B. Granting the free R to Q permits Q to finish, after which P can finish.
C. No process can finish unless a held resource is preempted.
D. The free R is unusable because P already holds an R instance.

### Q61. [2 Marks] [NAT]

A write-back, write-allocate cache has initially empty lines, with16 bytes per block. A processor writes one byte at each of addresses0,1,16,17. The cache has enough space for both blocks and evicts neither during these stores. It is then flushed, writing every dirty block once. Ignoring metadata and counting full-block transfers, how many bytes move between cache and memory in total?

**Answer format:** Exact integer.

### Q62. [2 Marks] [NAT]

A memoized function F(n) has base F(0)=0,F(1)=1. For n≥2 it calls F(n−1), then F(n−2), sums the results, and stores the result. The cache is initially empty, and base cases are cached too. On a cache hit, the function returns immediately. During evaluation of F(6), how many function invocations occur, including cache hits and the initial call?

**Answer format:** Exact integer.

### Q63. [2 Marks] [NAT]

Let an count length-n strings over {0,1,2} in which every run of consecutive2s has even length; runs of0s and1s are unrestricted. The empty string is allowed. What is a4?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

The domain is the labeled set {a,b}. How many binary relations R on this domain satisfy both FOR ALL x EXISTS y R(x,y) and EXISTS x FOR ALL y R(x,y)?

**Answer format:** Exact integer.

### Q65. [2 Marks] [NAT]

For a real parameter t, consider

```text
x + y + z = 1
x + t*y + z = 2
x + y + t*z = 2
```

For every t for which a unique solution exists, let s(t)=x+y+z of that solution. How many real values of t make the system inconsistent?

**Answer format:** Exact integer.

---

## ANSWER KEY — MOCK TEST 034

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 2 |
| 3 | MSQ | 1 | A, C |
| 4 | NAT | 1 | 72 |
| 5 | NAT | 1 | 10 |
| 6 | NAT | 2 | 1.394 (accepted range 1.3935–1.3945) |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 42 |
| 9 | NAT | 2 | 3 |
| 10 | NAT | 2 | 8 |
| 11 | MSQ | 1 | A, B |
| 12 | MSQ | 1 | A, C, D |
| 13 | NAT | 1 | 4 |
| 14 | NAT | 1 | 20 |
| 15 | NAT | 1 | 1 |
| 16 | MCQ | 1 | B |
| 17 | NAT | 1 | 0 |
| 18 | NAT | 1 | 2 |
| 19 | MCQ | 1 | C |
| 20 | MSQ | 1 | A, C |
| 21 | NAT | 1 | 988 |
| 22 | MSQ | 1 | A, B, D |
| 23 | NAT | 1 | 6 |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 3 |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 36 |
| 28 | NAT | 1 | 768 |
| 29 | MCQ | 1 | C |
| 30 | MSQ | 1 | A, B, D |
| 31 | NAT | 1 | 14 |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 3 |
| 34 | MSQ | 1 | A, C |
| 35 | NAT | 1 | 6 |
| 36 | NAT | 2 | 3 |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 200 |
| 39 | NAT | 2 | 0.5 |
| 40 | MCQ | 2 | A |
| 41 | NAT | 2 | 0 |
| 42 | NAT | 2 | 8 |
| 43 | NAT | 2 | 42 |
| 44 | NAT | 2 | 0 |
| 45 | NAT | 2 | 9 |
| 46 | NAT | 2 | 9 |
| 47 | MSQ | 2 | A, C, D |
| 48 | NAT | 2 | 5 |
| 49 | MSQ | 2 | A, B, D |
| 50 | MCQ | 2 | B |
| 51 | MSQ | 2 | A, C |
| 52 | NAT | 2 | 1 |
| 53 | NAT | 2 | −288 |
| 54 | MSQ | 2 | A, B, D |
| 55 | NAT | 2 | 3 |
| 56 | NAT | 2 | 1 |
| 57 | NAT | 2 | 2 |
| 58 | NAT | 2 | 13 |
| 59 | NAT | 2 | 15 |
| 60 | MCQ | 2 | B |
| 61 | NAT | 2 | 64 |
| 62 | NAT | 2 | 11 |
| 63 | NAT | 2 | 29 |
| 64 | NAT | 2 | 5 |
| 65 | NAT | 2 | 1 |

