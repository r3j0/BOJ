#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int t;
    cin >> t;

    // 1. cin.tie(NULL);
    // 2. ios::sync_with_stdio(false);
    // 3. endl -> \n

    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        cout << a + b << '\n';
    }

    return 0;
}