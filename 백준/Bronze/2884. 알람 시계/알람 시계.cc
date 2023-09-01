#include <stdio.h>

int main(void) {
    int h, m;
    scanf("%d %d", &h, &m);

    int result = h * 60 + m - 45;
    if (result < 0) result += 1440;

    printf("%d %d", result / 60, result % 60);
    return 0;
}