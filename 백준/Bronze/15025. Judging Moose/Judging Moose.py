import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

if a == b == 0: print('Not a moose')
else:
    if a!=b: print('Odd', end=' ')
    else: print('Even', end=' ')

    print(max(a,b)*2)