import sys
input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
for i in range(n+1): dp[i][0][0] = 0

for burger in range(1, m+1):
    for potato in range(1, k+1):
        for thing in range(1, n+1):
            now_burger = arr[thing-1][0]
            now_potato = arr[thing-1][1]

            if burger >= now_burger and potato >= now_potato:
                dp[thing][burger][potato] = max(dp[thing - 1][burger][potato], dp[thing - 1][burger - now_burger][potato - now_potato] + 1)
            else:
                dp[thing][burger][potato] = dp[thing - 1][burger][potato]

print(dp[n][m][k])