import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().rstrip().split())
n = int(input().rstrip())
maps = [[0 for _ in range(w)] for _ in range(h)]
blocks = {'redstone_dust':1, 'redstone_block':2, 'redstone_lamp':3}
queue = deque()
lamp_list = deque()
redstone = [[0 for _ in range(w)] for _ in range(h)]
for _ in range(n):
    block, x, y = input().rstrip().split()
    maps[int(y)][int(x)] = blocks[block]

    if blocks[block] == 2: 
        queue.append([int(y), int(x), 16])
        redstone[int(y)][int(x)] = 16
    elif blocks[block] == 3:
        lamp_list.append([int(y), int(x)])



row = [-1, 0, 1, 0]
col = [0, -1, 0, 1]
while queue:
    now = queue.popleft()
    if now[2] == 1: continue
    for d in range(4):
        ny = now[0] + row[d]
        nx = now[1] + col[d]

        if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] != 0 and redstone[ny][nx] < now[2] - 1:
            redstone[ny][nx] = now[2] - 1
            if maps[ny][nx] != 3:
                queue.append([ny, nx, now[2]-1])

cnt = 0
for li in lamp_list:
    if redstone[li[0]][li[1]] > 0: cnt += 1

#for i in range(h): print(' '.join(map(str, maps[i])))
#print()    
#for i in range(h): print(' '.join(map(str, redstone[i])))

if cnt != len(lamp_list): print('failed')
else: print('success')
