#include <stdio.h>
int arr[101] = {0,};
int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i = 1; i <= n; i++) arr[i] = i;

    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;    
    }

    for (int i = 1; i <= n; i++) printf("%d ", arr[i]);
    return 0;
}