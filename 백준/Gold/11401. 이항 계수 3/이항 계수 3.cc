// 11401 : 이항 계수 3
#include <iostream>

#define MAX 4000000
typedef long long LL;

using namespace std;

LL MOD = 1000000007;
LL fac[MAX+1], inv[MAX+1];

LL comb(LL a, LL b) {
    return (((fac[a] * inv[a-b]) % MOD) * inv[b]) % MOD;
}

LL power(LL a, LL b) {
    if (b == 0) return 1;
    LL tmp = power(a, b / 2);
    tmp = (tmp * tmp) % MOD;
    if (b % 2) tmp = (tmp * a) % MOD;
    return tmp;
}

int main() {
    LL n, k;
    cin >> n >> k;

    fac[0] = 1;
    for (int i = 1; i <= MAX; i++) {
        fac[i] = (fac[i-1] * i) % MOD;
    }
    inv[MAX] = power(fac[MAX], MOD - 2);
    for (int i = MAX; i > 0; i--) {
        inv[i-1] = (inv[i] * i) % MOD;
    }

    cout << comb(n, k);
    return 0;
}