dp = [0 for _ in range(10001)]
dp[0] = 1

now = [1, 2, 3]
for k in now:
    for i in range(k, 10001):
        dp[i] += dp[i-k]

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(dp[n])