import sys
input = sys.stdin.readline

s, m = map(int, input().rstrip().split())
if s <= 1023: print('No thanks')
else:
    if (s - 1023) & m == (s - 1023): print('Thanks')
    else: print('Impossible')