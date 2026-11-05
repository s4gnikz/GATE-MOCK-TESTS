import json
from pathlib import Path
p=Path(__file__).with_name('pilot_core_high.json')
qs=json.loads(p.read_text(encoding='utf-8'))
q=next(q for q in qs if q['number']==41)
q.update(
stem='''A 5×5 matrix is stored in row-major order in a one-dimensional C array: row r, column c is a[5*r+c], for 0≤r,c<5. Consider this complete program. All arithmetic fits in int.
```c
#include <stdio.h>
static void swap(int *p, int *q) {
    int t = *p; *p = *q; *q = t;
}
int main(void) {
    int a[25];
    for (int i = 0; i < 25; ++i) a[i] = i;
    for (int k = 0; k < 2027; ++k) {
        for (int r = 0; r < 5; ++r)
            for (int c = r + 1; c < 5; ++c)
                swap(&a[5*r+c], &a[5*c+r]);
        for (int r = 0; r < 5; ++r)
            for (int c = 0; c < 2; ++c)
                swap(&a[5*r+c], &a[5*r+4-c]);
    }
    printf("%d %d", a[7], a[17]);
    return 0;
}
```
What is printed?''',
options=['13 11','11 13','7 17','17 7'],answer=['A'],nat=None,
solution='''The first nested loop swaps each pair of entries on opposite sides of the main diagonal exactly once, so it transposes the matrix. The second nested loop reverses each row. The composition is a clockwise 90-degree rotation. Four iterations restore the original array, and 2027 has remainder 3 modulo 4, so the net transformation is a counterclockwise 90-degree rotation. Under that net transformation, new[r,c]=old[c,4−r]. Index 7 is (r,c)=(1,2), so its value is old[2,3]=5×2+3=13. Index 17 is (3,2), so its value is old[2,1]=11. Hence the program prints `13 11`. Every pointer is inside the single a array and every swap uses distinct entries.''',
option_explanations=['True: three clockwise quarter-turns map the queried positions to original positions (2,3) and (2,1).',
'False: these are the values after one clockwise quarter-turn, not after 2027 iterations.',
'False: these are the unchanged initial values; 2027 is not divisible by four.',
'False: these are the values after two quarter-turns, not three.'],
misconception='The order of transpose and row reversal determines the rotation direction; repeated index permutations should be reduced by their period.',
family='composed-inplace-array-permutation-periodic-matrix-rotation',
reasoning_pattern='infer-two-index-transformations; compose; reduce-exponent; invert-position-map',
structure_signature='flat five-by-five row-major array; upper-triangle transpose; row reversal; quarter-turn cycle',
reasoning_steps=5,
verification={'status':'REVIEW_REQUIRED','method':'revised author derivation','independent_solution':'','evidence':''},
validation_status='REVIEW_REQUIRED')
p.write_text(json.dumps(qs,indent=2,ensure_ascii=False),encoding='utf-8')
print('Revised Q41 only; independent review required.')
