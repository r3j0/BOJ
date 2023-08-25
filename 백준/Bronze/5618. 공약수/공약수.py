import sys
from math import gcd
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

now = gcd(arr[0], arr[1])
if n == 3:
    now = gcd(now, arr[2])

for i in range(1, now+1):
    if now % i == 0: print(i)