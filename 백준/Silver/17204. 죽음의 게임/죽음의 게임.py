import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
now = arr[0]
vis = [0 for _ in range(n)]
vis[0] = 1
done = -1
time = 0
while True:
    if now == k:
        done = time + 1
        break

    vis[now] = 1
    now = arr[now]
    time += 1
    if vis[now] == 1:
        break

print(done)