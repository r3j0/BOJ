import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
queue = []
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 0:
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(-1)
    else:
        for i in range(1, len(arr)):
            heapq.heappush(queue, -arr[i])

    