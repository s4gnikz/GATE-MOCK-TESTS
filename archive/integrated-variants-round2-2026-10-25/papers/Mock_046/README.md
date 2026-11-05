# GATE CS 2027 — Full-Length Mock Test 046

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

### Q1. [1 Mark] [MCQ]

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

### Q2. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A point is first reflected across y=x, then translated by (2,−1). Which point maps to (5,3)?

A. (3,4)  
B. (4,3)  
C. (6,1)  
D. (1,6)

### Q3. [1 Mark] [MCQ]

“Complaints about bus delays fell after an online complaint form was introduced. During the same period, submitting a complaint began to require an account, and the number of completed complaint submissions fell. No independent measurements of bus arrival times were collected.” Which conclusion is best supported?

A. Buses necessarily became more punctual.
B. Every person who stopped submitting complaints encountered punctual buses.
C. The complaint count alone cannot distinguish improved punctuality from reduced reporting.
D. Requiring an account necessarily made buses less punctual.

### Q4. [1 Mark] [NAT]

Three of seven seats in a row are to be marked reserved. No two reserved seats may be adjacent. How many different sets of reserved seats are possible?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

A college's pass rates in both departments increased from one year to the next, but its overall pass rate decreased. Which explanation is possible?

A. The departmental statements and overall statement are mathematically incompatible.
B. The fraction of candidates in the department with the lower pass rate increased sufficiently.
C. The number of departments necessarily increased.
D. Every candidate must have changed departments.

### Q6. [2 Marks] [MSQ]

A cube net consists of unit squares on a square grid. Labelled square centres are A=(0,0), B=(1,0), C=(2,0), D=(1,1), E=(1,2), F=(1,−1). Adjacent grid squares share an edge. Fold the net into a cube. Which listed pairs of faces share an edge on the cube?

A. A and E  
B. A and C  
C. E and F  
D. B and E

### Q7. [2 Marks] [MCQ]

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

### Q8. [2 Marks] [NAT]

A box contains three red and two blue counters. Counters are drawn without replacement until the first blue counter appears. What is the expected number of counters drawn, including that first blue counter?

**Answer format:** Decimal rounded to four places.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The report is concise but not cursory: it omits repetition while addressing every required issue.” What distinction is emphasized?

A. Brevity need not imply superficial treatment.  
B. Concise reports necessarily omit required issues.  
C. Cursory reports must be longer than complete reports.  
D. Repetition is necessary for completeness.

### Q10. [2 Marks] [NAT]

Two fair six-sided dice are rolled independently. Given that their scores differ by exactly one, what is the expected larger score?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

An ER relationship between three distinct entities in set A and four distinct entities in set B is many-to-many, with total participation on both sides. Relationship instances are sets of distinct pairs from A×B. How many different relationship instances have exactly four pairs?

**Answer format:** Exact integer.

### Q12. [1 Mark] [MCQ]

A processor has a write-back data cache with no hardware coherence with DMA. It modifies a buffer, leaving the buffer's cache lines dirty, and then asks a DMA controller to copy that buffer from main memory to a device. The processor will not modify the buffer again during the transfer. Which action before starting DMA ensures that the device receives the updated data?

A. Invalidate the dirty lines without writing them back.  
B. Write back all dirty buffer lines and wait for completion.  
C. Disable device-completion interrupts.  
D. Wait for a DMA-completion interrupt before starting the DMA transfer.

### Q13. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process calls a blocking read on an empty pipe whose write end is still open elsewhere. No signal interrupts the call. Which statements are correct?

**Candidates**

**I.** The process must consume a CPU core continuously until data arrives.

**II.** The operating system can deschedule the blocked process.

**III.** Another process can run on the same core while this process waits.

**IV.** Empty at this instant necessarily means end-of-file.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q14. [1 Mark] [NAT]

A normalized binary floating-point format has five significant bits including the leading 1. What is the spacing between adjacent representable numbers in [8,16), assuming the exponent range includes this interval?

**Answer format:** Exact finite decimal.

### Q15. [1 Mark] [MCQ]

Two consecutive instructions write the same register, and the younger instruction completes first in an out-of-order execution system. Which hazard must be handled to preserve the correct final register value?

A. Write-after-write.
B. Read-after-read.
C. A mandatory memory-address alignment fault.
D. A control hazard caused by all register writes.

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A PDA for balanced parentheses pushes on '(' and pops on ')'. Which extra condition is needed besides having an empty stack at the end, assuming a separate bottom marker?

A. No prefix may attempt to pop below the bottom marker.  
B. The input must have odd length.  
C. Every '(' must be immediately followed by ')'.  
D. The stack may contain only two items throughout the input.

### Q17. [1 Mark] [MCQ]

For grammar A→Aa | Ab | c, which regular expression describes its language?

A. (a|b)*c
B. c(a|b)*
C. a*b*c
D. c(ab)*

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic machine on each fixed input has only finitely many possible configurations, and its full transition relation can be simulated effectively. Which statements are correct?

**Candidates**

**I.** Repeating an identical nonhalting configuration proves that the subsequent computation loops.

**II.** Simulating until it halts, without checking repeats, necessarily terminates.

**III.** Recording visited configurations permits deciding whether this computation eventually accepts.

**IV.** Finiteness alone makes every computation halt.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q19. [1 Mark] [MCQ]

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

### Q20. [1 Mark] [MSQ]

A real 4×4 matrix M satisfies M²=I and trace(M)=0. Which statements must hold?

A. det(M)=1.  
B. rank(M−I)=2.  
C. M is diagonalizable over the real numbers.  
D. M is symmetric.

### Q21. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For Boolean variables x,y, which expressions equal x XOR y for every assignment?

**Candidates**

**I.** (x OR y) AND NOT(x AND y).

**II.** (x AND NOT y) OR (NOT x AND y).

**III.** x OR y.

**IV.** NOT(x XOR y).

A. I and III  
B. I and IV  
C. I and II  
D. II and III

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rooted binary tree has five distinct node labels. Its preorder traversal is A,B,C,D,E and its postorder traversal is C,B,E,D,A. Left and right child positions are distinguished. How many different binary trees have both of these traversals?

A. 1  
B. 2  
C. 4  
D. 8

### Q23. [1 Mark] [MCQ]

In a four-variable Karnaugh map, why are columns labelled 00,01,11,10 rather than 00,01,10,11?

A. Every pair of horizontally adjacent columns, including wraparound, then differs in exactly one bit.
B. Binary numbers must always be written in Gray-code order.
C. The order changes the function's truth table values.
D. Adjacent columns must differ in both bits.

### Q24. [1 Mark] [MSQ]

Over {0,1}, let L be denoted by the regular expression (0|11)*. Which statements are correct?

A. Every maximal contiguous run of 1s in a string in L has even length.
B. Every binary string with an even total number of 1s belongs to L.
C. 110011 belongs to L.
D. 101 belongs to L.

### Q25. [1 Mark] [MCQ]

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

### Q26. [1 Mark] [MCQ]

To refute the regular-language pumping condition, which quantifier order must a proof establish? Here p is a positive pumping length, w∈L has length at least p, and a valid split means w=xyz, |xy|≤p, |y|>0; “fails” means xy^i z∉L for i≥0.

A. There exist p,w, a valid split and i that fails.
B. For every p, there exist w and a valid split for which every i fails.
C. There exists p such that every w has a failing split.
D. For every p, there exists w such that every valid split has some i that fails.

### Q27. [1 Mark] [MCQ]

A process executes the following pseudocode. Every fork succeeds, fork returns 0 only in the child, and all processes eventually execute print once. There is no buffered output before a fork.

```text
i = 0
while i < 3:
    if fork() == 0:
        break
    i = i + 1
print(i)
```

Ignoring output order, which multiset of values is printed?

A. {0,1,2,3}  
B. {0,1,1,2,2,2,3,3}  
C. {3,3,3,3}  
D. {0,0,0,3}

### Q28. [1 Mark] [NAT]

A real polynomial f has five distinct real roots. What is the minimum number of distinct real roots that its second derivative f'' must have?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

R(A,B)={(1,2),(1,3),(2,3)}. Using set semantics, form T(A,C) by joining R(A,B) with a renamed copy R(B,C) on B and projecting on A,C. Rename R's B attribute to C before taking the difference T−R. How many tuples are in this difference?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

Events A and B satisfy P(A)=0.4, P(B)=0.5 and P(A∪B)=0.7. What is P(A|B)?

**Answer format:** Exact decimal.

### Q31. [1 Mark] [NAT]

Among the positive divisors of 12 ordered by divisibility, what is the maximum size of an antichain?

**Answer format:** Integer.

### Q32. [1 Mark] [MCQ]

A depth-first search of a directed graph records discovery and finish times. Vertex u has interval [2,9] and vertex v has interval [4,7]. The graph contains an edge v→u. Which conclusion is necessarily correct?

A. The edge v→u is a tree edge.  
B. The graph contains a directed cycle.  
C. The edge v→u must be a cross edge.  
D. The graph must be acyclic because the intervals are nested.

### Q33. [1 Mark] [NAT]

A factorization PA=LU uses a permutation matrix P that interchanges exactly one pair of rows. L is unit lower triangular, and U has diagonal entries1,2,3. What is det(A)?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DNS configuration contains only the alias records alpha→beta and beta→alpha for the names being resolved, with neither leading to an address record. Which conclusion is appropriate?

A. The resolver can infer an address from either name's spelling.  
B. Following these aliases cycles and cannot produce an address from these records alone.  
C. Two aliases necessarily cancel, yielding the client's own address.  
D. The resolver must return whichever address it used for its previous unrelated query.

### Q35. [1 Mark] [MSQ]

A network-layer packet is carried through two links with different link-layer protocols. No tunnelling or address translation is used. Which statements are correct?

A. The outgoing link can use a different frame format from the incoming link.
B. A router must preserve the incoming link-layer checksum unchanged in the outgoing frame.
C. Link-specific headers may be removed and replaced while forwarding the packet.
D. Changing link-layer protocol necessarily changes the application's message content.

### Q36. [2 Marks] [NAT]

In a four-variable Boolean minimization problem, the only ON minterms are 0,1,2,3 and the only don't-care minterms are 8,9,10,11. All remaining minterms are OFF. Variables are a,b,c,d from most to least significant. What is the minimum number of literals in a single product term covering every ON minterm without covering an OFF minterm?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A continuous function f on[0,1] satisfies f(x)+f(1−x)=x(1−x) for all x in[0,1]. What is the integral of f from0 to1?

**Answer format:** Decimal rounded to four places.

### Q38. [2 Marks] [NAT]

An undirected graph on A,B,C,D has edges AB(1), BC(2), CD(3), DA(4), AC(5), BD(6), with weights in parentheses. What is the minimum weight of a spanning tree whose weight is strictly greater than the minimum-spanning-tree weight?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

An unsigned4-bit comparator is implemented by comparing the two most significant bits first, then the two least significant bits only if the first pair is equal. Over all256 equally likely ordered input pairs(A,B), how many require the second comparison?

**Answer format:** Exact integer.

### Q40. [2 Marks] [NAT]

A hypothetical machine executes ADD (R)+,−(R) with the following precise semantics: fetch the source word at R, increment R by 4, then decrement R by 4, then fetch the destination word at R, add the saved source to it, and write the result to that destination address. Initially R=100, memory word at 100 is 7, and word at 104 is 9. What is the sum of the final values of R and these two memory words?

**Answer format:** Exact integer.

### Q41. [2 Marks] [NAT]

A message queue has capacity3. It starts empty. Process P executes send(A),send(B),send(C),send(D) in order, and process Q has not yet run. Each send blocks if the queue is full; a successful send appends one item. How many of P's sends have completed when it first blocks?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Two threads each execute the following twice, sharing x initially 0:

```text
r = atomic_read(x)    // r is private to this thread
atomic_write(x, r+1)
```

All reads and writes are sequentially consistent, but the read/write pair is not atomic. Each thread preserves its own program order. Which final values of x are possible after both threads finish?

A. 1
B. 2
C. 3
D. 4

### Q43. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let S be the set of encodings of Turing machines whose recognized language contains the string00. Which statements are correct?

**Candidates**

**I.** S is recognizable by simulating the encoded machine on00.

**II.** S is decidable because the input string00 has fixed finite length.

**III.** S is a nontrivial semantic property of recognized languages.

**IV.** Both S and its complement are recognizable.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q44. [2 Marks] [MCQ]

An algorithm for a directed acyclic graph computes longest paths by processing vertices in topological order and relaxing outgoing edges using maximum instead of minimum. Edge weights may be negative. Which statement is correct?

A. Negative edges invalidate this dynamic program even in a DAG.
B. A topological order ensures all predecessors are processed before a vertex, so the recurrence is valid.
C. The algorithm requires all paths to have the same number of edges.
D. The graph must first be converted to an undirected graph.

### Q45. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler may reuse the caller's activation record for a tail call when no work remains after the callee returns and no live local address must survive. Which recursive return expression is eligible under exact integers and ordinary call-by-value semantics, assuming the recursive call otherwise meets these conditions?

A. `return 1 + f(n-1);`  
B. `return f(n-1) * n;`  
C. `return f(n-1, acc*n);`  
D. `return g(f(n-1));`

### Q46. [2 Marks] [MSQ]

Consider `p=A[i]; A[j]=7; q=A[i];` with valid indices, no other changes, and exact ordinary array storage. Which statements are correct?

A. If i≠j is proved, the final load may be replaced by p.
B. With no relation known between i,j, the final load may always be replaced by p.
C. If i=j is proved, the final load's value is 7.
D. The store can never affect any later load from A.

### Q47. [2 Marks] [MCQ]

A binary max-heap contains distinct keys 1 through 7 in an array indexed 1 through 7. The key 6 is at index 3. Which statement characterizes all possible positions of key 5?

A. It must be at index 2.
B. It can be at any of indices 2,4,5,6,7.
C. It can be at indices 2,6,7, and no others.
D. It can be at index 1 or 2 only.

### Q48. [2 Marks] [MSQ]

A directed graph has edges s→a of weight 2, s→b of weight 5, b→a of weight −4, a→t of weight 3 and b→t of weight 1. A standard Dijkstra implementation finalizes vertices in increasing tentative-distance order, breaks the a/b/t ties by choosing t before b, never reopens a finalized vertex, and stops when t is finalized. Which statements are true?

A. The true shortest s-to-t distance is 5.
B. The true shortest s-to-t distance is 4.
C. This graph contains a negative directed cycle.
D. The specified implementation returns 5.

### Q49. [2 Marks] [MSQ]

For a finite relation R(x,y), consider the formula R(x,y) AND NOT exists z(R(x,z) AND z≠y), with x,y free. Which statements are correct?

A. It selects tuples whose x value has exactly one distinct associated y value in R.
B. It rejects every tuple whenever R contains two different x values.
C. The existential variable z ranges over possible competing y values for the same x.
D. It can return an(x,y) pair not in R.

### Q50. [2 Marks] [NAT]

Population A has mean 2 and population variance 1. Population B has mean 8 and population variance 9, and contains three times as many observations as A. What is the population variance after combining all observations? Use divisor N for each population variance, not N−1.

**Answer format:** Exact finite decimal.

### Q51. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Records carry keys(city,year) and a distinct arrival number. The required order is ascending city, then ascending year, with original arrival order retained when both keys tie. Only single-key sorts are available. Which procedures always meet the requirement?

**Candidates**

**I.** Stable sort by year, then stable sort by city.

**II.** Stable sort by city, then stable sort by year.

**III.** Stable sort by arrival number, then stable sort by year, then stable sort by city.

**IV.** Arbitrary unstable sort by year, then stable sort by city.

A. I and II  
B. I and IV  
C. II and III  
D. I and III

### Q52. [2 Marks] [MSQ]

A finite monoid M has identity e and satisfies left cancellation: ax=ay implies x=y for all a,x,y in M. Which statements follow?

A. For fixed a, the map x↦ax is a bijection on M.
B. Every a has a right inverse b with ab=e.
C. Such a b also satisfies ba=e.
D. The conclusion that every element is invertible follows by the same finite-cardinality argument for arbitrary infinite monoids.

### Q53. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An NFA has states p,q,r, initial state p and sole accepting state r. Its transitions are δ(p,0)={p,q}, δ(p,1)={p}, δ(q,0)=δ(q,1)={r}, and δ(r,0)=δ(r,1)=∅. There are no epsilon transitions. Which statements are true?

A. After reading 010, the reachable-state set is {p,q}.  
B. The NFA accepts 010 because some earlier prefix reached r.  
C. Subset construction has exactly four reachable subsets.  
D. The recognized language consists of binary words whose second-last symbol is zero.

### Q54. [2 Marks] [MCQ]

A TCP connection has congestion window 10,000 bytes and advertised receive window 7,000 bytes. Its oldest unacknowledged sequence number is 20,000 and the next unsent byte has sequence number 25,000. There is no wraparound. An ACK arrives with acknowledgment number 23,000 and advertised receive window 4,000; assume the congestion window remains unchanged and no data are sent before processing it. How many additional data bytes may be sent immediately?

A. 1,000
B. 2,000
C. 4,000
D. 5,000

### Q55. [2 Marks] [NAT]

The grammar S→(S)S | epsilon generates balanced parenthesis strings. How many distinct strings with four opening and four closing parentheses have maximum nesting depth exactly 2?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

Evaluate (7+3)+(−5) using four-bit signed two's-complement integers, rounding neither operand. In implementation S, each addition saturates at −8 or 7 if needed. In implementation W, each addition wraps modulo 16. What are the final signed results (S,W)?

A. (5,5)  
B. (2,5)  
C. (2,−11)  
D. (7,−6)

### Q57. [2 Marks] [NAT]

A binary code consists of all length4 bit strings having even parity. A codeword is transmitted through a channel where each bit independently flips with probability1/4. What is the probability that at least one bit changes but the received string is another valid codeword?

**Answer format:** Exact decimal.

### Q58. [2 Marks] [MCQ]

A lexer has the token rules `a`, `b`, `d`, and `ab*c`, where `b*` means zero or more b symbols. It uses longest match. An implementation reads forward until no token rule can still match, then returns to the most recent accepting position to emit that token. Consider the inputs `ab^n d`, with no spaces and arbitrary integer n>=1. Before returning the first token, how much lookahead beyond the most recent accepting position can this implementation require?

A. At most one character, independently of n.  
B. At most two characters, independently of n.  
C. An amount unbounded as n grows.  
D. Zero, because the rule `a` can be emitted immediately upon reading a.

### Q59. [2 Marks] [MCQ]

Two positive-edge-triggered D flip-flops store bits (q1,q0). At every active clock edge both are updated simultaneously according to q1(next) = q0 XOR q1 and q0(next) = NOT q1. The initial state is (0,0). What is the state after 2027 active clock edges?

A. (0,0)  
B. (0,1)  
C. (1,1)  
D. (1,0)

### Q60. [2 Marks] [NAT]

A connected undirected graph has six vertices and seven edges. Removing a particular edge e leaves it connected. How many edges must then be removed from the remaining graph to obtain a spanning tree, if removals may be chosen appropriately?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

Sales(dept,amount) contains (A,10),(A,NULL),(A,20),(B,NULL),(B,NULL),(C,5). Standard SQL NULL and aggregate semantics apply. Consider:

```sql
SELECT dept, SUM(amount) AS total
FROM Sales
GROUP BY dept
HAVING COUNT(*) > COUNT(amount) AND SUM(amount) > 10;
```

Which statements are correct?

A. The query returns exactly one row.  
B. The row for A has total 30.  
C. The query returns B with total 0.  
D. Replacing COUNT(amount) in the HAVING clause by COUNT(*) makes the result empty.

### Q62. [2 Marks] [MSQ]

A directed graph permits parallel edges. Its adjacency-list representation stores one entry per edge, while its Boolean adjacency matrix stores only whether at least one edge exists for each ordered vertex pair. Which statements hold?

A. The Boolean matrix alone may not determine the number of edges.
B. Summing entries in a Boolean matrix row always gives the outdegree when parallel edges count separately.
C. Reachability is unchanged if parallel edges are collapsed to one edge.
D. Two different edge multisets can have the same Boolean adjacency matrix.

### Q63. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which expression is guaranteed to stay within the same C array object when a is an array of four integers and p=a+4? Forming a one-past pointer is permitted, but dereferencing it is not.

A. *p  
B. *(p−1)  
C. *(p+1)  
D. a[4]

### Q64. [2 Marks] [NAT]

A code generator evaluates the expression tree

```text
((a+b)*(c+d)) + ((e+f)*(g+h))
```

All eight leaves are distinct values initially in memory. Loading a leaf requires one register. Each binary operation requires its two operands in registers and may overwrite either operand. Subtrees may be evaluated in either order, but tree operations may not be reassociated, recomputed, or interleaved between sibling subtrees, and no intermediate value may be spilled to memory. What is the minimum number of registers required?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A microinstruction includes 12 independent control bits, a next-address field for a 256-word control store, and a two-bit sequencing mode. There are no other fields or encoding restrictions. How many bits wide is each microinstruction?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 046

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | MSQ | 1 | A, C, D |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 10 |
| 5 | MCQ | 1 | B |
| 6 | MSQ | 2 | A, C |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 2.0000 (accepted range 1.99995–2.00005) |
| 9 | MSQ | 2 | B, C, D |
| 10 | NAT | 2 | 4 |
| 11 | NAT | 1 | 36 |
| 12 | MCQ | 1 | B |
| 13 | MCQ | 1 | D |
| 14 | NAT | 1 | 0.5 |
| 15 | MCQ | 1 | A |
| 16 | MSQ | 1 | B, C, D |
| 17 | MCQ | 1 | B |
| 18 | MCQ | 1 | C |
| 19 | MCQ | 1 | C |
| 20 | MSQ | 1 | A, B, C |
| 21 | MCQ | 1 | C |
| 22 | MSQ | 1 | A, B, D |
| 23 | MCQ | 1 | A |
| 24 | MSQ | 1 | A, C |
| 25 | MCQ | 1 | B |
| 26 | MCQ | 1 | D |
| 27 | MCQ | 1 | A |
| 28 | NAT | 1 | 3 |
| 29 | NAT | 1 | 0 (exact) |
| 30 | NAT | 1 | 0.4 |
| 31 | NAT | 1 | 2 |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | -6 |
| 34 | MSQ | 1 | A, C, D |
| 35 | MSQ | 1 | A, C |
| 36 | NAT | 2 | 1 |
| 37 | NAT | 2 | 0.0833 (accepted range 0.08325–0.08335) |
| 38 | NAT | 2 | 7 |
| 39 | NAT | 2 | 64 |
| 40 | NAT | 2 | 123 |
| 41 | NAT | 2 | 3 |
| 42 | MSQ | 2 | B, C, D |
| 43 | MCQ | 2 | A |
| 44 | MCQ | 2 | B |
| 45 | MSQ | 2 | A, B, D |
| 46 | MSQ | 2 | A, C |
| 47 | MCQ | 2 | C |
| 48 | MSQ | 2 | B, D |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 13.75 |
| 51 | MCQ | 2 | D |
| 52 | MSQ | 2 | A, B, C |
| 53 | MCQ | 2 | B |
| 54 | MCQ | 2 | B |
| 55 | NAT | 2 | 7 (exact) |
| 56 | MCQ | 2 | B |
| 57 | NAT | 2 | 0.21484375 |
| 58 | MCQ | 2 | C |
| 59 | MCQ | 2 | C |
| 60 | NAT | 2 | 1 |
| 61 | MSQ | 2 | A, B, D |
| 62 | MSQ | 2 | A, C, D |
| 63 | MSQ | 2 | A, C, D |
| 64 | NAT | 2 | 4 |
| 65 | NAT | 2 | 22 |
