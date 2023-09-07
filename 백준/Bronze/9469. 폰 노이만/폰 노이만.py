import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n, d, a, b, f = input().rstrip().split()
    print(n, '%.6f'%((float(d)/(float(a) + float(b))) * float(f)))