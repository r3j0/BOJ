import sys
import heapq
input = sys.stdin.readline

def prim(start):
    queue = []
    visit = [False] * (n+1)
    available = 0
    sumw = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cdi, cde = heapq.heappop(queue)
        if not visit[cde]:
            visit[cde] = True
            available += 1
            sumw += cdi
            for nde, ndi in graph[cde]:
                if types[cde-1] != types[nde-1] and not visit[nde]:
                    heapq.heappush(queue, (ndi, nde))
    if available == n:
        return sumw
    else:
        return -1

n, m = map(int, input().rstrip().split())
types = list(input().rstrip().split())

graph = [[] for _ in range(n+1)]
allsum = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if a == b: continue
    graph[a].append((b, c))
    graph[b].append((a, c))
    allsum += c

print(prim(1))