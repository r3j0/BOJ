# 12849 : 본대 산책
import sys
input = sys.stdin.readline

dp = [0 for _ in range(8)]
dp[0] = 1
MOD = 1000000007

d = int(input().rstrip())
for _ in range(d):
    dp = [(dp[1] + dp[2]) % MOD, (dp[0] + dp[2] + dp[3]) % MOD, (dp[0] + dp[1] + dp[3] + dp[4]) % MOD, (dp[1] + dp[2] + dp[4] + dp[5]) % MOD, (dp[2] + dp[3] + dp[5] + dp[6]) % MOD, (dp[3] + dp[4] + dp[7]) % MOD, (dp[4] + dp[7]) % MOD, (dp[5] + dp[6]) % MOD]

print(dp[0])