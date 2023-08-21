import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = input().rstrip().split()

    print('Distances: ', end='')
    for i in range(len(a)):
        print((ord(b[i]) - ord(a[i])) + (0 if ord(b[i]) - ord(a[i]) >= 0 else 26), end=' ')
    print()