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
#define MAX 300
int n, m;
int board[MAX][MAX];
bool vis[MAX][MAX];
bool ans = false;
void dfs(int ny, int nx) {
    vis[ny][nx] = true;
    if (ny == n - 1 && nx == m - 1) {
        ans = true;
        return;
    }
    if (ny + 1 < n && !vis[ny+1][nx] && board[ny+1][nx]) dfs(ny+1, nx);
    if (ans) return;
    if (nx + 1 < m && !vis[ny][nx+1] && board[ny][nx+1]) dfs(ny, nx+1);
}
int main() { fastio 
    // 31575 : 도시와 비트코인
    cin >> m >> n;
    rep(i,0,n) {
        rep(j,0,m) cin >> board[i][j];
    }

    dfs(0,0);
    cout << ((ans) ? "Yes" : "No");
    return 0;
}