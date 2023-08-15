import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    arr = list(input().rstrip().split())
    now = float(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == '@': now *= 3
        elif arr[i] == '%': now += 5
        elif arr[i] == '#': now -= 7
    
    print('%.2f'%now)