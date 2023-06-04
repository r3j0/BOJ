import sys
import heapq
input = sys.stdin.readline

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

def dijkstra():
    global maps
    global row
    global col
    global n

    distances = [[int(1e6) for _ in range(n)] for _ in range(n)]
    distances[0][0] = maps[0][0]
    queue = []
    heapq.heappush(queue, (distances[0][0], 0, 0))

    while queue:
        cdi, cdy, cdx = heapq.heappop(queue)

        if cdi > distances[cdy][cdx]: continue

        for d in range(4):
            ndy = cdy + row[d]
            ndx = cdx + col[d]
            if 0 <= ndy < n and 0 <= ndx < n:
                di = cdi + maps[ndy][ndx]
                if di < distances[ndy][ndx]:
                    distances[ndy][ndx] = di
                    heapq.heappush(queue, (di, ndy, ndx))
    
    return distances

problem = 1
while True:
    n = int(input().rstrip())
    if n == 0: break

    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

    result = dijkstra()
    print('Problem %d: %d'%(problem, result[n-1][n-1]))
    problem += 1