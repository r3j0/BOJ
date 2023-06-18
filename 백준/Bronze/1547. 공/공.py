import sys
input = sys.stdin.readline

m = int(input().rstrip())
c = {1:1, 2:2, 3:3}
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    c[a], c[b] = c[b], c[a]

for k, v in c.items():
    if v == 1: print(k)