# Mock 019 draft checkpoint — 18 October 2026

Unpublished replacement draft has Q1–Q65, at drafts/mock019_rebuilt_README.md. No key or solutions yet. Old paper and solutions are backed up under archive/pre-rebuild-2026-10-18/Mock_019/; do not overwrite that backup. Do not count this as a rebuilt paper. Resume by completing all worked solutions and the final key, then perform all checks. Proposed answers below are author-derived, not independent verification.

1 C; 2 4; 3 C; 4 5; 5 B; 6 0.3333 (range 0.33325–0.33335); 7 D; 8 6; 9 C; 10 0.5556 (range 0.55555–0.55565); 11 C; 12 6; 13 9; 14 4; 15 7; 16 3; 17 B,C; 18 A,C; 19 1; 20 A,D; 21 1; 22 1; 23 1; 24 16; 25 A,C; 26 0.3; 27 2; 28 5; 29 1.5; 30 3; 31 3; 32 B,D; 33 B; 34 4; 35 3.

Reasoning notes: Q2 endings 12,20,32 admit 1,2,1 leading pairs. Q4 inverse folds yield original coordinates 2,4,6,8. Replacement Q6: fix the first subset; nine nonidentical second subsets remain, three have union all five, probability1/3. Q8 cumulative A=4(2^n−1), B=(3^n−1)/2; n5 gives124 versus121 and n6 gives252 versus364. Q10 remaining painted faces30, newly exposed24; fraction30/54. Q16 with don't-care single literal c; without it needs a'c+b'c (four literals), difference3. Q26 normalization c=6, second moment6(1/4−1/5)=0.3. Replacement Q27: exponent2026 is even but not divisible by three; only4,5 are fixed. Q35 p≤2 fails on a³; p3 works using pump lengths3 for a³,2 for a⁵,1 for all lengths≥6.

Mathematics one-mark slots are22,26,27,29,33; two-mark slots to author are37,54,59,65. Difficulty and originality remain unchecked. In particular textbook families such as dynamic-array amortization and implicant charts must be compared against earlier papers before inclusion. The full 100-paper series remains incomplete; only Mock001 is accepted in the canonical bank.

## Continuation saved: Q36–Q65 now drafted

The replacement now has all 65 question stems but still no answer key or worked solutions. Do not publish it as complete. Review the questions before accepting the proposed answers below; do not mistake this authoring ledger for verification evidence.

36 A,C; 37 0.5385 (range 0.53845–0.53855); 38 B,D; 39 19; 40 4; 41 B; 42 A,C; 43 7; 44 A,C,D; 45 A,C; 46 A,C; 47 B; 48 7; 49 10; 50 0.25; 51 A,C; 52 8; 53 7; 54 10; 55 4; 56 C; 57 112; 58 B,C; 59 3.5; 60 A,C; 61 A,D; 62 7; 63 B,D; 64 B; 65 0.6817 (range 0.68165–0.68175).

Important derivations to verify independently: Q37 posterior (7/8)/(3/4+7/8)=7/13. Q40 Moore states encode (previous bit, last output), all four distinguishable. Q43 leaders1,2,3,4,7,9 and seven distinct edges. Q44 reachable subsets {p},{p,q},{p,r},{p,q,r}; after010 set{p,q}. Q47 minimum-node recurrence N(h)=1+N(h−1)+N(h−2) gives20 nodes, leaf recurrence gives8. Q48 RHS list ABA,BA,AA,AB,A,B,epsilon. Q49 multiply completion3..8 with adds ending4..9; unpipelined multiply completion3,6,...18, last add19, gain10. Q51 addA gives safe sequence P,R,Q; addB alone enables none. Q54 row-prefix lengths 0≤b≤a≤3 give10. Q59 Pb=(2,1,3), forward values(2,−3,14), x3=14/4. Q62 visited8,4,6,7,12,10,9. Q65 crossing r=(sqrt5−1)/2 gives integral(5sqrt5−3)/12.

Potential originality/difficulty concerns to review: Q17 implicant chart family; Q18 dynamic-array amortization; Q40 automaton-state minimization; Q46 aggregation with exceptions; Q58 loop-invariant constant expression resembles but extends Mock018 Q11's branch correlation; Q64 remote-aware NAT capacity extends Mock017 Q49 and must be assessed for meaningful reasoning novelty. No cross-series lexical screen or independent verification has yet been performed for Mock019.


## Lexical/structural review performed on the draft

Number-normalized word-trigram screening compared all 65 draft stems with the 1,170 stems of Mocks001–018. It is screening, not semantic certification. The high Q65/integration lexical match was inspected and is a false positive: max-envelope integration requires splitting at an algebraic crossing, unlike Mock016 Q24's substitution integral. Further inspection found true repeated reasoning in Q15 versus Mock004 Q21 (link-state transient loops), Q27 versus Mock001 Q35 (rank-two idempotents), and Q28 versus Mock007 Q18 (VIPT capacity/index constraint). These were replaced with duplicate-suppressed LSP flooding, powers of disjoint permutation cycles, and dirty line-transfer tracing. Q6 was proactively replaced because its conditional minimum reduced to the order-statistic family in Mock007 Q10.

New proposed answers after replacements: Q6=0.3333; Q15=7; Q27=2; Q28=5. Q15: source degree2 plus A's2, B's2, C's1 forwarded transmissions totals7; equivalently2E−(V−1). Q28: three fills and two dirty evictions, no final flush. The earlier draft answer forms for those questions are obsolete. Q2 versus Mock004 Q8 changes the divisibility rule from a final-digit rule to final-two-digit cases, but remains flagged for stricter task-family review. Q17/Q18 and the other previously listed family concerns still need deeper comparison. Do not declare uniqueness accepted.

## Superseded draft status
The key and all worked solutions are now saved and the replacement is published as review-pending. See MOCK_019_REBUILD_2026-10-18.md for actual checks and remaining gates.
