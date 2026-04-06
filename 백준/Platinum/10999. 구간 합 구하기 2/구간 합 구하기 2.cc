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
#define MAX 2000000

vl arr(MAX), tree(MAX << 2), lazy(MAX << 2);

void build(int s, int e, int i) {
    if (s == e) {
        tree[i] = arr[s];
        return;
    }

    int m = (s + e) >> 1;
    build(s, m, i << 1);
    build(m + 1, e, (i << 1) + 1);
    tree[i] = tree[i << 1] + tree[(i << 1) + 1];
}

void prop(int s, int e, int i) {
    if (lazy[i] == 0) return;
    tree[i] += lazy[i] * (e - s + 1);
    if (s != e) {
        lazy[i << 1] += lazy[i];
        lazy[(i << 1) + 1] += lazy[i];
    }
    lazy[i] = (ll)0;
}
void interval_update(int s, int e, int i, int l, int r, ll v) {
    prop(s, e, i);
    if (e < l || r < s) return;
    if (l <= s && e <= r) {
        lazy[i] += v;
        prop(s, e, i);
        return;
    }

    int m = (s + e) >> 1;
    interval_update(s, m, i << 1, l, r, v);
    interval_update(m + 1, e, (i << 1) + 1, l, r, v);
    tree[i] = tree[i << 1] + tree[(i << 1) + 1];
}
ll interval_sum(int s, int e, int i, int l, int r) {
    prop(s, e, i);
    if (e < l || r < s) return (ll)0;
    if (l <= s && e <= r) return tree[i];
    int m = (s + e) >> 1;
    return interval_sum(s, m, i << 1, l, r) + interval_sum(m + 1, e, (i << 1) + 1, l, r);
}
int main() { fastio
    // 10999 : 구간 합 구하기 2
    int n, m, k; cin >> n >> m >> k;
    rep(i,n) cin >> arr[i+1];
    build(1, n, 1);
    rep(i,m+k) {
        ll a, b, c; cin >> a >> b >> c;
        if (a == 1) {
            ll d; cin >> d;
            interval_update(1, n, 1, b, c, d);
        }
        else cout << interval_sum(1, n, 1, b, c) << endl;
    }

    return 0;
}