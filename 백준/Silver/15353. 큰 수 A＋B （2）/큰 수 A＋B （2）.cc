#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char a[10005];
char b[10005];
char c[10005];
int plus = 0;

int main(void) {
    scanf("%s %s", a, b);
    int a_idx = strlen(a) - 1;
    int b_idx = strlen(b) - 1;
    int c_size = 0;
    while (!(a_idx < 0 && b_idx < 0 && plus == 0)) {
        int now = 0;
        if (a_idx >= 0)
            now += a[a_idx--] - '0';
        if (b_idx >= 0)
            now += b[b_idx--] - '0';
        plus += now;

        c[c_size++] = (plus % 10) + '0';
        plus /= 10;
    }

    c_size -= 1;
    while (c_size >= 0) {
        printf("%c", c[c_size--]);
    }

    return 0;
}