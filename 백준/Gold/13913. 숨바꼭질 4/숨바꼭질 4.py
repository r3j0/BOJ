import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

arr = [[-1, -1] for _ in range(100001)]
arr[n][0] = 0
arr[n][1] = -10

queue = deque()
queue.append(n)

while queue:
    now = queue.popleft()
    if now == k: break

    if now > 0 and (arr[now-1][0] == -1 or arr[now-1][0] > arr[now][0] + 1):
        arr[now-1][0] = arr[now][0] + 1
        arr[now-1][1] = now
        queue.append(now-1)
    if now < 100000 and (arr[now+1][0] == -1 or arr[now+1][0] > arr[now][0] + 1):
        arr[now+1][0] = arr[now][0] + 1
        arr[now+1][1] = now
        queue.append(now+1)
    if now * 2 <= 100000 and (arr[now*2][0] == -1 or arr[now*2][0] > arr[now][0] + 1):
        arr[now*2][0] = arr[now][0] + 1
        arr[now*2][1] = now
        queue.append(now*2)
        
result = [k]
go = arr[k][1]
while go != -10:
    result.append(go)
    go = arr[go][1]

print(len(result) - 1)
print(' '.join(map(str, result[::-1])))