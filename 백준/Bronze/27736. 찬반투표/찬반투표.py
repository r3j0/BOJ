import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
if (n % 2 == 0 and arr.count(0) >= n // 2) or (n % 2 == 1 and arr.count(0) > n // 2): print('INVALID')
else:
    if arr.count(-1) >= arr.count(1): print('REJECTED')
    else: print('APPROVED')