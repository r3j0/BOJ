import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
queue = []
now = int(input().rstrip())
for _ in range(n-1):
    heapq.heappush(queue, -int(input().rstrip()))

cnt = 0
while len(queue) > 0 and now <= -queue[0]:
    go = -queue[0]
    heapq.heappop(queue)
    now += 1
    heapq.heappush(queue, -go + 1)

    cnt += 1

print(cnt)