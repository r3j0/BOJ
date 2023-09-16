import sys 
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
sum_value = sum([arr[i][1] for i in range(n)])

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for weight_limit in range(1, t+1):
    for thing in range(1, n+1):
        now_weight = arr[thing-1][0]
        now_value = arr[thing-1][1]

        if weight_limit >= now_weight:
            dp[thing][weight_limit] = max(dp[thing-1][weight_limit], dp[thing-1][weight_limit - now_weight] + now_value)
        else:
            dp[thing][weight_limit] = dp[thing-1][weight_limit]

print(sum_value - dp[n][t])