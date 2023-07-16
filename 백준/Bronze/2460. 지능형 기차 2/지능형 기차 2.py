maxs = 0
now = 0
for _ in range(10):
    a, b = map(int, input().rstrip().split())
    now -= a
    now += b
    maxs = max(maxs, now)
print(maxs)