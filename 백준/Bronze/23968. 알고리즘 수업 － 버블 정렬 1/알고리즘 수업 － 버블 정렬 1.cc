#include <stdio.h>

int arr[10001];
int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i+1]);

    int count = 0;
    for (int last = n; last >= 2; last--) {
        for (int i = 1; i < last; i++) {
            if (arr[i] > arr[i+1]) {
                int tmp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = tmp;

                count += 1;
                if (count == k) {
                    printf("%d %d", arr[i], arr[i+1]);
                    return 0;
                }
            }
        }
    }

    printf("-1");
    return 0;
}