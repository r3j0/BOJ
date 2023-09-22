#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int sum_value = 0;
    int max_value = 0;
    for (int i = 0; i < n; i++) {
        int tmp;
        scanf("%d", &tmp);

        sum_value += tmp;
        if (max_value < tmp) max_value = tmp;
    }

    printf("%f", (double)sum_value / (double)max_value * 100 / (double)n);
    return 0;
}