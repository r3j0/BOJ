#include <stdio.h>

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    
    int arr[101] = {0,};
    int tmp[101] = {0,};
    for (int i = 1; i <= n; i++) arr[i] = i;

    while(m--) {
        int start, end;
        scanf("%d %d", &start, &end);

        for (int i = start; i <= end; i++) tmp[end-(i-start)] = arr[i];
        for (int i = start; i <= end; i++) arr[i] = tmp[i];
    }

    for (int i = 1; i <= n; i++) printf("%d ", arr[i]);
    return 0;
}