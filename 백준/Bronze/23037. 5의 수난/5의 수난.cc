#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int sums = 0;
    while (n != 0) {
        int now = n % 10;
        sums += now * now * now * now * now;

        n /= 10;
    }

    printf("%d", sums);
    return 0;
}