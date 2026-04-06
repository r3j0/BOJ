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

vl arr(MAX);
vl tree_d(MAX << 2);
vl lazy_d(MAX << 2);
vl tree_u(MAX << 2);

void prop(int s, int e, int i) {
    if (lazy_d[i] == 0) return;
    tree_d[i] += (lazy_d[i]) * (e - s + 1);
    if (s != e) {
        lazy_d[i<<1] += lazy_d[i];
        lazy_d[(i<<1)+1] += lazy_d[i];
    }
    lazy_d[i] = 0;
}

ll interval_sum(int s, int e, int i, int l, int r) {
    if (e < l || r < s) return (ll)0;
    if (l <= s && e <= r) return tree_u[i];

    int m = (s + e) >> 1;
    return interval_sum(s, m, i << 1, l, r) + interval_sum(m + 1, e, (i << 1) + 1, l, r);
}

ll one_sum(int s, int e, int i, int k) {
    prop(s, e, i);
    if (k < s || e < k) return (ll)0;
    if (s == e) return tree_d[i];

    int m = (s + e) >> 1;
    return one_sum(s, m, i << 1, k) + one_sum(m+1, e, (i << 1) + 1, k);
}

void range_update(int s, int e, int i, int l, int r, ll v) {
    prop(s, e, i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy_d[i] += v;
        prop(s, e, i);
        return;
    }

    int m = (s + e) >> 1;
    range_update(s, m, i << 1, l, r, v);
    range_update(m + 1, e, (i << 1) + 1, l, r, v);
    tree_d[i] = tree_d[i<<1] + tree_d[(i<<1)+1];
}

void update(int s, int e, int i, int k, ll v) {
    if (e < k || k < s) return;
    if (s == e) {
        tree_u[i] += v;
        return;
    }

    int m = (s + e) >> 1;
    update(s, m, i << 1, k, v);
    update(m+1, e, (i << 1)+1,k,v);
    tree_u[i] = tree_u[i<<1] + tree_u[(i<<1)+1];
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

int main() {
    fastio
    // 14288 : 회사 문화 4
    int n, m;
    cin >> n >> m;

    // ETT
    rep(i, n) {
        int x; cin >> x;
        if (x == -1) continue;
        edge[x].pb(i+1);
    }

    dfs(1);
    int mode = 0;

    rep(i, m) {
        ll a; cin >> a;
        if (a == 1) {
            int b; ll c; cin >> b >> c;
            if (mode == 0) range_update(1, n, 1, in[b], out[b], c);
            else update(1, n, 1, in[b], c);
        }
        else if (a == 2) {
            int b; cin >> b;
            cout << interval_sum(1, n, 1, in[b], out[b]) + one_sum(1, n, 1, in[b]) << endl;
        }
        else mode ^= 1;
    }

    return 0;
}
