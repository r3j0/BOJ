dp = [0 for _ in range(491)]
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3
for i in range(5, 491):
    dp[i] = dp[i-2] + dp[i-1]

while True:
    n = int(input())
    if n == -1: break
    print("Hour %d: %d cow(s) affected"%(n,dp[n]))