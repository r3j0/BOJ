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
#define rep(i,n) for (auto i = 0; i < (n); i++)
#define endl '\n'
const ll INF=INT64_MAX;

ll c[1001][1001];
int main() { fastio 
    // 11051 : 이항 계수 2
    int n, k; cin >> n >> k;
    c[1][1] = 1;
    for (int i = 1; i <= n; i++) {
        c[i][0] = 1;
        c[i][i] = 1;

        if (i > 1) {
            for (int j = 1; j <= i; j++) {
                c[i][j] = (c[i-1][j-1] + c[i-1][j]) % 10007;
            }
        }
    }

    cout << c[n][k];
    return 0;
}