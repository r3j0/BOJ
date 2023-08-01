import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    s = int(input().rstrip())
    n = int(input().rstrip())
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        s += a * b
    print(s)