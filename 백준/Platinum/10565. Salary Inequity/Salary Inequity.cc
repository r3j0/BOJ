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

typedef struct _node {
    ll maxs;
    ll mins;
} Node;

vector<vi> edge;
vl arr; vector<Node> tree; vl lazy;
vi in; vi out;
int cnt;

void dfs(int root) {
    stack<pii> st; st.push({root, 0});

    while (!st.empty()) {
        pii now = st.top(); st.pop();

        if (now.S == 0) {
            in[now.F] = ++cnt;
            st.push({now.F, 1});
            for (int i = (int)edge[now.F].size() - 1; i >= 0; --i) {
                int nxt = edge[now.F][i];
                st.push({nxt, 0});
            }
        }
        else out[now.F] = cnt;
    }
}

void build(int s, int e, int i) {
    if (s == e) {
        tree[i].maxs = arr[s];
        tree[i].mins = arr[s];
        return;
    }

    int m = (s+e)>>1;
    build(s,m,i<<1);
    build(m+1,e,(i<<1)+1);
    tree[i].maxs = max(tree[i<<1].maxs, tree[(i<<1)+1].maxs);
    tree[i].mins = min(tree[i<<1].mins, tree[(i<<1)+1].mins);
}

void prop(int s, int e, int i) {
    if (lazy[i] == 0) return;
    tree[i].maxs += lazy[i];
    tree[i].mins += lazy[i];

    if (s != e) {
        lazy[i<<1] += lazy[i];
        lazy[(i<<1)+1] += lazy[i];
    }

    lazy[i] = 0;
}

void range_update(int s, int e, int i, int l, int r, int v) {
    prop(s,e,i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy[i] += v;
        prop(s,e,i);
        return;
    }

    int m = (s+e)>>1;
    range_update(s,m,i<<1,l,r,v);
    range_update(m+1,e,(i<<1)+1,l,r,v);
    tree[i].maxs = max(tree[i<<1].maxs, tree[(i<<1)+1].maxs);
    tree[i].mins = min(tree[i<<1].mins, tree[(i<<1)+1].mins);
}

Node query(int s, int e, int i, int l, int r) {
    prop(s,e,i);
    if (e < l || r < s) return {0, 100000000};
    if (l <= s && e <= r) return tree[i];

    int m = (s+e)>>1;
    Node lq = query(s,m,i<<1,l,r);
    Node rq = query(m+1,e,(i<<1)+1,l,r);
    return {max(lq.maxs, rq.maxs), min(lq.mins, rq.mins)};
}

int main() { fastio 
    // 10565 : Salary Inequity
    int t; cin >> t;
    while(t--) {
        cnt = 0;
        int n; cin >> n;
        edge.assign(n+1, {});
        rep(i,2,n+1) {
            int x; cin >> x;
            edge[x].pb(i);
        }
        in.assign(n+1,0); out.assign(n+1,0);
        dfs(1);

        arr.assign(n+1,0); tree.assign(n*4,{0,0}); lazy.assign(n*4,0);
        rep(i,1,n+1) cin >> arr[in[i]];
        build(1,n,1);

        int q; cin >> q;
        while(q--) {
            char mode; cin >> mode;
            if (mode == 'R') {
                int x, v; cin >> x >> v;
                range_update(1,n,1,in[x],out[x],v);
            }
            else {
                int x; cin >> x;
                Node res = query(1,n,1,in[x],out[x]);
                cout << res.maxs - res.mins << endl;
            }
        }
    }
    return 0;
}