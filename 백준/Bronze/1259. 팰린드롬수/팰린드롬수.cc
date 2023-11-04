#include <stdio.h>
#include <string.h>

char str[10];
int main(void){
    while (1) {
        scanf("%s", str);
        if (strcmp(str, "0") == 0) break;

        int result = 1;
        for (int i = 0; i < strlen(str) / 2; i++) {
            if (str[i] != str[strlen(str) - 1 - i]) {
                result = 0;
                break;
            }
        }

        printf("%s\n", (result == 1) ? "yes" : "no");
    }
    return 0;
}