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
#define MAX 100
int a, b; 
vi graph[MAX+1];
bool vis[MAX+1];
int dfs(int now) {
    vis[now] = true;
    if (now == b) {
        return 0;
    } 
    for (auto& nxt : graph[now]) {
        if (!vis[nxt]) {
            int x = dfs(nxt);
            if (x > -1) return x + 1;
        }
    }
    return -1;
}
int main() { fastio 
    // 2644 : 촌수계산
    int n; cin >> n;
    cin >> a >> b;
    int m; cin >> m;
    while(m--) {
        int u, v; cin >> u >> v;
        graph[u].pb(v);
        graph[v].pb(u);
    }

    cout << dfs(a);
    return 0;
}