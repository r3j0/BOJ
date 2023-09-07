import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
narr = []
for i in range(n-1):
    narr.append(arr[i] - arr[i+1])

if n == 1 or max(narr) == min(narr):
    print('YES')
    print(' '.join(map(str, arr)))
    print('0 '*n)
else: print('NO')