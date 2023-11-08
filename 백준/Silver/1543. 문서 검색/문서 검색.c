#include <stdio.h>
#include <string.h>

char original[50005] = {0,};
int o_len = 0;
char search[50005] = {0,};
int s_len = 0;
int main(void) {
    gets(original);
    o_len = strlen(original);
    gets(search);
    s_len = strlen(search);

    int result = 0;
    for (int i = 0; i < o_len - s_len + 1; i++) {
        if (original[i] == search[0]) {
            int done = 1;
            for (int j = 0; j < s_len; j++) {
                if (original[i+j] != search[j]) {
                    done = 0;
                    break;
                }
            }

            if (done == 1) {
                result += 1;
                i += s_len - 1;
            }
        }
    }

    printf("%d", result);
    return 0;
}