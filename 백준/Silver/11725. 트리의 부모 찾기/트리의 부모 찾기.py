import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
edge = [{} for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    edge[a][b] = 1
    edge[b][a] = 1


queue = deque()
visited = [0 for _ in range(n+1)]

queue.append(1)
visited[1] = 1

result = [0 for _ in range(n+1)]

while queue:
    size = len(queue)

    for _ in range(size):
        parent = queue.popleft()

        for child in edge[parent].keys():
            if visited[child] == 0:
                visited[child] = 1
                queue.append(child)

                result[child] = parent

for i in range(2, n+1):
    print(result[i])