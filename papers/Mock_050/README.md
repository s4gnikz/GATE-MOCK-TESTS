# GATE CS 2027 — Full-Length Mock Test 050

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

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The reviewer gave the proposal a “qualified endorsement”: she supported its objective but required a smaller pilot before implementation. In this context, “qualified” most nearly means:

A. supported without any reservations  
B. conditional on stated reservations  
C. written by a certified professional  
D. withdrawn after reconsideration

### Q2. [1 Mark] [NAT]

What is the largest nonnegative integer n such that 2ⁿ divides 12! exactly?

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A screening procedure flags an item whenever its measured value exceeds a threshold. Raising that threshold while leaving all measurements unchanged can have which effect on the set of flagged items?

A. It can only stay the same or become a subset of its former set.  
B. It must strictly increase.  
C. Every formerly unflagged item must become flagged.  
D. It must become empty regardless of the measurements.

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A solid cube is made from27 identical unit cubes arranged3×3×3. Remove the central unit cube from each of the six outer faces, and also remove the central unit cube of the solid. All seven removed cubes are distinct. How many exposed unit-square faces belong to the remaining solid, counting newly exposed internal surfaces?

**Required precision:** Exact integer.

A. 144  
B. 72  
C. 36  
D. 73

### Q5. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A sequence starts with 3. To obtain successive terms, alternately multiply by 2 and subtract 1, starting with multiplication. What is its seventh term?

**Required precision:** Integer.

A. 34  
B. 9  
C. 18  
D. 17

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Eight people are arranged uniformly at random in a circle. Rotations are treated as the same arrangement. What is the probability that two specified people sit adjacent? Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.2857  
B. 0.7143  
C. 0.1429  
D. 0.6429

### Q7. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Choose the sentence that clearly states that the engineer inspected the bridge, found cracks, and then recommended closure, without assigning an action to an inappropriate subject.

**Candidate answers**
I. Having inspected the bridge, cracks prompted the engineer to recommend closure.
II. Having inspected the bridge and found cracks, the engineer recommended closure.
III. Having been inspected by the engineer, closure was recommended by cracks.
IV. The bridge inspected the engineer, who recommended closure after finding cracks.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q8. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A well-mixed tank contains 10 litres of a 30% salt solution by volume. Two litres are removed and replaced by two litres of pure water. After thorough mixing, the operation is repeated once. What is the final salt percentage? Volumes are additive.

**Required precision:** Exact finite decimal percentage, without the percent sign.

A. 19.2  
B. 38.4  
C. 9.6  
D. 20.2

### Q9. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A product's price is increased by 20%. It is then reduced by a percentage r of the increased price so that the final price is 10% below the original price. Find r.

**Required precision:** Integer percentage.

A. 50  
B. 25  
C. 13  
D. 26

### Q10. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

On a Cartesian plane, operation R rotates a point90 degrees anticlockwise about the origin, and operation M reflects a point in the vertical line x=1. Starting at(2,1), perform R followed by M repeatedly. Where is the point after four such pairs of operations?

**Candidate answers**
I. (2,1)
II. (6,5)
III. (-2,-1)
IV. (0,3)

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An array-based binary min-heap is [2,7,4,12,9,6,5], using one-based indices. Delete the minimum by moving the last element to the root and repeatedly exchanging it with its smaller child until the heap property holds. What is the sum of the values at indices2 and3 afterward?

**Required precision:** Integer.

A. 24  
B. 6  
C. 13  
D. 12

### Q12. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A NAT keeps an expiring UDP mapping from an internal endpoint to a public endpoint. After it expires, the same public endpoint is assigned to a different internal endpoint. A delayed incoming datagram addressed to the reused public endpoint then arrives. Assume mapping lookup uses only the destination public endpoint. Which statement is correct?

**Candidate answers**
I. The datagram necessarily reaches the original internal endpoint.
II. The NAT can deliver it to the newly mapped endpoint because the datagram carries no mapping-generation identifier used by this lookup.
III. UDP sequence numbers universally prevent this.
IV. The mapping can never expire while datagrams are delayed.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q13. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let U be an undecidable but recognizable language. Which statements are correct?

**Candidates**

**I.** U's complement cannot also be recognizable.

**II.** U must be infinite.

**III.** Every subset of U is recognizable.

**IV.** U cannot contain any decidable infinite subset.

A. I and II  
B. III and IV  
C. I and III  
D. I and IV

### Q14. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Use set semantics. R(A,B)={(1,x),(1,y),(2,x)} and S(B)={(x),(y)}. Define

`E = projection_A(R) - projection_A((projection_A(R) x S) - R)`

where x is Cartesian product and - is set difference. Which statements are correct? Each proposed change is applied independently to the original relations.

**Candidate answers**
I. For the original relations, E={(1)}.
II. If S is empty, E={(1),(2)}.
III. If (2,y) is added to R, E remains {(1)}.
IV. If (z) is added to S, E is empty.

A. I: valid; II: valid; III: invalid; IV: valid  
B. I: invalid; II: valid; III: invalid; IV: valid  
C. I: valid; II: valid; III: valid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A matrix has Doolittle factorization A=LU with diagonal entries of L all one and diagonal entries of U equal to 2,−3,4. No row permutation is used. Find det(A).

**Required precision:** Integer.

A. -24  
B. -48  
C. -12  
D. -23

### Q16. [1 Mark] [NAT]

R(x,y) contains (1,a),(1,b),(2,a),(3,c), and S contains a,b. Over these domains, how many x values satisfy `(∃y R(x,y)) AND (∀z (R(x,z) → S(z)))`?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Let f be continuous on[0,1], and define F(x)=the integral of f(t) from0 to x. If f(x)=2x and F(0)=0, what is the integral of F(x) from0 to1?

**Required precision:** Decimal rounded to four places.

A. 0.6667  
B. 0.3333  
C. 0.1667  
D. 0.2500

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An unsigned fixed-point format uses six bits with a scale factor of 1/8: the stored unsigned integer k represents k/8. Addition wraps modulo 64 in the stored integer. What numerical value is stored after adding the encodings of 5.75 and 3.5?

**Required precision:** Exact decimal.

A. 1.25  
B. 2.50  
C. 0.63  
D. 2.25

### Q19. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

On an eight-bit two's-complement machine, x has bits 11111011. Define arithmetic right shift as copying the sign bit and logical right shift as inserting zero. What signed values result from one arithmetic right shift and one logical right shift, respectively?

**Candidate answers**
I. −2 and 125
II. −3 and 125
III. −3 and −3
IV. −2 and −2

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q20. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A process with three private writable pages forks using copy-on-write. Initially all three physical pages are shared between parent and child. The parent writes page 0, the child writes page 1, and the parent writes page 0 again. Neither process exits. A first write to a shared page makes one physical copy; a write to an exclusively owned page makes none. How many physical pages now hold these processes' three logical pages each?

**Required precision:** Integer.

A. 5  
B. 10  
C. 3  
D. 6

### Q21. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A TCP sender's next unsent byte has sequence number5000. It receives a cumulative ACK with acknowledgment number4200 and advertised window600 bytes. Assume no sequence-number wraparound and that the congestion window imposes no tighter restriction. How many new bytes may it send immediately, without retransmitting already sent bytes?

**Required precision:** Exact integer.

A. 1  
B. 0  
C. 2  
D. 3

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP server has a listening socket l. A successful accept(l) returns connected socket c. Which statement is correct?

A. The listening socket becomes c and can no longer accept connections.  
B. Every write to l broadcasts data to all accepted clients.  
C. Closing c necessarily closes l.  
D. l can continue accepting other connections while c serves the accepted connection.

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An optimizer considers reusing a+b across a function call. Arithmetic is exact. Which conditions are sufficient for this reuse to preserve the expression value?

A. a and b are unchanged local scalars whose addresses have never escaped, and the called function has no access to them.  
B. a and b are mutable globals, and the function's effects are unknown.  
C. The function is proven not to modify either operand, directly or indirectly.  
D. The expression text is identical before and after the call, regardless of side effects.

### Q24. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Five nonnegative real observations have total 20. What is the greatest possible median? Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 13.3334  
B. 3.3334  
C. 6.6667  
D. 7.6667

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a directed weighted graph, a negative-weight cycle is reachable from s but no vertex on that cycle can reach t. A path from s to t exists. Which statements are correct?

**Candidates**

**I.** A finite shortest s-to-t distance can still exist.

**II.** Every reachable vertex necessarily has distance minus infinity.

**III.** Repeating that cycle cannot produce arbitrarily cheap s-to-t walks under the stated reachability condition.

**IV.** The mere existence of that cycle implies no s-to-t path exists.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q26. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

What integer is printed by this conforming C program?

```c
#include <stdio.h>
struct S { int a[2]; int *p; };
int main(void) {
    struct S s = {{1,2}, 0};
    s.p = s.a;
    struct S t = s;
    t.a[0] = 7;
    *t.p = 9;
    printf("%d\n", s.a[0] + t.a[0]);
    return 0;
}
```

**Required precision:** Integer.

A. 32  
B. 8  
C. 16  
D. 17

### Q27. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An application sends 2400 bytes using three UDP datagrams, each with 800 application bytes. Each datagram adds an 8-byte UDP header and a 20-byte IPv4 header. No fragmentation occurs. How many total IPv4 bytes are transmitted?

**Required precision:** Integer.

A. 2484  
B. 4968  
C. 1242  
D. 2485

### Q28. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A stable sorting algorithm sorts records by a numeric key. Which statements are correct?

**Candidates**

**I.** Equal-key records retain their relative input order.

**II.** Stability alone guarantees O(n log n) running time.

**III.** Stability matters when a previous ordering among equal keys must be preserved.

**IV.** A stable sort necessarily leaves all unequal-key records in their original relative order.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q29. [1 Mark] [MCQ]

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

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

On the set of residues {0,1,2,3,4} modulo 5, define permutations f(x)=2x mod 5 and g(x)=(x+1) mod 5. Let h=f composed with g composed with f-inverse composed with g-inverse; the rightmost map acts first. What is the smallest positive integer k for which h applied k times is the identity?

A. 1  
B. 2  
C. 4  
D. 5

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

For grammar S→aSb | SS | ε, what is the minimum number of applications of S→aSb needed in any derivation of aabbab?

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q32. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A parent creates a pipe and forks two children, both inheriting both pipe ends. The parent closes its write end and reads. Child I writes a finite message and closes both ends. Child II closes its read end but keeps its write end open indefinitely without writing. After consuming Child I's entire message, what happens to the parent's next blocking read, assuming no signals or errors?

**Candidate answers**
I. It immediately returns end-of-file because Child I finished.
II. It blocks because a write end remains open.
III. It returns the last byte repeatedly.
IV. It necessarily raises a broken-pipe error.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q33. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A bipartite graph has left vertices a,b,c,d and right vertices 1,2,3,4. Each of a,b,c is adjacent exactly to 1 and 2; d is adjacent exactly to 3 and 4. What is the maximum matching size?

**Required precision:** Integer.

A. 6  
B. 3  
C. 2  
D. 4

### Q34. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A directed graph on n=6 vertices is represented by six adjacency lists. Self-loops are allowed, and no ordered pair occurs more than once. The sum of all outdegrees is11 and exactly three edges are self-loops. What is the sum of all indegrees?

**Required precision:** Integer.

A. 22  
B. 6  
C. 12  
D. 11

### Q35. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A byte-addressed 64 KiB memory is built from 16 KiB × 8-bit chips. Address lines not connected to a chip's internal address pins select the chip through a decoder. How many address bits are used for chip selection?

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean inputs x,y,z, a circuit outputs F=(x AND y) OR ((NOT x) AND z). Which statements hold?

A. Flipping x leaves F unchanged exactly when y=z.  
B. F equals (x OR z) AND ((NOT x) OR y).  
C. F is independent of z whenever y=1.  
D. When y=NOT z, F XOR z equals x.

### Q37. [2 Marks] [MSQ]

A linear-probing hash table uses EMPTY for never-used slots and DELETED for tombstones. Searches stop at EMPTY, but continue past DELETED. Which claims hold?

A. Replacing a deleted occupied slot by EMPTY can make another existing key unreachable by search.
B. An insertion can remember the first DELETED slot, continue searching for an existing copy of its key, then reuse that slot if the key is absent.
C. A search can always stop at DELETED because it no longer contains a key.
D. Tombstones can increase the number of probes in an unsuccessful search.

### Q38. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Use the standard SLR(1) construction for the augmented grammar below. How many LR(0) item-set states have a shift/reduce conflict in the resulting SLR table?

```text
S' -> S
S  -> A a | b A c | d c | b d a
A  -> d
```

A. 0  
B. 2  
C. 1  
D. 3

### Q39. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A syntax-directed translator emits postfix code for fully parenthesized binary expressions. It recursively emits the entire left operand, then the entire right operand, and finally the binary operator. The generated code is evaluated on an initially empty stack: an operand pushes one value, and an operator pops two values and pushes their result. No temporary storage other than this stack is used. What is the maximum stack depth reached when evaluating the translation of `(a+b)*(c+(d*e))`?

A. 4  
B. 8  
C. 2  
D. 5

### Q40. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A TCP sender learns that the path MTU is 1280 bytes and wishes to send full-sized IPv4 packets without fragmentation. IPv4 and TCP each use a 20-byte header, with no options or other encapsulation. The application has 3000 bytes ready. What is the payload size, in bytes, of the final packet when earlier packets use the maximum permitted payload?

**Required precision:** Integer.

A. 1040  
B. 260  
C. 520  
D. 521

### Q41. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A PDA has one control state and initial stack containing one X. Reading a replaces a top X by XX; reading b pops one X. There are no epsilon moves and no transition when the stack is empty. It accepts when the whole input is consumed and the stack is empty. How many words of length5 over{a,b} are accepted?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q42. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

SQL uses bag semantics and ordinary three-valued logic. T(k) has rows 1,1,NULL and U(k) has rows 1,NULL. How many rows does this query return?

```sql
SELECT T.k, U.k
FROM T LEFT JOIN U ON T.k = U.k
WHERE U.k IS NULL;
```

**Required precision:** Exact integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q43. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A language permits a function to return a nested function that refers to its local variable x. Two separate calls to the outer function return functions F and G, capturing different x variables. Both returned functions are called after the outer calls have returned. Which implementation preserves lexical scoping and separate mutable x variables?

**Candidate answers**
I. Put every captured x in the same global cell.
II. Keep each captured environment alive beyond the outer call and associate the appropriate environment with each returned function.
III. Keep only a pointer into the outer function's discarded stack frame.
IV. Copy the current value of x anew from the most recent caller whenever F or G is invoked.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q44. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An inclusive two-level cache requires every block in L1 also to be present in L2. An exclusive design instead requires blocks resident in L1 to be absent from L2. Ignore other cache levels. Which statements are correct?

**Candidate answers**
I. Evicting an L2 block in the inclusive design may require invalidating its L1 copy.
II. An inclusive L1 miss can never be an L2 hit.
III. The exclusive design permits the same block to remain simultaneously in both levels by definition.
IV. Replication in the inclusive design can reduce the number of distinct resident blocks compared with equal-capacity exclusive levels.

A. I: invalid; II: invalid; III: invalid; IV: valid  
B. I: valid; II: invalid; III: valid; IV: valid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: invalid; IV: valid

### Q45. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For variables a,b,c,d, f=1 exactly when a XOR b=1, independently of c,d. A conventional sum-of-products Karnaugh-map minimization uses cubes that do not cover a zero. Which statements are correct?

A. f has a two-product implementation (NOT a)b+a(NOT b).  
B. One product term is sufficient because eight of the sixteen inputs produce1.  
C. Each of the two displayed products covers four minterms.  
D. A valid product covering both(a,b)=(0,1) and(1,0) can omit both a and b without covering zeros.

### Q46. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A cache starts empty, has two sets with two ways each, and uses LRU within each set. Block b maps to set b modulo2. Compare reference sequences0,2,4,0,2,4 and0,3,6,0,3,6. Each reference accesses one block, and the cache is reset between sequences. How many more misses occur in the first sequence than in the second?

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q47. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Shared x initially equals0. Two threads each execute this sequence once, using the same binary semaphore mutex initially1:

```text
wait(mutex);
t = x;          // t is local to the thread
x = t + 1;
signal(mutex);
```

A third thread performs only wait(mutex); signal(mutex). All three threads finish successfully. How many distinct final values of x are possible?

**Required precision:** Exact integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q48. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A single resource type has R identical reusable instances. Three processes each need at most three instances in total, may request one at a time, never release before completion, and finish once their total demand is met. What is the smallest R that guarantees absence of resource deadlock for every allocation state consistent with these maximum demands? Scheduling fairness is not being asked about.

**Required precision:** Integer.

A. 14  
B. 7  
C. 4  
D. 8

### Q49. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A SQL table has nullable columns a,b, CHECK(a+b>0), UNIQUE(a,b), and a composite foreign key (a,b) with MATCH SIMPLE semantics. For this question, UNIQUE treats tuples containing NULL as distinct, CHECK rejects only FALSE, and MATCH SIMPLE skips the referenced-row check if any referencing column is NULL. The referenced table is empty. Which statements are true?

**Candidates**

**I.** Inserting (NULL,−5) can satisfy all these constraints.

**II.** CHECK(a+b>0) alone forces both columns to be non-null.

**III.** Two copies of (NULL,−5) can coexist under the specified UNIQUE semantics.

**IV.** Inserting (1,1) satisfies the foreign key despite the empty referenced table.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q50. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

How many distinct arrangements of AAABBBCCC have no two A symbols adjacent? Identical letters are indistinguishable.

**Required precision:** Integer.

A. 1400  
B. 700  
C. 350  
D. 701

### Q51. [2 Marks] [NAT]

A six-bit unsigned register x initially holds 45. One operation rotates its bits left by two positions within the six-bit word, then XORs the result with binary 001111. What decimal value results after two such operations?

**Answer format:** Integer.

### Q52. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A receiver expects byte 1000. Segments containing bytes 1100–1199,1200–1299,1300–1399 arrive before the segment containing 1000–1099. It immediately sends a cumulative ACK for each arrival and buffers out-of-order bytes. No bytes are lost. What ACK numbers are sent for these four arrivals in order?

**Candidate answers**
I. 1200,1300,1400,1100
II. 1000,1000,1000,1400
III. 1100,1200,1300,1400
IV. 1000,1100,1200,1300

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q53. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A sequence has a0=1 and an=sum(a_i for i=0,...,n−1) for n≥1. What is a6?

**Required precision:** Integer.

A. 64  
B. 32  
C. 16  
D. 33

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Three jobs arrive at times 0,1,2 with CPU bursts 7,4,1 respectively. A preemptive shortest-remaining-time scheduler breaks equal remaining-time ties by earlier arrival. Context switches cost zero. What is the total waiting time of the three jobs?

**Required precision:** Integer time units.

A. 6  
B. 12  
C. 3  
D. 7

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B,C,D) has dependency set F={AB→C, C→B, A→D, D→C}. Which statements are correct?

**Candidates**

**I.** AB→C can be removed without changing the closure of F.

**II.** C→B can be removed without changing the closure of F.

**III.** A is a candidate key of R.

**IV.** D is a candidate key of R.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

### Q56. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

During a 1000-cycle interval, a DMA controller steals one memory-bus cycle in every group of five cycles. A CPU instruction stream requires the bus every cycle and otherwise could complete one instruction per cycle. Assume a stolen cycle stalls exactly one instruction opportunity, with no other stalls. How many instructions complete during the interval?

**Required precision:** Integer.

A. 1600  
B. 400  
C. 800  
D. 801

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What pair of values is printed? Assume C integer arithmetic is exact for the values used.

```c
#include <stdio.h>
int main(void) {
    int a[] = {2,4,6,8};
    int *p = a + 1;
    int **q = &p;
    (*q)++;
    **q += *(p-1);
    printf("%d %d", a[2], (int)(p-a));
}
```

A. 6 1  
B. 10 1  
C. 10 2  
D. 12 2

### Q58. [2 Marks] [MSQ]

Consider the following algorithm, with n≥2 and a constant-time body that allocates no storage:

```text
for i = 1 to n:
    for j = i to n step i:
        body()
```

Which statements are correct?

A. The body executes exactly Σ(i=1..n) floor(n/i) times.
B. The running time is Θ(n log n).
C. The algorithm needs Θ(n) auxiliary words merely to execute these loops.
D. The body executes Θ(n²) times.

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

On domain D={1,2,3}, how many binary relations R satisfy (for every x there exists y with R(x,y)) but do not satisfy (there exists y such that R(x,y) for every x)?

**Required precision:** Integer.

A. 348  
B. 87  
C. 175  
D. 174

### Q60. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

L is context-free and R is regular. Which languages are necessarily context-free?

A. L∩R  
B. L∪R  
C. The complement of L  
D. The concatenation LR

### Q61. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

For the finite language L={ε,a,a²,…,a⁷}, what is the smallest positive pumping length p satisfying the regular-language pumping lemma? The lemma imposes its decomposition requirement only on words of length at least p.

**Candidate answers**
I. 8
II. 7
III. 1
IV. No pumping length exists because the language is finite.

A. I: valid; II: invalid; III: invalid; IV: invalid  
B. I: invalid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q62. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A global integer x initially equals zero. Run visit(3) below, with exact arithmetic. What is the sum of all printed integers?

```text
visit(n):
    if n == 0:
        print(x)
        return
    x = x+1
    visit(n-1)
    x = x-1
    visit(n-1)
```

**Required precision:** Integer.

A. 24  
B. 6  
C. 12  
D. 13

### Q63. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An array [a,b,c,d,e,f] is permuted in place by the index mapping i→(2i+1) modulo7, with indices restricted to0 through5. This mapping permutes those six indices. How many disjoint cycles does it contain?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q64. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A real matrix A has three columns. Its reduced row-echelon form has pivots in columns1 and3. The system Ax=b is consistent. Which statements are correct?

**Candidates**

**I.** There is exactly one free variable.

**II.** Every consistent right-hand side yields a unique solution.

**III.** The solution set is an affine line in R³.

**IV.** The nullspace has dimension2.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q65. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A 4000-byte message is divided into n equal-payload packets, each with an additional 100-byte header. Choose n among the positive divisors of 4000. Packets traverse three store-and-forward links with rates 1,2,1 megabits per second, in that order. Each link serves packets in order; different links can operate simultaneously. There are no other delays or traffic, and one megabit is 10⁶ bits. Which n minimizes the time until the entire message reaches the destination?

**Required precision:** Integer.

A. 16  
B. 4  
C. 9  
D. 8

## ANSWER KEY — MOCK TEST 050

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C, D |
| 2 | NAT | 1 | 10 |
| 3 | MSQ | 1 | B, C, D |
| 4 | MCQ | 1 | B |
| 5 | MSQ | 1 | A, B, C |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | C |
| 8 | MSQ | 2 | B, C, D |
| 9 | MCQ | 2 | B |
| 10 | MCQ | 2 | B |
| 11 | MCQ | 1 | D |
| 12 | MCQ | 1 | C |
| 13 | MCQ | 1 | A |
| 14 | MCQ | 1 | A |
| 15 | MCQ | 1 | A |
| 16 | NAT | 1 | 2 |
| 17 | MCQ | 1 | B |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | B |
| 20 | MSQ | 1 | B, C, D |
| 21 | MSQ | 1 | A, C, D |
| 22 | MSQ | 1 | A, B, C |
| 23 | MSQ | 1 | B, D |
| 24 | MSQ | 1 | A, B, D |
| 25 | MCQ | 1 | C |
| 26 | MSQ | 1 | A, B, D |
| 27 | MSQ | 1 | B, C, D |
| 28 | MCQ | 1 | C |
| 29 | MCQ | 1 | C |
| 30 | MSQ | 1 | A, B, C |
| 31 | MCQ | 1 | A |
| 32 | MCQ | 1 | B |
| 33 | MSQ | 1 | A, C, D |
| 34 | MCQ | 1 | D |
| 35 | MSQ | 1 | A, B, C |
| 36 | MCQ | 2 | C |
| 37 | MSQ | 2 | A, B, D |
| 38 | MSQ | 2 | A, C, D |
| 39 | MCQ | 2 | A |
| 40 | MSQ | 2 | A, B, D |
| 41 | MCQ | 2 | C |
| 42 | MSQ | 2 | B, C, D |
| 43 | MCQ | 2 | D |
| 44 | MCQ | 2 | D |
| 45 | MSQ | 2 | B, D |
| 46 | MSQ | 2 | B, C, D |
| 47 | MSQ | 2 | B, C, D |
| 48 | MSQ | 2 | A, C, D |
| 49 | MCQ | 2 | C |
| 50 | MCQ | 2 | B |
| 51 | NAT | 2 | 40 |
| 52 | MCQ | 2 | D |
| 53 | MSQ | 2 | A, C, D |
| 54 | MCQ | 2 | A |
| 55 | MCQ | 2 | D |
| 56 | MCQ | 2 | C |
| 57 | MSQ | 2 | A, B, D |
| 58 | MSQ | 2 | A, B |
| 59 | MCQ | 2 | D |
| 60 | MCQ | 2 | C |
| 61 | MCQ | 2 | A |
| 62 | MSQ | 2 | A, B, D |
| 63 | MSQ | 2 | A, B, D |
| 64 | MCQ | 2 | C |
| 65 | MCQ | 2 | D |
