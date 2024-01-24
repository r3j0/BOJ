import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    j, n = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    arr.sort(key=lambda x:(-(x[0]*x[1])))
    
    narr = []
    for a in arr:
        if len(narr) == 0:
            narr.append(a[0]*a[1])
        else:
            narr.append(narr[-1] + (a[0] * a[1]))
    
    idx = 0
    while narr[idx] < j:
        idx += 1
    print(idx+1)