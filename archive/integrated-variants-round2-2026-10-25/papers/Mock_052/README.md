# GATE CS 2027 — Full-Length Mock Test 052

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

### Q1. [1 Mark] [NAT]

A sequence has a1=2, a2=6 and a(n+2)=2a(n+1)−a(n)+2 for n≥1. Find a6.

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A6-by-4 rectangle has a1-by-1 square removed at each of its four corners. Count all exposed edges of the remaining shape. What is its perimeter?

**Answer format:** Integer length units.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sentence has correct subject–verb agreement?

A. Each of the reports have an appendix.  
B. The list of required documents are on the desk.  
C. Neither of the two proposed routes is suitable.  
D. The results of the experiment indicates a change.

### Q4. [1 Mark] [NAT]

A uniform mixture of two grains has average cost50 currency units per kilogram. Five kilograms are removed and replaced by five kilograms of grain costing40 per kilogram. The resulting average is45 per kilogram. What was the mixture's original mass?

**Answer format:** Exact number of kilograms.

### Q5. [1 Mark] [NAT]

An integer x is in {1,2,3,4}. Exactly two of these statements are true: x≤2; x is even; x=3. What is x?

**Answer format:** Integer.

### Q6. [2 Marks] [MCQ]

A plane transformation T maps (x,y) to (1−y,x). Starting at (1,0), apply T exactly 2027 times. What is the final point?

A. (1,1)
B. (0,1)
C. (0,0)
D. (1,0)

### Q7. [2 Marks] [MCQ]

A researcher writes: “No failure was observed in a hundred trials. This excludes failure in those trials but does not establish that failure is impossible.” Which additional claim conflicts with that qualification?

A. The observed failure count was zero.
B. The tested system may still fail in an untested situation.
C. Future observations could require revising the assessment.
D. A future failure is logically impossible solely because of these trials.

### Q8. [2 Marks] [NAT]

How many six-digit positive integers use each digit 0,1,2,3,4,5 exactly once and are divisible by 5? A six-digit integer cannot begin with 0.

**Answer format:** Integer.

### Q9. [2 Marks] [MSQ]

A dataset contains 1 twice, 3 three times and 7 once. Two additional observations, both equal to x, are added. The resulting mean is 4. Which statements are correct about the resulting eight observations?

A. x=7.  
B. The median is 3.  
C. There is a unique mode, 7.  
D. The range is 6.

### Q10. [2 Marks] [NAT]

A 180 km journey consists of two equal-distance parts. A vehicle covers the first at 45 km/h. It stops for 30 minutes and then covers the second part at a constant speed. If its overall average speed, including the stop, is 40 km/h, what is its speed on the second part?

**Answer format:** Integer km/h.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A NAT rewrites an outgoing IPv4 packet's source address and TCP source port. Assume ordinary checksums are used and no checksum offload is involved. Which statements are correct?

**Candidates**

**I.** The IPv4 header checksum must reflect the address change.

**II.** The TCP checksum may need updating because it covers the TCP header and an IP pseudo-header.

**III.** The TCP checksum covers only application payload, so ports are irrelevant.

**IV.** Changing an IPv4 address never affects transport-layer checksum calculation.

A. I and III  
B. I and IV  
C. I and II  
D. II and III

### Q12. [1 Mark] [MSQ]

For a directed simple graph on n labelled vertices, an adjacency matrix M stores M[u,v]=1 exactly when u→v exists. There are no self-loops. Which statements are correct?

A. A diagonal entry of M² counts directed walks of length two returning to that vertex.
B. The sum of all entries of M always equals twice the number of directed edges.
C. Transposing M reverses every edge.
D. A zero diagonal of M implies a zero diagonal of M².

### Q13. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under SQL's usual three-valued logic, table T(x) contains rows 1,2,NULL, and table U(y) contains rows 2,NULL. Which statements are correct?

**Candidates**

**I.** `SELECT x FROM T WHERE x NOT IN (SELECT y FROM U)` returns no rows.

**II.** `SELECT x FROM T WHERE NOT EXISTS (SELECT 1 FROM U WHERE U.y=T.x)` returns the rows 1 and NULL.

**III.** Removing NULL from U makes the NOT IN query return both 1 and NULL.

**IV.** Replacing NOT IN with IN in the first query returns three rows.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q14. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two established TCP connections terminate at the same server IPv4 address and local port. Which statements are correct?

**Candidates**

**I.** They may be distinguished by different remote IPv4 addresses or remote ports.

**II.** The shared local port alone forces the two connections to be the same connection.

**III.** The connection-identifying four-tuple includes both endpoint addresses and both endpoint ports.

**IV.** Every established server-side connection must use a different local port.

A. I and III  
B. I and II  
C. I and IV  
D. II and III

### Q15. [1 Mark] [NAT]

Initially one single-threaded process executes the following pseudocode. Every fork succeeds; a child returns0 from fork, and the parent returns a positive value. No process exits early.

```text
x = fork();
if x == 0 {
    fork();
} else {
    fork();
    fork();
}
```

How many processes, including the original, reach the end?

**Answer format:** Exact integer.

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relation R contains finitely many integers, while the domain of possible integers is infinite. Consider the tuple-calculus query {x | NOT R(x)}, with no restriction to the active domain. Which statement is correct?

A. It is not range-restricted and its result can be infinite even though R is finite.  
B. Its result must be a subset of R.  
C. Its result is always empty.  
D. Negation makes every tuple-calculus query safe automatically.

### Q17. [1 Mark] [NAT]

A dataset of four values has mean 5 and population variance 4. Append two more observations, both equal to the old mean. What is the new population variance?

**Answer format:** Decimal rounded to four places.

### Q18. [1 Mark] [MSQ]

A cover-minimization procedure has two feasible covers: C1 uses two rows with total cost8; C2 uses three rows with total cost6. Each is assumed optimal for the count/cost pair shown, and no other cover improves either objective. Which statements are correct?

A. Minimizing row count first and total cost second selects C1.
B. Minimizing total cost first and row count second selects C2.
C. The two objectives necessarily choose the same cover.
D. Reporting only “minimum cover” without specifying the objective can be ambiguous here.

### Q19. [1 Mark] [MCQ]

A processor initially spends half its execution time stalled for memory and half doing other work. An upgrade halves only the memory-stall time for the same program and input. What is the overall speedup?

A. 2
B. 3/2
C. 4/3
D. 1

### Q20. [1 Mark] [NAT]

A 16 KiB cache has four ways and 64-byte lines. How many sets does it have? Count data capacity only; 1 KiB=1024 bytes.

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A3-to-8 decoder has active-high outputs and an active-high enable. Two such decoders form a4-to-16 decoder, sharing the lower three address bits. One is enabled by the highest address bit and the other by its complement. For each valid stable input, how many of the sixteen outputs are high?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

Let G be the additive group of integers modulo12. Define a group homomorphism f:G→G by f(x)=8x modulo12. How many cosets of the kernel of f are there in G?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A directed graph has edges s→a of weight0, a→b of weight0, b→t of weight4, and s→t of weight5. A programmer adds the same positive integer c to every edge weight before finding a shortest path. What is the smallest c for which the direct edge s→t becomes strictly cheaper than the three-edge route?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

Two blocking message queues A and B each have capacity one and are initially empty. Process P sends two messages to A before receiving from B. Process Q sends two messages to B before receiving from A. Both processes are eventually scheduled, and neither removes messages in any other way. What happens?

A. Both processes necessarily complete because the queues start empty.
B. Only P can block; Q cannot.
C. Both eventually block on their second send, with neither able to reach its receive.
D. Sending to a full queue automatically deletes the older message.

### Q25. [1 Mark] [MSQ]

A bipartite graph has left vertices a,b,c and right vertices1,2,3. Its edges are a–1,a–2,b–2,c–2,c–3. Which statements are correct?

A. The graph has exactly one perfect matching.
B. Removing edge a–2 destroys every perfect matching.
C. Edge b–2 belongs to every perfect matching.
D. Adding edge b–1 creates a second perfect matching.

### Q26. [1 Mark] [NAT]

Let h be a homomorphism from binary words to words over {a,b}, defined by h(0)=ab and h(1)=aabb. How many binary words w satisfy h(w)∈a*b*? Include the empty word when applicable.

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

Relations R(A)={1,2,3} and S(B)={x,y} use set semantics. How many tuples remain in their Cartesian product after removing every tuple whose A component equals 2?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

Among permutations π of {1,2,3,4,5}, how many satisfy π(1)≠1 and π(2)≠2? No restriction is placed on the other positions.

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A counting semaphore is initialized to2. Three threads each execute wait(S), then enter a region, and signal(S) only upon leaving it. All semaphore operations are atomic. Before any thread leaves the region, what is the maximum number of threads that can have entered it?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

A virtually indexed, physically tagged cache has 32 KiB data capacity and 64-byte lines. Pages are 4 KiB. To keep every set-index bit within the page offset, what is the minimum power-of-two associativity? Ignore all metadata and use conventional contiguous offset/index fields.

**Answer format:** Integer number of ways.

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proposed proof applies the regular-language pumping lemma to L={0ⁿ1ⁿ:n≥0}. After choosing w=0ᵖ1ᵖ, it picks the particular decomposition x=ε,y=0,z=0^(p−1)1ᵖ and shows that this decomposition fails when pumped. What must be repaired to make the argument valid?

A. The proof must show failure for every decomposition satisfying |xy|≤p and |y|>0.  
B. The proof must show that L is finite.  
C. Pumping down is forbidden; only pumping up is permitted.  
D. The selected word must have length less than p.

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What does this C program print? Assume a conforming C implementation.

```c
#include <stdio.h>
int main(void) {
    int a[2][3] = {{2,4,6},{1,3,5}};
    int (*p)[3] = a;
    int *q = p[1];
    p[0][2] += q[1];
    int *r = p[0] + 1;
    *r++ = q[0];
    q[2] = *r;
    printf("%d\n", a[0][1] + a[1][2]);
    return 0;
}
```

A. 7  
B. 10  
C. 13  
D. The program has undefined behaviour.

### Q33. [1 Mark] [MCQ]

A syntax-directed translation emits each operand when recognized and emits a binary operator after translating both operands. Multiplication binds more tightly than addition. What does it emit for a+b*c?

A. ab+c*
B. +a*bc
C. abc*+
D. abc+*

### Q34. [1 Mark] [NAT]

A binary search finds the first array position whose value is at least7 in the sorted array[2,7,7,7,9]. Positions are zero-based and the returned position may be the array length if no value qualifies. What is the returned position?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A formal power series F(x) satisfies(1−x)²F(x)=1+x. What is the coefficient of x4 in F(x)?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A relation R(A,B,C) uses domains of sizes 3,4,5, respectively, and satisfies AB→C and AC→B. Tuples are distinct. What is the maximum possible number of tuples in R?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A system has two resource types A and B. It uses the Banker's safety test. Current allocation and maximum claims are:

| Process | Allocation (A,B) | Maximum (A,B) |
|---|---|---|
| P0 | (1,0) | (2,2) |
| P1 | (0,1) | (1,2) |
| P2 | (1,1) | (3,1) |

The available vector is (1,1). P0 requests (0,1). The request is within its remaining claim and the available resources. Which conclusion is correct?

A. Grant it: P0,P1,P2 is a safe sequence afterward.  
B. Grant it: P2,P1,P0 is a safe sequence afterward.  
C. Defer it: the present state is safe, but the tentative grant is unsafe.  
D. Defer it: the present state is already unsafe.

### Q38. [2 Marks] [NAT]

A pipeline has four stages whose combinational delays are2,3,10,4ns. Each stage adds1ns register overhead to the clock-period requirement. A redesign splits the10ns stage into two5ns stages with the same overhead per stage. There are100 independent instructions, no stalls, and initially empty pipelines. How many nanoseconds does the redesign save from first launch to the last instruction's completion?

**Answer format:** Integer nanoseconds.

### Q39. [2 Marks] [MSQ]

Parent(a,b) has the single row (1,2), with composite primary key (a,b). Child(a,b,qty) has a composite foreign key referencing Parent with MATCH SIMPLE, and CHECK(qty>0). All Child columns allow NULL. MATCH SIMPLE skips the referential check when either foreign-key component is NULL; a CHECK rejects only FALSE, not UNKNOWN. Starting with an empty Child table, which individual insertions succeed?

A. (1,NULL,5)  
B. (NULL,9,−1)  
C. (9,9,NULL)  
D. (1,2,NULL)

### Q40. [2 Marks] [MSQ]

A TCP peer performs an orderly shutdown of its sending direction after transmitting some bytes. The receiver drains all those bytes. Assume no errors. Which statements are correct?

A. A subsequent receive can return zero to indicate end-of-stream in that direction.
B. The receiver must treat zero as one received byte whose value is0.
C. A half-close does not by itself prevent the other direction from carrying data.
D. TCP requires both applications to terminate immediately when one direction closes.

### Q41. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A total computable function maps every pair(machine M,input w) to a machine N that ignores its own input, simulates M on w and accepts if that simulation accepts. Which statements are correct?

A. If M accepts w, N recognizes all strings.  
B. If M does not accept w, N recognizes the empty language.  
C. A decider for whether N's language is empty would decide arbitrary machine acceptance.  
D. The construction requires deciding whether M accepts w before producing N.

### Q42. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the following control-flow graph. Variables are ordinary scalars without aliases, both branches are feasible, and only the returned value is observable. A variable is live at a point if some path from that point reads its current value before redefining it.

```text
B1: x = a+b
    y = x*c
    if p goto B2 else B3
B2: z = y+1
    goto B4
B3: x = a-b
    z = x+c
    goto B4
B4: return z
```

At the point immediately after `y=x*c` and before the conditional, which statements are correct?

A. y is live.  
B. c is dead.  
C. x is dead.  
D. a is live.

### Q43. [2 Marks] [NAT]

A single CPU uses preemptive shortest-remaining-processing-time scheduling, with no switching overhead. Processes P,Q,R arrive at times0,1,3 and require CPU times7,4,1 respectively. When remaining times tie, the currently running process continues. What is the sum of their waiting times?

**Answer format:** Integer time units.

### Q44. [2 Marks] [NAT]

A synchronous circuit has two flip-flops storing bits A,B. Their next-state equations are A'=A XOR B and B'=NOT A, both evaluated from the old state. Starting at(A,B)=(0,0), what is the smallest positive number of clock edges after which the circuit returns to(0,0)?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A byte-addressed machine loads a32-bit word using effective address Rbase+4×Rindex−8. Initially Rbase=100 and Rindex=3. Memory bytes at addresses104 through111 are 01,02,03,04,05,06,07,08 in hexadecimal. The machine is little-endian. What is the decimal value of the least significant16 bits of the loaded word?

**Answer format:** Exact integer.

### Q46. [2 Marks] [NAT]

The domain is the labeled set {a,b}. How many binary relations R on this domain satisfy both FOR ALL x EXISTS y R(x,y) and EXISTS x FOR ALL y R(x,y)?

**Answer format:** Exact integer.

### Q47. [2 Marks] [NAT]

A signed eight-bit fixed-point format has three fractional bits. An exact real result of 17 is converted to this format using saturation to the largest representable value on positive overflow. What real value is stored?

**Answer format:** Exact finite decimal.

### Q48. [2 Marks] [MSQ]

A procedure returns a nested function that references a local variable of the procedure. The language permits calling that function after the procedure returns. Which statements are correct?

A. The referenced variable's storage must remain valid for the later call.
B. A raw pointer into an ordinary reclaimed stack frame always suffices.
C. A closure can carry access to a separately retained environment.
D. Lexical scope alone implies that every activation record may be discarded immediately on return without preserving anything.

### Q49. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An n-bit ALU, n≥2, computes A−B as A+(NOT B)+1. Which statements hold when carry-out is retained separately from the n-bit result?

A. Carry-out 1 indicates no borrow in unsigned subtraction.  
B. The retained result represents (A−B) modulo 2ⁿ.  
C. Unsigned borrow and signed overflow are always the same event.  
D. Signed subtraction overflow can occur when A and B have opposite signs and the result's sign differs from A's.

### Q50. [2 Marks] [NAT]

Over alphabet {0,1}, a DFA must accept exactly strings whose length is divisible by3 and whose number of1s is even. What is the minimum number of states in a complete DFA?

**Answer format:** Exact integer.

### Q51. [2 Marks] [NAT]

A recursive procedure enumerates subsets of positions 1 through 5 with no two adjacent positions selected. At each position, it always makes a recursive call excluding that position. It also makes a call including it if the previous position was not selected. After position 5 it outputs once and returns. The initial call handles position 1 with no previous position selected. How many nonleaf calls occur, counting separate calls even when their remaining-position arguments coincide?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

Let A be the real 4x4 matrix

```text
A = [0 1 0 0]
    [0 0 1 0]
    [0 0 0 1]
    [1 0 0 0].
```

How many real matrices X simultaneously satisfy X=X^T, AX=XA, X^2=X, and X*(1,1,1,1)^T=0?

**Answer format:** Numeric value; integer.

### Q53. [2 Marks] [MSQ]

For grammar S→aSb | T and T→cT | ε, which statements are true?

A. Every generated word has equally many a and b symbols.
B. Every generated word has all c symbols between its a and b blocks.
C. The grammar generates abcc.
D. The grammar generates aacbb.

### Q54. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An IP router forwards a packet across two different Ethernet links. The packet's IPv4 source and destination are unchanged by assumption; TTL is decremented. Which statements are correct?

A. The outgoing Ethernet header can differ from the incoming Ethernet header.  
B. The IPv4 header checksum must account for the TTL change.  
C. End-to-end IP destination being unchanged requires the Ethernet destination address to remain unchanged on every hop.  
D. Link-layer addressing and network-layer addressing serve different scopes.

### Q55. [2 Marks] [MCQ]

Consider the schedule `w1(x), w2(x), w1(x), w2(y), r3(y), w3(z)`, followed by commits of all three transactions. The subscripts identify transactions; writes are blind writes of distinct values. There are no other reads or writes. For view equivalence, preserve every read-from relationship and the identity of the final writer of each item. Which pair correctly states whether the schedule is conflict serializable and the number of serial transaction orders view equivalent to it?

A. Not conflict serializable; 2 orders
B. Conflict serializable; 2 orders
C. Not conflict serializable; 0 orders
D. Conflict serializable; 1 order

### Q56. [2 Marks] [NAT]

A 0/1 knapsack has capacity 8 and five distinct items with (weight,value): A=(2,3), B=(2,3), C=(3,4), D=(3,4), E=(4,5). Each may be selected at most once. How many distinct subsets attain the maximum possible value without exceeding capacity? Subsets differing only by A versus B or C versus D still count as distinct.

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler translates `x != 0 && 10/x > 1` using left-to-right short-circuit evaluation over exact integers, with division by zero raising an observable exception. Which transformations preserve behaviour for every x?

**Candidates**

**I.** Test x!=0 first and branch around the division when false.

**II.** Evaluate 10/x before testing x!=0 for all x.

**III.** Replace the conjunction by an evaluation that performs the division only on the x!=0 branch.

**IV.** Replace the whole expression by true because 10 is positive.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II

### Q58. [2 Marks] [NAT]

Jobs have unit processing time and pairs (deadline,profit): A=(1,20), B=(2,15), C=(2,30), D=(3,10). At most one job is executed in each integer slot, and a job in slot k meets deadline d when k≤d. All jobs are available initially. What is the maximum total profit from jobs completed by their deadlines?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A binary floating-point system has precision p=4 significant bits, includes an implicit leading1 for normalized numbers, and has enough exponent range for all numbers here. It rounds to nearest, ties to even. Compute fl(fl(8+0.5)+0.5), rounding after each addition. What value results?

**Answer format:** Exact decimal or integer.

### Q60. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For x≠0 define g(x)=sin(1/x). Which statements are correct?

A. There exists a sequence of positive x approaching0 on which g(x)=1.  
B. There exists a sequence of positive x approaching0 on which g(x)=−1.  
C. The limit of xg(x) as x approaches0 is0.  
D. Assigning g(0)=0 makes g continuous at0.

### Q61. [2 Marks] [MCQ]

A singly linked list initially consists of six distinct nodes with values 1,2,3,4,5,6 in that order, followed by NULL. The following pointer operations are executed. Node fields are modified in place; no nodes are allocated or freed.
```text
p = head
q = NULL
while p != NULL and p.next != NULL:
    r = p.next
    p.next = r.next
    r.next = q
    q = r
    p = p.next
```
Which pair gives the lists reached from (head, q) after termination?

A. (1→3→5, 2→4→6)  
B. (1→3→5, 6→4→2)  
C. (1→5, 6→4→3→2)  
D. (1→2→3, 6→5→4)

### Q62. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

### Q63. [2 Marks] [NAT]

X and Y are independent numbers of failures before the first success in repeated independent Bernoulli trials, each with success probability 1/3. What is E[min(X,Y)]?

**Answer format:** Decimal rounded to two places.

### Q64. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Binary Huffman coding is applied to five symbols with weights 1,1,2,2,4. Ties may be resolved arbitrarily. Which codeword lengths can the weight-4 symbol receive in a resulting Huffman tree? The root has depth zero.

**Candidates**

**I.** 1

**II.** 2

**III.** 3

**IV.** 4

A. I and II  
B. II and III  
C. II and IV  
D. III and IV

### Q65. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A disk uses shortest-seek-time-first scheduling. New requests may arrive while earlier requests wait. Which statements are correct?

**Candidates**

**I.** A sufficiently persistent stream of nearby requests can postpone a distant pending request indefinitely.

**II.** SSTF guarantees bounded waiting for every request without any restriction on arrivals.

**III.** If only finitely many requests exist and no new ones arrive, repeated service eventually serves all of them.

**IV.** SSTF must visit the highest-numbered cylinder before every direction reversal.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

## ANSWER KEY — MOCK TEST 052

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 42 |
| 2 | NAT | 1 | 20 |
| 3 | MSQ | 1 | A, B, D |
| 4 | NAT | 1 | 10 |
| 5 | NAT | 1 | 2 |
| 6 | MCQ | 2 | C |
| 7 | MCQ | 2 | D |
| 8 | NAT | 2 | 216 (exact) |
| 9 | MSQ | 2 | A, B, D |
| 10 | NAT | 2 | 45 |
| 11 | MCQ | 1 | C |
| 12 | MSQ | 1 | A, C |
| 13 | MCQ | 1 | C |
| 14 | MCQ | 1 | A |
| 15 | NAT | 1 | 6 |
| 16 | MSQ | 1 | B, C, D |
| 17 | NAT | 1 | 2.6667 (accepted range 2.66665–2.66675) |
| 18 | MSQ | 1 | A, B, D |
| 19 | MCQ | 1 | C |
| 20 | NAT | 1 | 64 |
| 21 | NAT | 1 | 1 |
| 22 | NAT | 1 | 3 |
| 23 | NAT | 1 | 1 |
| 24 | MCQ | 1 | C |
| 25 | MSQ | 1 | A, C, D |
| 26 | NAT | 1 | 3 |
| 27 | NAT | 1 | 4 |
| 28 | NAT | 1 | 78 |
| 29 | NAT | 1 | 2 |
| 30 | NAT | 1 | 8 |
| 31 | MSQ | 1 | B, C, D |
| 32 | MSQ | 1 | A, C, D |
| 33 | MCQ | 1 | C |
| 34 | NAT | 1 | 1 |
| 35 | NAT | 1 | 9 |
| 36 | NAT | 2 | 12 |
| 37 | MSQ | 2 | A, B, D |
| 38 | NAT | 2 | 509 |
| 39 | MSQ | 2 | A, D |
| 40 | MSQ | 2 | A, C |
| 41 | MCQ | 2 | D |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 6 |
| 44 | NAT | 2 | 3 |
| 45 | NAT | 2 | 513 |
| 46 | NAT | 2 | 5 |
| 47 | NAT | 2 | 15.875 |
| 48 | MSQ | 2 | A, C |
| 49 | MCQ | 2 | C |
| 50 | NAT | 2 | 6 |
| 51 | NAT | 2 | 19 |
| 52 | NAT | 2 | 4 (exact) |
| 53 | MSQ | 2 | A, B, D |
| 54 | MCQ | 2 | C |
| 55 | MCQ | 2 | A |
| 56 | NAT | 2 | 3 |
| 57 | MCQ | 2 | A |
| 58 | NAT | 2 | 60 |
| 59 | NAT | 2 | 8 |
| 60 | MCQ | 2 | D |
| 61 | MCQ | 2 | B |
| 62 | MSQ | 2 | A, B, C |
| 63 | NAT | 2 | 0.80 (two decimals) |
| 64 | MCQ | 2 | A |
| 65 | MCQ | 2 | D |
