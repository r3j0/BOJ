import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[[float('inf'), -1] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b][0] = min(graph[a][b][0], c)

for i in range(1, n+1): graph[i][i][0] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b][0] > graph[a][k][0] + graph[k][b][0]:
                graph[a][b][0] = graph[a][k][0] + graph[k][b][0]
                graph[a][b][1] = k

for i in range(n): 
    for j in range(n):
        print(graph[i+1][j+1][0] if graph[i+1][j+1][0] != float('inf') else 0, end=' ')
    print()

def findPath(start, end):
    arr = [start]
    if graph[start][end][1] != -1:
        arr.extend(findPath(start, graph[start][end][1])[1:])
        arr.extend(findPath(graph[start][end][1], end)[1:])
    else:
        arr.append(end)
    return arr

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or graph[i][j][0] == float('inf'): print(0)
        else:
            result = findPath(i, j)
            print(len(result), ' '.join(map(str, result)))