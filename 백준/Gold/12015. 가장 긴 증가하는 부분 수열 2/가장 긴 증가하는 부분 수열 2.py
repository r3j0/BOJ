import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
dp = [0 for _ in range(1000001)]
size = 1

def binarySearch(now, start, end):
    mid = (start + end) // 2
    if start > end: return -1
    if dp[mid] < now <= dp[mid+1]: return mid+1
    if dp[mid] >= now: return binarySearch(now, start, mid - 1)
    if dp[mid] < now: return binarySearch(now, mid + 1, end)

for a in arr:
    index = binarySearch(a, 0, size-1)

    if index == -1:
        dp[size] = a
        size += 1
    else:
        dp[index] = a

print(size - 1)