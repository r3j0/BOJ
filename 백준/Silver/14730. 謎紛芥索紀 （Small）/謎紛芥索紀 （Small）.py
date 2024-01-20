import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    result += a * b
print(result)