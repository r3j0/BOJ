# 11000 : 강의실 배정
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[0], x[1]))
pq = []
heapq.heappush(pq, arr[0][1])
for i in range(1, n):
    if pq[0] <= arr[i][0]:
        heapq.heappop(pq)
    heapq.heappush(pq, arr[i][1])

print(len(pq))