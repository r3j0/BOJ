import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
start = max(arr)
end = sum(arr)
res = sum(arr)
while start <= end:
    mid = (start + end) // 2
    rest = 0
    cnt = 0
    for i in range(n):
        if rest < arr[i]:
            cnt += 1
            rest = mid - arr[i]
        else:
            rest -= arr[i]
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = min(res, mid)
print(res)