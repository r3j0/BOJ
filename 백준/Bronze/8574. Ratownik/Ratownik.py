n, k, x, y = map(int, input().rstrip().split())
cnt = 0
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    if ((a - x)**2 + (b - y)**2) > k**2: cnt += 1
print(cnt)