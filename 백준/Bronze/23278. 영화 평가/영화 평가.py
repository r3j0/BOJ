import sys
input = sys.stdin.readline

n, l, h = map(int, input().rstrip().split())
arr = list(sorted(map(int, input().rstrip().split())))
if h == 0: print('%.11f'%(sum(arr[l:]) / (n - (l))))
else: print('%.11f'%(sum(arr[l:-h]) / (n - (l + h))))