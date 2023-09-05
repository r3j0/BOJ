#include <stdio.h>

int main(void) {
    int x, n, sumPrice = 0;
    scanf("%d", &x);
    scanf("%d", &n);

    while(n--) {
        int a, b;
        scanf("%d %d", &a, &b);
        sumPrice += a * b;
    }

    if (sumPrice == x) printf("Yes");
    else printf("No");

    return 0;
}