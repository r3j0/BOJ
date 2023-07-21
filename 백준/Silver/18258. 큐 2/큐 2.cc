#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false); // Fase IO
	cin.tie(NULL);

	int n; cin >> n;
	queue<int> q;

	while (n--) {
		string str; cin >> str;
		if (!str.compare("push")) {
			int value; cin >> value;
			q.push(value);
		}
		else if (!str.compare("pop")) {
			if (q.empty()) cout << -1 << "\n";
			else {
				cout << q.front() << "\n";
				q.pop();
			}
		}
		else if (!str.compare("size")) cout << q.size() << "\n";
		else if (!str.compare("empty")) cout << q.empty() << "\n";
		else if (!str.compare("front")) {
			if (q.empty()) cout << -1 << "\n";
			else cout << q.front() << "\n";
		}
		else if (!str.compare("back")) {
			if (q.empty()) cout << -1 << "\n";
			else cout << q.back() << "\n";
		}
	}
	return 0;
}