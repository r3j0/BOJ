import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
# 가로, 세로, 대각선

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0: continue
        if arr[i][j] == 1: continue
        if j > 0: dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2] # 가로, 대각선 -> 가로
        if i > 0: dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2] # 세로, 대각선 -> 세로
        if i > 0 and j > 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0: dp[i][j][2] += sum(dp[i-1][j-1]) # 가로, 세로, 대각선 -> 대각선
            
print(sum(dp[n-1][n-1]))