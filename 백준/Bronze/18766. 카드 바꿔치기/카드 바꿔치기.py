import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    a = list(input().rstrip().split())
    b = list(input().rstrip().split())
    a.sort()
    b.sort()

    if a != b: print('CHEATER')
    else: print('NOT CHEATER')