import sys
from math import *
input = sys.stdin.readline

n = int(input().rstrip())

tarr = []
for _ in range(n): tarr.append(int(input().rstrip()))
arr = []
for i in range(n):
    if i == 0: continue
    arr.append(tarr[i] - tarr[i-1])

#print(arr)
now = 0
for i in range(n-1):
    if i == 0: now = arr[i]
    now = gcd(now, arr[i])

#print(now)

result = 0
for a in range(n-1):
    result += arr[a] // now - 1

print(result)