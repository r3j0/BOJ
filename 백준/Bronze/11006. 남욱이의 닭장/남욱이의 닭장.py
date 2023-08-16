import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    print(m*2-n, m - (m*2-n))