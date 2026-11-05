# GATE CS 2027 — Full-Length Mock Test 071

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

A rule returns the median of an odd-length list of real numbers. To the list, append one number strictly smaller than every original entry and one strictly larger than every original entry. What follows about the returned median?

A. It is unchanged.  
B. It strictly increases.  
C. It becomes the average of the two appended numbers.  
D. It cannot be related to the original median without knowing every entry.

### Q2. [1 Mark] [NAT]

Some unit cubes occupy cells of a2×2×2 grid. Looking along each of the three coordinate axes, all four cells in the corresponding2×2 projection must appear occupied. What is the minimum possible number of unit cubes?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

Five consecutive readings should form a sequence whose consecutive differences increase by the same amount. The displayed readings are 3,8,16,25,41. Exactly one reading was copied incorrectly. What is the corrected value of that reading?

**Answer format:** Integer.

### Q4. [1 Mark] [NAT]

A rectangle has perimeter 40 cm and area 96 cm². Its longer side is increased by 1 cm and its shorter side decreased by 1 cm. By how many square centimetres does its area decrease?

**Answer format:** Integer.

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Select the pair completing the sentence with correct subject–verb agreement: “One of the proposals that ___ discussed yesterday ___ now been withdrawn.”

A. was, have  
B. were, have  
C. was, has  
D. were, has

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A bag contains two red and two blue balls. Balls are drawn uniformly without replacement until the first red ball is drawn, and then drawing stops. What is the expected number of balls left in the bag? Round to three decimal places.

**Required precision:** Number to 3 decimal places.

A. 2.333  
B. 4.666  
C. 1.167  
D. 3.333

### Q7. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Exactly one of four labeled boxes A,B,C,D contains a token. Their labels state:

- A: “The token is in B or C.”
- B: “The token is in A.”
- C: “The token is not in C.”
- D: “The token is in D.”

Exactly two labels are true. How many possible token locations are consistent with this information?

**Required precision:** Exact integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q8. [2 Marks] [NAT]

A square sheet occupies 0≤x≤8 and 0≤y≤8. First fold its right half onto its left half along x=4, then fold the upper half of the folded sheet downward along y=4. A hole is punched through every layer at (1,2) in the folded sheet. After unfolding, what is the sum of the x-coordinates of all distinct holes?

**Answer format:** Integer.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A switch is either ON or OFF. A says, “The switch is ON.” B says, “A's statement is false.” C says, “The switch is OFF.” Exactly two of the three statements are true. Which conclusions follow?

A. The switch is OFF.  
B. A and B are both truthful.  
C. B and C are truthful.  
D. The information is inconsistent.

### Q10. [2 Marks] [NAT]

Six distinct students A,B,C,D,E,F are partitioned into two unlabelled groups of three. One leader is chosen in each group. A and B must be in different groups, C must lead the group containing C, and B must not be a leader. How many different group-and-leader assignments are possible? Swapping the names or display order of the two groups does not create a new assignment.

**Answer format:** Exact integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

X is uniformly distributed over {−2,−1,0,1,2}, and Y=X². What is E[Y²]?

**Answer format:** Exact decimal.

### Q12. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An undirected multigraph has three vertices, two parallel edges between vertices 1 and 2, one edge between 2 and 3, and one self-loop at vertex 3. In the standard degree convention a self-loop contributes two. What is the sum of vertex degrees?

**Required precision:** Integer.

A. 16  
B. 4  
C. 9  
D. 8

### Q13. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An IPv4 fragment has a 20-byte header, 800 payload bytes, fragment offset 100, and MF=1. It encounters an MTU of 420 bytes and is split into two fragments with equal payloads. What is the fragment offset field of the second new fragment?

**Required precision:** Exact integer.

A. 150  
B. 300  
C. 75  
D. 151

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A DMA transfer moves 4 KiB using bursts of 16 bytes. Each burst occupies the memory bus for 3 cycles, and different bursts do not overlap. How many bus cycles are occupied by the transfer? Here 1 KiB=1024 bytes.

**Required precision:** Integer.

A. 768  
B. 1536  
C. 384  
D. 769

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

B is a 3×4 array of four-byte elements stored in row-major order, with B[0][0] at byte address 1000. A transposed view C is defined by C[i][j]=B[j][i], without copying any elements. What is address(C[1][2])−address(C[0][1]), in bytes?

**Required precision:** Integer.

A. 40  
B. 20  
C. 10  
D. 21

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A three-variable Karnaugh map represents F=1 exactly when an even number of inputs are1. There are no don't-care entries. Which statement about a two-level SOP using only uncomplemented or complemented input literals is correct?

A. One four-cell group covers all1-cells.  
B. Two two-cell groups cover all1-cells.  
C. Four singleton groups are required.  
D. No SOP can represent this function.

### Q17. [1 Mark] [NAT]

Five real observations all lie in [−1,1], have mean0, and have median0. What is the largest possible population variance?

**Answer format:** Exact decimal.

### Q18. [1 Mark] [NAT]

A file occupies eight data blocks. Its only directory link is removed while one process still has the file open. Assume blocks are reclaimed only when both link count and open-reference count become zero. How many of its data blocks are reclaimed by this unlink operation itself?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A stack stores pairs(value,current minimum). Pushing x stores(x,min(x,previous minimum)); on an empty stack it stores(x,x). Execute push5,push2,push2,pop,push4,pop,pop. What minimum is stored in the final top pair?

**Answer format:** Exact integer.

### Q20. [1 Mark] [NAT]

Remove a perfect matching from the complete bipartite graph K3,3. How many spanning trees does the remaining graph have?

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A complete DFA has a start state that is accepting and one rejecting sink. On a it remains in the start state, and on b it enters the sink, which loops on both letters. How many strings of length4 over{a,b} does it accept?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q22. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For real t, let A be the matrix below. An LU factorization here means A=LU without row exchanges, with L lower triangular with diagonal entries1 and U upper triangular. Which statements hold?

```text
A = [ t  1
      1  0 ]
```

A. A is invertible for every real t.  
B. Such an LU factorization exists for t=0.  
C. Such an LU factorization exists for every nonzero t.  
D. For nonzero t, U22=−1/t.

### Q23. [1 Mark] [NAT]

A successful read system call requests10 bytes but returns4, having copied four bytes and advanced the regular file's offset by four. The caller then successfully reads the remaining six bytes. If the initial offset was20 and no seeks occur, what is the final offset?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Routers A,B,C use synchronous distance-vector updates for destination C. Link costs are A–B=1, B–C=1 and A–C=10. Initially routes are converged. Link B–C fails immediately before round 1. In every round each router recomputes its distance using its still-working links and the neighbours' distances from the end of the preceding round; C always advertises 0. No split horizon, poison reverse or triggered intermediate updates are used. What distance does A advertise after round 2?

**Answer format:** Numeric value; integer.

### Q25. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A pipeline issues one instruction per cycle except for branch-misprediction stalls. Branches are 20% of instructions, 25% of branches are mispredicted, and every misprediction adds four nonoverlapping stall cycles. Ignoring filling and draining, find its average CPI.

**Required precision:** Exact finite decimal.

A. 2.4  
B. 1.2  
C. 0.6  
D. 2.2

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Over alphabet{a,b}, how many strings of length3 belong to the language described by the regular expression(a|ba)*?

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A committed transaction's update is lost after a crash despite the system acknowledging its commit. Which ACID property is directly violated?

A. Durability  
B. Atomicity necessarily, even if every update of that transaction was lost together  
C. Isolation only  
D. No property, because crashes are excluded from ACID concerns

### Q28. [1 Mark] [MCQ]

A lexer recognizes identifiers by `[a-z][a-z0-9]*`, the keyword `if`, and operators `==`, `=`, `++`, `+`. It uses maximal munch; an identifier lexeme exactly equal to `if` is classified as a keyword. Whitespace is ignored. What token-lexeme sequence is produced for `ifx==if+++x`?

A. if, x, ==, if, ++, +, x  
B. ifx, ==, if, ++, +, x  
C. ifx, =, =, if, +, ++, x  
D. ifx, ==, if, +++, x

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler considers common-subexpression elimination in this fragment. Arithmetic is exact, and a,b,c,d are distinct variables.

```text
if p { t=a+b; } else { t=c+d; }
u=a+b;
```

Which proposed justification for replacing u=a+b by u=t is valid?

A. The expression a+b appears earlier in the text, so the replacement is always valid.  
B. The replacement is valid if c+d=a+b is proved on every execution taking the else branch.  
C. The replacement is valid merely because neither a nor b changes in the fragment.  
D. The replacement is valid merely because both branches assign t.

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A depth-first search of an undirected simple graph records parent pointers. Which statements hold?

**Candidates**

**I.** Every edge joining an ancestor to a descendant can be represented as a tree edge or a back edge.

**II.** A non-tree edge necessarily joins vertices in unrelated DFS subtrees.

**III.** An edge to the parent should not by itself be treated as evidence of a cycle.

**IV.** DFS discovery order must equal breadth-first discovery order.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV

### Q31. [1 Mark] [MSQ]

T1 holds an exclusive lock on x and requests y. T2 holds an exclusive lock on y and requests x. No locks are released until commit or abort. Which statements are correct?

A. Both transactions can remain blocked indefinitely without intervention.
B. Aborting either transaction and releasing all its locks can allow the other to proceed.
C. Two-phase locking makes this wait cycle impossible.
D. Both transactions must commit simultaneously to resolve it.

### Q32. [1 Mark] [MSQ]

Under strict two-phase locking, exclusive locks are retained until commit or abort. Which statements are correct?

A. Another transaction cannot read an item modified under an unreleased exclusive lock.
B. Retaining exclusive locks prevents cascading aborts caused by reading those uncommitted writes.
C. The rule alone makes deadlock impossible.
D. A transaction may release an exclusive lock immediately after its write under this strict rule.

### Q33. [1 Mark] [NAT]

A real upper-triangular 3×3 matrix A has diagonal entries 1,2,3; entries above the diagonal are arbitrary. Find det(A²−A−I), where I is the identity.

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For connected undirected weighted graphs, which statements are correct?

**Candidates**

**I.** Repeated edge weights make a unique MST impossible.

**II.** Pairwise distinct edge weights guarantee a unique MST.

**III.** If the graph itself is a tree, it has a unique spanning tree regardless of repeated weights.

**IV.** A globally heaviest edge can never belong to an MST, even if it is a bridge.

A. II and III  
B. I and IV  
C. II and IV  
D. III and IV

### Q35. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A synchronous two-bit state machine has next-state equations Q1'=Q0 and Q0'=NOT Q1. Starting at00, how many clock edges occur before the state first returns to00?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q36. [2 Marks] [MSQ]

Consider languages over {0,1}. Which statements are true?

A. {wwᴿ : w∈{0,1}*} is context-free.
B. {ww : w∈{0,1}*} is context-free.
C. Restricting {ww : w∈{0,1}*} to the unary alphabet {0} gives a regular language.
D. Every context-free language is closed under intersection with every other context-free language.

### Q37. [2 Marks] [NAT]

In the subset lattice of {a,b,c}, let X={a,b} and Y={b,c}. How many subsets Z satisfy X∩Y⊆Z⊆X∪Y and are incomparable with both X and Y under inclusion?

**Answer format:** Integer.

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A forwarding table routes 10.2.0.0/25 and 10.2.0.128/25 to next hop H, and 10.2.0.64/26 to next hop J. A default route goes to K. Replace the two /25 entries by 10.2.0.0/24→H while retaining the /26 exception and default. Under longest-prefix matching, which statements are true?

**Candidates**

**I.** Every destination keeps the same next hop.

**II.** The /24 aggregate overrides the /26 exception because it was inserted later.

**III.** Destinations outside 10.2.0.0/24 continue using the default route.

**IV.** Removing the /26 exception as well would preserve every destination's next hop.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q39. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A router has routes 10.0.0.0/8 to A, 10.64.0.0/10 to B, 10.96.0.0/11 to C and 10.100.0.0/16 to D. Within 10.96.0.0/11, how many complete /16 blocks are forwarded to C under longest-prefix matching?

**Required precision:** Integer.

A. 62  
B. 16  
C. 31  
D. 32

### Q40. [2 Marks] [NAT]

Assume all array accesses in this C program are valid and int can represent all values shown. What value is returned?

```c
int f(void) {
    int a[4] = {3, 5, 7, 9};
    int *p = a + 1;
    int **q = &p;
    (*q)++;
    **q += a[0];
    return p[-1] + a[2] + (int)(p - a);
}
```

**Answer format:** Exact integer.

### Q41. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A shift-reduce parser has recognized the right-hand side E+T of production E→E+T. The three grammar symbols occupy three stack entries, and reduction pops all three and pushes one E entry. By how many grammar-symbol entries does the stack size decrease?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q42. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A process starts with integer x=1. It forks once, creating independent address spaces. Both parent and child then execute x=x+1. Only the parent forks a second time. Every existing process then prints its own x once and exits. Assuming all forks succeed and output buffering does not duplicate earlier output, what is the sum of the printed integers?

**Required precision:** Integer.

A. 12  
B. 3  
C. 6  
D. 7

### Q43. [2 Marks] [NAT]

A machine uses byte addresses. An instruction has a signed eight-bit displacement, measured in four-byte words relative to the address immediately after the instruction. The next-instruction address is 1000 and the displacement field is 11110110₂. What is the effective target byte address?

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary min-heap contains distinct keys. Decreasing the key at an arbitrary nonroot index may violate heap order with which nodes first?

A. Its parent; upward restoration may be needed.  
B. Only its children; downward restoration is always required.  
C. Every node necessarily becomes invalid.  
D. No heap-order violation can result from decreasing a key.

### Q45. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A circuit maps input bits x,y,z to u=x XOR y, v=y XOR z, w=x XOR z. Let t be the three-input majority bit. Which statements are correct?

**Candidates**

**I.** w=u XOR v.

**II.** The triple(u,v,w) uniquely determines(x,y,z).

**III.** The four outputs(u,v,w,t) uniquely determine(x,y,z).

**IV.** All eight possible triples(u,v,w) occur.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q46. [2 Marks] [NAT]

Four unit-time jobs have (deadline,profit): A(1,70), B(2,60), C(2,50), D(3,40). At most one job runs in each integer slot 1,2,3; a job earns its profit only if completed in a slot no later than its deadline. What maximum total profit is possible?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A disk head at cylinder40 uses SSTF with pending requests at10,45,70. No new requests arrive; ties favour the smaller cylinder. After all requests are served, what is its total head movement?

**Required precision:** Integer cylinders.

A. 180  
B. 45  
C. 91  
D. 90

### Q48. [2 Marks] [NAT]

How many truth assignments to p,q,r,s,t satisfy all five clauses `(p OR q)`, `(NOT p OR r)`, `(NOT q OR r)`, `(NOT r OR s)` and `(NOT s OR t)`?

**Answer format:** Integer.

### Q49. [2 Marks] [NAT]

On the fixed domain {1,2,3}, how many binary relations R satisfy both (∀x ∃y R(x,y)) and NOT(∃y ∀x R(x,y))? Relations are distinguished by their sets of ordered pairs.

**Answer format:** Exact integer.

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For a nondeterministic pushdown automaton, compare acceptance by final state and by empty stack, always requiring all input to be consumed. Which statements are correct?

A. Every language accepted by final state has an empty-stack NPDA recognizing the same language.  
B. The same NPDA with its transitions unchanged always recognizes the same language under either convention.  
C. Every empty-stack NPDA language can also be recognized by a final-state NPDA.  
D. Both conventions characterize context-free languages when suitable machine conversions are allowed.

### Q51. [2 Marks] [NAT]

Relation E(src,dst) is{(a,b),(b,c),(c,a),(a,c)}. Let P contain all pairs(x,z) for which some y satisfies E(x,y) and E(y,z), using set semantics. How many pairs belong to P−E?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A message of6000 data bytes crosses three equal-rate store-and-forward links in sequence. Each link sends1000 bytes per millisecond. There is no propagation or processing delay. Packets have an extra100-byte header and may be pipelined across links. Splitting the message into six equal data packets instead of three equal data packets changes the time until the entire message reaches the destination. How many milliseconds are saved?

**Answer format:** Exact number.

### Q53. [2 Marks] [NAT]

An urn initially contains one red and one blue ball. Draw a ball uniformly, replace it, and add one extra ball of the same color. Then draw a second ball uniformly from the three balls now present. Given that the second ball is red, what is the probability that the first was blue?

**Answer format:** Decimal rounded to four places.

### Q54. [2 Marks] [MSQ]

In first-order notation, consider the query {x : R(x) AND (exists x S(x))}, where the inner quantifier binds only its own occurrence of x and shadows the outer name within its parentheses. R and S are finite unary relations. Which statements are correct?

A. Renaming the bound inner variable to y leaves the query unchanged.
B. The query always returns R intersect S.
C. If S is nonempty, the query returns all of R.
D. If S is empty, the query returns the empty relation.

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In four-variable cube notation, a dash means either bit. Two implicants are 0−0− and −00−. Suppose every minterm in either cube is an ON minterm and all other minterms are OFF, except 1100 and 1101, which are don't-cares. Which statements are correct?

**Candidates**

**I.** The cubes cannot be combined by the ordinary one-bit-difference Quine–McCluskey combination rule because their dash positions differ.

**II.** Their union alone already contains all minterms of −−0−.

**III.** The larger cube −−0− includes an OFF minterm under the specified classification.

**IV.** Using the two don't-cares permits −−0− as a valid implicant covering their union.

A. I and III  
B. II and III  
C. II and IV  
D. I and IV

### Q56. [2 Marks] [MSQ]

A four-bit two's-complement ALU computes subtraction as A+(bitwise NOT B)+1 and discards the final carry. For A=0111 and B=1111, which statements are correct?

A. The four result bits are1000.
B. There is a final carry-out of1.
C. Signed overflow occurs.
D. Interpreting the operands as unsigned integers, the subtraction needs a borrow.

### Q57. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An eight-bit binary floating-point encoding has one sign bit, a three-bit biased exponent and four fraction bits, with the usual sign-and-magnitude ordering of finite magnitudes. Consider only finite, nonzero represented values. Let raw be the unsigned eight-bit encoding. Define T(raw) as the eight-bit bitwise complement of raw for negative values, and raw XOR 0x80 for positive values. Which statements are true?

**Candidates**

**I.** Sorting raw as unsigned integers gives increasing numerical order across both signs.

**II.** Within positive values, unsigned raw order agrees with numerical order.

**III.** Within negative values, larger unsigned raw always represents a numerically larger value.

**IV.** Sorting T(raw) as unsigned integers gives increasing numerical order across both signs.

A. III and IV  
B. I and II  
C. II and IV  
D. I and III

### Q58. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A compiler computes array widths using attributes: width(int)=4 and width(array(n,T))=n×width(T). A record lays out fields without padding. It contains an array(3,array(2,int)) followed by an int. What is its computed width in bytes?

**Required precision:** Integer.

A. 56  
B. 14  
C. 28  
D. 29

### Q59. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An n-bit ripple-carry adder has a carry dependency from each bit to the next. Each stage's carry propagation takes one time unit; inputs are available at time zero. Ignore sum-output delays. Which statements are correct?

**Candidates**

**I.** The final carry may require n time units.

**II.** All carries necessarily settle within one time unit because the stages are physically parallel.

**III.** Grouping carry logic using additional gates can reduce carry depth compared with a ripple chain.

**IV.** Increasing n never changes worst-case carry delay.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q60. [2 Marks] [NAT]

A microprogram has40 microinstructions. Each has12 independent control bits and a next-address field able to address every microinstruction. A redesigned store has the same40 entries but adds a two-bit branch-condition selector to every word. What is the increase in total control-store capacity, in bits?

**Answer format:** Integer.

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A binary max-heap is stored from index 1 as [20,15,18,8,10,12,17]. Delete the element at index 4 by moving the final element into that position and shrinking the array. Restore heap order using swaps with parents or children as necessary. How many swaps are required after the replacement?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q62. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A sequential file stores250 records of120 bytes in4096-byte blocks with a16-byte header per block. Records do not span blocks. How many data blocks are required?

**Required precision:** Integer.

A. 16  
B. 4  
C. 8  
D. 9

### Q63. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Four activities have (start,finish,profit) triples A=(0,2,3), B=(2,4,3), C=(0,4,9), D=(4,5,2). Activities sharing only an endpoint are compatible. A greedy algorithm selects a remaining compatible activity with earliest finish, breaking a tie in favor of earlier alphabetical label. By how much does the maximum achievable total profit exceed this algorithm's profit?

**Required precision:** Exact integer.

A. 6  
B. 3  
C. 2  
D. 4

### Q64. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={w#w^R:w∈{0,1}*}, where # is a distinct separator and w^R reverses w. Which statements are correct?

A. A deterministic pushdown automaton with final-state acceptance can recognize L.  
B. L is regular.  
C. Erasing the separator from every word of L produces a context-free language.  
D. L intersect 0*#1* is exactly {#}.

### Q65. [2 Marks] [NAT]

A hash table has slots0 through6 and uses linear probing with h(k)=k modulo7. Insert keys0,7,14,1 in that order. Delete7 by marking its slot EMPTY rather than using a tombstone or moving entries. A search stops at the first EMPTY slot. How many of the remaining three stored keys are now incorrectly reported absent by their ordinary searches?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 071

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | NAT | 1 | 4 |
| 3 | NAT | 1 | 27 |
| 4 | NAT | 1 | 5 (exact) |
| 5 | MSQ | 1 | A, B, C |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 16 |
| 9 | MSQ | 2 | B, D |
| 10 | NAT | 2 | 15 |
| 11 | NAT | 1 | 6.8 |
| 12 | MCQ | 1 | D |
| 13 | MCQ | 1 | A |
| 14 | MCQ | 1 | A |
| 15 | MCQ | 1 | B |
| 16 | MSQ | 1 | A, B, D |
| 17 | NAT | 1 | 0.8 |
| 18 | NAT | 1 | 0 |
| 19 | NAT | 1 | 5 |
| 20 | NAT | 1 | 6 |
| 21 | MCQ | 1 | D |
| 22 | MCQ | 1 | B |
| 23 | NAT | 1 | 30 |
| 24 | NAT | 1 | 4 (exact) |
| 25 | MCQ | 1 | B |
| 26 | MCQ | 1 | A |
| 27 | MSQ | 1 | B, C, D |
| 28 | MCQ | 1 | B |
| 29 | MSQ | 1 | A, C, D |
| 30 | MCQ | 1 | C |
| 31 | MSQ | 1 | A, B |
| 32 | MSQ | 1 | A, B |
| 33 | NAT | 1 | -5 |
| 34 | MCQ | 1 | A |
| 35 | MCQ | 1 | A |
| 36 | MSQ | 2 | A, C |
| 37 | NAT | 2 | 0 |
| 38 | MCQ | 2 | C |
| 39 | MCQ | 2 | C |
| 40 | NAT | 2 | 17 |
| 41 | MCQ | 2 | A |
| 42 | MCQ | 2 | C |
| 43 | NAT | 2 | 960 |
| 44 | MSQ | 2 | B, C, D |
| 45 | MCQ | 2 | B |
| 46 | NAT | 2 | 170 |
| 47 | MCQ | 2 | D |
| 48 | NAT | 2 | 3 |
| 49 | NAT | 2 | 174 |
| 50 | MCQ | 2 | B |
| 51 | NAT | 2 | 4 |
| 52 | NAT | 2 | 1.7 |
| 53 | NAT | 2 | 0.3333 (accepted range 0.33325–0.33335) |
| 54 | MSQ | 2 | A, C, D |
| 55 | MCQ | 2 | D |
| 56 | MSQ | 2 | A, C, D |
| 57 | MCQ | 2 | C |
| 58 | MCQ | 2 | C |
| 59 | MCQ | 2 | B |
| 60 | NAT | 2 | 80 |
| 61 | MCQ | 2 | A |
| 62 | MCQ | 2 | C |
| 63 | MCQ | 2 | B |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 2 |
