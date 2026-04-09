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
    // 3986 : 좋은 단어
    int n; cin >> n;
    int ans=0;
    while(n--) {
        string s; cin >> s;
        stack<char> st;
        rep(i,0,s.size()) {
            if (st.empty()) st.push(s[i]);
            else {
                if (st.top() == s[i]) st.pop();
                else st.push(s[i]);
            }
        }

        if (st.empty()) ans++;
    }
    cout << ans << endl;
    return 0;
}