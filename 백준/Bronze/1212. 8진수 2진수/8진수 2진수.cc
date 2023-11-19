#include <stdio.h>
#include <string.h>

char n[340000];

int main(void) {
    scanf("%s", n);
    int n_size = strlen(n);

    if (n_size == 1 && n[0] == '0') printf("0");
    else {
        for (int i = 0; i < n_size; i++) {
            if (i == 0) { // 첫 번째 수는 앞 0이 나오지 않아야 함.
                int done = 0;
                for (int k = 2; k >= 0; k--) {
                    if (((n[i] - '0') & (1 << k)) >> k == 0 && done == 0) continue;
                    else {
                        printf("%d", ((n[i] - '0') & (1 << k)) >> k);
                        done = 1;
                    }
                }
            }
            else {
                for (int k = 2; k >= 0; k--) printf("%d", ((n[i] - '0') & (1 << k)) >> k);
            }
        }
    }
    return 0;
}