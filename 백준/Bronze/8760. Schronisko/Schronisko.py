import sys
input = sys.stdin.readline

z = int(input().rstrip())
for _ in range(z):
    w, h = map(int, input().rstrip().split())
    print((w*h)//2)