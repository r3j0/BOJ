import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n): arr.append(int(input().rstrip()))

dp = [[] for _ in range(n)]
# 이전거 마심 / 이전거 안마심
maxv = arr[0]
dp[0] = [arr[0], 0]
if n >= 2: 
    dp[1] = [arr[0] + arr[1], arr[1]]
    maxv = max(maxv, max(dp[1]))
if n >= 3: 
    dp[2] = [arr[1] + arr[2], arr[0] + arr[2]]
    maxv = max(maxv, max(dp[2]))
for i in range(3, n):
    dp[i] = [dp[i-1][1] + arr[i], max(dp[i-3][0], dp[i-3][1], dp[i-2][0], dp[i-2][1]) + arr[i]]
    maxv = max(maxv, max(dp[i]))

print(maxv)