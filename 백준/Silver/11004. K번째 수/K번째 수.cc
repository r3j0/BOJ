#include <iostream>
#include <vector>
#include <algorithm>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

int main() {
    fastio
    int n, k;
    cin >> n >> k;

    vector<int> a (n);
    for (int i = 0; i < n; i++) cin >> a[i];

    sort(a.begin(), a.end());
    cout << a[k-1];

    return 0;
}