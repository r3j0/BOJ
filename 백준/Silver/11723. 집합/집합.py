import sys
input = sys.stdin.readline

m = int(input().rstrip())
S = 0
for _ in range(m):
    ope = list(input().rstrip().split())
    if ope[0] == 'add': S = S | (1 << (int(ope[1]) - 1))
    elif ope[0] == 'remove': S = S & ((1 << 20) - 1 - (1 << (int(ope[1]) - 1)))
    elif ope[0] == 'check': print((S & (1 << (int(ope[1]) - 1))) >> (int(ope[1]) - 1))
    elif ope[0] == 'toggle': S = S ^ (1 << (int(ope[1]) - 1))
    elif ope[0] == 'all': S = (1 << 20) - 1
    elif ope[0] == 'empty': S = 0 