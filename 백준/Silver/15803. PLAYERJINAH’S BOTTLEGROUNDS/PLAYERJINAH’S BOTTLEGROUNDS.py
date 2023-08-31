import sys
input = sys.stdin.readline

a1, b1 = map(int, input().rstrip().split())
a2, b2 = map(int, input().rstrip().split())
a3, b3 = map(int, input().rstrip().split())

if (0 if a1 - a2 == 0 or b1 - b2 == 0 else ((a1 - a2) / (b1 - b2))) == (0 if a1 - a3 == 0 or b1 - b3 == 0 else ((a1 - a3) / (b1 - b3))) == (0 if a2 - a3 == 0 or b2 - b3 == 0 else ((a2 - a3) / (b2 - b3))): print('WHERE IS MY CHICKEN?')
else: print('WINNER WINNER CHICKEN DINNER!')