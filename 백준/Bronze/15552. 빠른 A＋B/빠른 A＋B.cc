#include <iostream>
using namespace std;

int main(void) {
	cin.tie(NULL); ios::sync_with_stdio(false);
	
	int t; cin >> t;
	
	while(t--) {
		int a, b; cin >> a >> b;
		cout << a + b << "\n";
	}
	return 0;
}