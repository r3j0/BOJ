import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, -1, 1, -1, 1]

for i in range(n):
    for j in range(n):
        if maps[i][j] != '.':
            print('*', end='')
        else:
            cnt = 0
            for d in range(8):
                ny = i + row[d]
                nx = j + col[d]

                if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] != '.':
                    cnt += int(maps[ny][nx])
            
            if cnt >= 10:
                print('M', end='')
            else: 
                print(cnt, end='')
    print()