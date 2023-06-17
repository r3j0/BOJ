#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* line1[10] = {"0000","   1","2222","3333","4  4","5555","6666","7777","8888","9999"};
char* line2[10] = {"0  0","   1","   2","   3","4  4","5","6","   7","8  8","9  9"};
char* line3[10] = {"0  0","   1","2222","3333","4444","5555","6666","   7","8888","9999"};
char* line4[10] = {"0  0","   1","2","   3","   4","   5","6  6","   7","8  8","   9"};
char* line5[10] = {"0000","   1","2222","3333","   4","5555","6666","   7","8888","   9"};

char str[1000000];

int main(void) {
    scanf("%s", str);
    for (int i = 0; i < strlen(str); i++) {
        printf("%s\n%s\n%s\n%s\n%s\n\n", line1[str[i]-'0'], line2[str[i]-'0'], line3[str[i]-'0'], line4[str[i]-'0'], line5[str[i]-'0']);
    }
    return 0;
}