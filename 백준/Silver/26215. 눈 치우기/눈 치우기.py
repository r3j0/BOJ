import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
queue = []
res = 0
for a in arr:
    heapq.heappush(queue, -a)

while queue:
    if len(queue) > 1:
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)

        now = min(-a, -b)
        res += now
        a += now
        b += now
        if a != 0: heapq.heappush(queue, a)
        if b != 0: heapq.heappush(queue, b)
    else:
        res -= heapq.heappop(queue)
print(res if res <= 1440 else -1)