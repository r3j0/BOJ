#include <stdio.h>
#include <string.h>

int main(void) {
    char str[105];
    char reverse_str[105];

    scanf("%s", str);
    int len = strlen(str);
    int result = 1;
    for (int i = 0; i < len/2; i++) {
        if (str[i] != str[len - 1 - i]) {
            result = 0;
            break;
        }
    }
    printf("%d", result);
    return 0;
}