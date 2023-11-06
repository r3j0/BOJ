import sys
input = sys.stdin.readline

m = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

couple = [0 for _ in range(1001)]
div = []
for i in range(1, m):
    if arr[i-1] == arr[i] != 0:
        div.append(i)

if len(div) == 0:
    print(1)
    print(m)
    print(1)
else:
    if len(div) == 1:
        flag = True
        if m == 2:
            print(-1)
            flag = False
        elif arr[0] == arr[m-1] != 0:
            div.append(div[-1]+1)
        
        if flag:
            res = [div[0]]
            for i in range(1, len(div)):
                res.append(div[i] - div[i-1])
            if m > div[-1]: res.append(m - div[-1])
            print(len(res))
            print(' '.join(map(str, res)))
            print(' '.join(map(str, [i for i in range(len(div)+1, 0, -1)])))
    else:
        res = [div[0]]
        for i in range(1, len(div)):
            res.append(div[i] - div[i-1])
        if m > div[-1]: res.append(m - div[-1])
        print(len(res))
        print(' '.join(map(str, res)))
        print(' '.join(map(str, [i for i in range(len(div)+1, 0, -1)])))