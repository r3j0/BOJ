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

int main() { fastio
    // 2606 : 바이러스
    int n, m; cin >> n >> m;
    vi edges[n+1];
    while (m--) {
        int a, b; cin >> a >> b;
        edges[a].pb(b);
        edges[b].pb(a);
    }

    // BFS
    queue<int> q;
    vi vis(n+1, 0);
    vis[1] = 1;
    q.push(1);
    int ans = -1;
    while (!q.empty()) {
        int now = q.front(); q.pop(); ans++;
        for (auto& nxt : edges[now]) {
            if (!vis[nxt]) {
                vis[nxt] = 1;
                q.push(nxt);
            }
        }
    }

    cout << ans;
    return 0;
}