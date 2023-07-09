import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j] = maps[i][j]
        # left
        if j != 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + maps[i][j])
        # up
        if i != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + maps[i][j])

print(dp[n-1][m-1])