import sys
input = sys.stdin.readline

arr = [int(input().rstrip()) for _ in range(9)]

max_value = arr[0]
max_idx = 0

for i in range(1, 9):
    if max_value < arr[i]:
        max_value = arr[i]
        max_idx = i

print(max_value)
print(max_idx + 1)