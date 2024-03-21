import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(max(6, n+1))]
dp[2] = 1
dp[3] = 2
dp[4] = 9 
dp[5] = 44
for i in range(6, n+1):
    dp[i] = ((dp[i-1] + dp[i-2]) * (i - 1)) % 1000000000
print(dp[n])