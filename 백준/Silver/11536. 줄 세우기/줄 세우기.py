import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [input().rstrip() for _ in range(n)]

if arr == list(sorted(arr)):
    print('INCREASING')
elif arr == list(sorted(arr))[::-1]:
    print('DECREASING')
else:
    print('NEITHER')