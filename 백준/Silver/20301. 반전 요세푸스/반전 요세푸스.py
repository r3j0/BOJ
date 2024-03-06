import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().rstrip().split())
queue = deque()
for i in range(1, n+1): queue.append(i)
queue.appendleft(queue.pop())

mode = 0
cnt = 0
while queue:
    if mode == 0:
        for _ in range(k):
            queue.append(queue.popleft())
        print(queue.popleft())
        if queue: queue.appendleft(queue.pop())
    else:
        for _ in range(k):
            queue.appendleft(queue.pop())
        print(queue.pop())
        if queue: queue.append(queue.popleft())
    cnt += 1
    if queue and cnt == m:
        cnt = 0
        if mode == 0:
            for _ in range(2): queue.append(queue.popleft())
        else:
            for _ in range(2): queue.appendleft(queue.pop())
        mode ^= 1