def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    pud = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in puddles:
        pud[y-1][x-1] = 1
    
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i > 0 and pud[i-1][j] == 0:
                dp[i][j] += dp[i-1][j]
            if j > 0 and pud[i][j-1] == 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    
    answer = dp[n-1][m-1]
    return answer