import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
if list(sorted(arr)) == arr or list(sorted(arr))[::-1] == arr: print(0)
else:
    up = [[arr[0]]]

    for i in range(1, n):
        if arr[i-1] > arr[i]: 
            up.append([])
        up[-1].append(arr[i])

    down = [[arr[0]]]

    for i in range(1, n):
        if arr[i-1] < arr[i]: 
            down.append([])
        down[-1].append(arr[i])

    """ print(up)
    print(down) """

    if len(up) == 2 and up[-1][-1] <= up[0][0]: 
        if len(down) == 2 and up[-1][-1] >= up[0][0]:
            print(min(len(up[0]), len(down[0])))
        else:
            print(len(up[0]))
    elif len(down) == 2 and up[-1][-1] >= up[0][0]: print(len(down[0]))
    else: print(-1)