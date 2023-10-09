#include <stdio.h>

int main(void) {
    int n; scanf("%d", &n);
    for (int i = 0; i < 4; i++) { // 1 ~ 4번째 줄 출력
        for (int i = 0; i < n; i++) { // 한 셀에 n x n 크기의 @ 출력
            for (int j = 0; j < n; j++) printf("@");
            printf("\n");
        }
    }
    // 5번째 줄 출력
    for (int i = 0; i < n; i++) { // n x 5n 크기의 @ 출력
        for (int j = 0; j < n; j++) printf("@@@@@");
        printf("\n");
    }
    return 0;
}