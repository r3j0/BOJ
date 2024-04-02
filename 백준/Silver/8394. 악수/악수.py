import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(max(3, n+1))]
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10
print(dp[n])