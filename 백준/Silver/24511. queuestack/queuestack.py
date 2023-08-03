import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
qs_info = list(map(int, input().rstrip().split()))
qs_data = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
c = list(map(int, input().rstrip().split()))

queue = deque()
for i in range(n - 1, -1, -1):
    if qs_info[i] == 0: queue.append(qs_data[i])

for i in c:
    queue.append(i)
    print(queue[0], end=' ')
    queue.popleft()