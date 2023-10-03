import sys
input = sys.stdin.readline

n, q = map(int, input().rstrip().split())
arr = [i for i in range(n+1)]
arr[0] = -1
for _ in range(q):
    start, interval = map(int, input().rstrip().split())
    arr[start] = 0
    now = 1
    while start + now * interval <= n:
        arr[start + now * interval] = 0
        now += 1

print(n - arr.count(0))