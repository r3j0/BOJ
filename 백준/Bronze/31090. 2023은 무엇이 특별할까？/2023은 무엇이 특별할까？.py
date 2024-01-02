import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print('Good' if (n + 1) % (n % 100) == 0 else 'Bye')