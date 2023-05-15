#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define MAX 10001
using namespace std;

int id, d[MAX] = {0,};
bool finished[MAX];
vector<int> a[MAX];
vector<vector<int>> SCC;
int order[MAX][2];
stack<int> s;

int dfs(int x) {
	d[x] = ++id;
	s.push(x);

	int parent = d[x];
	for (int i = 0; i < a[x].size(); i++) {
		int y = a[x][i];
		if(d[y] == 0) parent = min(parent, dfs(y));
		else if(!finished[y]) parent = min(parent, d[y]);
	}

	if (parent == d[x]) {
		vector<int> sc;
		while(1) {
			int t = s.top();
			s.pop();
			sc.push_back(t);
			finished[t] = true;
			if (t == x) break;
		}
		sort(sc.begin(), sc.end());
		SCC.push_back(sc);
	}

	return parent;
}

bool Comp(vector<int>& va, vector<int>& vb){
  return va[0] < vb[0];
}

int main(void) {
	int v, e; cin >> v >> e;
	while(e--) {
		int st, en; cin >> st >> en;
		a[st].push_back(en);
	}

	for (int i = 1; i <= v; i++) {
		if(d[i] == 0) dfs(i);
	}

	sort(SCC.begin(), SCC.end(), Comp);

	cout << SCC.size() << endl;
	for (int i = 0; i < SCC.size(); i++) {
		for (int j = 0; j < SCC[i].size(); j++) {
			cout << SCC[i][j] << " ";
		}
		cout << -1 << endl;
	}
	return 0;
}
