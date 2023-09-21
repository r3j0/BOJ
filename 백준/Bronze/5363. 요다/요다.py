import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    arr = list(input().rstrip().split())
    for i in range(2, len(arr)): print(arr[i], end=' ')
    for i in range(2): print(arr[i], end=' ')
    print()