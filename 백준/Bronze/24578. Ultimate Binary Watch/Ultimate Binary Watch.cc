#include <stdio.h>

int main(void) {
    char digits[5];
    scanf("%s", digits);

    for (int i = 3; i >= 0; i--) {
        for (int j = 0; j < 4; j++) {
            if (j == 1 || j == 3) printf(" ");
            else if (j == 2) printf("   ");
            if (((digits[j] - '0') & (1 << i)) >> i) printf("*");
            else printf(".");
        }
        printf("\n");
    }
    return 0;
}