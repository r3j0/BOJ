#include <iostream>
#include <vector>
#include <algorithm>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

int main() {
    fastio
    string s; cin >> s;
    vector<string> v;
    for (int i = 0; i < s.size(); i++) v.push_back(s.substr(i));
    sort(v.begin(), v.end());
    for (string si : v) cout << si << '\n';
    return 0;
}
