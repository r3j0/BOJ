import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])

height_arr = [0 for _ in range(arr[-1][0]+1)]

idx = 0
now_height = 0
for i in range(arr[0][0], arr[-1][0]+1):
    if idx == 0:
        now_height = arr[0][1]
        idx += 1
    else:
        if arr[idx][0] == i:
            if now_height < arr[idx][1]:
                now_height = arr[idx][1]
            idx += 1
        
    height_arr[i] = now_height

idx = n - 1
now_height = 0
for i in range(arr[-1][0], arr[0][0]-1, -1):
    if idx == n - 1:
        now_height = arr[-1][1]
        idx -= 1
    else:
        if arr[idx][0] == i:
            if now_height < arr[idx][1]:
                now_height = arr[idx][1]
            idx -= 1

    height_arr[i] = min(height_arr[i], now_height)
""" 
for i in range(arr[-1][0]+1):
    print(height_arr[i], end=' ')
print()
 """
print(sum(height_arr))
