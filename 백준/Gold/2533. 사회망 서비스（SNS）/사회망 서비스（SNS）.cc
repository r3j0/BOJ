#include <stdio.h>
#include <stdlib.h>

typedef struct _Point {
    int now;
    struct _Point* next;
} Point;
Point arr[1000001];
Point* last[1000001];
int visited[1000001] = {0,};

Point* newnode(Point* go, Point* dest, int src) {
    Point* tmp = (Point*)malloc(sizeof(Point));
    tmp->now = src;
    tmp->next = NULL;

    if (dest == NULL) go->next = tmp;
    else dest->next = tmp;
    return tmp;
}

void dfs(int start) {
    visited[start] = -1;
    Point* search = arr[start].next;
    Point* tmp = search;
    int vis = 0;
    int early = 0;
    int only = 0;
    while(search) {
        if (visited[search->now] == 0) {
            vis += 1;
            only = search->now;
            dfs(search->now);
            if (visited[search->now] == 2) early += 1;
        }
        search = search->next;
        free(tmp);
        tmp = search;
    }

    if (vis >= 2) {
        if (early == vis) visited[start] = 1;
        else visited[start] = 2;
    }
    else if (vis == 1) {
        if (visited[only] != 2) visited[start] = 2;
        else visited[start] = 1;
    }
    else visited[start] = 1;
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        arr[i].now = 0;
        arr[i].next = NULL;
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        Point* addr = newnode(&arr[u], last[u], v);
        last[u] = addr;
        addr = newnode(&arr[v], last[v], u);
        last[v] = addr;
    }

    dfs(1);
    int res = 0;
    for (int i = 1; i <= n; i++) {
        if (visited[i] == 2) res += 1;
    }

    printf("%d", res);
    return 0;
}