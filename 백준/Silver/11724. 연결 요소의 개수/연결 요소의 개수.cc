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

void dfs(int now) {
    vis[now] = true;
    each(nxt,graph[now]) {
        if (!vis[nxt]) dfs(nxt);
    }
}

int main() { fastio 
    // 11724 : 연결 요소의 개수
    int n, m; cin >> n >> m;
    graph.resize(n+1); vis.resize(n+1, false);
    while (m--) {
        int a, b; cin >> a >> b;
        graph[a].pb(b); graph[b].pb(a);
    }

    int cnt = 0;
    rep(i, 1, n+1) {
        if (!vis[i]) {
            dfs(i);
            cnt++;
        }
    }

    cout << cnt;
    return 0;
}