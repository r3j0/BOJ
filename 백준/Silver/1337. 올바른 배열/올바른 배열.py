import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()

max_value = 4
for i in range(n-1):
    for j in range(i+1, n):
        if arr[j] - arr[i] <= 4:
            max_value = min(max_value, 4 - (j - i))

print(max_value)