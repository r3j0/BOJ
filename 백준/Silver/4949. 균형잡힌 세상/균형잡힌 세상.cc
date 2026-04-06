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
    // 4949 : 균형잡힌 세상
    while(1) {
        string s; getline(cin, s);
        if(s == ".") break;

        stack<int> st;
        bool done = true;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') st.push(1);
            else if (s[i] == '[') st.push(2);
            else if (s[i] == ')' || s[i] == ']') {
                if (st.empty()) done = false; 
                else {
                    if (s[i] == ')') {
                        if (st.top() == 1) st.pop();
                        else done = false;
                    }
                    else if (s[i] == ']') {
                        if (st.top() == 2) st.pop();
                        else done = false;
                    }
                }
            }
            if (!done) break;
        }
        if (!st.empty()) done = false;

        cout << ((done) ? "yes" : "no") << endl;

    }
    return 0;
}