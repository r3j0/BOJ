import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arrC = list(map(int, input().rstrip().split()))
arrW = list(map(int, input().rstrip().split()))

queue = []
for a in arrC: heapq.heappush(queue, -a)

done = 1
for a in arrW:
    if len(queue) == 0: 
        done = 0
        break
    now = -1 * heapq.heappop(queue)
    aq = []
    while queue and now < a: 
        aq.append(-now)
        now = -1 * heapq.heappop(queue)
    
    if now > a: heapq.heappush(queue, (now - a) * -1)
    elif now < a and len(queue) == 0: 
        done = 0
        break
    for i in aq: heapq.heappush(-i)

print(done)