import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

if max(arr) != arr[0]: print('N')
else: print('S')