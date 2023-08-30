import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(n)]
ey, ex = map(int, input().rstrip().split())
ny = 1; nx = 1
for i in range(n):
    nx = 1
    for j in range(m):
        print(arr[i][j] if not (ey == ny and ex == nx) else ('.' if arr[i][j] == '#' else '#'), end='')
        nx += 1
    for j in range(m-1, -1, -1):
        print(arr[i][j] if not (ey == ny and ex == nx) else ('.' if arr[i][j] == '#' else '#'), end='')
        nx += 1
    ny += 1
    print()


for i in range(n-1, -1, -1):
    nx = 1
    for j in range(m):
        print(arr[i][j] if not (ey == ny and ex == nx) else ('.' if arr[i][j] == '#' else '#'), end='')
        nx += 1
    for j in range(m-1, -1, -1):
        print(arr[i][j] if not (ey == ny and ex == nx) else ('.' if arr[i][j] == '#' else '#'), end='')
        nx += 1
    ny += 1
    print()