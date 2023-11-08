#include <stdio.h>

int main(void) {
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        double now; scanf("%lf", &now);
        printf("$%.2lf\n", now*0.8);
    }
    return 0;
}