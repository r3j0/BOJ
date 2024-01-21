import sys
from collections import deque
input = sys.stdin.readline

size = int(input().rstrip())
queue = deque()

while True:
    n = int(input().rstrip())
    if n == -1: break
    if n > 0: 
        if len(queue) != size:
            queue.append(n)
    if n == 0: queue.popleft()

if len(queue) == 0: print('empty')
else:
    for a in queue:
        print(a, end=' ')
