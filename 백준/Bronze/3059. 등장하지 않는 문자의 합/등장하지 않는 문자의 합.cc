#include <stdio.h>
#include <string.h>

int main(void) {
    int t;
    scanf("%d", &t);

    char str[1005];
    while(t--) {
        scanf("%s", str);

        int alpha[26] = {0,};
        for (int i = 0; i < strlen(str); i++) alpha[str[i] - 'A'] = 1;

        int result = 0;
        for (int i = 0; i < 26; i++) {
            if (alpha[i] == 0) result += i + 'A';
        }

        printf("%d\n", result);
    }
    return 0;
}