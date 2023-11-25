#include <stdio.h>
#include <string.h>

int main(void) {
    char str[100];
    gets(str);

    char stack[100];
    int stackSize = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (stackSize == 0 || str[i] == '(' || stack[stackSize - 1] == ')') stack[stackSize++] = str[i];
        else stackSize -= 1;
    }

    printf("%d", stackSize);
    return 0;
}