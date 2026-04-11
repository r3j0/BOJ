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

vector<vi> graph;
vi que;
vi tra;

int main() { fastio 
    // 34846 : 이웃 마을
    int n, m, q; cin >> n >> m >> q;
    graph.resize(n+1); que.resize(n+1, 0); tra.resize(n+1, 0);

    while(m--) {
        int a, b; cin >> a >> b;
        graph[a].pb(b);
        graph[b].pb(a);
    }

    while(q--) {
        int a, b; cin >> a >> b;
        if (a == 1) {
            if (tra[b] == 0) {
                tra[b] = 1;
                each(nxt,graph[b]) {
                    que[nxt] += 1;
                }
            }
        }
        else {
            cout << que[b] << endl;
        }
    }

    return 0;
}