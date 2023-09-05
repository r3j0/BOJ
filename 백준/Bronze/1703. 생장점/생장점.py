import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 0: break

    now = 0
    for i in range(arr[0]):
        if i == 0:
            now += arr[i*2+1]
            now -= arr[i*2+2]
        else:
            now *= arr[i*2+1]
            now -= arr[i*2+2]
    
    print(now)