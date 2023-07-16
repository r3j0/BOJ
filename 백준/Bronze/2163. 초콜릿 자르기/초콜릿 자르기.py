import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
queue = []

heapq.heappush(queue, (n, m))
result = 0
while queue:
    now_n, now_m = heapq.heappop(queue)
    if now_n == 1 and now_m == 1: continue
    result += 1
    if now_n == 1 or now_m == 1:
        if now_n == 1:
            gone = now_m // 2
            heapq.heappush(queue, (now_n, gone))
            heapq.heappush(queue, (now_n, now_m - gone))
        else:
            gone = now_n // 2
            heapq.heappush(queue, (gone, now_m))
            heapq.heappush(queue, (now_n - gone, now_m))
    else:
        if now_n > now_m:
            gone = now_n // 2
            heapq.heappush(queue, (gone, now_m))
            heapq.heappush(queue, (now_n - gone, now_m))
        else:
            gone = now_m // 2
            heapq.heappush(queue, (now_n, gone))
            heapq.heappush(queue, (now_n, now_m - gone))

print(result)