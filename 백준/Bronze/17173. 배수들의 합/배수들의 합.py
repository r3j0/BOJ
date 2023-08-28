import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
k = list(map(int, input().rstrip().split()))

arr = [0 for _ in range(n+1)]

for i in k:
    now = i
    while now <= n:
        arr[now] = 1
        now += i

sums = 0
for i in range(1, n+1):
    sums += i if arr[i] == 1 else 0

print(sums)