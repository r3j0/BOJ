import sys
input = sys.stdin.readline

n, h = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(n+1)] for _ in range(50000)]

done = 0
cost = 1
while True:
    for thing in range(1, n+1):
        now_cost = arr[thing-1][1]
        now_value = arr[thing-1][0]

        if cost >= now_cost:
            dp[cost][thing] = max([(dp[cost-now_cost][thing - 1] + now_value) if cost == now_cost or dp[cost-now_cost][thing - 1] > 0 else 0, (dp[cost-now_cost][thing] + now_value) if cost == now_cost or dp[cost-now_cost][thing] > 0 else 0, dp[cost][thing-1]])
        else:
            dp[cost][thing] = dp[cost][thing-1]
        
        if max(dp[cost]) >= h:
            print(cost)
            done = 1
            break
    if done == 1: break
    cost += 1