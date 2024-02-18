import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

result = 0
for i in range(n-2, -1, -1):
    if arr[i] >= arr[i+1]:
        result += arr[i] - (arr[i+1] - 1)
        arr[i] = arr[i+1] - 1

print(result)