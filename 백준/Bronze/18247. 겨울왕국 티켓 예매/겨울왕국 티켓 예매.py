import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    if n >= 12 and m >= 4:
        print(m * 11 + 4)
    else:
        print(-1)