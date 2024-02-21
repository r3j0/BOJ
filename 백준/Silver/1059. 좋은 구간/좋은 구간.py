import sys
input = sys.stdin.readline

l = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.append(0)
arr.sort()
n = int(input().rstrip())
if n in arr: print(0)
else:
    idx = 0
    while idx < l and arr[idx] < n: idx += 1
    idx -= 1

    res = 0

    if idx < l and arr[idx] < n:
        for i in range(arr[idx]+1, min(arr[idx+1], n+1)):
            for j in range(max(n, i+1), max(arr[idx+1], n+1)):
                res += 1
        idx += 1
    
    print(res)