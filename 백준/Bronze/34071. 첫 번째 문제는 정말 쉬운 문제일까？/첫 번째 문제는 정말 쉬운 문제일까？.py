import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
if min(arr) == arr[0]: print('ez')
elif max(arr) == arr[0]: print('hard')
else: print('?')