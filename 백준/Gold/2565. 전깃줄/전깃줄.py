import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
order = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    heapq.heappush(order, (a, b))

arr = []
for _ in range(n):
    res = heapq.heappop(order)
    arr.append(res[1])


dp_a = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp_a[i] < dp_a[j]:
            dp_a[i] = dp_a[j]
    dp_a[i] += 1

print(n-max(dp_a))