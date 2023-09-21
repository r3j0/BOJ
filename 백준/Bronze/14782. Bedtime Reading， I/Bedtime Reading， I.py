import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0
for i in range(1, n+1):
    if n % i == 0: result += i
print(result)