import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split())) 

dp = [[0 for _ in range(21)] for _ in range(101)]
dp[0][arr[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if j - arr[i] >= 0: dp[i][j - arr[i]] += dp[i-1][j]
        if j + arr[i] < 21: dp[i][j + arr[i]] += dp[i-1][j]

print(dp[n-2][arr[-1]])