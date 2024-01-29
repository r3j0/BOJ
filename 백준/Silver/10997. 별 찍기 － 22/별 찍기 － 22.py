import sys
input = sys.stdin.readline

n = int(input().rstrip()) * 4 - 3

if n == 1: print('*')
else:
    arr = [['*' for _ in range(n)] for _ in range(n+2)]

    now = [1, n - 1]
    row = [0, 1, 0, -1]
    col = [-1, 0, 1, 0]
    dir = 0
    cnt = 0

    while True:
        arr[now[0]][now[1]] = ' '
        if (dir == 0 and (now[1] == 1 or arr[now[0]][now[1] - 2] == ' ')) or (dir == 1 and (now[0] == n or arr[now[0] + 2][now[1]] == ' ')) or (dir == 2 and (now[1] == n - 2 or arr[now[0]][now[1] + 2] == ' ')) or (dir == 3 and arr[now[0] - 2][now[1]] == ' '):
            dir = (dir + 1) % 4
            cnt += 1
        else: 
            cnt = 0
            now[0] += row[dir]
            now[1] += col[dir]

        if cnt == 5: break

    for i in range(n+2):
        if i == 1: print('*')
        else:
            for j in range(n):
                print(arr[i][j], end='')
            print()
