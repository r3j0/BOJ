import sys
input = sys.stdin.readline

while True:
    x, y = map(float, input().rstrip().split())
    if x == 0 and y == 0:
        print('AXIS')
        break
    if x == 0 or y == 0:
        print('AXIS')
    else:
        if x > 0 and y > 0: print('Q1')
        elif x < 0 and y > 0: print('Q2')
        elif x < 0 and y < 0: print('Q3')
        else: print('Q4')