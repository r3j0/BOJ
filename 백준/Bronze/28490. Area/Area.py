n = int(input())
maxs = 0
for _ in range(n):
    a, b = map(int, input().split())
    maxs = max(maxs, a*b)
print(maxs)