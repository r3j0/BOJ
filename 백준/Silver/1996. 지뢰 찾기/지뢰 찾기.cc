#include <stdio.h>

char map[1005][1005];
int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%s", map[i]);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == '.') {
                int count = 0;
                for (int y = -1; y <= 1; y++) {
                    for (int x = -1; x <= 1; x++) {
                        if (0 <= i + y && i + y < n && 0 <= j + x && j + x < n && map[i + y][j + x] != '.') count += map[i + y][j + x] - '0';
                    }
                }

                if (count >= 10) printf("M");
                else printf("%c", count + '0');
            }
            else printf("*");
        }
        printf("\n");
    }

    return 0;
}