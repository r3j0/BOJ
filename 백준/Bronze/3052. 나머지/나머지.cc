#include <stdio.h>

int main(void) {
    int arr[42] = {0,};
    int tmp;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &tmp);
        arr[tmp % 42] += 1;
    }

    int cnt = 0;
    for (int i = 0; i < 42; i++) {
        if (arr[i] > 0) cnt += 1;
    }

    printf("%d", cnt);
    return 0;
}