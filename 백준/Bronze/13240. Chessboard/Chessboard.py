import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
for i in range(n):
    for j in range(m):
        if i % 2 == j % 2: print('*', end='')
        else: print('.', end='')
    print()