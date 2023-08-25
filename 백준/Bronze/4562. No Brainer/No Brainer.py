import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().rstrip().split())

    if a < b: print('NO BRAINS')
    else: print('MMM BRAINS')