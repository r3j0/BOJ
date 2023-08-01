import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [[0, 0] for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().rstrip().split())
    arr[y-1][s] += 1

res = 0
for i in range(6):
    for j in range(2):
        if arr[i][j] == 0: continue
        if arr[i][j] <= k:
            res += 1
        else:
            res += arr[i][j] // k + (1 if arr[i][j] % k != 0 else 0)

print(res)