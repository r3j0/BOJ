import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
result = 1

for i in range(a, b+1):
    result = (result * ((i*(i+1))//2)) % 14579

print(result)