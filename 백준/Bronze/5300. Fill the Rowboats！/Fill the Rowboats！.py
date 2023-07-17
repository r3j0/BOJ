import sys
input = sys.stdin.readline

n = int(input())
now = 1
while now <= n:
    print(now, end=' ')
    if now % 6 == 0: print('Go!', end=' ')
    now += 1
if n % 6 != 0: print('Go!')