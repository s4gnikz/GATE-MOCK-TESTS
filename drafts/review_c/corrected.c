#include <stdio.h>
int main(void) {
    int a[2][3] = {{2,4,6},{1,3,5}};
    int (*p)[3] = a;
    int *q = p[1];
    p[0][2] += q[1];
    int *r = p[0] + 1;
    *r++ = q[0];
    q[2] = *r;
    printf("%d\n", a[0][1] + a[1][2]);
    return 0;
}