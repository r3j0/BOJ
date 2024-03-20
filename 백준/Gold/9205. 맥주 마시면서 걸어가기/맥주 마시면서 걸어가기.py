import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    node = [list(map(int, input().rstrip().split()))]
    for _ in range(n):
        now = list(map(int, input().rstrip().split()))
        node.append(now)
    node.append(list(map(int, input().rstrip().split())))

    start = 0
    end = len(node) - 1

    vis = [0 for _ in range(n+2)]
    vis[0] = 1

    queue = deque()
    queue.append(0)
    
    res = 0
    while queue:
        now = queue.popleft()
        if now == end:
            res = 1
            break
            
        for i in range(1, n+2):
            if vis[i] == 0 and abs(node[now][0] - node[i][0]) + abs(node[now][1] - node[i][1]) <= 1000:
                queue.append(i)
                vis[i] = 1
    
    print('happy' if res == 1 else 'sad')