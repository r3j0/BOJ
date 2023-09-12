import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
u, l, r, d = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

mode = 0
for _ in range(u):
    for j in range(l+r+m):
        if j % 2 == mode:
            print('#', end='')
        else:
            print('.', end='')
    print()
    mode = 1 if mode == 0 else 0

for i in range(n):
    for j in range(l+r+m):
        if l <= j < l + m:
            print(maps[i][j-l], end='')
        else:
            if j % 2 == mode:
                print('#', end='')
            else:
                print('.', end='')
    print()
    mode = 1 if mode == 0 else 0

for _ in range(d):
    for j in range(l+r+m):
        if j % 2 == mode:
            print('#', end='')
        else:
            print('.', end='')
    print()
    mode = 1 if mode == 0 else 0