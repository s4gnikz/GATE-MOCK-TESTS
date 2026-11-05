import json
from pathlib import Path
p=Path(__file__).with_name('pilot_core_high.json')
qs=json.loads(p.read_text(encoding='utf-8'))
by={q['number']:q for q in qs}
def change(n,**kw):
    by[n].update(kw)
    by[n]['verification']={'status':'REVIEW_REQUIRED','method':'revised author derivation','independent_solution':'','evidence':''}
    by[n]['validation_status']='REVIEW_REQUIRED'

change(37,
stem='''A stack log uses symbol a for a push and b for a pop. A valid log starts with an empty stack, never pops an empty stack, and ends with an empty stack. Let L contain exactly the valid logs in which neither aaa nor bbb occurs as a substring; the empty log belongs to L. Which statement about L is correct?''',
options=['L is regular because no run has more than two identical operations.',
'L is not regular, but a deterministic pushdown automaton can recognize it.',
'L is context-free, but no deterministic pushdown automaton can recognize it.',
'L is not context-free because the run restriction and the stack restriction must both be checked.'],
answer=['B'],nat=None,
solution='''A deterministic pushdown automaton can push a stack symbol on a and pop one on b, rejecting underflow. Its finite control also remembers the preceding symbol and whether its current run has length one or two; it rejects a third repetition. It accepts at end of input exactly when the stack is empty. Thus L is deterministic context-free.

To show nonregularity, consider the prefixes u_n=(aab)^n for n≥0. For distinct m,n, append v_n=(abb)^n. The string u_n v_n has no triple repetition, never underflows, and has net stack change n−n=0, so it lies in L. But u_m v_n has net stack change m−n≠0, so it cannot lie in L. Hence infinitely many prefixes are pairwise distinguishable by suffixes, and no finite automaton recognizes L. In particular, banning long runs does not bound stack depth: repeated aab blocks keep increasing it.''',
option_explanations=['False: (aab)^n raises the stack height without creating aaa or bbb; suffixes distinguish infinitely many such prefixes.',
'True: finite control checks the run restriction while the deterministic stack checks balanced legal operations; the suffix argument proves nonregularity.',
'False: the explicit deterministic push/pop construction handles both restrictions without guessing.',
'False: a pushdown stack together with finite control can impose both restrictions simultaneously.'],
misconception='Bounding consecutive pushes does not bound total nesting depth when pushes can be interspersed with fewer pops.',
family='bounded-operation-runs-with-unbounded-stack-depth',
reasoning_pattern='construct-product-of-stack-and-finite-control; distinguish-prefixes-by-balancing-suffixes',
structure_signature='Dyck logs avoiding triple runs; aab growth blocks versus abb drain blocks',reasoning_steps=4)

change(43,
stem='''The following pseudocode uses static (lexical) scoping and ordinary stack activation records. Main contains A; A contains the sibling procedures B and C. Each call has fresh local variables, assignments to a variable found in an enclosing activation modify that variable, and the two assignments in the recursive case of B execute in their displayed order.
```text
procedure Main():
    local x = 20
    procedure A():
        local x = 4
        procedure C():
            x = x + 1
            return x
        procedure B(n):
            local x = 100 + n
            if n == 0:
                return C()
            t = B(n-1)
            u = C()
            return t + u
        return B(2)
    print A()
```
Here t and u are local temporaries of each B activation. What is printed?''',
options=['18','306','15','66'],answer=['A'],nat=None,
solution='''C is declared directly inside A, so every C activation reaches the same active A through its static link. Its references to x therefore name A's x, initially 4, even when a B activation containing its own x is C's caller. B(2) first calls B(1), which first calls B(0). B(0) calls C: A.x becomes 5 and 5 is returned. B(1) next calls C, obtaining 6, and returns 5+6=11. B(2) next calls C, obtaining 7, and returns 11+7=18. Main prints 18. The recursive B locals would matter under dynamic lookup, but not under the specified lexical lookup.''',
option_explanations=['True: the calls to C update the single enclosing A.x to 5,6,7 and their returned values sum to 18.',
'False: 101+102+103=306 uses each calling B activation as the variable environment, which would be dynamic rather than static scoping.',
'False: 15 assumes all three C calls start from a fresh copy of A.x=4; the enclosing activation persists and is modified.',
'False: 21+22+23=66 uses Main.x, but the nearer enclosing declaration in A shadows it.'],
misconception='A static link follows lexical nesting, so recursion in a sibling procedure does not create fresh copies of the sibling\'s enclosing variables.',
family='recursive-sibling-calls-mutating-shared-lexical-environment',
reasoning_pattern='resolve-static-binding; trace-recursive-unwinding; accumulate-stateful-return-values',
structure_signature='Main/A/{B,C}; recursive B local shadows x; C increments A.x on unwind',reasoning_steps=4)

change(54,
stem='''A microprogrammed control unit uses a fixed-width microinstruction. One field jointly encodes the following bus-transfer commands:

- An idle command, in which no source drives the bus and no destination is loaded.
- A non-idle command chooses exactly one of eight sources and a nonempty subset of five destination registers. Every such source/subset pair is allowed.

There are no other bus-transfer commands. Each allowed command needs a distinct binary code, and unused codes are permitted. The other independently encoded fields select one of six ALU operations (including no-operation), one of 128 next addresses, and one of four sequencing conditions (including unconditional sequencing). Codes cannot be shared across these four fields. What is the minimum microinstruction width?''',
options=['19 bits','20 bits','21 bits','25 bits'],answer=['B'],nat=None,
solution='''Five destinations have 2^5−1=31 nonempty subsets. There are 8×31=248 non-idle bus commands and one idle command, giving 249 commands. Since 128<249≤256, the joint bus field needs 8 bits. Independently, six ALU choices need 3 bits, 128 addresses need 7 bits, and four sequencing conditions need 2 bits. The total is 8+3+7+2=20 bits. A separate source field plus five literal destination-enable bits would consume more bits, but the question explicitly permits a joint binary command encoding.''',
option_explanations=['False: the other fields need 12 bits, leaving only seven bus-command bits, which cannot encode 249 commands.',
'True: 8 bits for the 249 bus commands plus 3+7+2 bits for the other fields gives 20.',
'False: 21 bits suffice but are not minimal; joint encoding uses eight bus bits instead of separately encoding source and destination enables.',
'False: the command choices can be binary encoded; 20 bits already suffice.'],
misconception='When controls may be encoded jointly, count legal combined commands rather than blindly adding separate control-signal widths.',
family='joint-microinstruction-field-encoding-with-restricted-command-space',
reasoning_pattern='count-nonempty-destination-subsets; count-source-subset-products; encode-fields',
structure_signature='one idle plus eight times thirty-one legal bus commands; separate 6/128/4 fields',reasoning_steps=4)

change(61,
stem='''Eight nonpreemptive activities have the following half-open time intervals; an activity may begin exactly when another finishes.

| Activity | Interval |
|---|---|
| A | [0,3) |
| B | [1,2) |
| C | [2,4) |
| D | [3,5) |
| E | [4,6) |
| F | [5,7) |
| G | [6,8) |
| H | [7,9) |

Let m be the maximum number of mutually nonoverlapping activities that can be selected, and let r be the number of distinct activity subsets attaining this maximum. What is (m,r)?''',
options=['(3,4)','(4,4)','(4,5)','(5,1)'],answer=['C'],nat=None,
solution='''Earliest-finish selection gives B,C,E,G, a feasible four-activity schedule. The earliest-finish exchange argument guarantees that its cardinality is maximum, so m=4. To count all maximum subsets, partition by the first activity. Starting with A forces D,F,H to fit three more, yielding {A,D,F,H}. Starting with B, the next activity can be C or D. If it is C, the final pair can be (E,G), (E,H), or (F,H). If it is D, the final pair must be (F,H). Starting with C or any later activity permits at most three activities total, so adds no maximum subset. The five maximum subsets are {A,D,F,H}, {B,C,E,G}, {B,C,E,H}, {B,C,F,H}, and {B,D,F,H}. Hence (m,r)=(4,5).''',
option_explanations=['False: B,C,E,G is already a feasible set of four activities.',
'False: it omits one of the five listed optimal subsets, often the one beginning with the later-finishing A.',
'True: earliest-finish greedy establishes m=4, and partitioning by the first two choices gives five optimal subsets.',
'False: earliest-finish greedy reaches four and is optimal; five compatible activities cannot be selected.'],
misconception='An earliest-finish greedy algorithm finds one optimum, but it does not enumerate every optimal schedule.',
family='count-all-optimal-interval-schedules-after-greedy-bound',
reasoning_pattern='establish-optimal-cardinality-with-greedy; enumerate-tied-optima-by-first-choice',
structure_signature='eight staggered intervals; four-slot optimum; five distinct maximum subsets',reasoning_steps=4)

p.write_text(json.dumps(qs,indent=2,ensure_ascii=False),encoding='utf-8')
print('Revised only Q37,Q43,Q54,Q61; each remains REVIEW_REQUIRED.')
