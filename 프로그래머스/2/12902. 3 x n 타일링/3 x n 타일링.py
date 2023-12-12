def solution(n):
    answer = 0
    dp = [0 for _ in range(5001)]
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = (dp[i-2] * 3)
        for j in range(0, i-2, 2):
            dp[i] += dp[j] * 2
        dp[i] %= 1000000007
    answer = dp[n]
    return answer