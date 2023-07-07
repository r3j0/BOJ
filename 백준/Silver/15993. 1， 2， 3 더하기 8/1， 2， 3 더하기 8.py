dp = [[0, 0] for _ in range(100001)]
# 0 : 짝수
# 1 : 홀수
dp[1] = [0, 1]
dp[2] = [1, 1] # 1 + 1, 2
dp[3] = [2, 2] # 1 + 1 + 1, 1 + 2, 2 + 1, 3
for i in range(4, 100001):
    dp[i][0] = (dp[i-3][1] + dp[i-2][1] + dp[i-1][1]) % 1000000009 # 짝수
    dp[i][1] = (dp[i-3][0] + dp[i-2][0] + dp[i-1][0]) % 1000000009 # 홀수

import sys
input = sys.stdin.readline

test = int(input().rstrip())
for _ in range(test):
    n = int(input().rstrip())

    print(dp[n][1], dp[n][0])