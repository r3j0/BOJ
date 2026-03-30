#include <iostream>
#define fastio ios::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define MAX 1000001
using namespace std;
typedef long long LL;

LL arr[MAX];
LL tree[MAX*4];

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
    int n, m, k; cin >> n >> m >> k;

    for (int i = 1; i <= n; i++) cin >> arr[i];
    build(1, n, 1);

    for (int i = 0; i < m + k; i++) {
        LL a, b, c; cin >> a >> b >> c;
        if (a == 1) update(1, n, 1, b, c);
        else cout << interval_sum(1, n, 1, b, c) << '\n';
    }
    return 0;
}