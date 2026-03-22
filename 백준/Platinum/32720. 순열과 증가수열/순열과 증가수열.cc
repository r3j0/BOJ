// 32720 : 순열과 증가수열
#include <iostream>
#define fastio ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define MAX 1000000
using namespace std;
typedef long long LL;

LL MOD = 1000000007;
LL fac[MAX+1], inv[MAX+1];

LL solve(LL n, LL k) {
    LL ans = fac[n];
    LL plus = n % k;
    for (LL i = 0; i < k; i++) {
        if (i < plus) ans = (ans * inv[n / k + 1]) % MOD;
        else ans = (ans * inv[n / k]) % MOD;
    }
    return ans;
}
LL power(LL a, LL b) {
    if (b == 0) return 1;
    LL tmp = power(a, b / 2);
    tmp = (tmp * tmp) % MOD;
    if (b % 2) tmp = (tmp * a) % MOD;
    return tmp;
}
int main() {
    fac[0] = 1;
    for (int i = 1; i <= MAX; i++) fac[i] = (fac[i-1] * i) % MOD;
    inv[MAX] = power(fac[MAX], MOD-2);
    for (int i = MAX; i > 0; i--) inv[i-1] = (inv[i] * i) % MOD;

    LL n, k; cin >> n >> k;
    cout << solve(n, k);
    return 0;
}