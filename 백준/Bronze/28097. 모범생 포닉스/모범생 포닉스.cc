#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int tmp;
    int sum_value = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        sum_value += tmp;
    }

    int result = sum_value + (8 * (n - 1));
    printf("%d %d", result / 24, result % 24);

    return 0;
}