import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, c = input().rstrip().split()
    print(c*int(n))