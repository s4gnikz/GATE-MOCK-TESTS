# Worked Solutions — Additional Practice Set 011

## Q1

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. With s=1, invert B to 0101 and add 1: 0111+0101+1=1101, with no fifth bit. Thus C=0.
2. Signed interpretation gives 7-(-6)=13, outside [-8,7], so V=1 even though the unsigned carry-out is zero.
- Original option A: Carry-out is zero and signed overflow is present.
- Original option B: It gets result and carry right but misses signed overflow.
- Original option C: The stated bit addition does not yield 0011.
- Original option D: Both the bit arithmetic and signed range test agree.

## Q2

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first iteration detaches node 2 and prepends it to q, leaving head 1→3→4→5→6, q 2, and p at 3. The second detaches 4, leaving head 1→3→5→6, q 4→2, p at 5. The third detaches 6, leaving head 1→3→5, q 6→4→2, p NULL. Every detached successor is prepended, so its list is reversed. All terminal next pointers are NULL.
- Original option A: False: prepending each removed node reverses their order.
- Original option B: True: odd-position nodes remain, and removed even-position nodes are reversed.
- Original option C: False: p advances to the next surviving node, so node 3 is never detached.
- Original option D: False: removal is based on alternating successors, not splitting the original list in half.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Algorithms — Graph traversals

Nested intervals show that u is a proper ancestor of v in the DFS forest. The tree path from u to v consists of directed edges. Adding v→u closes a directed cycle; v→u is a back edge. Thus only B follows.

- **A:** False: a tree edge runs from an ancestor to a newly discovered descendant, not back to an ancestor.
- **B:** True: the tree path u to v together with v→u is a directed cycle.
- **C:** False: the nested intervals identify an ancestor relationship, not separate branches.
- **D:** False: this return edge closes a cycle.

**Common misconception:** Nested DFS intervals alone do not imply acyclicity; edge direction matters.

## Q4

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Databases — Conflict and view serializability with blind writes

1. The first w1(x) precedes w2(x), creating conflict edge T1→T2. The last w1(x) follows w2(x), creating T2→T1. The conflict graph is cyclic.
2. The only read, r4(x), sees T2's write. The final writer of x is T1; the final writer of y is T4.
3. A view-equivalent serial order must place T2 before T4. Because T1 must be the final x writer, T1 is after T2; because T4 must still read T2's x, T1 cannot intervene between T2 and T4. Thus T2<T4<T1.
4. Both T2 and T3 write y, so both must precede final y-writer T4. T2 and T3 can be ordered either way. The only view-equivalent orders are (T2,T3,T4,T1) and (T3,T2,T4,T1).
5. Delete the first w1(x). The y conflicts now force T3<T2<T4, and the x conflicts force T2<T4<T1. Together they yield the unique conflict-equivalent order (T3,T2,T4,T1).

- **A:** Incorrect: T1 and T2 form a conflict cycle in the original schedule.
- **B:** Correct: the two displayed serial orders preserve the read source and final writers.
- **C:** Correct: the precedence requirements leave only the relative order of T2 and T3 free.
- **D:** Correct: after deletion all four transactions lie on the forced chain T3→T2→T4→T1.

**Common misconception:** Blind writes can make a schedule view-serializable even when its conflict graph has a cycle; preserving final writers is essential.

## Q5

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Logarithm bases and domain constraints.

Put y=log₂x. The domain requires x>0 and x≠1, hence y≠0. Change of base gives log_x16=4/y, so 4/y=y and y²=4. Therefore x=2²=4 or x=2⁻²=1/4. A and B satisfy the original equation. C has a negative base and argument for real logarithms; D uses the invalid base 1.

**Common misconception:** A logarithm base may lie between zero and one; only positivity and exclusion of one are required.

## Q6

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Divisor lattices as products of chains.

Write 60=2²×3×5. Divisors correspond to exponent vectors in {0,1,2}×{0,1}×{0,1}, with meet and join given by coordinatewise minimum and maximum. This is a lattice and is distributive, proving A,D. A complemented vector must choose either zero or the full exponent in each coordinate, giving 2³=8: C is true. A divisor with 2-exponent one, such as 2, has no complement, so B is false.

**Common misconception:** Distributive does not imply that every element is complemented; a three-element chain is not Boolean.

## Q7

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Matching, vertex cover and bipartiteness.

Edges {a,2},{b,3},{c,1} give a size-three matching. No matching exceeds the smaller side's size three, proving A. The side {a,b,c} is a vertex cover, disproving B. The graph remains bipartite and has edges, so its chromatic number is exactly two, proving C. A matching cannot cover an odd number of vertices, refuting D.

**Common misconception:** Deleting selected cross-edges does not necessarily reduce maximum matching size.

## Q8

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Row dependence, null space, and consistency.

Row 1 minus twice row 2 plus row 3 is zero, so rank is at most 2. The upper-left 2×2 minor has determinant 1, making rank exactly 2 (A). Direct multiplication sends (1,−2,1)ᵀ to zero; nullity is one, so this vector spans the null space (B). The same dependence requires b1−2b2+b3=0. It is sufficient because the first two independent equations can be solved and the third is then their combination (C). Adding any multiple of the nonzero null vector to a solution gives another solution, disproving D.

**Common misconception:** Consistency and uniqueness are separate conditions; a nontrivial null space rules out uniqueness.

## Q9

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Circular wait and lock ordering.

P may acquire A while Q acquires B; each then waits for the other's mutex, so A holds. If P finishes before Q begins, no deadlock occurs, disproving B. Acquiring A before B in both threads prevents this cycle, proving C. Releasing locks immediately does not protect an operation that needs both held together, so D is false.

**Common misconception:** Avoiding deadlock does not by itself preserve the required mutual exclusion.

## Q10

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordering resource and mutex waits in a bounded buffer.

The consumer can lock M and block on F=0. The producer can obtain E but then blocks on M, so it cannot insert and signal F; A,D describe this cycle. Waiting for F before acquiring M means an empty-buffer consumer holds no mutex, allowing the producer to fill and signal; B holds for this specific deadlock. Extra capacity changes E but not the blocked consumer's need for F or the producer's need for M, refuting C.

**Common misconception:** More buffer space cannot fix an ordering cycle involving a mutex and an empty-item semaphore.

## Q11

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Mutual exclusion versus progress.

Both threads can set their flags before either tests the other, after which both wait forever with flags true (A). For simultaneous entry, both would need to read the other's flag false after setting their own true. Sequential consistency cannot order those four events that way: whichever thread sets its flag first prevents the other from passing once that other sets its own. Thus mutual exclusion holds (C), and B is false. Volatile alone does not change the allowed flag-setting interleaving or add a tie-breaker, refuting D.

**Common misconception:** Mutual exclusion does not imply deadlock freedom or progress.

## Q12

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** ON filtering in an outer join.

For L.id=1, only R's row (1,5) satisfies both ON predicates. For L.id=2, no row matches, so LEFT JOIN supplies a NULL-extended row. C is correct. A drops the preserved unmatched row; B ignores R.v>0; D overlooks the successful match.

**Common misconception:** A filter in ON can preserve an unmatched left row that the same filter in WHERE would remove.

## Q13

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recognizer scheduling for union and intersection.

For union, dovetailing eventually discovers an acceptance from either recognizer, proving A. Sequential execution in B can loop forever on the first machine even when the second would accept. For intersection, members make both sequential recognitions accept; nonmembers never make both accept, so C is a valid recognizer even if it sometimes loops. D can accept a member whose recognizing computation takes more than one million steps, so it is invalid.

**Common misconception:** A strategy unsuitable for union may still be suitable for intersection because the required acceptance conditions differ.

## Q14

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Unequal-count context-free language.

Split L into i<j and i>j; a PDA can match counts with its stack and accept an unmatched excess on either side, so their union is context-free (A). Its complement within a*b* is exactly the equal-count language (C). If L were regular, subtracting it from regular a*b* would make that equal-count language regular, a contradiction, so B is false. ε has equal zero counts and is excluded (D false).

**Common misconception:** Context-free unequal-count languages need not be regular.

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** IPv4 subnet boundaries.

A /27 leaves five host bits and covers addresses 96 through 127. The last address is broadcast, so the highest host is 126. A is broadcast, C lies outside the subnet, and D is valid but not highest.

**Common misconception:** Assigning the all-one host field to a host.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Copy propagation and killed facts.

Before the assignment y=5, x and y have the same value, so the use in z may be replaced. Afterwards x still has the original y while y has 5, so a direct replacement in w is generally wrong. B is correct. A ignores the redefinition; C assumes every initial y equals 5; D forbids the valid first substitution.

**Common misconception:** Treating a copy assignment as a permanent alias relationship.

## Q17

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Stack recognition and homomorphism closure.

A deterministic PDA pushes the prefix until #, then pops and compares each following bit, accepting exactly on a complete match; thus A holds. Mapping # to ε is a homomorphism, and CFLs are closed under homomorphism, proving C. A finite automaton cannot remember arbitrary prefixes: distinct prefixes x,y are distinguished by suffix #xᴿ, so infinitely many distinguishable prefixes refute regularity in B. D confuses individually finite inputs with a uniform finite memory bound.

**Common misconception:** Believing a visible midpoint removes the need to remember unbounded prefix content.

## Q18

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Asynchronous reset priority.

Asserting an asynchronous reset changes Q independently of a clock edge, so A holds even while the clock remains low. B describes synchronous reset, C incorrectly substitutes toggling, and D is unrelated to reset behaviour.

**Common misconception:** Applying the normal data-sampling edge condition to an asynchronous control.

## Q19

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Regular versus unbounded matching requirements.

C has regular expression (aa)*b*. A requires matching two unbounded counts and is nonregular. For B, pumping a sufficiently long prime-length unary word by q extra copies of a nonempty pumped block, where q is the chosen prime length, gives composite length q(1+|y|), violating the prime condition. D is nonregular: distinct prefixes 0^n1 are distinguished by suffixes 0^n1, since equality of the two zero-block lengths is required for the resulting two-one word to be a square.

**Common misconception:** Treating all numerical length restrictions as nonregular; fixed modular restrictions are regular.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Testing a proposed predictor with comparison data.

B supplies observations where the suspected condition is present and absent, allowing comparison. A and D claim certainty without the missing evidence; C deliberately keeps the comparison condition unobserved.

**Common misconception:** Counting only instances consistent with a hypothesis instead of testing alternatives.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Prime attributes and 3NF versus BCNF.

A is never derived and must be in every key. AB determines C; AC determines B via C→B. Both are minimal keys, and all attributes are prime. Thus every nontrivial dependency has either a superkey determinant or prime right-hand attribute, satisfying 3NF. But C is not a superkey while C→B holds, violating BCNF. B is correct. A misses AC and the BCNF violation; C overstates individual closures; D misclassifies B as nonprime.

**Common misconception:** Treating the 3NF exception for a prime right-hand attribute as valid in BCNF too.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Persistence of acknowledged commits.

Durability requires committed effects to survive the specified crash model, so A is the direct violation. Atomicity concerns all-or-nothing behaviour and need not be violated if all effects are lost together, refuting B's necessity. C names the wrong property; D excludes the very failure scenario durability addresses.

**Common misconception:** Treating every recovery error as necessarily an atomicity violation.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Characterizing a recursive grammar.

Each a is prepended and each b appended around the remaining S. Thus all generated words are a^n b^m, with counts independently chosen; every such word is obtainable. A is correct. B and C impose unjustified equal counts or alternation; D includes ba, which cannot be generated.

**Common misconception:** Assuming grammar ambiguity changes the generated language into all strings.

## Q24

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: composition of reflections. Reflection across y=x swaps coordinates, giving (0,2). Reflection across x=1 changes x to 2−x, giving (2,2). A is correct. B changes the second coordinate incorrectly; C stops after the first reflection; D introduces an unwarranted vertical reflection. Reflection order matters.

## Q25

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: alias-sensitive optimization. When i≠j, the store does not modify A[i], so reuse p (A). When i=j, the last load reads 7 (C). Without a proven relation, the i=j case with old value not 7 defeats B. The same case defeats D. Equal expression text does not ensure an unchanged memory value across a store.

## Q26

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: limits on dense subsets. Since |f(x)|=|x|, f tends to zero at zero and f(0)=0, proving A. For nonzero x, the difference quotient f(x)/x is 1 on rationals and −1 on irrationals; rational and irrational inputs occur arbitrarily close to zero, so this quotient has no limit and no derivative exists. B is true and D false. At one the rational and irrational limits are 1 and −1, so C is false. Continuity of the function does not force its difference quotient to converge.

## Q27

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: divide-and-conquer tree sums. Level j has 3ʲ calls of size n/2ʲ, costing Θ(n²(3/4)ʲ). Summing this decreasing geometric series gives Θ(n²), A; B incorrectly adds a logarithmic factor. The depth is log₂n and the number of leaves 3^(log₂n)=n^(log₂3), C. D confuses logarithmic depth with n levels.

## Q28

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: affine hashing over a prime field. Given outputs r,s, subtract the equations to get a(x−y)=r−s modulo five. Since x−y is nonzero, its inverse determines one a, and then b is determined, proving A. Equal outputs occur exactly when a=0, with probability 1/5, proving C and disproving B because these functions are constant. Conditional on a≠0, outputs can never be equal, whereas independent uniforms would be equal with probability 1/5; D is false. Conditioning can destroy pairwise independence.

## Q29

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: safety versus current deadlock. Initially no remaining need fits available (0,0), so the state is unsafe, A. Adding only B gives (0,1), still enabling none, so B is false. Adding A gives (1,0): P can finish, making (1,1); R then finishes, making (2,2); Q can finish. C is true. Maximum claims need not be current requests, so unsafe does not itself prove actual deadlock; D is false.

## Q30

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Before line3, y must survive to line4, so B is true. The old x has already been used to compute y and is overwritten at line3 before its next direct use, making A false. Line1 affects y and thereby z; line3 affects the other operand of z, so C is true and D false. A value may cease to be live even though an earlier computation using it still contributes to the output.

## Q31

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

R∩S contains only the three diagonal pairs, proving B. R∪S includes(1,2) and(2,3) but not(1,3), so A and D are false. Transitive equivalence closure connects all three elements, making C true. A union of equivalence relations need not itself be an equivalence relation.

## Q32

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A's and B's statements are logical opposites, so exactly one of them is true regardless of the coin's location. To have exactly one true label overall, C's statement must be false: the coin is in C. Thus C is correct; locations A and B each make two labels true, and D incorrectly denies the valid location.

## Q33

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A checksum can reject corrupt frames but does not restore lost data, disproving A. End-to-end acknowledgment/retransmission can recover losses across the path under the stated eventual-communication condition, proving B and D. A checksum validates one received frame under its error model, not complete arrival of all message data, so C is false.

## Q34

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A has matching dash positions and differs only in the third bit, producing0--1. C differs only in the last bit and produces-10-. B has different dash positions and cannot be combined by the stated rule. D differs in four positions. Adjacency is determined by fixed-bit differences, not visual proximity of the rows.

## Q35

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The link's stored path may stop resolving after deletion, so A is true. Pathnames can cross mounted file systems, making C true. Symbolic links do not increment the target's hard-link count or inherently retain its inode, so B,D are false. Name resolution and inode reference counting are separate.

## Q36

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first computed x is overwritten before any read, so it is dead and removable under the no-side-effect assumptions: A,B. Only the second definition reaches return, disproving C. That reaching definition is needed, disproving D. A dead value is identified by uses, not merely by repeated assignment names.

## Q37

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For2k+1 original entries, the median has sorted rank k+1. Adding the smallest and largest values increases the size to2k+3 and shifts the old median's rank to k+2, exactly the new middle rank. A is true and B false. The appended extremes need not average to this middle value, disproving C; their placement suffices without all numerical entries, disproving D. Paired extreme insertions preserve the central order statistic.

## Q38

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

R introduces the measurement, Q introduces repetition, P refers to that second measurement, and S draws the resulting decision. A has that sequence. B introduces repetition before the first measurement and delays its result; C begins with an unexplained second reading; D discusses a second reading before the repetition occurs. Pronoun references and cause–effect order constrain the sequence.

## Q39

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first p symbols are all a, and y is nonempty within them, so A is true. Removing y decreases only the a count, establishing C for every permitted decomposition. A regular-language pumping guarantee is existential over a suitable decomposition; disproving one convenient decomposition is insufficient, so B is false. The pumping length must work for every sufficiently long language word and cannot be reset to suit later choices, refuting D. Correct quantifier order is essential.

## Q40

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Totality makes each simulation finish, proving C. A finite-index accepted input in the enumeration is therefore reached after finitely many terminating earlier simulations, proving A. If none is accepted, there are always more inputs to examine; no finite rejected prefix establishes emptiness, so B is false. The promise gives no finite maximum relevant length, refuting D. Total decision procedures may still recognize languages whose emptiness cannot be settled by this enumeration.

## Q41

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Expansion gives xz+(NOT x)y+yz; the consensus term yz is redundant, yielding A,B. If y=z, selection by x yields that common value, proving D. For x=1,y=0,z=1, F=1 while yz=0, refuting C.

## Q42

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The successor is the leftmost node in v's right subtree, so it cannot have a left child, proving A and refuting D. It may lie several edges below v, refuting B. Its possible right child can replace it at its original parent link, proving C. If s is v's immediate right child, that former parent is v itself.

## Q43

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

With at least two elements, every x has a different witness y, proving A. For Q, take x equal to its proposed y; x≠y then fails, so Q is false in every nonempty domain, proving C and refuting B. Any two-element domain makes P true and Q false, refuting D. Moving the existential quantifier outside removes the ability to choose a witness depending on x.

## Q44

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

With x=0 the loop is skipped, proving A. With x=1, every update keeps x positive and strictly increases it, so the original never returns while the rewritten code returns immediately, proving B. C ignores observable termination; D correctly recognizes that obligation. An unused computed value does not automatically make its entire computation removable.

## Q45

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Key 7 must be the root. Key 6 is already at index 3. If 5 were at index 4 or 5, its parent at index 2 would have to exceed 5; both available larger keys are already elsewhere. Index 2 is possible, and indices 6,7 have parent 6, so each is possible. Hence exactly {2,6,7}: C. A excludes feasible child positions; B includes impossible positions 4,5; D includes the root occupied by 7.

## Q46

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Reclaiming a resource removes the no-preemption condition and can let one process finish, breaking the circular wait execution. Priorities, an unrelated ready process, and CPU speed do not release either held resource, so A,C,D do not resolve this resource cycle. Scheduling progress elsewhere is not resolution of the deadlocked pair.

## Q47

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Sequence43 supersedes41, even though its advertised cost is larger. Sequence42 arrives later but is older and is discarded; the repeated43 carries the same information. The retained cost is9(C). A uses last different arrival instead of freshness, B retains obsolete data, and D adds advertisements that should be replacements rather than path segments.

## Q48

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Every aS production adds one a; every aSb adds one a and a matching trailing b. Consequently the language is a^n b^m with n≥m≥0. A has counts2,1 and C has3,2, both allowed. B has fewer a's than b's, and D violates the block order, so neither is generated. Different productions may contribute unmatched a's, but never unmatched b's.

## Q49

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Matrix multiplication gives (M²)[u,u]=Σ_v M[u,v]M[v,u], counting return walks of length two, so A. Transposition interchanges source and destination, proving C. Each directed edge contributes one entry, not two, disproving B. Opposite edges u→v and v→u give a positive diagonal in M² without self-loops, refuting D.

## Q50

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The third left-hand side is the sum of the first two, requiring t=3. The first two rows are independent, leaving one free variable when consistent. Subtracting twice the first equation from the second gives −x1+x3=0. Equivalently, solutions are (s,1−2s,s) for arbitrary real s. Thus A,B,C hold. Rank is 2, not 3, so D is false.

