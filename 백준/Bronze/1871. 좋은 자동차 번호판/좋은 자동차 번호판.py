import sys
input = sys.stdin.readline

def alpha(now):
    sums = 0
    for i in range(len(now)):
        sums += (ord(now[i]) - ord('A'))*(26**(len(now) - 1 - i))
    return sums

n = int(input().rstrip())
for _ in range(n):
    l, d = input().rstrip().split('-')
    if abs(alpha(l) - int(d)) <= 100: print('nice')
    else: print('not nice')

