import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [i for i in range(1, n+1)]

for _ in range(m):
    start, end = map(int, input().rstrip().split())
    arr[start-1:end] = arr[start-1:end][::-1]

print(' '.join(map(str, arr)))