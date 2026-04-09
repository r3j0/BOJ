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
#define MAX 1000001

typedef struct _node {
    ll sums, maxs;
} Node;

vector<pii> query;
vector<Node> tree(MAX*4);

Node merge(Node a, Node b, int m) {
    Node c;
    c.sums = a.sums + b.sums;
    c.maxs = max(a.maxs + b.sums, b.maxs);
    return c;
}
void build(int s, int e, int i) {
    if (s == e) {
        tree[i] = {0, s};
        return;
    }

    int m = (s + e) >> 1;
    build(s, m, i<<1);
    build(m+1, e, (i<<1)+1);
    tree[i] = merge(tree[i<<1], tree[(i<<1)+1], m+1);
}
void update(int s, int e, int i, int k, ll v) {
    if (e < k || k < s) return;
    if (s == e) {
        tree[i].sums += v;
        tree[i].maxs = s + tree[i].sums;
        return;
    }

    int m = (s + e) >> 1;
    update(s,m,i<<1,k,v);
    update(m+1,e,(i<<1)+1,k,v);
    tree[i] = merge(tree[i<<1], tree[(i<<1)+1], m+1);
}
Node solve (int s, int e, int i, int l, int r) {
    Node tmp = {0, 0};
    if (e < l || r < s) return tmp;
    if (l <= s && e <= r) return tree[i];

    int m = (s + e) >> 1;
    return merge(solve(s,m,i<<1,l,r), solve(m+1,e,(i<<1)+1,l,r), m+1);
}

int main() { fastio 
    // 16670 : King Kog's Reception
    int q; cin >> q;
    while(q--) {
        char mode; cin >> mode;
        ll a; cin >> a;
        ll b = 0LL;

        if (mode == '+') { // join
            cin >> b;
            update(1,MAX-1,1,a,b);
        }
        else if (mode == '-') { // cancel
            update(1,MAX-1,1,query[a-1].first,-query[a-1].second);
        }
        else { // query
            Node res = solve(1,MAX-1,1,1, a);
            cout << max((ll)0, res.maxs - a) << endl;
        }

        query.pb(make_pair(a,b));
    }
    return 0;
}