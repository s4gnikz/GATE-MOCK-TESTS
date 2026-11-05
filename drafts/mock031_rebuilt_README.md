# GATE CS 2027 — Full-Length Mock Test 031

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

The examination lasts180 minutes. Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes15 marks, Engineering Mathematics13, and core Computer Science72.

MCQs have exactly one correct option. MSQs have multiple correct options and earn credit only when all and only those choices are selected. Incorrect one-mark and two-mark MCQs incur penalties of1/3 and2/3 mark respectively. MSQ and NAT questions have no negative marking. Unattempted questions receive zero; there is no partial credit. Follow each NAT answer format. The answer key follows Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MSQ]

For a statement P(n) about integers n≥2, a proof establishes P(2) and P(k) implies P(k+2) for every integer k≥2. Which conclusions follow?

A. P(n) holds for every even integer n≥2.
B. These facts alone prove P(3).
C. Adding a proof of P(3) would establish P(n) for every integer n≥2.
D. The step from k to k+2 supplies the missing odd base case automatically.

### Q2. [1 Mark] [NAT]

The central unit square is removed from a3×3 board of unit squares. How many tilings of the remaining eight squares by1×2 dominoes exist? Rotations and reflections of a tiling count as different if the occupied domino pairs differ.

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

Let a(n) be the largest exponent k such that2^k divides n!. What is a(16)−a(15)?

**Answer format:** Integer.

### Q4. [1 Mark] [NAT]

A6-by-4 rectangle has a1-by-1 square removed at each of its four corners. Count all exposed edges of the remaining shape. What is its perimeter?

**Answer format:** Integer length units.

### Q5. [1 Mark] [MCQ]

Select the pair completing the sentence with correct subject–verb agreement: “One of the proposals that ___ discussed yesterday ___ now been withdrawn.”

A. was, have
B. were, have
C. was, has
D. were, has

### Q6. [2 Marks] [NAT]

A fixed event budget initially allocates40% to food,35% to transport and25% to other costs. Food costs rise by25% of their originally allocated amount, and other costs stay fixed. To keep total spending unchanged, by what percentage must the original transport allocation be reduced?

**Answer format:** Percentage rounded to four decimal places, without the percent sign.

### Q7. [2 Marks] [MCQ]

Each of four people is either a truth-teller, whose statement below is true, or a liar, whose statement is false. A says “B is a liar.” B says “C is a liar.” C says “D is a liar.” D says “A and B are both truth-tellers.” Which pair consists exactly of the truth-tellers?

A. A,B
B. A,C
C. B,D
D. C,D

### Q8. [2 Marks] [NAT]

A cube on a horizontal grid has top face1, bottom6, north-facing face2, south-facing5, east-facing3 and west-facing4. It rolls one square north, then east, then south, then west, without slipping or turning about the vertical axis between rolls. A north roll puts the former north-facing face on the bottom; analogous conventions apply to the other directions. What number is on top afterward?

**Answer format:** Integer face label.

### Q9. [2 Marks] [MCQ]

A report states: “The mean travel time was unchanged after the timetable revision, although individual passengers experienced both increases and decreases.” Which conclusion is supported?

A. Every passenger's travel time stayed unchanged.
B. Equal means imply identical travel-time distributions.
C. An unchanged aggregate measure can coexist with changes in individual outcomes.
D. The timetable revision necessarily improved every passenger's journey.

### Q10. [2 Marks] [NAT]

Five distinct files must be assigned to two labelled storage boxes. Each box must receive at least two files. Two specified files must go to different boxes. How many assignments satisfy both conditions?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

SQL table T(x) has two rows, both x=NULL. Compare Q1=SELECT COUNT(*) FROM (SELECT DISTINCT x FROM T) AS U and Q2=SELECT COUNT(DISTINCT x) FROM T. What pair of scalar results (Q1,Q2) is returned?

A. (0,0)
B. (2,0)
C. (1,1)
D. (1,0)
### Q12. [1 Mark] [MCQ]

A finite language contains no word longer than20 symbols. Why can21 serve as a pumping length in the necessary pumping condition for regular languages?

A. Every word in the language has a nonempty substring of length21.
B. Every word of length21 must be in the language.
C. There are no language words of length at least21 to which the pumping requirement applies.
D. Pumping lengths may be chosen only for infinite languages.

### Q13. [1 Mark] [NAT]

How many triples of nonnegative integers(x,y,z) satisfy x+y+z=8, x≤2, and y odd?

**Answer format:** Integer.

### Q14. [1 Mark] [MCQ]

A datagram socket has two queued datagrams, with payloads ABCDE and FG in that order. A receive buffer has space for three bytes. In this specified model, a receive returns at most one datagram and discards any excess bytes of a truncated datagram. After one receive returns ABC, what payload does the next receive return?

A. FG
B. DE
C. DEF
D. DEFG

### Q15. [1 Mark] [MSQ]

Given an arbitrary Turing machine M over{0,1}, consider whether it accepts at least one word of length at most3. Which statements are correct?

A. Dovetailing simulations on the finitely many candidate words recognizes YES instances.
B. The finite number of candidate words alone makes this property decidable for arbitrary M.
C. Its negation is also recognizable for arbitrary M.
D. If M is promised to halt on every input, sequentially testing all candidates decides the property under that promise.

### Q16. [1 Mark] [NAT]

A normalized binary floating-point format has a fixed number of significant bits, enough exponent range, and spacing0.25 between successive values in[8,16). It rounds to nearest with ties to an even least significant significand bit. What is the rounded value of9.125?

**Answer format:** Exact decimal.

### Q17. [1 Mark] [MCQ]

A three-input Boolean function satisfies F(x,y,z)=NOT F(NOT x,NOT y,NOT z) on every input and F(0,0,0)=0. How many different truth tables satisfy these conditions?

A. 4
B. 8
C. 16
D. 32
### Q18. [1 Mark] [NAT]

A system has one resource type and three processes. Currently available instances=2. Allocations to P1,P2,P3 are1,2,2, and their maximum demands are3,4,6 respectively. A process may finish if its remaining need can be met, then releases its entire allocation. How many permutations of the three processes are safe completion orders?

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

Records (key,id) occur initially as(1,A),(1,B),(2,C). They are stably sorted by ascending key and the whole resulting array is then reversed. Relative to the original input, is this a stable descending-key sort?


A. No, because A and B appear in the opposite order.
B. Yes, because reversing always preserves equal-key order.
C. No, because key2 appears before key1.
D. Yes, because the ascending sort was stable.

### Q20. [1 Mark] [NAT]

For the augmented grammar S'→S, S→CC, C→cC | d, let I0 be the LR(0) closure of S'→·S. How many items are in GOTO(I0,C), including closure items?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A formal power series F(x) satisfies(1−x)²F(x)=1+x. What is the coefficient of x4 in F(x)?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

An eight-slot hash table probes i² modulo8 for i=0,1,2,... when inserting a particular key. All slots reached by this sequence are occupied. What is the largest possible number of empty slots elsewhere in the table despite this insertion being unable to reach them?

**Answer format:** Integer.

### Q23. [1 Mark] [MSQ]

Consider formulas P:∀x∃y(x≠y) and Q:∃y∀x(x≠y), with equality interpreted normally over a nonempty domain. Which statements are correct?

A. P is true on every domain with at least two elements.
B. Q is true on every domain with at least two elements.
C. Q is false on every nonempty domain, finite or infinite.
D. P implies Q on every nonempty domain.

### Q24. [1 Mark] [MCQ]

An arithmetic right shift by one on the signed value−7 produces floor(−7/2). Integer division by2 instead truncates toward zero. What is the shifted value minus the division result?

A. 0
B. 1
C. −7
D. −1

### Q25. [1 Mark] [NAT]

Let u=(1,2,3)ᵀ, v=(2,−1,0)ᵀ, and A=I+uvᵀ. What is the entry in row2,column1 of A^(−1)?

**Answer format:** Exact signed number.

### Q26. [1 Mark] [MCQ]

A dynamic array doubles capacity when an append encounters a full array and halves capacity immediately when a removal leaves size exactly half the current capacity. Each resize copies all retained elements. Starting with size and capacity both n, repeatedly append one element and then remove it, for k repetitions. Ignore unrelated work. What is the total copying cost?

A. Θ(k)
B. Θ(n+k)
C. Θ(kn)
D. Θ(log n)

### Q27. [1 Mark] [NAT]

A microinstruction independently selects at most one of three signals in group A, at most one of five signals in group B, and any subset of two further independent signals. Each group needs an explicit “none” encoding. Encode each group in its own minimum-width binary field and the further signals as individual bits. How many control bits are required?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

For production S→ABC, which proposed inherited-attribute dependency violates the left-to-right dependency restriction of an L-attributed definition?


A. A.in depends on C.out.
B. B.in depends on A.out.
C. C.in depends on B.out.
D. A.in depends on S.in.

### Q29. [1 Mark] [MCQ]

A DNS configuration contains only the alias records alpha→beta and beta→alpha for the names being resolved, with neither leading to an address record. Which conclusion is appropriate?

A. The resolver can infer an address from either name's spelling.
B. Following these aliases cycles and cannot produce an address from these records alone.
C. Two aliases necessarily cancel, yielding the client's own address.
D. The resolver must return whichever address it used for its previous unrelated query.

### Q30. [1 Mark] [MSQ]

An SQL integer column x has CHECK(x>0) but no NOT NULL constraint. A CHECK passes when its condition is TRUE or UNKNOWN. Which statements are correct?

A. A row with x=NULL can satisfy this CHECK.
B. Every non-NULL value satisfying this CHECK is positive.
C. The CHECK alone excludes NULL values.
D. Adding NOT NULL would impose no additional restriction.

### Q31. [1 Mark] [NAT]

Three jobs arrive at0. Estimated CPU bursts for A,B,C are1,2,3, while actual bursts are8,1,1. A nonpreemptive scheduler executes jobs by increasing estimate. What is its total waiting time minus the minimum total waiting time attainable with knowledge of the actual bursts? There is no switching overhead.

**Answer format:** Integer time units.

### Q32. [1 Mark] [NAT]

Functions F,G are defined on integers by F(n)=1 for n≤0, otherwise F(n)=1+G(n−2); and G(n)=1 for n≤0, otherwise G(n)=1+F(n−1). What is F(7)?

**Answer format:** Integer.

### Q33. [1 Mark] [MCQ]

An instance of R(A,B) contains exactly(1,2) and(2,2). Which proposed functional dependency is violated by this instance?

A. A→B
B. AB→A
C. B→A
D. AB→B

### Q34. [1 Mark] [NAT]

An array initially contains[1,2,3,4,5]. First copy its first four entries to positions1 through4, using zero-based indices and semantics as if the source were saved in a temporary array before writing. Then similarly copy positions2 through4 to positions0 through2. What is the sum of all five final entries?

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

A real function f is defined on a neighbourhood of0. Which statements are correct?

A. Differentiability at0 implies continuity there.
B. Continuity at0 implies differentiability there.
C. If both one-sided derivatives at0 exist as finite real numbers, f is continuous at0 even if those derivatives differ.
D. Equal finite one-sided derivatives at0 are insufficient for differentiability there.

### Q36. [2 Marks] [MSQ]

Inputs A,B encode only the three states00,01,10;11 is unreachable. The required output is0 at00 and1 at01 and10. Behaviour at11 is unconstrained. Which expressions correctly implement the specified behaviour on every reachable state?

A. A OR B
B. A XOR B
C. A AND B
D. NOT(A AND B)

### Q37. [2 Marks] [NAT]

A512-byte slotted page has a32-byte fixed header and six retained four-byte slot entries. Each record must occupy a contiguous region. Its six records, in adjacent physical order, have lengths60,70,80,50,40,30 bytes. All remaining free space is one contiguous gap between the slot directory and records. Delete the adjacent80-byte and50-byte records, retaining their slot entries. A new record must use a new four-byte slot entry. What is the increase in the maximum insertable record length if the remaining records may be compacted, compared with insertion without moving them?

**Answer format:** Integer bytes.

### Q38. [2 Marks] [MSQ]

A16-bit memory interface consists of two independently enabled eight-bit banks. The low bank holds even byte addresses; the high bank holds odd byte addresses. One bus transaction accesses both bytes of one aligned two-byte word, and can enable either bank or both. Which statements are correct?

A. An aligned two-byte load can be serviced in one transaction.
B. A two-byte load starting at an odd address always fits in one aligned-word transaction.
C. A byte store can preserve the other byte by enabling only its target bank.
D. Changing endianness changes which numerical byte address is even.

### Q39. [2 Marks] [MSQ]

Random variables X∈{1,2} and Y∈{0,1} have joint probabilities P(X=x,Y=y)=c(x+y), for a normalizing constant c. Which statements are correct?

A. c=1/8.
B. X and Y are independent.
C. P(Y=1)=5/8.
D. E[X|Y=0]=5/3.

### Q40. [2 Marks] [MSQ]

A fractional knapsack has capacity5 and two available items, each of weight4 and value8. Any real fraction between0 and1 of each item may be selected. Which statements are correct?

A. Selecting weight2.5 from each item is optimal.
B. Every optimal solution must have at most one partially selected item.
C. An optimal solution with one whole item and one partially selected item exists.
D. The optimal allocation is unique.

### Q41. [2 Marks] [NAT]

A prime-implicant chart requires columns1,2,3,4,5. Rows A,B,C,D cover respectively{1,2},{2,3},{3,4,5},{1,4,5}, with literal costs2,2,3,3. Only these rows are available. How many distinct minimum-total-cost covers exist?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A procedure make() creates a fresh variable x=0 and returns a closure inc that increments that captured variable by1 and returns its new value. Set f=make(), g=f, and h=make(). Each closure retains its environment after make returns. Calls f(),g(),h(),f() are made in that order. What is the sum of the returned values?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A path starts at the top-left cell and ends at the bottom-right cell of the cost grid below, moving only one cell right or down. Its cost is the sum of visited cell costs, including both endpoints. Once during the path, it may replace one visited cell's cost by0. What is the minimum possible path cost?

```text
 0   5   1
 2  -4   3
 9   2   0
```

**Answer format:** Exact signed integer.

### Q44. [2 Marks] [MSQ]

Assume ordinary TCP, UDP and IPv4 layering, without application-specific boundary reconstruction. Which statements are correct?

A. TCP does not preserve individual application write boundaries as receive-message boundaries.
B. A UDP datagram can never be fragmented at the IPv4 layer.
C. IPv4 fragmentation may be hidden from the receiving UDP application by IP reassembly.
D. A link-layer frame's header must remain unchanged across all routers on a path.

### Q45. [2 Marks] [MCQ]

An array a initially contains[1,2], with i=0,j=1,k=0. The intended intermediate operation is a[i]=a[j]+a[k], evaluating both loads before the store. A faulty translation instead executes a[i]=a[j]; followed by a[i]=a[i]+a[k]. What is the faulty final a[0] minus the intended final a[0]?

A. −1
B. 0
C. 2
D. 1

### Q46. [2 Marks] [MCQ]

A B+ tree has all leaves exactly two edges below the root. The root and each nonroot internal node have between two and four children. Each leaf stores between two and four data keys; internal separator copies are not data keys. Which pair gives the minimum and maximum possible data-key counts?

A. (4,16)
B. (8,64)
C. (8,32)
D. (16,64)

### Q47. [2 Marks] [MSQ]

Two sorted singly linked lists have distinct prefix nodes but share the same suffix nodes. A standard in-place merge is written assuming disjoint lists: it links the smaller current node to the result, advances that list pointer, and repeats, without testing pointer equality. Which statements are correct?

A. Shared nodes can make the merge create a cycle or fail to terminate.
B. If both current pointers are equal, appending that shared suffix once and terminating avoids duplicate processing of that suffix.
C. Equality of node values alone proves that two pointers refer to the same node.
D. Sortedness alone guarantees safety of this disjoint-list merge on shared-suffix inputs.

### Q48. [2 Marks] [MSQ]

Let f:{a,b,c}→{0,1} satisfy f(a)=f(b)=0 and f(c)=1. Which statements are correct?

A. Exactly two functions g:{0,1}→{a,b,c} satisfy f composed with g equal to the identity on{0,1}.
B. Some function g satisfies g composed with f equal to the identity on{a,b,c}.
C. Every g satisfying the identity in A is injective.
D. f is injective.

### Q49. [2 Marks] [MSQ]

An inclusive two-level cache requires every block in L1 also to be present in L2. An exclusive design instead requires blocks resident in L1 to be absent from L2. Ignore other cache levels. Which statements are correct?

A. Evicting an L2 block in the inclusive design may require invalidating its L1 copy.
B. An inclusive L1 miss can never be an L2 hit.
C. The exclusive design permits the same block to remain simultaneously in both levels by definition.
D. Replication in the inclusive design can reduce the number of distinct resident blocks compared with equal-capacity exclusive levels.

### Q50. [2 Marks] [NAT]

A disk head is at cylinder50. Three requests target55,30,80. Seek time is one time unit per cylinder. Their additional rotational waits after reaching the target are respectively50,0,0 time units; transfer times are equal and may be ignored. How much larger is the first-request service time selected by shortest-seek-time-first than the smallest available first-request service time?

**Answer format:** Integer time units.

### Q51. [2 Marks] [NAT]

Free memory holes, in address order, have sizes200,500,300 bytes. Process requests250 bytes and then200 bytes; each allocation consumes space from the beginning of its chosen hole, without overhead. Compare first-fit with best-fit, starting separately from the original holes. What is the largest remaining hole under best-fit minus that under first-fit?

**Answer format:** Integer bytes.

### Q52. [2 Marks] [NAT]

Values1,2,3,4,5 arrive in that order at a single stack, with pushes and pops interleaved as needed. What is the minimum stack capacity permitting the complete pop sequence3,4,2,1,5?

**Answer format:** Integer elements.

### Q53. [2 Marks] [MSQ]

A circuit maps input bits x,y,z to u=x XOR y, v=y XOR z, w=x XOR z. Let t be the three-input majority bit. Which statements are correct?

A. w=u XOR v.
B. The triple(u,v,w) uniquely determines(x,y,z).
C. The four outputs(u,v,w,t) uniquely determine(x,y,z).
D. All eight possible triples(u,v,w) occur.

### Q54. [2 Marks] [MSQ]

Two transactions both hold shared locks on x and each requests an upgrade to an exclusive lock before releasing its shared lock. No other transaction holds a lock. Which statements are correct?

A. Both upgrade requests can block, creating a deadlock.
B. The two-phase-locking rule by itself prevents this deadlock.
C. Each exclusive upgrade conflicts with the other transaction's shared lock.
D. The original pair of shared locks already conflicted with each other.

### Q55. [2 Marks] [NAT]

For a binary input string, prepend zeroes if needed to obtain at least three bits. Accept exactly when the last three bits of this padded string have even parity; thus the empty string is accepted. What is the minimum number of states of a complete DFA recognizing this language?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

A full binary recursion tree has n=2^k leaves at depth k, with the root at depth0. Every call at depth d allocates and initializes2^d buffer cells, retains them while processing its children sequentially in depth-first order, then frees them before returning. Leaves also allocate their stated buffers. What are the tight orders of total cell initializations and maximum simultaneously live buffer cells, respectively?


A. (Θ(n²),Θ(n))
B. (Θ(n log n),Θ(n))
C. (Θ(n²),Θ(n²))
D. (Θ(n log n),Θ(log n))

### Q57. [2 Marks] [NAT]

A circuit-switched transfer has setup time1ms and then sends L payload bits at2 Mbit/s with no other overhead. A packet-switched alternative has no setup, sends at1 Mbit/s, and adds100 header bits per packet with at most900 payload bits per packet. Packets are filled except possibly the last; ignore all other delays. What is the smallest positive integer L for which the circuit-switched transfer finishes strictly earlier?

**Answer format:** Integer bits.

### Q58. [2 Marks] [MSQ]

A program over mathematical integers executes while(x!=0){x=2*x+1;} and then returns0. No value of x is observed afterward. An optimizer removes the loop because x is unused at the return. Which statements are correct?

A. For initial x=0, both versions return0.
B. For initial x=1, the rewrite changes a nonterminating execution into a terminating one.
C. Absence of a later use of x is sufficient to justify this rewrite for every input.
D. Preserving termination behaviour matters for this transformation.

### Q59. [2 Marks] [MSQ]

A DMA device is programmed with a physical frame address, and it does not consult the process's page table on subsequent writes. An operating system is considering evicting and reusing that frame before DMA completion. Which statements are correct?

A. Pinning the frame until completion can prevent reuse during the transfer.
B. Keeping the process's virtual address unchanged alone guarantees that reuse is safe.
C. Reusing the frame can direct later DMA writes into another allocation.
D. The DMA device automatically follows any new page-table mapping under the stated model.

### Q60. [2 Marks] [NAT]

Let A=[[0,1],[−2,3]] and let v=(x,y)ᵀ satisfy x+y=6. The sequence A^n v must remain bounded as n tends to infinity. What is x?

**Answer format:** Exact number.

### Q61. [2 Marks] [MSQ]

Grammar S→aSa | bSb | a | b is over{a,b}. Which statements are correct?

A. Every generated string is an odd-length palindrome.
B. The grammar generates ε.
C. Reversing a generated string always gives a generated string.
D. The language is closed under concatenation.

### Q62. [2 Marks] [NAT]

A PDA has one control state and initial stack containing one X. Reading a replaces a top X by XX; reading b pops one X. There are no epsilon moves and no transition when the stack is empty. It accepts when the whole input is consumed and the stack is empty. How many words of length5 over{a,b} are accepted?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

On the interval[−2,2], how many distinct x values attain the global maximum of |x³−3x|?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A CRC uses generator g(x)=x²+x+1 over GF(2). A seven-bit frame suffers exactly two distinct bit flips, at positions chosen from0 through6. How many unordered position pairs produce an undetected error?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A direct-mapped cache has four sets and two-word blocks. A four-row matrix stores four data words per row, followed by p padding words per row. The matrix starts at word address0, and each row must begin at an even word address. What is the smallest nonnegative p making the first data words of the four rows map to four different cache sets?

**Answer format:** Integer words.



---

## ANSWER KEY — MOCK TEST 031

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C |
| 2 | NAT | 1 | 2 |
| 3 | NAT | 1 | 4 |
| 4 | NAT | 1 | 20 |
| 5 | MCQ | 1 | D |
| 6 | NAT | 2 | 28.5714 (accepted range 28.57135–28.57145) |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 5 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 12 |
| 11 | MCQ | 1 | D |
| 12 | MCQ | 1 | C |
| 13 | NAT | 1 | 11 |
| 14 | MCQ | 1 | A |
| 15 | MSQ | 1 | A, D |
| 16 | NAT | 1 | 9 |
| 17 | MCQ | 1 | B |
| 18 | NAT | 1 | 3 |
| 19 | MCQ | 1 | A |
| 20 | NAT | 1 | 3 |
| 21 | NAT | 1 | 9 |
| 22 | NAT | 1 | 5 |
| 23 | MSQ | 1 | A, C |
| 24 | MCQ | 1 | D |
| 25 | NAT | 1 | -4 |
| 26 | MCQ | 1 | C |
| 27 | NAT | 1 | 7 |
| 28 | MCQ | 1 | A |
| 29 | MCQ | 1 | B |
| 30 | MSQ | 1 | A, B |
| 31 | NAT | 1 | 14 |
| 32 | NAT | 1 | 6 |
| 33 | MCQ | 1 | C |
| 34 | NAT | 1 | 16 |
| 35 | MSQ | 1 | A, C |
| 36 | MSQ | 2 | A, B |
| 37 | NAT | 2 | 122 |
| 38 | MSQ | 2 | A, C |
| 39 | MSQ | 2 | A, C, D |
| 40 | MSQ | 2 | A, C |
| 41 | NAT | 2 | 2 |
| 42 | NAT | 2 | 7 |
| 43 | NAT | 2 | -2 |
| 44 | MSQ | 2 | A, C |
| 45 | MCQ | 2 | D |
| 46 | MCQ | 2 | B |
| 47 | MSQ | 2 | A, B |
| 48 | MSQ | 2 | A, C |
| 49 | MSQ | 2 | A, D |
| 50 | NAT | 2 | 35 |
| 51 | NAT | 2 | 200 |
| 52 | NAT | 2 | 3 |
| 53 | MSQ | 2 | A, C |
| 54 | MSQ | 2 | A, C |
| 55 | NAT | 2 | 8 |
| 56 | MCQ | 2 | A |
| 57 | NAT | 2 | 1601 |
| 58 | MSQ | 2 | A, B, D |
| 59 | MSQ | 2 | A, C |
| 60 | NAT | 2 | 3 |
| 61 | MSQ | 2 | A, C |
| 62 | NAT | 2 | 2 |
| 63 | NAT | 2 | 4 |
| 64 | NAT | 2 | 5 |
| 65 | NAT | 2 | 2 |
