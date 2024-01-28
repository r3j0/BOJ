#include <stdio.h>
#include <stdlib.h>

typedef struct NEXT_ {
    int key;
    struct NEXT_* next;
} Next;

typedef struct NODE_ {
    Next* head;
} Node;

Node graph[2000];
int visited[2000] = {0,};

int maxn(int a, int b) {
    if (a > b) return a;
    return b;
}

int DFS(int n, int now, int cnt) {
    visited[now] = 1;
    if (cnt == 4) return cnt;
    int result = cnt;
    Next* nownode = graph[now].head;
    while(nownode) {
        if (visited[nownode->key] == 0) {
            result = maxn(result, DFS(n, nownode->key, cnt + 1));
        }
        nownode = nownode->next;
    }
    visited[now] = 0;
    return result;
}

Next* newnode(int k) {
    Next* tmp = (Next*)malloc(sizeof(Next));
    tmp->key = k;
    tmp->next = NULL;
    return tmp;
}

void add(Node* headnode, int key) {
    if (headnode->head == NULL) headnode->head = newnode(key);
    else {
        Next* pre = NULL;
        Next* now = headnode->head;
        while(now) {
            pre = now;
            now = now->next;
        }

        pre->next = newnode(key);
    }
}

void frees(Next* head) {
    if (head == NULL) return;
    frees(head->next);
    free(head);
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) graph[i].head = NULL;

    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        add(&graph[a], b);
        add(&graph[b], a);
    }

    int done = 0;
    for (int i = 0; i < n; i++) {
        int result = DFS(n, i, 0);
        if (result >= 4) {
            done = 1;
            break;
        }
    }

    for (int i = 0; i < n; i++) frees(graph[i].head);

    printf("%d", done);
    return 0;
}