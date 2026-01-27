# 14925 : 목장 건설하기
import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(m)]

ans = 0
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if maps[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        else: dp[i][j] = 0

        ans = max(ans, dp[i][j])

print(ans)