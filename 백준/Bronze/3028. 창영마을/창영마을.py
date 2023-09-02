import sys
input = sys.stdin.readline

string = input().rstrip()
a, b, c = 1, 0, 0
for s in string:
    if s == 'A': a, b = b, a
    elif s == 'B': b, c = c, b
    else: a, c = c, a
if a == 1: print(1)
elif b == 1: print(2)
else: print(3)