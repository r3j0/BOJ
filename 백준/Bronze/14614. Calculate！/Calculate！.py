import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
if c % 2 == 1: a ^= b
print(a)