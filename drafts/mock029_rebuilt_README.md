# GATE CS 2027 — Full-Length Mock Test 029

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

The examination lasts180 minutes. Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes15 marks, Engineering Mathematics13, and core Computer Science72.

MCQs have exactly one correct option; MSQs have multiple correct options and award marks only for selecting all and only those options. Incorrect one-mark and two-mark MCQs incur penalties of1/3 and2/3 mark respectively. MSQ and NAT questions have no negative marking. Unattempted questions receive zero. No partial credit applies. Use the indicated NAT precision; exact decimals and integers require exact answers. The answer key follows Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

A report describes four events: obtaining permission(P), collecting samples(C), calibrating the instrument(K), and measuring the samples(M). Permission was obtained before collection; both collection and calibration occurred before measurement. No other ordering information is given, and no events were simultaneous. How many chronological orders are consistent with the report?

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

Cards labelled1,2,3 are placed in uniformly random order. Given that the first card's number is smaller than the second card's number, what is the probability that the second card's number is smaller than the third card's number?

**Answer format:** Decimal rounded to four places.

### Q3. [1 Mark] [MCQ]

“The grant was contingent on the laboratory obtaining approval.” Which phrase best replaces “contingent on” without changing the meaning?

A. unrelated to
B. dependent on
C. completed before
D. guaranteed despite

### Q4. [1 Mark] [NAT]

How many digits are in the ordinary binary representation, without leading zeroes, of the positive integer8^5/4^2?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

After observing3,5,7, someone conjectures that every odd integer greater than1 is prime. What is the smallest integer satisfying the stated domain that disproves the conjecture?

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

Unit cubes are stacked in four columns on a2×2 base. A column may have height0,1,or2. The maximum heights seen in the two rows are respectively2 and1; the maximum heights seen in the two columns are respectively2 and1. Rows and columns have fixed labels. How many different height arrays satisfy these four maxima?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A sequence starts a1=0. For each positive integer n, define a(n+1)=a(n)+n when n is odd and a(n+1)=a(n)−n when n is even. What is a101?

**Answer format:** Integer, including a minus sign if needed.

### Q8. [2 Marks] [NAT]

Two filled, axis-aligned squares have coordinate ranges[0,4]×[0,4] and[1,5]×[2,6]. What is the perimeter of their union, counting only its outer boundary?

**Answer format:** Integer length units.

### Q9. [2 Marks] [MCQ]

An editor wants to say that the archivist digitized the files and then found them easier to search. Which revision correctly expresses that meaning without a dangling modifier?

A. Having digitized the files, searching was easier for the archivist.
B. Having digitized the files, the search facility became faster.
C. Having digitized the files, the archivist found them easier to search.
D. Having digitized the files, the documents were easier for the archivist to search.

### Q10. [2 Marks] [NAT]

A100-kg salt solution contains10% salt by mass. Exactly20kg of water evaporates, with no salt lost. Then10kg of the remaining uniform solution is removed and replaced by10kg of pure water. What is the final salt percentage by mass?

**Answer format:** Exact percentage without the percent sign.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A directed simple graph has edges a→b,b→a,b→c,c→d,d→c,a→d. If M is its zero-one adjacency matrix, what is trace(M²), using ordinary integer matrix multiplication?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

A five-stage IF–ID–EX–MEM–WB pipeline executes a load followed immediately by a store of the loaded register. Their address calculations are independent. Load data becomes available at the end of its MEM stage; store data is needed only at the start of its MEM stage. Which statements are correct?

A. A forwarding path from the completed load's data to the next cycle's store-data input can avoid a stall.
B. The store necessarily needs the loaded value for its EX address calculation.
C. Without forwarding, waiting for register write-back may be necessary.
D. Every load-followed-by-store pair must stall regardless of available forwarding paths.

### Q13. [1 Mark] [NAT]

In the additive group of integers modulo12, how many distinct elements can be obtained as 4m+6n modulo12 with nonnegative integers m,n?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

A deterministic finite automaton has missing transitions, which cause immediate rejection. To recognize the complement over the same alphabet, which statements are correct?

A. Swapping accepting and rejecting states alone always suffices.
B. Completing the automaton with a rejecting sink before swapping accepting states works.
C. A word rejected by taking a missing transition must be accepted by a correct complement automaton.
D. Adding a sink after swapping states and leaving that sink rejecting always works.

### Q15. [1 Mark] [NAT]

Remove a perfect matching from the complete bipartite graph K3,3. How many spanning trees does the remaining graph have?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

Six labelled positions lie on a circle. How many assignments of exactly two1 bits and four0 bits have no adjacent1 bits, including across the last-to-first boundary? Rotations remain distinct assignments.

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

In a basic block, t=a+b is computed, then a store through pointer p occurs, then u=a+b is computed. The scalar values a,b reside in memory and p may alias them. Arithmetic is exact and has no side effects. Which statements are correct?

A. Reusing t for u without alias information can be unsound.
B. Proving the store cannot change a or b permits reuse in this block.
C. Identical expression text alone guarantees equal values across the store.
D. Recomputing a+b after the store preserves the required new operand values.

### Q18. [1 Mark] [NAT]

A synchronous three-bit state register is interpreted as an unsigned integer q. At every clock edge, q becomes0 if q≥5, and otherwise becomes q+1. Starting with q=7 before the first edge, what is q after14 edges?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

In a directed weighted graph, a negative-weight cycle is reachable from s but no vertex on that cycle can reach t. A path from s to t exists. Which statements are correct?

A. A finite shortest s-to-t distance can still exist.
B. Every reachable vertex necessarily has distance minus infinity.
C. Repeating that cycle cannot produce arbitrarily cheap s-to-t walks under the stated reachability condition.
D. The mere existence of that cycle implies no s-to-t path exists.

### Q20. [1 Mark] [NAT]

SQL table A(k) contains1,2,NULL; B(k) contains2,NULL. Compare the counts returned by these predicates on rows of A: NOT EXISTS(SELECT 1 FROM B WHERE B.k=A.k), and A.k NOT IN(SELECT k FROM B). Using ordinary SQL three-valued logic, what is the first count minus the second?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A grammar has start symbol S and productions S→AB, A→a, B→bB, C→c. A nonterminal is productive if it derives some finite terminal string. How many nonterminals are both reachable from S and productive?

**Answer format:** Integer.
### Q22. [1 Mark] [MSQ]

A condition variable wait atomically releases its associated mutex and blocks, and reacquires the mutex before returning. Wakeups do not guarantee the application's predicate is true. Which statements are correct?

A. The predicate should be rechecked after returning from wait.
B. A single if test before wait is sufficient for every execution.
C. Another thread can change the predicate before the awakened thread reacquires the mutex.
D. Returning from wait means the mutex remains released under this specification.

### Q23. [1 Mark] [MCQ]

An HTTP cache has a stale response with an entity tag. It validates the response using If-None-Match and receives304 Not Modified. Which action matches the response's meaning?

A. Replace the representation body by the digits304.
B. Treat the resource as permanently deleted.
C. Reuse the cached representation body subject to the updated cache metadata.
D. Assume the server transmitted a complete replacement body.

### Q24. [1 Mark] [NAT]

In C, int a[2][3]={{1,2,3},{4,5,6}}; int (*p)[3]=a; is followed by p++;. What is (*p)[1]+p[-1][2]? All accesses are valid.

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

A byte-addressed machine fetches a four-byte instruction beginning at address100. Its PC-relative branch displacement is a signed count of four-byte words measured from the address immediately following the instruction. If the displacement is−3, what is the branch target byte address?

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

A network-layer packet is carried through two links with different link-layer protocols. No tunnelling or address translation is used. Which statements are correct?

A. The outgoing link can use a different frame format from the incoming link.
B. A router must preserve the incoming link-layer checksum unchanged in the outgoing frame.
C. Link-specific headers may be removed and replaced while forwarding the packet.
D. Changing link-layer protocol necessarily changes the application's message content.

### Q27. [1 Mark] [NAT]

A signed eight-bit fixed-point code represents its two's-complement integer divided by16. The exactly represented numbers3.5 and−1.75 are added without overflow. What is the unsigned decimal interpretation of the eight stored result bits?

**Answer format:** Integer.

### Q28. [1 Mark] [MSQ]

An n-bit adder has carry-in0, carry into the sign bit c and final carry-out d. Which statements are correct for two's-complement addition?

A. Signed overflow is indicated by c XOR d.
B. Final carry-out alone always indicates signed overflow.
C. Adding operands of opposite signs cannot cause signed overflow.
D. A result with sign bit1 always indicates overflow.

### Q29. [1 Mark] [NAT]

Let a0=1,a1=1 and a(n)=a(n−1)+2a(n−2) for n≥2. What is the coefficient of x5 in (1−x−2x²) times the formal power series sum from n=0 to infinity of a(n)x^n?

**Answer format:** Integer.

### Q30. [1 Mark] [MSQ]

A foreign key Child.parent_id references Parent.id. It uses ON DELETE SET NULL, and Child.parent_id is also declared NOT NULL. A parent with a referencing child is deleted. Assume constraints are enforced immediately and no other action modifies the child. Which statements are correct?

A. The referential action would require setting the child's foreign key to NULL.
B. The deletion can violate the child's NOT NULL constraint and be rejected.
C. SET NULL silently overrides every NOT NULL constraint.
D. The child row must necessarily be deleted instead.

### Q31. [1 Mark] [NAT]

A binary search finds the first array position whose value is at least7 in the sorted array[2,7,7,7,9]. Positions are zero-based and the returned position may be the array length if no value qualifies. What is the returned position?

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

Two identical resource instances exist. P holds one and Q holds the other; each waits for one additional instance and neither releases before obtaining it. There are no other processes. Which statements are correct?

A. Both processes are blocked indefinitely under these rules.
B. Having multiple instances makes deadlock impossible.
C. Releasing one held instance could permit one process to finish, if that change were allowed.
D. Each process already holds enough instances to satisfy its outstanding request without any release.

### Q33. [1 Mark] [NAT]

A lexer returns the longest available operator token from {>,>=,>> ,>>=}, ignoring the displayed spacing in this set. With input >>>= and no whitespace, how many operator tokens does it return?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

On a nonempty domain, P and Q are unary predicates. Which implications are valid for every interpretation?

A. (∀x P(x)) OR (∀x Q(x)) implies ∀x(P(x) OR Q(x)).
B. ∀x(P(x) OR Q(x)) implies (∀x P(x)) OR (∀x Q(x)).
C. ∃x(P(x) AND Q(x)) implies (∃x P(x)) AND (∃x Q(x)).
D. (∃x P(x)) AND (∃x Q(x)) implies ∃x(P(x) AND Q(x)).

### Q35. [1 Mark] [NAT]

Grammar E→E+T | T and T→id is parsed bottom-up. Ignoring the end marker, how many reductions occur in a complete parse of id+id+id?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

An expression node has synthesized attribute p, the parity of its integer value. Leaves provide their value modulo2. Addition combines child parities using XOR; multiplication combines them using AND. For expression (u+v)*(v+w)+u*w, how many of the eight assignments of parities to u,v,w make the root parity1?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

A PDA for even-length palindromes over{a,b} pushes symbols in phase1, nondeterministically guesses the midpoint using an epsilon move, then matches and pops in phase2. Acceptance requires exhausting input and returning to the bottom marker. Which statements are correct?

A. A successful branch guesses a midpoint after exactly half the input.
B. Every midpoint guess must succeed for a palindrome to be accepted.
C. Guessing at the beginning accepts every nonempty input.
D. The empty word can be accepted by guessing immediately.

### Q38. [2 Marks] [NAT]

A binary floating-point system has three significant bits, including the leading1, and sufficient exponent range. It rounds each operation to nearest, with ties to an even significand low bit. Compute the absolute difference between fl(fl(8+1)−8) and fl(8+fl(1−8)). Here fl means rounding one operation in that format.

**Answer format:** Exact number.

### Q39. [2 Marks] [NAT]

Round-robin scheduling has quantum2, zero overhead, and a ready queue initially[A,B,C]. All arrive at0, with CPU bursts A=5,B=3,C=1. A process with remaining work joins the queue tail after its quantum. What is the mean turnaround time?

**Answer format:** Decimal rounded to four places.

### Q40. [2 Marks] [MSQ]

A real matrix A has three columns. Its reduced row-echelon form has pivots in columns1 and3. The system Ax=b is consistent. Which statements are correct?

A. There is exactly one free variable.
B. Every consistent right-hand side yields a unique solution.
C. The solution set is an affine line in R³.
D. The nullspace has dimension2.

### Q41. [2 Marks] [NAT]

For x≠0, f(x)=(exp(x)−1−x)/x². Set f(0) to the value making f continuous at0. What is f'(0)?

**Answer format:** Decimal rounded to four places.

### Q42. [2 Marks] [NAT]

The function below uses a single shared counter c, initially0. Evaluation order is exactly as written.

```text
F(n):
    if n == 0: return c
    c = c + 1
    x = F(n-1)
    c = c + 1
    return x + c
```

What does F(3) return?

**Answer format:** Integer.

### Q43. [2 Marks] [MSQ]

For Boolean inputs x,y,z, consider F=(x OR y) AND ((NOT x) OR z). Which statements are correct?

A. F=(x AND z) OR ((NOT x) AND y).
B. The product term yz can be added to the expression in A without changing F.
C. F is always equal to y AND z.
D. When y=z, F equals that common value.

### Q44. [2 Marks] [NAT]

A hash table has11 slots and uses double hashing h1(k)=k mod11 and h2(k)=1+(k mod10). To insert a key, probe(h1+i·h2) mod11 for i=0,1,... . Initially slots0,1,3,5 are occupied and all others empty. How many probes are made to insert key22, counting the successful probe?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A microprogram has40 microinstructions. Each has12 independent control bits and a next-address field able to address every microinstruction. A redesigned store has the same40 entries but adds a two-bit branch-condition selector to every word. What is the increase in total control-store capacity, in bits?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

Let L={ww : w in {a,b}*}. Which statements are correct?

A. Every word in L has even length.
B. Every even-length palindrome belongs to L.
C. L contains words that are not palindromes.
D. L is closed under reversal.

### Q47. [2 Marks] [MSQ]

Someone argues that a language is regular because one selected word has one decomposition that pumps for every exponent. Which statements are correct?

A. This establishes the pumping lemma's required property for every sufficiently long word.
B. The argument omits a uniform pumping length and quantification over words.
C. Even satisfying the regular pumping lemma's condition would not by itself prove regularity.
D. Showing one decomposition fails is sufficient to establish nonregularity.

### Q48. [2 Marks] [NAT]

A disk head starts at cylinder40. Pending requests are10,45,70, and no new requests arrive. Under shortest-seek-time-first, choose the nearest pending request, breaking ties toward the lower cylinder. What total distance is travelled to serve all requests?

**Answer format:** Integer cylinders.

### Q49. [2 Marks] [NAT]

A process has virtual pages0–7. A page table maps pages0,1,4,5 to physical frames3,7,3,9; other pages are absent. The page size is1024 bytes. How many distinct physical byte addresses are represented by all valid virtual addresses in those four mapped pages?

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

A closure captures a local variable by reference. The closure can be invoked after its defining procedure returns. Which statements are correct?

A. The captured storage must remain valid for those later invocations.
B. Keeping only a pointer into an already-reused stack frame is always sufficient.
C. Heap allocation or another lifetime-preserving mechanism can support the capture.
D. Lexical scope alone guarantees that arbitrary stack storage remains allocated forever.

### Q51. [2 Marks] [NAT]

An array [a,b,c,d,e,f] is permuted in place by the index mapping i→(2i+1) modulo7, with indices restricted to0 through5. This mapping permutes those six indices. How many disjoint cycles does it contain?

**Answer format:** Integer.

### Q52. [2 Marks] [MCQ]

For n a positive perfect square, determine the tight asymptotic number of loop iterations as n grows. Arithmetic and floor-square-root evaluation each take constant time.

```text
i = 1
while i < n:
    i = i + floor(sqrt(i))
```

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(sqrt(n))
### Q53. [2 Marks] [NAT]

A packet of1200 bits travels through two store-and-forward links, with rates600 and1200 bits/s respectively. Each link has propagation delay0.1 seconds. There is no queueing or processing delay. What is the time from starting transmission on link1 until the final bit arrives at the destination?

**Answer format:** Exact seconds.

### Q54. [2 Marks] [NAT]

A three-address code generator translates x=(a+b)*(a+b)+(a+b) and performs local common-subexpression elimination. All operands are unchanged mathematical integers. Each binary operation requires one assignment, and assigning the final expression to x needs no separate copy. What is the minimum number of binary-operation assignments in the resulting code?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which statements are correct?

A. AC and BC are candidate keys.
B. A alone is a candidate key.
C. R is in3NF.
D. R is in BCNF.

### Q56. [2 Marks] [NAT]

A sorted file occupies100 pages, each with100 records. A sparse index has one entry per data page, with20 entries fitting per index page. The index is searched in memory after all its pages are fetched once. A query then fetches one qualifying data page. With an empty buffer and no other reads, how many page reads occur?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

A B+ tree has a root with two internal children. Each of those children has exactly three leaf children. Every leaf contains exactly four data entries. Internal separator copies are not data entries. How many data entries does the tree contain?

**Answer format:** Integer.

### Q58. [2 Marks] [MSQ]

Over GF(2), a CRC generator is g(x)=x³+x+1. The transmitted codeword suffers error polynomial e(x)=x^k g(x), for some k≥0 that fits within the transmitted frame. Which statements are correct?

A. The CRC remainder of the error polynomial is zero.
B. This nonzero error can escape detection.
C. Multiplication by x^k guarantees detection of every nonzero polynomial.
D. The error polynomial must be a single-bit error.

### Q59. [2 Marks] [NAT]

A byte-addressed device has256 byte locations. Its chip-select decoder matches address bits15–12 to1010, while address bits11–8 are ignored; bits7–0 address the device. Within the16-bit address space, how many distinct CPU byte addresses alias device offset0x35?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

Independent Bernoulli random variables X,Y have success probabilities1/2 and1/3. Define Z=X+Y and W=XY. What is Cov(Z,W)?

**Answer format:** Decimal rounded to four places.

### Q61. [2 Marks] [NAT]

Functions f:{1,2,3}→{1,2,3} are chosen subject to f(f(x))=f(x) for every x. How many such functions exist?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

Two Ethernet stations independently choose backoff counters uniformly from{0,1,2,3} after the same collision. Under the simplified model that only equal counters cause another collision, what is the probability that one station selects a counter exactly one larger than the other?

**Answer format:** Exact decimal.

### Q63. [2 Marks] [MSQ]

A fractional knapsack permits dividing items; all weights and values are positive. Which statements are correct?

A. Sorting by decreasing value/weight yields an optimal packing.
B. Sorting by decreasing absolute value always yields an optimal packing.
C. With distinct ratios, an optimum produced by the ratio rule has at most one partially selected item.
D. The same ratio rule is guaranteed optimal when items become indivisible.

### Q64. [2 Marks] [NAT]

A cache performs write-through with a write buffer of capacity two pending writes. Stores occur at cycles0,1,2. Each buffered write occupies memory for five cycles, serially, and the first begins immediately at cycle0. A completed write leaves the buffer at the start of its completion cycle; a blocked store can enter then. How many cycles does the third store wait before entering the buffer? Count the in-service write as occupying one buffer slot.

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A singly linked list is A→B→C→D→E→NULL. Pointers p and q initially point to B and D. Execute these pointer assignments in order:

```text
t = p.next
p.next = q.next
q.next = t
```

Starting from A afterward, how many distinct list nodes are reachable by repeatedly following next pointers?

**Answer format:** Integer.



---

## ANSWER KEY — MOCK TEST 029

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 3 |
| 2 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 12 |
| 5 | NAT | 1 | 9 |
| 6 | NAT | 2 | 5 |
| 7 | NAT | 2 | -50 |
| 8 | NAT | 2 | 22 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 10.9375 |
| 11 | NAT | 1 | 4 |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 6 |
| 14 | MSQ | 1 | B, C |
| 15 | NAT | 1 | 6 |
| 16 | NAT | 1 | 9 |
| 17 | MSQ | 1 | A, B, D |
| 18 | NAT | 1 | 1 |
| 19 | MSQ | 1 | A, C |
| 20 | NAT | 1 | 2 |
| 21 | NAT | 1 | 1 |
| 22 | MSQ | 1 | A, C |
| 23 | MCQ | 1 | C |
| 24 | NAT | 1 | 8 |
| 25 | NAT | 1 | 92 |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 28 |
| 28 | MSQ | 1 | A, C |
| 29 | NAT | 1 | 0 |
| 30 | MSQ | 1 | A, B |
| 31 | NAT | 1 | 1 |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 2 |
| 34 | MSQ | 1 | A, C |
| 35 | NAT | 1 | 6 |
| 36 | NAT | 2 | 2 |
| 37 | MSQ | 2 | A, D |
| 38 | NAT | 2 | 1 |
| 39 | NAT | 2 | 7.3333 (accepted range 7.33325–7.33335) |
| 40 | MSQ | 2 | A, C |
| 41 | NAT | 2 | 0.1667 (accepted range 0.16665–0.16675) |
| 42 | NAT | 2 | 18 |
| 43 | MSQ | 2 | A, B, D |
| 44 | NAT | 2 | 3 |
| 45 | NAT | 2 | 80 |
| 46 | MSQ | 2 | A, C, D |
| 47 | MSQ | 2 | B, C |
| 48 | NAT | 2 | 90 |
| 49 | NAT | 2 | 3072 |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 2 |
| 52 | MCQ | 2 | D |
| 53 | NAT | 2 | 3.2 |
| 54 | NAT | 2 | 3 |
| 55 | MSQ | 2 | A, C |
| 56 | NAT | 2 | 6 |
| 57 | NAT | 2 | 24 |
| 58 | MSQ | 2 | A, B |
| 59 | NAT | 2 | 16 |
| 60 | NAT | 2 | 0.1944 (accepted range 0.19435–0.19445) |
| 61 | NAT | 2 | 10 |
| 62 | NAT | 2 | 0.375 |
| 63 | MSQ | 2 | A, C |
| 64 | NAT | 2 | 3 |
| 65 | NAT | 2 | 3 |
