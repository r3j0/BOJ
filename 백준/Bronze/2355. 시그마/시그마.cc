#include <stdio.h>

int main(void) {
    long long a, b;
    scanf("%lld %lld", &a, &b);

    if (a > b) {
        long long tmp = a;
        a = b;
        b = tmp;
    }

    printf("%lld", (b*(b+1)/2) - (a*(a-1)/2));
    return 0;
}