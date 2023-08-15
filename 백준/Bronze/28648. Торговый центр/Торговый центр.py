import sys
input = sys.stdin.readline

t = int(input().rstrip())
maxs = -1
for _ in range(t):
    a, b = map(int, input().split())
    if maxs == -1 or maxs > a + b: maxs = a + b

print(maxs)