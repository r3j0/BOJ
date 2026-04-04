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
    // 9461 : 파도반 수열
    
    vl v(101);
    for (int i = 0; i <= 100; i++) {
        if (i <= 3) {
            v[i] = 1;
            continue;
        }
        v[i] = v[i-2] + v[i-3];
    }
    
    int t; cin >> t;
    while(t--) {
        int n; cin >> n; cout << v[n] << endl;
    }
    return 0;
}