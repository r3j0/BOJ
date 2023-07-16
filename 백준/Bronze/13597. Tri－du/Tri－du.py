import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
if a == b: print(a)
else: print(max(a, b))