import sys
input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
if k == 0:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print(dp[n-1][m-1])
else:
    row1 = (k - 1) // m + 1
    col1 = (k - 1) % m + 1

    row2 = (n) - row1 + 1
    col2 = (m) - col1 + 1

    dp = [[0 for _ in range(col1)] for _ in range(row1)]
    dp[0][0] = 1
    for i in range(row1):
        for j in range(col1):
            if i == 0 and j == 0: continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    res = dp[row1-1][col1-1]
    dp = [[0 for _ in range(col2)] for _ in range(row2)]
    dp[0][0] = 1
    for i in range(row2):
        for j in range(col2):
            if i == 0 and j == 0: continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    res *= dp[row2-1][col2-1]
    print(res)