import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

queue = []
for a in arr: heapq.heappush(queue, a)

cost = 0
while len(queue) != 1:
    first = heapq.heappop(queue)
    second = heapq.heappop(queue)
    cost += first + second
    heapq.heappush(queue, first + second)

print(cost)