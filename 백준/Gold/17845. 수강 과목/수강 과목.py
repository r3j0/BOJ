import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(k)]

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for time_limit in range(1, n+1):
    for thing in range(1, k+1):
        now_time = arr[thing-1][1]
        now_value = arr[thing-1][0]

        if time_limit >= now_time:
            dp[thing][time_limit] = max(dp[thing - 1][time_limit], dp[thing - 1][time_limit - now_time] + now_value)
        else:
            dp[thing][time_limit] = dp[thing - 1][time_limit]

print(dp[k][n])