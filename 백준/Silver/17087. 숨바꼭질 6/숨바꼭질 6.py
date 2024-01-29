import sys
import math
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
for i in range(n):
    arr[i] = abs(s - arr[i])

if n == 1: print(arr[0])
else:
    now = math.gcd(arr[0], arr[1])
    for i in range(2, n):
        now = math.gcd(now, arr[i])
    
    print(now)