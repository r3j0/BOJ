#include <stdio.h>

int main(void) {
    int r, s;
    scanf("%d %d", &r, &s);

    if (r * 8 + s * 3 > 28) printf("%d", r * 8 + s * 3 - 28);
    else printf("0");

    return 0;
}