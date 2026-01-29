# 1911 : 흙길 보수하기
import sys
inpuyt = sys.stdin.readline

n, l = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])

cnt = 0
start = -1
for i in range(n):
    if arr[i][0] < start: # 시작 지점을 포함하는 웅덩이
        arr[i][0] = start
    
    now_nul = (arr[i][1] - arr[i][0]) // l + (1 if (arr[i][1] - arr[i][0]) % l != 0 else 0)
    cnt += now_nul
    start = arr[i][0] + now_nul * l

print(cnt)