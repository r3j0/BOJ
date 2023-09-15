import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
go_graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
back_graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    go_graph[a][b] = 1
    back_graph[b][a] = 1

for i in range(n+1):
    go_graph[i][i] = 0
    back_graph[i][i] = 0


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            go_graph[a][b] = min(go_graph[a][b], go_graph[a][k] + go_graph[k][b])
            back_graph[a][b] = min(back_graph[a][b], back_graph[a][k] + back_graph[k][b])

s = int(input())
for _ in range(s):
    a, b = map(int, input().rstrip().split())
    if go_graph[a][b] == back_graph[a][b] == float('inf'): print(0)
    elif go_graph[a][b] != float('inf'): print(-1)
    else: print(1)