#include <stdio.h>

int n;
int count = 0;

int col[15] = {0,};
int diag_slash[30] = {0,};
int diag_rev_slash[30] = {0,};

void dfs(int y) {
    if (y == n) {
        count += 1;
        return;
    }

    for (int x = 0; x < n; x++) {
        if (col[x] == 0 && diag_slash[y+x] == 0 && diag_rev_slash[x-y+n] == 0) {
            col[x] = 1;
            diag_slash[y+x] = 1;
            diag_rev_slash[x-y+n] = 1;

            dfs(y + 1);

            col[x] = 0;
            diag_slash[y+x] = 0;
            diag_rev_slash[x-y+n] = 0;
        }
    }
}

int main(void) {
    scanf("%d", &n);
    dfs(0);
    printf("%d", count);
    return 0;
}