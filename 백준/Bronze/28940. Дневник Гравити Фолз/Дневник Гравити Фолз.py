import sys
input = sys.stdin.readline

w, h = map(int, input().rstrip().split())
n, a, b = map(int, input().rstrip().split())

if w < a or h < b: print(-1)
else:
    pages = n // ((w//a) * (h//b))
    res = n % ((w//a) * (h//b))

    print(pages + (1 if res > 0 else 0))