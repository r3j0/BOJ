n = int(input())
arr = list(map(int, input().rstrip().split()))
idx = 0
for i in range(1, n):
    if arr[idx] > arr[i]:
        idx = i
print(idx)