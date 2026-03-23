// 10090 : Counting Inversions
#include <iostream>
#define fastio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
#define MAX 1000000
using namespace std;
typedef long long LL;

LL ans = 0;
int arr[MAX];
int tmp[MAX];

void merge(int start, int end) {
    int leftidx = start;
    int mid = (start + end) / 2;
    int rightidx = mid + 1;
    int allidx = start;

    while (leftidx <= mid && rightidx <= end) {
        if (arr[leftidx] > arr[rightidx]) {
            ans += (LL)(mid - leftidx + 1);
            tmp[allidx++] = arr[rightidx++];
        }
        else {
            tmp[allidx++] = arr[leftidx++];
        }
    }

    while (leftidx <= mid) {
        tmp[allidx++] = arr[leftidx++];
    }
    while (rightidx <= end) {
        tmp[allidx++] = arr[rightidx++];
    }

    for (int i = start; i <= end; i++) {
        arr[i] = tmp[i];
    }
}

void solve(int start, int end) {
    if (start >= end) return;
    int mid = (start + end) / 2;
    solve(start, mid);
    solve(mid + 1, end);
    merge(start, end);
}

int main() {
    fastio
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    solve(0, n - 1);

    cout << ans;
    return 0;
}