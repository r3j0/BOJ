import sys
import heapq
input = sys.stdin.readline

n, p = map(int, input().rstrip().split())
arrA = list(map(int, input().rstrip().split()))
arrB = list(map(int, input().rstrip().split()))

countA = [0 for _ in range(1024)]
countB = [0 for _ in range(1024)]
sumA = 0
sumB = 0

for a in arrA: 
    countA[a] += 1
    sumA += a
    
for b in arrB: 
    countB[b] += 1
    sumB += b

queue = []

for i in range(1024):
    for j in range(1024):
        if countA[i] > 0 and countB[j] > 0: heapq.heappush(queue, (i & j, countA[i] * countB[j]))

result = (n * (sumA + sumB))
now = n * n - p
while queue:
    value, count = heapq.heappop(queue)
    if now <= 0: 
        result -= value * count
    else:
        result -= 2 * value * count
        now -= count

        if now < 0: 
            result -= 2 * value * now
            result += value * now

print(result)