import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

max_value = 1

for i in range(n):
    now = 1
    for j in range(i - 1, -1, -1):
        if arr[j + 1] > arr[j]: now += 1
        else: break
    for j in range(i + 1, n):
        if arr[j - 1] > arr[j]: now += 1
        else: break
    
    max_value = max(max_value, now)
print(max_value)