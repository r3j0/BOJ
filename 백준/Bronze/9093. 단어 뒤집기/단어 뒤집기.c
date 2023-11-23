#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    while(n--) {
        char str[1005];
        gets(str);
        int pre = 0;
        for (int i = 0; i < strlen(str); i++) {
            if (str[i] == ' ') {
                for (int k = i - 1; k >= pre; k--) {
                    printf("%c", str[k]);
                }
                printf(" ");
                pre = i + 1;
            }
        }
        for (int k = strlen(str) - 1; k >= pre; k--) {
            printf("%c", str[k]);
        }
        printf("\n");
    }
    return 0;
}