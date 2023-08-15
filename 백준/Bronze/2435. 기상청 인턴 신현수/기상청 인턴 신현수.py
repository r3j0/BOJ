import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

now = arr[:k]
max_sum = sum(now)
go = k
while go != n:
    del now[0]
    now.append(arr[go])
    max_sum = max(max_sum, sum(now))
    go += 1

print(max_sum)