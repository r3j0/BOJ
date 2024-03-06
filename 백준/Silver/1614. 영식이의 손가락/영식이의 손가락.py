import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
arr = [-1 for _ in range(5)]
cnt = 0
if 2 <= n <= 4:
    arr[n-1] = k % 2
    cnt = 8 * (k // 2)
else:
    arr[n-1] = 1
    cnt = 8 * (k - 1)

mode = 0
idx = 0
while arr[idx] != 0:
    if arr[idx] > 0: arr[idx] -= 1
    if mode == 0: idx += 1
    else: idx -= 1
    cnt += 1

    if idx == 4:
        mode = 1
    elif idx == 0:
        mode = 0
print(cnt)