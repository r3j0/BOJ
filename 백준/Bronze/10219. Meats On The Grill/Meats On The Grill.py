import sys
input = sys.stdin.readline

test = int(input().rstrip())
for _ in range(test):
    n, m = map(int, input().rstrip().split())
    maps = [list(input().rstrip()) for _ in range(n)]

    for i in range(n):
        for j in range(m-1, -1, -1):
            print(maps[i][j], end='')
        print()