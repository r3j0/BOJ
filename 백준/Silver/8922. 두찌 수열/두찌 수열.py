import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    cnt = 0

    while True:
        new_arr = [abs(arr[n-1]-arr[0])]
        zero_cnt = 0
        for i in range(n-1):
            new_arr.append(abs(arr[i]-arr[i+1]))
        
        for i in range(n):
            arr[i] = new_arr[i]
            if new_arr[i] == 0: zero_cnt += 1
        
        if zero_cnt == n: break
        cnt += 1
        if cnt > 1000: break
    
    if cnt > 1000: print('LOOP')
    else: print('ZERO')