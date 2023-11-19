#include <stdio.h>

int main(void) {
    int s, m;
    scanf("%d %d", &s, &m);

    if (s <= 1023) printf("No thanks");
    else if (((s - 1023) & m) == (s - 1023)) printf("Thanks");
    else printf("Impossible");
    return 0;
}