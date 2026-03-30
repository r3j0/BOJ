#include <iostream>
#include <algorithm>
#define fastio ios::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define MAX 1000001
using namespace std;
typedef long long LL;

typedef struct _node {
    LL val;
    int idx;
} Node;

LL arr[MAX];
Node tree[MAX*4];

Node compare(Node a, Node b) {
    if (a.val <= b.val) return a;
    return b;
}

Node build(int s, int e, int i) {
    if (s == e) return tree[i] = {arr[s], s};

    int m = (s + e) / 2;
    return tree[i] = compare(build(s, m, i * 2), build(m + 1, e, i * 2 + 1));
}

Node solve(int s, int e, int i, int l, int r) {
    if (e < l || r < s) return {((LL)1 << 32) - 1, -1};
    if (l <= s && e <= r) return tree[i];

    int m = (s + e) / 2;
    return compare(solve(s, m, i*2, l, r), solve(m+1, e, i*2+1, l, r));
}

Node update(int s, int e, int i, int k, LL v) {
    if (k < s || e < k) return tree[i];
    if (s == e) return tree[i] = {v, s};

    int m = (s + e) / 2;
    return tree[i] = compare(update(s, m, i*2, k, v), update(m+1, e, i*2+1, k, v));
}

int main() {
    fastio
    int n; cin >> n;

    for (int i = 1; i <= n; i++) cin >> arr[i];
    build(1, n, 1);

    int m; cin >> m;

    for (int i = 0; i < m; i++) {
        LL a, b, c; cin >> a >> b >> c;
        if (a == 1) update(1, n, 1, b, c);
        else cout << solve(1, n, 1, b, c).idx << '\n';
    }
    return 0;
}