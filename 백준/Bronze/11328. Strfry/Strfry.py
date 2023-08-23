import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().rstrip().split()
    if list(sorted(list(a))) == list(sorted(list(b))): print('Possible')
    else: print('Impossible')