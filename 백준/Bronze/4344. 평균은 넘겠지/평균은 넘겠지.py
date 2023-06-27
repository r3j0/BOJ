import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    avg = (sum(arr) - arr[0]) / arr[0]

    cnt = 0
    for i in range(arr[0]):
        if arr[i+1] > avg:
            cnt += 1
    
    print('%.3f'%((cnt / arr[0]) * 100) + '%')