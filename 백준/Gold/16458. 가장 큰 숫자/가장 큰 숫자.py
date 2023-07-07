import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n): 
    for j in range(m-len(maps[i])):
        maps[i].append(' ')

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, -1, 1, -1, 1]

max_number = 0
max_side = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and maps[i][j] == '*':
            down = 1
            queue = deque()
            queue.append((i, j))

            while queue:
                y, x = queue.popleft()
                if y + 1 < n and maps[y + 1][x] == '*':
                    queue.append((y + 1, x))
                    down += 1

            right = 1
            queue = deque()
            queue.append((i, j))
            
            while queue:
                y, x = queue.popleft()
                if x + 1 < m and maps[y][x + 1] == '*':
                    queue.append((y, x + 1))
                    right += 1
            
            now_number = 0
            side = 0
            if down * 2 == right: # 1, 2
                side = down
                if maps[i + (side)][j + (side * 2)] == '*':
                    now_number = 2
                else:
                    now_number = 1
            
            elif down == right * 5: # 4, 6
                side = right
                if j + side < m and maps[i + (side * 2)][j + (side)] == '*':
                    now_number = 6
                else:
                    now_number = 4

            elif down * 3 == right: # 3, 7
                side = down
                if maps[i + (side * 2)][j + (side * 2)] == '*':
                    now_number = 3
                else:
                    now_number = 7

            elif down * 3 == right * 5: # 0, 8
                side = down // 5
                if maps[i + (side * 2)][j + (side)] == '*':
                    now_number = 8
                else:
                    now_number = 0

            elif down == right: # 5, 9
                side = down // 3
                if maps[i + (side)][j + (side * 2)] == '*':
                    now_number = 9
                else:
                    now_number = 5
            
            if side > max_side:
                max_side = side
                max_number = now_number

            # LEAST
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1

            while queue:
                y, x = queue.popleft()
                for d in range(8):
                    ny = y + row[d]
                    nx = x + col[d]

                    if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maps[ny][nx] == '*':
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
            
print(max_number)