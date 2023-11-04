#include <stdio.h>
#include <string.h>

char str[300];
int main(void) {
    while (1) {
        gets(str);
        if (str[0] == '#') break;

        int count = 0;
        for (int i = 2; i < strlen(str); i++) {
            if (str[i] == str[0] || str[i] + 32 == str[0]) count += 1;
        }

        printf("%c %d\n", str[0], count);
    }
    return 0;
}