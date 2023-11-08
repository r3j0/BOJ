#include <stdio.h>
#include <string.h>

char str[5][20] = {0,};
int main(void) {
    int max_col = 0;
    for (int i = 0; i < 5; i++) {
        scanf("%s", str[i]);
        if (max_col < strlen(str[i])) max_col = strlen(str[i]);
    }

    for (int j = 0; j < max_col; j++) {
        for (int i = 0; i < 5; i++) {
            if (str[i][j]) printf("%c", str[i][j]);
        }
    }
    
    return 0;
}