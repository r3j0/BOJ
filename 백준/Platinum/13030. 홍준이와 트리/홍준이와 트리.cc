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
#define rep(i,s,n) for (auto i = s; i < (n); i++)
#define endl '\n'
const ll INF=INT64_MAX;

#define MOD 1000000007

vector<vi> edge;
vi in; vi out; vi rev; vi depth;

vl tree;
vector<pll> lazy; // F : x     S : k   

void dfs(int now, int dep) {
    static int cnt = 0;
    in[now] = ++cnt;
    rev[cnt] = now;
    depth[now] = dep;
    each(nxt, edge[now]) dfs(nxt, dep + 1);
    out[now] = cnt;
}

void prop(int s, int e, int i) {
    if (lazy[i].F == 0 && lazy[i].S == 0) return;
    if (s != e) {
        lazy[i<<1].F = (lazy[i<<1].F + lazy[i].F) % MOD;
        lazy[i<<1].S = (lazy[i<<1].S + lazy[i].S) % MOD;

        lazy[(i<<1)+1].F = (lazy[(i<<1)+1].F + lazy[i].F) % MOD;
        lazy[(i<<1)+1].S = (lazy[(i<<1)+1].S + lazy[i].S) % MOD;
    }
    else {
        tree[i] = (tree[i] + (lazy[i].F - lazy[i].S * depth[rev[s]])) % MOD;
        if (tree[i] < 0) tree[i] += MOD;
    }
    lazy[i].F = 0; lazy[i].S = 0;
}

void range_update(int s, int e, int i, int l, int r, ll c, ll d) {
    prop(s, e, i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy[i].F = (lazy[i].F + c) % MOD;
        lazy[i].S = (lazy[i].S + d) % MOD;
        prop(s, e, i);
        return;
    }

    int m = (s + e) >> 1;
    range_update(s, m, i << 1, l, r, c, d);
    range_update(m+1, e, (i << 1) + 1, l, r, c, d);
}

ll query(int s, int e, int i, int k) {
    prop(s, e, i);
    if (k < s || e < k) return 0;
    if (s == e) return tree[i];

    int m = (s + e) >> 1;
    return query(s, m, i << 1, k) + query(m + 1, e, (i << 1) + 1, k);
}

int main() { fastio 
    // 13030 : 홍준이와 트리
    // v : x
    // v1 : x-k
    // v2 : x-2k
    // v3 : x-3k ...

    int n, q; cin >> n >> q;
    edge.assign(n+1, {});
    in.assign(n+1, 0); 
    out.assign(n+1, 0); 
    rev.assign(n+1, 0);
    depth.assign(n+1, 0);
    rep(i, 2, n+1) {
        int x; cin >> x; 
        edge[x].pb(i);
    }

    dfs(1, 0);

    tree.assign(4*n, 0); lazy.assign(4*n, {0, 0});

    while(q--) {
        int a; cin >> a;
        if (a == 1) {
            int b; ll c, d; cin >> b >> c >> d;
            range_update(1,n,1,in[b],out[b],c + d * depth[b], d);
        }
        else {
            int b; cin >> b;
            ll ans = query(1, n, 1, in[b]) % MOD;
            if (ans < 0) ans += MOD;
            cout << ans << endl;
        }
    }
    
    return 0;
}