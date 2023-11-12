#include <stdio.h>

int arr[101][101] = {0,};
int main(void) {
    for (int i = 0; i < 4; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        for (int x = x1; x < x2; x++) {
            for (int y = y1; y < y2; y++) {
                arr[x][y] = 1;
            }
        }
    }

    int count = 0;
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++)
            count += arr[i][j];
    }

    printf("%d", count);
    return 0;
}