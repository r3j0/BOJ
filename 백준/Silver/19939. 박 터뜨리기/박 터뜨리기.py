import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
if n >= (k*(k+1)//2): 
    arr = [i for i in range(1, k+1)]
    idx = k - 1
    left = n - (k*(k+1)//2)
    while left > 0:
        arr[idx] += 1
        left -= 1
        if idx == 0: idx = k - 1
        else: idx -= 1
    
    print(arr[-1] - arr[0])
else: print(-1)