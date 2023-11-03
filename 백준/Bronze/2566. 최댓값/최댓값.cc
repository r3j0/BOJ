#include <stdio.h>

int main(void) {
    int arr[9][9];
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++)
            scanf("%d", &arr[i][j]);
    }

    int max_value = arr[0][0];
    int max_y = 1;
    int max_x = 1;

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (max_value < arr[i][j]) {
                max_value = arr[i][j];
                max_y = i + 1;
                max_x = j + 1;
            }
        }
    }

    printf("%d\n%d %d", max_value, max_y, max_x);
    return 0;
}