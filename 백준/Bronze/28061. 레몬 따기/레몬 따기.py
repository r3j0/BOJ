import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
max_value = 0
for i in range(n):
    max_value = max(max_value, arr[i] - (n - i))
print(max_value)