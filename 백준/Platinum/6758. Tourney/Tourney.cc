#include <stdio.h>
#include <math.h>
#define SIZE 1100000
typedef long long LL;

LL arr[SIZE];
int win_count[SIZE]= {0,};
typedef struct _Node {
    //LL now_skill;
    LL now_numb;
    int already_wins;
} Node;
Node tree[SIZE * 4];

Node merge_init(Node a, Node b) {
    Node tmp;
    if (arr[a.now_numb] >= arr[b.now_numb]) {
        tmp.now_numb = a.now_numb;
    }
    else {
        tmp.now_numb = b.now_numb;
    }

    tmp.already_wins = 1;
    win_count[tmp.now_numb] += 1;
    return tmp;
}
Node merge(Node o, Node a, Node b) {
    win_count[o.now_numb] -= 1;

    Node tmp;
    if (arr[a.now_numb] >= arr[b.now_numb]) {
        tmp.now_numb = a.now_numb;
    }
    else {
        tmp.now_numb = b.now_numb;
    }

    win_count[tmp.now_numb] += 1;
    return tmp;
}

void init(int start, int end, int idx) {
    if (start == end) {
        tree[idx].now_numb = start;
        return;
    }

    int mid = (start + end) / 2;
    init(start, mid, idx * 2);
    init(mid + 1, end, idx * 2 + 1);
    tree[idx] = merge_init(tree[idx * 2], tree[idx * 2 + 1]);
}

void update(int start, int end, int idx, int what, LL value) {
    if (what < start || end < what) return;
    if (start == end) {
        arr[start] = value;
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, idx * 2, what, value);
    update(mid + 1, end, idx * 2 + 1, what, value);
    tree[idx] = merge(tree[idx], tree[idx * 2], tree[idx * 2 + 1]);
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    int last = (int)pow(2, n) - 1;

    for (int i = 0; i < last + 1; i++) {
        scanf("%lld", &arr[i]);
    }
    init(0, last, 1);
    
    for (int i = 0; i < m; i++) {
        getchar();
        char mode;
        scanf("%c", &mode);

        if (mode == 'R') {
            int a;
            LL b;
            scanf("%d %lld", &a, &b);
            update(0, last, 1, a - 1, b);
        }
        else if (mode == 'W') {
            printf("%d\n", tree[1].now_numb + 1);
        }
        else if (mode == 'S') {
            int a;
            scanf("%d", &a);
            printf("%d\n", win_count[a - 1]);
        }
    }

    return 0;
}