# GATE CS 2027 — Full-Length Mock Test 062

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

Exactly one of K,L,M is a coordinator. K is a coordinator only if L is available. L is unavailable. If M is a coordinator, N is available. Which conclusions necessarily follow?

**Candidates**

**I.** K is not the coordinator.

**II.** L is the coordinator.

**III.** Either L or M is the coordinator.

**IV.** N is available.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV

### Q2. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An ordered triangle has vertices A=(0,0),B=(4,0),C=(0,3). Reflect all its vertices across the y-axis, rotate them90 degrees counterclockwise about the origin, then translate them by(7,−2). What is the signed area of the resulting ordered triangle, with counterclockwise orientation positive?

**Required precision:** Exact signed number.

A. -12  
B. -3  
C. -6  
D. -5

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A study reports that among applicants who passed a competitive screening, experience and examination score were negatively associated. The screening favoured applicants with either strong experience or a high score. Which conclusion is justified by this description alone?

A. Experience causes lower examination scores in all applicants.  
B. Restricting attention to screened applicants may create an association absent in the full applicant pool.  
C. The screening must have ignored experience.  
D. No applicant can have both strong experience and a high score.

### Q4. [1 Mark] [NAT]

Six distinct people A,B,C,D,E,F sit around a circular table with six equally spaced seats. Arrangements differing only by rotation are identical; mirror images are distinct. A and B must sit opposite one another, and C and D must be adjacent. How many arrangements satisfy both restrictions?

**Answer format:** Exact integer.

### Q5. [1 Mark] [NAT]

Among25 recorded journey times,7 are at most10 minutes,19 are at most20 minutes, and all25 are at most30 minutes. A journey is selected uniformly from those lasting more than10 minutes. What is the probability that it lasted at most20 minutes?

**Answer format:** Decimal rounded to four places.

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A square sheet occupies 0 <= x <= 8 and 0 <= y <= 8. Fold its left half onto its right half along x=4. Next fold its bottom half onto its top half along y=4. Punch small point-like holes through all layers at (5,6) and (6,5) in the folded sheet. After fully unfolding, how many distinct holes lie on the line y=x+1? Ignore hole diameter and sheet thickness.

A. 4  
B. 1  
C. 2  
D. 3

### Q7. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A tariff charges 4 units for each of the first ten units consumed and 6 units for each additional unit. Consumption is an integer. A bill also includes a fixed charge of 15. What is the largest consumption whose total bill does not exceed 100?

**Required precision:** Integer units consumed.

A. 17  
B. 34  
C. 9  
D. 18

### Q8. [2 Marks] [NAT]

An urn contains two red and two blue balls. Balls are drawn uniformly without replacement until the first red ball appears. Given that the procedure stopped within the first two draws, what is the probability that it stopped on the first draw?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The evaluator called the design economical, not because it was cheap to manufacture, but because each component served several purposes.” Which interpretation best preserves the stated distinction?

A. The evaluator praised efficient use of components without asserting low manufacturing cost.  
B. The evaluator established that manufacturing was inexpensive.  
C. The design uses no components.  
D. Multifunctional components necessarily increase manufacturing cost.

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An investment grows by the same annual factor for two years, reaching 144% of its original value. In a third year it falls by 25%. What is its final value as a percentage of its original value?

**Required precision:** Integer percentage, without the percent sign.

A. 216  
B. 54  
C. 109  
D. 108

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A real 6×6 matrix A satisfies A²=0. What is the largest possible rank of A?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

Two increasing runs contain four and three distinct keys respectively, with all seven keys different. Every original left-run position precedes every right-run position. Exactly five cross inversions exist, where a cross inversion is a left key greater than a right key. Standard merging compares the first remaining keys, emits the smaller, and stops comparisons as soon as either run is exhausted. What is the minimum possible number of key comparisons?

**Answer format:** Numeric value; integer.

### Q13. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An instruction at byte address100 has length4 bytes and a signed PC-relative displacement−6. The architecture defines the target as the address of the next instruction plus twice the displacement. What is the target byte address?

**Required precision:** Integer.

A. 184  
B. 92  
C. 46  
D. 93

### Q14. [1 Mark] [NAT]

A ticket lock stores next-ticket and currently-served ticket numbers modulo eight. Every new contender obtains the next ticket and advances that counter atomically, then enters when its ticket equals the currently-served value. The owner has not yet released the lock and no previously issued ticket has completed. What is the smallest total number of outstanding contenders, including the current owner, that can give another contender the owner's ticket through counter wraparound?

**Answer format:** Integer.

### Q15. [1 Mark] [NAT]

An unknown Boolean condition selects one of two branches. The first assigns x=2 and y=x; the second assigns x=3 and y=x. Immediately after the branches join, z=x−y is evaluated with exact arithmetic. What value is guaranteed for z even though neither x nor y individually has a unique constant value at the join?

**Answer format:** Integer.

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A tuple-calculus query uses `Employee(e) AND EXISTS d (Department(d) AND Works(e,d))`. What does it require of each returned employee?

A. Assignment to at least one listed department.  
B. Assignment to every department.  
C. No assignments at all.  
D. That every domain object be a department.

### Q17. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A four-bit ripple-carry adder adds binary operands1011 and0110 with carry-in0. Let c1,c2,c3,c4 be the carry out of bit positions0,1,2,3 respectively, where bit0 is least significant. What unsigned integer is represented by c4c3c2c1?

**Required precision:** Exact integer.

A. 28  
B. 14  
C. 7  
D. 15

### Q18. [1 Mark] [NAT]

A four-bit ring counter circulates a single 1 through its flip-flops, starting at 1000. How many clock edges are needed to return to 1000 for the first time?

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An undirected graph has vertices 1–5 and edges {1,2},{2,3},{3,4},{4,2},{1,5}. How many articulation vertices does it have? Removing an articulation vertex and its incident edges increases the number of connected components.

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q20. [1 Mark] [NAT]

A signed six-bit two's-complement fixed-point value has two fractional bits. What is the greatest positive real number it can represent?

**Answer format:** Exact finite decimal.

### Q21. [1 Mark] [NAT]

Two balls are drawn without replacement from a bag containing two red and two blue balls. Let X and Y be the indicators that the first and second drawn balls, respectively, are red. Find Cov(X,Y), rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q22. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A DFA has exactly one accepting state, which is its initial state. Every input symbol moves it to a rejecting sink that loops on every symbol. Over a two-symbol alphabet, how many words does it accept?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q23. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic finite automaton has missing transitions, which cause immediate rejection. To recognize the complement over the same alphabet, which statements are correct?

**Candidates**

**I.** Swapping accepting and rejecting states alone always suffices.

**II.** Completing the automaton with a rejecting sink before swapping accepting states works.

**III.** A word rejected by taking a missing transition must be accepted by a correct complement automaton.

**IV.** Adding a sink after swapping states and leaving that sink rejecting always works.

A. I and II  
B. II and III  
C. I and III  
D. I and IV

### Q24. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Two independent fair coins are tossed. Their colours are red and blue, so they are distinguishable. A report states that the red coin is heads. What is the conditional probability that exactly one coin is heads?

**Required precision:** Exact decimal.

A. 0.3  
B. 0.8  
C. 0.5  
D. 0.1

### Q25. [1 Mark] [NAT]

A tree has ten vertices. What is the sum of its vertex degrees?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

Insert 8,3,10,1,6,4,7 into an initially empty ordinary binary search tree, with no rebalancing. Delete key 3 by replacing it with its inorder successor and then removing that successor's old node. What is the key of the left child of node 6 after deletion?

**Answer format:** Enter -1 if the child is absent; otherwise enter its key.

### Q27. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Order the set{1,2,3,4,12} by divisibility. Which statements are correct?

A. This poset is a lattice.  
B. This lattice is distributive.  
C. The join of2 and3 is12.  
D. The meet of4 and3 is1.

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Grammar S→SS | a generates strings of a's. Count ordered parse trees, not derivation orders. How many parse trees generate aaaa?

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A link-state router retains, for each origin, only the advertisement with the highest sequence number. Sequence numbers do not wrap in this scenario. For origin X, it receives advertisements (sequence,link cost)=(41,5),(43,9),(42,2),(43,9). Which link cost from X remains in its database?

A. 2  
B. 5  
C. 9  
D. 25

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider a resource-allocation graph for processes waiting for reusable resources; a resource type may have multiple instances. Which statements hold in the standard model?

**Candidates**

**I.** A deadlock implies a directed cycle.

**II.** An acyclic graph rules out deadlock.

**III.** Every directed cycle proves deadlock even with multiple instances per resource type.

**IV.** A cycle-free graph proves every process has already finished.

A. I and IV  
B. I and II  
C. II and III  
D. II and IV

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Table T(k,v) has rows(1,10),(1,NULL),(2,NULL). How many rows are returned?

```sql
SELECT k FROM T GROUP BY k HAVING COUNT(v) = 0;
```

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q32. [1 Mark] [NAT]

Gaussian elimination without row exchanges factors A=LU, where L has unit diagonal. For

```text
A = [ 2  1  0
      4  3  1
      2  2  3 ]
```

what is the entry U33 after both elimination stages?

**Answer format:** Exact integer.

### Q33. [1 Mark] [MSQ]

Consider this basic block; on exit only z is live. Variables have ordinary scalar values, and evaluating expressions has no side effects.

```text
1: x = a + b
2: y = x + c
3: x = d + e
4: z = y + x
```

Which statements are correct?

A. Immediately before line3, the old value of x is live.
B. Immediately before line3, y is live.
C. Both assignments to x contribute to the final z.
D. Line1 can be removed merely because line3 also assigns x.

### Q34. [1 Mark] [MCQ]

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

### Q35. [1 Mark] [MSQ]

A table T(a,b) has a UNIQUE constraint on a and a separate NOT NULL constraint on b. Values of a are restricted to non-NULL values in the instances considered. Which statements must hold in every legal instance?

A. No two rows have the same a value.
B. Every b value occurs in at most one row.
C. Every row has a non-NULL b value.
D. Every possible non-NULL a value appears in a row.

### Q36. [2 Marks] [NAT]

A three-address intermediate representation has one binary operation per assignment. To compute a*b+a*c+d*b+d*c, a compiler may reassociate and factor over mathematical integers and reuse intermediates. What is the minimum number of binary additions/multiplications needed if it uses the factorization(a+d)*(b+c)?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

An initially empty cache has two sets, two lines per set, and 16 bytes per line. A byte address belongs to block floor(address/16), mapped to set (block number mod 2). The cache uses LRU replacement within each set. Each miss fetches the referenced block; all accesses below are reads, in order:

```text
0, 32, 0, 64, 32, 16, 48, 80, 16
```

How many block fetches from memory occur?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

A microprogram has a two-entry return stack, initially empty. Instruction CALL pushes the following address and branches; RETURN pops and branches to that address. Starting at address0, execute:

```text
0: CALL 4
1: HALT
4: CALL 8
5: RETURN
8: RETURN
```

Every listed microinstruction takes one cycle. How many cycles elapse through HALT?

**Answer format:** Exact integer.

### Q39. [2 Marks] [NAT]

An undirected graph has triangle vertices A,B,C with all three triangle edges of weight1. Vertex D is joined to A by a weight2 edge and to B by a weight3 edge; there are no other edges. How many distinct minimum spanning trees does the graph have?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A store-and-forward network has links S→R and R→D, each taking 1 ms to transmit one packet. Propagation is zero. At time 0, S has packets A,B,C in order. A and C must traverse both links; B terminates at R. Each link begins transmitting whenever its next eligible packet is available, preserving source order among packets that use it. What time in milliseconds does C finish arriving at D?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A lexer recognizes keywords `if`, identifiers matching `[a-z]+`, and single-character operators `<` and `=`. It uses maximal munch, breaking equal-length keyword/identifier ties in favour of the keyword. For input `ifx<if==x`, how many tokens are identifiers? There are no multi-character operators in this language.

**Answer format:** Integer.

### Q42. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A simple undirected graph has degree sequence(3,3,2,2,2). How many edge entries are stored in ordinary adjacency lists when each edge is recorded at both endpoints?

**Required precision:** Integer.

A. 24  
B. 6  
C. 13  
D. 12

### Q43. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary floating-point system has four significant bits including the leading 1, unbounded exponents, and round-to-nearest with ties to even after each addition. Starting at x=8, perform x=x+0.5 sixteen times. Which statements are correct?

A. The final stored x is 8.  
B. The exact real-arithmetic result would be 16.  
C. Every one of the sixteen additions is exact in this format.  
D. Instead adding 2 to the initial x four times gives stored result 16.

### Q44. [2 Marks] [NAT]

Keys 40,20,60,10,30,50,70,25,35 are inserted in that order into an initially empty ordinary BST. Delete 20 by replacing its key with its inorder predecessor and physically removing that predecessor's original node. Then delete 40 by replacing its key with its inorder successor and physically removing that successor's original node. What is the key at the lowest common ancestor of 25 and 70 in the resulting tree?

**Answer format:** Integer key.

### Q45. [2 Marks] [NAT]

Evaluate ∫ from −1 to 2 of |x²−x| dx. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q46. [2 Marks] [NAT]

A byte-addressed 16-bit system selects one 4 KiB memory chip whenever address bits A15A14 equal 10. The chip uses A11…A0 as its local address, and A13,A12 are not decoded. How many distinct physical bytes are accessible in the selected 16 KiB address window?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

An unspanned fixed-record file uses 1000-byte blocks. Records are 120 bytes, and each block reserves a 40-byte header. How many blocks are needed for 81 records, with no compression and no record crossing a block boundary?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A disk uses C-SCAN on cylinders 0–99, moving upward. Initially the head is at 40 and requests are pending at 10,30,50,90. No new requests arrive. It services upward requests, travels to 99, jumps to 0, and then resumes upward service. Count the jump as head movement; service time is zero. How many cylinders does the head travel before all requests are served?

**Required precision:** Integer.

A. 376  
B. 94  
C. 188  
D. 189

### Q49. [2 Marks] [NAT]

A directed graph has edges s→a(1),s→b(4),b→a(−5),a→t(1),b→t(10). An implementation runs Dijkstra's algorithm and terminates as soon as t is extracted as minimum, despite the negative edge. What is its reported distance minus the actual shortest s-to-t distance?

**Answer format:** Integer.

### Q50. [2 Marks] [NAT]

An initially empty B+ tree has a single root leaf. Each leaf holds at most three keys. Inserting a fourth key splits a leaf into two leaves of two keys each, promoting the first key of the right leaf to the parent; the key remains in the leaf. Insert1,2,3,4,5,6 in order. The internal root can hold at least three separators. How many leaf nodes exist afterward?

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An NPDA chooses one of two branches at the start. Its first branch recognizes {a^i b^j c^k : i=j, i,j,k≥0}; its second recognizes {a^i b^j c^k : j=k, i,j,k≥0}. Acceptance requires consuming the entire input and acceptance by at least one branch. Which words does it accept?

A. aabbccc  
B. aabbbccc  
C. aaabcc  
D. abc

### Q52. [2 Marks] [MSQ]

Boolean function F=(x+y)(x+z). Which expressions are equivalent to F?

A. x+yz
B. x(y+z)
C. (x+y)(x+z)(x+y+z)
D. xy+xz

### Q53. [2 Marks] [NAT]

A disk head is at cylinder50. Three requests target55,30,80. Seek time is one time unit per cylinder. Their additional rotational waits after reaching the target are respectively50,0,0 time units; transfer times are equal and may be ignored. How much larger is the first-request service time selected by shortest-seek-time-first than the smallest available first-request service time?

**Answer format:** Integer time units.

### Q54. [2 Marks] [NAT]

Routers R and S forward packets by longest-prefix match. R has a connected route for 10.0.0.0/25 and a default route via S. S has a connected route for 10.0.0.192/26 and a default route via R. A packet addressed within 10.0.0.0/24 begins at R. Ignore TTL expiration and count every address, including subnet endpoints. For how many destination addresses does the packet loop between R and S rather than reach either connected network?

**Answer format:** Exact integer.

### Q55. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

X and Y are independent uniform random variables on [0,1]. Find E[min(X,Y) | X+Y>1]. Enter the exact decimal value.

**Required precision:** Exact finite decimal.

A. 0.3  
B. 0.8  
C. 0.1  
D. 0.5

### Q56. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two ascending lists each contain three distinct keys, and all six keys are distinct. Only pairwise comparisons between keys are permitted to determine their merged order. Which statements are true?

**Candidates**

**I.** There are 6! possible merged orders consistent with the internal list orders.

**II.** There are 20 possible interleavings consistent with the internal list orders.

**III.** Four binary-outcome comparisons suffice in the worst case for every input.

**IV.** Ordinary two-list merging achieves the optimal worst-case count of five comparisons.

A. II and III  
B. III and IV  
C. I and II  
D. II and IV

### Q57. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two private hosts, 10.0.0.1 and 10.0.0.2, each initiate a TCP connection from local port 5000 to 203.0.113.8 port 443. A NAT gateway uses the single public IPv4 address 198.51.100.6 and assigns public source port 41001 to the connection from 10.0.0.1 and public source port 41002 to the connection from 10.0.0.2. Packets are unfragmented. Which statements are correct for this port-translating NAT?

A. A reply arriving at public port 41002 can be mapped back to 10.0.0.2 port 5000.  
B. The remote server sees both connections as originating from the respective private IPv4 addresses.  
C. Translating the source IPv4 address of an outgoing packet requires updating its IPv4 header checksum.  
D. Translating the source IPv4 address and TCP source port requires updating the TCP checksum because both affect its checksum calculation.

### Q58. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Inputs A,B encode only the three states00,01,10;11 is unreachable. The required output is0 at00 and1 at01 and10. Behaviour at11 is unconstrained. Which expressions correctly implement the specified behaviour on every reachable state?

A. A OR B  
B. A XOR B  
C. A AND B  
D. NOT(A AND B)

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A real function f is twice continuously differentiable on [0,2], satisfies f(0)=f(2)=0, and has f″(x)≥2 for all x in [0,2]. What is the greatest possible value of f(1)?

**Required precision:** Integer.

A. -2  
B. 0  
C. 1  
D. -1

### Q60. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let R be regular and C be context-free over the same alphabet. Which statements hold for every such pair?

A. C∩R is context-free.  
B. C−R is context-free.  
C. R−C is necessarily context-free.  
D. C∪R is context-free.

### Q61. [2 Marks] [NAT]

Construct the usual predictive parsing table for grammar S→AB, A→aA | ε, B→bB | a, with start symbol S and end marker $. Count cells that contain more than one production; count a conflicting cell once regardless of how many productions it contains. How many such cells are there?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

Four memory banks are selected by word address modulo 4. Each request occupies its bank for 3 cycles; a bank accepting a request at cycle t is available again at t+3. The controller issues at most one request per cycle, in the listed order, and stalls if the next request's bank is busy. Initially all banks are idle. For word addresses 0,4,1,5,2,6,3,7, with the first issue at cycle 0, at what cycle does the last request finish?

**Answer format:** Integer cycle number.

### Q63. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A function F(n), for nonnegative integer n, returns immediately for n≤1. Otherwise it calls F(floor(n/2)) and F(ceil(n/2)), then returns. Count every invocation, including base cases. How many invocations are eliminated when computing F(10) if memoization causes each distinct argument to be evaluated only once? A memo-table hit is not counted as an evaluated invocation in the memoized version.

**Required precision:** Integer.

A. 28  
B. 7  
C. 15  
D. 14

### Q64. [2 Marks] [NAT]

Among all monic real quadratics p(x)=x²+ax+b, what is the smallest possible value of max{|p(x)|: −1≤x≤1}?

**Answer format:** Exact finite decimal.

### Q65. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A synchronous counter cycles through exactly five distinct states and then repeats. Which statements are correct?

**Candidates**

**I.** At least three binary storage bits are needed.

**II.** Exactly five flip-flops are necessary for every encoding.

**III.** A three-bit encoding has at least three unused binary patterns.

**IV.** Every unused pattern necessarily recovers to the valid cycle without any next-state design constraint.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

## ANSWER KEY — MOCK TEST 062

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MCQ | 1 | C |
| 3 | MSQ | 1 | A, C, D |
| 4 | NAT | 1 | 8 |
| 5 | NAT | 1 | 0.6667 (accepted range 0.66665–0.66675) |
| 6 | MCQ | 2 | C |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 0.6 |
| 9 | MSQ | 2 | B, C, D |
| 10 | MCQ | 2 | D |
| 11 | NAT | 1 | 3 |
| 12 | NAT | 1 | 6 (exact) |
| 13 | MCQ | 1 | B |
| 14 | NAT | 1 | 9 |
| 15 | NAT | 1 | 0 |
| 16 | MSQ | 1 | B, C, D |
| 17 | MCQ | 1 | B |
| 18 | NAT | 1 | 4 |
| 19 | MCQ | 1 | D |
| 20 | NAT | 1 | 7.75 |
| 21 | NAT | 1 | -0.0833 (range -0.08335–-0.08325) |
| 22 | MCQ | 1 | A |
| 23 | MCQ | 1 | B |
| 24 | MCQ | 1 | C |
| 25 | NAT | 1 | 18 |
| 26 | NAT | 1 | -1 |
| 27 | MCQ | 1 | B |
| 28 | MCQ | 1 | C |
| 29 | MSQ | 1 | A, B, D |
| 30 | MCQ | 1 | B |
| 31 | MCQ | 1 | A |
| 32 | NAT | 1 | 2 |
| 33 | MSQ | 1 | B, C |
| 34 | MCQ | 1 | D |
| 35 | MSQ | 1 | A, C |
| 36 | NAT | 2 | 3 |
| 37 | NAT | 2 | 8 |
| 38 | NAT | 2 | 5 |
| 39 | NAT | 2 | 3 |
| 40 | NAT | 2 | 4 |
| 41 | NAT | 2 | 2 |
| 42 | MCQ | 2 | D |
| 43 | MCQ | 2 | C |
| 44 | NAT | 2 | 50 |
| 45 | NAT | 2 | 1.8333 (range 1.83325–1.83335) |
| 46 | NAT | 2 | 4096 (exact) |
| 47 | NAT | 2 | 11 |
| 48 | MCQ | 2 | C |
| 49 | NAT | 2 | 2 |
| 50 | NAT | 2 | 3 |
| 51 | MCQ | 2 | C |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 35 |
| 54 | NAT | 2 | 64 |
| 55 | MCQ | 2 | D |
| 56 | MCQ | 2 | D |
| 57 | MCQ | 2 | B |
| 58 | MSQ | 2 | C, D |
| 59 | MCQ | 2 | D |
| 60 | MCQ | 2 | C |
| 61 | NAT | 2 | 1 |
| 62 | NAT | 2 | 18 |
| 63 | MCQ | 2 | D |
| 64 | NAT | 2 | 0.5 |
| 65 | MCQ | 2 | C |
