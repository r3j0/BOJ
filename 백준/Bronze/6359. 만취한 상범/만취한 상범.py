import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    now = 1
    while now**2 <= n:
        now += 1
    print(now - 1)