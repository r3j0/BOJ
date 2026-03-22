// 13977 : 이항 계수와 쿼리
#include <iostream>

#define fastio ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
#define MAX 4000000
typedef long long LL;
using namespace std;

LL MOD = 1000000007;
LL fac[MAX+1], inv[MAX+1];

LL comb(LL a, LL b) {
    return (((fac[a] * inv[a-b]) % MOD) * inv[b]) % MOD;
}

LL power(int a, int b) {
    if (b == 0) return 1;
    LL tmp = power(a, b / 2);
    tmp = (tmp * tmp) % MOD;
    if (b % 2) tmp = (tmp * a) % MOD;
    return tmp;
}

int main() {
    fac[0] = 1;
    for (int i = 1; i <= MAX; i++) fac[i] = (fac[i-1] * i) % MOD;
    inv[MAX] = power(fac[MAX], MOD - 2);
    for (int i = MAX; i > 0; i--) inv[i-1] = (inv[i] * i) % MOD;

    fastio
    int m; cin >> m;
    while (m--) {
        LL n, k; cin >> n >> k;
        cout << comb(n, k) << '\n';
    }
    return 0;
}