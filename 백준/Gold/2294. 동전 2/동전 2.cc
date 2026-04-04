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
const int MAX = 10001;

int main() { fastio 
    // 2294 : 동전 2
    int n, k; cin >> n >> k;
    vi v(k+1, -1);
    v[0] = 0;
    vi c; 
    rep(i,0,n) {
        int x; cin >> x;
        c.pb(x);
    }
    sort(all(c));

    rep(i,0,n) {
        rep(j,c[i],k+1) {
            if (v[j-c[i]] != -1) {
                if (v[j] == -1) v[j] = MAX;
                v[j] = min(v[j], v[j-c[i]] + 1);
            }
        }
    }

    cout << v[k];
    return 0;
}