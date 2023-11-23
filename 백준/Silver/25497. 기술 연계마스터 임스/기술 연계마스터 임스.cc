#include <stdio.h>
#include <string.h>

char str[200005];
int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    scanf("%s", str);

    int stackL = 0;
    int stackS = 0;
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == 'L') stackL += 1;
        else if (str[i] == 'S') stackS += 1;
        else if (str[i] == 'R') {
            if (stackL == 0) break;
            else {
                stackL -= 1;
                count += 1;
            }
        }
        else if (str[i] == 'K') {
            if (stackS == 0) break;
            else {
                stackS -= 1;
                count += 1;
            }
        }
        else count += 1;
    }
    printf("%d", count);

    return 0;
}