#include <stdio.h>
#include <string.h>

char s[55], t[55], fs[3000] = {0,}, ft[3000] = {0,};

int main(void) {    
    scanf("%s", s);
    scanf("%s", t);

    for (int i = 0; i < strlen(t); i++) strcat(fs, s);
    for (int i = 0; i < strlen(s); i++) strcat(ft, t);

    if (strcmp(fs, ft) == 0) printf("1");
    else printf("0");
    return 0;
}