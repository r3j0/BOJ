#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
    int ep;
    struct _Node* next;
    struct _Node* last;
} Node;
Node em[100001];
int parent[100001];
int compliment[100001] = {0,};

void newnode(Node* ptr, int e) {
    Node* now = (Node*)malloc(sizeof(Node));
    now->ep = e;
    now->next = NULL;
    now->last = NULL;

    if (ptr->next == NULL) ptr->next = now;
    else ptr->last->next = now;
    ptr->last = now;
}

void dfs(int now, int cu) {
    Node* search = em[now].next;
    Node* tmp = search;
    while(search) {
        dfs(search->ep, cu + compliment[now]);
        search = search->next;
        free(tmp);
        tmp = search;
    }
    compliment[now] += cu;
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    int root = 0;

    for (int i = 1; i <= n; i++) {
        int par; 
        scanf("%d", &par);
        parent[i] = par;
        if (par == -1) root = i;

        em[i].ep = -1;
        em[i].next = NULL;
        em[i].last = NULL;
    }

    for (int i = 0; i < m; i++) {
        int k, w;
        scanf("%d %d", &k, &w);
        compliment[k] += w;
    }

    for (int i = 1; i <= n; i++) {
        if (parent[i] != -1)
            newnode(&em[parent[i]], i);
    }

    dfs(root, 0);

    for (int i = 1; i <= n; i++) printf("%d ", compliment[i]);

    return 0;
}