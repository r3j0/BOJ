import sys
input = sys.stdin.readline

string = input().rstrip()
now = 0
for s in string:
    if now == 0 and s == 'U': now = 1
    elif now == 1 and s == 'C': now = 2
    elif now == 2 and s == 'P': now = 3
    elif now == 3 and s == 'C': now = 4

if now == 4: print('I love UCPC')
else: print('I hate UCPC')