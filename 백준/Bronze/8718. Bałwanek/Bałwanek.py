import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

if 7*k <= n: print(7000*k)
elif 3.5*k <= n: print(3500*k)
elif 1.75*k <= n: print(1750*k)
else: print(0)