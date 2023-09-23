import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0: cnt += 1
    print(n, cnt)