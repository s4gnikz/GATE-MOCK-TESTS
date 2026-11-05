# Mock 002 targeted review — 26 October 2026

Status: bounded model-based review; no answer corrections identified. This is not human review, a separate-model approval, full-paper acceptance or difficulty certification.

## Questions examined
| Source Q | Result and reasoning |
|---|---|
| 38 | A,B,C retained. Weight-6 trees: 3×3×3=27. Weight-7 trees: 9 using AE plus 36 with two weight-2 connectors. AE gives a counterexample to D. |
| 42 | A,C,D retained. Reverse port mapping identifies host 2; source IP affects both IPv4 checksum and TCP pseudoheader; the TCP port affects its header checksum contribution. |
| 43 | A retained. First-fit places B at 100; best-fit at 200. Freeing A and X creates largest holes 100 and 180 respectively. |
| 45 | B retained. Negative signed A minus nonnegative B overflows negatively iff b>r for A=128+r. Strict triangular count 8128. Prior interrupted review independently enumerated all 65536 byte pairs and obtained 8128. |
| 48 | B,C,D retained. Original conflicts include 1→2→1. View orders require 2<4<1 and 3<4, giving exactly two. Deleting initial w1 gives forced chain 3<2<4<1. |
| 51 | A,C retained. Bounded j makes a finite regular union. Removing regular R preserves context-freeness; the c-free slice is nonregular. Intersecting with S forces equal three-block counts, not context-free. |
| 53 | B retained. Two choices for the 1→2 edge give eight rotations of combined two-cycles; the three-cycle plus loop gives four. Prior interrupted review enumerated distinct-edge four-tuples and obtained 12. |
| 61 | 5000 retained. Sending opportunities permit 2000,0,3000 bytes with persistent next sequence number. |
| 39 | 5 retained. Inline JavaScript enumerated all 729 length-six colour strings: 24 valid labelled strings and 5 rotation orbits. No reflection quotient was applied. |
| 40 | B retained. Even-parity projection gives (1-x+x^3)/((1-x)^2-x^4). Direct enumeration through n=10 yields 1,1,1,2,4,7,11,17,27,44,72, agreeing with the rational-function recurrence. Other options fail at degrees 1,2 or 3. |
| 44 | B,D retained. A finite total successor relation has a cycle; transitivity forces a forbidden loop under I. Two-point swap witnesses B; singleton loop witnesses D. |
| 54 | 4 retained. Symmetric circulants have independent eigenvalues mu and nu after zero row sum. Idempotence restricts each to 0 or 1, yielding four matrices. |

The eight revised questions were read and re-derived during the preceding interrupted review; this report persists those findings alongside the four additional mathematics checks. No paper content was changed. No canonical record was promoted to ACCEPTED. Adapted occurrences retain their separate mapping checks and source-review limitations.

## Next review scope
Continue source Mock 002 Q36,Q37,Q41,Q46,Q47,Q49,Q50,Q52,Q55–Q60,Q62–Q65, prioritizing substantive errors. Do not repeat the twelve checks above unless their source content changes. Afterwards reconcile earlier review evidence for remaining questions and assess difficulty; this twelve-question pass alone does not complete Mock 002.

## Reviewed source blocks

SHA-256 of exact question heading and body as read; solutions reviewed separately.

| Q | SHA-256 |
|---|---|
| 38 | a8447a1d6afd91d8b5a0b9829e8a4efdbfdb3aa841d0f43672353aa82a0a03dc |
| 42 | 7ac0a8fb70c9ec10ecb25620a85646fd097cf5206e76870f1a8234c54fedd52a |
| 43 | a991b638006c42985d03d4257d3dca4ce7ff696a889392aa4e58c76052680e2f |
| 45 | d767fbb923e613390043e1ff3f37b48020c46ca50ca2a2d5bce6017856a74e23 |
| 48 | a0ae98c9563d991847599d97addabe0e5f2abe7b96a9f364c1101e30808e9b55 |
| 51 | 38fb045313ec8b5a92e49632538c8e8030cc812fd5ddadb5f240a5f69082bc7a |
| 53 | 7358225ba2c9dde37ecf39d1b1262c8069a6d3e0d1c58088695beac94a919039 |
| 61 | 111e406cf16d413bd3170432018505bd055e8e149f47985b489c4bdea96e1514 |
| 39 | 4e0f001c7ab6a024541e7e2bf1056244044f964ba6dd0f3e5730265578497c4f |
| 40 | 8b46960d20abc1596312623990285d00f4323834998578890f92adbe88b2887e |
| 44 | ca33c81a03bc43a305945ca558262fe4bcd5d9709b616f6f2c5943a42cbc4131 |
| 54 | 160843225295715c3334ba5598d2375b91bc1eef726aed0bac56e2aec5c9a5bb |
