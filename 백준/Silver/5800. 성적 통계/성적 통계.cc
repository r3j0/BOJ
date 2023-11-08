#include <stdio.h>

int main(void) {
    int k; scanf("%d", &k);

    for (int t = 0; t < k; t++) {
        int n; scanf("%d", &n);
        int arr[50];
        for (int p = 0; p < n; p++) scanf("%d", &arr[p]);
        
        for (int i = 0; i < n - 1; i++) {
            int max = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[max] < arr[j]) max = j;
            }

            if (max != i) {
                int tmp = arr[max];
                arr[max] = arr[i];
                arr[i] = tmp;
            }
        }

        int adj_minus = arr[0] - arr[1];
        for (int i = 1; i < n - 1; i++) {
            if (adj_minus < arr[i] - arr[i+1]) adj_minus = arr[i] - arr[i+1];
        }

        printf("Class %d\nMax %d, Min %d, Largest gap %d\n", t + 1, arr[0], arr[n-1], adj_minus);
    }

    return 0;
}