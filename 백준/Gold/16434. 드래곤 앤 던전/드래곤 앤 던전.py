import sys
input = sys.stdin.readline

n, atk = map(int, input().rstrip().split())
now = 0
nowmax = 0
for _ in range(n):
    t, a, h = map(int, input().rstrip().split())

    if t == 1:
        if h % atk == 0:
            now += (h // atk - 1) * a
        else:
            now += (h // atk) * a
    else:
        now = max(0, now - h)
        atk += a
    
    nowmax = max(now, nowmax)

print(nowmax + 1)