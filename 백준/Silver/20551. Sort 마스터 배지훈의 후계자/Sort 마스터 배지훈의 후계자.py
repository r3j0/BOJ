import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()
for _ in range(m):
    d = int(input().rstrip())
    start = 0
    end = n - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= d:
            end = mid - 1
        elif arr[mid] < d:
            start = mid + 1
        if arr[mid] == d: 
            if res == -1: res = mid
            else: res = min(res, mid)
    print(res)