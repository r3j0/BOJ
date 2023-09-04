import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().rstrip())

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            now = arr[j-1]

            if i >= now:
                dp[j][i] += dp[j-1][i] + dp[j][i-now] + (1 if i - now == 0 else 0)
            else:
                dp[j][i] += dp[j-1][i]
    
    print(dp[n][m])