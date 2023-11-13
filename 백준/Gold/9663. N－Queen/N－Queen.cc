#include <stdio.h>

int n;
int count = 0;

int col[15] = {0,};
int diag_slash[30] = {0,};
int diag_rev_slash[30] = {0,};

void dfs(int c) {
    if (c == n) {
        count += 1;
        return;
    }

    for (int i = 0; i < n; i++) {
        if (col[i] == 0 && diag_slash[c+i] == 0 && diag_rev_slash[-c+i+n] == 0) {
            col[i] = 1;
            diag_slash[c+i] = 1;
            diag_rev_slash[-c+i+n] = 1;
            dfs(c + 1);
            col[i] = 0;
            diag_slash[c+i] = 0;
            diag_rev_slash[-c+i+n] = 0;
        }
    }
}

int main(void) {
    scanf("%d", &n);
    dfs(0);
    printf("%d", count);
    return 0;
}