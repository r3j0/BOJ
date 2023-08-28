import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

for weight in range(1, t+1):
    for thing in range(1, n+1):
        now_weight = arr[thing-1][0]
        now_value = arr[thing-1][1]

        if now_weight <= weight:
            dp[thing][weight] = max(dp[thing-1][weight], dp[thing-1][weight-now_weight] + now_value)
        else:
            dp[thing][weight] = dp[thing-1][weight]

print(dp[thing][weight])