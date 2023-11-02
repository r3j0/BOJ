import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): graph[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_dist = 0
for j in range(1, n+1):
    min_dist += graph[1][j]
min_num = 1

for i in range(2, n+1):
    now_dist = 0
    for j in range(1, n+1):
        now_dist += graph[i][j]
    
    if min_dist > now_dist:
        min_dist = now_dist
        min_num = i
        
print(min_num)