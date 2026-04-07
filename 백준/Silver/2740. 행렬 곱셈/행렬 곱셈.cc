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
    // 2740 : 행렬 곱셈
    int n, m; cin >> n >> m;
    vector<vi> a(n);
    rep(i,0,n) {
        rep(j,0,m) {
            int x; cin >> x;
            a[i].pb(x);
        }
    }

    int m2, k; cin >> m2 >> k;
    vector<vi> b(m);
    rep(i,0,m) {
        rep(j,0,k) {
            int x; cin >> x;
            b[i].pb(x);
        }
    }

    rep(i,0,n) {
        rep(j,0,k) {
            int now = 0;
            rep(o,0,m) now += a[i][o] * b[o][j];
            cout << now << " ";
        }
        cout << endl;
    }
    return 0;
}