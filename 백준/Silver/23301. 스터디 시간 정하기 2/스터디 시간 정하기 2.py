import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
arr = [[0 for _ in range(1001)] for _ in range(n)]
for i in range(n):
    k = int(input().rstrip())
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        for j in range(a, b):
            arr[i][j] = 1

for i in range(n):
    for j in range(1, 1001):
        arr[i][j] += arr[i][j-1]

now = 0
for i in range(n):
    now += arr[i][t-1]
max_value = now
max_time = [0, t]

for j in range(t, 1001):
    now = 0
    for i in range(n):
        now += arr[i][j]
        now -= arr[i][j-t]
    
    if max_value < now:
        max_value = now
        max_time = [j-t+1, j+1]

print(' '.join(map(str, max_time)))
