// 13172 : Σ
#include <iostream>
using namespace std;
typedef long long int LL;

LL MOD = 1000000007;

LL power(LL a, LL b) {
    if (b == 0) return 1;

    LL tmp = power(a, b / 2);
    tmp = (tmp * tmp) % MOD;
    if (b % 2) tmp = (tmp * a) % MOD;

    return tmp;
}

int main() {
    int n;
    LL answer = 0;

    cin >> n;
    while (n--) {
        LL a, b;
        cin >> b >> a;

        // a x b^(mod-2) % mod
        answer = (answer + (a * power(b, MOD-2))) % MOD;
    }

    cout << answer << endl;
}