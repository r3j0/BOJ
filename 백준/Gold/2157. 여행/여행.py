import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
graph = [{} for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, input().rstrip().split())
    if a > b: continue
    if graph[b].get(a, -1) == -1: graph[b][a] = c
    else: graph[b][a] = max(graph[b][a], c)

dp = [[-1 for _ in range(m)] for _ in range(n+1)]
dp[1][0] = 0
for i in range(2, n+1):
    for j in range(m-1):
        for k, v in graph[i].items():
            if dp[k][j] != -1:
                dp[i][j+1] = max(dp[i][j+1], dp[k][j] + v)

print(max(dp[n]))