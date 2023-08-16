import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
max_now = arr[0]
cnt = 0
max_cnt = cnt
for a in range(1, n):
    if arr[a] > max_now: 
        max_now = arr[a]
        cnt = 0
    else: cnt += 1
    max_cnt = max(max_cnt, cnt)
    

print(max_cnt)