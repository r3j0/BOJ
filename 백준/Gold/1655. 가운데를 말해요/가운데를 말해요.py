import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

min_heap = []
max_heap = []

for a in arr:
    if len(min_heap) == 0: heapq.heappush(min_heap, -a)
    else:
        if (len(max_heap) != 0 and -min_heap[0] <= a <= max_heap[0]) or -min_heap[0] > a: heapq.heappush(min_heap, -a)
        else: heapq.heappush(max_heap, a)

        while abs(len(min_heap) - len(max_heap)) > 1:
            if len(min_heap) > len(max_heap): heapq.heappush(max_heap, -heapq.heappop(min_heap))
            else: heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    if (len(min_heap) + len(max_heap)) % 2 == 0:
        print(-min_heap[0])
    else:
        if len(max_heap) > len(min_heap): print(max_heap[0])
        else: print(-min_heap[0])