import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2 
    now = 0
    for a in arr: now += max(0, a - mid)

    if now >= m: start = mid + 1
    else: end = mid - 1

print(start - 1)