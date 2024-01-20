import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = [int(input().rstrip()) for _ in range(n)]
    if arr.count(max(arr)) > 1: print('no winner')
    elif max(arr) / sum(arr) > 0.5: print('majority winner %d'%(arr.index(max(arr))+1))
    else: print('minority winner %d'%(arr.index(max(arr))+1))