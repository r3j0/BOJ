import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, d = map(int, input().rstrip().split())
    cnt = 0
    for _ in range(n):
        v, f, c = map(int, input().rstrip().split())
        if v*f/c >= d: cnt += 1
    print(cnt)