import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))

    result = 0
    sums = arr[n-1]
    lens = 1
    maxs = arr[n-1]
    for a in range(n - 2, -1, -1):
        if maxs >= arr[a]:
            lens += 1
            sums += arr[a]
        else:
            if lens != 1: 
                result += (maxs * (lens - 1)) - (sums - maxs)
            
            sums = arr[a]
            lens = 1
            maxs = arr[a]

    if lens != 1: 
        result += (maxs * (lens - 1)) - (sums - maxs)
    
    print(result)