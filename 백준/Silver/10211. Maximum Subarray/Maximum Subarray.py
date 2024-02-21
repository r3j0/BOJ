import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    res = arr[0]
    for i in range(n):
        sums = 0
        for j in range(i, -1, -1):
            sums += arr[j]
            res = max(res, sums)
    print(res)