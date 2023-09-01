import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, c = map(int, input().rstrip().split())
    print(n//c + (1 if n % c != 0 else 0))