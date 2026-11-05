# GATE CS 2027 — Full-Length Mock Test 024

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all remaining questions carry two. Incorrect MCQs lose one-third of their marks. Each MCQ has one correct option. MSQs require all correct options, with no partial credit. MSQs and NATs have no negative marking. Unattempted questions score zero. GA carries15 marks, Engineering Mathematics13 and core CS72. Numerical answers are exact unless rounding is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

Of200 survey invitations,120 recipients responded. Of these respondents,75% supported a proposal. What is the smallest possible percentage of all200 invited recipients who supported the proposal, counting each person's view whether or not they responded?

**Answer format:** Percentage number, without the percent symbol.

### Q2. [1 Mark] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left across x=4 and then the top half down across y=4. A point-sized hole is punched at(4,2), on one fold line but not the other. How many distinct point holes appear after unfolding? Ignore the hole's radius and count distinct coordinates only.

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

A narrative contains: “Mira mailed the parcel after weighing it. She obtained the address before mailing it, but the text does not specify whether she obtained the address before or after weighing.” Which order is inconsistent with this account?

A. Obtain address, weigh, mail.
B. Weigh, obtain address, mail.
C. Weigh, mail, obtain address.
D. Both A and B are possible.

### Q4. [1 Mark] [NAT]

A bag contains one red and three blue balls. They are drawn without replacement until the red ball appears. What is the expected total number of draws, including the red ball?

**Answer format:** Exact decimal.

### Q5. [1 Mark] [MCQ]

Choose the words that fit: “The researcher made ___ measurements at separate time instants and was ___ when discussing confidential results.” Here the first blank means distinct, and the second means tactful.

A. discreet; discrete
B. discrete; discreet
C. discrete; discrete
D. discreet; discreet

### Q6. [2 Marks] [NAT]

A positive quantity is repeatedly multiplied by2. Starting from3, what is the smallest number of multiplications needed to exceed1000? Equality would not suffice.

**Answer format:** Integer.

### Q7. [2 Marks] [MCQ]

A conjecture states: “For every positive integer n, n²+n+41 is prime.” Which single calculation is sufficient to refute the conjecture?

A. It equals43 at n=1.
B. It equals47 at n=2.
C. It equals41² at n=40.
D. It is odd at n=3.

### Q8. [2 Marks] [NAT]

A cube has face labels equal to the original outward normal directions: +x,−x,+y,−y,+z,−z. First rotate the cube90 degrees about the positive x axis, then90 degrees about the positive y axis, each by the right-hand rule about fixed world axes. Encode the face finally pointing upward(+z) as follows: +x=1,−x=2,+y=3,−y=4,+z=5,−z=6. What code results?

**Answer format:** Integer code.

### Q9. [2 Marks] [NAT]

The three-digit strings000 through111 containing only binary digits are listed in increasing binary numerical order, with leading zeros retained. Between each consecutive pair, count how many digit positions change. What is the sum of these counts over all seven transitions?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

An open cylindrical container has a horizontal base area100 square centimetres and initially contains water to depth5 cm. A solid cube of side4 cm is placed flat on the bottom without spilling water. Assuming the cube becomes fully submerged, what is the final water depth?

**Answer format:** Exact decimal in centimetres.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A sequence satisfies a0=0 and an=2a(n−1)+2^n for n≥1. What is a5?

**Answer format:** Integer.
### Q12. [1 Mark] [MSQ]

A stable sorting algorithm sorts records by a numeric key. Which statements are correct?

A. Equal-key records retain their relative input order.
B. Stability alone guarantees O(n log n) running time.
C. Stability matters when a previous ordering among equal keys must be preserved.
D. A stable sort necessarily leaves all unequal-key records in their original relative order.

### Q13. [1 Mark] [NAT]

Grammar S→Aa, A→bA | ε is parsed by an LL(1) parser. The stack top is A and the next input token is a. How many terminal symbols does applying the selected A production add to the stack?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

After fork, a parent and child initially share read-only physical pages under copy-on-write. Each has its own virtual mappings. Which statements are correct?

A. The first write by one process may trigger a fault and a private copy.
B. Every page must be copied immediately at fork under this scheme.
C. A successful private copy can allow one process to modify its page without changing the other's contents.
D. Sharing a physical page initially implies that later writes must always be visible to both processes.

### Q15. [1 Mark] [NAT]

Assume conventional C semantics and representable integer values. What is the final value of a[1]?

```c
int a[3] = {1,2,3};
int *p = a;
int x = *p++;
*p += x;
```

**Answer format:** Integer.

### Q16. [1 Mark] [MSQ]

A NAT rewrites an outgoing IPv4 packet's source address and TCP source port. Assume ordinary checksums are used and no checksum offload is involved. Which statements are correct?

A. The IPv4 header checksum must reflect the address change.
B. The TCP checksum may need updating because it covers the TCP header and an IP pseudo-header.
C. The TCP checksum covers only application payload, so ports are irrelevant.
D. Changing an IPv4 address never affects transport-layer checksum calculation.

### Q17. [1 Mark] [NAT]

A simplified TCP sender uses congestion window10 segments and slow-start threshold6 segments. On a specified timeout, it sets the threshold to half the old window and the window to1 segment. What is the sum of its new threshold and new window, in segments?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

A direct-mapped cache has four lines and starts empty. Block b maps to line b modulo4. For references0,4,0,4, how many are conflict misses after excluding the first access to each distinct block as compulsory?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A syntax-directed definition for a list uses L→L1,d with L.count=L1.count+1, and L→d with L.count=1. How many applications of the recursive production occur in a parse of d,d,d,d,d?

**Answer format:** Integer.

### Q20. [1 Mark] [MCQ]

A function recursively calls itself. Its local scalar variable v must have a separate value for each active call. Which storage arrangement directly supports this requirement?

A. One shared static cell for v with no saving.
B. A separate v slot in each activation record.
C. A single constant compiled into the program.
D. The caller's instruction address used as v's only storage.

### Q21. [1 Mark] [NAT]

An unsigned fixed-point format has three integer bits and two fractional bits, with no padding. What is its largest representable value?

**Answer format:** Exact decimal.

### Q22. [1 Mark] [NAT]

Procedure F(n) returns1 when n=0 and otherwise returns F(n−1)+F(n−1), making both calls without memoization. How many base-case invocations occur in F(5)?

**Answer format:** Integer.

### Q23. [1 Mark] [MSQ]

For propositions p and q, which formulas are logically equivalent to NOT(p implies q)?

A. p AND NOT q.
B. NOT p OR q.
C. p AND (p XOR q).
D. NOT p AND q.

### Q24. [1 Mark] [MSQ]

A floating-point format has both signed zeros and infinities, with ordinary IEEE-style comparisons and division. Which statements are correct?

A. +0 and−0 compare equal.
B. Dividing positive1 by+0 and by−0 can distinguish their signs in the resulting infinities.
C. Equal comparison necessarily means identical bit representations.
D. Positive infinity is an ordinary largest finite number in the format.

### Q25. [1 Mark] [NAT]

A hash function distributes each key independently and uniformly over five buckets. For three distinct keys, what is the probability that all occupy different buckets?

**Answer format:** Exact decimal.

### Q26. [1 Mark] [MSQ]

A symbolic link stores a pathname rather than increasing its target file's hard-link count. Which statements are correct?

A. Deleting the target's only pathname can leave a dangling symbolic link.
B. A symbolic link necessarily prevents the target inode from being reclaimed forever.
C. A symbolic link can name a target on another file system under ordinary pathname resolution.
D. Every symbolic link is indistinguishable from a hard link in inode reference counting.

### Q27. [1 Mark] [NAT]

A real3×3 matrix has rank2. A consistent linear system Ax=b therefore has a solution set that is an affine space of what dimension?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A DMA transfer copies4096 bytes in16-byte bursts. Every burst requires one bus-grant handshake, and no burst is partial. How many handshakes are required?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

A recognizer for a language may loop on some nonmembers. Which statements are correct?

A. If it accepts an input, that input is a member.
B. If it has not halted after a fixed finite number of steps, the input must be a nonmember.
C. A decider must halt on every input.
D. Every recognizer is automatically a decider.

### Q30. [1 Mark] [NAT]

For x≠1, f(x)=(x³−1)/(x−1). What value must be assigned to f(1) to make f continuous at1?

**Answer format:** Exact number.

### Q31. [1 Mark] [NAT]

A nonnegative integer-valued random variable X satisfies P(X=0)=1/2, P(X=1)=1/4 and P(X=2)=1/4. What is Var(X)?

**Answer format:** Exact decimal.

### Q32. [1 Mark] [NAT]

A complete DFA has a start state that is accepting and one rejecting sink. On a it remains in the start state, and on b it enters the sink, which loops on both letters. How many strings of length4 over{a,b} does it accept?

**Answer format:** Integer.

### Q33. [1 Mark] [MSQ]

For Boolean variables x,y, which expressions equal x XOR y for every assignment?

A. (x OR y) AND NOT(x AND y).
B. (x AND NOT y) OR (NOT x AND y).
C. x OR y.
D. NOT(x XOR y).

### Q34. [1 Mark] [MCQ]

A transaction commits before any transaction whose uncommitted data it read has committed. Which recovery property can this violate?

A. Recoverability.
B. The fact that read–read operations commute.
C. The definition of a primary key.
D. The physical size of disk blocks.

### Q35. [1 Mark] [MSQ]

Under strict two-phase locking, exclusive locks are retained until commit or abort. Which statements are correct?

A. Another transaction cannot read an item modified under an unreleased exclusive lock.
B. Retaining exclusive locks prevents cascading aborts caused by reading those uncommitted writes.
C. The rule alone makes deadlock impossible.
D. A transaction may release an exclusive lock immediately after its write under this strict rule.

### Q36. [2 Marks] [MCQ]

For n≥4, what is the asymptotic number of calls to work()? Arithmetic uses unbounded integers.

```text
i = 2
while i <= n:
    j = 2
    while j <= i:
        work()
        j = j*j
    i = 2*i
```

A. Θ(log n)
B. Θ(log n log log n)
C. Θ(n log log n)
D. Θ((log n)²)

### Q37. [2 Marks] [NAT]

A process has descriptor3 for an open file. It calls dup(3), obtaining descriptor4. It then sets the close-on-exec flag on descriptor3 only and successfully executes a new program. No other descriptor refers to this open-file description. How many descriptors in the new program refer to it?

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

Grammar S→aS | aSbS | ε uses terminals a,b. Which statements are correct?

A. Every generated string has at least as many a's as b's.
B. Every prefix of every generated string has at least as many a's as b's.
C. The grammar generates ba.
D. The grammar generates aab.

### Q39. [2 Marks] [NAT]

A three-variable Boolean function is1 on every input except000 and111. Product terms may cover only1-inputs. What is the minimum number of product terms in a sum-of-products implementation?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

An application sends two messages over one TCP connection, adding no lengths, delimiters or other framing. The receiver knows neither message length. Which statements are correct?

A. TCP's ordered delivery alone identifies the boundary between the messages.
B. The same received byte string may correspond to more than one split into two messages.
C. A protocol-level length field can make boundaries recoverable.
D. One send call necessarily corresponds to one recv call.

### Q41. [2 Marks] [NAT]

One process executes the following pseudocode. Every fork succeeds and duplicates the current process; no process exits early.

```text
fork()
if fork() returns 0:
    fork()
```

Including the original process, how many processes exist after all forks complete?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

An array of eight distinct values is reordered in place by exchanging entries whose indices are reversals of each other's three-bit binary representation. Indices range0–7. Each unequal pair is exchanged once, and equal-index pairs are untouched. How many swaps occur?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A compiler translates a short-circuit Boolean expression (p AND q) OR r into a decision graph. Each predicate occurrence is evaluated at most once on any execution, in source short-circuit order. How many different subsets of {p,q,r} can be evaluated during an execution, as their truth values vary?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A scalar pipeline can issue one instruction per cycle. A multiply produces its result three cycles after its issue; an add produces its result one cycle after issue. A consumer may issue in the cycle its last operand becomes available. Consider independent multiplies M1,M2 followed by add A consuming both, then add B consuming A. Issue M1 at cycle0 and schedule as early as possible, without other hazards. In what cycle does B's result become available?

**Answer format:** Integer cycle number.

### Q45. [2 Marks] [MSQ]

A Boolean cover-selection chart contains candidate rows P and Q. P covers{u,v} at cost3; Q covers{u,v,w} at cost2. The objective is minimum total cost, and selecting a row has no effect except covering its columns. Which statements are correct?

A. An optimal cover can always be chosen without P.
B. Replacing P by Q in a cover cannot uncover a column and cannot increase cost.
C. P must be retained merely because some of its columns also appear in Q.
D. The same dominance conclusion follows if Q instead costs5, solely from its greater coverage.
### Q46. [2 Marks] [NAT]

An ER relationship connects Student and Course, each with its own key, and allows many students per course and many courses per student. The relationship has attribute grade, with at most one grade for a particular student-course pair. If there are3 students and4 courses and every pair participates, how many relationship rows are required in the ordinary relational mapping?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

Finite sets A and B have sizes3 and4. How many ordered pairs of functions f:A→B and g:B→A satisfy g(f(a))=a for every a in A?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

A singly linked list is acyclic. A pointer p identifies a non-tail node, but the predecessor of p is unavailable. A proposed deletion copies the successor's value into p and bypasses that successor. Which statements are correct?

A. The resulting value sequence matches deleting p's original value at that position.
B. The operation preserves the identity of every node that ordinary deletion of p would preserve.
C. It requires p to have a successor under the stated implementation.
D. External references to node identities can make this different from actually deleting node p.

### Q49. [2 Marks] [NAT]

An instruction computes an address by first adding a signed displacement to a base register, then reading a32-bit pointer from that address, then using the pointer as the final operand address. Base=1000, displacement=12, and memory word at1012 contains2040. The operand is a four-byte integer. How many data-memory reads are needed to obtain the operand, excluding instruction fetch and assuming no cache hits?

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

Let A=[[2,1],[0,2]]. Which statements are correct?

A. A has two linearly independent eigenvectors over the real numbers.
B. A⁵ has diagonal entries32 and32.
C. A⁵−32I has rank1.
D. A⁵=32I.

### Q51. [2 Marks] [NAT]

What is the maximum value of x²(1−x) for0≤x≤1? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q52. [2 Marks] [NAT]

A message queue has capacity3. It starts empty. Process P executes send(A),send(B),send(C),send(D) in order, and process Q has not yet run. Each send blocks if the queue is full; a successful send appends one item. How many of P's sends have completed when it first blocks?

**Answer format:** Integer.

### Q53. [2 Marks] [MSQ]

In the interval-scheduling problem, intervals are half-open and all have equal value. Which statements are correct about choosing a compatible interval with earliest finishing time at each step?

A. An exchange argument can replace the first interval of an optimal solution by an earliest-finishing interval without reducing the number still schedulable afterward.
B. The same rule necessarily maximizes total value when intervals have arbitrary positive weights.
C. Half-open intervals ending and starting at the same time are compatible.
D. Choosing the longest interval first is always equivalent to earliest finish.

### Q54. [2 Marks] [NAT]

A PDA starts with one bottom-of-stack marker. On each input a it pushes two ordinary symbols; on each b it pops one ordinary symbol and rejects if only the bottom marker remains. Acceptance requires input exhaustion with only the marker left. For input aabbbb, what is the maximum stack height, counting the marker, reached during the computation?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

Consider replacing x*2 by x+x in an integer intermediate representation. Which statements are correct?

A. For unbounded mathematical integers the two expressions are equal.
B. For arithmetic modulo2^w the two results are equal for every w-bit x.
C. This equivalence alone proves that replacing any signed C expression involving multiplication can ignore its language's overflow rules.
D. The replacement's profitability can depend on the target machine, even when semantic equivalence holds.

### Q56. [2 Marks] [NAT]

Under set semantics, R(A)={1,2,3} and S(A,B)={(1,x),(1,y),(2,x)}. Compute R−projection_A(S). How many tuples are in the result?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

In first-order notation, consider the query {x : R(x) AND (exists x S(x))}, where the inner quantifier binds only its own occurrence of x and shadows the outer name within its parentheses. R and S are finite unary relations. Which statements are correct?

A. Renaming the bound inner variable to y leaves the query unchanged.
B. The query always returns R intersect S.
C. If S is nonempty, the query returns all of R.
D. If S is empty, the query returns the empty relation.
### Q58. [2 Marks] [NAT]

An HTTP cache has a stored response with an entity tag. On revalidation the server returns a304 response with no representation body, confirming that the stored representation is usable. The representation is5000 bytes, and the304 response is200 bytes. Ignoring the request and all other overhead, how many response bytes are saved compared with a full response of5200 bytes?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

An unsigned four-bit adder adds inputs11 and9 with carry-in0. Let S be the low four-bit unsigned result and C the carry-out bit. What is S+16C?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A circular queue uses an array of length5 and reserves one slot to distinguish full from empty. Initially front=rear=0. Three enqueues, two dequeues, and then three enqueues all succeed. Indices advance modulo5. What is rear after the last enqueue?

**Answer format:** Integer index.

### Q61. [2 Marks] [MSQ]

An IP router forwards a packet across two different Ethernet links. The packet's IPv4 source and destination are unchanged by assumption; TTL is decremented. Which statements are correct?

A. The outgoing Ethernet header can differ from the incoming Ethernet header.
B. The IPv4 header checksum must account for the TTL change.
C. End-to-end IP destination being unchanged requires the Ethernet destination address to remain unchanged on every hop.
D. Link-layer addressing and network-layer addressing serve different scopes.

### Q62. [2 Marks] [NAT]

A16-to-1 multiplexer is built entirely from2-to-1 multiplexers arranged as a binary selection tree, without sharing data inputs between tree branches. How many2-to-1 multiplexers are required?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A longest-common-subsequence computation compares strings ABA and BAA. What is the length of a shortest common supersequence of the two strings?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

In a compiler's constant lattice, a join keeps a constant only if all reachable incoming values agree. A block has incoming x=5 from one reachable predecessor and x=7 from an unreachable predecessor. Which statements are correct if reachability information is used?

A. The unreachable predecessor need not force x to be nonconstant.
B. x may be propagated as5 at the block's entry.
C. Treating every syntactic predecessor as reachable can lose this optimization.
D. Reachability information never affects constant propagation.

### Q65. [2 Marks] [MSQ]

A condition D has probability0.1. Two tests are independent conditional on whether D holds. Each test is positive with probability0.9 given D and0.2 given NOT D. Which statements are correct?

A. The two positive-result indicators are independent without conditioning.
B. The probability both tests are positive is0.117.
C. Given both positive, P(D)=9/13.
D. Given one positive, a second positive leaves P(D) unchanged.


---

## ANSWER KEY — MOCK TEST 024

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 45 |
| 2 | NAT | 1 | 2 |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 2.5 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 9 |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 2 |
| 9 | NAT | 2 | 11 |
| 10 | NAT | 2 | 5.64 |
| 11 | NAT | 1 | 160 |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 0 |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 3 |
| 16 | MSQ | 1 | A, B |
| 17 | NAT | 1 | 6 |
| 18 | NAT | 1 | 2 |
| 19 | NAT | 1 | 4 |
| 20 | MCQ | 1 | B |
| 21 | NAT | 1 | 7.75 |
| 22 | NAT | 1 | 32 |
| 23 | MSQ | 1 | A, C |
| 24 | MSQ | 1 | A, B |
| 25 | NAT | 1 | 0.48 |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 1 |
| 28 | NAT | 1 | 256 |
| 29 | MSQ | 1 | A, C |
| 30 | NAT | 1 | 3 |
| 31 | NAT | 1 | 0.6875 |
| 32 | NAT | 1 | 1 |
| 33 | MSQ | 1 | A, B |
| 34 | MCQ | 1 | A |
| 35 | MSQ | 1 | A, B |
| 36 | MCQ | 2 | B |
| 37 | NAT | 2 | 1 |
| 38 | MSQ | 2 | A, B, D |
| 39 | NAT | 2 | 3 |
| 40 | MSQ | 2 | B, C |
| 41 | NAT | 2 | 6 |
| 42 | NAT | 2 | 2 |
| 43 | NAT | 2 | 3 |
| 44 | NAT | 2 | 6 |
| 45 | MSQ | 2 | A, B |
| 46 | NAT | 2 | 12 |
| 47 | NAT | 2 | 72 |
| 48 | MSQ | 2 | A, C, D |
| 49 | NAT | 2 | 2 |
| 50 | MSQ | 2 | B, C |
| 51 | NAT | 2 | 0.1481 (accepted range 0.14805–0.14815) |
| 52 | NAT | 2 | 3 |
| 53 | MSQ | 2 | A, C |
| 54 | NAT | 2 | 5 |
| 55 | MSQ | 2 | A, B, D |
| 56 | NAT | 2 | 1 |
| 57 | MSQ | 2 | A, C, D |
| 58 | NAT | 2 | 5000 |
| 59 | NAT | 2 | 20 |
| 60 | NAT | 2 | 1 |
| 61 | MSQ | 2 | A, B, D |
| 62 | NAT | 2 | 15 |
| 63 | NAT | 2 | 4 |
| 64 | MSQ | 2 | A, B, C |
| 65 | MSQ | 2 | B, C |


