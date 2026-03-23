// 10830 : 행렬 제곱
#include <iostream>
#include <vector>
using namespace std;
#define fastio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long LL;
#define MOD 1000

vector<vector<LL>> mul(vector<vector<LL>> a, vector<vector<LL>> b, LL n) {
    vector<vector<LL>> c (n, vector<LL>(n));

    for (LL i = 0; i < n; i++) {
        for (LL j = 0; j < n; j++) {
            c[i][j] = 0L;
            for (LL k = 0; k < n; k++) {
                c[i][j] = (c[i][j] + (a[i][k] * b[k][j])) % MOD;
            }
        }
    }

    return c;
}

vector<vector<LL>> power(vector<vector<LL>> m, LL n, LL b) {
    if (b == 1) return m;

    vector<vector<LL>> tmp (n, vector<LL>(n));
    tmp = power(m, n, b / 2);
    tmp = mul(tmp, tmp, n);
    if (b % 2) tmp = mul(tmp, m, n);
    return tmp;
}

int main() {
    fastio
    LL n, b; cin >> n >> b;
    
    vector<vector<LL>> m (n, vector<LL>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> m[i][j];
        }
    }

    m = power(m, n, b);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << m[i][j] % MOD << ' ';
        }
        cout << '\n';
    }

    return 0;
}