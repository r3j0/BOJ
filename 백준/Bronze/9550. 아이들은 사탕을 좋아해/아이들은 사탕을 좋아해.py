import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    cnt = 0
    for a in arr:
        if a >= k: cnt += a//k
    print(cnt)