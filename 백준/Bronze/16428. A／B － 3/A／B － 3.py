import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

if a > 0 and b < 0:
    print(-(a//(-b)))
    print(a%(-b))
elif a < 0 and b < 0 and a%b != 0:
    print(a//b+1)
    print(a%b-b)
else:
    print(a//b)
    print(a%b)