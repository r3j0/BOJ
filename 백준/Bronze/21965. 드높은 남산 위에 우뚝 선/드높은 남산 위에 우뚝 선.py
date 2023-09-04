import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
if n == 1: print('YES')
else:
    tarr = []

    for i in range(n-1):
        tarr.append(arr[i] - arr[i+1])

    done = 0
    now = 1 if tarr[0] > 0 else -1
    cnt = 0
    for i in range(1, len(tarr)):
        if (tarr[i] > 0 and now == -1):
            now = 1 if now == -1 else -1
            cnt += 1
        elif (tarr[i] < 0 and now == 1):
            done = 1
            break 
        elif tarr[i] == 0:
            done = 1
            break

    if cnt >= 2: done = 1

    print('YES' if done == 0 else 'NO')