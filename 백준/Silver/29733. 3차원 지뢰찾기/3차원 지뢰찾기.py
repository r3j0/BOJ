import sys
input = sys.stdin.readline

r, c, h = map(int, input().rstrip().split())
maps = [[list(input().rstrip()) for _ in range(r)] for _ in range(h)]
dir1 = [-1,-1,-1, 0, 0, 0, 1, 1, 1, -1,-1,-1, 0, 0, 1, 1, 1, -1,-1,-1, 0, 0, 0, 1, 1, 1]
dir2 = [-1, 0, 1,-1, 0, 1,-1, 0, 1, -1, 0, 1,-1, 1,-1, 0, 1, -1, 0, 1,-1, 0, 1,-1, 0, 1]
dir3 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,  0, 0, 0, 0, 0, 0, 0, 0,  1, 1, 1, 1, 1, 1, 1, 1, 1]

arr = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(h)]
for i in range(r):
    for j in range(c):
        for k in range(h):
            for d in range(26):
                ny = i + dir1[d]
                nx = j + dir2[d]
                nz = k + dir3[d]

                if 0 <= ny < r and 0 <= nx < c and 0 <= nz < h and maps[nz][ny][nx] == '*':
                    arr[k][i][j] = (arr[k][i][j] + 1) % 10

for k in range(h):
    for i in range(r):
        for j in range(c):
            if maps[k][i][j] == '*': print('*', end='')
            else: print(arr[k][i][j], end='')
        print()