import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
result = 0
for _ in range(m):
    k = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    if arr != sorted(arr, reverse=True): result = 1

print('No' if result == 1 else 'Yes')