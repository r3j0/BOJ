import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()

low = 1
high = arr[-1] - arr[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    now = arr[0]
    cnt = 1
    for i in range(1, n):
        if (arr[i] - now >= mid):
            cnt += 1
            now = arr[i]
    
    if cnt >= c:
        result = max(result, mid)
        low = mid + 1
    else:
        high = mid - 1

print(result)