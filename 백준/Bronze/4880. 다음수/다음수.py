import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().rstrip().split())
    if a == b == c == 0: break

    if abs(b-a) == abs(c-b): print('AP', c + (c-b))
    else: print('GP', c * (c//b))