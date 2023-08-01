import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

def pos(n):
    y = (n-1) // 4
    x = (n-1) % 4
    return y, x

ay, ax = pos(a)
by, bx = pos(b)

print(abs(ay - by) + abs(ax - bx))