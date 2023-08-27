import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().rstrip().split()))
    if len(arr) == 1 and arr[0] == -1: break

    dic = {i:0 for i in range(1, 101)}

    for a in arr:
        dic[a] = 1
    
    cnt = 0
    for a in arr:
        if a > 1 and a % 2 == 0 and dic[a//2] == 1:
            cnt += 1

    print(cnt)