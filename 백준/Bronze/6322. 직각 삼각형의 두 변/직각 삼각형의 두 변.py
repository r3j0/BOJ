import sys
import math
input = sys.stdin.readline

t = 1
while True:
    a, b, c = map(int, input().rstrip().split())
    if a == 0 and b == 0 and c == 0: break

    print("Triangle #%d"%t)
    if a == -1:
        if c**2-b**2 <= 0:
            print("Impossible.")
        else:
            print("a = %.3f"%math.sqrt(c**2-b**2))
    elif b == -1:
        if c**2-a**2 <= 0:
            print("Impossible.")
        else:
            print("b = %.3f"%math.sqrt(c**2-a**2))
    elif c == -1:
        if a**2+b**2 <= 0:
            print("Impossible.")
        else:
            print("c = %.3f"%math.sqrt(a**2+b**2))

    t += 1
    print()