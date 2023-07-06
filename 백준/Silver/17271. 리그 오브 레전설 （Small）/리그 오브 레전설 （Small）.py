import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

if n < m:
    print(1)
elif n == m:
    print(2)
else:
    dp = [0 for _ in range(n+1)]

    for i in range(1, m): dp[i] = 1
    dp[m] = 2
    for i in range(m+1, n+1): dp[i] = (dp[i-m] + dp[i-1]) % 1000000007

    print(dp[n])

