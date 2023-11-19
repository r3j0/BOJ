#include <stdio.h>

int main(void) {
    int n;
    int arr[100001];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    int cansee[100001];
    int cansee_length = 0;
    
    cansee[cansee_length++] = arr[0];

    for (int i = 1; i < n; i++) {
        while (cansee_length > 0 && cansee[cansee_length - 1] <= arr[i]) {
            cansee_length -= 1;
        }

        cansee[cansee_length++] = arr[i];
    }

    printf("%d", cansee_length);
    return 0;
}