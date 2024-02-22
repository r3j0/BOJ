import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
queue = [[] for _ in range(12)]
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    heapq.heappush(queue[a], -b)

res = 0
for _ in range(k):
    for i in range(1, 12):
        if len(queue[i]) == 0: continue
        now = heapq.heappop(queue[i])
        now *= -1
        if now != 0:
            now -= 1
        heapq.heappush(queue[i], -now)
    
    res = 0
    for i in range(1, 12):
        if len(queue[i]) == 0: continue
        now = heapq.heappop(queue[i])
        res -= now
        heapq.heappush(queue[i], now)

print(res) 