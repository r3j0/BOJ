import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
if n > 0:
    arr = list(map(int, input().rstrip().split()))

    now = 0
    cnt = 1
    for a in arr:
        if now + a > m:
            now = a
            cnt += 1
        else:
            now += a
    print(cnt)
else:
    print(0)