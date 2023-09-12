#include <stdio.h>

int go(int height, int width) {
    if ((height % 2 == 1 && width % 2 == 1) && height >= 1 && width >= 1) {
        return 1 + go(height/2, width/2) + go(height/2, width/2) + go(height/2, width/2) + go(height/2, width/2);
    }
    else {
        return 0;
    }
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    printf("%d", go(n, m));
    return 0;
}