import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
n = int(input().rstrip())

maxs = 0
for _ in range(n):
    now = 0
    for _ in range(3):
        i, j, k = map(int, input().rstrip().split())
        now += a*i+b*j+c*k
    maxs = max(maxs, now)

print(maxs)