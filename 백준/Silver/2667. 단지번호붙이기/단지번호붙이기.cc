#include <stdio.h>

int n;
char map[27][27];
int visited[25][25] = {0,};

int result[200];
int result_size = 0;

int row[4] = {-1, 1, 0, 0};
int col[4] = {0, 0, -1, 1};

int dfs(int y, int x) {
    int cnt = 1;
    for(int d = 0; d < 4; d++) {
        int ny = y + row[d];
        int nx = x + col[d];

        if (0 <= ny && ny < n && 0 <= nx && nx < n && map[ny][nx] == '1' && visited[ny][nx] == 0) {
            visited[ny][nx] = 1;
            cnt += dfs(ny, nx);
        }
    }
    return cnt;
}

int main(void) {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) scanf("%s", map[i]);

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (map[i][j] == '1' && visited[i][j] == 0) {
                visited[i][j] = 1;
                int value = dfs(i, j);

                result[result_size++] = value;                
            }
        }
    }

    printf("%d\n", result_size);
    for(int i = 0; i < result_size - 1; i++) {
        int min = i;
        for(int j = i + 1; j < result_size; j++) {
            if (result[min] > result[j]) min = j;
        }

        if (min != i) {
            int tmp = result[min];
            result[min] = result[i];
            result[i] = tmp;
        }
    }

    for(int i = 0; i < result_size; i++) 
        printf("%d\n", result[i]);

    return 0;
}