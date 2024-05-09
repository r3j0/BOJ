#include <stdio.h>

int maps[500][500] = { 0, };
int maxs = 0;

int max(int a, int b) {
    return a > b ? a : b;
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maps[i][j]);
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j >= 3) maxs = max(maxs, maps[i][j - 3] + maps[i][j - 2] + maps[i][j - 1] + maps[i][j]);
            if (j >= 2 && j < m - 1) maxs = max(maxs, maps[i][j - 2] + maps[i][j - 1] + maps[i][j] + maps[i][j + 1]);
            if (j >= 1 && j < m - 2) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i][j + 1] + maps[i][j + 2]);
            if (j < m - 3) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i][j + 3]);

            if (i >= 3) maxs = max(maxs, maps[i - 3][j] + maps[i - 2][j] + maps[i - 1][j] + maps[i][j]);
            if (i >= 2 && i < n - 1) maxs = max(maxs, maps[i - 2][j] + maps[i - 1][j] + maps[i][j] + maps[i + 1][j]);
            if (i >= 1 && i < n - 2) maxs = max(maxs, maps[i - 1][j] + maps[i][j] + maps[i + 1][j] + maps[i + 2][j]);
            if (i < n - 3) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 3][j]);

            if (j >= 1 && i >= 2) maxs = max(maxs, maps[i][j] + maps[i - 1][j] + maps[i - 2][j] + maps[i - 2][j - 1]);
            if (j >= 1 && i >= 1 && i < n - 1) maxs = max(maxs, maps[i + 1][j] + maps[i][j] + maps[i - 1][j] + maps[i - 1][j - 1]);
            if (j >= 1 && i < n - 2) maxs = max(maxs, maps[i + 2][j] + maps[i + 1][j] + maps[i][j] + maps[i][j - 1]);
            if (j < m - 1 && i < n - 2) maxs = max(maxs, maps[i + 2][j + 1] + maps[i + 1][j + 1] + maps[i][j + 1] + maps[i][j]);

            if (j < m - 1 && i >= 2) maxs = max(maxs, maps[i][j] + maps[i - 1][j] + maps[i - 2][j] + maps[i - 2][j + 1]);
            if (j < m - 1 && i >= 1 && i < n - 1) maxs = max(maxs, maps[i + 1][j] + maps[i][j] + maps[i - 1][j] + maps[i - 1][j + 1]);
            if (j < m - 1 && i < n - 2) maxs = max(maxs, maps[i + 2][j] + maps[i + 1][j] + maps[i][j] + maps[i][j + 1]);
            if (j >= 1 && i < n - 2) maxs = max(maxs, maps[i + 2][j - 1] + maps[i + 1][j - 1] + maps[i][j - 1] + maps[i][j]);

            if (i >= 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i - 1][j + 2]);
            if (i >= 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i][j + 1] + maps[i - 1][j + 1]);
            if (i >= 1 && j >= 2) maxs = max(maxs, maps[i][j - 2] + maps[i][j - 1] + maps[i][j] + maps[i - 1][j]);
            if (i < n - 1 && j >= 2) maxs = max(maxs, maps[i + 1][j - 2] + maps[i + 1][j - 1] + maps[i + 1][j] + maps[i][j]);

            if (i < n - 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 2]);
            if (i < n - 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1]);
            if (i < n - 1 && j >= 2) maxs = max(maxs, maps[i][j - 2] + maps[i][j - 1] + maps[i][j] + maps[i + 1][j]);
            if (i >= 1 && j >= 2) maxs = max(maxs, maps[i - 1][j - 2] + maps[i - 1][j - 1] + maps[i - 1][j] + maps[i][j]);

            if (i < n - 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]);
            if (i >= 1 && j < m - 2) maxs = max(maxs, maps[i - 1][j] + maps[i][j] + maps[i][j + 1] + maps[i][j + 2]);
            if (i >= 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j - 1] + maps[i][j - 1] + maps[i][j] + maps[i][j + 1]);
            if (i >= 1 && j >= 2) maxs = max(maxs, maps[i - 1][j - 2] + maps[i][j - 2] + maps[i][j - 1] + maps[i][j]);

            if (i >= 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i - 1][j] + maps[i - 1][j + 1] + maps[i - 1][j + 2]);
            if (i < n - 1 && j < m - 2) maxs = max(maxs, maps[i + 1][j] + maps[i][j] + maps[i][j + 1] + maps[i][j + 2]);
            if (i < n - 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i + 1][j - 1] + maps[i][j - 1] + maps[i][j] + maps[i][j + 1]);
            if (i < n - 1 && j >= 2) maxs = max(maxs, maps[i + 1][j - 2] + maps[i][j - 2] + maps[i][j - 1] + maps[i][j]);
                
            if (i >= 2 && j < m - 1) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i - 1][j + 1] + maps[i - 2][j + 1]);
            if (i >= 2 && j >= 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i - 1][j] + maps[i - 2][j]);
            if (i >= 1 && i < n - 1 && j >= 1) maxs = max(maxs, maps[i + 1][j - 1] + maps[i + 1][j] + maps[i][j] + maps[i - 1][j]);
            if (i < n - 2 && j >= 1) maxs = max(maxs, maps[i + 2][j - 1] + maps[i + 2][j] + maps[i + 1][j] + maps[i][j]);

            if (i < n - 2 && j < m - 1) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 2][j + 1]);
            if (i >= 1 && i < n - 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j] + maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1]);
            if (i >= 2 && j < m - 1) maxs = max(maxs, maps[i - 2][j] + maps[i - 1][j] + maps[i][j] + maps[i][j + 1]);
            if (i >= 2 && j >= 1) maxs = max(maxs, maps[i - 2][j - 1] + maps[i - 1][j - 1] + maps[i][j - 1] + maps[i][j]);

            if (i < n - 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 1][j + 2]);
            if (i < n - 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1]);
            if (i >= 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j - 1] + maps[i - 1][j] + maps[i][j] + maps[i][j + 1]);
            if (i >= 1 && j >= 2) maxs = max(maxs, maps[i - 1][j - 2] + maps[i - 1][j - 1] + maps[i][j - 1] + maps[i][j]);

            if (i >= 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i - 1][j + 1] + maps[i - 1][j + 2]);
            if (i >= 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i - 1][j] + maps[i - 1][j + 1]);
            if (i < n - 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i + 1][j - 1] + maps[i + 1][j] + maps[i][j] + maps[i][j + 1]);
            if (i < n - 1 && j >= 2) maxs = max(maxs, maps[i + 1][j - 2] + maps[i + 1][j - 1] + maps[i][j - 1] + maps[i][j]);

            if (i < n - 2 && j < m - 1) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j + 1]);
            if (i >= 1 && i < n - 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j] + maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1]);
            if (i >= 1 && i < n - 1 && j >= 1) maxs = max(maxs, maps[i - 1][j - 1] + maps[i][j - 1] + maps[i][j] + maps[i + 1][j]);
            if (i >= 2 && j >= 1) maxs = max(maxs, maps[i - 2][j - 1] + maps[i - 1][j - 1] + maps[i - 1][j] + maps[i][j]);

            if (i >= 2 && j < m - 1) maxs = max(maxs, maps[i][j] + maps[i - 1][j] + maps[i - 1][j + 1] + maps[i - 2][j + 1]);
            if (i >= 1 && i < n - 1 && j < m - 1) maxs = max(maxs, maps[i + 1][j] + maps[i][j] + maps[i][j + 1] + maps[i - 1][j + 1]);
            if (i >= 1 && i < n - 1 && j >= 1) maxs = max(maxs, maps[i + 1][j - 1] + maps[i][j - 1] + maps[i][j] + maps[i - 1][j]);
            if (i < n - 2 && j >= 1) maxs = max(maxs, maps[i + 2][j - 1] + maps[i + 1][j - 1] + maps[i + 1][j] + maps[i][j]);

            if (i < n - 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i][j + 2]);
            if (i < n - 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i + 1][j] + maps[i][j + 1]);
            if (i >= 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j - 1] + maps[i - 1][j] + maps[i][j] + maps[i - 1][j + 1]);
            if (i < n - 1 && j >= 2) maxs = max(maxs, maps[i][j - 2] + maps[i][j - 1] + maps[i + 1][j - 1] + maps[i][j]);

            if (i >= 1 && j < m - 2) maxs = max(maxs, maps[i][j] + maps[i][j + 1] + maps[i - 1][j + 1] + maps[i][j + 2]);
            if (i >= 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i - 1][j] + maps[i][j + 1]);
            if (i < n - 1 && j >= 1 && j < m - 1) maxs = max(maxs, maps[i + 1][j - 1] + maps[i + 1][j] + maps[i][j] + maps[i + 1][j + 1]);
            if (i >= 1 && j >= 2) maxs = max(maxs, maps[i][j - 2] + maps[i][j - 1] + maps[i - 1][j - 1] + maps[i][j]);

            if (i < n - 2 && j < m - 1) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j]);
            if (i >= 1 && i < n - 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j] + maps[i][j] + maps[i][j + 1] + maps[i + 1][j]);
            if (i >= 1 && i < n - 1 && j >= 1) maxs = max(maxs, maps[i - 1][j - 1] + maps[i][j - 1] + maps[i][j] + maps[i + 1][j - 1]);
            if (i >= 2 && j < m - 1) maxs = max(maxs, maps[i - 2][j] + maps[i - 1][j] + maps[i - 1][j + 1] + maps[i][j]);

            if (i < n - 2 && j >= 1) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i + 1][j - 1] + maps[i + 2][j]);
            if (i >= 1 && i < n - 1 && j >= 1) maxs = max(maxs, maps[i - 1][j] + maps[i][j] + maps[i][j - 1] + maps[i + 1][j]);
            if (i >= 1 && i < n - 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j + 1] + maps[i][j + 1] + maps[i][j] + maps[i + 1][j + 1]);
            if (i >= 2 && j >= 1) maxs = max(maxs, maps[i - 2][j] + maps[i - 1][j] + maps[i - 1][j - 1] + maps[i][j]);

            if (i < n - 1 && j < m - 1) maxs = max(maxs, maps[i][j] + maps[i + 1][j] + maps[i][j + 1] + maps[i + 1][j + 1]);
            if (i < n - 1 && j >= 1) maxs = max(maxs, maps[i][j - 1] + maps[i][j] + maps[i + 1][j - 1] + maps[i + 1][j]);
            if (i >= 1 && j < m - 1) maxs = max(maxs, maps[i - 1][j] + maps[i - 1][j + 1] + maps[i][j] + maps[i][j + 1]);
            if (i >= 1 && j >= 1) maxs = max(maxs, maps[i - 1][j - 1] + maps[i][j - 1] + maps[i - 1][j] + maps[i][j]);
        }
    }
    printf("%d", maxs);
    return 0;
}