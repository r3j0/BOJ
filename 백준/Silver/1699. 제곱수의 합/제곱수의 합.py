import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [i for i in range(n+1)]
for i in range(4, n+1):
    j = 2
    while j**2 <= i:
        dp[i] = min(dp[i], dp[i-(j**2)] + 1)
        j += 1

print(dp[n])