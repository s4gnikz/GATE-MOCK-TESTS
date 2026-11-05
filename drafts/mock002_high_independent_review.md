# Mock 002 — high-mark core question review

Reviewed 2026-10-13 by a separate model reviewer. The first pass solved the question-only file `mock002_high_questions.md` without reading author solutions or keys. This is model review, not human review. No new Python code was created or executed. Comparison with the full released Mock 001 paper was performed for reasoning-task overlap; this is not a search of every published examination or textbook.

Initial status: Q42 needs its mapping made explicit; Q43 and Q61 are pending author revisions. Q51 is technically sound but uses the standard textbook CFL nonclosure example and is recommended for redesign. Difficulty must not be inferred from its two-mark allocation. Several items below are only Medium.

## Q36 — 1536 — Medium-Hard

There are 256 eight-bit prefixes; 200 consume their entire suffix spaces, leaving 56. These support 56*16=896 twelve-bit opcodes. Allocating 800 consumes 800 suffix blocks, leaving 96 blocks of 16 sixteen-bit strings each: 1536. A prefix-tree allocation achieves the bound, so this is a maximum, not merely an upper bound. Exact integer NAT is appropriate. No correction.

## Q37 — 8 — Medium-Hard

Insert 35 into the middle leaf: [20,25] and [30,35]. The root now has four children, splits into two internal nodes with two children each, and receives a new root. The count becomes four leaves, two internal nodes, one root =7. Insert 55 into [40,45,50]: split into [40,45] and [50,55]. Its parent grows from two to three children without splitting. Count 8. The specified split conventions remove ambiguity. No correction.

## Q38 — A,C — Medium

A spanning tree needs three edges and can attain total weight 3 using any three sides of the square. Exactly four such subsets exist; any diagonal makes the total at least 4. Thus A and C are true, B false. After reducing AB to zero, every optimum uses AB and any two of the other three sides: three spanning trees of weight 2 remain. D is false. This is straightforward enumeration and should not be labelled Hard. No correction.

## Q41 — C — Medium-Hard

Use 10.4.1.0/24, 10.4.2.0/23, 10.4.4.0/23, 10.4.6.0/24. An aligned /22 block would include either third octet 0 or 7, outside the interval. A prefix covering octet 1 cannot include octet 2; similarly the final /24 cannot merge inward with octet 5. The four is necessary and achievable. A=2, B=3 underestimate; C=4 is correct; D=6 is feasible but not minimal. No correction.

## Q42 — A,C,D, conditional on explicit mapping — Medium

The question should state that public ports 41001 and 41002 map to hosts 10.0.0.1 and 10.0.0.2, respectively. Without that word or explicit mapping, A is not forced by the assigned port set. Under the intended mapping A is true; B is false because the remote source is the public address; C is true because the IPv4 header checksum covers the changed source address; D is true because the TCP checksum covers the source port and a pseudoheader containing the source IP. Awaiting mapping correction.

## Q43 — revision pending

The first draft's familiar 100,500,200,300,600 hole scenario with requests 212,417,112,426 is a standard textbook example and should not be released as a newly original question. Author is replacing it. This review does not approve that draft.

## Q45 — B — Medium, lower end; redesign recommended

The bit patterns denote -128 and 1 signed, versus 128 and 1 unsigned. Thus signed A<B is true and unsigned A<B is false, selecting B. A and C get the signed comparison wrong; D gets the unsigned comparison wrong. The flags are unnecessary to solve the question; the elaborate ALU setup does not create two meaningful steps. It is simpler than a typical two-mark item. Mock 001 Q16 already tests subtraction flags, though its requested output is meaningfully different. Recommend a task requiring inference from flags rather than simply reading the operands.

## Q46 — 3 — Medium-Hard

Two initial loads are necessary because p and q can designate distinct objects with arbitrary initial values and both a and b are outputs. After the store, c requires a fresh load of q because it may alias p; b is not always reusable. The optimizer knows d=7 and can reuse c for e because no intervening memory store occurs. Three loads are sufficient and fewer cannot preserve every required output for every alias case. No correction.

## Q47 — A,B,D — Medium-Hard

A is the consensus theorem: BC is already covered by AB or NOT(A)C according to A's value. With B=C=1, unequal path delays can momentarily turn both original product outputs off during an A transition, making B true. ABC also depends on A and can be off during the same gap; it provides no delay-independent protection, so C is false. BC stays high throughout that transition and holds the OR output high, so D is true. Settled initial state and single changing input are adequate. No correction.

## Q48 — B — Medium

The only cross-transaction data conflict is w1(x) before r2(x), giving edge T1->T2 and no cycle. T2 reads from T1 but commits before T1, so recoverability fails. It also reads before the source commits, failing cascadelessness. A falsely asserts recoverability; B is correct; C gets both properties wrong; D falsely asserts cascadelessness. No correction.

## Q49 — 16 — Medium

Directory indices are floor(VPN/1024): 0,0,1,1023. Three second-level pages plus one directory page consume 4*4=16 KiB. Mapped data pages are explicitly excluded. No correction.

## Q50 — D — Medium-Hard

The finite language has a DFA, so A can recognize it. An NPDA can guess when to pop its bottom symbol, so B can recognize it. A final-state DPDA can retain its stack and simulate the DFA, so C can recognize it. An empty-stack DPDA without an end marker must terminate its accepting computation on a, leaving no stack for the additional b in ab; determinism rules out an alternate computation. Thus D cannot recognize the non-prefix-free language. All acceptance conventions needed for this distinction are stated. No correction.

## Q51 — A,C — Medium; originality redesign recommended

Both individual languages are context-free. CFLs are closed under union and concatenation, so A,C are true. Their intersection is {a^n b^n c^n:n>=0}, which is not context-free and therefore not regular; B,D are false. Technically correct but this is the canonical textbook nonclosure example with standard closure questions; no novel reasoning task is apparent. This reviewer found no evidence of verbatim copying, but cannot certify it meets the requested originality standard. Recommend redesign before release.

## Q52 — C — Medium-Hard

Root must be 7. Choose the three keys for the left subtree in C(6,3)=20 ways. Within either three-node subtree its largest key is fixed at its root and its two leaves can be exchanged in two ways. Total 20*2*2=80, selecting C. A=40 loses one subtree's ordering factor, B=64 is not the count, D=120 is not the count. No correction.

## Q53 — C — Medium

Closed two-edge walks contribute M12*M21+M13*M31=2 at start 1, M21*M12+M23*M32=3 at start 2, and M31*M13+M32*M23+M33*M33=2 at start 3. Sum 7, selecting C. A=4 omits contributions, B=5 undercounts parallel-edge/reverse starts, D=9 overcounts. The explicit edge and start conventions remove ambiguity. This is a short computation, not Hard. No correction.

## Q55 — A — Medium-Hard

Each upgrade waits for the other's shared lock, so the wait-for graph is a two-cycle. Retaining exclusive locks through commit prevents dirty reads; A is true. Shared/shared compatibility does not mean exclusive/shared compatibility, so B is false. Releasing before acquiring another lock crosses from shrinking back into growing, so C is false. Exclusive-before-read serializes both increments and prevents a completed lost-update execution, so D is false. No correction.

## Q56 — B — Medium-Hard

First call saves a pointer to a[0], changes p to a[1], makes a[0]=2+5=7, then a[1]=6. Second call saves a pointer to a[1], changes p to a[0], makes a[1]=6+7=13, then a[0]=8. p-a=0. Output 8 13 0 selects B. A omits the last increment; C ignores the second call; D falsely treats legal aliasing as undefined behaviour. Each full expression is sequenced before the next and all pointer operations remain in the array. No correction. Supplementary evidence reported by the parent reviewer: extracted C compiled with installed GCC using `-std=c11 -Wall -Wextra -Werror -pedantic`, executed with exit 0 and output `8 13 0`. This reviewer did not run that command; the execution supports the trace but is not itself a proof of absence of undefined behaviour.

## Q57 — C — Medium-Hard

After accepting a, the lexer must keep exploring ab*c through n occurrences of b. The d makes that longer candidate impossible, requiring retreat to the accepting position after a. It can therefore examine n+1 further characters and the bound grows without limit. A,B give false fixed bounds; C is correct; D violates longest match on inputs that instead finish with c. No correction.

## Q58 — A,B — Medium-Hard

The simple routes have weights s-a-t=4, s-b-t=15, and s-b-a-t=3, so A is true. Specified Dijkstra settles a at 2, then t at 4 before b at 5, making B true. Adding 4 per edge changes these path weights to 12,23,15, so the minimizer changes and C is false. The graph is acyclic; D is false. Algorithm variant and stopping rule are explicit. No correction.

## Q59 — A,C — Medium-Hard

FIRST(aSbS)={a} and FOLLOW(S)={b,$}; the epsilon production's predictive entries do not conflict, so A is true. LL(1) implies unambiguous, so B is false. In LR item states containing epsilon reduction S->dot, shifts are on a, while SLR restricts that reduction to b or $, avoiding conflicts; the other completed production occurs in a reduction-only state, so C is true. LR(0) has both the epsilon reduction on all symbols and an a shift in the initial state, so D is false. No correction.

## Q60 — A,B,D — Medium-Hard

Direct blocks are 0..3, single-indirect blocks 4..259, double-indirect blocks 260..262. One single-indirect block plus the double-indirect root plus one child indirect block gives three metadata blocks, making A true. Reading 260 uncached needs double-indirect root, child, then data =3 reads, making B true. C is false because 259 is still single-indirect. Data size is 263*1024=269312, making D true. No correction.

## Q61 — revision pending

The initial answer was min(10000,6500)-4000=2500, but this single subtraction was too straightforward for the intended two-mark depth. Author is adding a window/ACK evolution scenario. This review does not approve the revised question until it is read.

## Q62 — B — Medium-Hard

Every legal decomposition has 1<=|y|<=p. Pumping twice yields p^2+|y|, strictly above p^2 and at most p^2+p, strictly below p^2+2p+1=(p+1)^2. B is valid for every decomposition. A wrongly fixes |y|=p; C proves failure for only one decomposition; D is false (pumping down does not generally land at the previous square, and membership there would not contradict regularity). This repeats the quantifier-trap theme of Mock 001 Q50 but has a different regular-language lemma and square-gap argument, so it is not a constants-only duplicate. No correction.

## Q63 — C — Medium-Hard

Every pair misses exactly one required column: P1P2 misses m6, P1P3 misses m5, P1P4 misses m4, P2P3 misses m3, P2P4 misses m2, P3P4 misses m1. All four triples cover every column. Literal totals of triples P1P2P3, P1P2P4, P1P3P4, P2P3P4 are 8,9,9,10. Thus C selects the unique least-literal three-term cover. A is not a cover; B is a cover with nine literals; D is a cover with ten. The question asks only the covering stage on the supplied chart. No correction.

## Q64 — B — Medium-Hard

B issues START once, repeatedly polls without side effects, and after readiness loads data and increments once. A can issue START and increment repeatedly while waiting; C repeats the increment during its wait; D can capture data before readiness. The statement that operations repeat on every visit makes these errors determinate. No correction.

## Q65 — B — Medium-Hard

The tournament always performs 12 comparisons to reduce 13 keys to one. Positions 1..12 have a first-round opponent. Keys in positions 1..8 have four opponents if minimum; keys in positions 9..12 have three, because their branch gets a later bye. Position 13 gets byes in the first two rounds and has two opponents. Scanning the loser's list then costs between 1 and 3 comparisons. Total range is 13..15. A's lower endpoint 12 is impossible; B is correct; C exceeds the maximum; D ignores the byes. No correction.

## Remaining actions

Review author revisions of Q42,Q43,Q61; redesign Q45/Q51 if requested by parent. Compare final author answer key and solutions against these independently derived answers. Whole-paper release remains the parent's responsibility, including subject/difficulty counts and resolved originality concerns.
