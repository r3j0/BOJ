#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);

    int count = 0;
    while (x > 0) {
        if (x % 2 == 1) count += 1;
        x /= 2;
    }

    printf("%d", count);
    return 0;
}