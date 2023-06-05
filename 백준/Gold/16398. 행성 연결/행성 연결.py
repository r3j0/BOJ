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
                if not visit[nde]:
                    heapq.heappush(queue, (ndi, nde))
    if available == n:
        return sumw
    else:
        return -1

n= int(input().rstrip())

graph = [[] for _ in range(n+1)]
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 0: continue
        graph[i].append((j, maps[i][j]))

print(prim(1))