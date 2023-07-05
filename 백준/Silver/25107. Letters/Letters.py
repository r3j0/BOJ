import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
order = list(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]

def up():
    for j in range(m):
        now = []
        for i in range(n):
            if maps[i][j] != '.': now.append(maps[i][j])
        
        for i in range(n):
            if i < len(now):
                maps[i][j] = now[i]
            else:
                maps[i][j] = '.'

def down():
    for j in range(m):
        now = []
        for i in range(n-1, -1, -1):
            if maps[i][j] != '.': now.append(maps[i][j])
        for i in range(n-len(now)):
            now.append('.')
        
        for i in range(n-1, -1, -1):
            maps[i][j] = now[(n-1)-i]
            

def left():
    for i in range(n):
        now = []
        for j in range(m):
            if maps[i][j] != '.': now.append(maps[i][j])

        for j in range(m-len(now)): now.append('.')
        maps[i] = now

def right():
    for i in range(n):
        now = []
        now = []
        for j in range(m):
            if maps[i][j] != '.': now.append(maps[i][j])

        for j in range(m-len(now)): now = ['.'] + now
        maps[i] = now

for o in order:
    if o == 'U': up()
    elif o == 'D': down()
    elif o == 'L': left()
    elif o == 'R': right()

for i in range(n): print(''.join(maps[i]))