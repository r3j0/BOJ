import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    print(int(((n**4)/8) + ((3*(n**3))/4) + ((11*(n**2))/8) + ((3*n)/4)))