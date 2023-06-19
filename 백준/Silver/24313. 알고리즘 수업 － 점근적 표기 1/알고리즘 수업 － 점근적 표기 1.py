import sys
input = sys.stdin.readline
a1, a0 = map(int, input().rstrip().split())
c = int(input().rstrip())
n0 = int(input().rstrip())

if a1 > c: print(0)
elif a1 == c:
    if a0 > 0: print(0)
    else: print(1)
else:
    pivot = a0 / (c - a1)
    if pivot > n0: print(0)
    else: print(1)