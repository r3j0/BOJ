from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
queue = deque()
for _ in range(n):
    ope = list(input().rstrip().split())
    if ope[0] == 'push': queue.append(ope[1])
    elif ope[0] == 'pop': print(-1 if len(queue) == 0 else queue.popleft())
    elif ope[0] == 'size': print(len(queue))
    elif ope[0] == 'empty': print(1 if len(queue) == 0 else 0)
    elif ope[0] == 'front': print(-1 if len(queue) == 0 else queue[0])
    elif ope[0] == 'back': print(-1 if len(queue) == 0 else queue[-1])