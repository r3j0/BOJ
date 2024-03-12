import sys
input = sys.stdin.readline

n = int(input().rstrip())
cost = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(2**n)]
def dfs(now, vis):
    if vis == (1 << n) - 1:
        if cost[now][0] != 0: return cost[now][0]
        else: return float('inf')
        
    if dp[vis][now] != -1: return dp[vis][now]
    dp[vis][now] = float('inf')
    
    for i in range(1, n):
        if vis & (1 << i) == 0 and cost[now][i] != 0:
            dp[vis][now] = min(dp[vis][now], dfs(i, vis|(1<<i)) + cost[now][i])

    return dp[vis][now]

print(dfs(0, 1))