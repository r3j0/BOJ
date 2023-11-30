import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    x, y = map(int, input().rstrip().split())
    i = 1
    while i * (i + 1) < y - x: i += 1
    i -= 1
    print(i * 2 + (2 if (y - x) - i * (i + 1) > i + 1 else 1))