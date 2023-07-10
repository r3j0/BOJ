import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]

dp[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0]) % 10007
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % 10007
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 10007
    dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % 10007
    dp[i][4] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % 10007
    dp[i][5] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5]) % 10007
    dp[i][6] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][6]) % 10007
    dp[i][7] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][6] + dp[i-1][7]) % 10007
    dp[i][8] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][6] + dp[i-1][7] + dp[i-1][8]) % 10007
    dp[i][9] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][6] + dp[i-1][7] + dp[i-1][8] + dp[i-1][9]) % 10007

print(sum(dp[n]) % 10007)