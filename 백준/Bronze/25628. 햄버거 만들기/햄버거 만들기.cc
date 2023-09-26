#include <stdio.h>

int min(int a, int b) {
    if (a < b) return a;
    return b;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);

    printf("%d", min(a/2, b));
    return 0;
}