import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b, c, d, aa, bb, cc, dd = map(int, input().rstrip().split())
    a = max(1, a+aa)
    b = max(1, b+bb)
    c = max(0, c+cc)
    d = d+dd

    print(a+5*b+2*c+2*d)