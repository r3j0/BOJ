dp = [0 for _ in range(11)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

import sys
input = sys.stdin.readline

test = int(input().rstrip())
for _ in range(test):
    n = int(input().rstrip())
    print(dp[n])