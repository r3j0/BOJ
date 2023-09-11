#include <stdio.h>
int arr[201] = {0,}; 

int main(void) {
    int n; scanf("%d", &n);
    int tmp;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        arr[tmp+100] += 1;
    }

    int v; scanf("%d", &v);
    printf("%d", arr[v+100]);
    return 0;
}