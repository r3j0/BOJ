import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    d, n, s, p = map(int, input().rstrip().split())

    if d + n * p > n * s: print('do not parallelize')
    elif d + n * p < n * s: print('parallelize')
    else: print('does not matter')