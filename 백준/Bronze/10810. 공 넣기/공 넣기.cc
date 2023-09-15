#include <stdio.h>
int arr[101] = {0,};
int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    int i, j, k;
    while(m--) {
        scanf("%d %d %d", &i, &j, &k);
        for (int idx = i; idx <= j; idx++) arr[idx] = k;
    }
    
    for (int idx = 1; idx <= n; idx++) printf("%d ", arr[idx]);
    return 0;
}