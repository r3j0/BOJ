#include <stdio.h>
#include <string.h>

char str[100005];
char stack[100005];
int stackSize = 0;
int main(void) {
    gets(str);

    int tag_mode = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '<') {
            while (stackSize)
                printf("%c", stack[--stackSize]);
            tag_mode = 1;
            printf("%c", str[i]);
        }
        else if (str[i] == '>') {
            tag_mode = 0;
            printf("%c", str[i]);
        }
        else if (tag_mode == 0 && str[i] == ' ') {
            while (stackSize)
                printf("%c", stack[--stackSize]);
            printf(" ");
        }
        else if (tag_mode == 1) printf("%c", str[i]);
        else stack[stackSize++] = str[i];
    }

    while (stackSize)
        printf("%c", stack[--stackSize]);

    return 0;
}