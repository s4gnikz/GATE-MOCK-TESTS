# Worked Solutions — Additional Practice Set 009

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. The required ones and don't-cares together are exactly the eight inputs with B=0.
2. Assign those don't-cares to 1 and group all eight cells. This yields NOT B with one literal.
3. A zero-literal constant is impossible because both required zeros and required ones exist.
- Original option A: It covers all required ones and no required zero with one literal.
- Original option B: It misses every required one, each of which has D=1.
- Original option C: For A=B=1,C=0,D=0 it produces a forbidden 1.
- Original option D: It is valid but has two literals, so it is not minimum-literal.

## Q2

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The OR evaluates its right operand exactly when its left operand is false. The left operand is false when x=0 or when x is nonzero and the quotient is at most 2, so A holds. For B use x=2,y=5,z=0: the original quotient is 2, so the original evaluates z++ and returns false, leaving z=1; the proposed comparison 5>4 is true, so it returns true without incrementing z. C is unsafe because x=0 would cause division by zero, an operation the original never evaluates. If x=0 the AND is false without division, so the right operand is evaluated and D follows. Side-effect freedom alone never justifies speculating an operation that can fail.
- Original option A: True: these are precisely the paths on which the left side of OR is false.
- Original option B: False: x=2,y=5,z=0 is a counterexample due to integer truncation and short-circuit effects.
- Original option C: False: the transformation introduces division by zero when x=0.
- Original option D: True: no division occurs, and the postfix increment is evaluated once.

## Q3

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Programming and Data Structures — Trees

A is the root. Its first subtree must contain B,C because B closes at the second postorder position; its other subtree contains D,E. Thus A has two children, B and D. B has only child C and D has only child E. Either only child may independently be placed left or right, giving 2*2=4 trees.

- **A:** False: traversals do not specify which side holds an only child.
- **B:** False: there are two independent only-child choices, not one.
- **C:** True: two independent left/right choices give four.
- **D:** False: A must have two children; it does not contribute a third binary choice.

**Common misconception:** Preorder and postorder can fix subtree membership without fixing the side of an only child.

## Q4

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Engineering Mathematics — Propositional and predicate logic

1. E lets us follow an R-edge indefinitely from any vertex. Finiteness forces a repeated vertex, hence a directed cycle. Under T, a directed cycle yields a self-loop, contradicting I. Thus A and C have no finite nonempty model, irrespective of F.
2. B has a two-element model {u,v} with only R(u,v) and R(v,u). Every element has one successor; the relation is symmetric and irreflexive.
3. D has a singleton model {u} with R(u,u). It satisfies E, T and S; irreflexivity was not required.

- **A:** A finite successor chain repeats, and transitivity then violates irreflexivity.
- **B:** The two-element swap relation is a witness.
- **C:** Adding functionality cannot repair the E,T,I contradiction.
- **D:** The singleton reflexive relation is a witness.

**Common misconception:** Finiteness changes satisfiability: an irreflexive transitive relation can have successors everywhere on an infinite ordered domain.

## Q5

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Conditional probability with a hidden box.

In Box I, both-red probability is 1/3 and at-least-one-red probability is 1. In Box II these probabilities are 0 and 2/3. Including the equal box priors gives P(both red)=1/6 and P(at least one red)=1/2+1/3=5/6. Their ratio is 1/5. A gives the unconditional numerator; B ignores the box information in the condition; D is twice the required ratio.

**Common misconception:** Conditioning changes the probability of the selected box as well as the probability of its ball outcomes.

## Q6

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** SQL aggregate and NULL semantics.

A has COUNT(*)=3, COUNT(amount)=2 and SUM=30, satisfying both predicates. B has counts 2 and 0, but SUM is NULL and NULL>10 is UNKNOWN, so it is excluded. C has equal counts and is excluded. Thus one row (A,30) remains: A,B true and C false. Replacing COUNT(amount) with COUNT(*) makes the strict inequality false in every group, proving D.

**Common misconception:** SUM of an all-NULL group is NULL, not zero, and HAVING retains only TRUE.

## Q7

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Quotient-group element order.

H={0,4,8}. A multiple k(5+H) is the identity coset exactly when 5k mod 12 belongs to H, equivalently 5k is divisible by 4. The least positive k is 4. A confuses |H| with the coset's order; C and D are larger than the least returning multiple.

**Common misconception:** Element order in a quotient is determined by return to the subgroup, not necessarily return to zero in the original group.

## Q8

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Probe-cycle length and coprimality.

The cycle length is 12/gcd(h2,12). It equals twelve exactly for h2=1,5,7,11. Four of eleven equally likely choices qualify, giving 4/11. A uses twelve rather than eleven choices; C counts non-coprime steps; D ignores short cycles.

**Common misconception:** A nonzero second hash is insufficient when the table size is composite.

## Q9

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** CPU execution-time comparison.

Ignoring the common factor N/10⁹, P's time is 1.5/3=0.5 and Q's time is 0.8×2/4=0.4. Speedup is old time divided by new time: 0.5/0.4=1.25. C is correct; A is its reciprocal, while B,D omit or miscombine factors.

**Common misconception:** Clock rate or CPI alone does not determine performance when instruction counts differ.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Aggregate analysis of parent-pointer traversal.

Across the entire traversal, each downward tree edge is followed once to visit its child, and each upward edge is followed at most once when a subtree is exhausted. All constant work over n successor operations plus at most n−1 downward and n−1 upward traversals is O(n). Visiting all n nodes also gives Ω(n), hence Θ(n). A cannot account for visiting n nodes. C,D incorrectly multiply the worst single-operation cost by n; even on a path, the final long ascent occurs only once.

**Common misconception:** A worst-case O(height) successor call does not imply O(n×height) total traversal time.

## Q11

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reconstructing a binary tree from traversals.

Preorder selects A as root; inorder splits its left labels D,B,E and right labels C,F. The left subtree has root B with children D,E; the right has root C with right child F. Postorder is D,E,B,F,C,A. Only A matches; B visits B before completing its left subtree, and C,D misorder or mix the two subtrees.

**Common misconception:** Preorder identifies each subtree's root, while inorder determines which labels belong to each side.

## Q12

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Finite cancellation monoids.

Left multiplication by a is injective by cancellation and hence onto on the finite set (A). Thus some b satisfies ab=e. Now a(ba)=(ab)a=a=ae; cancel a to get ba=e. Every element has a two-sided inverse, proving B and D. Noncommutative finite groups, such as the permutations of three elements under composition, refute C.

**Common misconception:** Finiteness is crucial when converting an injective self-map into a surjective one.

## Q13

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Context-free closure with regular languages.

Intersecting a CFL with a regular language preserves context-freeness (A). L minus R equals L∩complement(R), and a regular complement is regular, proving B. Union with R, itself a CFL, preserves context-freeness (D). C is not guaranteed: choose R=Σ* and a CFL L whose complement is not context-free, such as the complement of {aⁿbⁿcⁿ} over {a,b,c}; that L is context-free by separating incorrectly ordered strings and unequal adjacent block counts. Then R minus L is the non-CFL equal-three-count language.

**Common misconception:** Set difference is not symmetric; complementing the regular operand is safe, complementing an arbitrary CFL is not.

## Q14

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Direct-mapped conflicts.

Pairs A,B,C map to the same line within each pair: residues 1,2,3 respectively. Blocks 4 and 5 map to lines 0 and 1 and can coexist. Thus D is correct.

**Common misconception:** Distinct memory blocks can still compete for exactly the same direct-mapped cache line.

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Inherited descriptors and open file descriptions.

Both descriptors refer to the same open file description, which contains the current offset. B is correct. A describes separately maintained execution state, C incorrectly makes ordinary stack storage shared, and D contradicts the distinct process identities created by fork.

**Common misconception:** Equating a copied descriptor table with separately opened files.

## Q16

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Ancestor bounds during BST search.

After 50,20,40, the next node must lie strictly between 40 and 50, so 48 is possible (A). After 20 the upper bound 50 still applies, excluding 55 (B false). After 47 the interval becomes (40,47), proving C. Successive left and right choices are allowed when all ancestor bounds remain satisfied, so D is false.

**Common misconception:** Checking only the immediately previous comparison and forgetting older bounds.

## Q17

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Prime implicants and forbidden expansion.

A covers 0,1; dropping a′ would add minterm 4, and dropping b′ would add 3, both OFF. B covers 2,6; dropping b adds 4 and dropping c′ adds 3, so it is prime. C covers 5,7; dropping a adds 3 and dropping c adds 4, so it is prime. D covers 0,1,4,5 and includes OFF minterm 4, so it is not even an implicant.

**Common misconception:** Checking only that a product covers some ON minterms without checking all of its coverage.

## Q18

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Enumeration without an end-of-output signal.

A correct enumerator must eventually print every member and no nonmember; it need not announce exhaustion. It can keep testing strings forever after its last output, so B holds. A adds an unjustified termination test; C confuses enumeration duration with membership decidability; D is refuted by an enumerator that never prints.

**Common misconception:** Requiring finite languages to have enumerators that halt after their last member.

## Q19

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Equivalent Boolean XOR forms.

A lists the two unequal-input minterms. Expanding B gives xx′+xy′+yx′+yy′=xy′+x′y, so B is identical. C is XNOR, true on equal inputs. D is also true at x=y=1, where XOR is false.

**Common misconception:** Confusing inclusive OR with exclusive OR.

## Q20

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Liveness at a loop fixed point.

At L, p is read by the test, so C is live. The exit branch reads x, and B's assignment also reads old x, so A is live. The path into B reads old y before assigning y=0, making B live. These paths establish all three at the least fixed point; no use of z can propagate liveness, so D is false.

**Common misconception:** Treating a later assignment to y as killing its earlier use within the same iteration.

## Q21

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Differentiability without a continuous derivative.

|f(x)|≤x² gives continuity. The difference quotient x sin(1/x) tends to zero, proving f′(0)=0. For x≠0, f′(x)=2x sin(1/x)−cos(1/x), which oscillates and has no limit at zero, refuting C. Yet |f′(x)|≤2|x|+1, so it is bounded near zero, proving D along with A,B.

**Common misconception:** Assuming existence of a derivative implies continuity of that derivative.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Prefix balance as well as total balance.

A closing parenthesis cannot precede its matching opening parenthesis, so every prefix must have nonnegative unmatched-open count, A. Balanced words have even length, contradicting B; nesting refutes C and can require unbounded stack height, refuting D.

**Common misconception:** Checking only equal total numbers of opening and closing parentheses.

## Q23

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Nonnegative rather than strictly positive weights.

Dijkstra requires no negative edge, so zero weights are permitted, A. Zero edges or equal-cost routes can give equal distances, C. Paths need not be unique, refuting B, and zero cycles do not decrease path costs without bound, refuting D.

**Common misconception:** Confusing zero-weight cycles with negative-weight cycles.

## Q24

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Online scheduling fairness versus finite workloads.

Nearby arrivals can keep winning shortest-seek choices and starve a distant request, proving A and refuting B. For a finite queue without arrivals, each service removes one request, so all are eventually served, C. D describes an endpoint constraint associated with SCAN, not SSTF.

**Common misconception:** Inferring bounded waiting under arbitrary arrivals from termination on a fixed finite queue.

## Q25

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: BST deletion and successor. The original root's successor is 45, the leftmost node in its right subtree. Copy 45 to the root and replace node 45's original link from 50 by its child 47. Thus 47's parent is 50. With no right subtree, its next inorder node is its ancestor 50. B gives (50,50). A and D leave the old parent relation; C and D skip the closer successor 50. Copying the successor key does not move its entire subtree to the root.

## Q26

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: IPv4 fragment payload units. Subtract the 20-byte header: payloads are 512,520,532,536. Dividing by eight gives integers for A, B and D; 532 leaves remainder four, so C fails. MF=1 means more fragments follow, so this is not the final-payload exception. Alignment applies to payload length, not total length.

## Q27

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: exhaustive constraint satisfaction. For prize pairs AB,AC,AD,BC,BD,CD, the numbers of true labels are respectively 2,4,2,3,1,1. Thus only AB and AD are feasible. Both include A and exclude C, making A and C necessary. B fails for AD; D fails for AD as well. Necessary conclusions must hold in every feasible placement.

## Q28

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: comparison lower bounds for merging. Internal orders are fixed, so choose which three of six positions come from the first list: C(6,3)=20, B, not 6!, so A is false. Four comparisons provide at most 16 leaves in a binary decision tree, insufficient; C is false. Five are necessary, and ordinary merging uses at most 3+3−1=5, proving D. A lower bound becomes optimality only when paired with an achieving algorithm.

## Q29

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: duplicate minima. The two pushes of one store only one auxiliary minimum. Popping one removes that minimum even though the other one remains in the data stack, so A is true and B false. Storing equal minima as separate entries keeps their multiplicities synchronized, C. Never removing minima would retain values after their last occurrence was popped, so D fails. An auxiliary summary must represent duplicate occurrences or their counts.

## Q30

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Every spanning tree has two edges, so all tree weights fall by4: A and C are true. Initially A–C and A–B–C both have weight3; afterward their weights are1 and−1, respectively. The shortest-path set changes, making B false and disproving D. The misconception is extending a fixed-edge-count argument to paths of different lengths.

## Q31

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

B attaches both participial actions to the engineer, who also recommends closure. A makes “cracks” the grammatical subject of having inspected. C incorrectly attributes the recommendation to cracks and misattaches inspection. D explicitly reverses the inspector and inspected object. The introductory modifier must attach to the intended actor.

## Q32

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both branch paths evaluate the same unchanged expression, so A is true. However the then and else values are held in different names: t is not defined on the else path and u is not defined on the then path, disproving B and D. Hoisting the side-effect-free expression into a common temporary is legal under the given assumptions, proving C. Expression availability is different from availability of a particular temporary variable.

## Q33

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

E[X]=0, E[Y]=2/3, and E[XY]=E[X³]=0, so covariance is0, proving A and C. Y=0 forces X=0, proving D and disproving independence B: P(X=0,Y=0)=1/3 differs from(1/3)(1/3). Zero covariance does not imply independence.

## Q34

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The nullable foreign key permits NULL, proving A. A non-null value must match an existing id, proving D; its own id is a possible match, proving C. Mutual references between two existing rows also satisfy the foreign key, disproving B. Referential integrity does not impose an acyclic hierarchy.

## Q35

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Negating NOT p OR q gives p AND NOT q, so A is true. Under p=true, p XOR q equals NOT q; under p=false, conjunction with p is false, proving C equivalent. B is the original implication and D represents the opposite asymmetric case.

## Q36

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The passage says intermediate passengers may wait longer, not that every one's total journey must increase. C overstates both universality and the total-time conclusion. A,B,D accurately reflect the location-specific and tentative nature of the findings. Distinguish waiting time from total journey time.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Implication transitivity gives p→r, proving A. Its contrapositive is NOT r→NOT p, proving B. The premises prohibit p true with r false, proving D. The converse r→p need not hold, so C is false. Implication chains do not reverse direction.

## Q38

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The feasible pairs are (1,2),(2,1), both with sum3, so A is true. Joining x's constants1 and2 produces nonconstant; y does the same. Their pairing is lost, proving B and refuting C. A relational invariant x+y=3 can preserve that fact, proving D. Independent possible-value information can admit infeasible combinations unless correlations are retained.

## Q39

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Bitwise NOT1111 is0000, so addition gives0111+0000+1=1000, without a fifth-bit carry. A is true and B false. Signed values are7−(−1)=8, outside the four-bit signed range, proving C. Unsigned values are7−15<0, requiring a borrow, proving D. Carry, unsigned borrow and signed overflow are related but distinct flags.

## Q40

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Each column appears in two rows, so no row is essential; A is false. Each row omits one column, proving B. Every pair of rows covers all three columns, giving exactly the three minimum covers PQ,PR,QR, proving C. After deleting any one row, the remaining pair still covers all columns, proving D. Wide coverage does not make an implicant essential; a uniquely covered required column would.

## Q41

**Correct answer:** A

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Matching consumes one input symbol per stored symbol, so a successful branch's guess splits the length equally, proving A. Immediate guessing accepts ε, proving D. Acceptance is existential, refuting B. Immediate guessing leaves no symbols to match a nonempty input, refuting C.

## Q42

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Don't-cares may be used to enlarge useful cubes, proving A, but they need not be covered, refuting B. OFF inputs must remain0, so C is true. Covering only don't-cares cannot satisfy an additional required ON input and is not mandatory, refuting D. Optimization freedom is not an additional output requirement.

## Q43

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The eight inputs split into four complementary pairs. In each pair, choosing one output forces the other's opposite value. The specified output at000 fixes the pair000/111, leaving three independent binary choices, or2³=8 truth tables. B is correct. A leaves too few free choices; C ignores the fixed pair; D exceeds even the unconstrained self-dual count16.

## Q44

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each transaction's shared lock prevents the other from obtaining an exclusive lock, proving C and allowing the wait cycle in A. Two-phase locking ensures a serializability property but does not by itself exclude deadlock, refuting B. Shared locks are mutually compatible, refuting D. The conflict arises on upgrade.

## Q45

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A finite simulation of k transitions decides both acceptance within the bound and the number of distinct tape cells visited, so A,C are decidable even if binary k makes the simulation expensive. Unbounded acceptance is undecidable, ruling out B. Halting on every input is also undecidable, ruling out D. Complexity and decidability are different issues.

## Q46

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For all n≥1, n≤f(n)≤n². Along odd n, f(n)/n=n grows unbounded, excluding Theta(n). Along even n, f(n)/n²=1/n tends to zero, excluding Omega(n²) and Theta(n²). Thus only D holds. Asymptotic bounds must hold for every sufficiently large input, not only a subsequence.

## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

On the true branch t already equals a+b. On the else branch t equals c+d, so proving equality to a+b there makes the replacement valid on every incoming path: B. A ignores path coverage; C preserves operand values but does not ensure t holds their sum on the else path; D establishes only that t is initialized, not what value it contains. Availability and value equivalence are properties of all feasible predecessor paths.

## Q48

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Substituting x=0 leaves y AND1=y, proving A; x=1 leaves 1 AND z=z, proving B. With x=0,y=1,z=0, F=1 but yz=0, refuting C. With x=1,y=0,z=0, F=0 while x XOR y XOR z=1, refuting D. The expression implements a selector, not a three-way parity operation.

## Q49

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The closure can redirect readers, so B is a plausible contributor, not an established cause. Sampling only voluntary evening visitors leaves other users' views unconstrained, giving D. A claims a uniquely identified cause despite the simultaneous change. C incorrectly generalizes a selected sample to all residents. Evidence of perceived usefulness among respondents does not by itself establish population-wide opinion or causality.

## Q50

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For id=1 only employee 11 passes the ON condition; both counts are 1. For id=2 the left join supplies one NULL-extended row. COUNT(*) counts it, while COUNT(E.eid) ignores its NULL, yielding n=1,m=0. Hence A,B are true and D false. Moving the active filter to WHERE rejects that NULL-extended row, removing id=2 and disproving C. Filtering matches and filtering the joined result have different effects on outer joins.

