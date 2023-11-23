import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    s = list(input().rstrip().split())
    for i in s:
        print(i[::-1], end=' ')
    print()