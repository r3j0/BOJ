import sys
input = sys.stdin.readline

n = int(input().rstrip())
times = [0 for _ in range(366)]
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0], -(x[1] - x[0])))
for i in range(1, 1001):
    arr_size = len(arr)
    if arr_size == 0: break
    lastarr = []
    for j in range(arr_size):
        mt = max(times[arr[j][0]:arr[j][1]+1])
        if mt != i:
            for ki in range(arr[j][0], arr[j][1]+1):
                times[ki] = mt + 1
        else: lastarr.append(arr[j])
    
    arr = []
    for l in lastarr: arr.append(l)
    

max_height = 0
start_day = 1
result = 0
for i in range(1, 366):
    if times[i] == 0:
        result += max_height * (i - start_day)
        max_height = 0
        start_day = i+1
    else:
        max_height = max(max_height, times[i])

if max_height != 0:
    result += max_height * (366 - start_day)

print(result)
