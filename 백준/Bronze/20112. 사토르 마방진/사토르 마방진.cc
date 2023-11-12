#include <stdio.h>

char str[105][105];
int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%s", str[i]);

    int done = 1;
    for (int idx = 0; idx < n; idx++) {
        for (int c = 0; c < n; c++) {
            if (str[idx][c] != str[c][idx]) {
                done = 0;
                break;
            }
        }
        if (done == 0) break;
    }

    if (done == 1) printf("YES");
    else printf("NO");

    return 0;
}