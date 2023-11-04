#include <stdio.h>
#include <string.h>

char str[100];
int main(void) {
    while(1) {
        gets(str);
        if (strcmp(str, "***") == 0) break;
        for (int i = strlen(str) - 1; i >= 0; i--) printf("%c", str[i]);
        printf("\n");
    }
    return 0;
}