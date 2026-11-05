# Worked Solutions — Additional Practice Set 002

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Reflection maps (x,y) to (x,-y).
2. Clockwise quarter-turn maps (u,v) to (v,-u). The combined map is (x,y) to (-y,-x).
3. Applying it separately to the labelled vertices gives (-1,-1), (-1,-3), (-2,-1).
- Original option A: All three vertices obey (-y,-x).
- Original option B: This is the combined map for a counterclockwise rotation after reflection.
- Original option C: This applies clockwise rotation without the preceding reflection.
- Original option D: This applies counterclockwise rotation without reflection.

## Q2

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Bu=Au+u(v^T u)=2u-2u=0, so zero is an eigenvalue.
2. Choose a basis (u,w1,w4) in which Aw1=w1 and Aw4=4w4. Distinct eigenvalues ensure this is a basis. In this basis A is diag(2,1,4), and u v^T has nonzero entries only in its first row, whose first entry is -2.
3. Therefore B is upper triangular with diagonal (0,1,4). These distinct real eigenvalues make B diagonalizable, and exactly two are nonzero, so rank(B)=2.
4. Commutation need not hold. In this basis choose v^T=(-2,1,0). Then B has first row (0,1,0); AB has entry (1,2)=2, whereas BA has that entry 1. A and B do not commute.
- Original option A: u is a nonzero vector in the null space of B.
- Original option B: The three eigenvalues are 0,1,4, all distinct and real.
- Original option C: The explicit choice A=diag(2,1,4), u=(1,0,0)^T, v=(-2,1,0)^T is a counterexample.
- Original option D: Similarity to a diagonal matrix with exactly two nonzero entries gives rank two.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Vocabulary in context

1. The reviewer supports the objective, so the endorsement is not withdrawn.
2. The requirement of a smaller pilot places a condition on that support. Here “qualified” means limited by reservations, rather than describing professional credentials.

- **A:** This contradicts the explicit condition.
- **B:** This captures support with a limitation.
- **C:** The context gives no information about credentials.
- **D:** Support remains; it has not been withdrawn.

**Common misconception:** A familiar word can have a contextual meaning unrelated to its usual professional use.

## Q4

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Databases — File organization

If the first record is at slot 0, the 16 records occupy two pages. If it starts at any slot 1 through7, the 16 consecutive records cross into a third data page. Thus at most three data pages are needed, and this is attainable. Add two index reads for a largest total of 5.

- **A:** False: this counts only the worst-case data pages and omits the index reads.
- **B:** False: it assumes the range begins exactly at a page boundary.
- **C:** True: three data pages plus two index pages attain the maximum.
- **D:** False: sixteen consecutive records cannot span four eight-record pages.

**Common misconception:** A contiguous record range can span one extra page because its first record need not be page-aligned.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Theory of Computation — Pumping lemma

A permitted decomposition has |xy|<=p and |y|>=1, so k=|y| satisfies 1<=k<=p. Pumping y twice changes the length to p^2+k. It exceeds p^2 and is at most p^2+p, strictly less than p^2+2p+1=(p+1)^2. There is no square strictly between consecutive squares, so every permitted decomposition fails when pumped twice.

A wrongly requires k=p. B gives the necessary argument for every permitted decomposition. C treats a single bad decomposition as sufficient even though the pumping lemma promises only the existence of a good one. D is false: pumping down subtracts an arbitrary k between 1 and p, not necessarily 2p-1.

- **A:** False: wrongly fixes |y| = p instead of considering all decompositions with 1 <= |y| <= p.
- **B:** True: for every valid decomposition, pumping twice gives length p^2 + |y| with p^2 < p^2 + |y| < (p+1)^2, which cannot be a square.
- **C:** False: testing only one specific decomposition is insufficient to disprove regularity via the pumping lemma.
- **D:** False: pumping down does not necessarily land at (p-1)^2.

**Common misconception:** Refuting a pumping property requires defeating every allowed decomposition of the selected word.

## Q6

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Sequential state evolution.

Starting at 01: 01→11→10→01. Its period is three, and the second state after reset is 10. A,C are true. State 00 is a separate fixed point, never reached from reset, so B is false. At 11 the bits are equal, refuting D.

**Common misconception:** Reset selects one state-cycle component; not every representable state is reachable from it.

## Q7

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Recursion-tree cost with a nonuniform nested loop.

For each i, there are i iterations of j and Θ(log i+1) iterations of k. Summing gives Θ(n² log n), using the i values from n/2 through n for a matching lower bound. The recurrence is T(n)=2T(n/2)+Θ(n² log n). At successive recursion depths the quadratic factor drops geometrically after accounting for the number of subproblems, so total cost remains Θ(n² log n). A loses a loop factor; B loses the k loop's logarithm; D adds an unnecessary logarithm for recursion depth despite the geometric decrease.

**Common misconception:** Multiplying root work by recursion depth is incorrect when per-level work decreases geometrically.

## Q8

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Generating function with initial conditions.

For F=Σa_nx^n, summing the recurrence for n≥2 gives F−x=3xF−2x²F. Thus F=x/(1−3x+2x²)=x/((1−x)(1−2x)). A has the wrong constant coefficient; B has the wrong recurrence sign; C also has nonzero constant coefficient.

**Common misconception:** A recurrence denominator alone does not determine a generating function; initial conditions determine its numerator.

## Q9

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Exhaustive consistency of statements.

If the prize is in A, the three truth values are false,false,true: valid. If it is in B, they are true,false,true: invalid. If it is in C, they are false,true,false: valid. Hence A and C are possible locations, B is impossible, and label A is false in every valid case. Options A,C hold; B,D do not.

**Common misconception:** Exactly one true statement need not determine a unique location.

## Q10

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Eliminating nongenerating and unreachable grammar symbols.

B has no terminating alternative: every derivation from B retains a B. Thus S→AB cannot produce a terminal string. All successful derivations use S→C, which generates exactly c*, proving A. Only S and C occur in successful derivations, proving C. Although A is separately reachable and generating, its only reachable context includes the nonterminating B; it is not useful, refuting B. D generates a terminal string but is unreachable from S, refuting D.

**Common misconception:** Reachability and generation tested in the unpruned grammar are not independently sufficient; remove nongenerating productions before recomputing reachability.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Handles in bottom-up parsing.

The stack suffix id matches T→id and must first become T. The stack then becomes E+T, permitting E→E+T. B is the next step. A reduces a right-hand side not yet present; C reverses a production in the wrong direction on the wrong symbol; D ignores reductions that remain after all tokens have been shifted.

**Common misconception:** Exhausting input does not imply that parsing is finished; reductions may still be necessary.

## Q12

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Prefix closure and recognizer dovetailing.

For a DFA of L, mark as accepting every state from which an original accepting state is reachable; the same transitions then recognize Pref(L), proving A. For recognizable L, on x dovetail recognizer runs for xy over all finite y and accept when one accepts, proving B. C is false: over {0,1}, let L={w1 0^|w|:w∈{0,1}*}. Every binary x is a prefix of x1 0^|x|, so Pref(L) is all binary strings, but L is nonregular: intersecting with 0*1 0* yields {0ⁿ1 0ⁿ}, a nonregular language. Finally, ε prefixes every word, so D holds for nonempty L.

**Common misconception:** Taking all prefixes can erase complexity; regularity of the prefix closure does not imply regularity of the original language.

## Q13

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Stack permutations.

A is produced by pushing 1,2,3, popping all three, then pushing 4,5 and popping both. C is produced by push 1,2/pop 2; push 3,4/pop 4,3; push 5/pop 5,1. In B, after popping 3 the top is 2, blocking 1. In D, after popping 4 the top is 3, blocking 2. Thus A,C are possible and B,D are not.

**Common misconception:** Unread input cannot remove an already stacked obstruction to the next requested output.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Predictive-parser pending terminals.

Each of the two leading a symbols causes an S→aSb expansion that leaves one future b on the stack. After both a symbols are consumed, two b symbols are pending around the remaining S. S→ε then allows them to be consumed. Thus the maximum is two, B; the other counts do not match the two expansions.

**Common misconception:** Count pending stack terminals, not all input symbols already read or still unconsumed.

## Q15

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Rank of a composition.

The image of B has dimension three. A's one-dimensional kernel can remove at most one dimension from that image, so rank(AB)≥2, proving A and excluding C. Taking A=B=diag(1,1,1,0) gives rank three (B). Taking A=diag(1,1,1,0) and B=diag(1,1,0,1) gives AB=diag(1,1,0,0), rank two (D).

**Common misconception:** Knowing the two individual ranks does not uniquely determine the product rank; the kernel/image alignment matters.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Key–foreign-key join cardinality.

Every R tuple finds at least one S tuple by the foreign key and at most one by the key of S. Hence exactly 100 joined tuples result. Set projection cannot collapse them here because the join includes all R attributes: distinct R tuples remain distinct. A contradicts the foreign key; C ignores uniqueness in S; D ignores the exact bound established by both constraints.

**Common misconception:** Assuming every join can expand to the Cartesian-product size regardless of keys.

## Q17

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** B+ leaf splitting and separator copies.

The stipulated leaves are [4,7,9] and [12,15]. The right leaf's smallest key is 12, so B is correct. A is the left leaf's largest key, C is internal to the left leaf, and D is the right leaf's largest key. None matches the given separator policy.

**Common misconception:** Applying a different split convention despite an explicit rule.

## Q18

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Aligned prefix aggregation.

The adjacent third octets 4 and 5 differ only in the last bit and form an aligned pair. Their common prefix yields 10.0.4.0/23, A. B and D include additional /24 blocks. C has host bits set and is not the aligned network-address notation of the requested block.

**Common misconception:** Aggregating by adjacency without checking prefix alignment.

## Q19

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Clear subject assignment in modifying clauses.

B explicitly gives Meera as the subject of submitting and checking, with the correct time order. A leaves an introductory participial clause grammatically attached to “the figures”; C makes figures submit a report; D grammatically describes Meera as having been submitted. These defects prevent the unambiguous intended statement.

**Common misconception:** Assuming a reader's ability to guess the intended actor repairs a dangling modifier.

## Q20

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Tree reconstruction from traversals.

Preorder makes A the root. Inorder splits left D,B,E from right C,F. The left subtree root is B with children D,E; the right subtree root is C with right child F. Postorder is D,E,B,F,C,A, option A. B places B before E, C reverses children and right-subtree order, and D interleaves nodes from different subtrees.

**Common misconception:** Preserving preorder's root-first order while attempting a postorder traversal.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reachability limits on negative-cycle effects.

A source-to-destination walk cannot exploit a cycle unreachable from the source. Thus that cycle alone does not make source-reachable distances undefined, proving B. A overgeneralizes; C unnecessarily blocks reachability analysis; D imposes no justified restriction on other edges.

**Common misconception:** Declaring all graph distances undefined whenever any negative cycle exists anywhere.

## Q22

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Segment-bound checking before translation.

Valid offsets are 0–99, but 120 is outside that interval, so C holds. A adds the base before disregarding the bounds violation; B clamps the address without authorization; D ignores both base and validity.

**Common misconception:** Assuming every base-plus-offset calculation is a valid address.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Monotonic threshold selection.

Any measurement above the higher threshold was also above the old one, so the new flagged set is contained in the old set, A. A strict increase (B) and newly flagging all previously unflagged items (C) contradict that inclusion. The set need not become empty, refuting D.

**Common misconception:** Assuming every threshold change strictly changes the selected set.

## Q24

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reversal matching versus copying.

Even palindromes are context-free: a PDA can guess the midpoint and match the second half by stack reversal, proving A. The copy language is not context-free. Intersecting it with 0*1*0*1* gives matching separated zero and one blocks; the word 0^p1^p0^p1^p cannot satisfy every CFL pumping requirement because a length-p window cannot change both separated copies of each affected block while retaining their equalities and order. This refutes B. On the unary alphabet the copy language is exactly (00)*, proving C. CFLs are not closed under general CFL intersection, refuting D.

**Common misconception:** Assuming a stack can compare a second copy in the same order as easily as a reversed copy.

## Q25

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: transaction atomicity. Atomicity requires the transfer's updates to take effect together or not at all. Persisting only the debit violates A. B and C are not transaction requirements. D mistakes partial success for an atomic outcome. Merely retaining a durable partial update is not sufficient.

## Q26

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: left factoring versus ambiguity. Both S alternatives start with a, producing the LL(1) conflict in A. Factoring a leaves X alternatives distinguished by b and c, so C is true. The language consists only of ab and ac and has an unambiguous grammar, disproving B. A deterministic parser exists, disproving D. A predictive-table conflict need not mean an ambiguous language.

## Q27

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: Huffman tie choices. Merge the two ones to make 2; then merge any two of the three weight-two nodes to make 4. Remaining weights are 2,4,4, one four being the original symbol. If the next merge uses the other four, the original four is a child of the final root and has length one (A). If it uses the original four, that symbol has length two (B). Its first possible merge is this penultimate merge, so depths three or four cannot occur; C and D fail. Equal-weight choices can change individual lengths while preserving optimal weighted cost.

## Q28

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: pumping with a common multiple. The pumped a-count is p+(i−1)k. Set this equal to the fixed b-count p+p!, yielding i=1+p!/k. This is a positive integer because every k≤p divides p!, making B correct for every valid split. A does not generally solve the equation; C removes rather than adds the required amount and can be negative; D only adds k², not necessarily p!. The factorial makes one chosen witness handle all permitted pump lengths.

## Q29

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: frame lifetime in tail calls. Q uses the address of x, so a correct transformation must retain valid storage and the intended value for that use, B. Tail position by itself does not justify overwriting all of P's frame, D. A ignores the live addressed object; C contradicts the explicitly passed pointer. Tail-call optimization is constrained by observable storage lifetimes.

## Q30

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Distinguishing a rate, a count and causal evidence.

For example,100 issued books with20 late returns gives20%;200 issued books with30 late returns gives15%. Thus a declining fraction can accompany an increasing count. The passage also explicitly withholds a causal conclusion, making D correct. A invents both causality and a claim about every borrower. B contradicts the numerical possibility. C is false: if total volume rises while the timely fraction also rises, the timely count rises, not falls.

**Misconception:** Comparing percentages without their denominators, or treating an observed before/after change as causal proof.

## Q31

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Simulate the machine on00 and accept its encoding if it accepts00; this recognizes S, so A is true. Membership depends only on the recognized language and holds for some languages but not others, so C is true. By the undecidability of nontrivial semantic language properties, S is undecidable, disproving B. Equivalently one can reduce arbitrary machine acceptance to acceptance on the fixed string by embedding the original machine and input in a new machine. If both S and its complement were recognizable, dovetailing their recognizers would decide S, so D is false. A fixed input length does not bound computation time.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first update temporarily gives both rows code B, violating immediate uniqueness. The completed swap has distinct codes B and A, so commit-only validation can accept it. B is correct. A overlooks the intermediate violation; C contradicts the specified check timing; D confuses the code column with the unchanged primary keys. Constraint timing can affect executability without changing final-state validity.

## Q33

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If either predicate holds universally, their pointwise disjunction does too, so A is true. On a two-element domain, let P hold only at the first element and Q only at the second. Then F is true but G false, proving C and disproving B. On a singleton, both reduce to the same P-or-Q statement, proving D. Universal quantification does not generally distribute over disjunction.

## Q34

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The qualification explicitly denies inferring impossibility from zero observed failures. D asserts exactly that inference and conflicts. A restates the observation; B and C acknowledge untested possibilities and future revision. Empirical absence is not a universal logical proof.

## Q35

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Both weighing and obtaining the address must precede mailing; their mutual order is unspecified. A and B satisfy this, and D accurately recognizes both possibilities. C places address acquisition after mailing, contradicting the account. Partial order information need not specify a unique chronology.

## Q36

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The identity holds over integers and remains equal after reduction modulo2^w, proving A,B. Whether the rewrite helps depends on instruction costs and target code generation, proving D. Semantic reasoning must still respect the language and representation, so the broad permission in C is false. Equivalence and profitability are separate tests.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At the first '<', longest match among the listed tokens is'<<', then the remaining'=' forms its own token. A,B,D are true. A lexer does not invent an unlisted token based on adjacency, so C is false.

## Q38

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Simulate at most k transitions while checking the halting condition, including the initial configuration if k=0. This always terminates, so A is true and B false. An m-bit value of k can be about 2^m, supporting D. No universal finite simulation bound decides unrestricted eventual halting, so C is false. Large finite running time and undecidability are different properties.

## Q39

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Q can progress and release S; P can then proceed. No request from Q leads back to P, so there is no cycle. D is correct. A equates waiting with deadlock, B invents a missing circular edge, and C invents a request not stated. A blocked process need not belong to a deadlock.

## Q40

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

At w=2 the update sets dp[2]=3. At w=4 it reads that updated value and produces6, reusing the only item. Thus B is true and A,D false. Descending order reads the preceding item's states at smaller capacities, so no updated dp[w−2] is reused during this pass, proving C. Loop direction encodes whether repeated item use is permitted.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The cycle cannot lie on any s-to-t walk, since no cycle vertex can reach t. Its repetitions therefore cannot lower the s-to-t cost, proving C; examples with no other negative cycles have finite distance, proving A. B incorrectly spreads its effect to all reachable vertices. D contradicts the stated existence of a path. A says “can,” not that other negative cycles are excluded.

## Q42

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The state, head position and contents of the bounded tape range form a finite configuration space, proving C. Determinism means a repeated complete configuration repeats the future forever. Simulating until halt or repetition therefore decides halting, proving A. A machine may loop within one cell, refuting B. The finite bound is essential and does not apply to unrestricted machines, refuting D.

## Q43

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The base2 and increments of2 reach every even integer, proving A. They never reach an odd integer, so B,D do not follow. A separate odd base3 starts the odd chain; together the two chains cover every n≥2, proving C. The induction step's stride determines which base cases are needed.

## Q44

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both items have value density2. Any feasible packing of total weight5 achieves the maximum value10, proving A. A whole four-unit item plus one unit from the other also attains it, proving C. The allocation2.5+2.5 has two partial items, refuting B, and many such allocations refute D. A greedy algorithm can produce an optimum with at most one partial item without that property holding for every optimum.

## Q45

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Context-free languages are closed under homomorphisms, including erasing ones, giving A. Intersection with a regular language preserves context-freeness, giving B,D. General context-free languages are not closed under complement, so C has no guarantee. Closure with a regular operand is stronger than closure with an arbitrary context-free operand.

## Q46

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The combined map is (x,y)→(y+2,x−1). Matching (5,3) gives y=3,x=4, so B. A maps to (6,2), C to (3,5), and D to (8,0). Reversing a composition requires undoing the translation before the reflection.

## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

B attaches the storage clause directly to “samples” while retaining the researcher as the agent of analysis. A makes the introductory participle modify the researcher; C reverses the analysis roles; D explicitly attaches storage to the researcher and also uses an inappropriate relative pronoun for a person. Modifier placement determines which noun has the property.

## Q48

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The observed count can fall either because delays became less frequent or because people submitted fewer reports under the new procedure. With no independent arrival data, these explanations are not separated, so C. A,B assert a punctuality improvement not established by the evidence; D asserts the opposite causal effect without evidence. A change in reporting can change a measured indicator without the underlying service changing.

## Q49

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concrete execution increments x,y together from zero, so x=y=n and z=0(A). The stated per-variable abstraction joins0 with 1 at the loop header, making each nonconstant(C). It does not store the relational invariant x=y, so B is false; D is contradicted by the concrete invariant. An imprecise analysis does not make an impossible program result possible.

## Q50

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A strict greater-than shift never moves an equal predecessor past the key, so A holds. On sorted input no predecessor exceeds its key, proving C. A non-strict comparison can move equal records past each other, disproving B. Shifts correspond to strict inversions; distinct descending records already disprove D. Equality is crucial to stability but not to the shift count claimed in D.

