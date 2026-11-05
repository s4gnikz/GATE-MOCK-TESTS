# GATE CS — Additional Practice Set 002

**Questions:** 50  
**Maximum marks:** 71

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A triangular tile has labelled vertices P=(1,1), Q=(3,1), R=(1,2) in a Cartesian plane. First reflect the tile in the x-axis. Then rotate the result clockwise by 90 degrees about the origin. Which ordered triple gives the final positions of P, Q and R?

A. ((-1,-1),(-1,-3),(-2,-1))  
B. ((1,1),(1,3),(2,1))  
C. ((1,-1),(1,-3),(2,-1))  
D. ((-1,1),(-1,3),(-2,1))  

### Q2. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A is a real 3x3 matrix with distinct eigenvalues 1, 2 and 4. Let u be a nonzero column vector satisfying Au=2u, and let v be a real column vector satisfying v^T u=-2. Define B=A+u v^T. Which statements hold for every such A,u,v?

A. Zero is an eigenvalue of B.  
B. B is diagonalizable over the real numbers.  
C. A and B necessarily commute.  
D. rank(B)=2.  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The reviewer gave the proposal a “qualified endorsement”: she supported its objective but required a smaller pilot before implementation. In this context, “qualified” most nearly means:

A. supported without any reservations  
B. conditional on stated reservations  
C. written by a certified professional  
D. withdrawn after reconsideration  

### Q4. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A sorted data file has fixed-length records, with exactly eight records per data page and no unused slots. A range query matches exactly 16 consecutive records in file order. An index lookup requires exactly two page reads and identifies the first matching record's page and slot. Index pages are separate from data pages, no page is initially cached, and scanning the range reads each needed data page once. What is the largest possible total number of page reads, over the possible starting slots?

A. 3  
B. 4  
C. 5  
D. 6  

### Q5. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={a^(n^2) : n is a nonnegative integer}. A proof assumes that L is regular, takes a pumping length p>=1, and chooses w=a^(p^2). Which continuation correctly contradicts the regular-language pumping lemma?

A. In every permitted decomposition w=xyz, y must have length p; pumping twice gives a length outside L.  
B. In every permitted decomposition w=xyz, 1<=|y|<=p; pumping twice gives a length strictly between p^2 and (p+1)^2.  
C. It suffices to choose one permitted decomposition with |y|=1 and show that pumping it twice leaves L.  
D. Pumping down always gives the immediately preceding square length (p-1)^2, which contradicts regularity.  

### Q6. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A synchronous two-bit machine updates (q1,q0) to (q0,q1 XOR q0) on each clock edge. Its reset state is 01. Which statements are correct?

**Candidates**

**I.** The reset trajectory has period 3.

**II.** State 00 is reached after three edges from reset.

**III.** State 10 is reached after two edges from reset.

**IV.** q1 and q0 are complements throughout the reset trajectory.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n a power of two, consider the following routine. Each work() and every arithmetic or control operation takes constant time. What is its asymptotic running time?

```text
F(n):
    if n <= 1: return
    F(n/2)
    F(n/2)
    for i = 1 to n:
        for j = 1 to i:
            k = 1
            while k <= i:
                work()
                k = 2*k
```

A. Θ(n log n)  
B. Θ(n²)  
C. Θ(n² log n)  
D. Θ(n² (log n)²)  

### Q8. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

a0=0, a1=1 and a_n=3a_(n−1)−2a_(n−2) for n≥2. Which formal generating function equals Σ_(n≥0) a_n x^n?

A. 1/(1−3x+2x²)  
B. x/(1−3x−2x²)  
C. (1−x)/(1−2x)  
D. x/((1−x)(1−2x))  

### Q9. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Exactly one of three boxes A,B,C contains a prize. Their labels say, respectively, “The prize is in B,” “The prize is in C,” and “The prize is not in C.” Exactly one label is true. Which statements follow?

**Candidates**

**I.** The prize may be in A.

**II.** The prize must be in C.

**III.** The prize cannot be in B.

**IV.** The label on A must be true.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q10. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider a CFG with start S and productions S→AB | C, A→aA | a, B→bB, C→cC | ε, D→d. A useful nonterminal must occur in some derivation from S that ends in a terminal string. Which statements are correct?

**Candidates**

**I.** The generated language is c*.

**II.** A is useful because it is reachable from S and generates terminal strings.

**III.** Exactly two nonterminals are useful.

**IV.** D is useful because it generates d.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q11. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A bottom-up parser for E→E+T | T and T→id has already reduced the first id in `id+id` to E and shifted `+ id`. Its stack, ignoring states and the bottom marker, is `E + id`; the lookahead is end-of-input. What is the next reduction in the successful reverse-rightmost derivation?

A. E→E+T, reducing the entire stack immediately.  
B. T→id, reducing only the final id.  
C. E→T, reducing the initial E.  
D. No reduction is possible because the input is exhausted.  

### Q12. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be any language over a finite alphabet. Define Pref(L)={x:xy∈L for some string y}. Which statements are correct?

A. If L is regular, Pref(L) is regular.  
B. If L is recognizable, Pref(L) is recognizable.  
C. If Pref(L) is regular, L must be regular.  
D. If L is nonempty, ε belongs to Pref(L).  

### Q13. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The input sequence 1,2,3,4,5 is passed through one stack. Each input may be pushed only in this order; a pop emits the current top. Which output permutations are possible?

**Candidates**

**I.** 3,2,1,5,4

**II.** 3,1,2,4,5

**III.** 2,4,3,5,1

**IV.** 4,2,3,1,5

A. II and IV  
B. III and IV  
C. I and III  
D. I and II  

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The grammar S→aSb | ε is used by a predictive parser. On valid input aabb, what is the maximum number of unconsumed b terminals simultaneously present on its stack, excluding input and the end marker?

A. 1  
B. 2  
C. 3  
D. 4  

### Q15. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A and B are real 4×4 matrices, each of rank 3. Which statements are correct?

A. rank(AB) is at least 2.  
B. rank(AB) can be 3.  
C. rank(AB) can be 1.  
D. rank(AB) can be 2.  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relations R(A,B) and S(B,C) each contain 100 tuples. B is a key of S, and every R.B value references an existing S.B value. No additional constraints are given. Under set semantics, how many tuples must R⋈S contain?

A. 0  
B. 100  
C. 10,000  
D. It cannot be determined even under these constraints.  

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A B+ tree leaf stores at most four keys. An insertion gives the sorted leaf [4,7,9,12,15]. The split rule keeps the first three keys in the left leaf and the final two in the right leaf; it copies the smallest key in the right leaf into the parent. Which key is copied?

A. 9  
B. 12  
C. 7  
D. 15  

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What is the smallest single CIDR block containing both 10.0.4.0/24 and 10.0.5.0/24, without covering any additional /24 block? Use canonical network-address notation with all host bits zero.

A. 10.0.4.0/23  
B. 10.0.4.0/22  
C. 10.0.5.0/23  
D. 10.0.0.0/21  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sentence unambiguously states that Meera checked the figures before submitting the report?

A. Before submitting the report, the figures were checked by Meera.  
B. Before Meera submitted the report, she checked the figures.  
C. The figures submitted the report after Meera checked them.  
D. Having been submitted, Meera checked the report's figures.  

### Q20. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary tree has distinct labels. Its preorder is A,B,D,E,C,F and its inorder is D,B,E,A,C,F. Which postorder is correct?

A. D,E,B,F,C,A  
B. D,B,E,F,C,A  
C. E,D,B,C,F,A  
D. D,E,F,B,C,A  

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed graph has a negative-weight cycle that is unreachable from source s. Which statement about source-reachable shortest paths follows?

A. Every source-reachable distance is necessarily undefined.  
B. The unreachable cycle alone does not destroy shortest-path distances from s.  
C. The cycle must be removed before even identifying vertices reachable from s.  
D. All edge weights reachable from s must therefore be nonnegative.  

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A segmented address has segment number 2 and offset 120. Segment 2 has base 4000 and limit 100, where valid offsets are 0 through limit−1. What is the correct outcome of translation?

A. Physical address 4120.  
B. Physical address 4100.  
C. An address-bound violation.  
D. Physical address 120.  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A screening procedure flags an item whenever its measured value exceeds a threshold. Raising that threshold while leaving all measurements unchanged can have which effect on the set of flagged items?

A. It can only stay the same or become a subset of its former set.  
B. It must strictly increase.  
C. Every formerly unflagged item must become flagged.  
D. It must become empty regardless of the measurements.  

### Q24. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider languages over {0,1}. Which statements are true?

**Candidates**

**I.** {wwᴿ : w∈{0,1}*} is context-free.

**II.** {ww : w∈{0,1}*} is context-free.

**III.** Restricting {ww : w∈{0,1}*} to the unary alphabet {0} gives a regular language.

**IV.** Every context-free language is closed under intersection with every other context-free language.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A transfer transaction subtracts from one account but crashes before adding to the other. Recovery leaves the subtraction permanent while undoing no part and completing no addition. Which transaction property is directly broken?

A. Atomicity.  
B. A requirement that all transactions be read-only.  
C. A requirement that every table contain one row.  
D. No property because part of the transaction succeeded.  

### Q26. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For grammar S→aA | aB, A→b, B→c, which statements are true?

**Candidates**

**I.** The two S alternatives conflict in an LL(1) predictive table.

**II.** The generated language is inherently ambiguous.

**III.** Replacing the grammar by S→aX, X→b | c gives an LL(1) grammar for the same language.

**IV.** No deterministic parser can recognize the generated language.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q27. [2 Marks] [MCQ]

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

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider L={aⁿbᵐ:n,m≥0 and n≠m}. For an arbitrary positive proposed regular pumping length p, choose w=aᵖb^(p+p!). Every valid split w=xyz with |xy|≤p and |y|>0 has y=aᵏ for some 1≤k≤p. Which pumping exponent i makes xy^i z have equal a and b counts and therefore leave L?

A. i=p!  
B. i=1+p!/k  
C. i=1−p!/k  
D. i=k+1  

### Q29. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Procedure P makes a call as its final action, passing the address of a local variable x to callee Q. Q dereferences that address during the call. Which statements about optimizing this call are correct?

**Candidates**

**I.** P's frame may always be discarded and overwritten before Q reads x, solely because the call is in tail position.

**II.** Any transformation must preserve the addressed object's value and valid storage for Q's use.

**III.** Q cannot observe x because callees never receive pointers to caller variables.

**IV.** Tail position alone is insufficient to justify overwriting all storage in P's frame.

A. III and IV  
B. I and II  
C. II and IV  
D. I and III  

### Q30. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A library reports: “After online reservations began, the fraction of issued books returned late fell. However, the number of late returns increased because the number of issued books rose substantially. The figures do not identify what would have happened without online reservations.” Which interpretation is justified?

A. Online reservations caused every borrower to return books sooner.  
B. A lower late-return fraction is incompatible with more late returns.  
C. The number of timely returns must have fallen.  
D. A larger borrowing volume can coexist with a lower late-return fraction and more late returns, without establishing a causal effect.  

### Q31. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let S be the set of encodings of Turing machines whose recognized language contains the string00. Which statements are correct?

**Candidates**

**I.** S is recognizable by simulating the encoded machine on00.

**II.** S is decidable because the input string00 has fixed finite length.

**III.** S is a nontrivial semantic property of recognized languages.

**IV.** Both S and its complement are recognizable.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q32. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A table has two rows with distinct primary keys1 and2 and a UNIQUE non-null code column initially containing A and B respectively. A transaction first updates row1's code to B and then row2's code to A. No other transaction runs. Which statement correctly distinguishes immediate checking from checking the UNIQUE constraint only at transaction commit?

A. Both modes must accept because the final state is unique.  
B. Immediate checking rejects the first update; commit-only checking can accept the final swapped state.  
C. Commit-only checking must reject because any intermediate duplicate is forbidden in that mode.  
D. Both modes necessarily change the primary keys.  

### Q33. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over a nonempty domain, consider propositions F=(for every x, P(x) OR Q(x)) and G=((for every x, P(x)) OR (for every x, Q(x))). Which statements are correct?

A. G implies F.  
B. F implies G in every interpretation.  
C. A two-element domain can make F true and G false.  
D. F and G are equivalent when the domain has one element.  

### Q34. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A researcher writes: “No failure was observed in a hundred trials. This excludes failure in those trials but does not establish that failure is impossible.” Which additional claim conflicts with that qualification?

A. The observed failure count was zero.  
B. The tested system may still fail in an untested situation.  
C. Future observations could require revising the assessment.  
D. A future failure is logically impossible solely because of these trials.  

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A narrative contains: “Mira mailed the parcel after weighing it. She obtained the address before mailing it, but the text does not specify whether she obtained the address before or after weighing.” Which order is inconsistent with this account?

A. Obtain address, weigh, mail.  
B. Weigh, obtain address, mail.  
C. Weigh, mail, obtain address.  
D. Both A and B are possible.  

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider replacing x*2 by x+x in an integer intermediate representation. Which statements are correct?

A. For unbounded mathematical integers the two expressions are equal.  
B. For arithmetic modulo2^w the two results are equal for every w-bit x.  
C. This equivalence alone proves that replacing any signed C expression involving multiplication can ignore its language's overflow rules.  
D. The replacement's profitability can depend on the target machine, even when semantic equivalence holds.  

### Q37. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer uses longest match among tokens '<','<=','<<','=' and identifiers. Which statements about input x<<=y are correct?

A. After identifier x, the next token is'<<'.  
B. The next token after'<<' is'='.  
C. The lexer must invent a'<<=' token because three symbols are adjacent.  
D. Choosing'<' first would violate longest match among the stated tokens.  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An algorithm receives a Turing machine M and a nonnegative integer k written in binary. It asks whether M, started on blank input, halts within k steps. Which statements are correct?

**Candidates**

**I.** This bounded question is decidable by direct simulation.

**II.** A potentially enormous value of k makes the problem undecidable.

**III.** The same simulation strategy decides eventual halting without any bound by choosing one universally sufficient finite k.

**IV.** Binary encoding can make the simulation duration much larger than the length of k's representation.

A. II and IV  
B. III and IV  
C. I and II  
D. I and IV  

### Q39. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

P holds a single-instance resource R and waits for S. Q holds the single instance of S but is running and will release it without requesting another resource. No other processes or requests exist. Which statement is justified?

A. P and Q are already deadlocked because P waits.  
B. A circular wait exists through R and S.  
C. Q must be waiting for R implicitly.  
D. The stated resource situation does not form a deadlock.  

### Q40. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A0/1 knapsack of capacity4 has just one item, of weight2 and value3. An implementation initializes dp[0..4] to0 and processes this item as follows:

```text
for w = 2 to 4, in increasing order:
    dp[w] = max(dp[w], dp[w-2] + 3)
```

Which statements are correct?

**Candidates**

**I.** The loop returns the correct0/1 optimum at dp[4].

**II.** It sets dp[4] to6 by effectively reusing the item.

**III.** Iterating w from4 down to2 instead avoids this reuse.

**IV.** Every dp[w-2] read in this loop is necessarily from before processing the item.

A. I and II  
B. II and III  
C. I and III  
D. I and IV  

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a directed weighted graph, a negative-weight cycle is reachable from s but no vertex on that cycle can reach t. A path from s to t exists. Which statements are correct?

**Candidates**

**I.** A finite shortest s-to-t distance can still exist.

**II.** Every reachable vertex necessarily has distance minus infinity.

**III.** Repeating that cycle cannot produce arbitrarily cheap s-to-t walks under the stated reachability condition.

**IV.** The mere existence of that cycle implies no s-to-t path exists.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q42. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic Turing machine on a fixed input is forbidden to visit more than100 tape cells. Its finite state set and tape alphabet are known. Which statements are correct?

**Candidates**

**I.** Whether it halts can be decided by simulating until halting or a repeated complete configuration.

**II.** Every such machine must halt.

**III.** Only finitely many complete configurations are possible on that input.

**IV.** This establishes decidability of unrestricted Turing-machine halting.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q43. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a statement P(n) about integers n≥2, a proof establishes P(2) and P(k) implies P(k+2) for every integer k≥2. Which conclusions follow?

**Candidates**

**I.** P(n) holds for every even integer n≥2.

**II.** These facts alone prove P(3).

**III.** Adding a proof of P(3) would establish P(n) for every integer n≥2.

**IV.** The step from k to k+2 supplies the missing odd base case automatically.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A fractional knapsack has capacity5 and two available items, each of weight4 and value8. Any real fraction between0 and1 of each item may be selected. Which statements are correct?

**Candidates**

**I.** Selecting weight2.5 from each item is optimal.

**II.** Every optimal solution must have at most one partially selected item.

**III.** An optimal solution with one whole item and one partially selected item exists.

**IV.** The optimal allocation is unique.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q45. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be a context-free language over {a,b}. Define h(a)=01 and h(b)=epsilon. Let R be a regular language over {0,1}. Which languages must be context-free?

A. h(L)  
B. h(L) intersect R  
C. The complement of L over {a,b}*  
D. L intersect {a}*  

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A point is first reflected across y=x, then translated by (2,−1). Which point maps to (5,3)?

A. (3,4)  
B. (4,3)  
C. (6,1)  
D. (1,6)  

### Q47. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that most clearly expresses both stated facts without a misplaced modifier: the researcher analyzed the samples, and the samples—not the researcher—had been stored overnight.

A. Stored overnight, the researcher analyzed the samples.  
B. The researcher analyzed the samples that had been stored overnight.  
C. Analyzing the researcher, the samples had been stored overnight.  
D. The researcher, which had been stored overnight, analyzed the samples.  

### Q48. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“Complaints about bus delays fell after an online complaint form was introduced. During the same period, submitting a complaint began to require an account, and the number of completed complaint submissions fell. No independent measurements of bus arrival times were collected.” Which conclusion is best supported?

A. Buses necessarily became more punctual.  
B. Every person who stopped submitting complaints encountered punctual buses.  
C. The complaint count alone cannot distinguish improved punctuality from reduced reporting.  
D. Requiring an account necessarily made buses less punctual.  

### Q49. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler analyzes the loop below using a non-relational constant lattice, meeting different constants as “nonconstant.” It does not unroll the loop or track relationships between variables. Input n is an arbitrary nonnegative integer.

```text
x=0; y=0;
repeat n times:
    x=x+1;
    y=y+1;
z=x-y;
```

Which statements hold?

**Candidates**

**I.** Concrete execution always sets z=0.

**II.** The stated abstraction necessarily retains x=y at the loop exit.

**III.** Joining the entry values with the first-iteration values makes both x and y nonconstant.

**IV.** The program can set z=1 for some nonnegative n.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q50. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An insertion-sort implementation shifts a preceding element only when it is strictly greater than the key being inserted. Records have a sorting key and a distinct label. Which statements are correct?

**Candidates**

**I.** Equal-key records retain their initial relative order.

**II.** Replacing the strict comparison by “greater than or equal” still guarantees stability.

**III.** On an already sorted array, no record is shifted by the inner loop.

**IV.** On every input, the number of shifts equals the number of adjacent equal-key pairs.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

---

## ANSWER KEY — SET 002

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | MCQ | 2 | C |
| 3 | MSQ | 1 | A, C, D |
| 4 | MSQ | 1 | A, B, D |
| 5 | MSQ | 2 | A, C, D |
| 6 | MCQ | 1 | D |
| 7 | MSQ | 2 | A, B, D |
| 8 | MSQ | 1 | A, B, C |
| 9 | MCQ | 1 | C |
| 10 | MCQ | 2 | D |
| 11 | MSQ | 1 | A, C, D |
| 12 | MCQ | 2 | C |
| 13 | MCQ | 2 | C |
| 14 | MSQ | 1 | A, C, D |
| 15 | MCQ | 2 | C |
| 16 | MSQ | 2 | A, C, D |
| 17 | MSQ | 1 | A, C, D |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 1 | A, C, D |
| 20 | MSQ | 2 | B, C, D |
| 21 | MSQ | 1 | A, C, D |
| 22 | MSQ | 1 | A, B, D |
| 23 | MSQ | 1 | B, C, D |
| 24 | MCQ | 2 | B |
| 25 | MSQ | 1 | B, C, D |
| 26 | MCQ | 1 | D |
| 27 | MCQ | 2 | A |
| 28 | MSQ | 1 | A, C, D |
| 29 | MCQ | 1 | C |
| 30 | MSQ | 2 | A, B, C |
| 31 | MCQ | 2 | A |
| 32 | MSQ | 2 | A, C, D |
| 33 | MCQ | 1 | B |
| 34 | MSQ | 2 | A, B, C |
| 35 | MSQ | 1 | A, B, D |
| 36 | MCQ | 2 | C |
| 37 | MCQ | 2 | C |
| 38 | MCQ | 2 | D |
| 39 | MSQ | 1 | A, B, C |
| 40 | MCQ | 1 | B |
| 41 | MCQ | 1 | C |
| 42 | MCQ | 1 | D |
| 43 | MCQ | 1 | A |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 1 | C |
| 46 | MSQ | 1 | A, C, D |
| 47 | MSQ | 2 | A, C, D |
| 48 | MSQ | 1 | A, B, D |
| 49 | MCQ | 2 | C |
| 50 | MCQ | 1 | D |
