# GATE CS 2027 — Full-Length Mock Test 067

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

Four runners finish without ties. A finishes before B; C finishes after B; D finishes before C. Which runner can finish neither first nor last?

A. A
B. B
C. C
D. D

### Q2. [1 Mark] [NAT]

How many four-digit positive integers use each of the digits 0,1,2,3 exactly once and are divisible by four? A leading zero is not permitted.

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A report lists the following mutually exclusive journey categories. A journey is chosen uniformly from all recorded journeys. What is the probability that it is a delayed journey lasting more than 20 minutes?

| Duration | Total journeys | Delayed journeys |
|---|---:|---:|
| At most 20 minutes | 40 | 6 |
| More than 20, at most 40 minutes | 35 | 14 |
| More than 40 minutes | 25 | 10 |

**Answer format:** Exact decimal.

### Q4. [1 Mark] [NAT]

A thin square sheet occupies 0≤x≤4, 0≤y≤4. Fold the right half onto the left along x=2, then the top half onto the bottom along y=2. From the resulting folded square, remove the entire horizontal strip 0≤x≤2, 0.5<y<1 through every layer. After unfolding, how many connected pieces of paper remain? The cuts extend fully to both side edges of the folded square.

**Answer format:** Exact integer.

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The word “qualified” in “The reviewer offered qualified support for the proposal” most nearly means:

A. Entirely unconditional  
B. Subject to reservations or conditions  
C. Expressed by an untrained person  
D. Legally prohibited

### Q6. [2 Marks] [NAT]

A bag contains four distinct red balls and two distinct blue balls. Three balls are selected uniformly without replacement. Given that the selection contains at least one blue ball, what is the probability that it contains exactly one blue ball?

**Answer format:** Exact finite decimal.

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A policy states: “Unless the permit is renewed before Monday, the pilot must stop on Monday. Renewal alone does not authorize expansion; an independent review is also required.” Assume the policy is followed and the pilot continues on Tuesday. Which conclusion is justified?

A. An independent review must already have authorized expansion.  
B. The permit was renewed before Monday, but authorization for expansion cannot be inferred.  
C. Continuing the pilot automatically authorizes expansion.  
D. The permit could have remained unrenewed because an independent review replaces renewal.

### Q8. [2 Marks] [NAT]

A positive quantity doubles every three hours. Another positive quantity triples every six hours. They begin with equal values. After how many hours does the ratio of the first quantity to the second first reach16/9? Growth is continuous with these constant exponential rates.

**Answer format:** Exact number of hours.

### Q9. [2 Marks] [MSQ]

For real numbers a,b, define a⋆b=2a+b. Which identities or implications hold for all real a,b,c?

A. (a⋆b)⋆c=a⋆(b⋆c)
B. a⋆b=b⋆a
C. If a⋆b=a⋆c, then b=c.
D. a⋆(b+c)=(a⋆b)+c

### Q10. [2 Marks] [NAT]

A 5×5 grid of unit squares is rotated by 90 degrees about its centre. How many distinct orbits of squares are there under repeated applications of this rotation? Squares in the same orbit count once.

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

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

### Q12. [1 Mark] [MSQ]

A foreign key has two columns(x,y) and uses the stated rule: if either referencing component is NULL, no referenced-row match is required; otherwise the pair must match. Which inserted pairs can pass the foreign-key check when the referenced table is empty?

A. (NULL,5)
B. (7,NULL)
C. (NULL,NULL)
D. (7,5)

### Q13. [1 Mark] [MSQ]

Let f(x)=|x| for real x. Which statements are correct at x=0?

A. f is continuous.
B. Its left derivative is−1 and its right derivative is1.
C. Its derivative exists and equals0 because f has a minimum there.
D. Every continuous function is differentiable there.

### Q14. [1 Mark] [MSQ]

A nondeterministic pushdown automaton accepts if at least one computation branch consumes the whole input and reaches a designated final state. Which statements are correct?

A. A rejecting branch prevents acceptance even if another branch accepts.
B. An infinite branch need not prevent acceptance by a different finite branch.
C. Reaching a final state before consuming all input is sufficient under the stated rule.
D. Acceptance uses an existential condition over branches.

### Q15. [1 Mark] [NAT]

A discrete random variable takes values 0,1,2 with probabilities k,2k,3k respectively. What is P(X≥1)? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q16. [1 Mark] [NAT]

An array initially contains[1,2,3,4,5]. First copy its first four entries to positions1 through4, using zero-based indices and semantics as if the source were saved in a temporary array before writing. Then similarly copy positions2 through4 to positions0 through2. What is the sum of all five final entries?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A four-variable Boolean function is1 on exactly the minterms0000,0001,0011,0010 and0 elsewhere. How many literals occur in a minimum sum-of-products expression?

**Answer format:** Integer.

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A dynamic array doubles capacity when an append encounters a full array and halves capacity immediately when a removal leaves size exactly half the current capacity. Each resize copies all retained elements. Starting with size and capacity both n, repeatedly append one element and then remove it, for k repetitions. Ignore unrelated work. What is the total copying cost?

A. Θ(k)  
B. Θ(n+k)  
C. Θ(kn)  
D. Θ(log n)

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Routers A,B,D initially have link costs AD=1, BD=4, AB=1 and correct shortest-path routes to D. AD then changes to 10. A recomputes using the new complete link-state graph, while B temporarily retains its old table. What can happen to a packet for D forwarded by A during this interval?

A. It must follow A→D because A has a direct link.  
B. It can loop A→B→A until a table changes or the packet expires.  
C. It must follow A→B→D because B's direct link is unchanged.  
D. A correctly computed individual table makes transient loops impossible.

### Q20. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An n-bit adder has carry-in0, carry into the sign bit c and final carry-out d. Which statements are correct for two's-complement addition?

**Candidates**

**I.** Signed overflow is indicated by c XOR d.

**II.** Final carry-out alone always indicates signed overflow.

**III.** Adding operands of opposite signs cannot cause signed overflow.

**IV.** A result with sign bit1 always indicates overflow.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A transaction commits before any transaction whose uncommitted data it read has committed. Which recovery property can this violate?

A. Recoverability.  
B. The fact that read–read operations commute.  
C. The definition of a primary key.  
D. The physical size of disk blocks.

### Q22. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Transaction T1 locks every existing row satisfying salary>100 and counts those rows twice. Between the counts, T2 inserts and commits a new row with salary150. The system uses only row locks on existing rows; no predicate or range locks are acquired. Which statements hold?

A. T1's locks need not prevent T2's insertion.  
B. The second count can exceed the first despite locking all originally qualifying rows.  
C. Locking existing rows necessarily locks every future row satisfying the same predicate.  
D. A suitable predicate lock can prevent the insertion until T1 releases it.

### Q23. [1 Mark] [MSQ]

Consider this program with exact integers and an arbitrary Boolean input flag. A conventional nonrelational constant-propagation analysis tracks, for each variable separately, either a single constant or 'not constant'; at a join, distinct incoming constants become 'not constant'.
```text
if flag:
    x = 2; y = 3
else:
    x = 3; y = 2
z = x + y
```
Which statements are correct?

A. Every execution assigns5 to z.  
B. The stated analysis finds x constant at the join.  
C. The stated analysis necessarily infers z=5 directly from the joined abstract values of x and y.  
D. Moving the assignment z=x+y into the end of each branch allows the stated analysis to find z=5 after the join.

### Q24. [1 Mark] [MCQ]

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

### Q25. [1 Mark] [NAT]

A scalar constant-propagation analysis sees three incoming paths to a join. Two set x=4; the third is provably unreachable and would set x=9. If unreachable paths are excluded, what constant value can be assigned to x at the join?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

A process incurs three page faults in sequence. Each fault reads one page from disk; the first and third evict dirty pages, while the second evicts a clean page. No writes are merged or deferred. How many page-sized disk transfers occur in total?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

A control ROM is addressed by a two-bit operation code, a three-bit microstep index and two condition bits. Every address combination has a word containing 20 control bits and a seven-bit next address. How many bits does the ROM contain, including unused address combinations?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A recursive algorithm on an input of size16 calls itself on sizes n/2 and n/4 whenever n≥4, and stops immediately for n<4. How many leaf calls occur?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A real3×3 matrix A has rank1 and trace5. What is trace(A²)?

**Answer format:** Exact number.

### Q30. [1 Mark] [NAT]

For real c, let f(x)=x³−3x²+cx on [0,2]. What is the smallest c for which f is nondecreasing throughout this interval?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

A synchronous two-bit machine updates Q0′=NOT Q0 and Q1′=Q1 XOR Q0, using the old state for both expressions. Starting at Q1Q0=10, what unsigned integer does its state represent after five clock edges?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

An inode has a link count of3. One pathname is renamed within the same file system without replacing an existing destination, and another pathname is then unlinked. Assume no other directory changes. What is the inode's final hard-link count?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

An ER relationship assigns each of 17 employees to exactly one department, and each department must have at least three assigned employees. Departments with no assigned employees are forbidden. What is the largest possible number of departments?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An HTTP cache has two stored representations of the same URL, selected by different values of a request header named in Vary. Why must that header be considered during lookup?

A. The same URL can require different cached representations depending on that header.  
B. Vary means every cached representation has an infinite lifetime.  
C. HTTP never uses request headers.  
D. The header changes the TCP sequence-number arithmetic.

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Over alphabet {0,1}, let L be the set of strings having equal numbers of0s and1s. Which statements are correct?

**Candidates**

**I.** L is regular.

**II.** L is context-free.

**III.** The intersection of L with 0*1* is {0^n1^n : n≥0}.

**IV.** L contains only strings in which every0 precedes every1.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q36. [2 Marks] [NAT]

A ternary relationship R(A,B,C) contains exactly (a1,b1,c1), (a1,b2,c2), (a2,b1,c2). It is replaced by its three binary projections on AB, AC and BC, then reconstructed by their natural join. How many tuples appear in the reconstructed relation but not in R?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

Memory has four interleaved banks. Consecutive word addresses use banks 0,1,2,3 cyclically. The controller issues at most one request per cycle; a bank next accepts a request no earlier than six cycles after its previous request. Eight consecutive word reads starting at address zero are issued in order as early as possible. All banks are initially idle and the first request issues at cycle 0. At which cycle does the eighth request issue?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

At the exit of the following straight-line block, only r is live. Assignments are evaluated sequentially.

```text
a=b+c;
d=a+e;
a=f;
r=d+a;
```

How many distinct variables are live at block entry?

**Answer format:** Exact integer.

### Q39. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The available closed intervals are [0,4], [3,8], [7,10], [0,6], [6,9], [8,10]. Starting at 0, a greedy covering algorithm repeatedly chooses, among intervals beginning at or before the current covered endpoint, an interval extending that endpoint farthest. It stops when [0,10] is covered. Which sequence does it select?

A. [0,4], [3,8], [8,10]  
B. [0,6], [6,9], [8,10]  
C. [0,6], [7,10]  
D. [0,4], [7,10]

### Q40. [2 Marks] [NAT]

A processor can perform two arithmetic operations per ns and main memory can transfer eight bytes per ns. Each independent iteration needs eight arithmetic operations and 24 bytes of memory traffic. An optimization reduces arithmetic work to four operations per iteration without changing traffic. Assume perfect overlap of computation and transfers, no startup cost, and no other bottleneck. What is the ratio of optimized to original steady-state iteration throughput? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q41. [2 Marks] [NAT]

A binary max-heap contains distinct keys. The heap has15 elements and is represented in a one-based array. A decrease-key operation changes the root to a value smaller than every other key, then restores heap order by repeatedly swapping with the larger child. How many swaps occur?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A stop-and-wait sender retransmits one packet until it receives an acknowledgment. Each data transmission is independently lost with probability 0.2. Each successfully received copy triggers an acknowledgment, independently lost with probability 0.1. An unsuccessful attempt times out before the next begins; there are no delayed packets or acknowledgments. Count every receiver arrival, including duplicates. What is the expected number of duplicate arrivals before the sender stops, excluding the first received copy? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q43. [2 Marks] [NAT]

An undirected multigraph has vertices a,b,c, two parallel edges between a and b, one edge between b and c, and one self-loop at a. An incidence matrix has one column per edge; a non-loop contributes 1 to each endpoint, and a loop contributes 2 to its vertex. An adjacency-list representation stores two entries for every undirected edge, including a loop. What is the sum of the degree of a and the total number of adjacency-list entries?

**Answer format:** Exact integer.

### Q44. [2 Marks] [NAT]

A paged machine uses 1 KiB pages and two page-table levels. Its six-bit virtual page number splits into a two-bit root index and a four-bit leaf index. For root index 2, the root entry selects a leaf table whose entry 3 maps to physical frame 9. What physical byte address corresponds to virtual byte address (35×1024)+17? All mentioned mappings are valid.

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A fair coin selects whether a second experiment uses two or three independent tosses of another fair coin. You are told only that the second experiment contained at least one head. What is the conditional probability that it used three tosses? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q46. [2 Marks] [NAT]

Under set semantics, R(A)={1,2,3} and S(A,B)={(1,x),(1,y),(2,x)}. Compute R−projection_A(S). How many tuples are in the result?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A process has ordinary private integer x=2 and an integer y=3 in an explicitly shared memory mapping. It forks. The child sets x=10 and y=20, then exits. After waiting for that child, the parent starts one thread that executes x=x+y and then joins it. No other changes occur. What is the parent's final x?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let P be the set of all subsets of {a,b,c}, ordered by inclusion. Remove only {a,b,c}, keeping the other seven elements. Which statements hold in the resulting poset?

**Candidates**

**I.** Every pair still has a greatest lower bound.

**II.** Every pair still has a least upper bound.

**III.** The empty set remains the least element.

**IV.** There is a greatest element.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q49. [2 Marks] [NAT]

A direct-mapped cache has four lines and one word per line. Word address w maps to line w mod4. Starting empty, it accesses words0,4,1,5,0,4,1,5. A fully associative cache of four lines, using LRU and starting empty, sees the same trace. How many misses in the direct-mapped cache are eliminated by the fully associative cache?

**Answer format:** Exact integer.

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In tuple relational calculus, R(x) is a unary relation containing {1,2}. Consider the expression {x | NOT R(x)}, with x ranging over the entire interpretation domain. Which statements hold?

A. Over domain {1,2,3}, its result is {3}.  
B. Over domain {1,2,3,4}, its result is still {3}.  
C. Its result depends on values outside R, so it is not domain-independent.  
D. Replacing the formula by R(x) AND NOT R(x) yields a domain-independent empty result.

### Q51. [2 Marks] [NAT]

Let A be the4×4 tridiagonal matrix with diagonal entries2, immediate subdiagonal and superdiagonal entries−1, and all other entries0. In its LU factorization without pivoting, with L unit lower triangular, what is U's last diagonal entry?

**Answer format:** Exact decimal.

### Q52. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider a context-free pumping-lemma proof attempt for L = {a^n b^n c^n : n ≥ 0}. For an arbitrary pumping length p ≥ 1, choose s = a^p b^p c^p. A legal decomposition is s = uvxyz, with |vxy| ≤ p and |vy| > 0, and pumping produces uv^i xy^i z. Which claims are correct?

A. The substring vxy cannot contain both an a and a c.  
B. For every legal decomposition, pumping with i=0 produces a string outside L.  
C. It is sufficient to exhibit one legal decomposition for which pumping with i=0 produces a string outside L.  
D. A proof may assume, without treating other cases, that v and y each contain only a symbols.

### Q53. [2 Marks] [NAT]

A2-to-4 decoder has active-high outputs D0,D1,D2,D3, with exactly the output matching its two-bit input asserted. A combinational circuit computes F=D1 OR D2. Due to a fault, D1 is permanently stuck at1, while other decoder outputs behave normally. Over all four equally likely input combinations, what fraction of inputs produce an incorrect F?

**Answer format:** Exact decimal.

### Q54. [2 Marks] [NAT]

The exact value −1.375 is rounded to a signed fixed-point format with two fractional bits and sufficient integer range. Rounding is to nearest, ties to an even encoded integer. What real value is stored?

**Answer format:** Exact finite decimal.

### Q55. [2 Marks] [NAT]

A continuously differentiable function f on[0,2] satisfies f(2)=4 and the integral of f(x) over[0,2] equals3. What is the integral of x f'(x) over[0,2]?

**Answer format:** Exact number.

### Q56. [2 Marks] [NAT]

A TCP sender has congestion window 10 segments, advertised receive window 12 segments and eight unacknowledged segments. It first sends as many additional segments as allowed. A subsequent cumulative ACK acknowledges five of the outstanding segments; for the next send decision, congestion window is set to eight and the new advertised receive window is six segments. There are no retransmissions or other changes. How many new segments can be sent in total across these two send decisions?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

Two signed8-bit fixed-point values each have four fractional bits. Their exact product is computed using a signed16-bit intermediate with eight fractional bits. The operand encodings are00011000 and11110100. What signed integer is stored in the16-bit intermediate, before any rescaling?

**Answer format:** Exact integer, possibly negative.

### Q58. [2 Marks] [MSQ]

For an arbitrary Turing machine M, define L_M={x : M accepts x within at most |x| transition steps}. Which statements are correct?

A. L_M is decidable for every M.
B. Deciding L_M requires deciding whether M eventually halts on x.
C. A decider can simulate exactly the bounded number of allowed steps and reject if no acceptance has occurred.
D. L_M must be empty whenever M fails to halt on some other input.

### Q59. [2 Marks] [MSQ]

A basic block is `t=a+b; a=a+1; u=a+b; v=t;`. Arithmetic is exact, and scalar variables have no aliases. Which transformations preserve the final values of a,t,u,v for all initial a,b?

A. Replace `v=t` by `v=a+b-1` after the other statements.
B. Replace `u=a+b` by `u=t`.
C. Replace `u=a+b` by `u=t+1`.
D. Delete `t=a+b` while leaving `v=t` unchanged and without introducing another definition of t.

### Q60. [2 Marks] [MSQ]

An undirected graph on A,B,C,D has edges AB=1, AC=2, BC=2, BD=3, CD=3, AD=4. Which statements are correct?

A. Every minimum spanning tree contains AB.
B. Exactly four minimum spanning trees exist.
C. The smallest spanning-tree weight strictly greater than the minimum is 8.
D. Raising AD's weight from 4 to 100 leaves the set of minimum spanning trees unchanged.

### Q61. [2 Marks] [NAT]

Two processes communicate using two separate FIFO channels, one in each direction. Each channel has a positive integer capacity measured in messages. Each process sends two messages to the other, then receives two. A send blocks only while its channel is full; a receive blocks only while its channel is empty. Under fair execution, what is the minimum sum of the two channel capacities that guarantees completion?

**Answer format:** Integer.

### Q62. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be any language over a finite alphabet. Define Pref(L)={x:xy∈L for some string y}. Which statements are correct?

A. If L is regular, Pref(L) is regular.  
B. If L is recognizable, Pref(L) is recognizable.  
C. If Pref(L) is regular, L must be regular.  
D. If L is nonempty, ε belongs to Pref(L).

### Q63. [2 Marks] [NAT]

How many Boolean functions of three labelled variables depend essentially on all three variables? A variable is essential if changing only that variable changes the function value for at least one assignment of the other variables.

**Answer format:** Integer.

### Q64. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider ordinary IPv4 fragmentation. Payload means the fragment's bytes after its own IP header. Which statements are correct?

A. A fragment with MF=1 must have a payload length divisible by8.  
B. A final fragment may have a payload length that is not divisible by8.  
C. The fragment-offset field directly gives a byte count without scaling.  
D. A fragment's own IP header bytes are not included when locating its payload using the fragment offset.

### Q65. [2 Marks] [NAT]

A syntax-directed definition for binary strings uses S→S1 b and S→b, where b is0 or1. For S→b, set S.val=b and S.len=1. For S→S1 b, set S.val=S1.val+2^(S1.len)·b and S.len=S1.len+1. What is S.val for the string10110?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 067

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 4 |
| 3 | NAT | 1 | 0.24 |
| 4 | NAT | 1 | 3 |
| 5 | MSQ | 1 | A, C, D |
| 6 | NAT | 2 | 0.75 |
| 7 | MSQ | 2 | A, C, D |
| 8 | NAT | 2 | 12 |
| 9 | MSQ | 2 | C, D |
| 10 | NAT | 2 | 7 |
| 11 | NAT | 1 | 6 |
| 12 | MSQ | 1 | A, B, C |
| 13 | MSQ | 1 | A, B |
| 14 | MSQ | 1 | B, D |
| 15 | NAT | 1 | 0.8333 (range 0.83325–0.83335) |
| 16 | NAT | 1 | 16 |
| 17 | NAT | 1 | 2 |
| 18 | MSQ | 1 | A, B, D |
| 19 | MSQ | 1 | A, C, D |
| 20 | MCQ | 1 | C |
| 21 | MSQ | 1 | B, C, D |
| 22 | MCQ | 1 | C |
| 23 | MSQ | 1 | A, D |
| 24 | MCQ | 1 | C |
| 25 | NAT | 1 | 4 |
| 26 | NAT | 1 | 5 |
| 27 | NAT | 1 | 3456 |
| 28 | NAT | 1 | 5 |
| 29 | NAT | 1 | 25 |
| 30 | NAT | 1 | 3 (exact) |
| 31 | NAT | 1 | 3 |
| 32 | NAT | 1 | 2 |
| 33 | NAT | 1 | 5 |
| 34 | MSQ | 1 | B, C, D |
| 35 | MCQ | 1 | D |
| 36 | NAT | 2 | 1 |
| 37 | NAT | 2 | 9 |
| 38 | NAT | 2 | 4 |
| 39 | MSQ | 2 | A, C, D |
| 40 | NAT | 2 | 1.3333 (range 1.33325–1.33335) |
| 41 | NAT | 2 | 3 |
| 42 | NAT | 2 | 0.1111 (range 0.11105–0.11115) |
| 43 | NAT | 2 | 12 |
| 44 | NAT | 2 | 9233 |
| 45 | NAT | 2 | 0.5385 (range 0.53845–0.53855) |
| 46 | NAT | 2 | 1 |
| 47 | NAT | 2 | 22 |
| 48 | MCQ | 2 | D |
| 49 | NAT | 2 | 4 |
| 50 | MCQ | 2 | B |
| 51 | NAT | 2 | 1.25 |
| 52 | MSQ | 2 | C, D |
| 53 | NAT | 2 | 0.5 |
| 54 | NAT | 2 | -1.5 |
| 55 | NAT | 2 | 5 |
| 56 | NAT | 2 | 3 |
| 57 | NAT | 2 | −288 |
| 58 | MSQ | 2 | A, C |
| 59 | MSQ | 2 | A, C |
| 60 | MSQ | 2 | A, B, D |
| 61 | NAT | 2 | 3 |
| 62 | MCQ | 2 | C |
| 63 | NAT | 2 | 218 |
| 64 | MCQ | 2 | C |
| 65 | NAT | 2 | 13 |
