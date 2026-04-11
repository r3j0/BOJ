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
vi vis;

void dfs(int now) {
    static int cnt = 1;
    vis[now] = cnt++;
    sort(all(graph[now]));
    for (auto& nxt : graph[now]) {
        if (!vis[nxt]) dfs(nxt);
    }
}

int main() { fastio 
    // 24479 : 알고리즘 수업 - 깊이 우선 탐색 1
    int n, m, r; cin >> n >> m >> r;
    graph.resize(n+1); vis.resize(n+1, 0);

    while(m--) {
        int a, b; cin >> a >> b;
        graph[a].pb(b);
        graph[b].pb(a);
    }

    dfs(r);
    for (int i = 1; i <= n; i++) cout << vis[i] << endl;
    
    return 0;
}