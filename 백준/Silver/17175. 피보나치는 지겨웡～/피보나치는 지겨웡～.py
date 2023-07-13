import sys
input = sys.stdin.readline

n = int(input())
dp = [1 for _ in range(51)] 
for i in range(2, n+1):
    dp[i] += dp[i-2] + dp[i-1]
    dp[i] %= 1000000007

print(dp[n])