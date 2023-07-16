import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    arr = list(map(int, input().rstrip().split()))
    print(' '.join(map(str, arr)))
    if arr.count(18) == 1 and arr.count(17) == 1: print('both')
    elif arr.count(18) == 1: print('mack')
    elif arr.count(17) == 1: print('zack')
    else: print('none')
    print()