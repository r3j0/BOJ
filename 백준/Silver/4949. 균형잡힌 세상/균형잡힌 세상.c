#include <stdio.h>
#include <string.h>

int main(void) {
    while(1) {
        char str[105];
        gets(str);
        if(!strcmp(str, ".")) break;
        int stack[105] = {0,};
        int stackSize = 0;
        int done = 1;
        for (int i = 0; i < strlen(str); i++) {
            if (str[i] == '(') stack[stackSize++] = 1;
            else if (str[i] == ')') {
                if (stackSize == 0 || stack[stackSize - 1] == 2) {
                    done = 0;
                    break;
                }
                else stackSize -= 1;
            }
            else if (str[i] == '[') stack[stackSize++] = 2;
            else if (str[i] == ']') {
                if (stackSize == 0 || stack[stackSize - 1] == 1) {
                    done = 0;
                    break;
                }
                else stackSize -= 1;
            }
        }

        if (stackSize > 0) done = 0;

        if (done) printf("yes\n");
        else printf("no\n");
    }
    return 0;
}