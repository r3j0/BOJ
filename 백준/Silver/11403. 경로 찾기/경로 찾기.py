import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(n):
    visited = [0 for _ in range(n)]
    queue = deque()
    queue.append(i)

    while queue:
        now = queue.popleft()

        for j in range(n):
            if visited[j] == 0 and arr[now][j] == 1:
                visited[j] = 1
                queue.append(j)
    
    print(' '.join(map(str, visited)))