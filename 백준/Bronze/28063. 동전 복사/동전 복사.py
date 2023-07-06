import sys
input = sys.stdin.readline

n = int(input().rstrip())
x, y = map(int, input().rstrip().split())

if n == 1: print(0)
else:
    now = 4
    if x == 1 or x == n: now -= 1
    if y == 1 or y == n: now -= 1

    print(now)