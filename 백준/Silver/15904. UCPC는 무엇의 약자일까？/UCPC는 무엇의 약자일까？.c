#include <stdio.h>
#include <string.h>

char str[1005];
char search[5] = "UCPC";
int main(void) {
    int now = 0;
    gets(str);
    for (int i = 0; i < strlen(str); i++) {
        if (now < 4 && str[i] == search[now]) now += 1;
    }

    printf("%s", (now == 4) ? "I love UCPC" : "I hate UCPC");
    return 0;
}