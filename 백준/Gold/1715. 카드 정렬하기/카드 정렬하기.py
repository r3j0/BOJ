# 1715 : 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

q = []
for i in range(n): heapq.heappush(q, arr[i])

ans = 0
while len(q) > 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    heapq.heappush(q, first + second)
    ans += first + second

print(ans)