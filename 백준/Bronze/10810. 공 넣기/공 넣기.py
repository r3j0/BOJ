import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for p in range(i-1,j):
        arr[p] = k

print(' '.join(map(str, arr)))