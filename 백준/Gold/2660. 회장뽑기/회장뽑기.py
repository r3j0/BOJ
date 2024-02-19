import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

while True:
    a, b = map(int, input().rstrip().split())
    if a == -1 and b == -1: break
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
max_value = 51
max_arr = []
for i in range(1, n+1):
    now_value = 0
    for j in range(1, n+1):
        if graph[i][j] != float('inf'):
            now_value = max(now_value, graph[i][j])
    
    if max_value > now_value:
        max_value = now_value
        max_arr = [i]
    elif max_value == now_value:
        max_arr.append(i)

print(max_value, len(max_arr))
print(' '.join(map(str, max_arr)))