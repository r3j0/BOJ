#include <stdio.h>
#include <string.h>

int main(void) {
    int t;
    scanf("%d", &t);
    while(t--) {
        int n;
        char str[85];
        scanf("%d %s", &n, str);

        for (int i = 0; i < strlen(str); i++) {
            if (i == n - 1) continue;
            printf("%c", str[i]);
        }
        printf("\n");
    }
    return 0;
}