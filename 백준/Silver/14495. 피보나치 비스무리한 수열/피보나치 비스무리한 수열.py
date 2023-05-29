import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
if n >= 2: dp[2] = 1
if n >= 3: dp[3] = 1

for i in range(4, n + 1): dp[i] = dp[i - 3] + dp[i - 1]

print(dp[n])