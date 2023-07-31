import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
arr = [] 
for _ in range(k):
    arr.append(int(input().rstrip()))

start = 1
end = max(arr)
mid = 0
res = 0
while start <= end:
    mid = (start + end) // 2

    now = 0
    for a in arr: now += a // mid

    if now >= n: 
        res = mid
        start = mid + 1
    elif now < n: end = mid - 1

print(res)