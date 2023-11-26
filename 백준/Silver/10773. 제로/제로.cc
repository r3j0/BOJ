#include <stdio.h>

int main(void) {
    int k;
    scanf("%d", &k);

    int stack[100005];
    int stackSize = 0;

    for (int i = 0; i < k; i++) {
        int n;
        scanf("%d", &n);

        if (n == 0) stackSize--;
        else stack[stackSize++] = n;
    }

    int result = 0;
    for (int i = 0; i < stackSize; i++) result += stack[i];

    printf("%d", result);
    return 0;
}