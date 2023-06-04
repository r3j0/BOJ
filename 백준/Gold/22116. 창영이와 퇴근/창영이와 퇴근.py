import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

def dijkstra():
    distances = [[int(1e9) for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0
    queue = []
    heapq.heappush(queue, (distances[0][0], 0, 0))

    while queue:
        cdi, cdy, cdx = heapq.heappop(queue)

        if distances[cdy][cdx] < cdi: continue

        for d in range(4):
            ndy = cdy + row[d]
            ndx = cdx + col[d]
            if 0 <= ndy < n and 0 <= ndx < n:
                ndi = abs(maps[cdy][cdx] - maps[ndy][ndx])
                di = max(cdi, ndi)
                if di < distances[ndy][ndx]:
                    distances[ndy][ndx] = di
                    heapq.heappush(queue, (di, ndy, ndx))
    
    return distances

result = dijkstra()
print(result[n-1][n-1])