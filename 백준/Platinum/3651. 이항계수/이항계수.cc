// 3651 : 이항계수
#include <iostream>
#include <vector>
#include <algorithm>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
typedef long long LL;
using namespace std;

vector<vector<LL>> answer;
LL comb(LL n, LL k, LL m) {
    // 이항 계수를 다른 방식으로 구한다?
    // (n - k + i) / i
    LL res = 1;
    for (int i = 1; i <= k; i++) {
        res = (res * (n - k + i)) / i;
        if (res < 0 || res > m) return m + 1;
    }
    return res;
}

int main() {
    fastio
    LL m; cin >> m;

    // 1. (n k) = m 이라고 한다면, k는 어차피 m 이하이다. (15 1, 15 14)
    // 2. k를 지정해서 1부터 시작하자. (m 1) (m 14) 이런 식으로 나와야 한다.
    // 3. 그에 맞는 n을 찾아야 하는데, 파라매트릭처럼 이분탐색으로 mid마다 조합을 구해보자.
    //    시작점 : 절반은 안 봐도 되니, 2k부터 시작한다.
    //    끝점  : m+1
    // 4. 우리가 k에서 볼 최소 이항 계수는 (2k, k) 니까, 이게 m보다 커지면 종료
    // 5. 정답 정렬 후 출력

    // + m = 1 예외 케이스
    if (m == 1) {
        cout << 1 << '\n' << "1 1";
        return 0;
    }

    for (LL k = 1; comb(2*k, k, m) <= m; k++) {
        LL start = 2 * k;
        LL end = m + 1;
        while (start <= end) {
            LL mid = (start + end) / 2;
            LL now = comb(mid, k, m);

            if (now == m) {
                vector<LL> a1 = {mid, k};
                answer.push_back(a1);
                if (mid - k != k) {
                    vector<LL> a2 = {mid, mid-k};
                    answer.push_back(a2);
                }
                break;
            }

            if (now < m) start = mid + 1;
            else end = mid - 1;
        }
    }

    cout << answer.size() << '\n';
    sort(answer.begin(), answer.end());
    for (int i = 0; i < answer.size(); i++)
        cout << answer[i][0] << ' ' << answer[i][1] << '\n';

    return 0;
}
