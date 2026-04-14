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

vector<vi> edge;
vi in; vi out;
vi depth;
vector<bool> vis;

void dfs(int now, int dep) {
    static int cnt = 0;
    in[now] = ++cnt;
    vis[now] = true;
    depth[now] = dep;
    each(nxt, edge[now]) {
        if (!vis[nxt]) dfs(nxt, dep+1);
    }
    out[now] = cnt;
}

vi tree; vi lazy;

void prop(int s, int e, int i) {
    if (lazy[i] == 0) return;
    tree[i] += lazy[i] * (e - s + 1);
    if (s != e) {
        lazy[i<<1] += lazy[i];
        lazy[(i<<1)+1] += lazy[i];
    }
    lazy[i] = 0;
}

void range_update(int s, int e, int i, int l, int r) {
    prop(s, e, i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy[i] += 1;
        prop(s, e, i);
        return;
    }

    int m = (s + e) >> 1;
    range_update(s,m,i<<1,l,r);
    range_update(m+1,e,(i<<1)+1,l,r);
    tree[i] = tree[i<<1] + tree[(i<<1)+1];
}

int query(int s, int e, int i, int k) {
    prop(s, e, i);
    if (k < s || e < k) return 0;
    if (s == e) return tree[i];

    int m = (s + e) >> 1;
    return query(s, m, i << 1, k) + query(m+1, e, (i<<1)+1,k);
}

int main() { fastio 
    // 8145 : Megalopolis
    int n; cin >> n;
    edge.assign(n+1, {});
    rep(i,0,n-1) {
        int a, b; cin >> a >> b;
        edge[a].pb(b); edge[b].pb(a);
    }

    in.assign(n+1, 0); out.assign(n+1, 0);
    vis.assign(n+1, false); depth.assign(n+1, 0);
    dfs(1, 0);

    tree.assign(4*n, 0); lazy.assign(4*n, 0);
    int m; cin >> m;
    rep(i,0,n+m-1) {
        char mode; cin >> mode;
        if (mode == 'A') {
            int a, b; cin >> a >> b;
            int tar = a;
            if (in[a] < in[b]) tar = b;
            range_update(1,n,1,in[tar],out[tar]);
        }
        else { // mode == 'W;
            int a; cin >> a;
            cout << depth[a] - query(1,n,1,in[a]) << endl;
        }
    }
    return 0;
}