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
const int MAX=10001;

int main() { fastio 
    // 2293 : 동전 1
    ll n, k; cin >> n >> k;
    vl v(k+1, 0);
    vl c; 
    rep(i,0,n) {
        ll x; cin >> x;
        c.pb(x);
    }
    sort(all(c));

    v[0] = 1;
    rep(i,0,n) {
        rep(j,0,k) {
            if (j+c[i] > k) break;
            v[j+c[i]] += v[j];
        }
    }

    cout << v[k];
    return 0;
}