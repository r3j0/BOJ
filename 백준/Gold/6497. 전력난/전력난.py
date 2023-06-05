import sys
import heapq
input = sys.stdin.readline

def prim(start):
    queue = []
    visit = [False] * (n+1)
    sumw = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cdi, cde = heapq.heappop(queue)
        if not visit[cde]:
            visit[cde] = True
            sumw += cdi
            for nde, ndi in graph[cde]:
                if not visit[nde]:
                    heapq.heappush(queue, (ndi, nde))
    
    return sumw

while True:
    n, m = map(int, input().rstrip().split())
    if n == 0 and m == 0: break

    graph = [[] for _ in range(n+1)]
    allsum = 0
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        if a == b: continue
        graph[a].append((b, c))
        graph[b].append((a, c))
        allsum += c

    print(allsum - prim(1))