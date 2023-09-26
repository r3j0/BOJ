import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    r, s = input().rstrip().split()
    for i in s: print(i*int(r), end='')
    print()