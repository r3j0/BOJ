#include <stdio.h>
#define SIZE 100001
typedef long long LL;

int arr[SIZE];
typedef struct Node {
    LL lMax;
    LL rMax;
    LL sums;
    LL allMax;
} Node;

Node tree[SIZE * 4];
// 0. 왼쪽 최대 구간
// 1. 오른쪽 최대 구간
// 2. 총합
// 3. 전체 최대 구간

LL max2(LL a, LL b) { return (a >= b) ? a : b; }
LL max3(LL a, LL b, LL c) { return (a >= b && a >= c) ? a : ((b >= a && b >= c) ? b : c); }

Node merge(Node a, Node b) {
    Node tmp;
    tmp.lMax = max2(a.lMax, a.sums + b.lMax);
    tmp.rMax = max2(b.rMax, a.rMax + b.sums);
    tmp.sums = a.sums + b.sums;
    tmp.allMax = max3(a.allMax, b.allMax, a.rMax + b.lMax);
    return tmp;
}
    
void init(int start, int end, int idx) {
    if (start == end) {
        tree[idx].lMax = arr[start];
        tree[idx].rMax = arr[start];
        tree[idx].sums = arr[start];
        tree[idx].allMax = arr[start]; 
        return;
    }

    int mid = (start + end) / 2;
    init(start, mid, idx * 2);
    init(mid + 1, end, idx * 2 + 1);
    tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}


Node interval_max(int start, int end, int idx, int left, int right, int* error) {
    //("[%d-%d]\n", start, end);
    Node tmp;
    if (end < left || right < start) {
        *error = 1;
        return tmp;
    }
    if (left <= start && end <= right) {
        *error = 0;
        //printf("[%d-%d] tree[idx] : %lld %lld %lld %lld\n", start, end, tree[idx].lMax, tree[idx].rMax, tree[idx].sums, tree[idx].allMax);
        return tree[idx];
    }

    int mid = (start + end) / 2;

    int e1 = 0;
    Node q1 = interval_max(start, mid, idx * 2, left, right, &e1);

    int e2 = 0;
    Node q2 = interval_max(mid + 1, end, idx * 2 + 1, left, right, &e2);

    if (e1 == 1 && e2 == 1) {
        *error = 1;
        return tmp;
    }
    
    if (e1 == 1) return q2;
    if (e2 == 1) return q1;
    
    tmp = merge(q1, q2);
    //printf("[%d-%d] Tmp : %lld %lld %lld %lld\n", start, end, tmp.lMax, tmp.rMax, tmp.sums, tmp.allMax);
    return tmp;
}

void tree_debug(int start, int end, int idx) {
    if (start == end) {
        printf("[%d] %lld %lld %lld %lld\n",start,tree[idx].lMax, tree[idx].rMax, tree[idx].sums, tree[idx].allMax);
        return;
    }
    printf("[%d-%d] %lld %lld %lld %lld\n",start,end,tree[idx].lMax, tree[idx].rMax, tree[idx].sums, tree[idx].allMax);
    int mid = (start + end) / 2;
    tree_debug(start, mid, idx * 2);
    tree_debug(mid + 1 ,end, idx * 2 + 1);
}

int main(void) {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    init(0, n - 1, 1);

    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        int e;
        Node result = interval_max(0, n - 1, 1, a - 1, b - 1, &e);
        printf("%lld \n", max3(result.lMax, result.rMax, result.allMax));
    }
    return 0;
}