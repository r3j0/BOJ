#pragma GCC optimize ("O3")
#pragma GCC optimize ("Ofast")
#pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef __int128_t LL;
typedef __uint128_t ULL;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
#define F first
#define S second
#define pb(x) push_back(x)
#define all(x) (x).begin(), (x).end()
#define each(x,a) for (auto &x : a)
#define rep(i,n) for (auto i = 0; i < (n); i++)
#define endl '\n'
const ll INF = INT64_MAX;
#define MAX 100001

vl arr(MAX), tree(MAX << 2), lazy(MAX << 2);

void prop(int s, int e, int i) {
    if (lazy[i] == 0) return;
    tree[i] += lazy[i] * (e - s + 1);
    if (s != e) {
        lazy[i << 1] += lazy[i];
        lazy[(i << 1) + 1] += lazy[i];
    }
    lazy[i] = (ll) 0;
}

void interval_update(int s, int e, int i, int l, int r, ll v) {
    prop(s, e, i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy[i] += v;
        prop(s, e, i);
        return;
    }

    int m = (s + e) >> 1;
    interval_update(s, m, i << 1, l, r, v);
    interval_update(m + 1, e, (i << 1) + 1, l, r, v);
    tree[i] = tree[i << 1] + tree[(i << 1) + 1];
}

vi edge[MAX];
int in[MAX];
int out[MAX];

void dfs(int i) {
    static int cnt = 0;
    in[i] = ++cnt;
    for (int next : edge[i]) {
        dfs(next);
    }
    out[i] = cnt;
}

ll query(int s, int e, int i, int k) {
    prop(s, e, i);

    if (e < k || k < s) return (ll) 0;
    if (s == e) return tree[i];

    int m = (s + e) >> 1;
    return query(s, m, i << 1, k) + query(m + 1, e, (i << 1) + 1, k);
}

int main() {
    fastio
    // 16404 : 주식회사 승범이네
    int n, m;
    cin >> n >> m;

    // ETT
    rep(i, n) {
        int x; cin >> x;
        if (x == -1) continue;
        edge[x].pb(i+1);
    }

    dfs(1);

    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        if (a == 1) {
            ll c; cin >> c;
            interval_update(1, n, 1, in[b], out[b], c);
        } else cout << query(1, n, 1, in[b]) << endl;
    }

    return 0;
}
