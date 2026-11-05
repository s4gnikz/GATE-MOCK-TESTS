### Q36

**Correct answer:** 1536 (exact).  
**Concept:** Expanding opcodes and prefix-free decoding.

There are 256 eight-bit prefixes. The 200 two-register opcodes consume 200 complete prefix subtrees, leaving 56. Each unused eight-bit prefix supplies 16 possible twelve-bit opcodes, so there are initially 56*16=896 available twelve-bit prefixes. Allocating 800 one-register opcodes leaves 96 such prefixes. Each can supply 16 sixteen-bit zero-register opcodes, giving 96*16=1536. Equivalently, subtract complete instruction encodings: 65536-200*256-800*16=1536.

**Common misconception:** Instructions with different operand counts cannot reuse an opcode prefix that already decodes as a shorter opcode.

### Q37

**Correct answer:** 8 (exact).  
**Concept:** B+ tree split propagation.

Inserting 35 splits the middle leaf into [20,25] and [30,35]. The root now has four children and separators 20,30,40. Split it into two internal nodes, with separator 30 in a new root. The two child internal nodes have separators 20 and 40. At this point there are four leaves, two internal children and one root: seven nodes.

Inserting 55 splits [40,45,50,55] into [40,45] and [50,55]. Its parent acquires separator 50 and has three children, so it does not overflow. The final tree has five leaves and three internal nodes, for eight nodes.

**Common misconception:** A leaf split can trigger an internal split and creation of a root; later splits need not propagate to the root.

### Q38

**Correct answer:** A, C.  
**Concept:** Equal-weight cycles and minimum spanning trees.

A spanning tree has three edges. Since every edge weighs at least 1, its weight is at least 3. Deleting any one edge of the unit-weight four-cycle attains weight 3, giving four trees. These are all optimum trees: any diagonal would increase the weight to at least 4.

- A is true: choose the omitted cycle edge in four ways.
- B is false: AC weighs 2 and cannot be in a weight-3 tree.
- C is true: all three edges must have weight 1.
- D is false: after AB becomes 0, choose any two of BC,CD,DA together with AB. Each of these three trees weighs 2.

**Common misconception:** Making one edge uniquely light need not eliminate choices among the remaining edges.

### Q41

**Correct answer:** C.  
**Concept:** CIDR alignment and exact range covering.

One optimal cover is 10.4.1.0/24, 10.4.2.0/23, 10.4.4.0/23 and 10.4.6.0/24. The first /24 cannot be enlarged without including third octet 0. The last /24 cannot be enlarged without including third octet 7. The intervening four /24 blocks, third octets 2 through 5, are not one aligned /22, and therefore require at least two prefixes. Thus at least four prefixes are necessary, and the displayed four suffice.

A and B underestimate the alignment constraints. C attains the lower bound. D is feasible using six /24 prefixes but is not minimum.

**Common misconception:** A power-of-two number of addresses forms a CIDR block only when the starting address has the required alignment.

### Q42

**Correct answer:** A, C, D.  
**Concept:** Port-translating NAT and transport pseudoheaders.

The NAT distinguishes the simultaneous connections using its assigned public ports. Its reverse mapping for 41002 restores destination address 10.0.0.2 and destination port 5000.

- A is true by the stated mapping.
- B is false: the server sees public source address 198.51.100.6 for both connections, with distinct source ports.
- C is true: the source address is part of the IPv4 header covered by its header checksum.
- D is true: the TCP checksum covers the TCP header, including the source port, and an IPv4 pseudoheader that includes the source and destination addresses.

**Common misconception:** A transport checksum can depend on network-layer addresses even though those addresses are not in the TCP header itself.

### Q43

**Correct answer:** A.  
**Concept:** Placement policies with external fragmentation.

First-fit places 212 in the 500-unit hole, leaving 288; 417 in the 600-unit hole, leaving 183; and 112 in the 288-unit remainder, leaving 176. The 426 request cannot fit. Final hole sizes are 100,176,200,300,183; their maximum is 300.

Best-fit places 212 in 300, 417 in 500, 112 in 200 and 426 in 600. The final holes, in original address order, are 100,83,88,88,174; their maximum is 174.

A matches both traces. B mistakes the last-address remainder for the largest first-fit hole. C uses a first-fit remainder as the best-fit maximum. D interchanges the policy results.

**Common misconception:** First-fit restarts at the beginning; it is not next-fit, and total free space does not guarantee that a request fits.

### Q45

**Correct answer:** B.  
**Concept:** Signed comparison after subtraction.

The bit patterns mean -128 and 1 as signed values, so signed A<B is true. As unsigned values they are 128 and 1, so unsigned A<B is false. The subtraction produces low bits 01111111, C=1,N=0,V=1. Thus the signed comparison uses N XOR V=1; using N alone would fail because the mathematical difference -129 is out of signed range. The unsigned comparison uses NOT C=0.

A misses signed overflow. B gives both comparisons correctly. C reverses both outcomes. D incorrectly treats the unsigned operands as signed.

**Common misconception:** A positive truncated subtraction result does not establish a signed ordering when overflow occurs.

### Q46

**Correct answer:** 3 (exact).  
**Concept:** Common subexpressions in the presence of possible aliasing.

The initial *p and *q must each be read: in the allowed case where the pointers differ, their original values are independent and both are returned. After *p=7, the old value b cannot always replace c: if p=q, the store changes *q to 7; otherwise *q retains its old value. Without the prohibited runtime pointer test, a third load is needed for c. No subsequent store occurs, so e=c. The store itself establishes d=7, even if p and q alias. Three loads therefore suffice and are necessary under the allowed transformations.

An equivalent sequence retains the loads for a,b,c and replaces d by 7 and e by c.

**Common misconception:** Syntactically identical loads are not common subexpressions across a potentially aliasing store; a load from the exact stored address can, however, use the stored value.

### Q47

**Correct answer:** A, B, D.  
**Concept:** Consensus terms and static-1 hazards.

When B=C=1, the ideal function is A+(NOT A)=1. Different delays can nevertheless turn off the previously active product before turning on the other, causing a static-1 hazard.

- A is true by the consensus theorem. Whenever BC=1, either A=1 and AB=1, or A=0 and (NOT A)C=1, so BC adds no new on-set input.
- B is true because the two A-dependent paths may switch at different times.
- C is false: ABC still depends on A. On a 1-to-0 change of A, its path can become 0 before the NOT A path becomes 1.
- D is true: BC remains 1 throughout a change of A and keeps the OR output asserted.

**Common misconception:** A logically redundant term removes the hazard only if it bridges the transition independently of the changing input.

### Q48

**Correct answer:** B.  
**Concept:** Serializability versus recoverability.

The only intertransaction conflict is w1(x) before r2(x), giving precedence edge T1->T2. The graph is acyclic, so the schedule is conflict-serializable. T2 reads T1's uncommitted write and then commits before T1. This violates recoverability, which requires the producer to commit before the dependent reader commits. It also violates cascadelessness, which would require c1 before r2(x).

A falsely claims recoverability. B is correct. C gets both properties wrong. D falsely claims cascadelessness.

**Common misconception:** An acyclic precedence graph does not by itself guarantee a safe commit order.

### Q49

**Correct answer:** 16 (exact).  
**Concept:** Sparse two-level page tables.

Each second-level table covers 1024 virtual page numbers. Directory indices are floor(VPN/1024): the four mapped pages use indices 0,0,1,1023. Thus three distinct second-level tables are needed, in addition to one directory. Four pages times 4 KiB per page gives 16 KiB.

**Common misconception:** Four mapped data pages need not require four second-level tables; shared high-order address bits determine table reuse.

### Q50

**Correct answer:** D.  
**Concept:** Prefix-free restriction of deterministic empty-stack acceptance.

The finite language L is regular, so a DFA recognizes it. A final-state DPDA can simulate that DFA without using its stack. A nondeterministic empty-stack PDA can choose whether to finish after a or to wait for b and then finish.

A deterministic empty-stack PDA accepting a has a unique computation on that prefix. On input ab it must follow the same computation until the prefix a has been consumed. If it then empties its stack through epsilon transitions, determinism prevents choosing a b-consuming alternative, and no transition can consume b after the stack is empty. Hence it cannot also accept ab. This is the prefix-free obstruction under the stated conventions.

A, B and C can recognize L by the constructions above. D cannot.

**Common misconception:** Final-state and empty-stack acceptance have equivalent power for nondeterministic PDAs, but not automatically for deterministic PDAs without an end marker.

### Q51

**Correct answer:** A, C.  
**Concept:** Closure properties of context-free languages.

L1 is generated by S->XC, X->aXb|epsilon, C->cC|epsilon. L2 is generated by S->AY, A->aA|epsilon, Y->bYc|epsilon. Both are context-free. Context-free languages are closed under union and concatenation, proving A and C.

Their intersection is exactly {a^n b^n c^n:n>=0}, which is not context-free. For a pumping-lemma argument, choose a^p b^p c^p. The bounded substring containing both pumped pieces cannot contain both an a and a c. Pumping changes at most two of the three symbol counts (or destroys block order), and at least one count changes, so equality of all three counts cannot persist. Thus B is false. Every regular language is context-free, so D is also false.

**Common misconception:** Closure under union does not imply closure under intersection.

### Q52

**Correct answer:** C.  
**Concept:** Counting heaps by independent subtrees.

The root must be 7. Choose the three keys for the left subtree in C(6,3)=20 ways; the others form the right subtree. Each three-node subtree must place its largest key at its root, while its other two keys may occupy its two child positions in 2 ways. Thus the total is 20*2*2=80.

A misses the two arrangements in one subtree. B does not account for selecting subtree key sets. C is correct. D overcounts arrangements that violate a subtree's root constraint.

**Common misconception:** A heap fixes ancestor-descendant inequalities but does not sort the entire array.

### Q53

**Correct answer:** C.  
**Concept:** Matrix powers count walks, including edge multiplicity.

The required count is trace(M^2). Starting at vertex 1, the route through vertex 2 contributes 2*1=2, and the route through vertex 3 contributes 1*0=0. Starting at 2 contributes 1*2+1*1=3. Starting at 3 contributes 0*1+1*1+1*1=2. The last contribution is traversal of the self-loop twice. Total 2+3+2=7.

A ignores multiplicities or starting-vertex distinctions. B drops the two walks arising from additional parallel-edge choices. C counts all seven walks. D has no corresponding set of additional legal closed walks.

**Common misconception:** A closed walk is not an undirected cycle; changing its starting vertex can produce another counted walk.

### Q55

**Correct answer:** A.  
**Concept:** Lock conversion and deadlock under strict locking.

Each upgrade needs an exclusive lock, which is incompatible with the other transaction's shared lock. Neither shared lock is released until commit, and neither transaction can progress to commit, so a deadlock is possible. Retaining exclusive locks until commit still prevents dirty reads by other properly locking transactions.

A correctly states both facts. B confuses compatibility of existing shared locks with compatibility of an exclusive upgrade. C is false: releasing the shared lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking. D is false: acquiring an exclusive lock before the read serializes the entire read-modify-write operation, preventing a lost update.

**Common misconception:** A serializability or recovery guarantee does not imply deadlock freedom.

### Q56

**Correct answer:** B.  
**Concept:** Changing a caller's pointer while retaining an alias to its old target.

In the first call, t points to a[0], and assigning *p=q changes the caller's p to a+1. The next statement makes a[0]=2+5=7, and the last makes a[1]=6. In the second call, t points to a[1], while the caller's p changes back to a. Therefore a[1]=6+7=13 and then a[0]=8. The final offset p-a is 0.

A omits the last increment of a[0]. B matches the trace. C fails to follow the second call's target changes. D is false: each side effect occurs in a separate full expression, all pointers stay within the valid array, and no incompatible-type access occurs.

**Common misconception:** Saving the pointer value in t preserves its old target even when a pointer-to-pointer argument changes the caller's p.

### Q57

**Correct answer:** C.  
**Concept:** Longest-match lexing and backup length.

After reading a, the lexer has an accepting position for token a, but ab*c is still possible. It must continue across all n b symbols because a subsequent c would make them part of the longer token. The following d rules out that longer token. No position after the first a was accepting for a token beginning there, so the lexer returns to the position after a. It has inspected n+1 characters beyond that accepting position. This amount is unbounded as n grows.

A and B propose fixed bounds disproved by large n. C is correct. D would violate longest match on inputs that end the prefix with c instead of d.

**Common misconception:** Recognition by a finite automaton does not guarantee a fixed bound on longest-match backup.

### Q58

**Correct answer:** A, B.  
**Concept:** Negative edges, settling order, and path-length transformations.

The three s-to-t paths are s-a-t of weight 4, s-b-t of weight 15, and s-b-a-t of weight 3. Thus A is true. Dijkstra first settles s, then a at distance 2, then t at distance 4, before b at distance 5 can improve a. Hence B is true for the stated algorithm.

C is false. Adding 4 per edge changes the three path weights to 12,23,15 respectively. The shortest path becomes s-a-t instead of s-b-a-t. D is false: the graph is acyclic, so it contains no directed cycle at all.

**Common misconception:** Adding a constant to every edge preserves ordering only among paths with the same number of edges.

### Q59

**Correct answer:** A, C.  
**Concept:** Epsilon productions in predictive and bottom-up parsers.

FIRST(aSbS)={a} and FOLLOW(S)={b,$}. Therefore the epsilon alternative occupies lookaheads b and $, while the other alternative occupies a. There is no LL(1) conflict, proving A and also establishing unambiguity, so B is false.

The LR(0) initial state contains S->.aSbS and S->. (the completed epsilon item). LR(0) would reduce by epsilon on every lookahead while also shifting a, causing a shift/reduce conflict; D is false. In the SLR construction, epsilon reductions occur only on FOLLOW(S)={b,$}. States where an S is expected have the same a-shift versus epsilon-reduce distinction; their reductions do not conflict. The state with S->aS.bS only shifts b, and the completed nonempty production occupies a separate state. Thus the SLR table is conflict-free and C is true.

**Common misconception:** An LR(0) conflict caused by an epsilon reduction may disappear when reductions are restricted by FOLLOW sets.

### Q60

**Correct answer:** A, B, D.  
**Concept:** Multi-level indexed file allocation.

Each indirect block holds 1024/4=256 pointers. The direct range is 0-3 and the single-indirect range is 4-259. The remaining logical blocks 260-262 require a double-indirect root and one lower-level indirect block. Together with the single-indirect block, this gives three allocated indirect blocks.

A is true by the count above. B is true: read the double-indirect root, its selected lower-level block, and the data block. C is false: 259 is the last single-indirect data block. D is true because 263*1024=269312 bytes.

**Common misconception:** Metadata-block allocation depends on the populated part of the pointer tree, not its maximum possible capacity.

### Q61

**Correct answer:** 2500 (exact).  
**Concept:** Simultaneous TCP flow and congestion limits.

The largest permitted outstanding amount is min(10000,6500)=6500 bytes. Since 4000 bytes are already outstanding relative to the same acknowledgement, another 6500-4000=2500 bytes may be sent. The congestion window alone would allow 6000 more, but the advertised receive window is tighter.

**Common misconception:** The advertised window bounds the total outstanding data from its acknowledgement point, not an additional allowance independent of already transmitted bytes.

### Q62

**Correct answer:** B.  
**Concept:** Universal decomposition quantifier in pumping-lemma proofs.

A permitted decomposition has |xy|<=p and |y|>=1, so k=|y| satisfies 1<=k<=p. Pumping y twice changes the length to p^2+k. It exceeds p^2 and is at most p^2+p, strictly less than p^2+2p+1=(p+1)^2. There is no square strictly between consecutive squares, so every permitted decomposition fails when pumped twice.

A wrongly requires k=p. B gives the necessary argument for every permitted decomposition. C treats a single bad decomposition as sufficient even though the pumping lemma promises only the existence of a good one. D is false: pumping down subtracts an arbitrary k between 1 and p, not necessarily 2p-1.

**Common misconception:** Refuting a pumping property requires defeating every allowed decomposition of the selected word.

### Q63

**Correct answer:** C.  
**Concept:** Prime-implicant covering with lexicographic cost.

Every pair of rows misses one column: P1P2 misses m6; P1P3 misses m5; P1P4 misses m4; P2P3 misses m3; P2P4 misses m2; P3P4 misses m1. Therefore at least three product terms are necessary. Every triple covers all columns. Their literal totals are 8 for P1P2P3, 9 for P1P2P4, 9 for P1P3P4 and 10 for P2P3P4. The unique preferred set is P1P2P3.

A is not a cover. B is a cover with nine literals. C is the minimum-literal three-term cover. D is a cover with ten literals.

**Common misconception:** A chart with no essential prime implicant can still have a unique optimum once literal costs are considered.

### Q64

**Correct answer:** B.  
**Concept:** Microcode sequencing around variable-latency memory.

The START pulse must be outside the wait loop. The loop must avoid repeating the register increment, and DATA must be sampled only after READY establishes completion. Routine B issues START once, waits in a control-only state, and executes the data transfer and increment exactly once afterward.

A repeats START and the increment during waiting. B satisfies all requirements. C starts only once but increments on each wait-loop visit. D does not wait and can sample invalid data if memory takes longer than the start cycle.

**Common misconception:** A control-state self-loop reexecutes that state's data-path operations every cycle.

### Q65

**Correct answer:** B.  
**Concept:** Tournament certificates for the second-smallest key.

The tournament uses 12 comparisons regardless of input: each comparison eliminates one of thirteen keys from minimum contention. If the eventual minimum occupies position 13, it gets byes in the first two rounds, then wins two comparisons. Only two keys lost directly to it, so one more comparison finds the second-smallest: 13 total.

Positions 1-8 participate in all four rounds. If the minimum is in one of these positions, four keys lose directly to it; finding the smallest among those four takes three additional comparisons, giving 15 total. Positions 9-12 have one bye and give an intermediate total of 14. Thus the extrema are (13,15).

A omits the final comparison even in the shortest winner path. B is correct. C overcounts both extrema. D assumes all leaves have the same depth despite byes.

**Common misconception:** With a non-power-of-two input size, the eventual minimum can meet different numbers of opponents.
