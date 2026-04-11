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

vector<vi> graph;
vector<bool> vis;
vi parent;

void dfs(int now) {
    vis[now] = true;
    each(nxt,graph[now]) {
        if (!vis[nxt]) {
            parent[nxt] = now;
            dfs(nxt);
        }
    }
}

int main() { fastio 
    // 11725 : 트리의 부모 찾기
    int n; cin >> n;
    graph.resize(n+1); vis.resize(n+1, false); parent.resize(n+1);
    rep(i,0,n-1) {
        int a, b; cin >> a >> b;
        graph[a].pb(b); graph[b].pb(a);
    }

    dfs(1);

    rep(i, 2, n+1) cout << parent[i] << endl;
    return 0;
}