#include <stdio.h>

int main(void) {
    int n; 
    scanf("%d", &n);

    printf("%d\n", n*(n+1)/2);
    printf("%d\n", (n*(n+1)/2)*(n*(n+1)/2));
    printf("%d", (n*(n+1)/2)*(n*(n+1)/2));
    return 0;
}