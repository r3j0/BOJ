#include <stdio.h>

int main(void) {
    int arr[9] = {0,};
    for (int i = 0; i < 9; i++) scanf("%d", &arr[i]);

    int max_value = arr[0];
    int max_idx = 0;

    for (int i = 1; i < 9; i++) {
        if (max_value < arr[i]) {
            max_value = arr[i];
            max_idx = i;
        }
    }

    printf("%d\n%d", max_value, max_idx + 1);
    return 0;
}