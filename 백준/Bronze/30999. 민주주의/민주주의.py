import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
r = 0
for i in range(a):
    n = list(input().rstrip())
    if n.count('O') > (b//2): r += 1
print(r)