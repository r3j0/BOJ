#include <stdio.h>

int main(void) {
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int k; scanf("%d", &k);
        
        for (int num = 0; num < k; num++) printf("=");
        printf("\n");
    }
    return 0;
}