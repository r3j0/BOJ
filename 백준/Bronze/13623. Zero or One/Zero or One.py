import sys
input = sys.stdin.readline
arr = list(map(int, input().rstrip().split()))
if min(arr) != max(arr):
    if sum(arr) == 2:
        if arr[0] == 0: print('A')
        elif arr[1] == 0: print('B')
        elif arr[2] == 0: print('C')
    if sum(arr) == 1:
        if arr[0] == 1: print('A')
        elif arr[1] == 1: print('B')
        elif arr[2] == 1: print('C')
else: print('*')
