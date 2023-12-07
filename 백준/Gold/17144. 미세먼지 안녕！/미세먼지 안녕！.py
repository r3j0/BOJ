import sys
input = sys.stdin.readline

r, c, t = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(r)]

start_air = 0
for i in range(r):
    if maps[i][0] == -1:
        start_air = i
        maps[i][0] = 0
        maps[i+1][0] = 0
        break

def spread():
    global r
    global c
    global maps
    new_maps = [[0 for _ in range(c)] for _ in range(r)]
    row = [-1, 0, 1, 0]
    col = [0, -1, 0, 1]
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                value = maps[i][j]//5
                cnt = 0
                for d in range(4):
                    ny = i + row[d]
                    nx = j + col[d]

                    if 0 <= ny < r and 0 <= nx < c and ((nx == 0 and (start_air > ny or start_air + 1 < ny)) or nx != 0):
                        new_maps[ny][nx] += value
                        cnt += 1

                new_maps[i][j] += maps[i][j] - (value*cnt)

    for i in range(r):
        for j in range(c):
            maps[i][j] = new_maps[i][j]

def air():
    global r
    global c
    global maps
    global start_air

    # Up
    now_y = start_air
    now_x = 1
    tmp = maps[now_y][now_x]
    maps[now_y][now_x] = 0
    while now_x < c - 1:
        now_go = tmp
        tmp = maps[now_y][now_x + 1]
        maps[now_y][now_x + 1] = now_go
        now_x += 1
    
    while now_y > 0:
        now_go = tmp
        tmp = maps[now_y - 1][now_x]
        maps[now_y - 1][now_x] = now_go
        now_y -= 1
    
    while now_x > 0:
        now_go = tmp
        tmp = maps[now_y][now_x - 1]
        maps[now_y][now_x - 1] = now_go
        now_x -= 1
    
    while now_y < start_air - 1:
        now_go = tmp
        tmp = maps[now_y + 1][now_x]
        maps[now_y + 1][now_x] = now_go
        now_y += 1

    # Down
    now_y = start_air + 1
    now_x = 1
    tmp = maps[now_y][now_x]
    maps[now_y][now_x] = 0
    while now_x < c - 1:
        now_go = tmp
        tmp = maps[now_y][now_x + 1]
        maps[now_y][now_x + 1] = now_go
        now_x += 1
    
    while now_y < r - 1:
        now_go = tmp
        tmp = maps[now_y + 1][now_x]
        maps[now_y + 1][now_x] = now_go
        now_y += 1
    
    while now_x > 0:
        now_go = tmp
        tmp = maps[now_y][now_x - 1]
        maps[now_y][now_x - 1] = now_go
        now_x -= 1
    
    while now_y > start_air + 2:    
        now_go = tmp
        tmp = maps[now_y - 1][now_x]
        maps[now_y - 1][now_x] = now_go
        now_y -= 1
   
for _ in range(t):
    spread()
    #print('Spread') 
    #for i in range(r): print(' '.join(map(str, maps[i])))
    #print()
    air()
    #print('Air') 
    #for i in range(r): print(' '.join(map(str, maps[i])))
    #print()

sums = 0
for i in range(r): sums += sum(maps[i])
print(sums)