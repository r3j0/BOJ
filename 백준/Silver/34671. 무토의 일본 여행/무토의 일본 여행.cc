#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, Q;
    cin >> N >> M >> Q;

    unordered_map<ll, ll> best;
    best.reserve(M * 2);
    best.max_load_factor(0.7);

    for(int i = 0; i < M; i++) {
        ll u, v, w;
        cin >> u >> v >> w;

        ll key1 = u * (ll)(N + 1) + v;
        ll key2 = v * (ll)(N + 1) + u;

        if(!best.count(key1) || best[key1] > w) {
            best[key1] = w;
            best[key2] = w;
        }
    }

    while(Q--) {
        ll s, e;
        cin >> s >> e;
        ll key = s * (ll)(N + 1) + e;

        if(best.count(key)) {
            cout << best[key] << "\n";
        } else {
            cout << -1 << "\n";
        }
    }
    return 0;
}