import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

max_value = 0
now_min = arr[0]
for i in range(1, n):
    if now_min > arr[i]:
        now_min = arr[i]
    else:
        max_value = max(max_value, arr[i] - now_min)

print(max_value)