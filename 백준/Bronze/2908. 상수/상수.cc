#include <iostream>
using namespace std;

int main(void) {
    int a, b; cin >> a >> b;
    a = (a%100/10*10) + (a%10*100) + (a/100);
    b = (b%100/10*10) + (b%10*100) + (b/100);
    
    cout << max(a, b);
    return 0;
}