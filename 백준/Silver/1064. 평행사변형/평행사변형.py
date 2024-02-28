import sys
input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().rstrip().split())

if (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya) == 0: print(-1.0)
else:

    def Distance(ax, ay, bx, by):
        return ((((ax - bx)**2) + ((ay - by)**2))**0.5)

    result = [(Distance(xa, ya, xb, yb) + Distance(xa, ya, xc, yc))*2
            , (Distance(xb, yb, xa, ya) + Distance(xb, yb, xc, yc))*2
            , (Distance(xc, yc, xa, ya) + Distance(xc, yc, xb, yb))*2]
    print('%.10f'%(max(result) - min(result)))