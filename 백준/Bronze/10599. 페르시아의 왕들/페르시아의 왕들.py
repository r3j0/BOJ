import sys
input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().rstrip().split())
    if a == b == c == d == 0: break
    print(c-b, d-a)