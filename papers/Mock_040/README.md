# GATE CS 2027 — Full-Length Mock Test 040

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

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

“The new procedure reduced measurement variability but did not change the mean measurement.” Which conclusion is supported?

**Candidate answers**
I. Every new measurement equals the old mean.
II. New measurements are less dispersed under the reported variability measure.
III. The mean measurement became zero.
IV. The old procedure must have been biased.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q2. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A square paper is folded once along its vertical midline. A small circular hole is punched through both layers away from the fold and away from the edges. After unfolding, which statement must hold about the two holes?

A. They are images of each other under reflection in the fold line.  
B. They necessarily lie on the fold line.  
C. Their distance apart equals the side of the original square.  
D. Their positions are related by a 90-degree rotation about the centre for every punch location.

### Q3. [1 Mark] [MCQ]

Arrange these steps into a logically coherent experimental sequence: P, record the result; Q, formulate a hypothesis; R, design a test of that hypothesis; S, conduct that test.

A. Q–R–S–P
B. R–Q–P–S
C. P–S–R–Q
D. Q–P–R–S

### Q4. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A fair six-sided die is rolled twice independently. What is the probability that the second result exceeds the first? Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.4167  
B. 0.5833  
C. 0.2084  
D. 0.7084

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The grant was contingent on the laboratory obtaining approval.” Which phrase best replaces “contingent on” without changing the meaning?

A. unrelated to  
B. dependent on  
C. completed before  
D. guaranteed despite

### Q6. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For which of the following real values of x is the equation log_x(16)=log_2(x) defined and true?

**Candidates**

**I.** 4

**II.** 1/4

**III.** −4

**IV.** 1

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q7. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proposed rule maps every integer n to n²+n+1. Observations for inputs1,2,3 give outputs3,7,13. Which statements are correct?

A. The proposed rule agrees with all three observations.  
B. These observations uniquely establish the rule for every integer input.  
C. Adding (n−1)(n−2)(n−3) to the proposed rule gives another rule agreeing with the observations.  
D. The proposed rule predicts21 at input4.

### Q8. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Unit cubes are stacked in four columns on a2×2 base. Heights are nonnegative integers. Maximum heights in the first and second rows are3 and1; maximum heights in the first and second columns are2 and3. What is the minimum total number of cubes consistent with these four maxima?

**Required precision:** Integer.

A. 12  
B. 6  
C. 3  
D. 7

### Q9. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

The three-digit strings000 through111 containing only binary digits are listed in increasing binary numerical order, with leading zeros retained. Between each consecutive pair, count how many digit positions change. What is the sum of these counts over all seven transitions?

**Required precision:** Integer.

A. 22  
B. 6  
C. 12  
D. 11

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

The diagonals of a trapezium ABCD intersect at O, with AB parallel to CD. The areas of triangles AOB and COD are 4 and 9 square units respectively. What is the area of the entire trapezium?

**Required precision:** Integer square units.

A. 50  
B. 13  
C. 26  
D. 25

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A processor issues instructions out of order but commits their architectural results in program order using a reorder buffer. Which mechanism chiefly prevents a younger completed instruction from exposing its architectural result before an older faulting instruction is resolved?

A. In-order commit from the reorder buffer.
B. Issuing every ready instruction as soon as possible.
C. Increasing the number of execution units.
D. Predicting every branch as taken.

### Q12. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A three-input majority gate outputs one exactly when at least two inputs are one. Its input is currently 011. Among the three possible single-input-bit flips, how many change the gate's output?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q13. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A process writes a2048-byte buffer using a system call that may complete partially. The first call returns768 and the second, correctly adjusted call returns512. Both returns indicate successfully written bytes. How many buffer bytes remain to be written, assuming no other output occurs?

**Required precision:** Exact integer.

A. 768  
B. 1536  
C. 384  
D. 769

### Q14. [1 Mark] [MCQ]

An open-addressed hash table uses linear probing and tombstones for deletion. During insertion of key k, the first tombstone is encountered before an occupied slot containing k. Duplicate keys are forbidden. What must a correct insertion do?

A. Immediately place a second copy of k in the tombstone.
B. Treat the tombstone as proof that k is absent.
C. Stop searching at every tombstone as if it were never occupied.
D. Continue searching beyond the tombstone to detect the existing key before deciding to insert.

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A transport-layer port number is primarily used to distinguish what?

A. Application endpoints on a host.  
B. Individual bits within one Ethernet frame.  
C. Physical pins on a memory chip.  
D. Cache-line offsets inside a processor.

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

a0=0, a1=1 and a_n=3a_(n−1)−2a_(n−2) for n≥2. Which formal generating function equals Σ_(n≥0) a_n x^n?

A. 1/(1−3x+2x²)  
B. x/(1−3x−2x²)  
C. (1−x)/(1−2x)  
D. x/((1−x)(1−2x))

### Q17. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over a nonempty domain, consider propositions F=(for every x, P(x) OR Q(x)) and G=((for every x, P(x)) OR (for every x, Q(x))). Which statements are correct?

A. G implies F.  
B. F implies G in every interpretation.  
C. A two-element domain can make F true and G false.  
D. F and G are equivalent when the domain has one element.

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An instruction uses base-plus-scaled-index addressing: effective address=base+4×index+displacement. The index register contains−3, base contains100 and displacement is20. A32-bit word is loaded from that effective address. What is the byte address of its last byte?

**Required precision:** Integer.

A. 111  
B. 222  
C. 56  
D. 112

### Q19. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A syntax-directed translator for expressions uses E→E+T with E.val=Eleft.val+T.val, E→T with E.val=T.val, T→digit with T.val=digit.value, and T→(E) with T.val=2×E.val. What value is assigned to the complete expression (2+3)+(4)?

**Required precision:** Exact integer.

A. 36  
B. 9  
C. 19  
D. 18

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A timestamp protocol handles a write by transaction timestamp t as follows: abort if t<readTS(x); otherwise ignore the write if t<writeTS(x); otherwise perform it. Initially readTS(x)=5 and writeTS(x)=9. Two separate attempts are considered from this same initial state, with t=7 and t=4. What are their respective outcomes?

A. Perform, ignore  
B. Abort, ignore  
C. Ignore, abort  
D. Perform, abort

### Q21. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A dynamic array starts with capacity one. Appending to a full array allocates a new array of twice the capacity and copies all existing elements; other appends take constant time. Which statements hold over n appends starting empty?

**Candidates**

**I.** The total copying work is O(n).

**II.** The total copying work is necessarily Θ(n log n).

**III.** A single append can take Θ(n) time when the current number of elements is proportional to n.

**IV.** Every individual append has worst-case constant time.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q22. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A ternary ER relationship Assignment(Employee,Project,Role) records who fills each role on each project. Every (Project,Role) pair has at most one assigned employee. An employee may fill several roles on the same project, and may work on several projects. There are no other key constraints. Which statements hold?

**Candidate answers**
I. (Project,Role) is a candidate key of Assignment.
II. (Employee,Project) is necessarily a candidate key.
III. Two assignments with the same project and role but different employees violate the constraint.
IV. Replacing the relationship by Employee–Project alone preserves all assignment information.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q23. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

What does this conforming C program print? Array indices are valid and all arithmetic is representable.

```c
#include <stdio.h>
void f(int a[], int n) {
    int *p = a;
    a = a + 1;
    a[n-2] = p[0] + a[0];
}
int main(void) {
    int x[] = {4,7,9};
    f(x,3);
    printf("%d %d\n", x[0],x[2]);
    return 0;
}
```

**Candidate answers**
I. 7 11
II. 4 11
III. 4 9
IV. 11 9

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q24. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A coin system has denominations1,3,4 and unlimited coins. For amount6, how many more coins does repeatedly taking the largest affordable denomination use than an optimal solution?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q25. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A deterministic pushdown automaton recognizes balanced parentheses by pushing on '(' and popping on ')', rejecting a pop from an empty stack. Acceptance requires the stack to be empty at end of input. Which statements are correct?

**Candidate answers**
I. The empty string is accepted.
II. Equal total counts of '(' and ')' guarantee acceptance.
III. Every prefix of an accepted string has at least as many '(' as ')'.
IV. The string '())(' is accepted.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q26. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A doubly linked list has adjacent non-sentinel nodes P,X,N. Removing X while preserving the list requires which neighbour updates?

**Candidate answers**
I. P.next=N and N.prev=P.
II. P.prev=N and N.next=P.
III. P.next=X and N.prev=X.
IV. P.next=P and N.prev=N.

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: valid  
D. I: valid; II: invalid; III: invalid; IV: invalid

### Q27. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

SQL table L(id) contains 1,2 and table R(id,v) contains (1,0),(1,5). What rows are returned by the following query, using ordinary SQL bag semantics?

```sql
SELECT L.id, R.v
FROM L LEFT JOIN R ON L.id=R.id AND R.v>0;
```

**Candidate answers**
I. (1,5) only
II. (1,0),(1,5),(2,NULL)
III. (1,5),(2,NULL)
IV. (1,NULL),(2,NULL)

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A 3×4 matrix has rows (1,2,0,1),(0,1,1,0),(1,3,1,1). What is the dimension of its nullspace over the real numbers?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q29. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For x≠0, let f(x)=(sin(3x)−3x)/x³, with angles in radians. What value should be assigned to f(0) to make f continuous at zero?

**Required precision:** Exact finite decimal.

A. -9.0  
B. -4.5  
C. -2.3  
D. -3.5

### Q30. [1 Mark] [NAT]

Two D flip-flops store bits q1,q0. On every clock edge, q1 becomes the old q0 and q0 becomes NOT(old q1 XOR old q0). Starting at 00, what is the least positive number of edges after which the state is 00 again?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which language is regular?

A. {aⁿbⁿ : n≥0}  
B. {aᵖ : p is prime}  
C. {aⁿbᵐ : n,m≥0 and n is even}  
D. {ww : w∈{0,1}*}

### Q32. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

X has a Poisson distribution with parameter lambda>0. It is known that P(X=0)=P(X=1). What is E[X^2]?

A. 4  
B. 1  
C. 2  
D. 3

### Q33. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A link sends packets of1000 payload bits plus a100-bit header at1100 bits per millisecond. Packets are continuously available and there are no other delays or losses. What payload throughput, in bits per millisecond, is achieved?

**Required precision:** Exact number.

A. 2000  
B. 500  
C. 1001  
D. 1000

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Procedure P makes a call as its final action, passing the address of a local variable x to callee Q. Q dereferences that address during the call. Which statements about optimizing this call are correct?

**Candidates**

**I.** P's frame may always be discarded and overwritten before Q reads x, solely because the call is in tail position.

**II.** Any transformation must preserve the addressed object's value and valid storage for Q's use.

**III.** Q cannot observe x because callees never receive pointers to caller variables.

**IV.** Tail position alone is insufficient to justify overwriting all storage in P's frame.

A. III and IV  
B. I and II  
C. II and IV  
D. I and III

### Q35. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Two threads each execute the following two-iteration loop on shared x, initially 0. Each read and write is atomic, the computation uses a private register r, and execution is a sequentially consistent interleaving preserving each thread's order.

```text
repeat twice:
    r = x
    x = r + 1
```

Which values of x are possible after both threads finish?

**Candidate answers**
I. 1
II. 2
III. 3
IV. 4

A. I: valid; II: valid; III: valid; IV: valid  
B. I: invalid; II: valid; III: invalid; IV: valid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q36. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A compiler translates a short-circuit Boolean expression (p AND q) OR r into a decision graph. Each predicate occurrence is evaluated at most once on any execution, in source short-circuit order. How many different subsets of {p,q,r} can be evaluated during an execution, as their truth values vary?

**Required precision:** Integer.

A. 6  
B. 3  
C. 2  
D. 4

### Q37. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Each reference first spends 1 ns searching a TLB. A TLB miss, occurring on 10% of references, adds a 200 ns page-table walk before the data-cache lookup. Every data-cache lookup takes 2 ns; a data-cache miss, occurring on 5% of references, adds 50 ns. These delays do not overlap, and there are no page faults. What is the mean reference time in ns?

**Required precision:** Exact finite decimal.

A. 25.5  
B. 51.0  
C. 12.8  
D. 26.5

### Q38. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A microinstruction independently selects one of nine source choices, one of five ALU choices, and any subset of eight destination registers, including the empty subset. A format with separate fixed-width binary source and ALU fields plus an eight-bit destination mask is compared with an unrestricted single binary field encoding all legal combinations. How many bits does the separate-field format require in excess of the minimum single-field width?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q39. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An eight-bit two's-complement fixed-point format has four fractional bits. Multiply the values encoded by 0xE6 and 0x1C using an exact intermediate result, then round once to the nearest representable value, breaking a tie toward an even least significant retained bit. No overflow occurs. What is the final encoded byte?

**Candidate answers**
I. 0xD3
II. 0xD2
III. 0x2E
IV. 0xD4

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q40. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Relation R(x,y) contains(1,1),(1,2),(2,2),(3,1). Evaluate the domain-restricted tuple-calculus condition R(x,y) AND NOT EXISTS z(R(y,z) AND z≠x). How many tuples of R satisfy it?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q41. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Let u=(1,1,0)ᵀ, v=(1,0,1)ᵀ, P=uuᵀ/(uᵀu), and Q=vvᵀ/(vᵀv). Which statements are correct?

**Candidate answers**
I. PQ has rank one.
II. trace(PQ)=1/4.
III. PQ is symmetric.
IV. The eigenvalues of PQ, counting multiplicity, are 1/4,0,0.

A. I: invalid; II: valid; III: invalid; IV: valid  
B. I: valid; II: valid; III: valid; IV: valid  
C. I: valid; II: valid; III: invalid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q42. [2 Marks] [MSQ]

In a binary floating-point format with round-to-nearest, ties-to-even and finite precision, which statements are correct?

A. Addition is necessarily associative for all finite inputs whose computations stay finite.
B. Adding a sufficiently small positive number to a sufficiently large positive number can leave the stored result unchanged.
C. Cancellation of nearby numbers can reveal error already present in their approximations.
D. Every integer of arbitrary size is represented exactly.

### Q43. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A proposed proof claims that the regular language a*b* is not regular: “For pumping length p choose a^p b^p. Select a decomposition whose pumped part contains both a and b. Pumping twice destroys the required order.” Which objections correctly identify flaws?

**Candidates**

**I.** A nonregularity proof must defeat every legal decomposition, not just one selected decomposition.

**II.** Any legal decomposition with prefix-plus-pumped-part length at most p has its pumped part entirely among the a's.

**III.** The pumping lemma permits an empty pumped part, so the proof must use one.

**IV.** Choosing a string of length2p is forbidden by the pumping lemma.

A. I and III  
B. I and II  
C. I and IV  
D. II and III

### Q44. [2 Marks] [NAT]

Let A=[[0,1],[−2,3]] and let v=(x,y)ᵀ satisfy x+y=6. The sequence A^n v must remain bounded as n tends to infinity. What is x?

**Answer format:** Exact number.

### Q45. [2 Marks] [MSQ]

D(id) contains 1 and 2. E(eid,did,active) contains (10,1,0) and (11,1,1); all columns are non-NULL. Consider this SQL query:

```sql
SELECT D.id, COUNT(*) AS n, COUNT(E.eid) AS m
FROM D LEFT JOIN E
  ON D.id = E.did AND E.active = 1
GROUP BY D.id;
```

Which statements are correct?

A. The row for id=1 has n=1 and m=1.
B. The row for id=2 has n=1 and m=0.
C. Moving E.active=1 from ON to WHERE necessarily preserves the result.
D. The row for id=2 has n=0 and m=0.

### Q46. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

An HTTP client sends a conditional GET containing `If-None-Match: "v7"` for a cached representation. The server's current representation has the same entity tag and is otherwise eligible for the conditional request. Compare a 304 response with a 200 response carrying the entire unchanged representation. Which statement is correct?

**Candidate answers**
I. A 304 necessarily eliminates the request-response round trip.
II. A 304 supplies a new full representation body that must replace the cached body.
III. A 304 can save representation-body transfer while still requiring a network round trip.
IV. A 304 proves that all caches on the Internet contain the same body.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q47. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A synchronous message-passing send completes only when a matching receive occurs. Process P first sends to Q and then receives from Q; process Q first sends to P and then receives from P. Neither channel buffers a message. Which statements are correct?

**Candidates**

**I.** Both processes can block on their first operation.

**II.** The program is guaranteed to finish because each process eventually has a receive in its source code.

**III.** Changing Q to receive first and then send removes this particular cyclic wait.

**IV.** Adding a mutex around both sequences necessarily fixes the protocol.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A queue is implemented with an input stack and an output stack. Enqueue pushes onto the input stack. Dequeue pops the output stack; if it is empty, all items from the input stack are first moved to it, one pop and one push per item. Count only individual stack pushes and pops. Starting empty, perform enqueue(A), enqueue(B), dequeue, enqueue(C), enqueue(D), dequeue, dequeue. How many stack operations are performed in total?

**Required precision:** Integer.

A. 15  
B. 30  
C. 8  
D. 16

### Q49. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A 0/1 knapsack has capacity6. Items A,B,C have (weight,value) pairs (3,5),(4,7),(2,4). Each item can be selected at most once. A faulty implementation updates its one-dimensional DP array in increasing capacity order for each item, allowing an item to be reused. By how much can its final dp[6] exceed the true optimum, starting with all entries zero and processing items A,B,C in that order?

**Required precision:** Exact integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q50. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A byte-addressed processor has address lines A15 through A0. A memory board uses four 4K×8 RAM chips to provide one contiguous 16 KiB region starting at address 0x8000. Each selected chip supplies one byte. Chip address pins use A11 through A0; a decoder chooses one chip. Assume the decoder is enabled exactly for addresses in the intended region. Which statements are correct?

**Candidate answers**
I. A13 and A12 can select the chip, while A15=1 and A14=0 enable the board.
II. Address 0xB123 selects chip index 3 (indices 0–3 in increasing address order) at local offset 0x123.
III. If the board enable checks only A15=1 and ignores A14, each physical byte is mapped at two processor addresses.
IV. Connecting chip address pins to A12 through A1, while otherwise retaining the stated decoder, still gives one-to-one addressing of the 16 KiB region.

A. I: invalid; II: valid; III: valid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: valid  
D. I: valid; II: valid; III: valid; IV: invalid

### Q51. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A machine M is described together with a finite input x and a nonnegative integer bound k. Which questions are decidable uniformly from this data?

**Candidate answers**
I. Does M accept x within k steps?
II. Does M halt on x within k steps?
III. Does M eventually halt on x with no bound?
IV. Does the simulation visit the same full configuration twice within its first k steps?

A. I: invalid; II: valid; III: invalid; IV: valid  
B. I: valid; II: valid; III: valid; IV: valid  
C. I: valid; II: valid; III: invalid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q52. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A and B are real 4×4 matrices, each of rank 3. Which statements are correct?

**Candidate answers**
I. rank(AB) is at least 2.
II. rank(AB) can be 3.
III. rank(AB) can be 1.
IV. rank(AB) can be 2.

A. I: valid; II: valid; III: invalid; IV: valid  
B. I: invalid; II: valid; III: invalid; IV: valid  
C. I: valid; II: valid; III: valid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q53. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Integers x range over all four-bit signed values −8 through 7. Evaluate `y=(2*x)/2` by first multiplying with four-bit two's-complement wraparound, then dividing the resulting signed value by two using exact division on even integers. For how many x values is y=x?

**Required precision:** Integer.

A. 16  
B. 8  
C. 4  
D. 9

### Q54. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean inputs x,y,z, consider F=(x OR y) AND ((NOT x) OR z). Which statements are correct?

A. F=(x AND z) OR ((NOT x) AND y).  
B. The product term yz can be added to the expression in A without changing F.  
C. F is always equal to y AND z.  
D. When y=z, F equals that common value.

### Q55. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A partial DFA over {a,b} has states q0,q1,q2, start state q0, and accepting set {q2}. Its only transitions are q0 on a to q1, q1 on a to q2, and q2 on a to q2. Undefined transitions reject. What is the minimum number of states in a complete DFA recognizing the complement of its language over {a,b}*?

**Candidate answers**
I. 4
II. 3
III. 5
IV. 6

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q56. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A binary tree has distinct labels. Its preorder is A,B,D,E,C,F and its inorder is D,B,E,A,C,F. Which postorder is correct?

**Candidate answers**
I. D,E,B,F,C,A
II. D,B,E,F,C,A
III. E,D,B,C,F,A
IV. D,E,F,B,C,A

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: valid  
D. I: valid; II: invalid; III: invalid; IV: invalid

### Q57. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A comparison algorithm recursively divides an array of n=32 elements into equal halves. At every non-leaf call it first solves both halves and then compares every element in the left half with every element in the right half, once per pair. A one-element call makes no comparisons. How many comparisons occur in total?

**Required precision:** Exact integer.

A. 992  
B. 248  
C. 496  
D. 497

### Q58. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

In an idealized CSMA/CD network, the farthest stations have a one-way propagation time of12 microseconds. A100-Mbit/s transmitter must still be transmitting at the latest possible collision-detection instant. Ignoring all encoding overhead and assuming a collision can occur just before a distant station first senses the transmission, what is the minimum frame length in bytes?

**Required precision:** Integer.

A. 600  
B. 300  
C. 150  
D. 301

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A recursive DFS starts at s in a directed graph with edges s→a,s→b,a→c,b→c,c→d. Each adjacency list is processed in alphabetical order. A vertex is marked immediately upon its first visit. How many edges lead to vertices already marked at the moment that edge is examined?

**Required precision:** Integer.

A. 2  
B. 0  
C. 1  
D. 3

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A hidden source is chosen once: source I with probability 1/3, source II with probability 2/3. Conditional on that source, trials are independent; success probability is 1/4 for I and 1/2 for II. Given exactly two successes in the first three trials, what is the probability of success on the fourth trial?

A. 1/2  
B. 35/76  
C. 3/19  
D. 7/16

### Q61. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two threads execute the following operations on atomic Boolean flags, initially false, under sequential consistency:

```text
Thread 0: flag0 = true; while (flag1) {} ; critical_section; flag0 = false;
Thread 1: flag1 = true; while (flag0) {} ; critical_section; flag1 = false;
```

Which assessment is correct?

A. Mutual exclusion can fail because both flags may be false at the start.  
B. Mutual exclusion holds, but both threads can wait forever after setting their flags.  
C. Both mutual exclusion and progress are guaranteed.  
D. The algorithm implements strict alternation using a turn variable.

### Q62. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Resource A has two instances and B has one. P holds one A and requests B; Q holds B and requests one A; R holds the other A and requests nothing more. A process that receives its request completes and releases its resources; R can complete immediately. Which statements are correct?

A. The system can finish all processes in order R,Q,P.  
B. The cycle involving P and Q proves deadlock even with R able to release an A instance.  
C. A cycle in the resource-allocation graph is not sufficient here to establish deadlock.  
D. Releasing R's A can enable Q, whose completion can then enable P.

### Q63. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

In a finite directed network, every link has strictly positive cost and every router can reach destination d. Each router u other than d selects any outgoing neighbour v satisfying dist(u,d)=cost(u,v)+dist(v,d), using exact shortest-path distances. Different routers may break equal-cost ties independently. Which statements are correct?

**Candidate answers**
I. The selected next-hop graph can contain a directed cycle because tie-breaking is independent.
II. Distance to d strictly decreases at each selected hop.
III. Every packet following these next hops eventually reaches d.
IV. Allowing zero-cost links would leave the strict-decrease argument unchanged.

A. I: valid; II: valid; III: valid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: invalid; IV: valid

### Q64. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A loop begins with x=0 and repeatedly executes `x=x+1` while an input-dependent condition holds. A simple forward constant-propagation analysis joins facts from the initial edge and loop back edge at the header. Which statements are correct?

**Candidate answers**
I. x need not be a single known constant at the loop header after the fixed point is reached.
II. Treating x as zero on every header visit is sound merely because its initializer is zero.
III. Different iterations can reach the header with different x values.
IV. Constant propagation alone necessarily computes the exact iteration count for every input condition.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q65. [2 Marks] [MCQ]

Two initially empty tables P(id,qid) and Q(id,pid) have non-NULL foreign keys P.qid→Q.id and Q.pid→P.id. A transaction inserts P(1,1) and Q(1,1). What difference can deferred checking make, assuming both foreign keys permit checking at commit?

A. It allows both rows to be inserted and the final mutually referencing state to satisfy the constraints, whereas immediate checking would reject whichever insert occurs first.
B. It permits either foreign key to remain broken permanently after commit.
C. It removes the requirement that referenced keys exist at commit.
D. It forces both tables to remain empty.

---

## ANSWER KEY — MOCK TEST 040

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MSQ | 1 | B, C, D |
| 3 | MCQ | 1 | A |
| 4 | MSQ | 1 | B, C, D |
| 5 | MSQ | 1 | A, C, D |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | B |
| 8 | MSQ | 2 | A, C, D |
| 9 | MCQ | 2 | D |
| 10 | MCQ | 2 | D |
| 11 | MCQ | 1 | A |
| 12 | MCQ | 1 | C |
| 13 | MSQ | 1 | B, C, D |
| 14 | MCQ | 1 | D |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 1 | A, B, C |
| 17 | MCQ | 1 | B |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | D |
| 20 | MSQ | 1 | A, B, D |
| 21 | MCQ | 1 | D |
| 22 | MCQ | 1 | D |
| 23 | MCQ | 1 | D |
| 24 | MSQ | 1 | A, B, C |
| 25 | MCQ | 1 | D |
| 26 | MCQ | 1 | D |
| 27 | MCQ | 1 | B |
| 28 | MCQ | 1 | C |
| 29 | MSQ | 1 | A, C, D |
| 30 | NAT | 1 | 3 |
| 31 | MSQ | 1 | A, B, D |
| 32 | MSQ | 1 | A, B, D |
| 33 | MSQ | 1 | A, B, C |
| 34 | MCQ | 1 | C |
| 35 | MCQ | 1 | D |
| 36 | MSQ | 2 | A, C, D |
| 37 | MCQ | 2 | A |
| 38 | MCQ | 2 | A |
| 39 | MCQ | 2 | D |
| 40 | MSQ | 2 | A, B, C |
| 41 | MCQ | 2 | C |
| 42 | MSQ | 2 | B, C |
| 43 | MCQ | 2 | B |
| 44 | NAT | 2 | 3 |
| 45 | MSQ | 2 | A, B |
| 46 | MCQ | 2 | A |
| 47 | MCQ | 2 | D |
| 48 | MCQ | 2 | A |
| 49 | MSQ | 2 | A, B, C |
| 50 | MCQ | 2 | D |
| 51 | MCQ | 2 | C |
| 52 | MCQ | 2 | A |
| 53 | MCQ | 2 | B |
| 54 | MCQ | 2 | C |
| 55 | MCQ | 2 | B |
| 56 | MCQ | 2 | D |
| 57 | MSQ | 2 | A, B, D |
| 58 | MCQ | 2 | B |
| 59 | MCQ | 2 | C |
| 60 | MSQ | 2 | A, C, D |
| 61 | MSQ | 2 | A, C, D |
| 62 | MCQ | 2 | B |
| 63 | MCQ | 2 | B |
| 64 | MCQ | 2 | B |
| 65 | MCQ | 2 | A |
