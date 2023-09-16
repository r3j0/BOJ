import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
m = int(input().rstrip())

if m == 1: print(0)
else:
    dp = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = 0

    for weight in range(1, m+1):
        for thing in range(1, n+1):
            now_weight = arr[thing-1][0] - 1
            now_value = arr[thing-1][1]

            if weight == now_weight:
                dp[thing][weight] = min(dp[thing-1][weight], dp[thing-1][weight-now_weight] + now_value)
            elif weight > (now_weight - 1):
                dp[thing][weight] = min(dp[thing-1][weight], dp[thing-1][weight-(now_weight - 1)] + now_value)
            else:
                dp[thing][weight] = dp[thing-1][weight]

    print(dp[n][m] if dp[n][m] != float('inf') else -1)