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

vector<vector<pii>> edge;
vector<bool> vis;
vi in; 
vi out;

vi cst, arr;
vector<vi> tree;
vi lazy;

void dfs(int now, int cu, int prev) {
    static int cnt = 0;
    in[now] = ++cnt;
    arr[in[now]] = cu;
    cst[in[now]] = prev;

    for (auto& nxt : edge[now]) {
        if (!vis[nxt.first]) {
            vis[nxt.first] = true;
            dfs(nxt.first, cu ^ nxt.second, nxt.second);
        }
    }
    out[now] = cnt;
}

vi tree_sum(vi l, vi r) {
    vi tmp(32, 0);
    rep(i,0,32) tmp[i] = l[i] + r[i];
    return tmp;
}

void build(int s, int e, int i) {
    if (s == e) {
        tree[i].resize(32, 0);
        tree[i][arr[s]] = 1;
        return;
    }

    int m = (s+e) >> 1;
    build(s, m, i << 1); build(m + 1, e, (i << 1) + 1);
    tree[i] = tree_sum(tree[i<<1], tree[(i<<1)+1]);
}

void prop(int s, int e, int i) {
    if (lazy[i] == 0) return;

    vi tmp(32, 0);
    rep(j,0,32) tmp[j^lazy[i]] += tree[i][j];
    if (s != e) {
        lazy[i<<1] ^= lazy[i];
        lazy[(i<<1)+1] ^= lazy[i];
    }
    lazy[i] = 0;
    tree[i] = tmp;
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
    tree[i] = tree_sum(tree[i<<1], tree[(i<<1)+1]);
}

int main() { fastio 
    // 23091 : Calculate! 3
    int n,m; cin>>n>>m;

    // 1. 간선 그래프를 정점 그래프로
    edge.resize(n+1);
    rep(i,0,n-1) {
        int u,v,c; cin>>u>>v>>c; 
        edge[u].pb(make_pair(v, c)); edge[v].pb(make_pair(u, c));
    }

    // 2. DFS + ETT
    in.resize(n+1); out.resize(n+1);
    cst.resize(n+1); arr.resize(n+1); tree.resize(n*4); lazy.resize(n*4);
    vis.resize(n+1); vis[1] = true;
    dfs(1, 0, 0); // dfs에 현재 정점 i까지의 xor 결과 저장

    // 3. Lazy XOR Prop
    build(1,n,1);
    while(m--) {
        int a,b; cin>>a>>b;
        if (a==1) {
            int c,d; cin>>c>>d;
            // 더 부모에 있는 정점 골라서 range_update
            int nin, nout;
            if (in[b] > in[c]) {
                nin = in[b]; nout = out[b];
            }
            else {
                nin = in[c]; nout = out[c];
            }

            range_update(1,n,1,nin,nout,d ^ cst[nin]);
            cst[nin] = d;
        }
        else {
            ll ans = 0;
            if (b == 0) {
                rep(i,0,32) ans += 1LL * tree[1][i] * (tree[1][i] - 1) / 2;
            }
            else {
                rep(i,0,32) ans += 1LL * tree[1][i] * tree[1][i ^ b];
                ans /= 2;
            }
            cout << ans << endl;
        }
    }

    return 0;
}