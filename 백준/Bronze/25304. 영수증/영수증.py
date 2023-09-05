import sys
input = sys.stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())
sumPrice = 0

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    sumPrice += a * b

if sumPrice == x: print('Yes')
else: print('No')