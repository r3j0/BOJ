import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    a, b = input().split()
    if '0' <= a[0] <= '9':
        arr.append([int(a) // 2, b])
    else:
        arr.append([int(b), a])

arr.sort(key=lambda x:x[0])
for i in range(n):
    print(arr[i][1])