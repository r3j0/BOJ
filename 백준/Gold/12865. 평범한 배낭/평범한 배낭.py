import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
thing = []
for _ in range(n): thing.append(list(map(int, input().rstrip().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for weight_limit in range(1, k+1):
    for things in range(1, n+1):
        weight = thing[things - 1][0]
        value = thing[things - 1][1]

        if weight <= weight_limit:
            dp[things][weight_limit] = max(dp[things-1][weight_limit], dp[things-1][weight_limit - weight]+value)
        else:
            dp[things][weight_limit] = dp[things-1][weight_limit]

print(dp[n][k])