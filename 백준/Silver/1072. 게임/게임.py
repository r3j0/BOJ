import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())
res = (y*100)//x + 1
start = y + 1
end = 100000000000
while start < end:
    mid = (start + end) // 2
    go = (mid * 100) // (x + (mid - y))
    if go >= res:
        end = mid
    else:
        start = mid + 1

if res <= (start * 100) // (x + (start - y)):
    print(start - y)
else:
    print(-1)