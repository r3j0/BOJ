#include <stdio.h>

int main(void) {
    int n;
    char arr[105][105];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) scanf("%s", arr[i]);

    int k; 
    scanf("%d", &k);

    if (k == 1) {
        for (int i = 0; i < n; i++) printf("%s\n", arr[i]);
    }
    else if (k == 2) {
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j >= 0; j--)
                printf("%c", arr[i][j]);
            printf("\n");
        }
    }
    else {
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < n; j++)
                printf("%c", arr[i][j]);
            printf("\n");
        }
    }

    return 0;
}