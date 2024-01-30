import sys
input = sys.stdin.readline

MOD = 1000000009

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
dp = [[1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0: continue

        if j > 0 and maps[i][j-1] in ['E', 'B']: dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
        if i > 0 and maps[i-1][j] in ['S', 'B']: dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD

print(dp[n-1][m-1])