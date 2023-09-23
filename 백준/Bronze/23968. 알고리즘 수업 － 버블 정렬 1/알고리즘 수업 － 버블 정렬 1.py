import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
cnt = 0
res = []
for i in range(n, 1, -1):
    for j in range(i - 1):
        if arr[j] > arr[j + 1]:
            cnt += 1

            arr[j:j + 2] = arr[j:j + 2][::-1]
            if cnt == k: res = [arr[j], arr[j+1]]

if len(res) == 0: print(-1)
else: print(' '.join(map(str, res)))