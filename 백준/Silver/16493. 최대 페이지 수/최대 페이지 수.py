import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for limit in range(1, n+1):
    for thing in range(1, m+1):
        now_weight = arr[thing-1][0]
        now_value = arr[thing-1][1]
        
        if limit >= now_weight:
            dp[thing][limit] = max(dp[thing-1][limit], dp[thing-1][limit - now_weight] + now_value)
        else:
            dp[thing][limit] = dp[thing - 1][limit]

print(dp[m][n])