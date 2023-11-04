#include <stdio.h>

int main(void) {
    int arr[101][101] = {0,};
    int n;
    scanf("%d", &n);
    int result = 0;

    while(n--) {
        int left, down;
        scanf("%d %d", &left, &down);

        for (int i = down; i < down + 10; i++) {
            for (int j = left; j < left + 10; j++) {
                if (arr[i][j] == 0) {
                    arr[i][j] = 1;
                    result += 1;
                }
            }
        }
    }
    printf("%d", result);
    return 0;
}