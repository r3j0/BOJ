#include <stdio.h>

void blank(int k) {
    while(k--) printf(" ");
}

void line(int k) {
    if(k == 1) {
        printf("-");
        return;
    }

    line(k/3);
    blank(k/3);
    line(k/3);
}

int power(int n, int k) {
    if(k == 0) return 1;
    else return n * power(n, k - 1);
}

int main(void) {
    while(1) {
        int n;
        int r = scanf("%d", &n);
        if(r != 1) break;
        
        line(power(3, n));
        printf("\n");
    }
    return 0;
}