# -5 -5
# -4 3
# -3 2
# -2 -1
# -1 1
# 0 0
# 1 1
# 2 1
# 3 2
# 4 3

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 1
for i in range(3, 1000001): dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

import sys
input = sys.stdin.readline

n = int(input())

if n > 0: 
    print(1)
    print(dp[n])
elif n == 0:
    print(0)
    print(0)
else:
    if abs(n) % 2 == 0: print(-1)
    else: print(1)
    print(dp[abs(n)])