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
    // 2156 : 포도주 시식
    int n; cin >> n;
    vi v(n); rep(i,0,n) cin >> v[i];

    vi dp; 
    rep(i, 0, n) {
        int res = v[i];
        
        // 1. 지금 마시기 
        //  1-1. i-1 안 마시기 v[i] + dp[i-2]
        int now = v[i];
        if (i>=2) now += dp[i-2];
        res = max(res, now);
        //  1-2. i-2 안 마시기 v[i] + v[i-1] + dp[i-3]
        now = v[i];
        if (i>=1) now += v[i-1];
        if (i>=3) now += dp[i-3];
        res = max(res, now);

        // 2. 지금 안 마시기
        //  2-1. dp[i-1]
        if (i>=1) res = max(res, dp[i-1]);

        dp.pb(res);
    }
    cout << dp[n-1];
    return 0;
}