#include <stdio.h>

int maps[101][101];

int max(int a, int b) {
    if (a > b) return a;
    else return b;
}

int main(void) {
    int tidx = 1;
    while(1) {
        int n;
        scanf("%d", &n);

        if (n == 0) break;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &maps[i][j]);
            }
        }

        int max_value = 0;
        // I Mino
        // Garo
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 3; j++)
                if (i == 0 && j == 0) max_value = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i][j+3]; 
                else max_value = max(max_value, maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i][j+3]);
        }
        // Sero
        for (int i = 0; i < n - 3; i++) {
            for (int j = 0; j < n; j++)
                max_value = max(max_value, maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+3][j]);
        }
        // Z Mino
        // Garo
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 2; j++)
                max_value = max(max_value, maps[i][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+1][j+2]);
        }
        // Sero
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 1; j++)
                max_value = max(max_value, maps[i][j+1] + maps[i+1][j+1] + maps[i+1][j] + maps[i+2][j]);
        }
        // J Mino
        // Garo (Gun)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 2; j++)
                max_value = max(max_value, maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+2]);
        }
        // Sero (J)
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 1; j++)
                max_value = max(max_value, maps[i][j+1] + maps[i+1][j+1] + maps[i+2][j+1] + maps[i+2][j]);
        }
        // Garo (L)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 2; j++)
                max_value = max(max_value, maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+1][j+2]);
        }
        // Sero (r)
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 1; j++)
                max_value = max(max_value, maps[i][j] + maps[i][j+1] + maps[i+1][j] + maps[i+2][j]);
        }
        // T Mino
        // Garo (umb)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 2; j++)
                max_value = max(max_value, maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+1]);
        }
        // Sero (j)
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 1; j++)
                max_value = max(max_value, maps[i][j+1] + maps[i+1][j+1] + maps[i+1][j] + maps[i+2][j+1]);
        }
        // Garo (h)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 2; j++)
                max_value = max(max_value, maps[i+1][j] + maps[i+1][j+1] + maps[i][j+1] + maps[i+1][j+2]);
        }
        // Sero (k)
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 1; j++)
                max_value = max(max_value, maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j]);
        }
        // O Mino
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) 
                max_value = max(max_value, maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i][j+1]);
        }
        printf("%d. %d\n", tidx, max_value);
        tidx += 1;
    }
    return 0;
}