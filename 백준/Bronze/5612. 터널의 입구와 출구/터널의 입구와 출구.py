import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
maxs = m
done = 0
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    m += a
    m -= b
    if m < 0:
        done = 1
    
    maxs = max(maxs, m)

if done == 1: print(0)
else: print(maxs)