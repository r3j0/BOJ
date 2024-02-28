dp = [0 for _ in range(68)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 68):
    dp[i] = dp[i-4] + dp[i-3] + dp[i-2] + dp[i-1]

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(dp[n])