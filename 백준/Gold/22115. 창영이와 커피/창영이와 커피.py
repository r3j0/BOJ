import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, k+1):
    dp[0][i] = float('inf')

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= arr[i-1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j - arr[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k] if dp[n][k] != float('inf') else -1)