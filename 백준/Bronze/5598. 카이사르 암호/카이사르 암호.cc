#include <stdio.h>
#include <string.h>

char str[1005];
int main(void) {
    scanf("%s", str);

    for (int i = 0; i < strlen(str); i++) {
        int now = str[i] - 3;
        if (now < 'A') now += 26;

        printf("%c", now);
    }
    return 0;
}