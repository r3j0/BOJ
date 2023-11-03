#include <stdio.h>

int main(void) {
    int now;
    int max_value = 0;
    int max_y;
    int max_x;

    for (int i = 0; i < 81; i++) {
        scanf("%d", &now);

        if (i == 0 || max_value < now) {
            max_value = now;
            max_y = i / 9;
            max_x = i % 9;
        }
    }

    printf("%d\n%d %d", max_value, max_y + 1, max_x + 1);
    return 0;
}