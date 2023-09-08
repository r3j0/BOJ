import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]

arr.sort(reverse=True)

now = 0
now_idx = 0
while now < m and now_idx < n:
    now += arr[now_idx]
    now_idx += 1

print(now_idx)