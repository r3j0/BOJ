import sys
input = sys.stdin.readline

n, p = map(int, input().rstrip().split())
now = n
arr = []
while True:
    go = (now*n)%p
    if go not in arr:
        arr.append(go)
    else:
        cnt = 0
        while arr[-1] != go:
            arr.pop()
            cnt += 1
        print(cnt + 1)
        break
    now = go