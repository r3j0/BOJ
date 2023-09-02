import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [[[0, 0] for _ in range(n)] for _ in range(n)]
now = [0, 0]

order = input().rstrip()
for o in order:
    if o == 'U':
        if now[0] != 0:
            maps[now[0]][now[1]][0] = 1
            now[0] -= 1
            maps[now[0]][now[1]][0] = 1
    elif o == 'D':
        if now[0] != n-1:
            maps[now[0]][now[1]][0] = 1
            now[0] += 1
            maps[now[0]][now[1]][0] = 1
    elif o == 'L':
        if now[1] != 0:
            maps[now[0]][now[1]][1] = 1
            now[1] -= 1
            maps[now[0]][now[1]][1] = 1
    elif o == 'R':
        if now[1] != n-1:
            maps[now[0]][now[1]][1] = 1
            now[1] += 1
            maps[now[0]][now[1]][1] = 1

for i in range(n):
    for j in range(n):
        if maps[i][j][0] == 1 and maps[i][j][1] == 1:
            print('+', end='')
        elif maps[i][j][0] == 1:
            print('|', end='')
        elif maps[i][j][1] == 1:
            print('-', end='')
        else:
            print('.', end='')
    print()