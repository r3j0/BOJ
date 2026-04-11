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

string board[26];
bool vis[26][26];
vi ans;
int n; 
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int dfs(int x, int y) {
    vis[x][y] = true;
    int now = 1;
    rep(d,0,4) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] == '0' || vis[nx][ny]) continue;
        now += dfs(nx, ny);
    }
    return now;
}

int main() { fastio 
    // 2667 : 단지번호붙이기
    cin >> n;
    rep(i,0,n) cin >> board[i];
    rep(i,0,n) {
        rep(j,0,n) {
            if (!vis[i][j] && board[i][j] == '1') {
                ans.pb(dfs(i, j));
            }
        }
    }
    cout << ans.size() << endl;
    sort(all(ans));
    each(a,ans) cout << a << endl;
    return 0;
}