"""One-time authored content serialization; not a template question generator."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
slots={s['number']:s for s in json.loads((ROOT/'blueprints/papers.json').read_text(encoding='utf-8'))[1]['slots']}
questions=[]
def add(n,typ,difficulty,stem,options,answer,solution,why,misconception,family,pattern,steps=2):
    s=slots[n]
    questions.append(dict(id=f'CS27-M002-Q{n:03}',paper=2,number=n,subject=s['subject'],subtopic=s['subtopic'],type=typ,marks=1,difficulty=difficulty,stem=stem,options=options,answer=answer,nat={'min':answer,'max':answer,'precision':0} if typ=='NAT' else None,solution=solution,option_explanations=why,misconception=misconception,family=family,reasoning_pattern=pattern,structure_signature=family+':'+pattern,reasoning_steps=steps,references=['research/SYLLABUS_2027.md'],verification={'status':'REVIEW_REQUIRED','method':'author derivation; independent review pending','independent_solution':'','evidence':''},validation_status='REVIEW_REQUIRED',assets=[]))

add(11,'NAT','Medium',
"A cache has two sets, two lines per set, and uses least-recently-used replacement within each set. Memory block b maps to set b mod 2. The cache is initially empty. The processor reads blocks 0, 2, 0, 4, 2 in that order. Every miss loads the requested block. How many cache misses occur?",[],4,
"All references map to set0. References0 and2 miss and fill both lines. The next0 hits and makes2 least recently used. Reading4 misses and evicts2. The final2 therefore misses, evicting0. There are four misses; set1 is unused.",[],
"Total cache capacity does not prevent conflicts when blocks map to one set.",'cache-set-local-lru-reuse-distance','map-conflicting-blocks;update-recency;count-misses')

add(12,'MCQ','Medium-Hard',
"A rooted binary tree has five distinct node labels. Its preorder traversal is A,B,C,D,E and its postorder traversal is C,B,E,D,A. Left and right child positions are distinguished. How many different binary trees have both of these traversals?",
['1','2','4','8'],['C'],
"A is the root. Its first subtree must contain B,C because B closes at the second postorder position; its other subtree contains D,E. Thus A has two children, B and D. B has only child C and D has only child E. Either only child may independently be placed left or right, giving2*2=4 trees.",
['False: traversals do not specify which side holds an only child.','False: there are two independent only-child choices, not one.','True: two independent left/right choices give four.','False: A must have two children; it does not contribute a third binary choice.'],
"Preorder and postorder can fix subtree membership without fixing the side of an only child.",'binary-traversal-unary-child-orientation-count','partition-by-subtree-postorder-close;count-unary-orientations')

add(13,'NAT','Medium',
"A merge-sort call has already sorted its left half as [2,6,9] and its right half as [1,4,8]. The original positions of every left-half element precede every right-half element. A cross inversion is a pair consisting of a left-half value and a smaller right-half value. How many cross inversions must this merge count?",[],6,
"For left value2, only1 is smaller. For6, both1 and4 are smaller. For9, all1,4,8 are smaller. The total is1+2+3=6. There are no within-half inversions after sorting, but the question asks only the cross pairs.",[],
"Counting comparisons during merging is different from counting cross inversions.",'merge-cross-inversion-prefix-count','count-smaller-right-values-per-left-element')

add(14,'MCQ','Medium',
"A processor has a write-back data cache with no hardware coherence with DMA. It modifies a buffer, leaving the buffer's cache lines dirty, and then asks a DMA controller to copy that buffer from main memory to a device. The processor will not modify the buffer again during the transfer. Which action before starting DMA ensures that the device receives the updated data?",
['Invalidate the dirty lines without writing them back.','Write back all dirty buffer lines and wait for completion.','Disable device-completion interrupts.','Wait for a DMA-completion interrupt before starting the DMA transfer.'],['B'],
"DMA reads main memory rather than the processor's dirty cache copies. Writing back the buffer lines and waiting makes main memory contain the updates before DMA reads them. Discarding dirty lines loses modifications. Interrupt control changes notification, not visibility of cached data, and a completion event cannot precede starting the transfer.",
['False: discarding dirty lines without write-back loses the updated data.','True: completed write-back makes the DMA source in main memory current.','False: interrupt masking does not update memory.','False: this ordering cannot start the required transfer and does not flush the cache.'],
"DMA bypassing the CPU does not automatically observe its dirty cache contents.",'dma-device-read-dirty-cache-publication','identify-dma-source;order-cache-clean-before-transfer')

add(15,'MCQ','Medium',
"A depth-first search of a directed graph records discovery and finish times. Vertex u has interval [2,9] and vertex v has interval [4,7]. The graph contains an edge v→u. Which conclusion is necessarily correct?",
['The edge v→u is a tree edge.','The graph contains a directed cycle.','The edge v→u must be a cross edge.','The graph must be acyclic because the intervals are nested.'],['B'],
"Nested intervals show that u is a proper ancestor of v in the DFS forest. The tree path from u to v consists of directed edges. Adding v→u closes a directed cycle; v→u is a back edge. Thus only B follows.",
['False: a tree edge runs from an ancestor to a newly discovered descendant, not back to an ancestor.','True: the tree path u to v together with v→u is a directed cycle.','False: the nested intervals identify an ancestor relationship, not separate branches.','False: this return edge closes a cycle.'],
"Nested DFS intervals alone do not imply acyclicity; edge direction matters.",'dfs-interval-ancestor-return-edge-cycle','infer-ancestry;combine-tree-path-with-return-edge')

add(16,'MSQ','Medium',
"A binary search tree stores distinct keys. A node x has both a left and a right child. Its inorder successor s is used when deleting x. Which statements about s in the tree before deletion are necessarily true?",
['s is in the right subtree of x.','s must be a leaf.','s has no left child.','s may have a right child.'],['A','C','D'],
"With a nonempty right subtree, the successor is its minimum-key node, found by following left-child links from x's right child. It therefore lies in that subtree and has no left child. It can have a right child: for root10 with children5,15 and node15 having right child20, the successor of10 is15. Hence A,C,D hold and B fails.",
['True: successor is the minimum of the nonempty right subtree.','False: the minimum node can have a right child.','True: a left child would have a smaller key in that same subtree.','True: a right child does not violate minimality in the right subtree.'],
"The successor's lack of a left child does not make it necessarily a leaf.",'bst-successor-deletion-child-structure','locate-subtree-minimum;distinguish-leaf-from-no-left-child')

add(17,'NAT','Medium-Hard',
"An epsilon-NFA has states 0,1,2,3, initial state0, and these transitions; unlisted transitions have empty target sets.\n```text\n0 --a--> 0,1\n1 --epsilon--> 2\n2 --b--> 3\n3 --epsilon--> 1\n```\nAfter consuming the entire input aab, take epsilon closure. How many states are in the resulting active-state set?",[],3,
"Initially the closure is{0}. After the first a it is{0,1,2}; after the second a, only0 has an a transition, again giving closure{0,1,2}. On b only2 moves, producing{3}. Its epsilon closure adds1 and then2, so the final set is{1,2,3}, size3.",[],
"Epsilon closure must be recomputed after the last input symbol, including chains of epsilon edges.",'epsilon-nfa-last-symbol-transitive-closure','propagate-set;follow-post-input-epsilon-chain',3)

add(18,'MCQ','Medium-Hard',
"The following basic block uses exact mathematical integers and ordinary scalar variables, with no aliases or externally visible intermediate states. All three final variable values must be preserved. Which replacement is equivalent for every initial value of b and c?\n```text\na = b + c\nb = a - c\nc = a - b\n```",
['a = b + c','a = b + c; b = c','a = b + c; c = a','a = b + c; b = a; c = 0'],['A'],
"Write initial values b0,c0. The first statement sets a=b0+c0. The second sets b=(b0+c0)-c0=b0. The third reads this restored b and sets c=(b0+c0)-b0=c0. Thus b and c end unchanged, and only a=b+c is required.",
['True: a becomes the sum and b,c retain their original values.','False: it changes b whenever b0 differs from c0.','False: it changes c to b0+c0 rather than preserving c0.','False: it generally changes both b and c.'],
"Algebraic simplification must track which version of each variable an expression uses.",'basic-block-symbolic-restoration-eliminates-writes','substitute-definition-versions;compare-final-state',3)

add(19,'MCQ','Medium-Hard',
"For the grammar S→aS | Sb | ab, which listed string has two distinct ordered parse trees? Only finite parse trees are counted.",
['ab','aab','abb','aabb'],['D'],
"The base production generates ab. To generate aabb one must add one leading a and one trailing b; choosing aS at the root and then Sb, or Sb at the root and then aS, gives distinct trees with the same yield. The other strings require zero or only one extra production and therefore have unique trees.",
['False: only the base production generates this length-two string.','False: the sole extra a must come from one aS production.','False: the sole extra b must come from one Sb production.','True: the leading-a and trailing-b productions can nest in either order.'],
"Ambiguity concerns distinct parse trees, not merely multiple derivation orders for one tree.",'grammar-independent-prefix-suffix-production-ambiguity','identify-required-productions;permute-nesting')

add(20,'NAT','Medium-Hard',
"Routers A,B,C use synchronous distance-vector updates for destination C. Link costs are A–B=1, B–C=1 and A–C=10. Initially routes are converged. Link B–C fails immediately before round1. In every round each router recomputes its distance using its still-working links and the neighbours' distances from the end of the preceding round; C always advertises0. No split horizon, poison reverse or triggered intermediate updates are used. What distance does A advertise after round2?",[],4,
"Initially dA=2 and dB=1. In round1 B loses its direct link and uses A's previous2, giving3. A still uses B's previous1 and remains2. In round2 A uses B's3 and obtains min(10,1+3)=4. B uses A's previous2 and remains3. The requested advertised metric is4, not the true surviving shortest-path distance10.",[],
"Synchronous distance vectors use previous-round advertisements, which can retain routes through the failed link.",'distance-vector-synchronous-failure-feedback','apply-old-advertisements;distinguish-metric-from-real-route',3)

add(21,'MSQ','Medium',
"A binary floating-point system retains three significant binary digits, including the leading1. Exponents are unbounded, and every result is rounded to nearest, ties to even. Which statements are correct?",
['The exact value 1.125 rounds to 1.0.','Consecutive representable numbers in [2,4) are separated by 0.25.','Adding represented values 1.75 and 0.25 yields exactly 2.0.','Every integer from 0 through 9 is represented exactly.'],['A','C'],
"Near1 the spacing is1/4, so1.125 is halfway between1.00(binary) and1.01(binary); the even last significand bit selects1.0. In[2,4), spacing doubles to1/2. The sum1.75+0.25=2 is exactly representable. At[8,16), spacing is2, so9 is not representable. A,C hold.",
['True: it is a midpoint and ties-to-even chooses significand1.00.','False: the spacing in this exponent binade is0.5.','True: both inputs and the exact sum are representable.','False:9 lies between consecutive representable values8 and10.'],
"Floating-point spacing depends on the exponent, and midpoint rounding depends on the retained low bit.",'floating-binade-spacing-and-midpoint-parity','scale-significand-unit;apply-tie-even-and-exact-sum')

add(23,'MSQ','Medium-Hard',
"Consider this program with exact integers and an arbitrary Boolean input flag. A conventional nonrelational constant-propagation analysis tracks, for each variable separately, either a single constant or 'not constant'; at a join, distinct incoming constants become 'not constant'.\n```text\nif flag:\n    x = 2; y = 3\nelse:\n    x = 3; y = 2\nz = x + y\n```\nWhich statements are correct?",
['Every execution assigns5 to z.','The stated analysis finds x constant at the join.','The stated analysis necessarily infers z=5 directly from the joined abstract values of x and y.','Moving the assignment z=x+y into the end of each branch allows the stated analysis to find z=5 after the join.'],['A','D'],
"Both concrete paths give x+y=5, proving A. At the join, x has values2 or3 and y has3 or2; each independently becomes not constant. This abstraction loses the relation x+y=5 and cannot evaluate the sum as a constant there. Evaluating within each branch first produces the same constant5 for z on both incoming paths, which survives the join. Thus D holds, B,C do not.",
['True: the two concrete branch sums both equal5.','False: x differs between the incoming paths.','False: independent unknown values do not retain their correlation.','True: equal incoming constants for z survive the join.'],
"A property true on every path may be lost by an abstraction that forgets correlations.",'nonrelational-constant-join-loses-sum-correlation','contrast-concrete-path-invariant-with-abstract-join',3)

add(25,'MCQ','Medium',
"For the following straight-line code, a variable is live at a point if its current value may be read later before being overwritten. There are no implicit uses after return. Which set is exactly the set of live variables immediately before the statement x=0?\n```text\nx = a + b\ny = x + c\nx = 0\nreturn y\n```",
['{y}','{x,y}','{c,y}','{a,b,c,y}'],['A'],
"Working backward, return reads y, so y is live before x=0. That assignment defines x but reads no variables; it neither uses x's old value nor changes y. No later statement reads a,b,c. Hence only y is live at the specified point.",
['True: y alone is read later before any redefinition.','False: the old x is overwritten and never used later.','False: c was needed earlier, not after this point.','False: a,b,c have no remaining uses.'],
"Past participation in a computation does not make a variable live now.",'liveness-dead-overwrite-after-last-use','backward-use-def-transfer-at-selected-point')

add(26,'MCQ','Medium',
"Let F(x,y,z)=x XOR (y AND z). Define D(x,y,z)=F(x,y,z) XOR F(x,NOT y,z). Which expression equals D for every Boolean input?",
['x','y','z','NOT z'],['C'],
"The two occurrences of x cancel under XOR. If z=0, both AND terms are0 and D=0. If z=1, their values are y and NOT y, whose XOR is1. Thus D=z independently of x and y.",
['False: when x=0,z=1 the result is1.','False: when y=0,z=1 the result is1.','True: flipping y affects F exactly when z=1.','False: z=0 yields D=0, not1.'],
"A Boolean input's influence may be gated by another variable even when the output also contains XOR.",'boolean-difference-gated-input-influence','cancel-common-xor-term;case-split-gating-variable')

add(27,'NAT','Medium-Hard',
"Three processes have (arrival time, CPU burst length) A=(0,7), B=(2,4), C=(4,1), in time units. A single CPU uses preemptive shortest-remaining-time-first scheduling with zero switching overhead. No process performs I/O. Waiting time is completion time minus arrival time minus burst length. What is the average waiting time?",[],2,
"A runs0–2, leaving5. B arrives with4 and runs2–4, leaving2. C runs4–5 and completes; B resumes5–7 and completes; A runs7–12. Waiting times are A:12-0-7=5, B:7-2-4=1, C:5-4-1=0. Average=(5+1+0)/3=2.",[],
"Preemption compares remaining time, and waiting time includes intervals after preemption.",'srtf-nested-preemptions-waiting-time','simulate-arrival-boundaries;recover-waits-from-completions',3)

add(28,'MCQ','Medium-Hard',
"Relation R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which is its highest normal form among the choices below? Assume atomic attribute values.",
['1NF but not2NF','2NF but not3NF','3NF but not BCNF','BCNF'],['C'],
"Neither A nor B determines C, so candidate keys are AC and BC. Every attribute is prime because each occurs in a candidate key. Each nontrivial dependency has a prime right-side attribute, satisfying3NF. A→B violates BCNF since A is not a superkey, and similarly for B→A. Thus3NF but notBCNF.",
['False: every attribute is prime, so there is no nonprime partial dependency violating2NF.','False: prime right-side attributes satisfy3NF.','True:3NF holds while A and B are non-superkey determinants.','False: A→B is nontrivial and A does not determine C.'],
"Third normal form allows a prime dependent attribute even when the determinant is not a superkey.",'normal-form-all-prime-with-nonsuperkey-determinants','derive-two-composite-keys;contrast-3nf-bcnf',3)

add(30,'NAT','Medium-Hard',
"An IPv4 fragment arrives with total length1020 bytes, header length20 bytes, fragment offset100, and MF=1. A router forwards it through an interface with MTU620 bytes and fragments it into the minimum number of fragments, using the largest permitted payload in the first new fragment. Every outgoing header is20 bytes. What is the fragment-offset field of the second outgoing fragment?",[],175,
"The incoming payload is1000 bytes. Each new fragment can hold620-20=600 payload bytes, and600 is divisible by8. The first retains offset100. The second begins600 bytes later, so its offset is100+600/8=175. Offsets remain relative to the original datagram, not relative to the incoming fragment.",[],
"Refragmentation adds to the existing fragment offset rather than restarting at zero.",'ipv4-refragmentation-preserves-original-offset-base','subtract-header;align-payload;add-existing-offset',3)

add(31,'NAT','Medium',
"A disk has cylinders0 through99. Its head is at50, moving toward larger cylinder numbers. Pending requests are at10,40,70,90; all are present initially and no new requests arrive. LOOK scheduling reverses at the last pending request in its current direction, not at the physical disk boundary. Ignoring rotational latency, what is the total head movement required to serve all four requests?",[],120,
"The order is70,90,40,10. Movement is20+20+50+30=120, equivalently(90-50)+(90-10)=40+80. LOOK reverses at90, without visiting99.",[],
"LOOK and SCAN differ in whether the head travels to an unrequested physical endpoint.",'look-directional-sweep-request-endpoint','order-two-sweeps;sum-span-distances')

add(32,'MCQ','Medium-Hard',
"A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, each one cycle. There is no forwarding and no automatic stalling. Register writes occur in the first half of a cycle and ID reads in the second half, so ID may read a value written in WB during the same cycle. The instructions below use ordinary integer registers; R0 is always available. What is the minimum total number of NOP instructions that must be inserted without reordering?\n```text\nADD R1,R0,R0\nADD R2,R1,R0\nADD R3,R2,R0\n```",
['2','3','4','6'],['C'],
"If the first ADD is fetched in cycle1, it writes R1 in cycle5. The second ADD's ID must be no earlier than5, so its IF must be4: two NOPs are needed between them. The second then writes R2 in cycle8, so the third's ID must be8 and IF7: two more NOPs. Four total suffice and fewer cannot meet both dependencies.",
['False: two NOPs repair only one of the two immediate dependencies.','False: at least two separations of two NOPs each are required.','True: both consumer ID stages coincide with the corresponding producer WB stages.','False: same-cycle write-before-read permits two, not three, NOPs per dependency.'],
"A producer's EX completion does not make its result available without forwarding.",'pipeline-no-forwarding-two-register-dependency-gaps','align-consumer-id-with-producer-wb;count-insertions',3)

add(34,'MCQ','Medium-Hard',
"A sorted data file has fixed-length records, with exactly eight records per data page and no unused slots. A range query matches exactly16 consecutive records in file order. An index lookup requires exactly two page reads and identifies the first matching record's page and slot. Index pages are separate from data pages, no page is initially cached, and scanning the range reads each needed data page once. What is the largest possible total number of page reads, over the possible starting slots?",
['3','4','5','6'],['C'],
"If the first record is at slot0, the16 records occupy two pages. If it starts at any slot1 through7, the16 consecutive records cross into a third data page. Thus at most three data pages are needed, and this is attainable. Add two index reads for a largest total of5.",
['False: this counts only the worst-case data pages and omits the index reads.','False: it assumes the range begins exactly at a page boundary.','True: three data pages plus two index pages attain the maximum.','False: sixteen consecutive records cannot span four eight-record pages.'],
"A contiguous record range can span one extra page because its first record need not be page-aligned.",'sorted-file-range-page-alignment-worstcase','bound-span-from-start-slot;add-index-io')

assert len(questions)==20
assert {q['number'] for q in questions}==set(range(11,36))-{22,24,29,33,35}
(ROOT/'drafts/mock002_core_low.json').write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Authored20 complete questions; all require independent review.')
