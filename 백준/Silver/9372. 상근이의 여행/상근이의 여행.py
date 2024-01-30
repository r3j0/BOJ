import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(m)]
    print(n-1)