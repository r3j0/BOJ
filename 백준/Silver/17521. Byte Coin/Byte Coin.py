import sys
input = sys.stdin.readline

n, w = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
if n == 1: print(w)
else:
    now = 1 # 1 : 올라감 -1 : 내려감
    
    now_coin = 0
    now_weight = w
    if arr[0] < arr[1]: 
        now = 1
        now_coin += now_weight // arr[0]
        now_weight %= arr[0]
    elif arr[0] > arr[1]: now = -1
    else: now = 0

    for i in range(1, n-1):
        if arr[i] < arr[i+1]: 
            if now != 1:
                now_coin += now_weight // arr[i]
                now_weight %= arr[i]
            now = 1
        elif arr[i] > arr[i+1]: 
            if now != -1:
                now_weight += now_coin * arr[i]
                now_coin = 0
            now = -1
    
    now_weight += now_coin * arr[-1]
    print(now_weight)