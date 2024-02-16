import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(r)]
arr = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'O': arr[i][j] = 3

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
time = 0
while time < n:
    queue = deque()
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                queue.append([i, j])
                arr[i][j] = 0
            elif arr[i][j] > 1:
                arr[i][j] -= 1
    
    while queue:
        now = queue.popleft()
        for d in range(4):
            ny = now[0] + row[d]
            nx = now[1] + col[d]

            if 0 <= ny < r and 0 <= nx < c:
                arr[ny][nx] = 0

    if time % 2 != 0:
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 0:
                    arr[i][j] = 3
    
    time += 1

for i in range(r):
    for j in range(c):
        if arr[i][j] > 0: print('O', end='')
        else: print('.', end='')
    print()