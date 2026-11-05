# GATE CS 2027 — Full-Length Mock Test 048

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

Twenty-five observations fall in intervals [0,10), [10,20), [20,30), [30,40), with respective frequencies 4,6,10,5. Which interval necessarily contains the median?

A. [0,10)
B. [10,20)
C. [20,30)
D. [30,40)

### Q2. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A square sheet is folded along both its horizontal and vertical midlines. Small holes are punched through all four layers, with every punch strictly away from the folds and sheet edges. Coordinates are measured from the original square's centre. Which set can be exactly the resulting hole centres after unfolding one punch?

A. {(1,1),(−1,1),(1,−1),(−1,−1)}  
B. {(1,1),(−1,1),(1,−1),(−2,−1)}  
C. {(1,1),(−1,1)}  
D. {(1,1),(−1,−1)}

### Q3. [1 Mark] [MCQ]

A narrative contains: “Mira mailed the parcel after weighing it. She obtained the address before mailing it, but the text does not specify whether she obtained the address before or after weighing.” Which order is inconsistent with this account?

A. Obtain address, weigh, mail.
B. Weigh, obtain address, mail.
C. Weigh, mail, obtain address.
D. Both A and B are possible.

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A rectangular sheet is folded once along its vertical midline, making two layers, and then once along the horizontal midline of the folded rectangle, making four layers. A small circular hole is punched strictly inside the four-layer region, away from all fold lines and boundaries. How many separate holes appear after complete unfolding?

**Required precision:** Integer.

A. 8  
B. 2  
C. 4  
D. 5

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The committee's endorsement was qualified: it supported the proposal only if its cost was independently audited.” In this sentence, “qualified” most nearly means:

A. Awarded a professional certificate.  
B. Expressed subject to a reservation or condition.  
C. Withdrawn without explanation.  
D. Unconditionally enthusiastic.

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A population triples at the end of every complete day. Another population doubles at the end of every complete day and initially has eight times as many members as the first. What is the first integer day at whose end the first population is larger?

**Required precision:** Integer.

A. 6  
B. 12  
C. 3  
D. 7

### Q7. [2 Marks] [NAT]

Four distinct tasks A,B,C,D are placed in a linear order. Consider the four assertions: A is before B; B is before C; C is before D; D is before A. How many task orders make exactly two assertions true?

**Answer format:** Integer.

### Q8. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Unit cubes are stacked on a 2×2 base with column heights [[3,1],[2,2]]. Adjacent entries in a row or column represent face-adjacent columns. All columns start on the same horizontal plane. Excluding the bottom faces on that plane, how many unit-square faces of the solid are exposed?

**Required precision:** Integer.

A. 48  
B. 12  
C. 24  
D. 25

### Q9. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A sequence satisfies a1=2 and a(n+1)=2a(n)+1 for n≥1. What is the sum of its first four terms?

**Required precision:** Integer.

A. 82  
B. 21  
C. 42  
D. 41

### Q10. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two circular disks of equal radius r>0 have centres separated by distance r. Let P be the perimeter of their union, excluding arcs lying inside the other disk. What is P/(πr)?

**Required precision:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

A. 5.3334  
B. 1.3334  
C. 3.6667  
D. 2.6667

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Grammar S→aS | Sb | ε generates which language?

A. a*b*
B. {aⁿbⁿ:n≥0}
C. (ab)* only
D. All strings over {a,b}

### Q12. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A process opens a regular file for reading, obtaining descriptor p with file offset 0, and then executes q=dup(p). It performs the following successful operations in order: read 2 bytes through p; read 3 bytes through q; seek through p to absolute byte offset 1; read 1 byte through q. The file is long enough for every read. What is the resulting shared file offset? Offsets are zero-based.

A. 4  
B. 1  
C. 3  
D. 2

### Q13. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A BST has root20, left child10, right child30, and node10 has right child15. A right rotation is performed at20. How many nodes are visited by a successful ordinary search for30 after the rotation, including root and target?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q14. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A directed graph has adjacency lists s:[a,b], a:[c,d], b:[d], c:[], d:[e], e:[]. BFS starts at s, scans each list in the displayed order and marks a vertex when enqueuing it. At the instant d is first enqueued, how many vertices are already in the queue immediately before that enqueue?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q15. [1 Mark] [MSQ]

A pushdown automaton accepts by final state after consuming its entire input. A proposed modification erases all its stack symbols immediately whenever it first enters any final state, then continues with the original transitions. The original transitions may depend on the stack top. Which statements are correct?

A. The modification can destroy an accepting computation that must leave a final state and read further input.
B. The modification always preserves the accepted language.
C. Entering a final state before input exhaustion does not by itself accept the input.
D. Every final state in every pushdown automaton must have no outgoing transitions.

### Q16. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A checksum scheme adds 16-bit unsigned words using one's-complement addition: every carry beyond bit 15 is added back to the low 16 bits. The checksum is the bitwise complement of the final 16-bit sum. For the two words hexadecimal FFFF and 0001, what is the checksum's decimal value?

**Required precision:** Integer.

A. 65534  
B. 131068  
C. 32767  
D. 65535

### Q17. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

At the point immediately before the code below, which current variable values are live? A value is live if some subsequent control-flow path reads it before overwriting it. There are no uses after return.

```text
if c:
    x = a
else:
    x = b
return x
```

A. a  
B. b  
C. x  
D. c

### Q18. [1 Mark] [MSQ]

M is a finite monoid with identity e and satisfies left cancellation: ax=ay implies x=y. Which statements must hold?

A. For each a, the map x↦ax is onto M.
B. Every a has a two-sided inverse.
C. M must be commutative.
D. M is a group.

### Q19. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A fixed 32-bit instruction contains three register fields, each able to name any of 32 registers, an eight-bit immediate field, and an opcode occupying all remaining bits. What is the maximum number of distinct opcode patterns?

**Required precision:** Integer.

A. 512  
B. 1024  
C. 256  
D. 513

### Q20. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

In an ER model, Department is a strong entity with key dept_id. Project is weak and identified by its owning Department and partial key project_code. Task is weak and identified by its owning Project and partial key task_no. Project codes may repeat across departments; task numbers may repeat across projects. No surrogate keys or additional uniqueness constraints are introduced. How many attributes are needed in the minimal primary key of the mapped Task relation?

A. 3  
B. 6  
C. 2  
D. 4

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A min-heap with distinct keys1 through7 is stored in an array indexed1 through7. The key7 is known to be at index2. How many such heaps exist?

**Required precision:** Exact integer.

A. 0  
B. 1  
C. 2  
D. 3

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, assuming the proper standard header and successful allocation, which statement about `int *p=malloc(3*sizeof *p);` is correct before any initialization of the allocated int objects?

A. All three int values are guaranteed to be zero.  
B. The allocated storage persists until it is freed, even if the local pointer variable leaves scope.  
C. sizeof *p evaluates an indeterminate pointed-to int value.  
D. The allocation contains exactly three bytes on every implementation.

### Q23. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

In the lattice of positive divisors of 30 ordered by divisibility, an element y complements 6 if gcd(6,y)=1 and lcm(6,y)=30. Find y.

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q24. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A prime-implicant chart has four columns m0,m1,m2,m3 and four rows. P covers m0,m1; Q covers m1,m2; R covers m2,m3; S covers m0,m3. All rows have equal literal cost and no other prime implicants exist. Which statements hold?

A. No row is essential.  
B. Every minimum cover contains P.  
C. {P,R} is a minimum cover.  
D. Removing P still leaves a cover using two rows.

### Q25. [1 Mark] [MSQ]

Under set relational algebra, R(A,B) contains (1,x),(1,y),(2,x), and S(B) contains x,y. Let D=R÷S and P=π_A(R). Which statements hold?

A. D contains exactly the tuple A=1.
B. D=P.
C. Adding (2,y) to R makes D=P.
D. Removing y from S makes D empty.

### Q26. [1 Mark] [MCQ]

An arithmetic right shift by one on the signed value−7 produces floor(−7/2). Integer division by2 instead truncates toward zero. What is the shifted value minus the division result?

A. 0
B. 1
C. −7
D. −1

### Q27. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A memory access normally takes 200 ns. Independently, a fraction p of accesses incur an additional 10 ms page-fault delay. Ignoring other overhead, what is the greatest p for which mean access time is at most 240 ns?

**Required precision:** Exact finite decimal.

A. 0.000004  
B. 0.999996  
C. 0.000002  
D. 0.500002

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A connected TCP socket receives application writes of lengths3 and5 bytes from its peer. The receiver calls recv with a buffer of8 bytes. Assume no errors and no end-of-stream, but allow arbitrary legal timing. Which statement is correct?

A. The first recv must return exactly3 bytes.  
B. The first recv must return exactly8 bytes.  
C. A successful positive return may contain bytes spanning both writes.  
D. The receiver can infer write boundaries from TCP's byte stream alone.

### Q29. [1 Mark] [MSQ]

An undirected connected graph has a unique minimum-weight edge e crossing a particular nontrivial cut. Which statements hold?

A. Every MST contains e.
B. No MST can contain any other edge crossing that cut.
C. Adding e to an MST that omitted it would allow a strictly lighter crossing edge exchange, contradicting minimality.
D. e must be a bridge in the original graph.

### Q30. [1 Mark] [MSQ]

An invertible matrix A has factorization A=LU, with L unit lower triangular and U upper triangular. To solve Aᵀx=b, which statements are correct?

A. Aᵀ=UᵀLᵀ.
B. Solving Lᵀy=b and then Uᵀx=y always gives the desired x.
C. One can first solve Uᵀy=b, then Lᵀx=y.
D. Lᵀ is unit upper triangular.

### Q31. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Evaluate the integral from 0 to 1 of max(x,1-2x) with respect to x. Round the result to three decimal places.

**Required precision:** Numeric value; 3 decimal places.

A. 0.333  
B. 0.334  
C. 0.834  
D. 0.667

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A bottom-up parser for E→E+T | T and T→id has already reduced the first id in `id+id` to E and shifted `+ id`. Its stack, ignoring states and the bottom marker, is `E + id`; the lookahead is end-of-input. What is the next reduction in the successful reverse-rightmost derivation?

A. E→E+T, reducing the entire stack immediately.  
B. T→id, reducing only the final id.  
C. E→T, reducing the initial E.  
D. No reduction is possible because the input is exhausted.

### Q33. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A microprogrammed controller has a control-store address register, a microinstruction register, and combinational next-address logic. A fetched microinstruction specifies both datapath controls and a conditional next address. Which statements hold?

**Candidates**

**I.** A datapath status flag can influence selection of the next microinstruction.

**II.** The control store must be writable during every machine instruction.

**III.** Several compatible datapath control signals can be asserted by the same microinstruction.

**IV.** Every machine instruction necessarily executes the same number of microinstructions.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q34. [1 Mark] [MCQ]

A half-adder adds bits x,y without a carry input. Which pair gives (sum,carry)?

A. (x XOR y, x AND y)
B. (x OR y, x XOR y)
C. (x AND y, x OR y)
D. (NOT x, NOT y)

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two datasets each contain three real observations. Their medians are2 and9, respectively. Combine all six observations and define the new median as the average of the third and fourth ordered observations. Which assertion is necessarily true?

A. The combined median equals5.5.  
B. The combined median lies in[2,9].  
C. The combined mean lies in[2,9].  
D. The combined median equals one of the original six observations.

### Q36. [2 Marks] [MSQ]

A directed graph has no negative cycle. Potentials h(v) reweight every edge u→v by w'(u,v)=w(u,v)+h(u)−h(v). Which statements are correct?

A. All paths between fixed endpoints have their weights shifted by the same amount.
B. The ordering of path weights between fixed endpoints is preserved.
C. An arbitrary choice of h necessarily makes every edge weight nonnegative.
D. Every directed cycle retains its original total weight.

### Q37. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

How many subgroups of the permutation group S3 are abelian? Include the trivial subgroup and count distinct subgroups, not isomorphism types.

**Required precision:** Integer.

A. 10  
B. 3  
C. 6  
D. 5

### Q38. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Student(S)={(1),(2)}, Enrollment(S,C)={(1,X)}, and Required(C) is empty. No constraint requires an enrolled course to be in Required. Compare:

- QI: all Student identifiers s such that for every c in Required, (s,c) is in Enrollment.
- QII: relational division Enrollment ÷ Required, with candidate S values taken from the projection of Enrollment on S.

Using set semantics, what are the results (QI,QII)?

A. (empty,empty)  
B. ({1},{1})  
C. ({1,2},{1,2})  
D. ({1,2},{1})

### Q39. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A comparison-based search probes a sorted array of15 distinct keys by repeatedly choosing the middle of the remaining interval. What is the maximum number of key comparisons for a successful search?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q40. [2 Marks] [NAT]

A three-bit synchronous machine interprets its state as an unsigned integer s. For s∈{0,1,2,3,4}, its next state is (s+1) mod 5. Invalid states 5,6,7 go respectively to 6,2,5 on the next clock. The initial state is chosen uniformly from all eight bit patterns. What is the expected number of clock edges until the machine first reaches a valid state, counting zero if it starts valid?

**Answer format:** Exact finite decimal.

### Q41. [2 Marks] [MCQ]

What does the following conforming C program print? All arithmetic fits in int.

```c
#include <stdio.h>
static void change(int **p, int *q) {
    int *t = *p;
    *p = q;
    *t += **p;
    **p += 1;
}
int main(void) {
    int a[3] = {2,5,9};
    int *p = a;
    change(&p, a+1);
    change(&p, a);
    printf("%d %d %d\n", a[0], a[1], (int)(p-a));
    return 0;
}
```

A. 7 13 0  
B. 8 13 0  
C. 8 6 1  
D. The program has undefined behaviour due to pointer aliasing.

### Q42. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

How many labelled trees on vertices 1,…,6 have degrees d1=3,d2=2,d3=2,d4=d5=d6=1?

**Required precision:** Integer.

A. 24  
B. 6  
C. 12  
D. 13

### Q43. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A lexer has tokens IF for the keyword if and ID for a letter followed by zero or more letters or digits. It first uses longest match and then gives IF priority over ID only when lengths tie. Spaces separate tokens. For input “if if2 iff if”, how many ID tokens are produced?

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A byte-addressed 16-bit address space contains a 16 KiB chip at 0x0000–0x3FFF and an 8 KiB chip at 0x4000–0x5FFF. Both chips use active-high enables and are fully decoded, with A15 the most significant address bit. Which statements are correct?

**Candidates**

**I.** The 16 KiB chip's enable can be NOT A15 AND NOT A14.

**II.** The 8 KiB chip's enable can be NOT A15 AND A14, without considering A13.

**III.** Exactly 32 KiB of the address space is unmapped by these chips.

**IV.** The 8 KiB chip's enable can be NOT A15 AND A14 AND NOT A13.

A. II and IV  
B. III and IV  
C. I and II  
D. I and IV

### Q45. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

For nonnegative integers n, the function below performs no memoization. Count every call, including calls that immediately return.

```text
F(n):
    if n <= 1: return n
    return F(n-1) + F(n-2)
```

When F(6) is evaluated, how many calls have argument2?

**Required precision:** Integer.

A. 10  
B. 5  
C. 3  
D. 6

### Q46. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

The shared integer x is initially 0. Three threads execute exactly once:
```text
A: rA = x;  x = 2*rA + 1;
B: rB = x;  x = rB + 3;
C: rC = x;  x = rC + 5;
```
Each displayed read and each displayed write is separately atomic. Local registers are private. Execution is sequentially consistent, and a thread's read precedes its write. After all six operations have completed, how many distinct final values of x are possible?

A. 24  
B. 6  
C. 12  
D. 13

### Q47. [2 Marks] [MSQ]

A client has a fresh cached DNS address for host h and an HTTP cache entry for a resource on h. The HTTP entry is stale but has an entity tag. Which statements hold?

A. Revalidating the HTTP entry need not require a fresh DNS query.
B. A conditional request can allow the server to confirm reuse of the cached body without resending that body.
C. A valid DNS cache entry guarantees that every cached HTTP resource for h is fresh.
D. Receiving an HTTP response automatically renews the DNS record's TTL.

### Q48. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

L is a nonregular language over alphabetΣ. Which statements must hold?

A. Its complement Σ*\L is nonregular.  
B. L union (Σ*\L) is regular.  
C. Intersecting L with any infinite regular language always gives a nonregular language.  
D. Removing finitely many strings from L leaves a nonregular language.

### Q49. [2 Marks] [MCQ]

A processor first checks L1. Every L1 access takes 1 ns. On an L1 miss it next checks L2, taking an additional 6 ns; on an L2 miss it additionally accesses memory, taking 60 ns. There is no overlap. Initially the L1 miss probability is 0.10 and the L2 local miss probability conditional on an L1 miss is 0.20. An L1 redesign reduces its miss probability to 0.05 but changes its access time to t ns. L2 timing and its conditional miss probability remain unchanged. For strictly lower average access time, which condition on t is necessary and sufficient?

A. t < 1.9 ns  
B. t < 2.8 ns  
C. t < 1.3 ns  
D. t < 3.6 ns

### Q50. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Table A(k) contains1,1,2 and table B(k) contains1,1,3, with no NULLs. Under SQL bag semantics, how many rows does SELECT A.k FROM A JOIN B ON A.k=B.k return?

**Required precision:** Integer.

A. 8  
B. 2  
C. 4  
D. 5

### Q51. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language L satisfies the regular pumping lemma's conclusion for some pumping length. What can be concluded from this fact alone?

A. L is regular, since the condition is sufficient.  
B. L is context-free but not regular.  
C. It does not by itself prove regularity; the lemma supplies a necessary condition.  
D. L must be finite.

### Q52. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two processes P,Q use single-instance resources A,B. P acquires A then requests B; Q acquires B then requests A. Resources cannot be preempted. Which modifications prevent deadlock in every execution of these two processes?

**Candidates**

**I.** Require both to acquire A before acquiring B.

**II.** Require a process to acquire both resources atomically or acquire neither.

**III.** Merely increase each process's CPU priority after it blocks.

**IV.** Allow each process to hold its first resource indefinitely while repeatedly requesting the second.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II

### Q53. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An application sends600 bytes over UDP. UDP adds8 bytes, IPv4 adds20 bytes with no options, and a link protocol adds18 bytes per frame. The link permits at most 400 bytes of IP packet per frame. The sender creates IPv4 fragments with the largest legal payloads, including the UDP header in the original IP payload. How many bytes in total are transmitted in the link frames? Ignore preambles and interframe gaps.

**Required precision:** Exact integer.

A. 1368  
B. 342  
C. 684  
D. 685

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A packet of1200 bits travels through two store-and-forward links, with rates600 and1200 bits/s respectively. Each link has propagation delay0.1 seconds. There is no queueing or processing delay. What is the time from starting transmission on link1 until the final bit arrives at the destination?

**Required precision:** Exact seconds.

A. 6.4  
B. 1.6  
C. 3.2  
D. 4.2

### Q55. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Round-robin scheduling uses quantum two and zero context-switch cost. Jobs P,Q,R arrive at times 0,1,2 with CPU bursts 5,3,1 respectively. Arrivals exactly at a quantum boundary join the ready queue before the just-preempted job. What is the sum of their waiting times?

**Required precision:** Integer.

A. 20  
B. 5  
C. 10  
D. 11

### Q56. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Define sat(x)=min(7,max(−8,x)). All additions below apply this signed four-bit saturation after each addition. For a=7,b=3,c=−3, calculate sat(sat(a+b)+c)−sat(a+sat(b+c)).

**Required precision:** Exact signed integer.

A. -3  
B. -6  
C. -2  
D. -4

### Q57. [2 Marks] [MSQ]

Consider the grammar

```text
S → a A | a B
A → b
B → c
```

The start symbol is S and the terminals are a,b,c. Which statements hold?

A. The grammar as written has an LL(1) conflict in S's row.
B. The language cannot be generated by any LL(1) grammar.
C. Left factoring S into S→aX, X→b|c yields an LL(1) grammar for the same language.
D. The grammar is ambiguous because both S productions begin with a.

### Q58. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An array has indices 0 through 14. A rearrangement moves the old element at index i to index 2i mod 15. To implement this permutation in place, an algorithm processes each nontrivial permutation cycle once, using one temporary element per cycle; a fixed point needs no processing. How many nontrivial cycles must it process?

**Required precision:** Exact integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An expression node has synthesized attribute p, the parity of its integer value. Leaves provide their value modulo2. Addition combines child parities using XOR; multiplication combines them using AND. For expression (u+v)*(v+w)+u*w, how many of the eight assignments of parities to u,v,w make the root parity1?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q60. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Real 4×4 matrices E,F satisfy E²=E, F²=F, EF=FE, rank(E)=3, and rank(F)=2. Which statements must hold?

A. rank(E−F) is either 1 or 3.  
B. trace(E+F)=5.  
C. rank(EF)=2 in every case.  
D. det(E+F) is either 0 or 2.

### Q61. [2 Marks] [MSQ]

Choose a,b independently and uniformly from {0,1,2,3,4}, and define h(x)=(ax+b) mod 5 on the same domain. For two distinct fixed keys x,y, which statements are true?

A. For each ordered pair (r,s) of output values, exactly one pair (a,b) gives h(x)=r,h(y)=s.
B. Every function in this family is a permutation of the domain.
C. The probability h(x)=h(y) is 1/5.
D. After conditioning on a≠0, h(x) and h(y) remain independent uniform variables.

### Q62. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A total decider D exists for language L over a finite alphabet. Consider a machine that enumerates all strings in length-lexicographic order, runs D on each, and prints precisely those D accepts. Which statements are correct?

**Candidates**

**I.** Every string of L is eventually printed.

**II.** If L is empty, the enumerator must eventually halt.

**III.** If L is finite, the enumerator as described can run forever after printing its last member.

**IV.** The construction requires a known uniform bound on D's running time over all inputs.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV

### Q63. [2 Marks] [MSQ]

Use set semantics. R(A,B) contains (1,x),(2,x), and S(B,C) contains (x,p),(x,q). The natural join J=R⋈S is formed. Which statements are correct?

A. J has four tuples.
B. A→C holds in J.
C. Projecting J onto (A,B) recovers R exactly.
D. B is a candidate key of J.

### Q64. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A sequence satisfies a0=0 and a_n=2a_(n−1)+n for n≥1. Find lim as n→∞ of a_n/2ⁿ.

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q65. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A binary floating-point format has four significant bits including the leading 1, and supports all exponents needed here. Rounding is to nearest with ties to an even least significant significand bit. Among the real inputs x=k/16 for integer k from 60 through 68 inclusive, how many round to the floating-point value 4?

**Required precision:** Integer.

A. 14  
B. 7  
C. 4  
D. 8

## ANSWER KEY — MOCK TEST 048

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MSQ | 1 | B, C, D |
| 3 | MCQ | 1 | C |
| 4 | MCQ | 1 | C |
| 5 | MSQ | 1 | A, C, D |
| 6 | MCQ | 2 | A |
| 7 | NAT | 2 | 16 (exact) |
| 8 | MCQ | 2 | C |
| 9 | MSQ | 2 | A, B, C |
| 10 | MSQ | 2 | A, B, C |
| 11 | MCQ | 1 | A |
| 12 | MCQ | 1 | D |
| 13 | MSQ | 1 | A, B, C |
| 14 | MSQ | 1 | A, C, D |
| 15 | MSQ | 1 | A, C |
| 16 | MCQ | 1 | A |
| 17 | MCQ | 1 | C |
| 18 | MSQ | 1 | A, B, D |
| 19 | MSQ | 1 | B, C, D |
| 20 | MSQ | 1 | B, C, D |
| 21 | MCQ | 1 | A |
| 22 | MSQ | 1 | A, C, D |
| 23 | MSQ | 1 | A, B, D |
| 24 | MCQ | 1 | B |
| 25 | MSQ | 1 | A, C |
| 26 | MCQ | 1 | D |
| 27 | MSQ | 1 | B, C, D |
| 28 | MSQ | 1 | A, B, D |
| 29 | MSQ | 1 | A, C |
| 30 | MSQ | 1 | A, C, D |
| 31 | MSQ | 1 | A, B, C |
| 32 | MSQ | 1 | A, C, D |
| 33 | MCQ | 1 | C |
| 34 | MCQ | 1 | A |
| 35 | MSQ | 1 | A, C, D |
| 36 | MSQ | 2 | A, B, D |
| 37 | MCQ | 2 | D |
| 38 | MSQ | 2 | A, B, C |
| 39 | MSQ | 2 | B, C, D |
| 40 | NAT | 2 | 0.75 |
| 41 | MCQ | 2 | B |
| 42 | MCQ | 2 | C |
| 43 | MCQ | 2 | D |
| 44 | MCQ | 2 | D |
| 45 | MCQ | 2 | B |
| 46 | MSQ | 2 | A, B, D |
| 47 | MSQ | 2 | A, B |
| 48 | MCQ | 2 | C |
| 49 | MCQ | 2 | A |
| 50 | MSQ | 2 | A, B, D |
| 51 | MSQ | 2 | A, B, D |
| 52 | MCQ | 2 | D |
| 53 | MSQ | 2 | A, B, D |
| 54 | MCQ | 2 | C |
| 55 | MCQ | 2 | C |
| 56 | MSQ | 2 | B, C, D |
| 57 | MSQ | 2 | A, C |
| 58 | MCQ | 2 | B |
| 59 | MCQ | 2 | C |
| 60 | MCQ | 2 | C |
| 61 | MSQ | 2 | A, C |
| 62 | MCQ | 2 | B |
| 63 | MSQ | 2 | A, C |
| 64 | MCQ | 2 | A |
| 65 | MCQ | 2 | B |
