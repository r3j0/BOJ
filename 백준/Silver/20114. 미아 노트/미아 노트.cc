#include <stdio.h>

char str[15][1005];
char result[105];
int main(void) {
    int n, h, w;
    scanf("%d %d %d", &n, &h, &w);
    for (int i = 0; i < h; i++) scanf("%s", str[i]);
    for (int i = 0; i < n; i++) result[i] = '?';
    result[n] = 0;

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < n * w; j++) {
            if (str[i][j] != '?') result[j/w] = str[i][j];
        }
    }

    printf("%s", result);
}