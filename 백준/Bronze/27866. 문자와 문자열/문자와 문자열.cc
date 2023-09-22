#include <stdio.h>

int main(void) {
    char str[1001];
    scanf("%s", str);
    int n;
    scanf("%d", &n);
    printf("%c", str[n - 1]);
    return 0;
}