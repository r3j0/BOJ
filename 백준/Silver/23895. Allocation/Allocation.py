import sys
input = sys.stdin.readline

test = int(input())
for t in range(test):
    a, b = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    res = 0
    cnt = 0
    for a in arr:
        if res + a <= b:
            res += a
            cnt += 1
    
    print('Case #%d: %d'%(t+1, cnt))