import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(max(3, n+1))]
dp[1] = 2
dp[2] = 6
for i in range(3, n+1):
    dp[i] = ((dp[i-2]*2) + (dp[i-1] - dp[i-2]) + dp[i-1] + 2) % 9901
print(dp[n]+1)