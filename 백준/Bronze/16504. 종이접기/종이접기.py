import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    result += sum(arr)
print(result)