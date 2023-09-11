#include <stdio.h>

char maps[10001][501];
int r, c;
int visited[10001][501];

int dfs(int y, int x) {
    if (x == c - 1) {
        maps[y][x] = 'x';
        return 1;
    }

    if (y - 1 >= 0 && maps[y-1][x+1] == '.' && visited[y-1][x+1] == 0) {
        if (dfs(y-1, x+1) == 1) {
            maps[y][x] = 'x';
            return 1;
        }
    }
    if (maps[y][x+1] == '.' && visited[y][x+1] == 0) {
        if (dfs(y, x+1) == 1) {
            maps[y][x] = 'x';
            return 1;
        }
    }
    if (y + 1 < r && maps[y+1][x+1] == '.' && visited[y+1][x+1] == 0) {
        if (dfs(y+1, x+1) == 1) {
            maps[y][x] = 'x';
            return 1;
        }
    }
    visited[y][x] = 1;
    return 0;
}

int main(void) {
    scanf("%d %d", &r, &c);

    for (int i = 0; i < r; i++)
        scanf("%s", maps[i]);

    int result = 0;
    for (int i = 0; i < r; i++) {
        if (dfs(i, 0) == 1) result += 1;
    }

    printf("%d", result);

    return 0;
}