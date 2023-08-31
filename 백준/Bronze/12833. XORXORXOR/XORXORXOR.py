import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
if c % 2 == 1:
    a ^= b
print(a)