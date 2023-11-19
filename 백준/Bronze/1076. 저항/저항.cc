#include <stdio.h>
#include <string.h>

int colorMatch(char* str) {
    if (!strcmp(str, "black")) return 0;
    if (!strcmp(str, "brown")) return 1;
    if (!strcmp(str, "red")) return 2;
    if (!strcmp(str, "orange")) return 3;
    if (!strcmp(str, "yellow")) return 4;
    if (!strcmp(str, "green")) return 5;
    if (!strcmp(str, "blue")) return 6;
    if (!strcmp(str, "violet")) return 7;
    if (!strcmp(str, "grey")) return 8;
    if (!strcmp(str, "white")) return 9;
}

long long power(int n, int k) {
    if (k == 0) return 1;
    else return (long long)n * power(n, k - 1);
}

int main(void) {
    char first[10];
    char second[10];
    char third[10];
    scanf("%s", first);
    scanf("%s", second);
    scanf("%s", third);

    long long result = (colorMatch(first) * 10 + colorMatch(second)) * power(10, colorMatch(third));
    printf("%lld", result);
    return 0;
}