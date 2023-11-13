#include <stdio.h>

void dfs(int n, int m, int now, int v[9], int s[9], int s_size) {
    if (s_size == m) {
        for (int i = 0; i < s_size; i++) {
            printf("%d ", s[i]);
        }
        printf("\n");
        return;
    }

    for (int i = now + 1; i <= n; i++) {
        if (v[i] == 0) {
            v[i] = 1;
            //printf("Now s_size : %d / -> i %d selected \n", s_size, i);
            s[s_size++] = i;
            dfs(n, m, i, v, s, s_size);
            //printf("i deleted %d\n", i);
            s_size -= 1;
            v[i] = 0;
        }
    }
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    int visited[9] = {0,};
    int selected[9] = {0,};
    int selected_size = 0;
    dfs(n, m, 0, visited, selected, selected_size);

    return 0;
}