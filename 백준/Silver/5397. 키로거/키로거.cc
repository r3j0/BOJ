#include <stdio.h>
#include <string.h>
#define SIZE 1000005

char str[SIZE];
char stack1[SIZE];
int stack1_size = 0;
char stack2[SIZE];
int stack2_size = 0;

int main(void) {
    int t;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", str);
        stack1_size = 0;
        stack2_size = 0;
        for (int i = 0; i < strlen(str); i++) {
            if (str[i] == '<') {
                if (stack1_size != 0) {
                    stack2[stack2_size++] = stack1[stack1_size - 1];
                    stack1_size -= 1;
                }
            }
            else if (str[i] == '>') {
                if (stack2_size != 0) {
                    stack1[stack1_size++] = stack2[stack2_size - 1];
                    stack2_size -= 1;
                }
            }
            else if (str[i] == '-') {
                if (stack1_size != 0) stack1_size -= 1;
            }
            else {
                stack1[stack1_size++] = str[i];
            }
        }

        for (int i = 0; i < stack1_size; i++) printf("%c", stack1[i]);
        for (int i = stack2_size - 1; i >= 0; i--) printf("%c", stack2[i]);
        printf("\n");
    }
    return 0;
}