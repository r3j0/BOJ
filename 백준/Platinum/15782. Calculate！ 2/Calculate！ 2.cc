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
vector<bool> vis;
vi in; 
vi out;

void dfs(int now) {
    static int cnt = 0;
    in[now] = ++cnt;
    for (auto& nxt : edge[now]) {
        if (!vis[nxt]) {
            vis[nxt] = true;
            dfs(nxt);
        }
    }
    out[now] = cnt;
}

vl arr, tree, lazy;

void build(int s, int e, int i) {
    if (s == e) {
        tree[i] = arr[s];
        return;
    }

    int m = (s+e) >> 1;
    build(s, m, i << 1); build(m + 1, e, (i << 1) + 1);
    tree[i] = tree[i<<1] ^ tree[(i<<1)+1];
}

void prop(int s, int e, int i) {
    if (lazy[i] == 0) return;
    if ((e-s+1)%2) tree[i] ^= lazy[i];
    if (s != e) {
        lazy[i<<1] ^= lazy[i];
        lazy[(i<<1)+1] ^= lazy[i];
    }
    lazy[i] = 0;
}

ll interval_xor(int s, int e, int i, int l, int r) {
    prop(s, e, i);
    if (e < l || r < s) return (ll)0;
    if (l <= s && e <= r) return tree[i];
    int m = (s+e)>>1;
    return interval_xor(s,m,i<<1,l,r)^interval_xor(m+1,e,(i<<1)+1,l,r);
}

void range_update(int s, int e, int i, int l, int r, ll v) {
    prop(s, e, i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy[i] = v;
        prop(s, e, i);
        return;
    }
    int m = (s+e)>>1;
    range_update(s,m,i<<1,l,r,v); range_update(m+1,e,(i<<1)+1,l,r,v);
    tree[i] = tree[i<<1] ^ tree[(i<<1)+1];
}

int main() { fastio 
    // 15782 : Calculate! 2
    int n,m; cin>>n>>m;

    // 1. DFS
    edge.resize(n+1);
    rep(i,0,n-1) {
        int u,v; cin>>u>>v; 
        edge[u].pb(v); edge[v].pb(u);
    }

    // 2. ETT
    in.resize(n+1); out.resize(n+1);
    vis.resize(n+1); vis[1] = true;
    dfs(1);

    // 3. Lazy XOR Prop
    arr.resize(n+1); tree.resize(n*4); lazy.resize(n*4);
    rep(i,0,n) {
        int x; cin>> x; arr[in[i+1]] = x;
    }

    build(1,n,1);
    while(m--) {
        int a,b; cin>>a>>b;
        if (a==1) cout<<interval_xor(1,n,1,in[b],out[b])<<endl;
        else {
            ll c; cin>>c;
            range_update(1,n,1,in[b],out[b],c);
        }
    }

    return 0;
}