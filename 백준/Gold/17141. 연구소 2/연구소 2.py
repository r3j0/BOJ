import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2: virus.append([i, j])

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
result = -1

def backtracking(start, now):
    global result
    if len(now) == m:
        now_map = [[0 for _ in range(n)] for _ in range(n)]
        cnt = -m
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 1: now_map[i][j] = 1
                else: cnt += 1

        queue = deque()
        for v in now: 
            queue.append(v)
            now_map[v[0]][v[1]] = 2

        time = 0
        while queue:
            if cnt == 0:
                break

            size = len(queue)
            for s in range(size):
                now = queue.popleft()
                for d in range(4):
                    ny = now[0] + row[d]
                    nx = now[1] + col[d]

                    if 0 <= ny < n and 0 <= nx < n and now_map[ny][nx] == 0:
                        now_map[ny][nx] = 2
                        cnt -= 1
                        queue.append([ny, nx])
            time += 1
        
        if cnt == 0: 
            if result == -1: result = time
            else: result = min(result, time)
        return
    
    for i in range(start, len(virus)):
        now.append(virus[i])
        backtracking(i + 1, now)
        now.pop()

backtracking(0, [])
print(result)