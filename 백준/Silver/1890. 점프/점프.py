import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0 for j in range(n)] for i in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or maps[i][j] == 0: continue
        if j+maps[i][j] < n: dp[i][j+maps[i][j]] += dp[i][j]
        if i+maps[i][j] < n: dp[i+maps[i][j]][j] += dp[i][j]

print(dp[n-1][n-1])