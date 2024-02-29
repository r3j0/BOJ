import sys
import heapq
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    r, c = map(int, input().rstrip().split())
    graph = [{} for _ in range(r*c)]
    edges = []
    for i in range(r):
        arr = list(map(int, input().rstrip().split()))
        for j in range(c-1):
            graph[i*c+j][i*c+j+1] = arr[j]
            graph[i*c+j+1][i*c+j] = arr[j]

            heapq.heappush(edges, [arr[j], i*c+j, i*c+j+1])
    for i in range(r-1):
        arr = list(map(int, input().rstrip().split()))
        for j in range(c):
            graph[i*c+j][(i+1)*c+j] = arr[j]
            graph[(i+1)*c+j][i*c+j] = arr[j]

            heapq.heappush(edges, [arr[j], i*c+j, (i+1)*c+j])
    
    par = [i for i in range(r*c)]
    def parent(now):
        if now != par[now]:
            par[now] = parent(par[now])
        return par[now]

    def union(a, b):
        a = parent(a)
        b = parent(b)

        if a < b: par[b] = a
        else: par[a] = b
    
    res = 0
    while edges:
        now = heapq.heappop(edges)
        if parent(now[1]) != parent(now[2]):
            union(now[1], now[2])
            res += now[0]
    
    print(res)