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

int n, m;
string board[20];
bool vis[20][20];
bool alpvis[26];

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int dfs(int x, int y) {
    int now = 1;
    rep(d,0,4) {
        int nx = x + dx[d];
        int ny = y + dy[d];

        if (nx < 0 || n <= nx || ny < 0 || m <= ny || vis[nx][ny] || alpvis[board[nx][ny] - 'A']) continue;
        vis[nx][ny] = true;
        alpvis[board[nx][ny] - 'A'] = true;

        now = max(now, dfs(nx, ny) + 1);

        vis[nx][ny] = false;
        alpvis[board[nx][ny] - 'A'] = false;
    }

    return now;
}

int main() { fastio 
    // 1987 : 알파벳
    cin >> n >> m;
    rep(i,0,n) cin >> board[i];

    vis[0][0] = true;
    alpvis[board[0][0] - 'A'] = true;
    cout << dfs(0, 0);
    return 0;
}