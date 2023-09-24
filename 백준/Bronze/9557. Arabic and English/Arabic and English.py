import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(input().rstrip().split())

    res = []
    idx = n - 1
    go = 0
    while idx >= 0:
        res.append(arr[idx])
        if arr[idx].count('#') == 0:
            go = 1
            break
        idx -= 1
        
    if go == 1:
        if len(res) != 1:
            print(' '.join(list(reversed(res))[1:]), end=' ')
            print(res[-1], end=' ')
        else: print(res[0], end=' ')
        res = []
        idx = 0
        while idx < n:
            if arr[idx].count('#') == 0: break
            res.append(arr[idx])
            idx += 1
        print(' '.join(res))
    else:
        print(' '.join(reversed(res)))
    