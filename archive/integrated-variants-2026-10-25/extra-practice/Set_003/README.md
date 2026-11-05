# GATE CS — Additional Practice Set 003

**Questions:** 50  
**Maximum marks:** 72

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Read the passage.

“A library extended its evening opening hours in June. Evening visits increased, while total daily visits remained unchanged. The library did not record whether evening visitors had previously visited at other times.”

Which conclusion is best supported by the passage?

A. The extended hours attracted no new visitors.  
B. Some visits may have shifted from earlier hours to the evening.  
C. Every evening visitor formerly visited in the morning.  
D. The extension reduced the total number of visits.  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 5×5 matrix is stored in row-major order in a one-dimensional C array: row r, column c is a[5*r+c], for 0≤r,c<5. Consider this complete program. All arithmetic fits in int.
```c
#include <stdio.h>
static void swap(int *p, int *q) {
    int t = *p; *p = *q; *q = t;
}
int main(void) {
    int a[25];
    for (int i = 0; i < 25; ++i) a[i] = i;
    for (int k = 0; k < 2027; ++k) {
        for (int r = 0; r < 5; ++r)
            for (int c = r + 1; c < 5; ++c)
                swap(&a[5*r+c], &a[5*c+r]);
        for (int r = 0; r < 5; ++r)
            for (int c = 0; c < 2; ++c)
                swap(&a[5*r+c], &a[5*r+4-c]);
    }
    printf("%d %d", a[7], a[17]);
    return 0;
}
```
What is printed?

A. 13 11  
B. 11 13  
C. 7 17  
D. 17 7  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A cube has six distinct face labels A,B,C,D,E,F. Three valid orientations are listed as (top, front, right): (A,B,C), (A,D,E), and (F,B,E). Which face is opposite B? Rotating the cube does not change its labels.

A. A  
B. C  
C. D  
D. E  

### Q4. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

G is a connected simple undirected graph with degree multiset {3,3,2,2,2,2}. Which statements must hold?

**Candidates**

**I.** G has exactly 7 edges.

**II.** G has an Euler trail that uses every edge exactly once.

**III.** G is bipartite.

**IV.** G has a Hamiltonian cycle.

A. III and IV  
B. I and III  
C. I and IV  
D. I and II  

### Q5. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In the covering stage of tabular Boolean minimization, the following is the complete prime-implicant chart. Column labels denote the six required on-set minterms; don't-care minterms, if any, need not be covered. A mark means the prime implicant covers that required minterm. Use only these prime implicants. Minimize the number of selected product terms first, then the total literal count among covers with that minimum term count.

| Prime implicant | m1 | m2 | m3 | m4 | m5 | m6 | Literals |
|---|---|---|---|---|---|---|---:|
| P1 | X | X | X | | | | 2 |
| P2 | X | | | X | X | | 3 |
| P3 | | X | | X | | X | 3 |
| P4 | | | X | | X | X | 4 |

Which set is selected by this criterion?

A. {P1,P2}  
B. {P1,P3,P4}  
C. {P1,P2,P3}  
D. {P2,P3,P4}  

### Q6. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a lexically scoped language, procedures Q and R are both immediately nested inside P. P declares x; Q and R do not declare x. During the calls P→Q→R, R accesses P's x. Static links point to the most recent activation of the immediately enclosing lexical procedure; dynamic links point to the caller. From R's activation, how many static links and dynamic links, respectively, lead to P's activation?

A. (2,1)  
B. (1,1)  
C. (2,2)  
D. (1,2)  

### Q7. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider the following code. Each call to more() returns an arbitrary Boolean value and does not change x. Consider only terminating executions. A conventional constant-propagation analysis tracks a single constant per variable or “not constant”; it joins distinct incoming constants as “not constant” and computes a fixed point over the loop.

```text
x = 1
while more():
    x = 2
y = x
```

Which statements are correct?

**Candidates**

**I.** At the loop header, this analysis establishes x=1 at its fixed point.

**II.** Immediately after the body assignment, this analysis establishes x=2.

**III.** On every terminating execution, the final y is 2.

**IV.** Replacing the while loop with a do-while loop executing x=2 before its first call to more() removes final value y=1 from the possible outcomes.

A. I and IV  
B. II and III  
C. II and IV  
D. III and IV  

### Q8. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under C17, i initially equals 1, a is an adequately sized int array, and f is an ordinary function taking two int arguments. Assume no arithmetic overflow. Consider each expression separately from this initial state. Which expressions have defined behaviour?

**Candidates**

**I.** i = i + 1

**II.** a[i] = i++

**III.** i++ && i++

**IV.** f(i++, i++)

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An arrow initially points in the positive x direction in a coordinate plane. First reflect the entire plane in the line y=x. Then rotate it clockwise by 90 degrees about the origin. Finally reflect it in the y-axis. In which direction does the arrow point?

A. Positive x  
B. Negative x  
C. Positive y  
D. Negative y  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP connection has congestion window 10,000 bytes and advertised receive window 7,000 bytes. Its oldest unacknowledged sequence number is 20,000 and the next unsent byte has sequence number 25,000. There is no wraparound. An ACK arrives with acknowledgment number 23,000 and advertised receive window 4,000; assume the congestion window remains unchanged and no data are sent before processing it. How many additional data bytes may be sent immediately?

A. 1,000  
B. 2,000  
C. 4,000  
D. 5,000  

### Q11. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An available-expression analysis tracks the expression a+b. One predecessor of a join computes t=a+b and then changes only c. The other computes u=a+b and then assigns a=0. There are no aliases. Which statements are correct immediately at the join?

**Candidates**

**I.** a+b is available on the first predecessor's exit.

**II.** a+b is available on the second predecessor's exit solely because it was evaluated there earlier.

**III.** A conventional must-availability analysis does not mark a+b available at the join.

**IV.** Replacing must-analysis intersection by union is always sound for eliminating a recomputation at the join.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q12. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler translates `if (p && q) x=1; else x=2;` with short-circuit evaluation. Evaluating p or q may have side effects, and each Boolean expression's result is determined at its evaluation. Which transformation preserves the evaluations and assignments for all executions?

A. Evaluate q first, then p, and test their conjunction.  
B. Evaluate both p and q unconditionally, then test their conjunction.  
C. Evaluate p; if false assign 2, otherwise evaluate q and assign 1 if q is true and 2 otherwise.  
D. Evaluate p twice and q only if the second evaluation is true.  

### Q13. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the simple complete bipartite graph K2,3. A Hamiltonian path visits every vertex exactly once; an Euler trail uses every edge exactly once. Which statements are correct?

A. It has an Euler trail.  
B. It has an Euler circuit.  
C. It has a Hamiltonian path.  
D. It has no Hamiltonian cycle.  

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

SQL table T(x) contains 2,2,3,NULL. What pair is returned by `SELECT COUNT(*), COUNT(x) FROM T`?

A. (4,3)  
B. (3,3)  
C. (4,2)  
D. (2,2)  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“Not every submitted report contains a diagram.” Which statement is logically equivalent?

A. No submitted report contains a diagram.  
B. At least one submitted report contains no diagram.  
C. Every submitted report contains no diagram.  
D. At least one report containing a diagram was not submitted.  

### Q16. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An n-bit two's-complement adder adds two operands and retains n result bits. Which conditions imply signed overflow?

A. Two positive operands produce a negative result.  
B. Two negative operands produce a nonnegative result.  
C. A positive and a negative operand produce a negative result.  
D. The carry into the sign bit differs from the carry out of the sign bit.  

### Q17. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A real 2×2 matrix A has distinct eigenvalues 2 and −1. Which statements must hold?

**Candidates**

**I.** A²−A−2I=0.

**II.** A is singular.

**III.** A is diagonalizable over the real numbers.

**IV.** A must be symmetric.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which conclusion is logically justified by the regular-language pumping lemma alone?

A. If a language violates the lemma's pumping property, it is not regular.  
B. If a language satisfies the pumping property, it must be regular.  
C. Every infinite language is nonregular.  
D. Every regular language has exactly one pumping length.  

### Q19. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A point initially at (1,2,3) is first rotated 90 degrees about the z-axis by the rule (x,y,z)→(−y,x,z). It is then rotated 90 degrees about the x-axis by the rule (x,y,z)→(x,−z,y). What is the final point?

A. (−2,−3,1)  
B. (−3,1,−2)  
C. (2,3,1)  
D. (−2,3,−1)  

### Q20. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

DFAs D1,D2 over the same alphabet have n and m states. Their complete product automaton tracks ordered state pairs. Which accepting-pair choices recognize the specified language?

A. Both component states accepting: L(D1)∩L(D2).  
B. Exactly one component state accepting: the symmetric difference of the languages.  
C. At least one component state accepting: the concatenation L(D1)L(D2).  
D. First component accepting and second not accepting: L(D1)−L(D2).  

### Q21. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Which formulas are logically equivalent to ¬∀x(P(x)→Q(x))?

**Candidates**

**I.** ∃x(P(x)∧¬Q(x))

**II.** ∀x(P(x)∧¬Q(x))

**III.** ¬∀x(¬P(x)∨Q(x))

**IV.** ∃x(¬P(x)∧Q(x))

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A client asks DNS for an AAAA record. Which result type is being requested?

A. An IPv6 address associated with the name.  
B. An Ethernet hardware address.  
C. A TCP acknowledgment number.  
D. The text of an HTTP response body.  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sentence has correct subject–verb agreement?

A. Each of the reports have an appendix.  
B. The list of required documents are on the desk.  
C. Neither of the two proposed routes is suitable.  
D. The results of the experiment indicates a change.  

### Q24. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A linear-probing table has occupied slots 2,3,4 holding keys whose home slots are respectively 2,2,4. Slot 5 has never been occupied. The key in slot 2 is deleted. Which repair preserves searches for the two remaining keys if no tombstones are allowed?

A. Leave slot 2 empty and do nothing else.  
B. Move the key from slot 3 to slot 2 and leave slot 3 empty; keep the key whose home is 4 in slot 4.  
C. Move the key from slot 4 to slot 2 and leave slot 3 unchanged.  
D. Clear all three slots without reinserting either remaining key.  

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Which Boolean expressions equal x for all x,y?

**Candidates**

**I.** x+xy

**II.** x(x+y)

**III.** x+y

**IV.** x XOR x

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q26. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Shared integers x,y start at zero. Thread A performs `x=1; rA=y;` and thread B performs `y=1; rB=x;`. Every displayed read/write is atomic, each thread's order is preserved, and all operations are sequentially consistent. Which final pairs (rA,rB) are possible?

A. (0,1)  
B. (0,0)  
C. (1,0)  
D. (1,1)  

### Q27. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A loop visits consecutive integer indices i starting at s and loads the four-byte array element at byte address base+4*i. Arithmetic is exact, base is unchanged, and i is also used by other statements. Which strength reductions preserve the load addresses and those other uses?

**Candidates**

**I.** Initialize address p=base and increment p by four each iteration for arbitrary s.

**II.** Initialize p=base+4*s, use p for each load, and increment p by four after each iteration while retaining i's original updates.

**III.** The multiplication used to form each load address can then be removed from the loop body if it has no other uses.

**IV.** Remove every update of i merely because a running address is available.

A. I and IV  
B. II and IV  
C. II and III  
D. III and IV  

### Q28. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An eight-bit ALU compares signed two's-complement operands A=0x80 and B=0x01 by computing A−B modulo 256. Let N be the result's sign bit, V the signed subtraction-overflow flag, and L the correct signed-less-than result. Which triple (N,V,L) is correct?

A. (1,0,1)  
B. (0,0,0)  
C. (1,1,0)  
D. (0,1,1)  

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A differentiable function on [0,3] has f(0)=1 and satisfies 2≤f′(x)≤5 throughout (0,3). Which value of f(3) is possible?

A. 6  
B. 10  
C. 17  
D. 20  

### Q30. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The distinct letters A,B,C,D,E are arranged in a row, each exactly once. Let X be the set of arrangements where A and B are adjacent in either order, and Y the set where B and C are adjacent in either order. Which statements are correct?

**Candidates**

**I.** X contains48 arrangements.

**II.** The intersection of X and Y contains24 arrangements.

**III.** Exactly72 arrangements belong to at least one of X and Y.

**IV.** Exactly36 arrangements belong to neither X nor Y.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q31. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A fully associative cache holds three blocks and starts empty. Compare FIFO replacement with LRU replacement for the block-reference sequence A,B,C,A,D,A. Every reference accesses one whole block, and every miss inserts it. Which statements are correct?

A. Both policies incur exactly four misses.  
B. FIFO evicts A on the reference to D.  
C. LRU evicts B on the reference to D.  
D. The final reference to A misses under FIFO but hits under LRU.  

### Q32. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The following code uses unbounded integers. The input y is arbitrary.

```text
if y > 0:
    x = 2
else:
    x = 2
if x == 2:
    z = 7
else:
    z = y
```

Which statements are correct about the values and constant-propagation opportunities?

**Candidates**

**I.** z is always7.

**II.** y must equal2 after the first conditional.

**III.** A flow-sensitive constant-propagation analysis can establish x=2 at the join and remove the unreachable second else branch.

**IV.** The two different predecessor blocks force x to be nonconstant at their join even when both assign2.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An ER model has entity Building with key building_id and weak entity Room with partial key room_no. Each Room belongs to exactly one Building; room_no is unique within a building but may repeat across buildings. Which statements are correct for the relational mapping?

A. The pair(building_id,room_no) can identify Room rows.  
B. room_no alone is necessarily a candidate key of Room.  
C. A non-null foreign key from Room.building_id to Building implements the required owner reference, together with the appropriate Room key.  
D. Removing building_id from Room loses information needed to distinguish equally numbered rooms in different buildings.  

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler considers replacing x/x by1 for a signed integer x. Division by zero is invalid; all other values here are representable. Which statements are correct?

**Candidates**

**I.** The rewrite preserves the defined result whenever x is known to be nonzero.

**II.** The rewrite preserves every possible runtime error when x may be zero.

**III.** A dominating condition that establishes x!=0, with no intervening modification, can justify the rewrite on that path.

**IV.** Textual repetition of x alone proves the rewrite safe for every input.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the words that fit: “The researcher made ___ measurements at separate time instants and was ___ when discussing confidential results.” Here the first blank means distinct, and the second means tactful.

A. discreet; discrete  
B. discrete; discreet  
C. discrete; discrete  
D. discreet; discreet  

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In first-order notation, consider the query {x : R(x) AND (exists x S(x))}, where the inner quantifier binds only its own occurrence of x and shadows the outer name within its parentheses. R and S are finite unary relations. Which statements are correct?

A. Renaming the bound inner variable to y leaves the query unchanged.  
B. The query always returns R intersect S.  
C. If S is nonempty, the query returns all of R.  
D. If S is empty, the query returns the empty relation.  

### Q37. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a DFA, states p and q are equivalent if every suffix yields the same acceptance result from both. Which statements are correct?

**Candidates**

**I.** If p is accepting and q rejecting, ε distinguishes them.

**II.** Having the same transitions on one input symbol alone guarantees equivalence.

**III.** If p,q are equivalent, their successors on any given symbol are equivalent.

**IV.** Two unreachable states must be equivalent to each other.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a finite relation R(x,y), consider the formula R(x,y) AND NOT exists z(R(x,z) AND z≠y), with x,y free. Which statements are correct?

**Candidates**

**I.** It selects tuples whose x value has exactly one distinct associated y value in R.

**II.** It rejects every tuple whenever R contains two different x values.

**III.** The existential variable z ranges over possible competing y values for the same x.

**IV.** It can return an(x,y) pair not in R.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q39. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a group, distinct nonidentity elements a,b satisfy a²=b²=e. Which statements are correct?

A. (ab)^(−1)=ba.  
B. The group must be abelian.  
C. If a and b commute, ab has order2.  
D. If ab has order2, a and b commute.  

### Q40. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An address-and-port translator lets two internal clients connect simultaneously to the same external server and server port, using one public IPv4 address. Assume its mapping distinguishes connections using the public source port. Which statements are correct?

**Candidates**

**I.** The two active mappings need different public source ports.

**II.** Both internal clients must have identical private source addresses.

**III.** Return traffic can be demultiplexed using the stored mappings.

**IV.** The translator must change the external server's application data to identify the clients.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A condition variable wait atomically releases its associated mutex and blocks, and reacquires the mutex before returning. Wakeups do not guarantee the application's predicate is true. Which statements are correct?

**Candidates**

**I.** The predicate should be rechecked after returning from wait.

**II.** A single if test before wait is sufficient for every execution.

**III.** Another thread can change the predicate before the awakened thread reacquires the mutex.

**IV.** Returning from wait means the mutex remains released under this specification.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q42. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

All operands below are unsigned n-bit integers, and operations wrap modulo2^n. Evaluating operands has no side effects. Which rewrites preserve both definedness and value for every input? Division by zero is undefined.

**Candidates**

**I.** x*(y+z) to x*y+x*z

**II.** x/x to1, including when x=0

**III.** x*0 to0

**IV.** x−y to y−x for every n≥2

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Select the pair completing the sentence with correct subject–verb agreement: “One of the proposals that ___ discussed yesterday ___ now been withdrawn.”

A. was, have  
B. were, have  
C. was, has  
D. were, has  

### Q44. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An array a initially contains[1,2], with i=0,j=1,k=0. The intended intermediate operation is a[i]=a[j]+a[k], evaluating both loads before the store. A faulty translation instead executes a[i]=a[j]; followed by a[i]=a[i]+a[k]. What is the faulty final a[0] minus the intended final a[0]?

A. −1  
B. 0  
C. 2  
D. 1  

### Q45. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process successfully calls exec to replace its program. Which statement is correct under the usual UNIX process model?

A. Its process identifier changes because a new process is created.  
B. All open file descriptors necessarily close.  
C. Execution eventually returns to the instruction after the successful exec call.  
D. The process keeps its identifier but executes the replacement program.  

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Read the statement: “When the library extended its hours, evening visits increased. Total daily visits stayed unchanged because morning visits fell by the same amount. The data alone do not establish whether additional people began using the library.” Which inference is supported?

A. Every new evening visitor was previously a morning visitor.  
B. The number of distinct users increased.  
C. The distribution of visits across the day changed.  
D. Extending hours caused no benefit to any visitor.  

### Q47. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

On a UNIX-like file system, path p refers to regular file F. Process R has already opened F for reading. Process W creates a different regular file G and atomically renames G over p. No process modifies F or G afterward. Assume rename succeeds and no symbolic links are involved. Which statements hold?

**Candidates**

**I.** R's existing descriptor still refers to F.

**II.** A later successful open of p refers to G.

**III.** The rename necessarily changes the inode referred to by R's existing descriptor.

**IV.** F's storage must be reclaimed before the rename can return, even while R retains its descriptor.

A. II and III  
B. II and IV  
C. I and II  
D. III and IV  

### Q48. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four events occur once each: filing F, inspection I, approval A, and publication P. Filing precedes both inspection and approval. Publication follows both inspection and approval. No order between inspection and approval is specified. Which conclusions necessarily follow?

A. Filing is the first of these four events.  
B. Inspection immediately precedes approval.  
C. Publication is the last of these four events.  
D. Exactly two orders of these four events satisfy the conditions.  

### Q49. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Transactions have timestamps T1=10,T2=20,T3=30, with lower meaning older. A wait-die lock manager lets an older requester wait for a younger holder but aborts a younger requester asking for an older holder's lock. T2 holds X, T3 requests X, then T1 requests X. What happens to these two requests, assuming T2 still holds X?

A. Both requesters wait.  
B. T3 aborts and T1 waits.  
C. T3 waits and T1 aborts.  
D. Both requesters abort.  

### Q50. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor initially spends half its execution time stalled for memory and half doing other work. An upgrade halves only the memory-stall time for the same program and input. What is the overall speedup?

A. 2  
B. 3/2  
C. 4/3  
D. 1  

---

## ANSWER KEY — SET 003

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C, D |
| 2 | MSQ | 2 | B, C, D |
| 3 | MSQ | 1 | A, B, D |
| 4 | MCQ | 1 | D |
| 5 | MSQ | 2 | A, B, D |
| 6 | MSQ | 1 | A, B, C |
| 7 | MCQ | 2 | C |
| 8 | MCQ | 2 | D |
| 9 | MSQ | 1 | A, C, D |
| 10 | MSQ | 2 | A, C, D |
| 11 | MCQ | 1 | C |
| 12 | MSQ | 2 | A, B, D |
| 13 | MCQ | 2 | B |
| 14 | MSQ | 1 | B, C, D |
| 15 | MSQ | 1 | A, C, D |
| 16 | MCQ | 2 | C |
| 17 | MCQ | 1 | A |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 2 | B, C, D |
| 20 | MCQ | 2 | C |
| 21 | MCQ | 1 | A |
| 22 | MSQ | 1 | B, C, D |
| 23 | MSQ | 1 | A, B, D |
| 24 | MSQ | 2 | A, C, D |
| 25 | MCQ | 1 | A |
| 26 | MCQ | 1 | B |
| 27 | MCQ | 2 | C |
| 28 | MSQ | 2 | A, B, C |
| 29 | MSQ | 1 | A, C, D |
| 30 | MCQ | 2 | B |
| 31 | MCQ | 2 | A |
| 32 | MCQ | 2 | D |
| 33 | MCQ | 2 | B |
| 34 | MCQ | 1 | B |
| 35 | MSQ | 1 | A, C, D |
| 36 | MCQ | 2 | B |
| 37 | MCQ | 2 | A |
| 38 | MCQ | 2 | B |
| 39 | MCQ | 1 | B |
| 40 | MCQ | 1 | D |
| 41 | MCQ | 1 | A |
| 42 | MCQ | 1 | B |
| 43 | MSQ | 1 | A, B, C |
| 44 | MSQ | 2 | A, B, C |
| 45 | MSQ | 1 | A, B, C |
| 46 | MSQ | 1 | A, B, D |
| 47 | MCQ | 1 | C |
| 48 | MCQ | 1 | B |
| 49 | MSQ | 2 | A, C, D |
| 50 | MSQ | 1 | A, B, D |
