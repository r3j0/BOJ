import sys
input = sys.stdin.readline

w, h = map(int, input().rstrip().split())
p, q = map(int, input().rstrip().split())
t = int(input().rstrip())
if ((p+t) // w) % 2 == 1: print(w - ((p+t) % w), end=' ')
else: print(((p+t) % w), end=' ')
if ((q+t) // h) % 2 == 1: print(h - ((q+t) % h), end=' ')
else: print(((q+t) % h), end=' ')