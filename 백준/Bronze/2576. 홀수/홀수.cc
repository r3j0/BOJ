#include <stdio.h>

int main(void) {
    int tmp;
    int sum_value = 0;
    int min_value = 100;
    for (int i = 0; i < 7; i++) {
        scanf("%d", &tmp);
        if (tmp % 2 == 1) {
            sum_value += tmp;
            if (min_value > tmp) min_value = tmp;
        }
    }

    if (sum_value == 0) printf("-1");
    else printf("%d\n%d", sum_value, min_value);
    return 0;
}