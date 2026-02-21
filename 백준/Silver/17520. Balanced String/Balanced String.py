n = int(input())
dp = [[0, 0] for _ in range(n+1)]
dp[1] = [1, 1]
MOD = 16769023
for i in range(2, n+1):
    if i % 2 == 0:
        dp[i] = [sum(dp[i-1]) % MOD, 0]
    else:
        dp[i] = [dp[i-1][0], dp[i-1][0]]

print(sum(dp[n]) % MOD)