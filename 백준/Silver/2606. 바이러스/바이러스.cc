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

vector<int> graph[MAX+1];
bool vis[MAX+1];
int ans = 0;
void dfs(int now) {
    vis[now] = true; ans++;
    for (auto& nxt : graph[now]) {
        if (!vis[nxt]) dfs(nxt);
    }
}

int main() { fastio 
    // 2606 : 바이러스
    int n, m; cin >> n >> m;
    while(m--) {
        int a, b; cin >> a >> b;
        graph[a].pb(b);
        graph[b].pb(a);
    }
    dfs(1); cout << ans - 1;
    return 0;
}