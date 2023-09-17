import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    lstring = string.lower()
    gs = lstring.count('g')
    bs = lstring.count('b')

    print(string, 'is', end=' ')
    if gs == bs: print('NEUTRAL')
    elif gs > bs: print('GOOD')
    else: print('A BADDY')
