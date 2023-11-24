#include <stdio.h>
#include <string.h>

char leftStack[600005];
int leftStackSize = 0;
char rightStack[600005];
int rightStackSize = 0;

int main(void) {
    scanf("%s", leftStack);
    leftStackSize = strlen(leftStack);

    int m;
    scanf("%d", &m);
    getchar();

    char order[10];
    while (m--) {
        gets(order);

        if (order[0] == 'L') {
            if (leftStackSize) rightStack[rightStackSize++] = leftStack[--leftStackSize];
        }
        else if (order[0] == 'D') {
            if (rightStackSize) leftStack[leftStackSize++] = rightStack[--rightStackSize];
        }
        else if (order[0] == 'B') {
            if (leftStackSize) leftStackSize--;
        }
        else if (order[0] == 'P') {
            leftStack[leftStackSize++] = order[2];
        }
    }

    while (rightStackSize) leftStack[leftStackSize++] = rightStack[--rightStackSize];
    leftStack[leftStackSize] = 0;
    printf("%s", leftStack);

    return 0;
}