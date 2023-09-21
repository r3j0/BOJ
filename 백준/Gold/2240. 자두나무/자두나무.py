import sys
input = sys.stdin.readline

t, w = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(t)]

# dp[i][j][k] : i 번 자두나무 아래에서 / j 번 자두까지 먹고 / k 번 이동했을 때
dp = [[[0 for _ in range(w+2)] for _ in range(t+1)] for _ in range(3)]
for i in range(1, t+1):
    for j in range(1, w+2):
        dp[1][i][j] = max(dp[1][i-1][j] + (1 if arr[i-1] == 1 else 0), dp[2][i-1][j-1] + (1 if arr[i-1] == 1 else 0))
        if i != 1 or j != 1: dp[2][i][j] = max(dp[2][i-1][j] + (1 if arr[i-1] == 2 else 0), dp[1][i-1][j-1] + (1 if arr[i-1] == 2 else 0))

res = 0
for i in range(1, w+2):
    res = max(res, dp[1][t][i], dp[2][t][i])
print(res)