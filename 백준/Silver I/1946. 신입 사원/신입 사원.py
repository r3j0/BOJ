import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0])
    res = n
    min1 = arr[0][1]
    for i in range(1, n): 
        if arr[i][1] > min1: res -= 1
        min1 = min(min1, arr[i][1])
    print(res)