# dp[i] = i 번쨰 자리 개수
dp = [[0 for _ in range(10)] for _ in range(65)]
for i in range(1, 65):
    if i == 1:
        for j in range(10): dp[i][j] = 1
    else:
        for j in range(10):
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(sum(dp[n]))