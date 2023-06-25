import sys
from collections import deque
import heapq
input = sys.stdin.readline

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

t = int(input().rstrip())
for _ in range(t):
    maps = [list(input().rstrip()) for _ in range(3)]
    visited = [[0 for _ in range(3)] for _ in range(3)]
    result = []
    for i in range(3):
        for j in range(3):
            if visited[i][j] == 0 and maps[i][j] == 'O':
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                cnt = 1
                while queue:
                    size = len(queue)
                    for s in range(size):
                        y, x = queue.popleft()
                        for d in range(4):
                            ny = y + row[d]
                            nx = x + col[d]

                            if 0 <= ny < 3 and 0 <= nx < 3 and maps[ny][nx] == 'O' and visited[ny][nx] == 0:
                                visited[ny][nx] = 1
                                queue.append((ny, nx))
                                cnt += 1
                
                heapq.heappush(result, cnt)
                #print(result)

    done = 0
    arr = list(map(int, input().rstrip().split()))
    if len(arr) == 1:
        if len(result) == 0: print(1)
        else: print(0)
    else:
        if len(arr) - 1 != len(result): 
            print(0)
        else:
            for a in range(len(arr)):
                if a == 0: continue
                if len(result) == 0: 
                    done = 1
                    print(0)
                    break
                now = heapq.heappop(result) 
                if now != arr[a]:
                    done = 1
                    print(0)
                    break
            if done == 0: print(1)
