import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        now = [0]
        if i-1 >= 0: now.append(dp[i-1][j])
        if j-1 >= 0: now.append(dp[i][j-1])
        if i-1 >= 0 and j-1 >= 0: now.append(dp[i-1][j-1])

        dp[i][j] = max(now) + maps[i][j]

print(dp[n-1][m-1])