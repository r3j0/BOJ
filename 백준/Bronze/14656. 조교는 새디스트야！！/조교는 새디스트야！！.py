n = int(input())
arr = list(map(int, input().split()))
result = 0
for i in range(n):
    if arr[i] != i+1:
        result += 1
print(result)