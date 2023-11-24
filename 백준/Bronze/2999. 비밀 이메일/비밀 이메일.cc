#include <stdio.h>
#include <string.h>

int main(void) {
    char str[105];
    scanf("%s", str);

    int r = 1, c = strlen(str);

    for (int i = 2; i <= strlen(str); i++) {
        if (strlen(str) % i == 0 && i <= strlen(str) / i) {
            r = i;
            c = strlen(str) / i;
        }
    }

    char arr[100][100];

    int cnt = 0;
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < r; i++) {
            arr[i][j] = str[cnt++];
        }
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%c", arr[i][j]);
        }
    }
    return 0;
}