arr = list(map(int, input().rstrip().split()))
arr.sort()
idx = 4
for i in range(3, -1, -1):
    if arr[-1] - arr[i] > 1000: break
    idx = i
print(4 - idx)