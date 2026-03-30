#include <iostream>
#define fastio ios::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define MAX 100001
using namespace std;
typedef long long LL;

LL arr[MAX];
LL tree[MAX*4][2];

LL build(int s, int e, int i) {
    if (s == e) return tree[i][0] = arr[s];

    int m = (s + e) / 2;
    return tree[i][0] = build(s, m, i * 2) + build(m + 1, e, i * 2 + 1);
}

void update(int s, int e, int i) {
    if (tree[i][1] == 0) return; 
    if (s == e) { 
        tree[i][0] += tree[i][1];
    }
    else {
        tree[i*2][1] += tree[i][1];
        tree[i*2+1][1] += tree[i][1];

        tree[i][0] += (e - s + 1) * tree[i][1];
    }

    tree[i][1] = 0;
}

LL update_range(int s, int e, int i, int l, int r, LL v) {
    update(s, e, i);
    if (e < l || r < s) return tree[i][0];
    if (l <= s && e <= r) {
        tree[i][1] += v;
        return tree[i][0] + ((e - s + 1) * v);
    }

    int m = (s + e) / 2;
    return tree[i][0] = update_range(s, m, i * 2, l, r, v) + update_range(m + 1, e, i * 2 + 1, l, r, v);
}

LL solve(int s, int e, int i, int k) {
    update(s, e, i);
    if (k < s || e < k) return 0;
    if (s == e) return tree[i][0];

    int m = (s + e) / 2;
    return solve(s, m, i * 2, k) + solve(m + 1, e, i * 2 + 1, k);
}

int main() {
    fastio
    int n; cin >> n;

    for (int i = 1; i <= n; i++) cin >> arr[i];
    build(1, n, 1);

    int m; cin >> m;

    for (int i = 0; i < m; i++) {
        LL a; cin >> a;
        if (a == 1) {
            LL b, c, d; cin >> b >> c >> d;
            update_range(1, n, 1, b, c, d);
        }
        else {
            LL x;
            cin >> x;
            cout << solve(1, n, 1, x) << '\n';
        }
    }
    return 0;
}