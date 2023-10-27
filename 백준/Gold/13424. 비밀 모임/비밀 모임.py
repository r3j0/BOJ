import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    
    k = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))

    for i in range(1, n+1):
        graph[i][i] = 0

    for k in range(1, n+1):
        for ai in range(1, n+1):
            for bi in range(1, n+1):
                graph[ai][bi] = min(graph[ai][k] + graph[k][bi], graph[ai][bi])

    min_num = -1
    min_cost = float('inf')
    for i in range(1, n+1):
        sums = 0
        for now in arr:
            sums += graph[now][i]
        
        if min_cost > sums:
            min_cost = sums
            min_num = i
    
    print(min_num)