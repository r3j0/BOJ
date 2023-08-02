import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

n = int(input().rstrip())
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))

    if arr[0] == 1:
        queue.appendleft(arr[1])
    elif arr[0] == 2:
        queue.append(arr[1])
    elif arr[0] == 3:
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif arr[0] == 4:
        if queue:
            print(queue[-1])
            queue.pop()
        else:
            print(-1)
    elif arr[0] == 5:
        print(len(queue))
    elif arr[0] == 6:
        if queue: print(0)
        else: print(1)
    elif arr[0] == 7:
        if queue: print(queue[0])
        else: print(-1)
    elif arr[0] == 8:
        if queue: print(queue[-1])
        else: print(-1)