import sys
input = sys.stdin.readline 

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    n = str(n + int(str(n)[::-1]))
    if n == n[::-1]: print('YES')
    else: print('NO')