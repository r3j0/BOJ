#include <stdio.h>
#include <stdlib.h>

typedef struct _NODE {
    int key;
    struct _NODE* lc;
    struct _NODE* rc;
} Node;

Node* head = NULL;

Node* newnode(int k) {
    Node* t = (Node*)malloc(sizeof(Node));
    t->key = k;
    t->lc = NULL;
    t->rc = NULL;
    return t;
}

void addnode(Node* now) {
    Node* pre = NULL;
    Node* go = head;
    while (go) {
        pre = go;
        if (go->key > now->key) go = go->lc;
        else go = go->rc;
    }

    if (pre->key > now->key) pre->lc = now;
    else pre->rc = now;
}

void searchNode(Node* now) {
    if (now == NULL) return;
    searchNode(now->lc);
    searchNode(now->rc);
    printf("%d\n", now->key);
}
void freeNode(Node* now) {
    if (now == NULL) return;
    freeNode(now->lc);
    freeNode(now->rc);
    free(now);
}

int main(void) {
    int tmp;
    while(scanf("%d", &tmp) != EOF) {
        Node* now = newnode(tmp);

        if (head == NULL) head = now;
        else addnode(now);
    }

    searchNode(head);
    freeNode(head);
    return 0;
}