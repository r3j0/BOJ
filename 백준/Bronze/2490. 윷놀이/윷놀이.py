import sys
input = sys.stdin.readline
for _ in range(3):
    arr = list(map(int, input().rstrip().split()))
    if arr.count(0) == 4: print('D')
    elif arr.count(1) == 4: print('E')
    elif arr.count(0) == 1: print('A')
    elif arr.count(0) == 2: print('B')
    else: print('C')