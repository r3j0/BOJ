import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
backpack = [int(input().rstrip()) for _ in range(m)]

dp = [[0 for _ in range(max(backpack)+1)] for _ in range(n+1)]
for weight in range(1, max(backpack)+1):
    for thing in range(1, n+1):
        now_weight = arr[thing-1][0]
        now_value = arr[thing-1][1]

        if weight >= now_weight: dp[thing][weight] = max(dp[thing-1][weight], dp[thing-1][weight-now_weight]+now_value)
        else: dp[thing][weight] = dp[thing-1][weight]

max_eff = 0
max_num = 0

for i in range(m):
    if max_eff < dp[n][backpack[i]] / backpack[i]:
        max_eff = dp[n][backpack[i]] / backpack[i]
        max_num = i
print(max_num + 1)