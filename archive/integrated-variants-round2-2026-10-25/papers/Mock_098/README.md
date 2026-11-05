# GATE CS 2027 — Full-Length Mock Test 098

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

The reviewer gave the proposal a “qualified endorsement”: she supported its objective but required a smaller pilot before implementation. In this context, “qualified” most nearly means:

A. supported without any reservations  
B. conditional on stated reservations  
C. written by a certified professional  
D. withdrawn after reconsideration

### Q2. [1 Mark] [NAT]

A positive real number x satisfies log₂x + log₄x = 9. Find x.

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A rule is claimed for every positive integer n: if n leaves remainder1 upon division by3, then n² leaves remainder1 upon division by3. Which observations are logically valid?

**Candidates**

**I.** Writing n=3k+1 and expanding its square proves the claim for all eligible n.

**II.** Checking n=1,4,7 proves the universal claim without any further argument.

**III.** A number with remainder2 can also have a square with remainder1.

**IV.** The converse follows solely because the forward implication holds.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q4. [1 Mark] [NAT]

A 3×5 rectangular grid of unit squares is rotated 180 degrees about its centre. How many unit squares map onto themselves as sets?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

Let a(n) be the largest exponent k such that2^k divides n!. What is a(16)−a(15)?

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

A triangle has vertices A=(0,8),B=(−6,0),C=(6,0). Its orthocentre H is the intersection of its altitude lines. What is the y-coordinate of H?

**Answer format:** Exact decimal.

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that clearly states that the engineer inspected the bridge, found cracks, and then recommended closure, without assigning an action to an inappropriate subject.

A. Having inspected the bridge, cracks prompted the engineer to recommend closure.  
B. Having inspected the bridge and found cracks, the engineer recommended closure.  
C. Having been inspected by the engineer, closure was recommended by cracks.  
D. The bridge inspected the engineer, who recommended closure after finding cracks.

### Q8. [2 Marks] [NAT]

Every item in a batch costs a retailer ₹80, and the listed selling price is ₹100. The retailer sells three-fifths of the batch at the listed price, then sells all remaining items at one discounted price. The overall profit is 12.5% of the batch's total cost. What percentage discount from the listed price was used for the remaining items? Ignore taxes and other costs.

**Answer format:** Exact integer.

### Q9. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Exactly two of boxes A,B,C,D contain prizes. Four labels state: A, “Exactly one of A and B contains a prize”; B, “C contains a prize”; C, “D contains no prize”; D, “A contains a prize.” Exactly two labels are true. Which conclusions necessarily follow?

**Candidates**

**I.** A contains a prize.

**II.** B contains a prize.

**III.** C contains no prize.

**IV.** D contains no prize.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q10. [2 Marks] [NAT]

A square has vertices(0,0),(2,0),(2,2),(0,2). It is rotated90 degrees anticlockwise about(1,1) and then translated by(3,−1). What is the sum of the x-coordinates of its four resulting vertices?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An IPv4 packet carrying a TCP segment crosses one router between two Ethernet LANs. The router performs ordinary forwarding, with no NAT, fragmentation or tunnelling. Its incoming TTL is greater than 1. Which statements are correct about the outgoing packet/frame?

**Candidates**

**I.** The destination IPv4 address is unchanged.

**II.** The destination Ethernet address must be unchanged.

**III.** The IPv4 TTL is one less than on arrival.

**IV.** The TCP destination port is replaced by the router's port number.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q12. [1 Mark] [NAT]

A matrix has Doolittle factorization A=LU with diagonal entries of L all one and diagonal entries of U equal to 2,−3,4. No row permutation is used. Find det(A).

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A paging system uses 4 KiB pages. A process requires 9,000 bytes of contiguous virtual storage starting at a page boundary. How many bytes of internal fragmentation are present in its allocated final page if all required pages are allocated?

**Answer format:** Integer bytes; 1 KiB=1024 bytes.

### Q14. [1 Mark] [NAT]

Let f be integrable on[0,1] and satisfy f(x)+f(1−x)=6 for every x. What is its integral over[0,1]?

**Answer format:** Exact number.

### Q15. [1 Mark] [NAT]

A link sends packets of1000 payload bits plus a100-bit header at1100 bits per millisecond. Packets are continuously available and there are no other delays or losses. What payload throughput, in bits per millisecond, is achieved?

**Answer format:** Exact number.

### Q16. [1 Mark] [NAT]

In a pumping-lemma argument for L={a^n b^m : n,m≥0 and n≠m}, consider z=a³b⁹ and every decomposition z=uvw satisfying |uv|≤3 and |v|≥1. For each decomposition, choose an integer i≥0 such that uv^i w has equally many a's and b's. What is the largest i required among these decompositions?

**Answer format:** Exact integer.

### Q17. [1 Mark] [MCQ]

A transfer transaction subtracts from one account but crashes before adding to the other. Recovery leaves the subtraction permanent while undoing no part and completing no addition. Which transaction property is directly broken?

A. Atomicity.
B. A requirement that all transactions be read-only.
C. A requirement that every table contain one row.
D. No property because part of the transaction succeeded.

### Q18. [1 Mark] [NAT]

Five observations are 2,4,x,8,11, and their arithmetic mean is 6. What is their median?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

Binary search on a sorted array of length 15 chooses the lower midpoint of the current inclusive interval and compares the target once to that entry. What is the maximum number of such comparisons for a successful search?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

A byte-addressed machine executes a 4-byte load instruction beginning at address 100. Its indirect PC-relative mode first sign-extends an 8-bit displacement, multiplies that signed displacement by 4, and adds it to the address immediately after the instruction. The 32-bit word at this intermediate address is the effective address of the operand. The displacement bits are 11111010. Memory words M[80]=120 and M[120]=7 are given. What is the effective address of the operand? All addresses are decimal; the machine uses two's-complement displacements.

**Answer format:** Numeric value; integer.

### Q21. [1 Mark] [NAT]

A Boolean function of five variables is independent of its fifth variable and is 1 on exactly six assignments of the first four variables. On how many full five-variable assignments is it 1?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

In C, int a[2][3]={{1,2,3},{4,5,6}}; int (*p)[3]=a; is followed by p++;. What is (*p)[1]+p[-1][2]? All accesses are valid.

**Answer format:** Integer.

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Integer division discards the fractional part. What sequence is printed by visit(4)?

```text
visit(n):
    if n == 0: return
    visit(n / 2)
    print(n)
    visit((n - 1) / 2)
```

A. 1,2,1,4  
B. 1,2,4,1  
C. 4,2,1,1  
D. 1,2,3,4

### Q24. [1 Mark] [NAT]

How many group homomorphisms exist from the additive group Z12 to the additive group Z18?

**Answer format:** Integer.

### Q25. [1 Mark] [MCQ]

A B+ tree leaf stores at most four keys. An insertion gives the sorted leaf [4,7,9,12,15]. The split rule keeps the first three keys in the left leaf and the final two in the right leaf; it copies the smallest key in the right leaf into the parent. Which key is copied?

A. 9
B. 12
C. 7
D. 15

### Q26. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The input consists of a deterministic Turing machine M, a finite word w, and a nonnegative integer k. Which questions are decidable?

**Candidates**

**I.** Does M halt on w within k transitions?

**II.** Does M ever halt on w?

**III.** Does M enter an accepting state during its first k transitions, including its initial configuration?

**IV.** Is the language accepted by M empty?

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q27. [1 Mark] [MSQ]

T1 writes x. Before T1 commits, T2 reads that written value and then commits. T1 later aborts. Which statements are correct?

A. T2 performed a dirty read.
B. This schedule is recoverable.
C. T2 committed based on a value later rolled back.
D. The schedule is strict.

### Q28. [1 Mark] [MCQ]

A synchronous three-bit binary counter has next-state equations q0′=NOT q0, q1′=q1 XOR q0, q2′=q2 XOR (q1 AND q0). Starting in 011, what is its state after five clock edges?

A. 111
B. 000
C. 001
D. 101

### Q29. [1 Mark] [NAT]

Relations R(A)={1,2,3} and S(B)={x,y} use set semantics. How many tuples remain in their Cartesian product after removing every tuple whose A component equals 2?

**Answer format:** Integer.

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An arithmetic right shift by one on the signed value−7 produces floor(−7/2). Integer division by2 instead truncates toward zero. What is the shifted value minus the division result?

A. 0  
B. 1  
C. −7  
D. −1

### Q31. [1 Mark] [MCQ]

An open-addressed hash table uses linear probing and tombstones for deletion. During insertion of key k, the first tombstone is encountered before an occupied slot containing k. Duplicate keys are forbidden. What must a correct insertion do?

A. Immediately place a second copy of k in the tombstone.
B. Treat the tombstone as proof that k is absent.
C. Stop searching at every tombstone as if it were never occupied.
D. Continue searching beyond the tombstone to detect the existing key before deciding to insert.

### Q32. [1 Mark] [NAT]

The set {1,2,3,4,5,6} is partially ordered by divisibility. What is the largest possible size of an antichain, a subset in which no two distinct elements divide one another?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

B is a 3×4 array of four-byte elements stored in row-major order, with B[0][0] at byte address 1000. A transposed view C is defined by C[i][j]=B[j][i], without copying any elements. What is address(C[1][2])−address(C[0][1]), in bytes?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

For Boolean variables a,b,c, let f(a,b,c)=(a AND b) XOR ((NOT a) AND c). For how many assignments of(b,c) does flipping a change f, regardless of a's initial value?

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For production S→ABC, which proposed inherited-attribute dependency violates the left-to-right dependency restriction of an L-attributed definition?

A. A.in depends on C.out.  
B. B.in depends on A.out.  
C. C.in depends on B.out.  
D. A.in depends on S.in.

### Q36. [2 Marks] [NAT]

A microinstruction has 16 independent control bits, a field selecting one of eight branch conditions, and two absolute next-address fields for true and false outcomes. The control store holds 256 microinstructions. With fixed-width fields and no shared encoding, how many bits does one microinstruction require?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

A transaction's lock sequence is lock-S(A), lock-X(B), unlock-S(A), lock-S(C), commit, unlock-X(B), unlock-S(C). Use basic two-phase locking to mean that no new lock is acquired after the first unlock. Use strictness to mean that exclusive locks are held until commit or abort. Which statements are correct?

A. The sequence violates basic two-phase locking.
B. The sequence obeys basic two-phase locking because X(B) is held until commit.
C. Its exclusive-lock release satisfies the specified strictness condition.
D. Holding X(B) until commit repairs every possible two-phase-locking violation automatically.

### Q38. [2 Marks] [MSQ]

On a Unix-style file system, an ordinary file has two hard-link names and an open descriptor. Both names are unlinked, but the descriptor remains open and has suitable access permission. No other references exist. Which statements are correct?

A. Reading the file's data through the open descriptor remains possible.  
B. The file's data blocks must be freed immediately after the second unlink.  
C. Opening either removed pathname fails unless a new directory entry is created there.  
D. The inode's hard-link count remains 1 because an open descriptor is a hard link.

### Q39. [2 Marks] [MCQ]

The following pseudocode uses static (lexical) scoping and ordinary stack activation records. Main contains A; A contains the sibling procedures B and C. Each call has fresh local variables, assignments to a variable found in an enclosing activation modify that variable, and the two assignments in the recursive case of B execute in their displayed order.
```text
procedure Main():
    local x = 20
    procedure A():
        local x = 4
        procedure C():
            x = x + 1
            return x
        procedure B(n):
            local x = 100 + n
            if n == 0:
                return C()
            t = B(n-1)
            u = C()
            return t + u
        return B(2)
    print A()
```
Here t and u are local temporaries of each B activation. What is printed?

A. 18  
B. 306  
C. 15  
D. 66

### Q40. [2 Marks] [NAT]

A synchronous three-bit shift register has next-state equations q2′=q1, q1′=q0, q0′=q2 XOR q0. Starting in state q2q1q0=001, after how many clock edges does it first return to 001?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

A systematic CRC encoder uses generator polynomial x³+x+1, represented by 1011. For data bits 1101, append three zeros and divide by 1011 over GF(2). Interpret the three-bit remainder as an unsigned integer. What is that integer?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Consider a CFG with start S and productions S→AB | C, A→aA | a, B→bB, C→cC | ε, D→d. A useful nonterminal must occur in some derivation from S that ends in a terminal string. Which statements are correct?

A. The generated language is c*.
B. A is useful because it is reachable from S and generates terminal strings.
C. Exactly two nonterminals are useful.
D. D is useful because it generates d.

### Q43. [2 Marks] [NAT]

A process opens the same regular file twice in two separate successful open calls, obtaining descriptors p and q. No append mode is used. It reads4 bytes through p, seeks q to absolute offset7, then reads2 bytes through p. All reads succeed fully. What is the sum of the file offsets associated with p and q afterward?

**Answer format:** Integer.

### Q44. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A singly linked list is acyclic. A pointer p identifies a non-tail node, but the predecessor of p is unavailable. A proposed deletion copies the successor's value into p and bypasses that successor. Which statements are correct?

A. The resulting value sequence matches deleting p's original value at that position.  
B. The operation preserves the identity of every node that ordinary deletion of p would preserve.  
C. It requires p to have a successor under the stated implementation.  
D. External references to node identities can make this different from actually deleting node p.

### Q45. [2 Marks] [NAT]

How many permutations of {1,2,3,4,5} place1 before2 before3, with no restriction on the relative positions of4 and5?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A Boolean minimization problem has prime implicants P,Q,R,S. Their covered required minterms and literal costs are:

| Implicant | Covered minterms | Literal cost |
|---|---|---:|
| P | 0,1,2 | 3 |
| Q | 2,3 | 2 |
| R | 0,3 | 2 |
| S | 1,2 | 2 |

All required minterms are0,1,2,3. A cover may use only these implicants. What is the minimum total literal cost of a cover?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A byte-addressed 16-bit system selects one 4 KiB memory chip whenever address bits A15A14 equal 10. The chip uses A11…A0 as its local address, and A13,A12 are not decoded. How many distinct physical bytes are accessible in the selected 16 KiB address window?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Define MUX(s,u,v) to return u when s=0 and v when s=1. A circuit computes T=MUX(s,a,b), then F=MUX(T,s,NOT s). Which statements are correct?

A. F=(NOT s AND a) OR (s AND NOT b).  
B. If a=b, toggling s toggles F.  
C. If a and b differ, F is independent of s.  
D. F always equals s XOR a XOR b.

### Q49. [2 Marks] [NAT]

A queue is implemented using two stacks. Enqueue pushes onto input stack I. Dequeue pops from output stack O; if O is empty, it first transfers every element of I to O, one pop and one push per transferred element. Starting empty, execute enqueue(a), enqueue(b), dequeue, enqueue(c), dequeue, dequeue. How many primitive stack pushes and pops are performed in total?

**Answer format:** Exact integer.

### Q50. [2 Marks] [NAT]

An insertion-sort implementation counts only comparisons between keys inside the shifting loop. It scans left while the preceding key is strictly greater than the inserted key, stopping at the first non-greater key or the array boundary. On input [5,1,4,2,3], how many key comparisons occur? Index-boundary tests are not key comparisons.

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In the interval-scheduling problem, intervals are half-open and all have equal value. Which statements are correct about choosing a compatible interval with earliest finishing time at each step?

**Candidates**

**I.** An exchange argument can replace the first interval of an optimal solution by an earliest-finishing interval without reducing the number still schedulable afterward.

**II.** The same rule necessarily maximizes total value when intervals have arbitrary positive weights.

**III.** Half-open intervals ending and starting at the same time are compatible.

**IV.** Choosing the longest interval first is always equivalent to earliest finish.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q52. [2 Marks] [NAT]

Let en count ordered compositions of n into parts 1 and 3 with an even number of parts equal to 3; the empty composition contributes e0=1. Odd numbers of 3-parts are excluded. What is the coefficient of x10 in E(x)=Σ(n≥0) en x^n?

**Answer format:** Exact integer.

### Q53. [2 Marks] [NAT]

Partition this three-address code into maximal basic blocks using the usual leader rules. Count distinct directed edges between the resulting blocks, including both outcomes of conditional branches. There are no exceptional-control-flow edges.

```text
1: i = 0
2: if i >= n goto 9
3: if a[i] < 0 goto 7
4: s = s + a[i]
5: i = i + 1
6: goto 2
7: i = i + 2
8: goto 2
9: return s
```

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

How many truth assignments to propositions p,q,r,s satisfy all three conditions: p implies q, r implies q, and s is true exactly when p and r have different truth values?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A hypothetical CSMA/CD link transmits at 100 million bits per second with a minimum frame of 512 bits. Signal propagation speed in the cable is 200 million metres per second. In addition to cable propagation, devices introduce 0.4 microseconds of delay in each direction. Requiring the minimum-frame transmission time to be at least the worst-case round-trip delay, what is the maximum cable length in metres?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

A rooted tree has root r with children a,b. Node a has children c,d, and b has child e; c,d,e are leaves. A vertex's depth is its edge distance from the root. If the same undirected tree is rerooted at c, by how much does the sum of all six vertex depths increase?

**Answer format:** Exact integer.

### Q57. [2 Marks] [NAT]

A distance-vector router has neighbours A and B with link costs2 and5. Their advertised distances to destination d are7 and3 respectively. No other routes exist. What distance does the router select?

**Answer format:** Integer.

### Q58. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For real t consider

```text
x1 + x2 + x3 = 1
x1 + 2x2 + 3x3 = 2
2x1 + 3x2 + 4x3 = t
```

Which statements are correct?

A. The system is consistent exactly when t=3.  
B. When t=3, there are infinitely many solutions.  
C. Every solution satisfies x1=x3.  
D. When t=3, the coefficient matrix is invertible.

### Q59. [2 Marks] [NAT]

Four memory banks are selected by word address modulo 4. Each request occupies its bank for 3 cycles; a bank accepting a request at cycle t is available again at t+3. The controller issues at most one request per cycle, in the listed order, and stalls if the next request's bank is busy. Initially all banks are idle. For word addresses 0,4,1,5,2,6,3,7, with the first issue at cycle 0, at what cycle does the last request finish?

**Answer format:** Integer cycle number.

### Q60. [2 Marks] [NAT]

Grammar S→aSbS | bSaS | ε generates equal numbers of a and b. How many distinct strings of length four does it generate? Count strings, not parse trees.

**Answer format:** Integer.

### Q61. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In an expression language, evaluating an operand may have side effects; && and || evaluate left to right and short-circuit. Values are Boolean. Which rewrites preserve both returned value and operand side effects in every execution?

**Candidates**

**I.** false && f() → false

**II.** f() && false → false

**III.** true || f() → true

**IV.** f() || true → true

A. II and IV  
B. I and III  
C. III and IV  
D. I and II

### Q62. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A nondeterministic PDA recognizes even-length palindromes over {a,b} by pushing an initial segment, guessing its midpoint using an epsilon transition, and then matching and popping the remaining symbols; it accepts only after consuming all input and returning to its bottom marker. Which statements are correct?

**Candidates**

**I.** Any accepting computation on abba must guess the midpoint after two input symbols.

**II.** Guessing the midpoint after one input symbol can accept abba by ignoring a mismatched stack symbol.

**III.** The word abab is rejected on every computation.

**IV.** An incorrect midpoint guess must make every computation on an actual palindrome reject.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q63. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An ER model has entity Building with key building_id and weak entity Room with partial key room_no. Each Room belongs to exactly one Building; room_no is unique within a building but may repeat across buildings. Which statements are correct for the relational mapping?

A. The pair(building_id,room_no) can identify Room rows.  
B. room_no alone is necessarily a candidate key of Room.  
C. A non-null foreign key from Room.building_id to Building implements the required owner reference, together with the appropriate Room key.  
D. Removing building_id from Room loses information needed to distinguish equally numbered rooms in different buildings.

### Q64. [2 Marks] [NAT]

Relation E(src,dst) is{(a,b),(b,c),(c,a),(a,c)}. Let P contain all pairs(x,z) for which some y satisfies E(x,y) and E(y,z), using set semantics. How many pairs belong to P−E?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Matrices A,B,C have dimensions10×2,2×20,20×3. Scalar multiplication count for multiplying an r×s matrix by an s×t matrix is rst. How many scalar multiplications are saved by choosing the cheaper parenthesization of ABC instead of the more expensive one?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 098

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 64 |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 1 |
| 5 | NAT | 1 | 4 |
| 6 | NAT | 2 | 4.5 |
| 7 | MSQ | 2 | A, C, D |
| 8 | NAT | 2 | 25 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 16 |
| 11 | MCQ | 1 | A |
| 12 | NAT | 1 | -24 |
| 13 | NAT | 1 | 3288 |
| 14 | NAT | 1 | 3 |
| 15 | NAT | 1 | 1000 |
| 16 | NAT | 1 | 7 |
| 17 | MCQ | 1 | A |
| 18 | NAT | 1 | 5 |
| 19 | NAT | 1 | 4 |
| 20 | NAT | 1 | 120 (exact) |
| 21 | NAT | 1 | 12 |
| 22 | NAT | 1 | 8 |
| 23 | MSQ | 1 | A, C, D |
| 24 | NAT | 1 | 6 |
| 25 | MCQ | 1 | B |
| 26 | MCQ | 1 | C |
| 27 | MSQ | 1 | A, C |
| 28 | MCQ | 1 | B |
| 29 | NAT | 1 | 4 |
| 30 | MSQ | 1 | A, B, C |
| 31 | MCQ | 1 | D |
| 32 | NAT | 1 | 3 |
| 33 | NAT | 1 | 20 (exact) |
| 34 | NAT | 1 | 2 |
| 35 | MSQ | 1 | B, C, D |
| 36 | NAT | 2 | 35 |
| 37 | MSQ | 2 | A, C |
| 38 | MSQ | 2 | A, C |
| 39 | MCQ | 2 | A |
| 40 | NAT | 2 | 7 |
| 41 | NAT | 2 | 1 |
| 42 | MSQ | 2 | A, C |
| 43 | NAT | 2 | 13 |
| 44 | MCQ | 2 | B |
| 45 | NAT | 2 | 20 |
| 46 | NAT | 2 | 4 |
| 47 | NAT | 2 | 4096 (exact) |
| 48 | MCQ | 2 | D |
| 49 | NAT | 2 | 12 |
| 50 | NAT | 2 | 9 |
| 51 | MCQ | 2 | D |
| 52 | NAT | 2 | 16 |
| 53 | NAT | 2 | 7 |
| 54 | NAT | 2 | 5 |
| 55 | NAT | 2 | 432 |
| 56 | NAT | 2 | 4 |
| 57 | NAT | 2 | 8 |
| 58 | MCQ | 2 | D |
| 59 | NAT | 2 | 18 |
| 60 | NAT | 2 | 6 |
| 61 | MCQ | 2 | B |
| 62 | MCQ | 2 | C |
| 63 | MCQ | 2 | B |
| 64 | NAT | 2 | 4 |
| 65 | NAT | 2 | 820 |
