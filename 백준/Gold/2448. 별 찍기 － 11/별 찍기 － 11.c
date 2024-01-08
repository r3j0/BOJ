#include <stdio.h>

char level3[3][5] = {
    {' ', ' ', '*', ' ', ' '},
    {' ', '*', ' ', '*', ' '},
    {'*', '*', '*', '*', '*'}
};

char triangle(int y, int x, int level) {
    if (level == 3) printf("%c", level3[y][x]);
    else {
        if (level / 2 > y) {
            if ((((level*2-1) - (level-1)) / 2 > x) || (((level*2-1) - (level-1)) / 2 + (level - 1) <= x)) printf(" ");
            else triangle(y, x - (((level*2-1) - (level-1)) / 2), level/2);
        }
        else {
            if (x == level - 1) printf(" ");
            else triangle(y - (level / 2), ((x < level - 1) ? (x) : (x - (level))), level/2);
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n * 2 - 1; j++) triangle(i, j, n);
        printf("\n");
    }
    return 0;
}