#pragma GCC optimize ("O3")
#pragma GCC optimize ("Ofast")
#pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef __int128_t LL;
typedef __uint128_t ULL;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
#define F first
#define S second
#define pb(x) push_back(x)
#define all(x) (x).begin(), (x).end()
#define each(x,a) for (auto &x : a)
#define rep(i,n) for (auto i = 0; i < (n); i++)
#define endl '\n'
const ll INF=INT64_MAX;

int board[5][5];
bool used[12];
bool done = false;

void bt(int c) {
    if (c == 0) {
        // Check

        /*
               1
            2  4  12 8
               10    6
               11 5  3  7
                     9

            5x5 배열 / 체크해야 할 것
            1. 가로 두 줄 / Start : (1, 0), (3, 1)
            2. 세로 두 줄 / Start : (0, 1), (1, 3)
            3. 대각 두 줄 / Start : (1, 0), (0, 1)
        */

        // 1. 가로 두 줄
        int sums = 0;
        rep(j,4) sums += board[1][j];
        if (sums != 26) return;

        sums = 0;
        rep(j,4) sums += board[3][j+1];
        if (sums != 26) return;

        // 2. 세로 두 줄
        sums = 0;
        rep(i,4) sums += board[i][1];
        if (sums != 26) return;

        sums = 0;
        rep(i,4) sums += board[i+1][3];
        if (sums != 26) return;

        // 3. 대각 두 줄
        sums = 0;
        rep(i,4) sums += board[i][i+1];
        if (sums != 26) return;

        sums = 0;
        rep(i,4) sums += board[i+1][i];
        if (sums != 26) return;

        done = true;
        return;
    }

    rep(i,5) {
        rep(j,5) {
            if (board[i][j] == -1) {
                rep(a,12) {
                    if (!used[a]) {
                        board[i][j] = a + 1;
                        used[a] = true;
                        bt(c-1);
                        if (done) return;
                        used[a] = false;
                        board[i][j] = -1;
                    }
                }
                return;
            }
        }
    }
}

int main() { fastio 
    // 3967 : 매직 스타

    int cnt = 0;
    rep(i,5) {
        string s; cin >> s;
        int jidx;
        if (i == 0 || i == 2 || i == 3) jidx = 1;
        else if (i == 1) jidx = 0;
        else if (i == 4) jidx = 3;

        rep(j,9) {
            if (s[j]!='.') {
                if ('A'<=s[j]&&s[j]<='L') {
                    board[i][jidx] = (s[j]-'A'+1);
                    used[s[j]-'A'] = true;
                }
                else {
                    board[i][jidx] = -1;
                    cnt += 1;
                }

                if (i == 1 || i == 3) jidx += 1;
                else if (i == 2) jidx += 2;
            }
        }
    }

    bt(cnt);

    cout << "...." << (char)(board[0][1]+'A'-1) << "...." << endl;
    rep(j,4) cout << "." << (char)(board[1][j]+'A'-1);
    cout << "." << endl << ".." << (char)(board[2][1]+'A'-1) << "..." << (char)(board[2][3]+'A'-1) << ".." << endl;
    rep(j,4) cout << "." << (char)(board[3][j+1]+'A'-1);
    cout << "." << endl << "...." << (char)(board[4][3]+'A'-1) << "...." << endl;

    return 0;
}