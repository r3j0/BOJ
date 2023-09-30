#include <stdio.h>

int main(void) {
    int s, m, l;
    scanf("%d", &s);
    scanf("%d", &m);
    scanf("%d", &l);

    if (s+2*m+3*l >= 10) printf("happy");
    else printf("sad");
    return 0;
}