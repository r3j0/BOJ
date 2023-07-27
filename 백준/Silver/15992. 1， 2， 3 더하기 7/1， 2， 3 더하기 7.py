# dp[i][j] i 수를 만듬. j 개의 수를 사용함
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4, 1001):
    # Use 1 in [3]
    for j in range(1, i):
        dp[i][j+1] += dp[i-1][j]
    
    # Use 2 in [2]
    for j in range(1, i):
        dp[i][j+1] += dp[i-2][j]

    # Use 3 in [1]
    for j in range(1, i):
        dp[i][j+1] += dp[i-3][j]
        dp[i][j+1] %= 1000000009

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    print(dp[n][m])