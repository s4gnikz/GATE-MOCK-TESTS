# GATE CS — Additional Practice Set 019

**Questions:** 50  
**Maximum marks:** 73

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider this recursive function on a positive integer n. Arithmetic is exact.

```text
f(n):
    if n == 1: return 1
    r = f(floor(n/2))
    if n is even: return 2*r
    else: return 2*r + 1
```

Which pair gives f(45) and the number of simultaneous active calls at maximum recursion depth, including the initial and base calls?

A. (45,6)  
B. (45,5)  
C. (32,6)  
D. (63,6)  

### Q2. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For a 0/1 knapsack with nonnegative integer capacity W and items of positive integer weights wi and positive values vi, let D[j] initially be zero for every 0 ≤ j ≤ W. Each item may be used at most once. Consider the update `D[j] = max(D[j], D[j-wi] + vi)` for j ≥ wi. Which statements are correct?

A. Processing each item once and scanning j downward from W to wi computes the maximum value for capacity W.  
B. Processing each item once and scanning j upward from wi to W always computes the same 0/1 optimum.  
C. With one item of weight 2 and value 3 and capacity 4, an upward scan produces D[4]=6.  
D. For a downward scan, immediately before updating D[j] for an item, D[j-wi] still excludes that item.  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relation R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which is its highest normal form among the choices below? Assume atomic attribute values.

A. 1NF but not 2NF  
B. 2NF but not 3NF  
C. 3NF but not BCNF  
D. BCNF  

### Q4. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed graph has exactly these weighted edges:

```text
s -> a :  2
s -> b :  5
b -> a : -4
a -> t :  2
b -> t : 10
```

For the version of Dijkstra's algorithm in this question, the unsettled vertex with smallest tentative distance is settled, settled vertices are never revised, and the algorithm stops when t is settled. Which statements are correct?

**Candidates**

**I.** The true shortest-path distance from s to t is 3.

**II.** The specified Dijkstra algorithm returns 4 on this graph.

**III.** Adding 4 to every edge weight leaves the identity of a shortest s-to-t path unchanged.

**IV.** The negative edge implies that the graph contains a negative-weight directed cycle.

A. III and IV  
B. I and III  
C. I and IV  
D. I and II  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 4-to-1 multiplexer has select bits A,B, with A more significant. Its data inputs for select values 00,01,10,11 are C, NOT C, 1,0 respectively. Minterms are numbered using A,B,C with A most significant. Which set is the output's on-set?

A. {0,3,4,5}  
B. {1,2,4,5}  
C. {1,2,6,7}  
D. {0,1,2,5}  

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A Banker's-algorithm system has two resource types. Current available resources are (1,1). Allocation and remaining need are:

| Process | Allocation | Remaining need |
|---|---|---|
| P0 | (1,0) | (1,2) |
| P1 | (0,1) | (2,0) |
| P2 | (1,1) | (1,1) |

Consider each request independently from the displayed state. Which statements are correct?

A. The current state has exactly two safe process-completion orders.  
B. Granting P0's request (1,0) would make the state unsafe.  
C. Granting P1's request (1,0) leaves a safe state.  
D. Granting P2's request (1,0) leaves a safe state.  

### Q7. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A two-level AND–OR circuit implements F=AB+(NOT A)C. Only A changes while B=C=1. Gate delays are positive and unequal. Which single redundant product term can be added to eliminate the possible static-1 hazard for this transition without changing F?

A. AC  
B. (NOT B)C  
C. BC  
D. A(NOT C)  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two private hosts each use UDP source port 5000. H1 sends to server endpoint S1 and to distinct server endpoint S2; H2 sends to S1. Compare NAT mapping policies: endpoint-dependent creates a separate mapping for each (private address,private port,destination address,destination port); endpoint-independent creates one for each (private address,private port). All mappings remain live. How many mappings are needed under the two policies, respectively?

A. (3,2)  
B. (2,3)  
C. (3,3)  
D. (2,2)  

### Q9. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider exact integers, pure arithmetic, and an arbitrary input n. A compiler proposes moving the division in this loop to just before the loop:

```text
i = 0
while i < n:
    t = 100 / n
    use(t)
    i = i + 1
```

Integer division truncates toward zero; division by zero traps. `use` does not modify n. Which statements are correct?

A. The expression 100/n is loop invariant.  
B. Unconditionally hoisting it is semantics-preserving for every integer n.  
C. Hoisting it inside a preceding `if n > 0` guard preserves division behaviour and use results.  
D. Invariance alone is insufficient to justify evaluating the expression on a path where the original did not evaluate it.  

### Q10. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A quicksort variant partitions a subarray into keys less than, equal to, and greater than its pivot, in time Θ(m) for a subarray of length m. It recurses only on the less-than and greater-than parts. What is its running time on n equal keys?

A. Θ(1)  
B. Θ(log n)  
C. Θ(n)  
D. Θ(n²)  

### Q11. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router receives destination 172.16.5.200. Its routes are 172.16.0.0/16→A, 172.16.4.0/22→B, 172.16.5.128/25→C, and a default route→D. A forwarding policy first chooses the longest matching prefix; among equal-length matches it chooses the lowest metric. The /25 route has metric 100 and the /22 route metric 1. Which next hop is selected, and why?

A. B, because metric 1 is smaller than 100.  
B. C, because prefix length is considered before metric.  
C. A, because a /16 covers more addresses.  
D. D, because the overlapping routes are ambiguous.  

### Q12. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a basic block, p and q are pointers to valid int objects and may alias. Consider `t=*p; *q=7; u=*p;`. There is no concurrency or volatile access. Which statements are correct?

**Candidates**

**I.** Replacing the final load by u=t is valid whenever p and q are proved to point to different objects.

**II.** The replacement is valid for all possible aliases and initial values.

**III.** If p=q and the initial pointed-to value is 3, the original block ends with t=3,u=7.

**IV.** A store through q cannot affect a subsequent load through p because the pointer names differ.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q13. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An eight-bit pattern is interpreted either as sign-magnitude or as two's complement. Which statements are correct?

A. 10000000 denotes zero in sign-magnitude.  
B. 10000000 denotes −128 in two's complement.  
C. Both representations assign the same value to every pattern with leading bit 1.  
D. Both assign the same value to every pattern with leading bit 0.  

### Q14. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language L is both recognizable and co-recognizable. Given recognizers for L and its complement, how can a decider be constructed?

A. Run the recognizer for L forever and reject if it has not accepted after any fixed universal timeout.  
B. Dovetail the two recognizers and decide according to which accepts first.  
C. Reject all strings because nontermination is possible.  
D. Reverse the transitions of the recognizer for L.  

### Q15. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected weighted graph has a cycle whose edge weights are 1,2,2,5. Other edges may exist. Which statements necessarily hold?

**Candidates**

**I.** The weight-5 edge on this cycle belongs to no minimum spanning tree of a connected graph containing it.

**II.** Every weight-2 edge on the cycle belongs to no minimum spanning tree.

**III.** Removing that weight-5 edge preserves connectivity of its original connected component.

**IV.** The minimum spanning tree is necessarily unique.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A JK flip-flop is initially 0. Across four successive active clock edges, its (J,K) inputs are (1,0),(1,1),(0,0),(0,1). What are the four successive output values?

A. 1,0,0,0  
B. 1,1,1,0  
C. 0,1,1,0  
D. 1,0,1,0  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Town A introduced a road-safety campaign and its accident count fell by 20%. During the same period a similar town without the campaign also had a 20% fall. Which conclusion is most defensible from these facts alone?

A. The campaign certainly caused all of A's reduction.  
B. The campaign certainly had no effect whatsoever.  
C. A common external change could explain both reductions; these counts alone do not isolate the campaign's effect.  
D. Accident counts in different towns must always move together.  

### Q18. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The domain is a nonempty set and R is a binary relation. Which implications are valid for every interpretation?

**Candidates**

**I.** (∃y∀x R(x,y)) → (∀x∃y R(x,y))

**II.** (∀x∃y R(x,y)) → (∃y∀x R(x,y))

**III.** (∀x∀y R(x,y)) → (∃y∀x R(x,y))

**IV.** (∃x∃y R(x,y)) → (∀x∃y R(x,y))

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q19. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Variables x and y are unsigned w-bit integers, w≥2, and all arithmetic is modulo 2^w. Which transformations preserve values for all x,y?

A. Replace x+x by 2*x.  
B. Replace (x+y)−y by x.  
C. Replace x/2 by x>>1, where division truncates and >> is logical.  
D. Replace x/2 by x*2.  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two processes share a memory region but use no synchronization. Why does shared-memory IPC alone not guarantee a correct producer–consumer protocol?

A. Shared memory cannot store more than one byte.  
B. Visibility of common storage does not by itself ensure correct ordering or mutual exclusion.  
C. The two processes necessarily have identical register values.  
D. Sharing storage automatically serializes all accesses.  

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“A train service reduced the average delay but increased the maximum delay.” Which statement follows from these two statistics alone?

A. Every passenger experienced a shorter delay.  
B. At least one statistic improved while the worst observed delay became larger.  
C. The statistics are mathematically inconsistent.  
D. The median delay necessarily increased.  

### Q22. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider `t=a+b; if (p) a=0; u=a+b;`, with ordinary nonaliased scalars and both branches feasible. Which statements hold?

A. Replacing the final expression by t unconditionally is generally unsound.  
B. On the path where p is false, the earlier value t remains available for the final expression.  
C. On the path where p is true, t necessarily equals the new a+b for all initial values.  
D. Common-subexpression availability must account for definitions along paths.  

### Q23. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP receiver initially expects byte 1000. Four 100-byte segments cover byte ranges 1000–1099,1100–1199,1200–1299,1300–1399. They arrive in the order third,first,fourth,second. The receiver buffers out-of-order data and sends a cumulative ACK after each arrival, stating the next missing byte. Which ACK sequence is correct?

A. 1300,1100,1400,1200  
B. 1000,1100,1100,1400  
C. 1000,1200,1300,1400  
D. 1100,1200,1300,1400  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A memory allocator has two nonadjacent free holes of 40 bytes each, but no free hole of 60 bytes. A request needs a contiguous 60-byte block. What explains failure despite 80 free bytes in total?

A. External fragmentation.  
B. Internal fragmentation inside the requested block before it is allocated.  
C. A necessary arithmetic overflow.  
D. The existence of exactly two CPU cores.  

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A, B and C finish a race at distinct times. Exactly two of these statements are true: “A finishes before B”; “B finishes before C”; “C finishes before A.” B does not finish last. Which competitors could finish first?

**Candidates**

**I.** A

**II.** B

**III.** C

**IV.** None of the three

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q26. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B,C,D) has dependencies A→B, B→A and C→D, with no additional independent dependencies. Which statements are true?

**Candidates**

**I.** AC and BC are exactly its candidate keys.

**II.** R is already in BCNF.

**III.** Decomposition into AB, CD and AC is lossless and preserves all the given dependencies.

**IV.** Decomposition into AB and CD alone is guaranteed lossless.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV  

### Q27. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L1={aⁿbⁿ:n≥0} and L2={aⁿb^(2n):n≥0}. Which statements are true?

A. L1∪L2 is context-free.  
B. L1∩L2={ε}.  
C. Every intersection of two context-free languages is context-free.  
D. L1L2 is context-free.  

### Q28. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A dynamic array starts with capacity one. Appending to a full array allocates a new array of twice the capacity and copies all existing elements; other appends take constant time. Which statements hold over n appends starting empty?

**Candidates**

**I.** The total copying work is O(n).

**II.** The total copying work is necessarily Θ(n log n).

**III.** A single append can take Θ(n) time when the current number of elements is proportional to n.

**IV.** Every individual append has worst-case constant time.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A notice must express that a visitor may enter only when accompanied by a guide, while making no promise that accompaniment alone guarantees entry. Which sentence states precisely this necessary condition?

A. Every visitor accompanied by a guide may enter.  
B. A visitor may enter if and only if accompanied by a guide.  
C. A visitor may enter only if accompanied by a guide.  
D. A visitor may enter unless accompanied by a guide.  

### Q30. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A proposed proof claims that the regular language a*b* is not regular: “For pumping length p choose a^p b^p. Select a decomposition whose pumped part contains both a and b. Pumping twice destroys the required order.” Which objections correctly identify flaws?

**Candidates**

**I.** A nonregularity proof must defeat every legal decomposition, not just one selected decomposition.

**II.** Any legal decomposition with prefix-plus-pumped-part length at most p has its pumped part entirely among the a's.

**III.** The pumping lemma permits an empty pumped part, so the proof must use one.

**IV.** Choosing a string of length2p is forbidden by the pumping lemma.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider ordinary integer variables with no overflow or side effects:

```text
x = a * 0
y = x + b
x = 7
return y
```

Which replacement computes the same returned value for all inputs?

A. return 7+b  
B. return a+b  
C. return b  
D. return 0  

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes unsigned integer tokens, the operator '-', and identifiers. It tokenizes x--12 without treating '--' as a separate operator. The parser alone distinguishes unary and binary minus. Which token sequence is produced?

A. identifier(x), minus, integer(−12)  
B. identifier(x), minus, minus, integer(12)  
C. identifier(x−−12)  
D. identifier(x), decrement, integer(12)  

### Q33. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sentence states that every report was read by at least one reviewer, without asserting that a single reviewer read all reports?

A. One reviewer read every report.  
B. Every report was read by some reviewer.  
C. Every reviewer read every report.  
D. No reviewer read a report.  

### Q34. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let h be a homomorphism that maps each symbol of a finite alphabet to a finite string, possibly ε. Which statements are correct?

A. The image under h of a regular language is regular.  
B. The image under h of a context-free language is context-free.  
C. A nonregular language must remain nonregular under every such h.  
D. Erasing every symbol maps every nonempty language to{ε}.  

### Q35. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A singly linked list is acyclic. A pointer p identifies a non-tail node, but the predecessor of p is unavailable. A proposed deletion copies the successor's value into p and bypasses that successor. Which statements are correct?

A. The resulting value sequence matches deleting p's original value at that position.  
B. The operation preserves the identity of every node that ordinary deletion of p would preserve.  
C. It requires p to have a successor under the stated implementation.  
D. External references to node identities can make this different from actually deleting node p.  

### Q36. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed graph has a DFS forest. Which statements are correct?

**Candidates**

**I.** An edge from a vertex to a currently active ancestor on the recursion stack certifies a directed cycle.

**II.** Every edge to a previously finished vertex certifies a directed cycle.

**III.** A DAG has no DFS back edge under the ancestor definition.

**IV.** A graph with one back edge is necessarily strongly connected.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q37. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A PDA can make epsilon transitions that do not consume input. Which statements are correct?

**Candidates**

**I.** An epsilon transition may still change the state and stack.

**II.** Every epsilon transition must leave the stack unchanged.

**III.** A computation can contain several epsilon transitions between consecutive consumed symbols.

**IV.** An epsilon transition consumes a special extra input character not in the input string.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q38. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router forwards an IPv4 datagram from one Ethernet link to another. Assume no tunnelling or network address translation. Which pair of fields is necessarily replaced with values appropriate to the outgoing link?

A. Source and destination IPv4 addresses  
B. Source and destination TCP port numbers  
C. Ethernet source and destination MAC addresses  
D. Application sequence numbers  

### Q39. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A finite binary floating-point format rounds to nearest and has a largest finite positive value M. Which statements are correct, assuming real input values may exceed the representable range?

**Candidates**

**I.** Every real number in[−M,M] is exactly representable.

**II.** Distinct real values can round to the same finite floating-point number.

**III.** Having sufficient exponent range alone does not guarantee exact representation of every fraction.

**IV.** Every arithmetic result with magnitude below M must be represented exactly.

A. III and IV  
B. I and II  
C. II and III  
D. I and III  

### Q40. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A five-stage IF–ID–EX–MEM–WB pipeline executes a load followed immediately by a store of the loaded register. Their address calculations are independent. Load data becomes available at the end of its MEM stage; store data is needed only at the start of its MEM stage. Which statements are correct?

**Candidates**

**I.** A forwarding path from the completed load's data to the next cycle's store-data input can avoid a stall.

**II.** The store necessarily needs the loaded value for its EX address calculation.

**III.** Without forwarding, waiting for register write-back may be necessary.

**IV.** Every load-followed-by-store pair must stall regardless of available forwarding paths.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Every approved design is either tested or exempt, but never both. No exempt design uses material M. Design D is approved and uses material M. Which conclusions follow?

**Candidates**

**I.** D is tested.

**II.** D is exempt.

**III.** D is not exempt.

**IV.** Every tested design uses material M.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A one-slot producer–consumer buffer uses semaphores empty=1 and full=0. The producer incorrectly performs wait(empty), signal(full), then writes the item. The consumer performs wait(full), reads the item, signal(empty). Assume semaphore operations are atomic and scheduling may switch between any two operations. Which statements are correct?

**Candidates**

**I.** The consumer can read before the producer writes the new item.

**II.** Atomic semaphore operations alone eliminate this ordering error.

**III.** Moving the producer's signal(full) after the write repairs this particular publication error.

**IV.** The consumer's wait(full) forces all future producer writes to occur before its read.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q43. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Inputs A,B encode only the three states00,01,10;11 is unreachable. The required output is0 at00 and1 at01 and10. Behaviour at11 is unconstrained. Which expressions correctly implement the specified behaviour on every reachable state?

A. A OR B  
B. A XOR B  
C. A AND B  
D. NOT(A AND B)  

### Q44. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A BFS from s runs on an undirected graph with edges sa, sb, ac, ad, be, and ce. Vertices are marked when enqueued. Which discovery order is impossible, regardless of adjacency-list ordering?

A. s,a,b,c,d,e  
B. s,b,a,e,c,d  
C. s,a,b,c,e,d  
D. s,a,b,d,c,e  

### Q45. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider the grammar

```text
S → a A | a B
A → b
B → c
```

The start symbol is S and the terminals are a,b,c. Which statements hold?

**Candidates**

**I.** The grammar as written has an LL(1) conflict in S's row.

**II.** The language cannot be generated by any LL(1) grammar.

**III.** Left factoring S into S→aX, X→b|c yields an LL(1) grammar for the same language.

**IV.** The grammar is ambiguous because both S productions begin with a.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An algorithm is given a Turing machine M promised to halt on every input and an integer n≥0. Which tasks can be decided by an algorithm that terminates on every promised input?

**Candidates**

**I.** Determine whether M accepts every binary string of length exactly n.

**II.** Determine whether M accepts at least one binary string of length at most n.

**III.** Determine whether M accepts every binary string of arbitrary length.

**IV.** Determine whether M accepts no binary strings of arbitrary length.

A. I and IV  
B. I and II  
C. II and III  
D. II and IV  

### Q47. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two Turing machines recognize languages L1,L2 over a finite alphabet, but may loop on nonmembers. Which assertions hold?

**Candidates**

**I.** Nonemptiness of L1 intersect L2 can be recognized by dovetailing simulations on all strings.

**II.** Running both machines to completion on each string before considering the next always recognizes nonemptiness of their intersection.

**III.** If both accept some common string, a fair dovetailing search eventually finds one.

**IV.** Failure to find a common accepted string after any finite amount of simulation proves their intersection empty.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A write-ahead logging system uses undo and redo records. A transaction's commit record is forced to stable storage before success is reported, but its changed data pages need not yet be on disk. Which statements hold?

**Candidates**

**I.** Redo may be required after a crash for a transaction already reported committed.

**II.** A dirty data page may be written before its corresponding update log record is durable without violating write-ahead logging.

**III.** Forcing the commit record can ensure earlier records in the same sequential log are durable as well.

**IV.** A committed transaction must be undone merely because its data page was not flushed before the crash.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A learning Ethernet switch's forwarding table is initially empty. Host A on port 1 sends a unicast frame to host B, which is on port 2. The switch has three ports and no filtering restrictions. What does the switch do with this first frame?

A. Learn B on port 1 and forward only to port 2.  
B. Learn A on port 1 and flood through ports 2 and 3.  
C. Learn A on port 2 and drop the frame.  
D. Learn both A and B from the frame and forward only to port 2.  

### Q50. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An engineer tests a device at every integer temperature from 0°C through 100°C. It operates correctly in all tests. No rule governing its behaviour between tested temperatures is known. Which statements are justified solely by these observations?

**Candidates**

**I.** The device operates correctly at 37°C under the tested conditions.

**II.** The device must operate correctly at 37.5°C.

**III.** The observations are compatible with a device that fails at 37.5°C.

**IV.** The device must operate correctly at every integer temperature above 100°C.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

---

## ANSWER KEY — SET 019

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | MCQ | 2 | B |
| 3 | MSQ | 1 | A, B, D |
| 4 | MCQ | 2 | D |
| 5 | MSQ | 1 | A, C, D |
| 6 | MCQ | 2 | C |
| 7 | MSQ | 1 | A, B, D |
| 8 | MSQ | 2 | B, C, D |
| 9 | MCQ | 2 | B |
| 10 | MSQ | 1 | A, B, D |
| 11 | MSQ | 2 | A, C, D |
| 12 | MCQ | 1 | D |
| 13 | MCQ | 1 | C |
| 14 | MSQ | 2 | A, C, D |
| 15 | MCQ | 2 | C |
| 16 | MSQ | 1 | B, C, D |
| 17 | MSQ | 2 | A, B, D |
| 18 | MCQ | 2 | B |
| 19 | MCQ | 2 | D |
| 20 | MSQ | 1 | A, C, D |
| 21 | MSQ | 1 | A, C, D |
| 22 | MCQ | 2 | C |
| 23 | MSQ | 2 | A, C, D |
| 24 | MSQ | 1 | B, C, D |
| 25 | MCQ | 1 | A |
| 26 | MCQ | 2 | B |
| 27 | MCQ | 1 | C |
| 28 | MCQ | 1 | D |
| 29 | MSQ | 1 | A, B, D |
| 30 | MCQ | 2 | B |
| 31 | MSQ | 1 | A, B, D |
| 32 | MSQ | 1 | A, C, D |
| 33 | MSQ | 1 | A, C, D |
| 34 | MCQ | 2 | C |
| 35 | MCQ | 2 | B |
| 36 | MCQ | 1 | D |
| 37 | MCQ | 1 | A |
| 38 | MSQ | 1 | A, B, D |
| 39 | MCQ | 1 | C |
| 40 | MCQ | 1 | D |
| 41 | MCQ | 1 | A |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 2 | C, D |
| 44 | MSQ | 1 | A, B, D |
| 45 | MCQ | 2 | A |
| 46 | MCQ | 2 | B |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | D |
| 49 | MSQ | 1 | A, C, D |
| 50 | MCQ | 1 | B |
