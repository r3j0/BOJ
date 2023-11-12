#include <stdio.h>
#include <string.h>

char str[260];
int main(void) {
    gets(str);
    int happy = 0;
    int sad = 0;

    for (int i = 0; i < strlen(str) - 2; i++) {
        if (str[i] == ':' && str[i+1] == '-' && str[i+2] == ')') happy += 1;
        if (str[i] == ':' && str[i+1] == '-' && str[i+2] == '(') sad += 1;
    }

    if (happy == 0 && sad == 0) printf("none");
    else if (happy == sad) printf("unsure");
    else if (happy > sad) printf("happy");
    else printf("sad");
    return 0;
}