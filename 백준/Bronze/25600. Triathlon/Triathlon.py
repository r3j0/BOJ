n = int(input())
maxs = 0
for _ in range(n):
    a, d, g = map(int, input().split())
    maxs = max(maxs, a*(d+g) * (2 if a == d + g else 1))

print(maxs)