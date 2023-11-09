#include <stdio.h>

int power(int n, int k) {
    if (k == 0) return 1;
    else return n * power(n, k - 1);
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d", power((1+power(2, n)), 2));
    return 0;
}