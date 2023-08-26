import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    d = int(input().rstrip())
    i = 0
    while i+i**2 <= d:
        i += 1
    i -= 1

    print(i)