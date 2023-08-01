#include <iostream>
using namespace std;

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    
    int n;
    int s = 0;
    cin >> n;
    
    int x;
    for (int i = 0; i < n; i++){
        cin >> x;
        s = s + i - x;
    }
    cout << -s;
}