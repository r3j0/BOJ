#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int result = 1;
    while (n > 1) {
        if (n % 2 != 0) {
            result = 0;
            break;
        }
        n /= 2;
    }

    printf("%d", result);
    return 0;
}