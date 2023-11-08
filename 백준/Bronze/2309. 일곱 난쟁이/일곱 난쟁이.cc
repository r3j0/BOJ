#include <stdio.h>

int main(void) {
    int arr[9];
    int all_sum = 0; 
    for (int i = 0; i < 9; i++) {
        scanf("%d", &arr[i]);
        all_sum += arr[i];
    }

    for (int i = 0; i < 8; i++) {
        int min = i;
        for (int j = i + 1; j < 9; j++) {
            if (arr[min] > arr[j]) min = j;
        }

        if (min != i) {
            int tmp = arr[min];
            arr[min] = arr[i];
            arr[i] = tmp;
        }
    }

    int res1, res2;
    int done = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (all_sum - arr[i] - arr[j] == 100) {
                res1 = i;
                res2 = j;
                done = 1;
                break;
            }
        }

        if (done) break;
    }

    for (int i = 0; i < 9; i++) {
        if (i == res1 || i == res2) continue;
        printf("%d\n", arr[i]);
    }

    return 0;
}