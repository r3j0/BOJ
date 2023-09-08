import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
a, b = map(int, input().rstrip().split())

for i in range(r*a):
    for j in range(c*b):
        if (j // b) % 2 == (i // a) % 2: print('X', end='')
        else: print('.', end='')
    print()