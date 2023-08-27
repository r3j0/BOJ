import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
n = str(n)
now = 0
if len(n) * int(n) > m:
    for i in range(m):
        print(n[now], end='')
        now = (now + 1) % (len(n))
else:
    for i in range(int(n)):
        print(n, end='')