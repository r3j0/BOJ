import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

mos = [0, 0]
zag = [0, 0]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'M':
            mos = [i, j]
        elif maps[i][j] == 'Z':
            zag = [i, j]

def search_blank(pos):
    global maps
    y = pos[0]
    x = pos[1]

    dir = -1
    # Left Up Right Down

    row = [0,-1,0,1]
    col = [-1,0,1,0]

    while True:
        #print(y, x, maps[y][x])
        if maps[y][x] == 'M' or maps[y][x] == 'Z':
            # Left
            if 0 <= y+row[0] < n and 0 <= x+col[0] < m and maps[y+row[0]][x+col[0]] in ['-', '+', '1', '2']:
                dir = 0
            elif 0 <= y+row[1] < n and 0 <= x+col[1] < m and maps[y+row[1]][x+col[1]] in ['|', '+', '1', '4']:
                dir = 1
            elif 0 <= y+row[2] < n and 0 <= x+col[2] < m and maps[y+row[2]][x+col[2]] in ['-', '+', '3', '4']:
                dir = 2
            elif 0 <= y+row[3] < n and 0 <= x+col[3] < m and maps[y+row[3]][x+col[3]] in ['|', '+', '2', '3']:
                dir = 3
            else:
                return -1
            
            y += row[dir]; x += col[dir]
        elif maps[y][x] == '|' or maps[y][x] == '-' or maps[y][x] == '+':
            y += row[dir]; x += col[dir]
        elif maps[y][x] == '1':
            if dir == 0: dir = 3
            if dir == 1: dir = 2
            
            y += row[dir]; x += col[dir]
        elif maps[y][x] == '2':
            if dir == 0: dir = 1
            if dir == 3: dir = 2

            y += row[dir]; x += col[dir]
        elif maps[y][x] == '3':
            if dir == 2: dir = 1
            if dir == 3: dir = 0

            y += row[dir]; x += col[dir]
        elif maps[y][x] == '4':
            if dir == 2: dir = 3
            if dir == 1: dir = 0

            y += row[dir]; x += col[dir]
        else:
            return (y, x)

mos_search = search_blank(mos)
zag_search = search_blank(zag)

#print(mos_search, zag_search)

ry = 0; rx = 0
if mos_search == -1:
    ry = zag_search[0]; rx = zag_search[1]
else:
    ry = mos_search[0]; rx = mos_search[1]

open = [0,0,0,0]
# Left
if 0 <= rx-1 < m and maps[ry][rx-1] in ['-', '+', '1', '2']: open[0] = 1
if 0 <= rx-1 < m and maps[ry][rx-1] in ['M', 'X']: open[0] = 2
# Up
if 0 <= ry-1 < n and maps[ry-1][rx] in ['|', '+', '1', '4']: open[1] = 1
if 0 <= ry-1 < n and maps[ry-1][rx] in ['M', 'X']: open[1] = 2
# Right
if 0 <= rx+1 < m and maps[ry][rx+1] in ['-', '+', '3', '4']: open[2] = 1
if 0 <= rx+1 < m and maps[ry][rx+1] in ['M', 'X']: open[2] = 2
# Down
if 0 <= ry+1 < n and maps[ry+1][rx] in ['|', '+', '2', '3']: open[3] = 1
if 0 <= ry+1 < n and maps[ry+1][rx] in ['M', 'X']: open[3] = 2

resp = '0'
if '2' in open:
    if open.count('0') == 2:
        ans = []
        for o in range(len(open)):
            if open[o] == '1' or open[o] == '2':
                ans.append(o)
        
        if ans[0] == 0 and ans[1] == 2: resp = '-'
        elif ans[0] == 1 and ans[1] == 3: resp = '|'
        elif ans[0] == 0 and ans[1] == 1: resp = '3'
        elif ans[0] == 2 and ans[1] == 3: resp = '1'
        elif ans[0] == 1 and ans[1] == 2: resp = '2'
        elif ans[0] == 0 and ans[1] == 3: resp = '4'
    else:
        ans = []
        for o in range(len(open)):
            if open[o] == '1':
                ans.append(o)
        
        if ans[0] == 0 and ans[1] == 2: resp = '-'
        elif ans[0] == 1 and ans[1] == 3: resp = '|'
        elif ans[0] == 0 and ans[1] == 1: resp = '3'
        elif ans[0] == 2 and ans[1] == 3: resp = '1'
        elif ans[0] == 1 and ans[1] == 2: resp = '2'
        elif ans[0] == 0 and ans[1] == 3: resp = '4'
else:
    if open[0] == 1 and open[1] == 1 and open[2] == 1 and open[3] == 1: resp = '+'
    elif open[0] == 1 and open[2] == 1: resp = '-'
    elif open[1] == 1 and open[3] == 1: resp = '|'
    elif open[0] == 1 and open[1] == 1: resp = '3'
    elif open[2] == 1 and open[3] == 1: resp = '1'
    elif open[1] == 1 and open[2] == 1: resp = '2'
    elif open[0] == 1 and open[3] == 1: resp = '4'

print(ry+1, rx+1, resp)