#include <iostream>
#include <vector>
#include <algorithm>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MAX(a,b) ((a) > (b) ? (a) : (b))
using namespace std;

int main() {
    fastio
    int n; cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    sort(v.begin(), v.end(), greater<int>());
    long ans = 0;
    for (int i = 0; i < n; i++) ans += MAX(0, (long)(v[i]-i));
    cout << ans << '\n';
    return 0;
}
