import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split()) 
arr = list(map(int, input().rstrip().split()))

arr.sort()
cnt = 1
now = l-1
recent = arr.pop()
while len(arr) > 0:
    go = arr.pop()
    if recent - go > now:
        cnt += 1
        now = l-1
    else:
        now -= recent - go
    recent = go

print(cnt)