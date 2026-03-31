#include <iostream>
#include <stack>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

int main() {
    fastio
    int n; cin >> n;
    stack<int> s;
    while (n--) {
        int x; cin >> x;
        if (x == 0) {
            s.pop(); continue;
        }
        s.push(x);
    }
    int a = 0;
    while (!s.empty()) {
        a += s.top();
        s.pop();
    }
    cout << a;
    return 0;
}