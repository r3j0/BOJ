import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

result = 0
#garo
for i in range(n):
    arr = []
    now_num = maps[i][0]
    now_cnt = 1
    for j in range(1, n):
        if now_num == maps[i][j]: now_cnt += 1
        else:
            arr.append([now_num, now_cnt])
            now_num = maps[i][j]
            now_cnt = 1
    
    arr.append([now_num, now_cnt])

    done = True
    #up
    for k in range(len(arr)-1):
        if arr[k][0] < arr[k+1][0]:
            if arr[k+1][0]-arr[k][0] != 1 or arr[k][1] < l:
                done = False
                break
            arr[k][1] -= l
    #down
    for k in range(len(arr)-1):
        if arr[k][0] > arr[k+1][0]:
            if arr[k][0]-arr[k+1][0] != 1 or arr[k+1][1] < l:
                done = False
                break
            arr[k+1][1] -= l
    
    if done: result += 1

#sero
for j in range(n):
    arr = []
    now_num = maps[0][j]
    now_cnt = 1
    for i in range(1, n):
        if now_num == maps[i][j]: now_cnt += 1
        else:
            arr.append([now_num, now_cnt])
            now_num = maps[i][j]
            now_cnt = 1
    
    arr.append([now_num, now_cnt])

    done = True
    #up
    for k in range(len(arr)-1):
        if arr[k][0] < arr[k+1][0]:
            if arr[k+1][0]-arr[k][0] != 1 or arr[k][1] < l:
                done = False
                break
            arr[k][1] -= l
    #down
    for k in range(len(arr)-1):
        if arr[k][0] > arr[k+1][0]:
            if arr[k][0]-arr[k+1][0] != 1 or arr[k+1][1] < l:
                done = False
                break
            arr[k+1][1] -= l
    
    if done: result += 1

print(result)