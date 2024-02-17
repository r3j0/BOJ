# 50000 의 제곱근은 223.6
# 225까지 DP

import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, int(i**0.5)+1):
        if i - j**2 >= 0 and (i - j**2 == 0 or dp[i - j**2] > 0):
            if dp[i] == 0: dp[i] = dp[i - j**2] + 1
            else: dp[i] = min(dp[i], dp[i - j**2] + 1)
print(dp[n])