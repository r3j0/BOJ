#include <bits/stdc++.h>
typedef long long LL;
using namespace std;

typedef struct Point { LL x; LL y; } point;

LL CCW(point, point, point);

int main() {
    point pos1, pos2, pos3;
    cin >> pos1.x >> pos1.y;
    cin >> pos2.x >> pos2.y;
    cin >> pos3.x >> pos3.y;

    LL result = CCW(pos1, pos2, pos3);
    if (result > 0) cout << 1;
    else if (result < 0) cout << -1;
    else cout << 0;
    
    return 0;
}

LL CCW(point p1, point p2, point p3) { return (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y); }