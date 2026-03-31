#include <iostream>
#include <stack>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

int main() {
    fastio
    // 1. K
    // 2. K번 ( 숫자들, 0 )
    int k; cin >> k;
    stack<int> s;

    while (k--) {
        int n; cin >> n;
        if (n == 0) {
            s.pop();
        }
        else {
            s.push(n);
        }
    }

    int answer = 0;
    while (!s.empty()) {
        answer += s.top();
        s.pop();
    }

    cout << answer;

    return 0;
}