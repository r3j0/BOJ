#include <stdio.h>
#include <string.h>

char a[1000001];
char b[1000001];

int main(void) {
    scanf("%s", a);
    scanf("%s", b);
    if (strstr(a, b) == 0) printf("0");
    else printf("1");
    return 0;
}