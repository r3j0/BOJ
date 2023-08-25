import sys
input = sys.stdin.readline

r, c, zr, zc = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(r)]

for i in range(r):
    for _ in range(zr):
        for j in range(c):
            print(maps[i][j]*zc, end='')
        print()