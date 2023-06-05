import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if a == b: continue
    graph[a].append((b, c))
    graph[b].append((a, c))

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


print(prim(1))