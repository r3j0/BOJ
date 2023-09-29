#include <stdio.h>

int main(void) {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    int min = n - (m * k);
    int max = n - (m * (k - 1) + 1);
    
    if (min < 0) printf("0 ");
    else printf("%d ", min);
    if (max < 0) printf("0 ");
    else printf("%d ", max);

    return 0;
}