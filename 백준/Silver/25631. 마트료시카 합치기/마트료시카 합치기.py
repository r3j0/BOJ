import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(sorted(map(int, input().rstrip().split())))
pre = arr[0]
max_cnt = 1
cnt = 1
for i in range(1, n):
    if pre == arr[i]:
        cnt += 1
    else:
        pre = arr[i]
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
