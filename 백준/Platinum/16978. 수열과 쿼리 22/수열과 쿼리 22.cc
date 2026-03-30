#include <iostream>
#define fastio ios::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define MAX 1000001
using namespace std;
typedef long long LL;

typedef struct _query {
    LL a1, a2, a3, a4, idx, ans;
} Query;

LL arr[MAX];
LL tree[MAX*4];
Query q[MAX];

int cmp1(const void* a, const void* b) {
    Query* A = (Query*)a;
    Query* B = (Query*)b;

    if (A->a1 == B->a1) {
        if (A->a1 == 1) return A->a4 - B->a4;
        else return A->a2 - B->a2;
    }
    else {
        if (A->a1 == 1) {
            if (A->a4 <= B->a2) return -1;
            else return 1;
        }
        else {
            if (A->a2 >= B->a4) return 1;
            else return -1;
        }
    }
}

int cmp2(const void* a, const void* b) {
    Query* A = (Query*)a;
    Query* B = (Query*)b;

    return A->idx - B->idx;
}

LL build(int s, int e, int i) {
    if (s == e) return tree[i] = arr[s];

    int m = (s + e) / 2;
    return tree[i] = build(s, m, i * 2) + build(m + 1, e, i * 2 + 1);
}

LL interval_sum(int s, int e, int i, int l, int r) {
    if (e < l || r < s) return (LL)0;
    if (l <= s && e <= r) return tree[i];

    int m = (s + e) / 2;
    return interval_sum(s, m, i * 2, l, r) + interval_sum(m + 1, e, i * 2 + 1, l, r);
}

LL update(int s, int e, int i, int k, LL v) {
    if (k < s || e < k) return tree[i];
    if (s == e) return tree[i] = v;

    int m = (s + e) / 2;
    return tree[i] = update(s, m, i * 2, k, v) + update(m + 1, e, i * 2 + 1, k, v);
}

int main() {
    fastio
    int n; cin >> n;

    for (int i = 1; i <= n; i++) cin >> arr[i];
    build(1, n, 1);

    int m; cin >> m;
    int cnt1 = 1;
    for (int i = 0; i < m; i++) {
        LL a, b, c; cin >> a >> b >> c;
        if (a == 1) {
            q[i] = {a, b, c, cnt1++, i};
        }
        else {
            LL d; cin >> d;
            q[i] = {a, b, c, d, i};
        }
    }

    qsort(q, m, sizeof(Query), cmp1);

    for (int i = 0; i < m; i++) {
        LL a = q[i].a1, b = q[i].a2, c = q[i].a3, d = q[i].a4;

        if (a == 1) update(1, n, 1, b, c);
        else q[i].ans = interval_sum(1, n, 1, c, d);
    }

    qsort(q, m, sizeof(Query), cmp2);
    
    for (int i = 0; i < m; i++) {
        if (q[i].a1 == 2)
            cout << q[i].ans << '\n';
    }
    return 0;
}