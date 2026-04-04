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

int main() { fastio 
    // 1149 : RGB거리
    int n; cin >> n;
    vector<vi> v;
    rep(i,n) {
        int a, b, c; cin >> a >> b >> c;
        vi vv = {a, b, c};
        v.pb(vv);
    }
    for (int i = 1; i < n; i++) {
        rep(j,3) {
            v[i][j] += min(v[i-1][(j==0)?2:(j-1)], v[i-1][(j==2)?0:(j+1)]);
        }
    }
    cout << *min_element(all(v[n-1]));
    return 0;
}