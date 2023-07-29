a, b = map(int, input().split())
n = int(input())
for _ in range(n):
    now = int(input())
    if now > 1000:
        print(now, a*1000+b*(now-1000))
    else:
        print(now, now*a)