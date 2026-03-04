# 14728 : 벼락치기
import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for weight in range(1, t+1):
    for thing in range(1, n+1):
        if arr[thing-1][0] <= weight:
            dp[thing][weight] = max(dp[thing-1][weight], dp[thing-1][weight - arr[thing-1][0]] + arr[thing-1][1])
        else:
            dp[thing][weight] = dp[thing-1][weight]

print(dp[n][t])