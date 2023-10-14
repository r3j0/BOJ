import sys
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_item = 0
for start in range(1, n+1):
    now_item = 0
    for end in range(1, n+1):
        if graph[start][end] <= m:
            now_item += arr[end-1]
    max_item = max(max_item, now_item)

print(max_item)