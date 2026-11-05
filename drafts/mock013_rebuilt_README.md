# GATE CS 2027 — Full-Length Mock Test 013

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. MCQs have exactly one correct choice; MSQs have multiple correct choices and no partial credit. Incorrect MCQs lose one-third of the question's marks. Incorrect MSQ/NAT answers and unattempted questions earn zero. GA, Engineering Mathematics and core CS carry 15,13,72 marks. NAT answers are exact unless a rounding instruction is given. Use conventional mathematical notation and the explicit computational assumptions in each question.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Arrange these steps into a logically coherent experimental sequence: P, record the result; Q, formulate a hypothesis; R, design a test of that hypothesis; S, conduct that test.

A. Q–R–S–P
B. R–Q–P–S
C. P–S–R–Q
D. Q–P–R–S

### Q2. [1 Mark] [NAT]

A fair coin is tossed three times. Given that the first two tosses differ, what is the probability that the total number of heads is two?

**Answer format:** Exact finite decimal.

### Q3. [1 Mark] [MCQ]

“The conclusion is provisional and may be revised after further trials.” Which word is closest in meaning to provisional here?

A. Irrevocable
B. Tentative
C. Unrelated
D. Unanimous

### Q4. [1 Mark] [NAT]

Find the positive real x satisfying 3^(x+1)=27×9^(x−2).

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

A device failed on three occasions when its battery level was below 5%, but no observations at other battery levels were collected. Which proposed next step would best test whether low battery level predicts failure?

A. Declare that every failure has already been explained.
B. Collect comparable observations across both low and higher battery levels.
C. Exclude every future observation above 5%.
D. Infer that a full battery guarantees success without testing it.

### Q6. [2 Marks] [NAT]

A 4×4 grid of unit squares is coloured like a chessboard, with adjacent squares having opposite colours. How many axis-aligned 2×2 subgrids contain exactly two squares of each colour?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A sequence satisfies a1=2 and a(n+1)=2a(n)+1 for n≥1. What is the sum of its first four terms?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

A cylindrical tank has radius 3 m and initially contains water to height 4 m. A solid sphere of radius 1.5 m is lowered completely below the water without touching the tank walls, and no water spills. By how many metres does the water level rise? Treat π symbolically.

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MCQ]

Choose the sentence that preserves both the conditional meaning and correct grammar: the machine should be restarted only after the valve has been closed.

A. Restart the machine before the valve has been closed.
B. Do not restart the machine until the valve has been closed.
C. Closing the valve is unnecessary before restarting the machine.
D. The machine must restart whenever the valve closes, without any other condition.

### Q10. [2 Marks] [NAT]

An alloy containing 40% copper is mixed with one containing 70% copper to produce 20 kg containing 52% copper. How many kilograms of the 70% alloy are required?

**Answer format:** Integer kilograms.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

In the multiplicative group of units modulo 10, what is the order of the element 3?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

An undirected multigraph has three vertices, two parallel edges between vertices 1 and 2, one edge between 2 and 3, and one self-loop at vertex 3. In the standard degree convention a self-loop contributes two. What is the sum of vertex degrees?

**Answer format:** Integer.

### Q13. [1 Mark] [MCQ]

A four-line direct-mapped cache starts empty and uses block number modulo four as its line index. Which reference sequence has exactly one hit?

A. 0,4,0,4
B. 0,1,0,4
C. 0,1,2,3
D. 0,0,0,0

### Q14. [1 Mark] [MSQ]

A CPU can mask ordinary maskable interrupts while executing a short critical section. Which statements are correct?

A. Masking prevents delivery of those maskable interrupts during the masked interval.
B. Masking interrupts on one CPU automatically stops every other CPU from accessing shared memory.
C. Excessively long masked intervals can increase interrupt response latency.
D. Masking converts every ordinary load/store into a multi-CPU atomic read-modify-write operation.

### Q15. [1 Mark] [NAT]

A signed six-bit two's-complement fixed-point value has two fractional bits. What is the greatest positive real number it can represent?

**Answer format:** Exact finite decimal.

### Q16. [1 Mark] [MCQ]

In `t=a+b; c=d+e; u=a+b;`, variables a,b,c,d,e,t,u are distinct nonaliased scalars and arithmetic is exact. Which replacement is valid?

A. Replace the final a+b by t.
B. Replace the final a+b by c for all inputs.
C. Replace d+e by t for all inputs.
D. Delete the first assignment and leave u=t with no definition of t.

### Q17. [1 Mark] [NAT]

Under set semantics, R(A,B)={(1,2),(1,3),(2,3)}. How many tuples does π_A(R)×π_B(R) contain?

**Answer format:** Integer.

### Q18. [1 Mark] [MCQ]

In C, `int a[3]={5,6,7}; int *p=a+3;` is executed. Which subsequent operation is valid by the one-past-the-end pointer rule?

A. Evaluate *p.
B. Evaluate *(p-1).
C. Form p+1 and dereference it.
D. Write p[0]=8.

### Q19. [1 Mark] [MSQ]

A PDA's stack alphabet has only one ordinary symbol X plus a protected bottom marker. Which capabilities can it still support?

A. Counting an unbounded run of a symbols by pushing one X per a.
B. Matching a later run of b symbols to that count by popping one X per b.
C. Storing every arbitrary binary prefix exactly using only one X per input symbol and no other encoding or memory.
D. Having infinitely many possible stack heights despite a finite stack alphabet.

### Q20. [1 Mark] [NAT]

A connected undirected graph has four vertices and every edge has weight 7. How much does any minimum spanning tree weigh?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A bipartite graph has left vertices a,b,c,d and right vertices 1,2,3,4. Each of a,b,c is adjacent exactly to 1 and 2; d is adjacent exactly to 3 and 4. What is the maximum matching size?

**Answer format:** Integer.

### Q22. [1 Mark] [MCQ]

Relation R contains finitely many integers, while the domain of possible integers is infinite. Consider the tuple-calculus query {x | NOT R(x)}, with no restriction to the active domain. Which statement is correct?

A. It is not range-restricted and its result can be infinite even though R is finite.
B. Its result must be a subset of R.
C. Its result is always empty.
D. Negation makes every tuple-calculus query safe automatically.

### Q23. [1 Mark] [MCQ]

Two processes share a memory region but use no synchronization. Why does shared-memory IPC alone not guarantee a correct producer–consumer protocol?

A. Shared memory cannot store more than one byte.
B. Visibility of common storage does not by itself ensure correct ordering or mutual exclusion.
C. The two processes necessarily have identical register values.
D. Sharing storage automatically serializes all accesses.

### Q24. [1 Mark] [NAT]

How many ordered triples of positive integers (x,y,z) satisfy x+y+z=8 with each entry at most 4?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

A sequence satisfies T(0)=0 and T(n)=T(n−1)+2n−1 for n≥1. Find T(20).

**Answer format:** Integer.

### Q26. [1 Mark] [MCQ]

A lexical analyzer distinguishes an identifier token from a symbol-table entry. Which statement is correct?

A. Every occurrence of the same identifier spelling must create a permanently distinct name entry regardless of scope or implementation.
B. Token recognition and name binding are different tasks; returning an identifier token does not alone determine which declaration it denotes.
C. Recognizing a token proves that the entire program is type-correct.
D. Whitespace must always be emitted as an identifier token.

### Q27. [1 Mark] [NAT]

An IPv4 fragment has a 20-byte header, total length 420 bytes, and fragment-offset field 100. At what payload byte offset, measured from the start of the original datagram's payload, does this fragment end? Give the exclusive end offset.

**Answer format:** Integer.

### Q28. [1 Mark] [MSQ]

Let L be regular and F finite over the same alphabet. Which languages are necessarily regular?

A. L∪F
B. L−F
C. F−L
D. Every language containing L as a subset.

### Q29. [1 Mark] [NAT]

A routing table contains destination prefixes 0.0.0.0/0, 172.16.0.0/16, 172.16.32.0/20 and 172.16.40.0/24, each with a different next hop. For destination 172.16.41.7, what prefix length is selected by longest-prefix matching?

**Answer format:** Integer prefix length.

### Q30. [1 Mark] [NAT]

Table T(x) contains 2,2,NULL,5. What is the result of `SELECT COUNT(DISTINCT x) FROM T`?

**Answer format:** Integer.

### Q31. [1 Mark] [MCQ]

A directed graph has a negative-weight cycle that is unreachable from source s. Which statement about source-reachable shortest paths follows?

A. Every source-reachable distance is necessarily undefined.
B. The unreachable cycle alone does not destroy shortest-path distances from s.
C. The cycle must be removed before even identifying vertices reachable from s.
D. All edge weights reachable from s must therefore be nonnegative.

### Q32. [1 Mark] [NAT]

A normalized binary floating-point format has five significant bits including the leading 1. What is the spacing between adjacent representable numbers in [8,16), assuming the exponent range includes this interval?

**Answer format:** Exact finite decimal.

### Q33. [1 Mark] [MSQ]

Which formulas are logically equivalent to ¬∀x(P(x)→Q(x))?

A. ∃x(P(x)∧¬Q(x))
B. ∀x(P(x)∧¬Q(x))
C. ¬∀x(¬P(x)∨Q(x))
D. ∃x(¬P(x)∧Q(x))

### Q34. [1 Mark] [MCQ]

A counting semaphore initialized to 3 controls access to identical resources. Each successful wait decrements it and each release signals it once. With no erroneous extra signals, what does initialization to 3 represent?

A. At most three concurrent resource holders can be admitted.
B. Exactly three processes must execute wait simultaneously.
C. Every process must wait three times before entering.
D. No process can ever block.

### Q35. [1 Mark] [NAT]

Binary search on a sorted array of length 15 chooses the lower midpoint of the current inclusive interval and compares the target once to that entry. What is the maximum number of such comparisons for a successful search?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A single resource type has R identical reusable instances. Three processes each need at most three instances in total, may request one at a time, never release before completion, and finish once their total demand is met. What is the smallest R that guarantees absence of resource deadlock for every allocation state consistent with these maximum demands? Scheduling fairness is not being asked about.

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

A Boolean function F(x,y,z) satisfies F(x,y,z)=F(x,y,z′) for every assignment. Which statements must hold?

A. z is inessential: the two cofactors at z=0 and z=1 are identical.
B. F can be implemented by a function of x,y alone.
C. F must be constant.
D. Every sum-of-products expression for F must contain a literal z or z′.

### Q38. [2 Marks] [NAT]

Let A be the 3×3 upper-triangular matrix with rows (1,1,0),(0,1,1),(0,0,1). Find the entry in row 1, column 3 of A⁵+A⁻².

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

A processor can issue one instruction per cycle. A loop has 100 instructions, including ten branches. Exactly three of the branches mispredict, each inserting four cycles with no issue. Each of eight cache misses adds five stall cycles, but two of those misses occur entirely during branch-stall intervals and add no extra cycles. All other penalties are disjoint. Ignoring pipeline fill/drain, how many cycles does the loop take?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

An instruction uses base-plus-scaled-index addressing: address=base+4×index+signed displacement. The base register holds 1000, the index holds 7, and the eight-bit displacement field is 11111000₂. What byte address is computed?

**Answer format:** Integer.

### Q41. [2 Marks] [MSQ]

An n-bit ALU, n≥2, computes A−B as A+(NOT B)+1. Which statements hold when carry-out is retained separately from the n-bit result?

A. Carry-out 1 indicates no borrow in unsigned subtraction.
B. The retained result represents (A−B) modulo 2ⁿ.
C. Unsigned borrow and signed overflow are always the same event.
D. Signed subtraction overflow can occur when A and B have opposite signs and the result's sign differs from A's.

### Q42. [2 Marks] [NAT]

Nonpreemptive shortest-job-first scheduling handles jobs J1,J2,J3 with arrival times 0,1,2 and CPU bursts 5,2,1. Context switching costs zero. What is their mean turnaround time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q43. [2 Marks] [NAT]

A recursion on an input interval of length n returns immediately for n≤1. Otherwise it recursively processes the first floor(n/2) entries and then the remaining entries. For n=10, how many calls split their input into two parts of unequal lengths? Count separate calls, even when their input lengths are equal to one another.

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A chained hash table has three buckets containing respectively 1,2,3 distinct keys. All six keys are equally likely targets of a successful search, and each chain is searched from its head. What is the expected number of key comparisons? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q45. [2 Marks] [MCQ]

Two internal TCP clients connect to the same external server through a translator sharing one public address. The translator assigns different public source ports. Which information is essential for routing a returning server segment to the correct internal connection?

A. Only the external server's destination port, ignoring the translated port.
B. A translation mapping that includes the public-side connection endpoint information and its corresponding internal endpoint.
C. Only the Ethernet broadcast address.
D. Only the length of the TCP payload.

### Q46. [2 Marks] [MCQ]

A proof for L={aⁿbⁿcⁿ:n≥0} chooses aᵖbᵖcᵖ in the context-free pumping lemma. Why does |vxy|≤p help show every valid decomposition fails for some pumping exponent?

A. It forces v and y both to be empty.
B. It prevents the pumpable region from spanning all three blocks, so pumping changes some counts without changing all three equally, or disrupts the block order.
C. It forces the entire word to have length at most p.
D. It proves the language finite.

### Q47. [2 Marks] [MSQ]

Relation R(A,B) has primary key A and a CHECK constraint `B > 0`, with B allowed to be NULL. Under ordinary SQL CHECK semantics, a row is rejected by CHECK only when the condition is FALSE. Which insertions can satisfy these constraints if A is a fresh non-NULL key each time?

A. B=3
B. B=NULL
C. B=0
D. B=−2

### Q48. [2 Marks] [NAT]

A C array `int a[2][3]={{1,2,3},{4,5,6}};` is followed by `int (*p)[3]=a;`. Evaluate `*(*(p+1)+2) + (*p)[1]`.

**Answer format:** Integer.

### Q49. [2 Marks] [MSQ]

Let f(0)=0 and f(x)=x²sin(1/x) for x≠0. Which statements are true?

A. f is continuous at zero.
B. f is differentiable at zero with f′(0)=0.
C. f′ is continuous at zero.
D. f′ is bounded on some open interval containing zero.

### Q50. [2 Marks] [NAT]

In an idealized TCP congestion-avoidance model, cwnd starts at 4 MSS. Each complete loss-free RTT acknowledges the entire current window, then cwnd increases by exactly 1 MSS. The receiver window never limits transmission. How many MSS are transmitted over the first four RTTs? Count each round's transmitted data before its increase.

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

Three objects are sampled uniformly without replacement from five objects, two of which are red. Let X be the number of red objects selected. Find Var(X).

**Answer format:** Exact finite decimal.

### Q52. [2 Marks] [MSQ]

For an arbitrary Turing machine M, define L_M={x : M accepts x within at most |x| transition steps}. Which statements are correct?

A. L_M is decidable for every M.
B. Deciding L_M requires deciding whether M eventually halts on x.
C. A decider can simulate exactly the bounded number of allowed steps and reject if no acceptance has occurred.
D. L_M must be empty whenever M fails to halt on some other input.

### Q53. [2 Marks] [NAT]

How many functions f:{1,2,3,4,5}→{1,2,3,4,5} satisfy f(f(x))=x for every x and have exactly one fixed point?

**Answer format:** Integer.

### Q54. [2 Marks] [MCQ]

R(A,B,C) has dependencies AB→C and C→B. Which statement is correct?

A. Its only candidate key is AB and it is in BCNF.
B. Its candidate keys are AB and AC; it is in 3NF but not BCNF.
C. Every attribute is a candidate key by itself.
D. It fails 3NF because B is not prime.

### Q55. [2 Marks] [NAT]

A disk's cylinders are 0 through 199. The head is at 80 and is moving upward. Pending requests are 20,90,150. Under SCAN, the head continues to cylinder 199 before reversing, even after serving 150. Stop measuring when the final pending request is served. What total distance is travelled?

**Answer format:** Integer cylinders.

### Q56. [2 Marks] [MSQ]

Grammar E→E+T | T, T→T*F | F, F→id has its usual parse-tree interpretation. Which statements are true?

A. Multiplication binds more tightly than addition.
B. A chain of additions is left-associated.
C. The grammar is immediately suitable for a naive recursive-descent parser without eliminating left recursion.
D. The word id+id*id has two parse trees under this grammar.

### Q57. [2 Marks] [MCQ]

A TCP receiver calls a blocking `recv` requesting up to 100 bytes. The peer has sent 40 bytes, which are available, but has not closed the connection. Assuming the API allows a positive short return, which application behaviour is correct?

A. Treat a return of 40 as necessarily indicating end-of-file.
B. Accumulate received bytes according to the application's framing rule rather than assuming each receive corresponds to one send or fills the requested count.
C. Assume every return of fewer than 100 bytes is a network corruption.
D. Assume TCP inserts an application-message boundary after each send.

### Q58. [2 Marks] [NAT]

A three-input Boolean function F(a,b,c) is zero exactly at minterms 0,1,2,5 and one elsewhere. The minterm index uses a as the most significant bit. There are no don't-cares. What is the minimum number of sum clauses in a product-of-sums expression for F? Each clause may contain ordinary complemented or uncomplemented literals.

**Answer format:** Integer.

### Q59. [2 Marks] [MCQ]

A dynamic array doubles its capacity when full. Initially it is empty with capacity one. Appending a value costs one unit, and a resizing append additionally copies every existing value at one unit per copy. For n=2^k appends, k≥1, what is the exact total cost?

A. n+k
B. 2n−1
C. n log₂n
D. 3n

### Q60. [2 Marks] [NAT]

A compiler computes array widths using attributes: width(int)=4 and width(array(n,T))=n×width(T). A record lays out fields without padding. It contains an array(3,array(2,int)) followed by an int. What is its computed width in bytes?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

A complete DFA over {0,1} accepts exactly the strings that end in 01. What is the minimum number of states in such a DFA?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

An unspanned fixed-record file uses 1000-byte blocks. Records are 120 bytes, and each block reserves a 40-byte header. How many blocks are needed for 81 records, with no compression and no record crossing a block boundary?

**Answer format:** Integer.

### Q63. [2 Marks] [MCQ]

A recursive function has a local scalar variable x whose address is never returned or retained beyond its activation. Different recursive calls require separate x values until they return. Which allocation strategy directly supports this requirement?

A. A single global x shared by every activation with no saving.
B. One x slot in each activation record on the runtime stack.
C. No storage because recursion forbids locals.
D. One immutable constant substituted for x in every call regardless of assignments.

### Q64. [2 Marks] [MSQ]

In tabular Boolean minimization, a dash represents an eliminated variable. A direct combination is allowed when two patterns have identical dash positions and differ in exactly one nondash bit. Which pairs can be directly combined in a single step?

A. 01-10 and 01-11
B. 01-10 and 011-0
C. 0--10 and 1--11
D. 0--10 and 1--10

### Q65. [2 Marks] [MSQ]

A weighted undirected connected graph has some negative edge weights. Which statements about Kruskal's MST algorithm are true?

A. Sorting edges by nondecreasing weight and rejecting cycle-forming edges remains correct.
B. Every negative edge must be included, even if the negative edges form a cycle.
C. The cut/exchange justification does not require all weights to be nonnegative.
D. Replacing all weights w by w+c for one constant c can change which spanning trees minimize total weight.

## ANSWER KEY — MOCK TEST 013

NAT answers are exact except where rounded ranges are given.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 0.5 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 2 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 9 |
| 7 | NAT | 2 | 41 |
| 8 | NAT | 2 | 0.5 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 8 |
| 11 | NAT | 1 | 4 |
| 12 | NAT | 1 | 8 |
| 13 | MCQ | 1 | B |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 7.75 |
| 16 | MCQ | 1 | A |
| 17 | NAT | 1 | 4 |
| 18 | MCQ | 1 | B |
| 19 | MSQ | 1 | A, B, D |
| 20 | NAT | 1 | 21 |
| 21 | NAT | 1 | 3 |
| 22 | MCQ | 1 | A |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 12 |
| 25 | NAT | 1 | 400 |
| 26 | MCQ | 1 | B |
| 27 | NAT | 1 | 1200 |
| 28 | MSQ | 1 | A, B, C |
| 29 | NAT | 1 | 20 |
| 30 | NAT | 1 | 2 |
| 31 | MCQ | 1 | B |
| 32 | NAT | 1 | 0.5 |
| 33 | MSQ | 1 | A, C |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 4 |
| 36 | NAT | 2 | 7 |
| 37 | MSQ | 2 | A, B |
| 38 | NAT | 2 | 13 |
| 39 | NAT | 2 | 142 |
| 40 | NAT | 2 | 1020 |
| 41 | MSQ | 2 | A, B, D |
| 42 | NAT | 2 | 5.3333 (range 5.33325–5.33335) |
| 43 | NAT | 2 | 4 |
| 44 | NAT | 2 | 1.6667 (range 1.66665–1.66675) |
| 45 | MCQ | 2 | B |
| 46 | MCQ | 2 | B |
| 47 | MSQ | 2 | A, B |
| 48 | NAT | 2 | 8 |
| 49 | MSQ | 2 | A, B, D |
| 50 | NAT | 2 | 22 |
| 51 | NAT | 2 | 0.36 |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 15 |
| 54 | MCQ | 2 | B |
| 55 | NAT | 2 | 298 |
| 56 | MSQ | 2 | A, B |
| 57 | MCQ | 2 | B |
| 58 | NAT | 2 | 2 |
| 59 | MCQ | 2 | B |
| 60 | NAT | 2 | 28 |
| 61 | NAT | 2 | 3 |
| 62 | NAT | 2 | 11 |
| 63 | MCQ | 2 | B |
| 64 | MSQ | 2 | A, D |
| 65 | MSQ | 2 | A, C |

