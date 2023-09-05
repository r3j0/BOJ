import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    p, m = map(int, input().rstrip().split())
    arr = [0 for _ in range(m+1)]
    cnt = 0
    for _ in range(p):
        tmp = int(input().rstrip())
        if arr[tmp] == 0:
            arr[tmp] = 1
        else:
            cnt += 1
    print(cnt)