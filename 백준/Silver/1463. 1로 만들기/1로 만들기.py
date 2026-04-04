import sys
input = sys.stdin.readline

# 1463 : 1로 만들기
n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(n-1, 0, -1):
    dp[i] = dp[i+1] + 1
    if i * 2 <= n: dp[i] = min(dp[i], dp[i*2]+1)
    if i * 3 <= n: dp[i] = min(dp[i], dp[i*3]+1)

print(dp[1])