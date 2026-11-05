# Mock 002 — independent GA and mathematics review

Reviewed: 2026-10-13. Scope: the 19 questions in `mock002_main.json`.

Provenance: this is a separate model review, not human review or a blind review. The reviewer read both the author answers and the saved computational evidence in `review_mock002_main_evidence.json`, then checked the reasoning below. The saved enumeration results were inspected for consistency; they were not rerun in this review. No new Python program was created. Computational observations on finite examples are supplementary to the general proofs below.

Outcome: all 19 proposed answers agree with this review. No mathematical or option-key correction is required. Difficulty labels are judgment estimates, not empirically calibrated timings. Q1 is a routine contextual-vocabulary item at the easier end of the proposed Medium band; Q2 and Q6 are also relatively straightforward. This review does not establish series-wide uniqueness or whole-paper syllabus/structure compliance.

## Q1 — B — Medium, lower end

The requirement to run a smaller pilot limits the endorsement, so the contextual meaning is conditional support. A contradicts the reservation; B expresses it; C confuses a qualified endorsement with the qualifications of the speaker; D wrongly removes support altogether. The text determines one answer. No issue.

## Q2 — 20 — Medium, lower end

Write the growth multiplier at time t as exp(rt). Since 12r=ln(8)=3ln(2), the time for factor 32 is ln(32)/r=5ln(2)/(ln(2)/4)=20 hours. Exact NAT value 20 and zero decimal places are appropriate. No issue.

## Q3 — B — Medium

For the five rows in order, the observed acceptance vector is false,true,true,false,false. A gives true,true,true,false,false, failing row 1. B (red AND exclusive-or of circular and filled) matches every row. C accepts the blue hollow circle in row 5. D accepts every listed row because every blue card shown is circular and the other cards are red. Thus A,C,D are false and B alone is true. Specifying the candidate set avoids the usual underdetermination of induction questions. No issue.

## Q4 — C (face D) — Medium

B is adjacent to A and C from the first view and to F and E from the third. Four distinct adjacent faces exhaust B's possible neighbours, so the remaining face D is opposite B. The second view is consistent: the side ring around top A can be B,C,D,E, with F below. Option A (face A) is false, option B (face C) is false, option C (face D) is true, and option D (face E) is false. The distinction between option letters and face labels needs care in the answer key; canonical option C is correct. No figure is necessary.

## Q5 — 15 — Medium

Direct recurrence evaluation gives a3=2(5)-2+3=11, a4=2(11)-5+4=21, a5=2(21)-11+5=36. The requested difference is 36-21=15. Equivalently first differences grow by 3,4,5. Exact integer NAT accepted value 15 is correct. No issue.

## Q6 — B — Medium, lower end

The planted area must be 160-88=72. The path has width w on both sides of each dimension, giving (16-2w)(10-2w)=72. Roots are 2 and 11; only 2 lies between 0 and 5. Direct option checks give path areas 48,88,120,144 for A,B,C,D respectively. Only B fits. No issue.

## Q7 — B — Medium

The past event is counterfactual, requiring “had left” and “would have caught.” An introductory participial phrase must refer to the following subject, so “Having reached ... the meeting” wrongly attributes arrival to the meeting. A fails both requirements; B fixes both and retains the meeting's earlier start; C leaves the dangling modifier and changes the counterfactual result; D has an unsuitable conditional and exchanges the intended agents. One correct option. No issue.

## Q8 — B — Medium

Initially milk and water are 72 and 48. The first removal scales both by 3/4, and the water refill leaves (54,66). The second removal scales those by 5/6, leaving (45,55); adding milk produces (65,55), ratio 13:11. A reverses the components; B is correct; C retains an obsolete initial ratio; D implies 70 litres milk, which is wrong. No issue.

## Q9 — A,C — Medium-Hard

Because C occupies position 5, B and D must occupy either {1,3} or {2,4}. In the former case E can be 2 or 4, leaving A the other position. In the latter E must be 3 and A must be 1. Reversing B and D in these three cases gives six valid schedules, agreeing with the saved enumeration. A is true (B,E,D,A,C); B is false (same witness); C is true (A,B,E,D,C); D is false (the latter witness). No issue.

## Q10 — B — Medium-Hard

Every column must contain a stack reaching its column maximum, so at least 2+3+1=6 cubes are necessary. Rows [0,3,1] and [2,0,0] achieve six and satisfy row maxima 3,2. Each entry is bounded by the smaller of its row and column maximum, so the total is at most sum([2,3,1])+sum([2,2,1])=11; those rows achieve eleven. A has the wrong minimum, B has both tight bounds, C has an impossible maximum, D has both wrong. No issue.

## Q22 — A,C — Medium-Hard

Subtracting twice row 1 from row 2 and row 1 from row 3 leaves trailing matrix [[t-4,1],[1,0]], whose determinant is -1. A is true. At t=4, a unit-lower unpivoted factorization would force U22=0 but would need the (3,2) residual 1 to equal L32*0, impossible; B is false. Swapping trailing rows at t=4 makes the block identity, so C is true. At t=5 the final pivot is 0-1*1=-1, so D is false. Nonsingularity and existence of unpivoted LU are correctly distinguished. No issue.

## Q24 — 0.667 — Medium

The lines meet at x=1/3. The upper envelope is 1-2x on [0,1/3] and x on [1/3,1]. The corresponding areas are 2/9 and 4/9, total 2/3. Rounding to three decimal places gives 0.667. An exact acceptance of the explicitly requested rounded result is coherent; the key should show 0.667, not claim that 2/3 itself is the three-decimal answer. No issue.

## Q29 — 7.6 — Medium-Hard

The pooled mean is 4. Within-group squared deviations total 3*2+2*1=8. Shifts from individual group means to 4 contribute 3*(2-4)^2+2*(7-4)^2=12+18=30. Thus the total squared deviation is 38, divided by five gives 7.6. Both population sizes and variance convention are explicit. Exact one-decimal NAT value 7.6 is correct. No issue.

## Q33 — D — Medium-Hard

Modulo 5 the inverse multiplier of 2 is 3. Composing right to left sends x to x-1, then 3x-3, then 3x-2, then 6x-4=x+1. Therefore h has a single five-cycle. A (order 1), B (order 2), and C (order 4) all fail by their effect on 0; D (order 5) returns every residue and is least positive. No issue.

## Q35 — A,B — Medium-Hard

Degree sum is 14, forcing seven edges: A is true. Connectedness and exactly two odd vertices imply an open Euler trail: B is true. Two triangles joined by a bridge have precisely the given multiset. Their odd cycles disprove C, while the bridge prevents a Hamiltonian cycle and disproves D. The same counterexample is sufficient for both universal claims. No issue.

## Q39 — 5 — Hard

Independent orbit argument: count labelled proper colourings with two of each colour. There are 90 unrestricted colourings. For a particular colour, adjoining its two beads selects one of six edges and six assignments of the other four positions, giving 36. For two specified adjacent pairs, choose an edge and one of three disjoint edges, giving 18. All three adjacent pairs use one of two perfect matchings and one of six colour assignments, giving 12. Inclusion-exclusion gives 90-108+54-12=24. Under rotations of a six-cycle, the identity fixes 24; shifts 1 and 5 fix none; shifts 2 and 4 require colour counts divisible by 3 and fix none; shift 3 fixes exactly the six repetitions of a permutation of the three colours. Burnside's average is (24+6)/6=5. This independently verifies completeness rather than merely inspecting a list. The saved five representatives are consistent. Rotation-only equivalence and reflection handling are explicitly stated. Exact integer NAT value 5 is correct. No issue.

## Q40 — B — Hard

Let F(x,y) mark length by x and number of ones by y. Splitting a nonempty valid word into a leading 0 followed by any word, a lone 1, or leading 10 followed by any word gives F=1+xF+xy+x^2*y*F. Thus F=(1+xy)/(1-x-x^2*y). Even parity is extracted by [F(x,1)+F(x,-1)]/2. Combining fractions gives numerator 1-x+x^3 and denominator (1-x)^2-x^4. B is true. A includes the odd-parity length-one string; C gives two strings at length 2 whereas only 00 has even parity; D has coefficient 1 at length 3 whereas both 000 and 101 qualify. No analytic convergence assumption is needed for formal generating functions. Saved coefficients through length 12 agree with this derivation but are not the basis for the general identity. No issue.

## Q44 — B,D — Hard

Under E one can continue an edge walk indefinitely. In a finite nonempty domain a vertex repeats; transitivity collapses the resulting nonempty cycle to a self-loop, contradicting I. Therefore A is impossible and C, which adds F to A, is also impossible. B has the two-point relation {(u,v),(v,u)}: exactly one successor per point, symmetric and irreflexive. D has the one-point relation {(u,u)}, which is serial, transitive and symmetric. These witnesses establish B,D and the finite-cycle proof rules out A,C at every finite size; bounded enumeration alone would not prove impossibility. No issue.

## Q54 — 4 — Hard

Commuting with a single four-cycle shift forces all entries to be invariant under simultaneous cyclic row and column shifts, so X is circulant. Symmetry restricts its first row to (a,b,c,b). The all-ones constraint gives a+c+2b=0. On the alternating vector (1,-1,1,-1), X has eigenvalue a+c-2b=-4b; on the independent plane {(p,q,-p,-q)}, its action is multiplication by a-c. These subspaces together with the all-ones line form a direct sum of dimensions 1+2+1=4. Idempotence is therefore equivalent to each of the two remaining eigenvalues being 0 or 1. Every pair uniquely determines b=-mu/4, a=mu/4+nu/2, c=mu/4-nu/2, so there are four and only four matrices. They are the zero projector, the alternating-line projector, the two-dimensional plane projector, and I-J/4. The four saved explicit matrices match these cases. Completeness follows from the centralizer and symmetry constraints, not enumeration of arbitrary matrices. Exact integer NAT value 4 is correct. No issue.

## Release guidance

Answers: Q1 B; Q2 20; Q3 B; Q4 C; Q5 15; Q6 B; Q7 B; Q8 B; Q9 A,C; Q10 B; Q22 A,C; Q24 0.667; Q29 7.6; Q33 D; Q35 A,B; Q39 5; Q40 B; Q44 B,D; Q54 4.

These 19 questions pass this scoped correctness and ambiguity review. Parent-level checks must still cover the other 46 questions, rendered Markdown, all 65 answer-key entries, syllabus coverage, mark allocation, and duplicate review against released material. Do not describe the whole paper as human-reviewed or this review as blind.
