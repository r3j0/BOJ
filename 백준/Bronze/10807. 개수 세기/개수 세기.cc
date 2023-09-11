#include <stdio.h>
int arr[101]; 

int main(void) {
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    int v; scanf("%d", &v);
    int result = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == v) result += 1;
    }    

    printf("%d", result);
    return 0;
}