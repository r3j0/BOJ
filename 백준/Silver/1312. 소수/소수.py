import sys
input = sys.stdin.readline

a, b, n = map(int, input().rstrip().split())
for _ in range(n):
    a = (a % b) * 10

print(a//b)