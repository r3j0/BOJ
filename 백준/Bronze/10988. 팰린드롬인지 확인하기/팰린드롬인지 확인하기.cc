#include <stdio.h>
#include <string.h>

int main(void) {
    char str[105];
    char reverse_str[105];

    scanf("%s", str);
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        reverse_str[i] = str[len - 1 - i];
    }
    reverse_str[len] = 0;

    if (strcmp(str, reverse_str) == 0) printf("1");
    else printf("0");
    return 0;
}