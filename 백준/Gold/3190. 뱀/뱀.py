from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [[0 for _ in range(n)] for _ in range(n)]
maps[0][0] = 1
dir = 0 # 0 1 2 3
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
now = deque()
now.append([0, 0])
k = int(input().rstrip())
for _ in range(k):
    y, x = map(int, input().rstrip().split())
    maps[y-1][x-1] = 2

l = int(input().rstrip())
change = deque()
for _ in range(l):
    x, c = input().rstrip().split()
    change.append([int(x), c])

time = 0
while True:
    now_head = list(now[-1])
    
    now_head[0] += row[dir]
    now_head[1] += col[dir]
    if not (0 <= now_head[0] < n and 0 <= now_head[1] < n):
        time += 1
        break
    elif maps[now_head[0]][now_head[1]] == 1:
        time += 1
        break
    elif maps[now_head[0]][now_head[1]] != 2:
        maps[now[0][0]][now[0][1]] = 0
        now.popleft()    

    maps[now_head[0]][now_head[1]] = 1
    now.append(now_head)

    time += 1
    if len(change) != 0 and change[0][0] == time:
        if change[0][1] == 'L': 
            dir = dir - 1
            if dir < 0: dir += 4
        else:
            dir = dir + 1                                       
            if dir > 3: dir = 0
        change.popleft()

print(time)