#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
    int now;
    struct _Node* next;
    struct _Node* last;
} Node;

Node arr[100000];
int visited[100000] = {0,};


void newnode(Node* cur, int num) {
    Node* tmp = (Node*)malloc(sizeof(Node));
    tmp->now = num;
    tmp->next = NULL;

    if (cur->last == NULL) {
        cur->next = tmp;
        cur->last = tmp;
    }
    else {
        cur->last->next = tmp;
        cur->last = tmp;
    }
}

int dfs(int start) {
    Node* go = arr[start].next;
    visited[start] = 1;

    while(go) {
        if (visited[(go->now) - 1] == 0)
            visited[start] += dfs((go->now) - 1);
        go = go->next;
    }

    
    Node* tmp = arr[start].next;
    Node* del = tmp;
    while(tmp) {
        tmp = tmp->next;
        free(del);
        del = tmp;
    }
    
    return visited[start];
}

int main(void) {
    int n, r, q;
    scanf("%d %d %d", &n, &r, &q);

    for (int i = 0; i < n; i++) {
        arr[i].now = i + 1;
        arr[i].next = NULL;
        arr[i].last = NULL;
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        newnode(&arr[u-1], v);
        newnode(&arr[v-1], u);
    }

    dfs(r-1);

    for (int i = 0; i < q; i++) {
        int tmp;
        scanf("%d", &tmp);
        printf("%d\n", visited[tmp - 1]);
    }

    return 0;
}