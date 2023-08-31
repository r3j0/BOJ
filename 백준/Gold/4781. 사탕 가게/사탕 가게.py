import sys
input = sys.stdin.readline

dp = [0 for _ in range(10001)]
while True:
    n, m = input().rstrip().split()
    n = int(n)
    m = int(m[:m.index('.')] + m[m.index('.')+1:])
    if n == m == 0: break
    arr = []
    for _ in range(n):
        c, p = input().rstrip().split()
        arr.append([int(c), int(p[:p.index('.')] + p[p.index('.')+1:])])
    dp[0] = 0    
    for moneylimit in range(1, m+1):
        dp[moneylimit] = 0
        for thing in range(1, n+1):
            if moneylimit >= arr[thing-1][1]:
                dp[moneylimit] = max(dp[moneylimit], dp[moneylimit-1], dp[moneylimit - arr[thing-1][1]] + arr[thing-1][0])
            else:
                dp[moneylimit] = max(dp[moneylimit], dp[moneylimit-1])
    
    print(dp[m])
