import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
n = int(input().rstrip())
now = abs(a-b)
near = a
for _ in range(n):
    tmp = int(input().rstrip())
    if abs(near-b) > abs(tmp-b):
        near = tmp

print(min(now, abs(near-b) + 1))