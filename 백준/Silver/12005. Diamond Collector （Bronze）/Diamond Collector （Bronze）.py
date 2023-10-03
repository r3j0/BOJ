import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()
max_value = 0
for i in range(n):
    for j in range(i, n):
        if arr[j] - arr[i] <= k: 
            max_value = max(max_value, j - i + 1)

print(max_value)