#include <stdio.h>
#include <string.h>

int main(void)
{
    char c, input[7], ans[12]="", color[10][7] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    
    scanf("%s", input);
    for (int i=1; i<10; ++i) {
        if (!strcmp(input, color[i])) {
            c = '0' + i;
            ans[strlen(ans)] = c;
            break;
        }
    }
    scanf("%s", input);
    for (int i=0; i<10; ++i) {
        if (!strcmp(input, color[i])) {
            c = '0' + i;
            ans[strlen(ans)] = c;
            break;
        }
    }
    scanf("%s", input);
    if (strcmp(ans, "0")) {
        for (int i=0; i<10; ++i) {
            if (!strcmp(input, color[i])) {
                for (int j=0; j<i; ++j) {
                    ans[strlen(ans)] = '0';
                }
            }
        }
    }
    printf("%s\n", ans);
    return 0;
}